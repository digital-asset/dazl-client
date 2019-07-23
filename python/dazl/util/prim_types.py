# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
The :mod:`dazl.util.prim_types` module contains functions for converting arbitrary objects and
on-wire formats to/from canonical Python types.
"""
from decimal import Decimal

from datetime import datetime, timezone, date, timedelta
from functools import partial
from typing import overload, Any, Mapping, Tuple, Union


TimeDeltaConvertible = Union[int, float, Decimal, str, timedelta]

DATETIME_ISO8601_Z_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


@overload
def to_boolean(obj: 'Union[bool, str]') -> bool: ...


@overload
def to_boolean(obj: None) -> None: ...


def to_boolean(obj) -> bool:
    """
    Convert any of the common wire representations of a ``bool`` to a ``bool``.
    """
    if obj is None:
        # noinspection PyTypeChecker
        return None

    if isinstance(obj, bool):
        return obj
    elif isinstance(obj, str):
        lobj = obj.lower().strip()
        if lobj == 'true':
            return True
        elif lobj == 'false':
            return False
        else:
            raise ValueError(f"Could not parse a string as a boolean: {obj!r}")
    raise ValueError(f'Could not parse as a boolean: {obj!r}')


@overload
def to_timedelta(obj: TimeDeltaConvertible) -> timedelta: ...


@overload
def to_timedelta(obj: None) -> None: ...


def to_timedelta(obj) -> timedelta:
    """
    Convert an object to a timedelta. If the object is a timedelta, it is returned; if it is a
    numeric type, the value is interpreted as seconds and that is returned.

    :param obj: The object to convert.
    :return: A timedelta.

    >>> to_timedelta(timedelta(minutes=1, seconds=2))
    timedelta(minutes=1, seconds=2)
    >>> to_timedelta(30)
    timedelta(seconds=30)
    >>> to_timedelta(30.0)
    timedelta(seconds=30)
    >>> to_timedelta(Decimal(30))
    timedelta(seconds=30)
    """
    if obj is None:
        raise ValueError('obj cannot be None')
    if isinstance(obj, timedelta):
        return obj
    elif isinstance(obj, (int, float)):
        return timedelta(seconds=obj)
    elif isinstance(obj, Decimal):
        return timedelta(seconds=float(obj))
    elif isinstance(obj, str):
        return timedelta(seconds=float(obj))
    else:
        raise TypeError('could not convert {obj!r} to timedelta')


class PrimitiveTypeConverter:
    to_boolean = staticmethod(to_boolean)

    def to_int(self, obj: Any) -> int:
        if obj is None:
            # noinspection PyTypeChecker
            return None

        if isinstance(obj, int):
            return obj
        elif isinstance(obj, str):
            return int(obj)
        elif isinstance(obj, Decimal):
            return int(obj)
        raise ValueError(f'Could not parse as an int: {obj!r}')

    def to_decimal(self, obj: Any) -> Decimal:
        """
        Convert any of the common wire representations of a ``Decimal`` to a ``Decimal``.
        """
        if obj is None:
            # noinspection PyTypeChecker
            return None

        if isinstance(obj, Decimal):
            return obj
        elif isinstance(obj, (int, float)):
            return Decimal(str(obj))
        elif isinstance(obj, str):
            return Decimal(obj)
        raise ValueError(f'Could not parse as a Decimal: {obj!r}')

    def to_str(self, obj: Any) -> str:
        if obj is None:
            # noinspection PyTypeChecker
            return None

        if isinstance(obj, str):
            return obj
        else:
            return str(obj)

    def to_date(self, obj: Any) -> date:
        """
        Convert any of the common wire representations of a ``date`` to a ``date``.
        """
        if obj is None:
            # noinspection PyTypeChecker
            return None

        if isinstance(obj, date):
            return obj
        elif isinstance(obj, datetime):
            return obj.date()
        elif isinstance(obj, (int, float)):
            return date(1970, 1, 1) + timedelta(days=obj)
        elif isinstance(obj, str):
            for fmt in _KNOWN_DATE_FORMATS:
                try:
                    return fmt(obj).date()
                except ValueError:
                    pass

        raise ValueError(f'Could not parse as a date: {obj!r}')

    def to_datetime(self, obj: Any) -> datetime:
        """
        Convert any of the common wire representations of a ``datetime`` to a ``datetime``.
        """
        try:
            # noinspection PyPackageRequirements
            from google.protobuf.timestamp_pb2 import Timestamp
        except ImportError:
            # noinspection PyPep8Naming
            Timestamp = None

        if obj is None:
            # noinspection PyTypeChecker
            return None

        if isinstance(obj, datetime):
            # trivially return datetime objects untouched
            return obj
        elif Timestamp is not None and isinstance(obj, Timestamp):
            # straight from a Google Timestamp
            dt = obj.ToDatetime()
            return dt.replace(tzinfo=timezone.utc)
        elif isinstance(obj, (int, float)):
            # from the gRPC Ledger API; interpret as microseconds from the GMT epoch
            return datetime.utcfromtimestamp(obj / 1e6).replace(tzinfo=timezone.utc)
        elif isinstance(obj, str):
            # from the REST Ledger API or an end user; give preference to the unambiguous wire
            # format ISO8601, but otherwise try to parse in a variety of formats
            for fmt in _KNOWN_TIME_FORMATS:
                try:
                    return fmt(obj)
                except ValueError:
                    pass

        raise ValueError(f'Could not parse as a datetime: {obj!r}')

    to_timedelta = staticmethod(to_timedelta)


def decode_variant_dict(obj: Any) -> Tuple[str, Any]:
    if not isinstance(obj, dict):
        raise ValueError(f'cannot coerce {obj!r} to a variant')
    if len(obj) != 1:
        raise ValueError(f'variants must be encoded as single-key dicts (got {obj!r} instead)')
    key = list(obj)[0]
    value = obj.get(key)
    return key, value


def standard_format(fmt, value):
    return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc)


def nano_format(value):
    if value.endswith('Z'):
        return standard_format(DATETIME_ISO8601_Z_FORMAT, value[0:-4] + 'Z')
    else:
        raise ValueError('could not parse')


def unflatten_dotted_keys(m: Mapping[str, Any]):
    if m is None:
        return None

    # pull out any specialized dotted-field mappings
    reformatted = dict()
    for key, value in m.items():
        k1, d, k2 = key.partition('.')
        if d:
            v = reformatted.get(k1)
            if v is None:
                v = dict()
                reformatted[k1] = v
            v[k2] = value
        else:
            reformatted[key] = value

    return reformatted


DEFAULT_TYPE_CONVERTER = PrimitiveTypeConverter()
to_int = DEFAULT_TYPE_CONVERTER.to_int
to_decimal = DEFAULT_TYPE_CONVERTER.to_decimal
to_str = DEFAULT_TYPE_CONVERTER.to_str
to_date = DEFAULT_TYPE_CONVERTER.to_date
to_datetime = DEFAULT_TYPE_CONVERTER.to_datetime


_KNOWN_DATE_FORMATS = [
    partial(standard_format, '%Y-%m-%d'),
    partial(standard_format, '%Y.%m.%d'),
]


_KNOWN_TIME_FORMATS = [
    partial(standard_format, DATETIME_ISO8601_Z_FORMAT),
    nano_format,
    partial(standard_format, '%Y-%m-%dT%H:%M:%S.%f'),
    partial(standard_format, '%Y-%m-%d %H:%M:%S.%f'),
    partial(standard_format, '%Y-%m-%dT%H:%M:%SZ'),
    partial(standard_format, '%Y-%m-%dT%H:%M:%S'),
    partial(standard_format, '%Y-%m-%d %H:%M:%S'),
]


def frozendict(*args, **kwargs):
    """
    Create a :class:`FrozenDict`, a special subclass of `dict` that is immutable and hashable.
    """
    class HackyDict(dict):
        def __hash__(self):
            return 0

        def __delitem__(self, *args, **kwargs):
            raise RuntimeError('frozendicts are immutable')

        def __setitem__(self, key, value):
            raise RuntimeError('frozendicts are immutable')

        def pop(self, *args, **kwargs):
            raise RuntimeError('frozendicts are immutable')

        def popitem(self, *args, **kwargs):
            raise RuntimeError('frozendicts are immutable')

        def setdefault(self, *args, **kwargs):
            raise RuntimeError('frozendicts are immutable')

        def update(self, *args, **kwargs):
            raise RuntimeError('frozendicts are immutable')

        def clear(self, *args, **kwargs):
            raise RuntimeError('frozendicts are immutable')

    return HackyDict(*args, **kwargs)


def to_hashable(obj):
    from collections import Mapping, Collection
    if isinstance(obj, Mapping):
        return frozendict(obj)
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, Collection):
        return tuple(obj)
    else:
        return obj
