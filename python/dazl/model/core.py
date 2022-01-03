# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module has been relocated to ``dazl.client``, ``dazl.damlast``, ``dazl.protocols``, or
``dazl.query``.
"""
from typing import TYPE_CHECKING, TypeVar, Union
import warnings

from ..client.errors import ConfigurationError, DazlPartyMissingError, UnknownTemplateWarning
from ..client.state import (
    ContractContextualData,
    ContractContextualDataCollection,
    ContractsHistoricalState,
    ContractsState,
)
from ..damlast.daml_lf_1 import TypeConName
from ..damlast.pkgfile import Dar
from ..prim import ContractData, ContractId as ContractId_, DazlError, DazlWarning, Party
from ..prim.errors import DazlImportError
from ..protocols.errors import ConnectionTimeoutError, UserTerminateRequest
from ..query import ContractMatch
from ..util.proc_util import ProcessDiedException

if TYPE_CHECKING:
    from .types import Type, TypeReference

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
        warnings.warn(
            "ContractId.exercise is deprecated; prefer calling dazl.ledger.Connection.exercise or "
            "dazl.client.PartyClient.submit_exercise, or use dazl.ledger.ExerciseCommand instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        from .writing import ExerciseCommand

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
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
