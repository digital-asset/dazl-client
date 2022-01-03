# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from argparse import ArgumentParser

from .. import LOG, Network
from ..client.config import NetworkConfig, configure_parser
from ..pretty.table import DEFAULT_FORMATTER_NAME, write_acs
from ._base import CliCommand


class ListAllCommand(CliCommand):
    name = "ls"

    def parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser("dazl ls")

        configure_parser(arg_parser, config_file_support=True)
        arg_parser.add_argument("--format", "--fmt", "-F", type=str, default=DEFAULT_FORMATTER_NAME)
        arg_parser.add_argument("--template-filter", "-T", type=str)
        arg_parser.add_argument("--all", "-A", action="store_true")
        return arg_parser

    def execute(self, args) -> int:
        fmt = args.format
        template_filter = (
            [template.strip() for template in args.template_filter.split(",")]
            if args.template_filter is not None
            else None
        )
        include_archived = bool(args.all)
        LOG.debug("Executing an ls...")

        final_config = NetworkConfig.get_config(args)

        network = Network()
        network.set_config(final_config)
        network.set_config(eager_package_fetch=False)
        if include_archived:
            network.set_config(use_acs_service=False)

        for party in args.parties:
            network.aio_party(party)

        network.run_until_complete(self._main(network, fmt, include_archived))
        return 0

    async def _main(self, network: "Network", fmt: str, include_archived: bool):
        import sys

        LOG.debug("Starting our parties...")
        for party in network.parties():
            await network.aio_party(party).ready()
            LOG.debug("Party %s is ready.", party)
        metadata = await network.aio_global().metadata()
        LOG.debug("Our parties are now ready.")

        write_acs(sys.stdout, network, fmt=fmt, include_archived=include_archived)
