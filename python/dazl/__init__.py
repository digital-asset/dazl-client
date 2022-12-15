# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the Python API for interacting with the Ledger API.
"""

__all__ = [
    "AIOPartyClient",
    "Command",
    "connect",
    "ContractData",
    "ContractId",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "DazlError",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "LOG",
    "Network",
    "Party",
    "SimplePartyClient",
    "__version__",
    "async_network",
    "create",
    "create_and_exercise",
    "exercise",
    "exercise_by_key",
    "frozendict",
    "run",
    "setup_default_logger",
    "simple_client",
    "write_acs",
]

from ._logging import LOG
from .client import AIOPartyClient, Network, SimplePartyClient, async_network, run, simple_client
from .client.commands import (
    CreateAndExerciseCommand,
    CreateCommand,
    ExerciseByKeyCommand,
    ExerciseCommand,
    create,
    create_and_exercise,
    exercise,
    exercise_by_key,
)
from .ledger import Command, connect
from .model.core import ContractId
from .pretty.table import write_acs
from .prim import ContractData, DazlError, FrozenDict as frozendict, Party
from .util.logging import setup_default_logger

# Large Protobuf message support

# These methods are undocumented, but is required to read even moderately sized DALF's.
try:
    # For Protobuf libraries version 4 or later (using upb)
    # noinspection PyPackageRequirements,PyUnresolvedReferences,PyProtectedMember
    from google._upb._message import SetAllowOversizeProtos

    SetAllowOversizeProtos(True)
except ImportError:
    pass

try:
    # For Protobuf libraries version 3 or earlier (using upb)
    # noinspection PyPackageRequirements,PyUnresolvedReferences,PyProtectedMember
    from google.protobuf.pyext import _message

    _message.SetAllowOversizeProtos(True)
except ImportError:
    pass


__version__ = "7.10.2"
