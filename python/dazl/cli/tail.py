# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser
from asyncio import ensure_future, get_event_loop
import datetime
import json
import logging
from typing import Optional

from .. import LOG, Network
from ..client.config import NetworkConfig, configure_parser
from ..damlast.daml_types import con
from ..prim import Party
from ..values import Context, JsonDecoder
from ._base import CliCommand

__all__ = ["TailCommand"]


def elide_at(s: str, limit: "Optional[int]") -> str:
    if limit and len(s) > limit:
        return s[:limit] + "..."
    return s


def pprint_cdata(event, args):
    def default(o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()

    format_args = {} if args.one_line else {"indent": 4}

    ctx = Context(JsonDecoder(), event.lookup)
    cdata = ctx.convert(con(event.cid.value_type), event.cdata)

    return elide_at(
        json.dumps(cdata, default=default, sort_keys=True, **format_args),
        None if args.details else 1024,
    )


def pprint_cid(event, args):
    tid = str(event.cid.value_type)

    delim_pos = tid.find(":")

    cid = elide_at(event.cid.value, None if args.details else 10)

    return f"{tid[delim_pos + 1:]}({cid})"


class TailCommand(CliCommand):
    name = "tail"

    def parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser("dazl tail")

        configure_parser(arg_parser, config_file_support=True)
        arg_parser.add_argument(
            "--details",
            help="Ensure all output is printed with all details.",
            dest="details",
            action="store_true",
            default=False,
        )
        arg_parser.add_argument(
            "--one-line",
            help="Ensure all events are written as a single line",
            dest="one_line",
            action="store_true",
            default=False,
        )

        return arg_parser

    def execute(self, args) -> int:
        LOG.debug("Executing a tail...")

        loop = get_event_loop()
        loop.run_until_complete(self._main(args))

        return 0

    def setup_monitor_stream(self, network: "Network", party: "Party", args):
        party_client = network.aio_party(party)

        PLOG = logging.getLogger(f"tail-{party}")
        PLOG.setLevel(logging.INFO)

        @party_client.ledger_ready()
        async def on_ledger_ready(event):
            PLOG.info("...party log stream ready")

        @party_client.ledger_created("*")
        async def on_contract_create(event):
            PLOG.info(f"Create - {pprint_cid(event, args)} {pprint_cdata(event, args)}")

        @party_client.ledger_archived("*")
        async def on_contract_archived(event):
            PLOG.info(f"Archive - {pprint_cid(event, args)}")

    async def _main(self, args):
        final_config = NetworkConfig.get_config(args)

        network = Network()
        network.set_config(final_config)
        network.set_config(eager_package_fetch=False)

        for party in args.parties:
            self.setup_monitor_stream(network, party, args)

        await ensure_future(network.aio_run())
