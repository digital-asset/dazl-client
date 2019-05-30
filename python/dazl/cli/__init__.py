# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Simple command-line handlers.
"""

import logging
import sys
from typing import List

from .. import setup_default_logger
from ..model.core import ConfigurationError
from ._base import CliCommand
from .fetch import FetchComponentCommand
from .ls import ListAllCommand
from .metadata import PrintMetadataCommand
from .package import PackageDarCommand
from .sandbox import SandboxCommand
from .tail import TailCommand
from .version import VersionCommand

COMMANDS = [
    FetchComponentCommand(),
    ListAllCommand(),
    PrintMetadataCommand(),
    PackageDarCommand(),
    SandboxCommand(),
    TailCommand(),
    VersionCommand(),
]  # type: List[CliCommand]


def main():
    """
    Executes one of the known commands.
    """
    if len(sys.argv) > 1:
        command = sys.argv[1]
        command_args = sys.argv[2:]

        for cmd in COMMANDS:
            if cmd.name == command:
                try:
                    sys.exit(run(cmd, command_args))
                except ConfigurationError as error:
                    for reason in error.reasons:
                        print(reason)
                    sys.exit(-1)

        print("Unknown command: " + command)

    print_cmd_help()


def run(cmd, args) -> int:
    parser = cmd.parser()
    parsed_args = parser.parse_args(args)

    log_level = getattr(parsed_args, 'log_level', logging.WARNING)
    if log_level is None:
        log_level = logging.WARNING

    setup_default_logger(level=log_level)
    return cmd.execute(parsed_args)


def print_cmd_help():
    print("Valid commands:")
    for cmd in COMMANDS:
        if not cmd.hidden:
            print(cmd.name)
