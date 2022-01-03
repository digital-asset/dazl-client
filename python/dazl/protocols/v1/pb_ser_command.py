# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Conversion methods to Ledger API Protobuf-generated types from dazl/Pythonic types.
"""
from typing import TYPE_CHECKING, Any, Union
import warnings

from ..._gen.com.daml.ledger.api import v1 as lapipb
from ...damlast.daml_lf_1 import TypeConName
from ...damlast.util import module_local_name, module_name, package_ref
from ...ledger.grpc.codec_aio import Codec
from ...prim import ContractId, timedelta_to_duration
from ...values.protobuf import ProtobufEncoder, set_value
from ..serializers import AbstractSerializer

if TYPE_CHECKING:
    from ...client.commands import CommandPayload
    from ...model.types import TypeReference
    from ...model.writing import CommandPayload

__all__ = ["as_identifier", "ProtobufSerializer"]


def as_identifier(tref: "Union[TypeReference, TypeConName]") -> "lapipb.Identifier":
    from ...model.types import TypeReference

    warnings.warn("Use Codec.encode_identifier instead.", DeprecationWarning, stacklevel=2)

    if isinstance(tref, TypeReference):
        tref = tref.con

    return Codec.encode_identifier(tref)


class ProtobufSerializer(AbstractSerializer):

    mapper = ProtobufEncoder()

    ################################################################################################
    # COMMAND serializers
    ################################################################################################

    def serialize_command_request(
        self, command_payload: "CommandPayload"
    ) -> "lapipb.SubmitAndWaitRequest":
        commands = [self.serialize_command(command) for command in command_payload.commands]
        if command_payload.deduplication_time is not None:
            return lapipb.SubmitAndWaitRequest(
                commands=lapipb.Commands(
                    ledger_id=command_payload.ledger_id,
                    workflow_id=command_payload.workflow_id,
                    application_id=command_payload.application_id,
                    command_id=command_payload.command_id,
                    party=command_payload.party,
                    commands=commands,
                    deduplication_time=timedelta_to_duration(command_payload.deduplication_time),
                )
            )
        else:
            return lapipb.SubmitAndWaitRequest(
                commands=lapipb.Commands(
                    ledger_id=command_payload.ledger_id,
                    workflow_id=command_payload.workflow_id,
                    application_id=command_payload.application_id,
                    command_id=command_payload.command_id,
                    party=command_payload.party,
                    commands=commands,
                )
            )

    def serialize_create_command(
        self, name: "TypeConName", template_args: "Any"
    ) -> "lapipb.Command":
        create_ctor, create_value = template_args
        if create_ctor != "record":
            raise ValueError("Template values must resemble records")

        cmd = lapipb.CreateCommand()
        _set_template(cmd.template_id, name)
        cmd.create_arguments.MergeFrom(create_value)
        return lapipb.Command(create=cmd)

    def serialize_exercise_command(
        self, contract_id: "ContractId", choice_name: str, choice_args: "Any"
    ) -> lapipb.Command:
        type_ref = contract_id.value_type
        ctor, value = choice_args

        cmd = lapipb.ExerciseCommand()
        _set_template(cmd.template_id, type_ref)
        cmd.contract_id = contract_id.value
        cmd.choice = choice_name
        set_value(cmd.choice_argument, ctor, value)
        return lapipb.Command(exercise=cmd)

    def serialize_exercise_by_key_command(
        self,
        template_name: "TypeConName",
        key_arguments: Any,
        choice_name: str,
        choice_arguments: Any,
    ) -> lapipb.Command:
        key_ctor, key_value = key_arguments
        choice_ctor, choice_value = choice_arguments

        cmd = lapipb.ExerciseByKeyCommand()
        _set_template(cmd.template_id, template_name)
        set_value(cmd.contract_key, key_ctor, key_value)
        cmd.choice = choice_name
        set_value(cmd.choice_argument, choice_ctor, choice_value)
        return lapipb.Command(exerciseByKey=cmd)

    def serialize_create_and_exercise_command(
        self,
        template_name: "TypeConName",
        create_arguments: "Any",
        choice_name: str,
        choice_arguments: Any,
    ) -> lapipb.Command:
        create_ctor, create_value = create_arguments
        if create_ctor != "record":
            raise ValueError("Template values must resemble records")
        choice_ctor, choice_value = choice_arguments

        cmd = lapipb.CreateAndExerciseCommand()
        _set_template(cmd.template_id, template_name)
        cmd.create_arguments.MergeFrom(create_value)
        cmd.choice = choice_name
        set_value(cmd.choice_argument, choice_ctor, choice_value)
        return lapipb.Command(createAndExercise=cmd)


def _set_template(message: "lapipb.Identifier", name: "TypeConName") -> None:
    message.package_id = package_ref(name)
    message.module_name = str(module_name(name))
    message.entity_name = module_local_name(name)
