# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module has been relocated to ``dazl.client``, ``dazl.damlast``, ``dazl.protocols``, or
``dazl.query``.
"""
from typing import TypeVar
import warnings

from ..client.errors import ConfigurationError, DazlPartyMissingError, UnknownTemplateWarning
from ..client.state import (
    ContractContextualData,
    ContractContextualDataCollection,
    ContractsHistoricalState,
    ContractsState,
)
from ..damlast.pkgfile import Dar
from ..prim import ContractData, ContractId, DazlError, DazlWarning, Party
from ..prim.errors import DazlImportError
from ..protocols.errors import ConnectionTimeoutError, UserTerminateRequest
from ..query import ContractMatch
from ..util.proc_util import ProcessDiedException

T = TypeVar("T")


__all__ = [
    "ConfigurationError",
    "ConnectionTimeoutError",
    "ContractContextualData",
    "ContractContextualDataCollection",
    "ContractData",
    "ContractId",
    "ContractMatch",
    "ContractsHistoricalState",
    "ContractsState",
    "Dar",
    "DazlError",
    "DazlImportError",
    "DazlPartyMissingError",
    "DazlWarning",
    "Party",
    "ProcessDiedException",
    "UnknownTemplateWarning",
    "UserTerminateRequest",
]


class CommandTimeoutError(DazlError):
    """
    Raised when a corresponding event for a command was not seen in the appropriate time window.
    """

    def __init__(self):
        warnings.warn(
            "This error is never raised; this symbol will be removed in dazl v9",
            DeprecationWarning,
            stacklevel=2,
        )


class ConnectionClosedError(DazlError):
    """
    Raised when trying to do something that requires a connection after connection pools have been
    closed.
    """

    def __init__(self):
        warnings.warn(
            "This error is never raised; this symbol will be removed in dazl v9",
            DeprecationWarning,
            stacklevel=2,
        )
