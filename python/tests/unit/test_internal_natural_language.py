# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime, timedelta, timezone

from dazl.util.prim_natural import parse_datetime

MY_TIMEZONE = timezone(timedelta(hours=10), name='Spamland')
MOCK_NOW = lambda: datetime(2016, 6, 25, 12, 0, 0, tzinfo=MY_TIMEZONE)


def test_today_time_local():
    expected = datetime(2016, 6, 25, 13, 0, tzinfo=MY_TIMEZONE)
    actual = parse_datetime('13:00', now_fn=MOCK_NOW)
    assert expected == actual


def test_today_time_utc():
    expected = datetime(2016, 6, 25, 13, 0, tzinfo=timezone.utc)
    actual = parse_datetime('13:00Z', now_fn=MOCK_NOW)
    assert expected == actual
