# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Write-Side types
----------------

The :mod:`dazl.model.writing` module contains the Python classes used on the write-side of the
Ledger API.

.. autoclass:: Command
   :members:

.. autoclass:: CreateCommand
   :members:

.. autoclass:: ExerciseCommand
   :members:
"""
from typing import Any, Mapping, NoReturn, Optional, Sequence, Union

from ..damlast.daml_lf_1 import Type, TypeConName
from ..damlast.daml_types import con
from ..damlast.lookup import find_choice, parse_type_con_name
from ..damlast.protocols import SymbolLookup
from ..prim import ContractData, ContractId
from ..util.typing import safe_cast
from ..values import ValueMapper

__all__ = [
    "Command",
    "CreateCommand",
    "CreateAndExerciseCommand",
    "ExerciseCommand",
    "ExerciseByKeyCommand",
    "Serializer",
    "AbstractSerializer",
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


class Serializer:
    """
    Serializer interface for objects on the write-side of the API.
    """

    def serialize_value(self, tt: "Type", obj: "Any") -> "Any":
        raise NotImplementedError("serialize_value requires an implementation")

    def serialize_command(self, command: "Any") -> "Any":
        raise NotImplementedError("serialize_command requires an implementation")


class AbstractSerializer(Serializer):
    """
    Implementation of :class:`Serializer` that helps enforce that all possible cases of type
    serialization have been implemented.
    """

    def __init__(self, lookup: "SymbolLookup"):
        self.lookup = lookup

    @property
    def mapper(self) -> "ValueMapper":
        raise NotImplementedError(f"{type(self)}.mapper() must be defined")

    def serialize_value(self, tt: "Type", obj: Any) -> "Any":
        from ..values import Context

        return Context(self.mapper, self.lookup).convert(tt, obj)

    def serialize_commands(self, commands: "Sequence[Command]") -> "Sequence[Any]":
        return [self.serialize_command(cmd) for cmd in commands]

    def serialize_command(self, command: "Command") -> "Any":
        if isinstance(command, CreateCommand):
            name = self.lookup.template_name(command.template_id)
            value = self.serialize_value(con(name), command.payload)
            return self.serialize_create_command(name, value)

        elif isinstance(command, ExerciseCommand):
            template = self.lookup.template(command.contract_id.value_type)
            choice = find_choice(template, command.choice)
            args = self.serialize_value(choice.arg_binder.type, command.argument)
            return self.serialize_exercise_command(command.contract_id, choice.name, args)

        elif isinstance(command, CreateAndExerciseCommand):
            name = self.lookup.template_name(command.template_id)
            template = self.lookup.template(name)
            create_value = self.serialize_value(con(name), command.payload)
            choice = find_choice(template, command.choice)
            choice_args = self.serialize_value(choice.arg_binder.type, command.argument)
            return self.serialize_create_and_exercise_command(
                name, create_value, choice.name, choice_args
            )

        elif isinstance(command, ExerciseByKeyCommand):
            name = self.lookup.template_name(command.template_id)
            template = self.lookup.template(name)
            key_value = self.serialize_value(template.key.type, command.key)
            choice = find_choice(template, command.choice)
            choice_args = self.serialize_value(choice.arg_binder.type, command.argument)
            return self.serialize_exercise_by_key_command(name, key_value, choice.name, choice_args)

        else:
            raise ValueError(f"unknown Command type: {command!r}")

    def serialize_create_command(self, name: "TypeConName", template_args: "Any") -> "Any":
        raise NotImplementedError("serialize_create_command requires an implementation")

    def serialize_exercise_command(
        self, contract_id: "ContractId", choice_name: str, choice_args: "Any"
    ) -> "Any":
        raise NotImplementedError("serialize_exercise_command requires an implementation")

    def serialize_exercise_by_key_command(
        self, name: "TypeConName", key_arguments: "Any", choice_name: str, choice_arguments: "Any"
    ) -> "Any":
        raise NotImplementedError("serialize_exercise_by_key_command requires an implementation")

    def serialize_create_and_exercise_command(
        self, name: "TypeConName", create_args: "Any", choice_name: str, choice_arguments: "Any"
    ) -> "Any":
        raise NotImplementedError(
            "serialize_create_and_exercise_command requires an implementation"
        )


def validate_template_id(value: "Union[str, TypeConName]") -> "TypeConName":
    if isinstance(value, TypeConName):
        return value
    else:
        return parse_type_con_name(value)
