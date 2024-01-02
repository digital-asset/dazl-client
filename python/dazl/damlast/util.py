# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional, Sequence, Union
import warnings

from .daml_lf_1 import (
    UNIT,
    DefDataType,
    DefValue,
    DottedName,
    Expr,
    Kind,
    ModuleRef,
    PackageRef,
    PrimType,
    Type,
    TypeConName,
    TypeVarWithKind,
    _Name,
)


# noinspection PyShadowingBuiltins
def unpack_arrow_type(type: "Optional[Type]") -> "Sequence[Type]":
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
def pack_arrow_type(types: Sequence[Type]) -> Optional[Type]:
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
def arrow_type(input: Type, output: Type) -> Type:
    """
    Convenience function for constructing a :class:`Type` of ``prim`` that is an abstraction taking
    the input type and returning the output type.
    """
    warnings.warn(
        "arrow_type is deprecated; Use dazl.damlast.daml_types.Arrow instead",
        DeprecationWarning,
        stacklevel=2,
    )
    from .daml_types import Arrow

    return Arrow(input, output)


def list_type(elem_type: Type) -> Type:
    """
    Convenience function for constructing a :class:`Type` of ``prim`` list.
    """
    warnings.warn(
        "list_type is deprecated; Use dazl.damlast.daml_types.List instead",
        DeprecationWarning,
        stacklevel=2,
    )
    from .daml_types import List

    return List(elem_type)


def type_var_with_kind(var: str, type: Kind = Kind(star=UNIT)):
    return TypeVarWithKind(var, type)


def def_value(name: Union[str, Sequence[str]], daml_type: Type, expr: Expr) -> DefValue:
    if isinstance(name, str):
        name = (name,)
    name_with_type = DefValue.NameWithType(name=name, type=daml_type)
    return DefValue(name_with_type, expr, True, False, None)


def package_ref(obj: "Union[ModuleRef, _Name]") -> "PackageRef":
    """
    Return the package ID for a :class:`ModuleRef` or a DAML name.
    """
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of a ModuleRef is changed.
    if isinstance(obj, ModuleRef):
        # noinspection PyProtectedMember
        return obj._package_id
    elif isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return obj._module._package_id
    else:
        raise ValueError(f"Could not extract a package_ref from {obj!r}")


def module_name(obj: "Union[ModuleRef, _Name]") -> "DottedName":
    """
    Return the module name of a :class:`ModuleRef` or a DAML name.
    """
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of ModuleRefs and _Name are changed.
    if isinstance(obj, ModuleRef):
        # noinspection PyProtectedMember
        return obj._module_name
    elif isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return obj._module._module_name
    else:
        raise ValueError(f"Could not extract a module_name from {obj!r}")


def module_ref(obj: "_Name") -> "ModuleRef":
    """
    Return the :class:`ModuleRef` of a DAML name.
    """
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of ModuleRefs and _Name are changed.
    if isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return obj._module
    else:
        raise ValueError(f"Could not extract a module_ref from {obj!r}")


# noinspection PyProtectedMember
def package_local_name(obj: "_Name") -> str:
    """
    Return the name of a DAML object, assuming that the referent exists in the same package as the
    target (i.e., _not_ scoped with a package ID).
    """
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of a ModuleRef is changed.
    if isinstance(obj, _Name):
        name_str = ".".join(obj._name)
        if obj._module._module_name:
            return f"{obj._module._module_name}:{name_str}"
        else:
            return name_str
    else:
        raise ValueError(f"Could not extract a package_local_name from {obj!r}")


def module_local_name(obj: "_Name") -> str:
    """
    Return the name of a DAML object, assuming that the referent exists in the same module as the
    target (i.e., in the same package and in the same module).
    """
    # TODO: Rewrite for dazl 7.0.0 when the internal structure of ModuleRefs and _Name are changed.
    if isinstance(obj, _Name):
        # noinspection PyProtectedMember
        return ".".join(obj._name)
    else:
        raise ValueError(f"Could not extract a module_local_name from {obj!r}")


def is_match(pattern: TypeConName, value: TypeConName) -> bool:
    if pattern == value:
        return True

    pkg = package_ref(pattern)
    name = package_local_name(pattern)

    if pkg == PackageRef("*"):
        return name == "*" or name == package_local_name(value)
    elif pkg == package_ref(value):
        return name == "*"
    else:
        return False


def find_variant_type(dt: "DefDataType", variant: "DefDataType.Fields", constructor: str) -> "Type":
    for fld_metadata in variant.fields:
        if fld_metadata.field == constructor:
            return fld_metadata.type

    raise ValueError(f"{constructor} is not a field of {dt.name}")
