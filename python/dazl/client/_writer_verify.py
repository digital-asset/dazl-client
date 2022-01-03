# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any
import warnings

from ..damlast.daml_lf_1 import TypeConName
from ..prim import ContractId
from ..protocols.serializers import AbstractSerializer
from ..values import CanonicalMapper
from .commands import CreateAndExerciseCommand, CreateCommand, ExerciseByKeyCommand, ExerciseCommand


class ValidateSerializer(AbstractSerializer):
    """
    A serializer that doesn't actually write to an on-wire form, but merely does lightweight
    conversion and give on-wire serialization the best chance of succeeding.

    This class essentially handles type conversion before a command is fully created and sent to
    a background thread for eventual writing to the Ledger API.
    """

    mapper = CanonicalMapper()

    def serialize_create_command(
        self, name: "TypeConName", template_args: "Any"
    ) -> "CreateCommand":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return CreateCommand(template=name, arguments=template_args)

    def serialize_exercise_command(
        self, contract_id: "ContractId", choice_name: str, choice_args: "Any"
    ) -> "ExerciseCommand":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return ExerciseCommand(contract=contract_id, choice=choice_name, arguments=choice_args)

    def serialize_exercise_by_key_command(
        self,
        template_name: "TypeConName",
        key_arguments: Any,
        choice_name: str,
        choice_arguments: "Any",
    ) -> "ExerciseByKeyCommand":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return ExerciseByKeyCommand(
                template=template_name,
                contract_key=key_arguments,
                choice=choice_name,
                choice_argument=choice_arguments,
            )

    def serialize_create_and_exercise_command(
        self,
        template_name: "TypeConName",
        create_arguments: Any,
        choice_name: str,
        choice_arguments: "Any",
    ) -> "CreateAndExerciseCommand":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return CreateAndExerciseCommand(
                template=template_name,
                arguments=create_arguments,
                choice=choice_name,
                choice_argument=choice_arguments,
            )
