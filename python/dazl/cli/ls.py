# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from asyncio import gather
from argparse import ArgumentParser
from .. import LOG, Network, write_acs
from ._base import CliCommand
from ..plugins import LedgerCapturePlugin
from ..client.config import configure_parser, NetworkConfig


class ListAllCommand(CliCommand):
    name = 'ls'

    def parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser('dazl ls')

        configure_parser(arg_parser, config_file_support=True)
        arg_parser.add_argument('--format', '--fmt', '-F', type=str, default=LedgerCapturePlugin.DEFAULT_FORMATTER_NAME)
        arg_parser.add_argument('--template-filter', '-T', type=str)
        arg_parser.add_argument('--all', '-A', action='store_true')
        return arg_parser

    def execute(self, args) -> int:
        fmt = args.format
        template_filter = [template.strip() for template in args.template_filter.split(',')] \
            if args.template_filter is not None else None
        include_archived = bool(args.all)
        LOG.debug('Executing an ls...')

        final_config = NetworkConfig.get_config(args)

        network = Network()
        network.set_config(final_config)

        global_ready = gather(*[network.aio_party(party).ready() for party in args.parties])
        network.run_until_complete(self._main(network, global_ready, fmt, include_archived))
        return 0

    async def _main(self, network, global_ready, fmt, include_archived):
        import sys
        await global_ready

        write_acs(sys.stdout, network, fmt=fmt, include_archived=include_archived)
        network.shutdown()
