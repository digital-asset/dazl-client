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

try:
    # This method is undocumented, but is required to read large size of model files when using
    # the C++ implementation.
    # noinspection PyPackageRequirements,PyUnresolvedReferences,PyProtectedMember
    from google.protobuf.pyext import _message

    _message.SetAllowOversizeProtos(True)

except ImportError:
    # ImportError for the Protobuf libraries is likely fatal, but this would not be the most helpful
    # place to throw an ImportError.
    pass


__version__ = "7.8.4"
