# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
DAML Types
----------

Constants and constructor functions for the various primitive DAML types.
"""
from typing import Mapping

from .daml_lf_1 import FieldWithType, PrimType, Type, TypeConName, TypeSynName

__all__ = [
    # Type.Var
    "var",
    # Type.Con
    "con",
    # Type.Prim
    "Unit",
    "Bool",
    "Int",
    "Decimal",
    "Text",
    "Time",
    "Party",
    "List",
    "Update",
    "Scenario",
    "Date",
    "ContractId",
    "Optional",
    "Arrow",
    "TextMap",
    "Numeric",
    "Any",
    "TypeRep",
    "Map",
    # Type.Struct
    "struct",
    # Type.ForAll (intentionally omitted)
    # Type.Syn
    "syn",
]


# region Variables (Type.Var)


def var(a: str, *args: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``a`` (a type variable of the specified
    name).
    """
    return Type(var=Type.Var(a, args=tuple(args)))


# endregion

# region Constructors (Type.Con)


def con(tycon: "TypeConName", *args: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is a reference to a :class:`DefDataType` (a record, variant,
    or enum).

    :param tycon: The fully-qualified name of the type constructor.
    :param args: Type arguments (only applicable if the type is a generic type).
    """
    if tycon is None:
        raise ValueError("tycon is required")

    return Type(con=Type.Con(tycon=tycon, args=tuple(args)))


# endregion

# region Primitive types (Type.Prim)


def _prim_type(pt: "PrimType", *a: "Type") -> "Type":
    return Type(prim=Type.Prim(prim=pt, args=tuple(a)))


# DAML's unit type (``()``).
Unit = _prim_type(PrimType.UNIT)

# DAML's boolean type (``Bool``).
Bool = _prim_type(PrimType.BOOL)

# DAML's 64-bit integer type (``Int``).
Int = _prim_type(PrimType.INT64)

# DAML's historical decimal type (``Decimal``). You should generally use :func:`Numeric`(10)
# instead, which means the same thing.
Decimal = _prim_type(PrimType.DECIMAL)

# DAML's text type (``Text``).
Text = _prim_type(PrimType.TEXT)

# DAML's datetime type (``Time``).
Time = _prim_type(PrimType.TIMESTAMP)

# DAML's Party type (``Party``).
Party = _prim_type(PrimType.PARTY)


# noinspection PyPep8Naming
def List(a: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``[a]`` (a list of objects).
    """
    return Type(prim=Type.Prim(PrimType.LIST, args=(a,)))


# noinspection PyPep8Naming
def Update(a: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``Update a``.

    This type is not normally used in ``dazl`` since we are primarily concerned with serializable
    types; it is included for completeness.
    """
    return Type(prim=Type.Prim(PrimType.UPDATE, args=(a,)))


# noinspection PyPep8Naming
def Scenario(a: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``Scenario a``.

    This type is not normally used in ``dazl`` since we are primarily concerned with serializable
    types; it is included for completeness.
    """
    return Type(prim=Type.Prim(PrimType.SCENARIO, args=(a,)))


# DAML's Date type (``Date``).
Date = _prim_type(PrimType.DATE)


# noinspection PyPep8Naming
def ContractId(a: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``ContractId a``.

    No checking is done to verify that the argument refers to a valid template.
    """
    return Type(prim=Type.Prim(PrimType.CONTRACT_ID, args=(a,)))


# noinspection PyPep8Naming
def Optional(a: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``Optional a`` (either ``Some a`` or
    ``None``).
    """
    return Type(prim=Type.Prim(PrimType.OPTIONAL, args=(a,)))


# noinspection PyPep8Naming
def Arrow(a: "Type", b: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``a -> b`` (a function type).

    This type is not normally used in ``dazl`` since we are primarily concerned with serializable
    types; it is included for completeness.
    """
    return _prim_type(PrimType.ARROW, a, b)


# noinspection PyPep8Naming
def TextMap(a: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``TextMap a``.
    """
    return _prim_type(PrimType.TEXTMAP, a)


# noinspection PyPep8Naming
def Numeric(n: int) -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``Numeric n``.
    """
    return _prim_type(PrimType.NUMERIC, Type(nat=n))


# DAML's DA.Internal.LF.Any type.
#
# This type is not normally used in ``dazl`` since we are primarily concerned with serializable
# types; it is included for completeness.
Any = _prim_type(PrimType.ANY)

# DAML's DA.Internal.LF.TypeRep type.
#
# This type is not normally used in ``dazl`` since we are primarily concerned with serializable
# types; it is included for completeness.
TypeRep = _prim_type(PrimType.TYPE_REP)


# noinspection PyPep8Naming
def Map(k: "Type", v: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is equivalent to ``Map k v``.
    """
    return _prim_type(PrimType.GENMAP, k, v)


# endregion

# region Type.Forall

# A forall convenience constructor function is intentionally omitted.

# endregion

# region Type.Struct


def struct(fields: "Mapping[str, Type]"):
    """
    Construct a DAML :class:`Type` that is equivalent to a structural tuple type (``(a, b, ...)``).

    :param fields:
        A map of field names to their types. DAML-LF structs generally define structs as having
        field names ``"_1"``, ``"_2"``, ``"_3"``, and so on.
    """
    return Type(
        struct=Type.Struct(
            fields=tuple([FieldWithType(field, typ) for field, typ in fields.items()])
        )
    )


# endregion

# region Type.Syn


def syn(tysyn: "TypeSynName", *args: "Type") -> "Type":
    """
    Construct a DAML :class:`Type` that is a reference to another type.

    :param tysyn: The fully-qualified name of the type synonym.
    :param args: Type arguments (only applicable if the type is a generic type).
    """
    return Type(syn=Type.Syn(tysyn=tysyn, args=tuple(args)))


# endregion
