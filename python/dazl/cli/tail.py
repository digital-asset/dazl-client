# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser

from .. import LOG
from ._base import CliCommand
from ..plugins import LedgerCapturePlugin
from ..client import Network
from ..client.config import configure_parser, NetworkConfig


class TailCommand(CliCommand):
    name = 'tail'

    def parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser('dazl tail')

        configure_parser(arg_parser)
        arg_parser.add_argument('--config', help='path to a YAML config file')
        arg_parser.add_argument('--format', '--fmt', '-F', type=str,
                                default=LedgerCapturePlugin.DEFAULT_FORMATTER_NAME)
        return arg_parser

    def execute(self, args) -> None:
        LOG.debug('Executing a tail...')

        config = NetworkConfig.get_config(args)
        network = Network()
        network.set_config(config)
        network.run_forever()
