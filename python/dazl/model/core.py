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
from typing import BinaryIO, Callable, Collection, Dict, Optional, Tuple, TypeVar, Union

from ..prim import ContractData, ContractId, Party

T = TypeVar("T")


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


class DazlError(Exception):
    """
    Superclass of errors raised by dazl.
    """


class DazlWarning(Warning):
    """
    Superclass of warnings raised by dazl.
    """


class DazlPartyMissingError(DazlError):
    """
    Error raised when a party or some information about a party is requested, and that party is not
    found.
    """

    def __init__(self, party: Party):
        super().__init__(f"party {party!r} does not have a defined client")
        self.party = party


class DazlImportError(ImportError, DazlError):
    """
    Import error raised when an optional dependency could not be found.
    """

    def __init__(self, missing_module, message):
        super().__init__(message)
        self.missing_module = missing_module


class UserTerminateRequest(DazlError):
    """
    Raised when the user has initiated a request to terminate the application.
    """


class ConnectionTimeoutError(DazlError):
    """
    Raised when a connection failed to be established before the connection timeout elapsed.
    """


class CommandTimeoutError(DazlError):
    """
    Raised when a corresponding event for a command was not seen in the appropriate time window.
    """


class ConfigurationError(DazlError):
    """
    Raised when a configuration error prevents a client from being started.

    .. attribute:: ConfigurationError.reasons

        A collection of reasons for a failure.
    """

    def __init__(self, reasons: "Union[str, Collection[str]]"):
        if reasons is None:
            self.reasons = []  # type: Collection[str]
        elif isinstance(reasons, str):
            self.reasons = [reasons]
        else:
            self.reasons = reasons  # type: Collection[str]


class ConnectionClosedError(DazlError):
    """
    Raised when trying to do something that requires a connection after connection pools have been
    closed.
    """


class UnknownTemplateWarning(DazlWarning):
    """
    Raised when trying to do something with a template name that is unknown.
    """


class ProcessDiedException(DazlError):
    pass
