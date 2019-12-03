# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Conversion methods to Ledger API Protobuf-generated types from dazl/Pythonic types.
"""
from datetime import date, datetime, timedelta, timezone
from typing import Any, Optional, Tuple

from ... import LOG
# noinspection PyPep8Naming
from . import model as G
from ...model.core import ContractId
from ...model.types import VariantType, RecordType, ListType, ContractIdType, \
    UnsupportedType, TemplateChoice, TypeReference, TypeEvaluationContext, SCALAR_TYPE_UNIT, \
    TextMapType, OptionalType, EnumType
from ...model.writing import AbstractSerializer, CommandPayload
from ...util.prim_types import to_boolean, to_date, to_datetime, to_decimal, to_int, to_str, \
    decode_variant_dict

# noinspection PyPackageRequirements
from google.protobuf.empty_pb2 import Empty
# noinspection PyPackageRequirements
from google.protobuf.timestamp_pb2 import Timestamp


R = Tuple[str, Any]


_NANOS_PER_MICROSECOND = 1000
_SECONDS_PER_DAY = 24 * 3600


def as_api_timestamp(dt: datetime) -> Timestamp:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    td = dt - datetime(1970, 1, 1, tzinfo=timezone.utc)
    ts = Timestamp()
    ts.seconds = td.seconds + td.days * _SECONDS_PER_DAY
    ts.nanos = td.microseconds * _NANOS_PER_MICROSECOND
    return ts


def pb_get_date(obj: date) -> int:
    """
    Return the Python ``datetime.date`` as the number of days since 1970 Jan 1.
    """
    return (obj - date(1970, 1, 1)).days


def pb_get_timestamp(obj: datetime) -> float:
    """
    Return the Python ``datetime.datetime`` as number of microseconds since
    1970 Jan 1 midnight, UTC.
    """
    if obj.tzinfo is not None and obj.tzinfo.utcoffset(obj) is not None:
        # aware time; translate to UTC
        obj = obj.astimezone(timezone.utc)
    obj = obj.replace(tzinfo=None)
    td: timedelta = obj - datetime(1970, 1, 1, 0, 0, 0)
    return (td.days * 86400 + td.seconds) * 10 ** 6 + td.microseconds


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
            ledger_effective_time=as_api_timestamp(command_payload.ledger_effective_time),
            maximum_record_time=as_api_timestamp(command_payload.maximum_record_time)))

    def serialize_create_command(self, template_type: RecordType, template_args: R) -> G.Command:
        create_ctor, create_value = template_args
        if create_ctor != 'record':
            raise ValueError('Template values must resemble records')

        cmd = G.CreateCommand()
        _set_template(cmd.template_id, template_type.name)
        _set_value(cmd.create_arguments, None, create_value)
        return G.Command(create=cmd)

    def serialize_exercise_command(
            self, contract_id: ContractId, choice_info: TemplateChoice, choice_args: R) \
            -> G.Command:
        type_ref = contract_id.template_id  # type: TypeReference
        ctor, value = choice_args

        cmd = G.ExerciseCommand()
        _set_template(cmd.template_id, type_ref)
        cmd.contract_id = contract_id.contract_id
        cmd.choice = choice_info.name
        _set_value(cmd.choice_argument, ctor, value)
        return G.Command(exercise=cmd)

    def serialize_exercise_by_key_command(
            self, template_ref: TypeReference, key_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> G.Command:
        key_ctor, key_value = key_arguments
        choice_ctor, choice_value = choice_arguments

        cmd = G.ExerciseByKeyCommand()
        _set_template(cmd.template_id, template_ref)
        _set_value(cmd.contract_key, key_ctor, key_value)
        cmd.choice = choice_info.name
        _set_value(cmd.choice_argument, choice_ctor, choice_value)
        return G.Command(exerciseByKey=cmd)

    def serialize_create_and_exercise_command(
            self, template_type: RecordType, create_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> G.Command:
        create_ctor, create_value = create_arguments
        if create_ctor != 'record':
            raise ValueError('Template values must resemble records')
        choice_ctor, choice_value = choice_arguments

        cmd = G.CreateAndExerciseCommand()
        _set_template(cmd.template_id, template_type.name)
        _set_value(cmd.create_arguments, None, create_value)
        cmd.choice = choice_info.name
        _set_value(cmd.choice_argument, choice_ctor, choice_value)
        return G.Command(createAndExercise=cmd)

    ################################################################################################
    # VALUE serializers
    ################################################################################################

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'unit', Empty()

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'bool', to_boolean(obj)

    def serialize_text(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'text', to_str(obj)

    def serialize_int(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'int64', to_int(obj)

    def serialize_decimal(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'numeric', str(to_decimal(obj))

    def serialize_party(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'party', to_str(obj)

    def serialize_date(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'date', pb_get_date(to_date(obj))

    def serialize_datetime(self, context: TypeEvaluationContext, obj: Any) -> R:
        return 'timestamp', pb_get_timestamp(to_datetime(obj))

    def serialize_timedelta(self, context: TypeEvaluationContext, obj: Any) -> R:
        raise ValueError('RelTime types are not supported by the gRPC API')

    def serialize_contract_id(
            self, context: TypeEvaluationContext, tt: ContractIdType, obj: Any) -> R:
        return 'contract_id', to_str(obj)

    def serialize_optional(self, context: TypeEvaluationContext, tt: OptionalType, obj: Any):
        from ..._gen.com.digitalasset.ledger.api.v1.value_pb2 import Optional
        ut = tt.type_parameter

        optional_message = Optional()
        if obj is not None:
            ctor, val = self._serialize_dispatch(context.append_path('?'), ut, obj)
            _set_value(optional_message.value, ctor, val)
        return 'optional', optional_message

    def serialize_list(self, context: TypeEvaluationContext, tt: ListType, obj: Any) -> R:
        from ..._gen.com.digitalasset.ledger.api.v1.value_pb2 import List
        ut = tt.type_parameter

        list_message = List()
        for i, item in enumerate(obj):
            value = list_message.elements.add()
            ctor, val = self._serialize_dispatch(context.append_path(f'[{i}]'), ut, item)
            _set_value(value, ctor, val)
        return 'list', list_message

    def serialize_map(self, context: TypeEvaluationContext, tt: TextMapType, obj: Any) -> R:
        from ..._gen.com.digitalasset.ledger.api.v1.value_pb2 import Map
        vt = tt.value_type

        map_message = Map()
        for key, value in obj.items():
            entry = map_message.entries.add()
            entry.key = key
            ctor, val = self._serialize_dispatch(context.append_path(f'[{key}]'), vt, value)
            _set_value(entry.value, ctor, val)
        return 'map', map_message

    def serialize_record(self, context: TypeEvaluationContext, tt: RecordType, obj: Any) -> R:
        from ..._gen.com.digitalasset.ledger.api.v1.value_pb2 import Record

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
            _set_value(field.value, ctor, value)
        if did_fail:
            raise ValueError('Failed to parse a record; check the logs for more information.')
        return 'record', record_message

    def serialize_variant(self, context: TypeEvaluationContext, tt: VariantType, obj: Any) -> R:
        from ..._gen.com.digitalasset.ledger.api.v1.value_pb2 import Variant
        try:
            obj_ctor, obj_value = decode_variant_dict(obj)
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
        _set_value(variant_message.value, ctor, value)
        return 'variant', variant_message

    def serialize_enum(self, context: TypeEvaluationContext, tt: EnumType, obj: Any) -> R:
        from ..._gen.com.digitalasset.ledger.api.v1.value_pb2 import Enum
        enum_message = Enum()
        enum_message.constructor = obj
        return 'enum', enum_message

    def serialize_unsupported(
            self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) -> R:
        raise Exception(f'UnsupportedType {tt} is not serializable in gRPC')


def _set_template(message: G.Identifier, tref: TypeReference) -> None:
    message.package_id = tref.module.package_id
    message.module_name = '.'.join(tref.module.module_name)
    message.entity_name = '.'.join(tref.name)
    # This field is set for historical reasons, and no longer required after Sandbox 0.10.12
    try:
        message.name = tref.full_name
    except AttributeError:
        pass


def _set_value(message: G.Value, ctor: 'Optional[str]', value) -> None:
    """
    Work around the somewhat crazy API of Python's gRPC library to apply a known value to a
    :class:`Value`.

    :param message:
        The :class:`Value` object to modify.
    :param ctor:
        The actual field to apply to, or ``None`` to interpret the entire message as a ``Record``
        instead.
    :param value:
        The actual value to set. Must be compatible with the appropriate field.
    """
    try:
        if ctor is None:
            message.MergeFrom(value)
        elif ctor == 'unit':
            message.unit.SetInParent()
        elif ctor in ('record', 'variant', 'list', 'optional', 'enum', 'map', 'gen_map'):
            getattr(message, ctor).MergeFrom(value)
        else:
            setattr(message, ctor, value)
    except:  # noqa
        LOG.error('Failed to set a value %s, %s', ctor, value)
        raise
