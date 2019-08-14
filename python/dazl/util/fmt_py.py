# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Any, NoReturn

from ..model.core import ContractId
from ..model.types import Type, UnsupportedType, VariantType, RecordType, ListType, TextMapType, \
    ContractIdType, TemplateChoice, TypeEvaluationContext, OptionalType
from ..model.types_store import PackageStore
from ..model.writing import AbstractSerializer


def python_example_object(store: PackageStore, tt: Type) -> str:
    example = PythonExampleSerializer(store)
    return repr(example.serialize_value(tt, None))


class PythonExampleSerializer(AbstractSerializer[Any, Any]):

    def serialize_value(self, tt: Type, obj: Any) -> Any:
        return self._serialize_dispatch(TypeEvaluationContext.from_store(self.store), tt, obj)

    def serialize_create_command(self, template_type: RecordType, template_args: Any) -> NoReturn:
        raise Exception()

    def serialize_exercise_command(self, contract_id: ContractId, choice_info: TemplateChoice,
                                   choice_args: Any) -> NoReturn:
        raise Exception()

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return dict()

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return 'true | false'

    def serialize_text(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return "text-value"

    def serialize_int(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return "int-value"

    def serialize_decimal(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return "decimal-value"

    def serialize_party(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return "party-value"

    def serialize_date(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return "date-value"

    def serialize_datetime(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return "datetime-value"

    def serialize_timedelta(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return "timedelta-value"

    def serialize_contract_id(self, context: TypeEvaluationContext, tt: ContractIdType, obj: Any) \
            -> Any:
        return "contractid-value"

    def serialize_optional(self, context: TypeEvaluationContext, tt: OptionalType, obj: Any):
        if len(context.path) > 6:
            return '...'
        else:
            try:
                item_type = tt.type_parameter
                return self._serialize_dispatch(context, item_type, None)
            except:
                from .. import LOG
                LOG.exception(f'Failed to serialize an optional: {tt}!')
                return '...O'

    def serialize_map(self, context: TypeEvaluationContext, tt: TextMapType, obj: Any) -> Any:
        if len(context.path) > 6:
            return '...'
        else:
            try:
                obj = self._serialize_dispatch(context, tt.value_type, None)
                return {'key1': obj, 'key2': obj}
            except:
                from .. import LOG
                LOG.exception(f'Failed to serialize an optional: {tt}!')
                return '...M'

    def serialize_list(self, context: TypeEvaluationContext, tt: ListType, obj: Any) -> Any:
        if len(context.path) > 6:
            return '...'
        else:
            try:
                item_type = tt.type_parameter
                return [self._serialize_dispatch(context.append_path('[]'), item_type, None)]
            except:
                from .. import LOG
                LOG.exception('Failed to serialize a list!')
                return '...L'

    def serialize_record(self, context: TypeEvaluationContext, tt: RecordType, obj: Any) -> Any:
        if len(context.path) > 6:
            return '...'
        else:
            try:
                return {name: self._serialize_dispatch(context.append_path(field_type), field_type, None) for name, field_type in tt.named_args}
            except:
                from .. import LOG
                LOG.exception(f'Failed to serialize a record: {tt}!')
                return '...R'

    def serialize_variant(self, context: TypeEvaluationContext, tt: VariantType, obj: Any) -> Any:
        if len(context.path) > 6 or context.path.count(tt.name) > 2:
            return '...'
        else:
            try:
                return {name: self._serialize_dispatch(context.append_path(field_type), field_type, None) for name, field_type in tt.named_args}
            except:
                return '...V'

    def serialize_unsupported(self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) \
            -> Any:
        return '<unsupported>'

