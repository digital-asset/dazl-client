# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains helper methods for detecting terminal capabilities.
"""

from subprocess import DEVNULL, PIPE, Popen
from typing import Optional, Tuple


def termsize() -> "Tuple[Optional[int], Optional[int]]":
    """
    Return the current size of the terminal. If the current terminal is not a tty, then
    ``(None, None)`` is returned.
    """
    try:
        with Popen(["stty", "size"], stdout=PIPE, stderr=DEVNULL) as proc:
            term_size_str = proc.stdout.read().decode("utf8") if proc.stdout is not None else None
    except FileNotFoundError:
        term_size_str = None
    if term_size_str is not None:
        dimensions = term_size_str.split()
        if len(dimensions) >= 2:
            return int(dimensions[0]), int(dimensions[1])
        else:
            return None, None
    else:
        return None, None


def print_termcap() -> None:
    """
    Output discovered settings to the terminal.
    """
    rows, cols = termsize()
    if rows is not None and cols is not None:
        print("The terminal size is:")
        print(termsize())
    else:
        print("Not a terminal.")


if __name__ == "__main__":
    print_termcap()
