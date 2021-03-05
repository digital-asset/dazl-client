# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Core types
----------

The :mod:`dazl.model.core` module contains classes used on both the read-side and the write-side of
the Ledger API.
"""
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import BinaryIO, Callable, Dict, Optional, Tuple, TypeVar, Union
import warnings

from ..prim import ContractData, ContractId, DazlError, DazlWarning, Party

T = TypeVar("T")


__all__ = [
    "ContractMatch",
    "ContractsState",
    "ContractsHistoricalState",
    "ContractContextualDataCollection",
    "ContractContextualData",
    "DazlError",
    "DazlWarning",
]


ContractMatch = Union[None, Callable[[ContractData], bool], ContractData]
ContractsState = Dict[ContractId, ContractData]
ContractsHistoricalState = Dict[ContractId, Tuple[ContractData, bool]]


class ContractContextualDataCollection(tuple):
    def __getitem__(self, index: Union[int, str, ContractId]):
        if index is None:
            raise ValueError("the index cannot be None")
        elif isinstance(index, int):
            return tuple.__getitem__(self, index)
        elif isinstance(index, str):
            for cxd in self:
                if cxd.cid.contract_id == index:
                    return cxd
            raise KeyError(index)
        elif isinstance(index, ContractId):
            for cxd in self:
                if cxd.cid == index:
                    return cxd
            raise KeyError(index)
        else:
            raise TypeError("cannot index into a ContractContextualDataCollection with {index!r}")


@dataclass(frozen=True)
class ContractContextualData:
    cid: "ContractId"
    cdata: "Optional[ContractData]"
    effective_at: datetime
    archived_at: "Optional[datetime]"
    active: bool


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
