# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any

from ..model.core import ContractId
from ..model.types import Type, UnsupportedType, VariantType, RecordType, ListType, \
    ContractIdType, TemplateChoice, TypeEvaluationContext, OptionalType, MapType, \
    UnresolvedTypeReference, TypeReference
from ..model.writing import Command, CreateCommand, ExerciseCommand, ExerciseByKeyCommand, \
    CreateAndExerciseCommand, AbstractSerializer
from ..util.prim_types import to_int, to_str, to_decimal, to_date, to_datetime, \
    unflatten_dotted_keys, to_hashable


class ValidateError(ValueError):
    pass


class ValidateSerializer(AbstractSerializer[Command, Any]):
    """
    A serializer that doesn't actually write to an on-wire form, but merely does lightweight
    conversion and give on-wire serialization the best chance of succeeding.

    This class essentially handles type conversion before a command is fully created and sent to
    a background thread for eventual writing to the Ledger API.
    """

    def serialize_create_command(self, template_type: RecordType, template_args: Any) \
            -> CreateCommand:
        return CreateCommand(template=template_type, arguments=template_args)

    def serialize_exercise_command(
            self, contract_id: ContractId, choice_info: TemplateChoice, choice_args: Any) \
            -> ExerciseCommand:
        if isinstance(contract_id.template_id, UnresolvedTypeReference):
            tref = next(iter(self.store.resolve_template_type(contract_id.template_id)))
            contract_id = ContractId(contract_id.contract_id, template_id=tref)

        return ExerciseCommand(contract=contract_id, choice=choice_info.name, arguments=choice_args)

    def serialize_exercise_by_key_command(
            self, template_ref: TypeReference, key_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> ExerciseByKeyCommand:
        return ExerciseByKeyCommand(
            template=template_ref, contract_key=key_arguments,
            choice=choice_info.name, choice_argument=choice_arguments)

    def serialize_create_and_exercise_command(
            self, template_type: RecordType, create_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> CreateAndExerciseCommand:
        return CreateAndExerciseCommand(
            template=template_type, arguments=create_arguments,
            choice=choice_info.name, choice_arguments=choice_arguments)

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return obj

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> Any:
        from ..protocols.v1.pb_parse_event import to_bool
        return to_bool(obj)

    def serialize_text(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return to_str(obj)

    def serialize_int(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return to_int(obj)

    def serialize_decimal(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return to_decimal(obj)

    def serialize_party(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return to_str(obj)

    def serialize_date(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return to_date(obj)

    def serialize_datetime(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return to_datetime(obj)

    def serialize_timedelta(self, context: TypeEvaluationContext, obj: Any) -> Any:
        return obj

    def serialize_contract_id(self, context: TypeEvaluationContext, tt: ContractIdType, obj: Any) \
            -> Any:
        return obj

    def serialize_optional(self, context: TypeEvaluationContext, tt: OptionalType, obj: Any) -> Any:
        # a `None` object is, of course, a valid Optional
        if obj is None:
            return None

        # any other object is considered in the context of its inner type
        return self._serialize_dispatch(context.append_path('?'), tt.type_parameter, obj)

    def serialize_list(self, context: TypeEvaluationContext, tt: ListType, obj: Any) -> Any:
        # a `None` object is trivially interpreted as an empty list
        if obj is None:
            return []

        if isinstance(obj, str):
            # Strings are a bit special because they're enumerable, but we don't really want to
            # treat them that way here. Additionally, if this is a bare string with commas in it,
            # use those commas to split the string. Additionally, if it's the empty string, treat
            # that as a null list instead of a single list with an empty string inside of it.
            obj = obj.split(',') if obj else []

        from collections import Collection
        if not isinstance(obj, Collection):
            obj = [obj]

        return [self._serialize_dispatch(context.append_path(f'[{i}]'), tt.type_parameter, item)
                for i, item in enumerate(obj)]

    def serialize_map(self, context: TypeEvaluationContext, tt: MapType, obj: Any) -> Any:
        if obj is None:
            return {}

        from collections import Mapping
        if isinstance(obj, Mapping):
            reformatted = {}
            for i, (key, value) in enumerate(obj.items()):
                new_key = to_hashable(self._serialize_dispatch(
                    context.append_path(f'[key {i}]'), tt.key_type, key))
                new_value = to_hashable(self._serialize_dispatch(
                    context.append_path(f'[value {i}]'), tt.value_type, value))
                reformatted[new_key] = new_value
            return reformatted
        else:
            raise ValueError(f'expected a dict here (got {type(obj)}: {obj!r} instead)')

    def serialize_record(self, context: TypeEvaluationContext, tt: RecordType, obj: Any) -> Any:
        from collections.abc import Mapping
        if isinstance(obj, Mapping):
            # pull out any specialized dotted-field mappings
            reformatted = unflatten_dotted_keys(obj)
            missing_keys = set()
            for name, field_type in tt.named_args:
                if name in reformatted:
                    new_value = self._serialize_dispatch(
                        context.append_path(name), field_type, reformatted[name])
                    reformatted[name] = new_value
                else:
                    missing_keys.add(name)
            if missing_keys:
                raise ValueError(f'missing entries in a record: {sorted(missing_keys)}')
            return reformatted
        else:
            raise ValueError(f'expected a dict at {".".join(context.path)}')

    def serialize_variant(self, context: TypeEvaluationContext, tt: VariantType, obj: Any) -> Any:
        from collections import Mapping
        if isinstance(obj, Mapping):
            proposed_variants = {}
            error_variants = {}
            reformatted = unflatten_dotted_keys(obj)
            for name, field_type in tt.named_args:
                if name in reformatted:
                    try:
                        new_value = self._serialize_dispatch(
                            context.append_path(name), field_type, reformatted[name])
                        proposed_variants[name] = new_value
                    except:
                        error_variants[name] = reformatted[name]

            if not proposed_variants:
                raise ValueError('got an empty dict where a single-key dict was expected')
            if len(proposed_variants) == 1:
                return proposed_variants
            else:
                non_optional_ctors = dict()
                optional_ctors = set()
                for name, field_type in tt.named_args:
                    if name in proposed_variants:
                        value = proposed_variants[name]
                        if can_be_optional(field_type, value):
                            optional_ctors.add(name)
                        else:
                            non_optional_ctors[name] = value
                if len(non_optional_ctors) == 1:
                    return non_optional_ctors
                else:
                    raise ValueError(f'too many entries in a variant dict: could not choose among '
                                     f'{sorted(non_optional_ctors)}')
        else:
            error = 'variants must be encoded as dictionaries with a single key and a value'
            raise ValueError(f'{error} (got {obj!r} instead)', obj)

    def serialize_unsupported(self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) \
            -> Any:
        return obj


def can_be_optional(tt: Type, obj: Any):
    from collections import Mapping
    if not obj and obj != 0:
        return True
    if isinstance(obj, Mapping):
        # TODO: For now we're not using type information; might be useful to introduce it at some
        #  point though
        cbo = all(can_be_optional(None, value) for value in obj.values())
        return cbo
    else:
        return False

