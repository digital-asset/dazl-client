# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Methods for serializing domain objects and other things into basic primitive
types over the wire on the REST interface using JSON.
"""

import abc
import json

from datetime import datetime, timezone, date
from decimal import Decimal
from typing import Union, Dict, Any, List

from ... import LOG
from ...model.core import ContractId
from ...model.types import ScalarType, ListType, RecordType, VariantType, \
    ContractIdType, UnsupportedType, as_contract_id, TemplateChoice, TextMapType
from ...model.writing import CommandPayload, AbstractSerializer, TypeEvaluationContext
from ...util.prim_types import to_boolean, to_date, to_str, to_decimal, decode_variant_dict, \
    to_int, to_datetime, to_timedelta

R = Union[bool, str, date, datetime, int, float, Decimal, List['R'], Dict[str, 'R']]


class BodyDecoder(abc.ABC):
    @abc.abstractmethod
    def parse(self, code, buf):
        """

        :param code: The HTTP status code associated with the body.
        :param buf:
        :return:
        """


class LedgerJSONEncoder(json.JSONEncoder):
    """
    Convert some known Ledger API primitive types into their appropriate JSON
    representations.
    """
    def default(self, o):
        # pylint: disable=E0202
        # bug in pylint https://github.com/PyCQA/pylint/issues/414)
        if isinstance(o, datetime):
            return _datetime_to_api_datetime(o)
        elif isinstance(o, date):
            return _date_to_api_date(o)
        elif isinstance(o, ContractId):
            return o.contract_id
        elif isinstance(o, Decimal):
            return _NoStringDecimal(o)

        return json.JSONEncoder.default(self, o)


def to_api_datetime(obj):
    """
    Converts the object to an ISO8601 datetime string.

    :param obj:
        A datetime. If the datetime is "naive" (no timezone information), it is
        assumed to refer to UTC. If the datetime has timezone information, the
        datetime will be converted to UTC before serializing.
    :return: An ISO8601 string that represents the time in UTC.
    """
    if isinstance(obj, datetime):
        return _datetime_to_api_datetime(obj)
    elif isinstance(obj, str):
        # attempt to understand this string as a datetime
        pass
    return obj


def _date_to_api_date(obj: date) -> str:
    """
    Convert date to a JSON string that represents a date.
    """
    return obj.isoformat()


def _datetime_to_api_datetime(obj: datetime) -> str:
    """
    Convert timezone "aware" dates to UTC.
    """
    if obj.tzinfo is not None and obj.tzinfo.utcoffset(obj) is not None:
        # aware time; translate to UTC
        obj = obj.astimezone(timezone.utc)
    obj = obj.replace(tzinfo=None)
    return obj.isoformat() + 'Z'


class _NoStringDecimal(float):
    def __new__(cls, decimal_value):
        # noinspection PyArgumentList
        return float.__new__(cls, float(decimal_value))

    def __init__(self, decimal_value):
        float.__init__(float(decimal_value))
        self.decimal_value = decimal_value

    def __repr__(self):
        return str(self.decimal_value)


####################################################################################################
# for_json support
####################################################################################################


def timedelta_for_json(value):
    from datetime import timedelta
    if isinstance(value, timedelta):
        # TODO: Implementation
        raise NotImplementedError('reltime are not currently supported')
    # TODO: Some light coercion is probably required here
    return value


def date_for_json(value):
    """
    Return a Python ``date``, and rely on the JSON encoder in
    :class:`LedgerJSONEncoder` to do the appropriate conversion.
    """
    return value


def time_for_json(value):
    """
    Return a Python ``datetime``, and rely on the JSON encoder in
    :mod:`da.protocols.ser_json` to do the appropriate conversion.
    """
    return value


def _weakbound_for_json(value):
    """
    Simply call `for_json` on the underlying value if it exists; otherwise, return the underlying
    value.
    """
    return value.for_json() if hasattr(value, 'for_json') else value


def _define_scalar_formatters():
    """
    Produce a dict whose keys are :class:`ScalarType` and values are methods that can take a
    value and convert them to a JSON representation.
    """
    formatters = {
        "Bool": bool,
        "Char": str,
        "Integer": int,
        "Decimal": Decimal,
        "Numeric": Decimal,
        "Text": str,
        "Party": str,
        "RelTime": timedelta_for_json,
        "Date": date_for_json,
        "Time": time_for_json,
        "Any": str,
    }

    if len(ScalarType.BUILTINS) != len(formatters):
        LOG.error('Programmer error. Formatters: %r, builtins: %r', formatters, ScalarType.BUILTINS)
        raise Exception('library configuration error')
    return {scalar_type: formatters[scalar_type.name] for scalar_type in ScalarType.BUILTINS}


_SCALAR_FORMATTERS = _define_scalar_formatters()


class JsonSerializer(AbstractSerializer[dict, R]):

    ################################################################################################
    # COMMAND serializers
    ################################################################################################

    def serialize_command_request(self, command_payload: CommandPayload) -> dict:
        commands = [self.serialize_command(command) for command in command_payload.commands]
        return dict(
            businessIntent=command_payload.command_id,
            ledgerEffectiveTime=command_payload.ledger_effective_time,
            maximumRecordTime=command_payload.maximum_record_time,
            commands=commands,
            application=command_payload.application_id)

    def serialize_create_command(self, template_type: RecordType, template_args: R) -> dict:
        # the package_id in ModuleRef is a convenient place to
        # stash legacy template IDs in the REST endpoint
        return {'create': {
            'template': template_type.name.module.package_id,
            'arguments': template_args}}

    def serialize_exercise_command(
            self, contract_id: ContractId, choice_info: TemplateChoice, choice_args: R) -> dict:
        return {'exercise': {
            'contract': contract_id.contract_id,
            'choice': choice_info.name,
            'arguments': choice_args}}

    ################################################################################################
    # VALUE serializers
    ################################################################################################

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> R:
        return dict()

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> R:
        return to_boolean(obj)

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
        obj_ctor, obj_value = decode_variant_dict(obj)
        value_ctor = tt.field_type(obj_ctor)

        new_value = self._serialize_dispatch(context.append_path(obj_ctor), value_ctor, obj_value)
        return {obj_ctor: new_value}

    def serialize_unsupported(
            self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) -> R:
        return obj

