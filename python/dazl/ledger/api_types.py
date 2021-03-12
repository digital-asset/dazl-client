# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Protocol basic object definitions
---------------------------------

The :mod:`dazl.protocols.obj` module contains the objects that define a common set of fields across
the gRPC Ledger API and HTTP JSON API.

.. autoclass:: Command
   :members:

.. autoclass:: CreateCommand
   :members:

.. autoclass:: CreateAndExerciseCommand
   :members:

.. autoclass:: ExerciseCommand
   :members:

.. autoclass:: ExerciseByKeyCommand
   :members:
"""
from typing import AbstractSet, Any, Collection, Mapping, NoReturn, Optional, Sequence, Union

from ..damlast.daml_lf_1 import TypeConName
from ..damlast.lookup import parse_type_con_name
from ..prim import ContractData, ContractId, Party
from ..util.typing import safe_cast

__all__ = [
    "Command",
    "CreateCommand",
    "CreateAndExerciseCommand",
    "ExerciseCommand",
    "ExerciseByKeyCommand",
    "CreateEvent",
    "ArchiveEvent",
    "ExerciseResponse",
    "PartyInfo",
]


class Command:
    """
    Base class for write-side commands.
    """

    def __setattr__(self, key, value) -> "NoReturn":
        """
        Raise :class:`AttributeError`; instances of this class are immutable.
        """
        raise AttributeError("Command instances are read-only")


class CreateCommand(Command):
    """
    A command that creates a contract without any predecessors.
    """

    __slots__ = ("_template_id", "_payload")

    def __init__(self, template_id: "Union[str, TypeConName]", payload: "ContractData"):
        """
        Initialize a :class:`CreateCommand`.

        :param template_id:
            The template of the contract to be created.
        :param payload:
            The template arguments for the contract to be created.
        """
        object.__setattr__(self, "_template_id", validate_template_id(template_id))
        object.__setattr__(self, "_payload", payload)

    @property
    def template_id(self) -> "TypeConName":
        """
        Return the template of the contract to be created.
        """
        return self._template_id

    @property
    def payload(self) -> "Mapping[str, Any]":
        """
        Return the template arguments for the contract to be created.
        """
        return self._payload

    def __repr__(self) -> str:
        return f"CreateCommand({self.template_id}, {self.payload})"

    def __eq__(self, other: "Any") -> bool:
        return (
            isinstance(other, CreateCommand)
            and self.template_id == other.template_id
            and self.payload == other.payload
        )


class CreateAndExerciseCommand(Command):
    __slots__ = ("_template_id", "_payload", "_choice", "_argument")

    def __init__(
        self,
        template_id: "Union[str, TypeConName]",
        payload: "ContractData",
        choice: str,
        argument: "Optional[Any]" = None,
    ):
        """
        Initialize a :class:`CreateAndExerciseCommand`.

        :param template_id:
            The template of the contract to be created.
        :param payload:
            The template arguments for the contract to be created.
        :param choice:
            The choice to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no arguments.
        """
        object.__setattr__(self, "_template_id", validate_template_id(template_id))
        object.__setattr__(self, "_payload", payload)
        object.__setattr__(self, "_choice", choice)
        object.__setattr__(self, "_argument", argument)

    @property
    def template_id(self) -> "TypeConName":
        """
        Return the template of the contract to be created.
        """
        return self._template_id

    @property
    def payload(self) -> "ContractData":
        """
        Return the template arguments for the contract to be created.
        """
        return self._payload

    @property
    def choice(self) -> str:
        """
        Return the choice to exercise.
        """
        return self._choice

    @property
    def argument(self) -> "Any":
        """
        Return the choice arguments.
        """
        return self._argument

    def __eq__(self, other: "Any") -> bool:
        return (
            isinstance(other, CreateAndExerciseCommand)
            and self.template_id == other.template_id
            and self.payload == other.payload
            and self.choice == other.choice
            and self.argument == other.argument
        )


class ExerciseCommand(Command):
    """
    A command that exercises a choice on a contract identified by its contract ID.
    """

    __slots__ = ("_choice", "_contract_id", "_argument")

    def __init__(self, contract_id: "ContractId", choice: str, argument: "Optional[Any]" = None):
        """
        Initialize an :class:`ExerciseCommand`.

        :param contract_id:
            The contract ID of the contract to exercise.
        :param choice:
            The choice to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no arguments.
        """
        object.__setattr__(self, "_choice", safe_cast(str, choice))
        object.__setattr__(self, "_contract_id", safe_cast(ContractId, contract_id))
        object.__setattr__(self, "_argument", dict(argument) if argument is not None else dict())

    @property
    def contract_id(self) -> "ContractId":
        """
        Return the contract ID of the contract to exercise.
        """
        return self._contract_id

    @property
    def choice(self) -> str:
        """
        Return the choice to exercise.
        """
        return self._choice

    @property
    def argument(self) -> "Any":
        """
        Return the choice arguments.
        """
        return self._argument

    def __repr__(self):
        return f"ExerciseCommand({self.choice!r}, {self.contract_id}, {self.argument}>"

    def __eq__(self, other: "Any") -> bool:
        return (
            isinstance(other, ExerciseCommand)
            and self.choice == other.choice
            and self.contract_id == other.contract_id
            and self.argument == other.argument
        )


class ExerciseByKeyCommand(Command):
    """
    A command that exercises a choice on a contract identified by its contract key.
    """

    __slots__ = ("_template_id", "_key", "_choice", "_argument")

    def __init__(
        self,
        template_id: "Union[str, TypeConName]",
        key: "Any",
        choice: str,
        argument: "Optional[Any]",
    ):
        """
        Initialize an :class:`ExerciseByKeyCommand`.

        :param template_id:
            The contract template type.
        :param key:
            The contract key of the contract to exercise.
        :param choice:
            The choice to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no arguments.
        """
        object.__setattr__(self, "_template_id", validate_template_id(template_id))
        object.__setattr__(self, "_key", key)
        object.__setattr__(self, "_choice", choice)
        object.__setattr__(self, "_argument", argument)

    @property
    def template_id(self) -> "TypeConName":
        """
        Return the contract template type.
        """
        return self._template_id

    @property
    def key(self) -> "Any":
        """
        Return the contract key of the contract to exercise.
        """
        return self._key

    @property
    def choice(self) -> str:
        """
        Return the choice to exercise.
        """
        return self._choice

    @property
    def argument(self) -> "Any":
        """
        Return the choice arguments.
        """
        return self._argument

    def __eq__(self, other: "Any") -> bool:
        return (
            isinstance(other, ExerciseByKeyCommand)
            and self.template_id == other.template_id
            and self.key == other.key
            and self.choice == other.choice
            and self.argument == other.argument
        )


class CreateEvent:
    """
    An event that indicates a newly-created contract.
    """

    __slots__ = (
        "_contract_id",
        "_payload",
        "_signatories",
        "_observers",
        "_agreement_text",
        "_key",
    )

    def __init__(
        self,
        contract_id: "ContractId",
        payload: "ContractData",
        signatories: "Collection[Party]",
        observers: "Collection[Party]",
        agreement_text: "Optional[str]",
        key: "Optional[Any]",
    ):
        object.__setattr__(self, "_contract_id", contract_id)
        object.__setattr__(self, "_payload", payload)
        object.__setattr__(self, "_signatories", frozenset(signatories))
        object.__setattr__(self, "_observers", frozenset(observers))
        object.__setattr__(self, "_agreement_text", agreement_text)
        object.__setattr__(self, "_key", key)

    @property
    def contract_id(self) -> "ContractId":
        return self._contract_id

    @property
    def payload(self) -> "ContractData":
        return self._payload

    @property
    def signatories(self) -> "AbstractSet[Party]":
        return self._signatories

    @property
    def observers(self) -> "AbstractSet[Party]":
        return self._observers

    @property
    def agreement_text(self) -> "Optional[str]":
        return self._agreement_text

    @property
    def key(self) -> "Optional[Any]":
        return self._key

    def __eq__(self, other: "Any") -> bool:
        return (
            isinstance(other, CreateEvent)
            and self.contract_id == other.contract_id
            and self.payload == other.payload
            and self.signatories == other.signatories
            and self.observers == other.observers
            and self.agreement_text == other.agreement_text
            and self.key == other.key
        )


class ArchiveEvent:
    """
    An event that indicates a contract was archived.
    """

    __slots__ = ("_contract_id",)

    def __init__(self, contract_id: "ContractId"):
        object.__setattr__(self, "_contract_id", contract_id)

    @property
    def contract_id(self) -> "ContractId":
        return self._contract_id


class ExerciseResponse:
    __slots__ = "_result", "_events"

    _result: "Optional[Any]"
    _events: "Sequence[Union[CreateEvent, ArchiveEvent]]"

    def __init__(
        self, result: "Optional[Any]", events: "Sequence[Union[CreateEvent, ArchiveEvent]]"
    ):
        object.__setattr__(self, "_result", result)
        object.__setattr__(self, "_events", tuple(events))

    @property
    def result(self) -> "Optional[Any]":
        return self._result

    @property
    def events(self) -> "Sequence[Union[CreateEvent, ArchiveEvent]]":
        return self._events

    def __repr__(self):
        return f"ExerciseResponse(result={self.result}, events={self.events})"


class PartyInfo:
    __slots__ = "_party", "_display_name", "_is_local"

    _party: "Party"
    _display_name: str
    _is_local: bool

    def __init__(self, party: "Party", display_name: str, is_local: bool):
        object.__setattr__(self, "_party", party)
        object.__setattr__(self, "_display_name", display_name)
        object.__setattr__(self, "_is_local", is_local)

    @property
    def party(self) -> "Party":
        return self._party

    @property
    def display_name(self) -> str:
        return self._display_name

    @property
    def is_local(self) -> bool:
        return self._is_local


def validate_template_id(value: "Union[str, TypeConName]") -> "TypeConName":
    if isinstance(value, TypeConName):
        return value
    else:
        return parse_type_con_name(value)
