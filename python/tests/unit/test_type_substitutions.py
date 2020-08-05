# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.model.types import type_ref, TypeReference, RecordType, \
    NamedArgumentList, \
    ListType, TypeVariable, TypeApp, SCALAR_TYPE_TEXT, SCALAR_TYPE_INTEGER, \
    type_evaluate_dispatch_default_error, TypeEvaluationContext
from dazl.model.types_store import PackageStoreBuilder


def record_type(name: TypeReference, type_args, **fields):
    return RecordType(
        named_args=NamedArgumentList((k, v) for k, v in fields.items()),
        name=name,
        type_args=tuple(map(TypeVariable, type_args)))


def list_type(tt):
    return ListType(tt)


def type_var(name):
    return TypeVariable(name)


def test_simple_translate():
    tr = type_ref(f'pkg0::Map')
    tt = type_ref(f'pkg0::Tuple')

    tuple_type = record_type(tt, 'AB', _1=type_var('A'), _2=type_var('B'))
    map_type = record_type(tr, 'KV', _1=list_type(TypeApp(tt, (type_var('K'), type_var('V')))))

    psb = PackageStoreBuilder()
    psb.add_type(tuple_type.name.con, tuple_type)
    psb.add_type(map_type.name.con, map_type)

    test_case_type = TypeApp(tr, (SCALAR_TYPE_INTEGER, SCALAR_TYPE_TEXT))

    def _1(context, actual: RecordType):
        assert 1 == len(actual.named_args)
        type_evaluate_dispatch_default_error(on_list=_2)(context, actual.named_args[0][1])

    def _2(context, inner_list_type: ListType):
        type_evaluate_dispatch_default_error(on_record=_3)(context, inner_list_type.type_parameter)

    def _3(context, inner_tuple_type: RecordType):
        type_evaluate_dispatch_default_error(on_scalar=_4)(context, inner_tuple_type.named_args[0][1])
        type_evaluate_dispatch_default_error(on_scalar=_5)(context, inner_tuple_type.named_args[1][1])

    def _4(context, first_param):
        assert first_param == SCALAR_TYPE_INTEGER

    def _5(context, second_param):
        assert second_param == SCALAR_TYPE_TEXT

    type_evaluate_dispatch_default_error(on_record=_1)(
        TypeEvaluationContext.from_store(psb.build()), test_case_type)
