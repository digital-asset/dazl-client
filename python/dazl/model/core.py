# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Core types
----------

The :mod:`dazl.model.core` module contains classes used on both the read-side and the write-side of
the Ledger API.

.. autoclass:: ContractId
   :members:
"""
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Collection, Dict, Optional, Tuple, TypeVar, Union
import warnings

from ..damlast.daml_lf_1 import TypeConName
from ..damlast.pkgfile import Dar
from ..prim import ContractData, ContractId as ContractId_, Party
from ..query import ContractMatch

if TYPE_CHECKING:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from .types import Type, TypeReference

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

T = TypeVar("T")


class ContractId(ContractId_):
    __slots__ = ("_value_type_deprecated",)
    _value_type_deprecated: "TypeReference"

    def __init__(self, contract_id: str, template_id: "Union[str, Type, TypeConName]"):
        warnings.warn(
            "dazl.model.core.ContractId is deprecated; use dazl.prim.ContractId instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        from ..damlast.compat import parse_template

        if not isinstance(contract_id, str):
            raise ValueError("contract_id must be a string")

        value = contract_id
        value_type, value_type_deprecated = parse_template(template_id)

        super().__init__(value_type, value)
        object.__setattr__(self, "_value_type_deprecated", value_type_deprecated)

    @property
    def contract_id(self) -> str:
        """
        Get the raw contract ID value (for example, ``"#4:1"``).
        """
        warnings.warn(
            "ContractId.contract_id is deprecated; use ContractId.value instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.value

    @property
    def template_id(self) -> "TypeReference":
        """
        Get the type of template that is pointed to by this :class:`ContractId` as a
        :class:`TypeReference`. Note that usage of :class:`Type` and :class:`TypeReference` are
        deprecated, and :meth:`value_type` should be used instead.

        As of dazl 7.3.0, the :class:`TemplateId` is always normalized to a :class:`TypeReference`,
        regardless of what the :class:`ContractId` was constructed with.
        """
        warnings.warn(
            "ContractId.template_id is deprecated; use ContractId.value_type instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._value_type_deprecated

    def exercise(self, choice_name, arguments=None):
        """
        Create an :class:`ExerciseCommand` that represents the result of exercising a choice on this
        contract with the specified choice.

        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            (optional) A ``dict`` of named values to send as parameters to the choice exercise.
        """
        from .writing import ExerciseCommand

        return ExerciseCommand(self, choice_name, arguments=arguments)

    def replace(self, contract_id=None, template_id=None):
        """
        Return a new :class:`ContractId` instance replacing specified fields with values.
        """
        warnings.warn(
            "ContractId.replace is deprecated; simply construct a ContractId with the desired "
            "values instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return ContractId(
                contract_id if contract_id is not None else self.value,
                template_id if template_id is not None else self.value_type,
            )

    def for_json(self):
        """
        Return the JSON representation of this contract. This is currently just the contract ID
        string itself.
        """
        return self.value


ContractsState = Dict[ContractId, ContractData]
ContractsHistoricalState = Dict[ContractId, Tuple[ContractData, bool]]


class ContractContextualDataCollection(tuple):
    def __getitem__(self, index):
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
    cid: ContractId
    cdata: "Optional[ContractData]"
    effective_at: "Optional[datetime]"
    archived_at: "Optional[datetime]"
    active: bool


@dataclass(frozen=True)
class SourceLocation:
    file_name: "Optional[str]"
    start_line: int
    end_line: int


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

    def __init__(self):
        warnings.warn(
            "This error is never raised; this symbol will be removed in dazl v8",
            DeprecationWarning,
            stacklevel=2,
        )


class ConfigurationError(DazlError):
    """
    Raised when a configuration error prevents a client from being started.

    .. attribute:: ConfigurationError.reasons

        A collection of reasons for a failure.
    """

    reasons: Collection[str]

    def __init__(self, reasons: "Union[str, Collection[str]]"):
        if reasons is None:
            self.reasons = []
        elif isinstance(reasons, str):
            self.reasons = [reasons]
        else:
            self.reasons = reasons


class ConnectionClosedError(DazlError):
    """
    Raised when trying to do something that requires a connection after connection pools have been
    closed.
    """

    def __init__(self):
        warnings.warn(
            "This error is never raised; this symbol will be removed in dazl v8",
            DeprecationWarning,
            stacklevel=2,
        )


class UnknownTemplateWarning(DazlWarning):
    """
    Raised when trying to do something with a template name that is unknown.
    """


class ProcessDiedException(DazlError):
    pass
