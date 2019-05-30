# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import get_event_loop
from argparse import ArgumentParser

from .. import sandbox
from ..util.dar import DamlcPackageError
from ._base import CliCommand


class SandboxCommand(CliCommand):
    name = 'sandbox'
    hidden = True

    def parser(self):
        arg_parser = ArgumentParser('dazl sandbox')
        arg_parser.add_argument(
            'file', metavar='FILE', help='A .daml file to compile into a package, or a .dar file')
        arg_parser.add_argument(
            '--port', metavar='PORT', default=7600, type=int)
        arg_parser.add_argument(
            '--log-level')
        return arg_parser

    def execute(self, args):
        try:
            with sandbox(args.file, args.port):
                get_event_loop().run_forever()
        except DamlcPackageError as ex:
            return ex.exit_code
