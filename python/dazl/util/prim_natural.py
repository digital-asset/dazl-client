# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime, timezone
from itertools import product
from typing import Callable, Optional


def n_things(count: int, plural_noun: str, singular_noun: Optional[str]=None):
    if count == 1:
        if singular_noun is None:
            return f'1 {plural_noun[0:-1]}'
        else:
            return f'1 {singular_noun}'
    else:
        return f'{count} {plural_noun}'


def parse_datetime(text: str, now_fn: Callable[[], datetime]=datetime.now) -> datetime:
    """
    Parse the given text, accounting for the fact that humans might be typing on the other side.

    :param text: The text to attempt to parse.
    :param now_fn: A function that, when called, provides the current time.
    :return: A ``datetime`` if the string could be parsed.
    """
    now = now_fn()

    dt = _parse_datetime_no_tz(text, now)
    if dt.tzinfo is not None:
        return dt
    elif text.endswith('Z') or text.endswith('z'):
        return dt.replace(tzinfo=timezone.utc)
    else:
        # Strange API, but this is the only safe way to get a local timezone out of the datetime
        # library. We're essentially forcing the returned datetime to carry the same timezone as
        # the current timezone.
        return dt.replace(tzinfo=now.astimezone(tz=now.tzinfo).tzinfo)


def _parse_datetime_no_tz(text: str, now: datetime) -> datetime:
    for combo_format in _ALL_FORMATS:
        try:
            return datetime.strptime(text, combo_format)
        except ValueError:
            pass

    for date_format in _DATE_ONLY_FORMATS:
        try:
            return datetime.strptime(text, date_format)
        except ValueError:
            pass

    for time_format in _TIME_ONLY_FORMATS:
        try:
            return datetime.strptime(text, time_format).replace(year=now.year, month=now.month, day=now.day)
        except ValueError:
            pass

    raise ValueError(f"Couldn't parse {text!r} as a datetime")


_DATE_ONLY_FORMATS = ('%Y-%m-%d', '%Y%m%d', '%y-%m-%d', '%y%m%d')
_TIME_ONLY_FORMATS = tuple(''.join(segments) for segments in product(
    ('%H:%M', '%H:%M:%S', '%H:%M:%S.', '%H:%M:%S.%f', '%I:%M %p', '%I:%M%p', '%I%p'),
    ('', 'Z', 'z', '%z')))

_ALL_FORMATS = [''.join(segments) for segments in product(_DATE_ONLY_FORMATS, (' ', 'T'), _TIME_ONLY_FORMATS)]
