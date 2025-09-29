# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Simple command-line handlers.
"""

from __future__ import annotations

import logging
from typing import NoReturn, Sequence

from .._logging import configure as configure_logger
from ._base import CliCommand
from .version import VersionCommand

COMMANDS = list[CliCommand]((VersionCommand(),))


def main() -> NoReturn:
    """
    Executes one of the known commands.
    """
    from sys import argv, exit

    exit(_main(argv))


def _main(argv: Sequence[str]) -> int:
    if len(argv) > 1:
        command = argv[1]
        command_args = argv[2:]

        for cmd in COMMANDS:
            if cmd.name == command:
                return run(cmd, command_args)

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


def print_cmd_help() -> None:
    print("Valid commands:")
    for cmd in COMMANDS:
        if not cmd.hidden:
            print(cmd.name)
