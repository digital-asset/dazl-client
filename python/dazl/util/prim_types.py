# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
The :mod:`dazl.util.prim_types` module contains functions for converting arbitrary objects and
on-wire formats to/from canonical Python types.
"""
from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Any, Mapping, Optional, Tuple, Union, overload
import warnings

from ..prim.datetime import DATETIME_ISO8601_Z_FORMAT, TimeDeltaLike as TimeDeltaConvertible

warnings.warn(
    "dazl.util.prim_types is deprecated; use dazl.prim instead.", DeprecationWarning, stacklevel=2
)

__all__ = [
    "to_boolean",
    "to_str",
    "to_int",
    "to_date",
    "to_datetime",
    "to_decimal",
    "to_ledger_api_decimal",
    "to_timedelta",
    "PrimitiveTypeConverter",
    "decode_variant_dict",
    "standard_format",
    "nano_format",
    "unflatten_dotted_keys",
    "DEFAULT_TYPE_CONVERTER",
    "DATETIME_ISO8601_Z_FORMAT",
    "frozendict",
    "to_hashable",
]


@overload
def to_boolean(obj: "Union[bool, str]") -> bool:
    ...


@overload
def to_boolean(obj: None) -> None:
    ...


def to_boolean(obj):
    from ..prim import to_bool

    warnings.warn(
        "dazl.util.prim_types.to_boolean is deprecated; use dazl.prim.to_bool instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_bool(obj) if obj is not None else None


def to_str(obj: "Optional[Any]") -> "Optional[str]":
    from ..prim import to_str

    warnings.warn(
        "dazl.util.prim_types.to_str is deprecated; use dazl.prim.to_str instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_str(obj) if obj is not None else None


def to_int(obj: Any) -> "Optional[int]":
    from ..prim import to_int

    warnings.warn(
        "dazl.util.prim_types.to_int is deprecated; use dazl.prim.to_int instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_int(obj) if obj is not None else None


def to_date(obj: "Optional[Any]") -> "Optional[date]":
    from ..prim import to_date

    warnings.warn(
        "dazl.util.prim_types.to_date is deprecated; use dazl.prim.to_date instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_date(obj) if obj is not None else None


def to_datetime(obj: "Optional[Any]") -> "Optional[datetime]":
    from ..prim import to_datetime

    warnings.warn(
        "dazl.util.prim_types.to_datetime is deprecated; use dazl.prim.to_datetime instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_datetime(obj) if obj is not None else None


def to_decimal(obj: "Optional[Any]") -> "Optional[Decimal]":
    from ..prim import to_decimal

    warnings.warn(
        "dazl.util.prim_types.to_decimal is deprecated; use dazl.prim.to_decimal instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_decimal(obj) if obj is not None else None


def to_ledger_api_decimal(obj: "Decimal") -> str:
    from ..prim import decimal_to_str

    warnings.warn(
        "dazl.util.prim_types.to_ledger_api_decimal is deprecated; use dazl.prim.decimal_to_str instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return decimal_to_str(obj)


def to_timedelta(obj: TimeDeltaConvertible) -> "timedelta":
    from ..prim import to_timedelta

    warnings.warn(
        "dazl.util.prim_types.to_timedelta is deprecated; use dazl.prim.to_timedelta instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_timedelta(obj)


class PrimitiveTypeConverter:
    to_boolean = staticmethod(to_boolean)
    to_str = staticmethod(to_str)
    to_int = staticmethod(to_int)
    to_decimal = staticmethod(to_decimal)
    to_date = staticmethod(to_date)
    to_datetime = staticmethod(to_datetime)
    to_timedelta = staticmethod(to_timedelta)


def decode_variant_dict(obj: "Any") -> "Tuple[str, Any]":
    from ..prim import to_variant

    warnings.warn(
        "dazl.util.prim_types.decode_variant_dict is deprecated; use dazl.prim.to_variant instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_variant(obj)


def standard_format(fmt, value):
    from ..prim.datetime import _parse

    warnings.warn(
        "dazl.util.prim_types.nano_format is deprecated; there is no replacement.",
        DeprecationWarning,
        stacklevel=2,
    )
    return _parse(fmt, value)


def nano_format(value):
    from ..prim.datetime import _parse_nano_format

    warnings.warn(
        "dazl.util.prim_types.nano_format is deprecated; there is no replacement.",
        DeprecationWarning,
        stacklevel=2,
    )
    return _parse_nano_format(value)


def unflatten_dotted_keys(m: "Mapping[str, Any]"):
    from ..prim import to_record

    warnings.warn(
        "dazl.util.prim_types.unflatten_dotted_keys is deprecated; use dazl.prim.to_record instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_record(m) if m is not None else None


DEFAULT_TYPE_CONVERTER = PrimitiveTypeConverter()


def frozendict(*args, **kwargs):
    from ..prim.map import FrozenDict

    warnings.warn(
        "dazl.util.prim_types.frozendict is deprecated; use dazl.prim.map.FrozenDict instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return FrozenDict(*args, **kwargs)


def to_hashable(*args, **kwargs):
    from ..prim.map import to_hashable

    warnings.warn(
        "dazl.util.prim_types.to_hashable is deprecated; use dazl.prim.map.to_hashable instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return to_hashable(*args, **kwargs)
