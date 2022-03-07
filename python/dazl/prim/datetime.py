# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from functools import partial
from typing import Any, Callable, Sequence, Union

from google.protobuf.duration_pb2 import Duration
from google.protobuf.timestamp_pb2 import Timestamp

__all__ = [
    "DATETIME_ISO8601_Z_FORMAT",
    "DATE_FORMATS",
    "DATETIME_FORMATS",
    "TimeDeltaLike",
    "date_to_int",
    "date_to_str",
    "datetime_to_str",
    "datetime_to_epoch_microseconds",
    "datetime_to_epoch_timedelta",
    "datetime_to_timestamp",
    "timedelta_to_duration",
    "to_date",
    "to_datetime",
    "to_timedelta",
    # these are only exposed until dazl.util.prim_types is removed
    "_parse",
    "_parse_nano_format",
]

TimeDeltaLike = Union[int, float, Decimal, str, timedelta]

DATETIME_ISO8601_Z_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

_NANOS_PER_MICROSECOND = 1000
_SECONDS_PER_DAY = 24 * 3600


def _parse(fmt: str, value: str) -> "datetime":
    return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc)


def _parse_nano_format(value: str) -> "datetime":
    if value.endswith("Z"):
        return _parse(DATETIME_ISO8601_Z_FORMAT, value[0:-4] + "Z")
    else:
        raise ValueError("could not parse")


DATE_FORMATS: Sequence[Callable[[str], datetime]] = [
    partial(_parse, "%Y-%m-%d"),
    partial(_parse, "%Y.%m.%d"),
]

DATETIME_FORMATS: Sequence[Callable[[str], datetime]] = [
    partial(_parse, DATETIME_ISO8601_Z_FORMAT),
    _parse_nano_format,
    partial(_parse, "%Y-%m-%dT%H:%M:%S.%f"),
    partial(_parse, "%Y-%m-%d %H:%M:%S.%f"),
    partial(_parse, "%Y-%m-%dT%H:%M:%SZ"),
    partial(_parse, "%Y-%m-%dT%H:%M:%S"),
    partial(_parse, "%Y-%m-%d %H:%M:%S"),
]


def to_date(obj: "Any") -> date:
    """
    Convert any of the common wire representations of a ``date`` to a ``date``.
    """
    if isinstance(obj, date):
        return obj
    elif isinstance(obj, datetime):
        return obj.date()
    elif isinstance(obj, (int, float)):
        return date(1970, 1, 1) + timedelta(days=obj)
    elif isinstance(obj, str):
        for fmt in DATE_FORMATS:
            try:
                return fmt(obj).date()
            except ValueError:
                pass

    raise ValueError(f"Could not parse as a date: {obj!r}")


def to_datetime(obj: "Any") -> datetime:
    """
    Convert any of the common wire representations of a ``datetime`` to a ``datetime``.
    """
    if isinstance(obj, datetime):
        # trivially return datetime objects untouched
        return obj
    elif isinstance(obj, Timestamp):
        # straight from a Google Timestamp
        dt = obj.ToDatetime()
        return dt.replace(tzinfo=timezone.utc)
    elif isinstance(obj, (int, float)):
        # from the gRPC Ledger API; interpret as microseconds from the GMT epoch
        return datetime.utcfromtimestamp(obj / 1e6).replace(tzinfo=timezone.utc)
    elif isinstance(obj, str):
        # from the REST Ledger API or an end user; give preference to the unambiguous wire
        # format ISO8601, but otherwise try to parse in a variety of formats
        for fmt in DATETIME_FORMATS:
            try:
                return fmt(obj)
            except ValueError:
                pass

    raise ValueError(f"Could not parse as a datetime: {obj!r}")


def to_timedelta(obj: "Any") -> "timedelta":
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
        raise ValueError("obj cannot be None")
    if isinstance(obj, timedelta):
        return obj
    elif isinstance(obj, (int, float)):
        return timedelta(seconds=obj)
    elif isinstance(obj, Decimal):
        return timedelta(seconds=float(obj))
    elif isinstance(obj, str):
        return timedelta(seconds=float(obj))
    else:
        raise TypeError("could not convert {obj!r} to timedelta")


def date_to_int(obj: "date") -> int:
    """
    Return the Python ``datetime.date`` as the number of days since 1970 Jan 1.
    """
    return (obj - date(1970, 1, 1)).days


def date_to_str(obj: "date") -> str:
    """
    Convert a date to a JSON string that represents a date.
    """
    return obj.isoformat()


def datetime_to_str(obj: "datetime") -> str:
    """
    Converts the object to an ISO8601 datetime string.

    :param obj:
        A datetime. If the datetime is "naive" (no timezone information), it is
        assumed to refer to UTC. If the datetime has timezone information, the
        datetime will be converted to UTC before serializing.
    :return: An ISO8601 string that represents the time in UTC.
    """
    if obj.tzinfo is not None and obj.tzinfo.utcoffset(obj) is not None:
        # aware time; translate to UTC
        obj = obj.astimezone(timezone.utc)
    obj = obj.replace(tzinfo=None)
    return obj.isoformat() + "Z"


def datetime_to_timestamp(obj: "datetime") -> "Timestamp":
    """
    Convert the ``datetime`` to a Protobuf ``google.protobuf.Timestamp``.

    :param obj:
        A datetime. If the datetime is "naive" (no timezone information), it is
        assumed to refer to UTC. If the datetime has timezone information, the
        datetime will be converted to UTC before serializing.
    :return: A :class:`Timestamp`.
    """
    td = datetime_to_epoch_timedelta(obj)
    ts = Timestamp()
    ts.seconds = td.seconds + td.days * _SECONDS_PER_DAY
    ts.nanos = td.microseconds * _NANOS_PER_MICROSECOND
    return ts


def datetime_to_epoch_microseconds(obj: "datetime") -> float:
    """
    Return the Python ``datetime.datetime`` as number of microseconds since
    1970 Jan 1 midnight, UTC.
    """
    td = datetime_to_epoch_timedelta(obj)
    return (td.days * 86400 + td.seconds) * 10**6 + td.microseconds


def datetime_to_epoch_timedelta(obj: "datetime") -> "timedelta":
    """
    Return the Python ``datetime.datetime`` as an elapsed time from
    1970 Jan 1 midnight, UTC.
    """
    if obj.tzinfo is not None and obj.tzinfo.utcoffset(obj) is not None:
        # aware time; translate to UTC
        obj = obj.astimezone(timezone.utc)
    obj = obj.replace(tzinfo=None)
    return obj - datetime(1970, 1, 1, 0, 0, 0)


def timedelta_to_duration(obj: "timedelta") -> "Duration":
    """
    Return the Python ``timestamp`` as a Protobuf ``google.protobuf.Duration``.
    """
    d = Duration()
    d.seconds = int(obj.total_seconds())
    d.nanos = obj.microseconds * 1000
    return d
