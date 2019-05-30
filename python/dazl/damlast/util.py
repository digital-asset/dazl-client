# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Mapping, Optional, Sequence, Union
from .daml_lf_1 import DefValue, Expr, Type, PrimType, Kind, VarWithType, UNIT, TypeVarWithKind
from ..model.types import ModuleRef, Type as OldType
from ..model.types_store import PackageStore


STRING = Type(prim=Type.Prim(prim=PrimType.TEXT, args=()))
PARTY_TYPE = Type(prim=Type.Prim(prim=PrimType.PARTY, args=()))


def var(var: str) -> 'Type':
    return Type(var=Type.Var(var, ()))


def values_by_module(store: 'PackageStore') \
        -> 'Mapping[ModuleRef, Mapping[Sequence[str], Union[Expr, OldType]]]':
    from collections import defaultdict
    d = defaultdict(defaultdict)
    for vn, vv in store._value_types.items():
        d[vn.module][vn.name] = vv
    for vn, vv in store._data_types.items():
        d[vn.module][vn.name] = vv
    return d


# noinspection PyShadowingBuiltins
def unpack_arrow_type(type: 'Optional[Type]') -> 'Sequence[Type]':
    """
    Unwind an arrow type the sequence of constituent types.

    If presented with something that is not an arrow type, it is simply returned.
    """
    if type is None:
        return []

    types = []
    next = type
    while True:
        if next.forall is not None:
            next = next.forall.body
        if next.prim is not None and next.prim.prim == PrimType.ARROW:
            types.append(next.prim.args[0])
            next = next.prim.args[1]
        else:
            types.append(next)
            return types


# noinspection PyShadowingBuiltins
def pack_arrow_type(types: 'Sequence[Type]') -> 'Optional[Type]':
    """
    Compute the arrow type that is the result of repeatedly applying values to a function and
    returning it.
    """
    if not types:
        return None

    t = types[-1]
    for type in reversed(types[0:-1]):
        t = arrow_type(type, t)
    return t


# noinspection PyShadowingBuiltins
def arrow_type(input: 'Type', output: 'Type') -> 'Type':
    """
    Convenience function for constructing a :class:`Type` of ``prim`` that is an abstraction taking
    the input type and returning the output type.
    """
    return Type(prim=Type.Prim(PrimType.ARROW, (input, output)))


def list_type(elem_type: 'Type') -> 'Type':
    """
    Convenience function for constructing a :class:`Type` of ``prim`` list.
    """
    return Type(prim=Type.Prim(PrimType.LIST, (elem_type,)))


def type_var_with_kind(var: str, type: Kind = Kind(star = UNIT)):
    return TypeVarWithKind(var, type)


def def_value(name: 'Union[str, Sequence[str]]', daml_type: 'Type', expr: 'Expr') -> 'DefValue':
    if isinstance(name, str):
        name = (name,)
    name_with_type = DefValue.NameWithType(name=name, type=daml_type)
    return DefValue(name_with_type, expr, True, False, None)
