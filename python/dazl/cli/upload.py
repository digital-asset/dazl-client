# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence
from .. import Network
from ._base import CliCommand
from ..client.config import configure_parser, AnonymousNetworkConfig


class UploadCommand(CliCommand):
    name = 'upload'

    def parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser('dazl upload')

        configure_parser(arg_parser, config_file_support=True)
        arg_parser.add_argument(
            'files', metavar='FILE', nargs='+', help='DAR files to upload to the remote DAML ledger')

        return arg_parser

    def execute(self, args) -> int:
        final_config = AnonymousNetworkConfig.get_config(args)

        contents = [Path(file).read_bytes() for file in args.files]

        network = Network()
        network.set_config(final_config)
        network.run_until_complete(upload_dars(network, contents))
        return 0


async def upload_dars(network, contents: Sequence[bytes]):
    for dar in contents:
        await network.aio_global().ensure_dar(dar)
