# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Conversion methods to Ledger API Protobuf-generated types from dazl/Pythonic types.
"""
from typing import Any, Tuple, Union

# noinspection PyPackageRequirements
from google.protobuf.empty_pb2 import Empty

# noinspection PyPep8Naming
from . import model as G
from ... import LOG
from ...damlast.daml_lf_1 import TypeConName
from ...model.core import ContractId
from ...model.types import VariantType, RecordType, ListType, ContractIdType, \
    UnsupportedType, TemplateChoice, TypeReference, TypeEvaluationContext, SCALAR_TYPE_UNIT, \
    TextMapType, OptionalType, EnumType
from ...model.writing import AbstractSerializer, CommandPayload
from ...prim import date_to_int, datetime_to_epoch_microseconds, decimal_to_str, \
    timedelta_to_duration, to_bool, to_date, to_datetime, to_decimal, to_int, to_str, to_variant
from ...values.protobuf import set_value

R = Tuple[str, Any]


def as_identifier(tref: 'Union[TypeReference, TypeConName]') -> 'G.Identifier':
    if isinstance(tref, TypeReference):
        tref = tref.con

    if isinstance(tref, TypeConName):
        identifier = G.Identifier()
        _set_template(identifier, tref)
        return identifier

    else:
        raise TypeError('as_identifier requires a TypeConName or a TypeReference')


class ProtobufSerializer(AbstractSerializer[G.Command, R]):

    ################################################################################################
    # COMMAND serializers
    ################################################################################################

    def serialize_command_request(self, command_payload: CommandPayload) -> G.SubmitRequest:
        commands = [self.serialize_command(command) for command in command_payload.commands]
        return G.SubmitRequest(commands=G.Commands(
            ledger_id=command_payload.ledger_id,
            workflow_id=command_payload.workflow_id,
            application_id=command_payload.application_id,
            command_id=command_payload.command_id,
            party=command_payload.party,
            commands=commands,
            deduplication_time=(timedelta_to_duration(command_payload.deduplication_time)
                                if command_payload.deduplication_time is not None else None)))

    def serialize_create_command(self, template_type: RecordType, template_args: R) -> G.Command:
        create_ctor, create_value = template_args
        if create_ctor != 'record':
            raise ValueError('Template values must resemble records')

        cmd = G.CreateCommand()
        _set_template(cmd.template_id, template_type.name.con)
        set_value(cmd.create_arguments, None, create_value)
        return G.Command(create=cmd)

    def serialize_exercise_command(
            self, contract_id: ContractId, choice_info: TemplateChoice, choice_args: R) \
            -> G.Command:
        type_ref = contract_id.value_type
        ctor, value = choice_args

        cmd = G.ExerciseCommand()
        _set_template(cmd.template_id, type_ref)
        cmd.contract_id = contract_id.value
        cmd.choice = choice_info.name
        set_value(cmd.choice_argument, ctor, value)
        return G.Command(exercise=cmd)

    def serialize_exercise_by_key_command(
            self, template_ref: TypeReference, key_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> G.Command:
        key_ctor, key_value = key_arguments
        choice_ctor, choice_value = choice_arguments

        cmd = G.ExerciseByKeyCommand()
        _set_template(cmd.template_id, template_ref.con)
        set_value(cmd.contract_key, key_ctor, key_value)
        cmd.choice = choice_info.name
        set_value(cmd.choice_argument, choice_ctor, choice_value)
        return G.Command(exerciseByKey=cmd)

    def serialize_create_and_exercise_command(
            self, template_type: RecordType, create_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> G.Command:
        create_ctor, create_value = create_arguments
        if create_ctor != 'record':
            raise ValueError('Template values must resemble records')
        choice_ctor, choice_value = choice_arguments

        cmd = G.CreateAndExerciseCommand()
        _set_template(cmd.template_id, template_type.name.con)
        set_value(cmd.create_arguments, None, create_value)
        cmd.choice = choice_info.name
        set_value(cmd.choice_argument, choice_ctor, choice_value)
        return G.Command(createAndExercise=cmd)

    ################################################################################################
    # VALUE serializers
    ################################################################################################

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'unit', Empty()

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'bool', to_bool(obj)

    def serialize_text(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'text', to_str(obj)

    def serialize_int(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'int64', to_int(obj)

    def serialize_decimal(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'numeric', decimal_to_str(to_decimal(obj))

    def serialize_party(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'party', to_str(obj)

    def serialize_date(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'date', date_to_int(to_date(obj))

    def serialize_datetime(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'timestamp', datetime_to_epoch_microseconds(to_datetime(obj))

    def serialize_timedelta(self, context: TypeEvaluationContext, obj: Any) -> R:
        raise ValueError('RelTime types are not supported by the gRPC API')

    def serialize_contract_id(
            self, context: TypeEvaluationContext, tt: ContractIdType, obj: Any) -> R:
        return 'contract_id', to_str(obj)

    def serialize_optional(self, context: TypeEvaluationContext, tt: OptionalType, obj: Any):
        from ..._gen.com.daml.ledger.api.v1.value_pb2 import Optional
        ut = tt.type_parameter

        optional_message = Optional()
        if obj is not None:
            ctor, val = self._serialize_dispatch(context.append_path('?'), ut, obj)
            set_value(optional_message.value, ctor, val)
        return 'optional', optional_message

    def serialize_list(self, context: TypeEvaluationContext, tt: ListType, obj: Any) -> R:
        from ..._gen.com.daml.ledger.api.v1.value_pb2 import List
        ut = tt.type_parameter

        list_message = List()
        for i, item in enumerate(obj):
            value = list_message.elements.add()
            ctor, val = self._serialize_dispatch(context.append_path(f'[{i}]'), ut, item)
            set_value(value, ctor, val)
        return 'list', list_message

    def serialize_map(self, context: TypeEvaluationContext, tt: TextMapType, obj: Any) -> R:
        from ..._gen.com.daml.ledger.api.v1.value_pb2 import Map
        vt = tt.value_type

        map_message = Map()
        for key, value in obj.items():
            entry = map_message.entries.add()
            entry.key = key
            ctor, val = self._serialize_dispatch(context.append_path(f'[{key}]'), vt, value)
            set_value(entry.value, ctor, val)
        return 'map', map_message

    def serialize_record(self, context: TypeEvaluationContext, tt: RecordType, obj: Any) -> R:
        from ..._gen.com.daml.ledger.api.v1.value_pb2 import Record

        did_fail = False
        record_message = Record()
        for key, vt in tt.named_args:
            if key not in obj:
                LOG.error('The field %s is missing on %s', key, tt)
                did_fail = True
                continue

            ctor, value = self._serialize_dispatch(context.append_path(key), vt, obj.get(key))
            field = record_message.fields.add()
            field.label = key
            set_value(field.value, ctor, value)
        if did_fail:
            raise ValueError('Failed to parse a record; check the logs for more information.')
        return 'record', record_message

    def serialize_variant(self, context: TypeEvaluationContext, tt: VariantType, obj: Any) -> R:
        from ..._gen.com.daml.ledger.api.v1.value_pb2 import Variant
        try:
            obj_ctor, obj_value = to_variant(obj)
        except ValueError:
            if len(tt.named_args) == 1:
                # there is only one variation on this variant; under very specific circumstances
                # we'll allow for some convenience representations of this case
                obj_ctor, vt = tt.named_args[0]
                if (isinstance(vt, (RecordType, VariantType)) and len(vt.named_args) == 0) or \
                        vt == SCALAR_TYPE_UNIT:
                    obj_value = {}
                else:
                    LOG.error('Could not find a helpful representation of the single-variant case '
                              'with value type %s', vt)
                    raise
            else:
                raise

        vt = tt._find_ctor(obj_ctor)

        ctor, value = self._serialize_dispatch(context.append_path(obj_ctor), vt, obj_value)

        variant_message = Variant()
        variant_message.constructor = obj_ctor
        set_value(variant_message.value, ctor, value)
        return 'variant', variant_message

    def serialize_enum(self, context: TypeEvaluationContext, tt: EnumType, obj: Any) -> R:
        from ..._gen.com.daml.ledger.api.v1.value_pb2 import Enum
        enum_message = Enum()
        enum_message.constructor = obj
        return 'enum', enum_message

    def serialize_unsupported(
            self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) -> R:
        raise Exception(f'UnsupportedType {tt} is not serializable in gRPC')


def _set_template(message: G.Identifier, name: 'TypeConName') -> None:
    from ...damlast.util import package_ref, module_name, module_local_name
    message.package_id = package_ref(name)
    message.module_name = str(module_name(name))
    message.entity_name = module_local_name(name)
