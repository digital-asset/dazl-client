# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Simple methods for instantiating an application written against dazl that incorporate common usage
patterns.
"""
from argparse import ArgumentParser
from typing import Callable
import warnings

from ..client.api import Network
from ..client.config import NetworkConfig, configure_parser


def run(init: "Callable[[Network], None]"):
    warnings.warn("dazl.run is deprecated", DeprecationWarning, stacklevel=2)

    if init is None:
        raise ValueError("The init callback cannot be None")

    arg_parser = ArgumentParser()

    configure_parser(arg_parser, config_file_support=True)
    args = arg_parser.parse_args()

    config = NetworkConfig.get_config(args)
    network = Network()
    network.set_config(config)

    init(network)

    network.run_forever()
