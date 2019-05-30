# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest

from datetime import datetime, timedelta, timezone

from dazl.util.prim_natural import parse_datetime

MY_TIMEZONE = timezone(timedelta(hours=10), name='Spamland')
MOCK_NOW = lambda: datetime(2016, 6, 25, 12, 0, 0, tzinfo=MY_TIMEZONE)


class DateTimeTest(unittest.TestCase):

    def test_today_time_local(self):
        expected = datetime(2016, 6, 25, 13, 0, tzinfo=MY_TIMEZONE)
        actual = parse_datetime('13:00', now_fn=MOCK_NOW)
        self.assertEqual(expected, actual)

    def test_today_time_utc(self):
        expected = datetime(2016, 6, 25, 13, 0, tzinfo=timezone.utc)
        actual = parse_datetime('13:00Z', now_fn=MOCK_NOW)
        self.assertEqual(expected, actual)
