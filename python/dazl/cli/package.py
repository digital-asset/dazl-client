# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser
from pathlib import Path

from ._base import CliCommand


class PackageDarCommand(CliCommand):
    name = 'package'
    hidden = True

    def parser(self):
        arg_parser = ArgumentParser('dazl package')
        arg_parser.add_argument(
            'file', metavar='DAML_FILE', help='A .daml file to compile into a package')
        arg_parser.add_argument(
            '--out', '-o', metavar='DAR_FILE', default=None)
        arg_parser.add_argument(
            '--log-level')
        return arg_parser

    def execute(self, args):
        from ..util.dar import build_dar, DamlcPackageError

        root_daml_file = Path(args.file)
        output_dar_file = args.out or root_daml_file.with_suffix('.dar')
        try:
            build_dar(str(root_daml_file), str(output_dar_file))
            return 0
        except DamlcPackageError as ex:
            return ex.exit_code
