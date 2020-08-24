# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Mapping, Optional, Sequence, Union, TYPE_CHECKING
from .daml_lf_1 import DefValue, Expr, ModuleRef, Type, PrimType, Kind, UNIT, TypeVarWithKind, _Name, PackageRef, \
    DottedName

if TYPE_CHECKING:
    from ..model.types import Type as OldType, TypeReference
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


def package_ref(obj: 'Union[ModuleRef, _Name, TypeReference]') -> 'PackageRef':
    """
    Return the package ID for a :class:`ModuleRef` or a DAML name.
    """
    from ..model.types import TypeReference
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of a ModuleRef is changed.
    if isinstance(obj, ModuleRef):
        # noinspection PyProtectedMember
        return obj._package_id
    elif isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return obj._module._package_id
    elif isinstance(obj, TypeReference):
        # noinspection PyProtectedMember
        return obj.con._module._package_id
    else:
        raise ValueError(f"Could not extract a package_ref from {obj!r}")


def module_name(obj: 'Union[ModuleRef, _Name, TypeReference]') -> 'DottedName':
    """
    Return the module name of a :class:`ModuleRef` or a DAML name.
    """
    from ..model.types import TypeReference
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of ModuleRefs and _Name are changed.
    if isinstance(obj, ModuleRef):
        # noinspection PyProtectedMember
        return obj._module_name
    elif isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return obj._module._module_name
    elif isinstance(obj, TypeReference):
        # noinspection PyProtectedMember
        return obj.con._module._module_name
    else:
        raise ValueError(f"Could not extract a module_name from {obj!r}")


def module_ref(obj: 'Union[_Name, TypeReference]') -> 'ModuleRef':
    """
    Return the :class:`ModuleRef` of a DAML name.
    """
    from ..model.types import TypeReference
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of ModuleRefs and _Name are changed.
    if isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return obj._module
    elif isinstance(obj, TypeReference):
        # noinspection PyProtectedMember
        return obj.con._module
    else:
        raise ValueError(f"Could not extract a module_ref from {obj!r}")


def package_local_name(obj: 'Union[_Name, TypeReference]') -> str:
    """
    Return the name of a DAML object, assuming that the referent exists in the same package as the
    target (i.e., _not_ scoped with a package ID).
    """
    from ..model.types import TypeReference
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of a ModuleRef is changed.
    if isinstance(obj, TypeReference):
        obj = obj.con

    if isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return f'{obj._module._module_name}:{".".join(obj._name)}'
    else:
        raise ValueError(f"Could not extract a package_local_name from {obj!r}")


def module_local_name(obj: 'Union[_Name, TypeReference]') -> str:
    """
    Return the name of a DAML object, assuming that the referent exists in the same module as the
    target (i.e., in the same package and in the same module).
    """
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of ModuleRefs and _Name are changed.
    from ..model.types import TypeReference
    if isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return '.'.join(obj._name)
    elif isinstance(obj, TypeReference):
        # noinspection PyProtectedMember
        return '.'.join(obj.con._name)
    else:
        raise ValueError(f"Could not extract a module_local_name from {obj!r}")

