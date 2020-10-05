# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Methods for serializing domain objects and other things into basic primitive
types over the wire on the REST interface using JSON.
"""

import warnings
from datetime import datetime, date
from decimal import Decimal
from typing import Union, Dict, Any, List

from ...model.types import ListType, RecordType, VariantType, \
    ContractIdType, UnsupportedType, as_contract_id, TemplateChoice, TextMapType
from ...model.writing import CommandPayload, AbstractSerializer, TypeEvaluationContext
from ...prim import ContractId, JSONEncoder, to_bool, to_date, to_datetime, to_decimal, \
    to_int, to_str, to_timedelta, to_variant

R = Union[bool, str, date, datetime, int, float, Decimal, List['R'], Dict[str, 'R']]


class LedgerJSONEncoder(JSONEncoder):
    """
    Convert some known Ledger API primitive types into their appropriate JSON
    representations.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            'dazl.protocols.v0.json_ser_command.LedgerJSONEncoder is deprecated; '
            'use dazl.prim.JSONEncoder instead.', DeprecationWarning, stacklevel=2)


def to_api_datetime(obj):
    """
    Converts the object to an ISO8601 datetime string.

    :param obj:
        A datetime. If the datetime is "naive" (no timezone information), it is
        assumed to refer to UTC. If the datetime has timezone information, the
        datetime will be converted to UTC before serializing.
    :return: An ISO8601 string that represents the time in UTC.
    """
    from ...prim import datetime_to_str
    warnings.warn(
        'dazl.protocols.v0.json_ser_command.to_api_datetime is deprecated; use dazl.prim.datetime_to_str instead.',
        DeprecationWarning, stacklevel=2)
    return datetime_to_str(obj) if isinstance(obj, datetime) else obj


class JsonSerializer(AbstractSerializer[dict, R]):

    ################################################################################################
    # COMMAND serializers
    ################################################################################################

    def serialize_command_request(self, command_payload: CommandPayload) -> dict:
        commands = [self.serialize_command(command) for command in command_payload.commands]
        return dict(
            businessIntent=command_payload.command_id,
            commands=commands,
            application=command_payload.application_id)

    def serialize_create_command(self, template_type: RecordType, template_args: R) -> dict:
        # the package_id in ModuleRef is a convenient place to
        # stash legacy template IDs in the REST endpoint
        return {'create': {
            'template': str(template_type.name.con),
            'arguments': template_args}}

    def serialize_exercise_command(
            self, contract_id: 'ContractId', choice_info: TemplateChoice, choice_args: R) -> dict:
        return {'exercise': {
            'contract': str(contract_id.value_type),
            'choice': choice_info.name,
            'arguments': choice_args}}

    ################################################################################################
    # VALUE serializers
    ################################################################################################

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> R:
        return dict()

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_bool(obj)

    def serialize_text(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_str(obj)

    def serialize_int(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_int(obj)

    def serialize_decimal(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_decimal(obj)

    def serialize_party(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_str(obj)

    def serialize_date(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_date(obj)

    def serialize_datetime(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_datetime(obj)

    def serialize_timedelta(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_timedelta(obj)

    def serialize_contract_id(
            self, context: TypeEvaluationContext, tt: ContractIdType, obj: Any) -> R:
        return as_contract_id(obj, template_id=tt.type_parameter).contract_id

    def serialize_list(self, context: TypeEvaluationContext, tt: ListType, obj: Any) -> R:
        return [self._serialize_dispatch(context.append_path(f'[{i}]'), tt.type_parameter, item)
                for i, item in enumerate(obj)]

    def serialize_map(self, context: TypeEvaluationContext, tt: TextMapType, obj: Any) -> R:
        return {self._serialize_dispatch(context.append_path(f'[key {i}]'), tt.key_type, key):
                self._serialize_dispatch(context.append_path(f'[value {i}]'), tt.value_type, value)
                for i, (key, value) in enumerate(obj.items())}

    def serialize_record(self, context: TypeEvaluationContext, tt: RecordType, obj: Any) -> R:
        return {arg: self._serialize_dispatch(context.append_path(arg), arg_type, obj.get(arg))
                for arg, arg_type in tt.named_args}

    def serialize_variant(self, context: TypeEvaluationContext, tt: VariantType, obj: Any) -> R:
        obj_ctor, obj_value = to_variant(obj)
        value_ctor = tt.field_type(obj_ctor)

        new_value = self._serialize_dispatch(context.append_path(obj_ctor), value_ctor, obj_value)
        return {obj_ctor: new_value}

    def serialize_unsupported(
            self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) -> R:
        return obj

