# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Simple methods for instantiating an application written against dazl that incorporate common usage
patterns.
"""

import logging
from argparse import ArgumentParser
from typing import Callable

from ..util.logging import setup_default_logger
from ..client.api import Network
from ..client.config import configure_parser, NetworkConfig


def run(init: 'Callable[[Network], None]'):
    if init is None:
        raise ValueError('The init callback cannot be None')
    setup_default_logger(logging.INFO)
    arg_parser = ArgumentParser()

    configure_parser(arg_parser, config_file_support=True)
    args = arg_parser.parse_args()

    print(args)
    config = NetworkConfig.get_config(args)
    network = Network()
    network.set_config(config)

    init(network)

    network.run_forever()
