# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module prints the metadata obtained from a remote server.
"""

from argparse import ArgumentParser
from typing import Collection

from ._base import CliCommand
from .. import LOG, Network
from ..client.config import configure_parser, AnonymousNetworkConfig
from ..model.core import UserTerminateRequest, ConnectionTimeoutError
from ..model.types_store import PackageStore
from ..util.dar import DamlcPackageError
from ..util.dar_repo import LocalDarRepository
from ..pretty import get_pretty_printer, PrettyOptions


class PrintMetadataCommand(CliCommand):
    name = 'metadata'

    def parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser()

        configure_parser(arg_parser, parties=False)
        arg_parser.add_argument('--file', help='path to a DAML or DAR file', action='append')
        arg_parser.add_argument('--show-hidden', help='show hidden types', action='store_true')
        arg_parser.add_argument('--format', help='one of \"daml\" or \"python\"', default='daml')
        return arg_parser

    def execute(self, args) -> int:
        LOG.debug('Executing a metadata fetch...')

        options = PrettyOptions(
            column_width=80,
            show_hidden_types=args.show_hidden,
            format=args.format)

        if args.file:
            return self.execute_static_metadata(args.file, options)

        config = AnonymousNetworkConfig.get_config(args)

        return self.execute_runtime_metadata(config, options)

    @staticmethod
    def execute_static_metadata(files: Collection[str], options: PrettyOptions) -> int:
        repo = LocalDarRepository()
        try:
            repo.add_source(*files)
            _process_metadata(repo.store, options)
            return 0

        except DamlcPackageError as ex:
            return ex.exit_code

    @staticmethod
    def execute_runtime_metadata(config: 'AnonymousNetworkConfig', options: PrettyOptions) -> int:
        try:
            network = Network()
            network.set_config(config)
            network.run_until_complete(_main(network, options))
            return 0
        except UserTerminateRequest:
            return 1
        except ConnectionTimeoutError as ex:
            print(str(ex))
            return 1


async def _main(network: Network, options):
    metadata = await network.aio_global().metadata()
    _process_metadata(metadata.store, options)


def _process_metadata(store: PackageStore, options: PrettyOptions):
    import sys
    if sys.stdout.isatty():
        try:
            import pygments
            from pygments.formatters.terminal256 import Terminal256Formatter
            formatter = Terminal256Formatter()
        except ImportError:
            pygments = None
            formatter = None
    else:
        pygments = None
        formatter = None

    pretty_printer = get_pretty_printer(options.format, options, store)
    code = pretty_printer.render_store()
    lexer = pretty_printer.lexer()

    if pygments is not None and lexer is not None and formatter is not None:
        print(pygments.highlight(code, lexer, formatter))
    else:
        print(code)

