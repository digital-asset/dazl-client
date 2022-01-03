# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains helper utilities for working within the constraints of Python's type system.
"""

from types import MappingProxyType
from typing import Any, Dict, Optional, Type, TypeVar

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")


def safe_cast(typ: Type[T], val: Any) -> T:
    """
    Safely casts an item to the specified type. Unlike ``typing.cast``, this method will actually
    throw an exception if types do not match.
    """
    if isinstance(typ, type):
        if isinstance(val, typ):
            return val
        else:
            raise ValueError(f"expected a value of type {typ} here (got {val} instead)")
    else:
        raise Exception(f"safe_cast can only be used with actual types (got {typ})")


def safe_optional_cast(typ: Type[T], val: Any) -> Optional[T]:
    """
    Safely casts an item to the specified type. Unlike ``typing.cast``, this method will actually
    throw an exception if types do not match.
    """
    if val is None:
        return None

    if isinstance(typ, type):
        if isinstance(val, typ):
            return val
        else:
            raise ValueError(f"expected a value of type {typ} here (got {val} instead)")
    else:
        raise Exception("safe_cast can only be used with actual types")


def safe_dict_cast(key_type: Type[K], value_type: Type[V], val: Any) -> Dict[K, V]:
    if isinstance(val, (dict, MappingProxyType)):
        for key, value in val.items():
            safe_cast(key_type, key)
            safe_cast(value_type, value)
        return val  # type: ignore
    else:
        raise ValueError(f"expected a dict (got {val} instead)")


def unpack_optional(typ: Any) -> Optional[Any]:
    """
    Return the single non-``NoneType`` type for an ``Optional[T]`` expression, or ``None`` if the
    given type does not match that pattern.

    :param typ: The type to attempt to unpack.
    :return: The type parameter, or ``None`` if the specified type is not ``Optional``.

    >>> unpack_optional(Optional[int])
    <class 'int'>

    >>> unpack_optional(Union[str, None])
    <class 'str'>

    >>> unpack_optional(Union[Optional[float]])
    <class 'float'>

    >>> unpack_optional(Union[float, None, int])
    """
    # noinspection PyUnresolvedReferences,PyProtectedMember
    try:
        from typing import Union
    except ImportError:
        from typing import _Union as Union  # type: ignore

    if type(typ) is Union:
        type_args = list(typ.__args__)
        if len(type_args) == 2:
            try:
                type_args.remove(type(None))
                return type_args[0]
            except ValueError:
                return None

    return None
