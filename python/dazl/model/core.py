# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Core types
----------

The :mod:`dazl.model.core` module contains classes used on both the read-side and the write-side of
the Ledger API.
"""
from pathlib import Path
from typing import BinaryIO, TypeVar, Union
import warnings

from ..prim import ContractData, ContractId, DazlError, DazlWarning, Party
from ..query import ContractMatch

T = TypeVar("T")


__all__ = [
    "ContractId",
    "ContractData",
    "ContractMatch",
    "DazlError",
    "DazlWarning",
    "Party",
]


# TODO: Import dazl.client.state types here when the circular references between the broader
#  dazl.client and dazl.model packages are resolved:
#       * ContractsState
#       * ContractsHistoricalState
#       * ContractContextualData
#       * ContractContextualDataCollection


# Wherever the API expects a DAR, we can take a file path, `bytes`, or a byte buffer.
Dar = Union[bytes, str, Path, BinaryIO]


# TODO: Import dazl.client.errors types here when the circular references between the broader
#  dazl.client and dazl.model packages are resolved:
#       * ConfigurationError
#       * DazlPartyMissingError
#       * UnknownTemplateWarning


# TODO: Import dazl.protocol.errors types here when the circular references between the broader
#  dazl.protocol and dazl.model packages are resolved:
#       * ConnectionTimeoutError
#       * UserTerminateRequest


# TODO: Import dazl.util.proc_util error types here when the circular references between the broader
#  dazl.util and dazl.model packages are resolved:
#       * ProcessDiedException


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
