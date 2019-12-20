# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#pylint: disable=invalid-name,missing-docstring,no-self-use
import unittest
from datetime import datetime, timezone

from dazl.model.core import ContractId
from dazl.util.prim_types import to_datetime

DUMMY_TEMPLATE_ID = 'DummyTemplate'


class ContractIdTest(unittest.TestCase):
    def test_contract_id_as_dict_key(self):
        cid_a = ContractId(template_id=DUMMY_TEMPLATE_ID, contract_id='1')
        cid_b = ContractId(template_id=DUMMY_TEMPLATE_ID, contract_id='1')
        test_dict = dict()
        test_dict[cid_a] = 'hello world'

        self.assertEqual(test_dict[cid_b], 'hello world')


class DateTimeTest(unittest.TestCase):
    def test_simple_date_parse(self):
        expected = datetime(2018, 8, 7, 23, 17, 31, 143080, tzinfo=timezone.utc)
        actual = to_datetime('2018-08-07T23:17:31.143080Z')
        assert expected == actual

    def test_simple_date_parse_with_nanos(self):
        expected = datetime(2018, 8, 7, 23, 17, 31, 143080, tzinfo=timezone.utc)
        actual = to_datetime('2018-08-07T23:17:31.143080698Z')
        assert expected == actual
