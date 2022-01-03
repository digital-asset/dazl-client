# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# This module will likely be deprecated in v8.

from typing import Any, Sequence

from ..damlast.daml_lf_1 import Type, TypeConName
from ..damlast.daml_types import con
from ..damlast.lookup import find_choice
from ..damlast.protocols import SymbolLookup
from ..ledger import (
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    ExerciseByKeyCommand,
    ExerciseCommand,
)
from ..prim import ContractId
from ..values import ValueMapper

__all__ = [
    "Serializer",
    "AbstractSerializer",
]


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
            key_type = template.key
            if key_type is None:
                raise ValueError(f"template {template.tycon} does not have a key")
            key_value = self.serialize_value(key_type.type, command.key)
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
