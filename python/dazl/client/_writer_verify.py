# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any

from ..damlast.daml_lf_1 import TypeConName
from ..ledger import CreateAndExerciseCommand, CreateCommand, ExerciseByKeyCommand, ExerciseCommand
from ..prim import ContractId
from ..protocols.serializers import AbstractSerializer
from ..values import CanonicalMapper

__all__ = ["ValidateSerializer"]


class ValidateSerializer(AbstractSerializer):
    """
    A serializer that doesn't actually write to an on-wire form, but merely does lightweight
    conversion and give on-wire serialization the best chance of succeeding.

    This class essentially handles type conversion before a command is fully created and sent to
    a background thread for eventual writing to the Ledger API.
    """

    mapper = CanonicalMapper()

    def serialize_create_command(self, name: TypeConName, template_args: Any) -> CreateCommand:
        return CreateCommand(template_id=name, payload=template_args)

    def serialize_exercise_command(
        self, contract_id: ContractId, choice_name: str, choice_args: Any
    ) -> ExerciseCommand:
        return ExerciseCommand(contract_id=contract_id, choice=choice_name, argument=choice_args)

    def serialize_exercise_by_key_command(
        self,
        template_name: TypeConName,
        key_arguments: Any,
        choice_name: str,
        choice_arguments: Any,
    ) -> ExerciseByKeyCommand:
        return ExerciseByKeyCommand(
            template_id=template_name,
            key=key_arguments,
            choice=choice_name,
            argument=choice_arguments,
        )

    def serialize_create_and_exercise_command(
        self,
        template_name: TypeConName,
        create_arguments: Any,
        choice_name: str,
        choice_arguments: Any,
    ) -> CreateAndExerciseCommand:
        return CreateAndExerciseCommand(
            template_id=template_name,
            payload=create_arguments,
            choice=choice_name,
            argument=choice_arguments,
        )
