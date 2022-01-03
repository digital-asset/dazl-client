# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Simple command-line handlers.
"""

import logging
from typing import List, Sequence

from .._logging import configure as configure_logger
from ..client.errors import ConfigurationError
from ._base import CliCommand
from .ls import ListAllCommand
from .metadata import PrintMetadataCommand
from .tail import TailCommand
from .upload import UploadCommand
from .version import VersionCommand

COMMANDS = [
    ListAllCommand(),
    PrintMetadataCommand(),
    TailCommand(),
    UploadCommand(),
    VersionCommand(),
]  # type: List[CliCommand]


def main():
    """
    Executes one of the known commands.
    """
    from sys import argv, exit

    exit(_main(argv))


def _main(argv: "Sequence[str]") -> int:
    if len(argv) > 1:
        command = argv[1]
        command_args = argv[2:]

        for cmd in COMMANDS:
            if cmd.name == command:
                try:
                    return run(cmd, command_args)
                except ConfigurationError as error:
                    for reason in error.reasons:
                        print(reason)
                    return -1

        print("Unknown command: " + command)

    print_cmd_help()
    return -2


def run(cmd, args) -> int:
    parser = cmd.parser()
    parsed_args = parser.parse_args(args)

    log_level = getattr(parsed_args, "log_level", logging.WARNING)
    if log_level is None:
        log_level = logging.WARNING

    configure_logger(level=log_level)
    return cmd.execute(parsed_args)


def print_cmd_help():
    print("Valid commands:")
    for cmd in COMMANDS:
        if not cmd.hidden:
            print(cmd.name)
