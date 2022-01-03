# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This model contains definitions for the data classes used at the client layer of this library.
"""

from enum import IntEnum
import sys
from typing import NamedTuple, Optional

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = [
    "ExitCode",
    "LedgerRun",
    "CREATE_IF_MISSING",
    "NONE_IF_MISSING",
    "EXCEPTION_IF_MISSING",
    "IfMissingPartyBehavior",
]


class ExitCode(IntEnum):
    """
    The different ways that a run of a dazl script can terminate.
    """

    SUCCESS = 0
    ABORT = 1
    ERROR = 2
    ERROR_INIT = 3


class LedgerRun(NamedTuple):
    """
    The results of a run of the ledger.

    Instance attributes:

    .. attribute:: LedgerRun.exit_code

        The exit code.

    .. attribute:: LedgerRun.block_start_height

        The block height of the first block consumed by the run.

    .. attribute:: LedgerRun.block_end_height

        The block height of the first block NOT consumed by the run.
    """

    exit_code: ExitCode
    block_start_height: Optional[int]
    block_end_height: Optional[int]


CREATE_IF_MISSING: Literal[1] = 1
NONE_IF_MISSING: Literal[2] = 2
EXCEPTION_IF_MISSING: Literal[3] = 3

IfMissingPartyBehavior = Literal[1, 2, 3]
