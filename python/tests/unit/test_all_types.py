# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import datetime
from decimal import Decimal

import unittest

from pathlib import Path

from dazl import sandbox, create, create_client


PARTY = 'Operator'
TEST_DAML = Path(__file__).parent.parent / 'resources' / 'AllKindsOf.daml'
TEMPLATE = 'AllKindsOf.OneOfEverything'
SOME_ARGS = dict(
    operator=PARTY,
    someBoolean=True,
    someInteger=5,
    someDecimal=Decimal(5.0),
    someMaybe=7,
    someMaybeNot=None,
    someText="Really Text",
    someDate=datetime.date(2018, 1, 1),
    someDatetime=datetime.datetime(2018, 1, 1, tzinfo=datetime.timezone.utc),
    someSimpleList=[1, 2, 3],
    someSimplePair=dict(left=1, right=2),
    someNestedPair=dict(left=dict(left=1, right=2), right=dict(left=3, right=4)),
    someUglyNesting=dict(Both=dict(Left=dict(left=dict(left=1, right=2), right=dict(left=3, right=4)))),
    someMeasurement=Decimal(10.0),
    theUnit=dict())


class TestAllTypes(unittest.TestCase):
    def test_all_types(self):
        test_case = AllTypesTestCase()
        with sandbox(TEST_DAML) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(test_case.create_one_of_everything)
                party_client.on_created(TEMPLATE, test_case.on_one_of_everything)
                client.run_until_complete()

        self.assertIsNotNone(
            test_case.found_instance,
            'Expected to find an instance of OneOfEverything!')

        self.assertEqual(
            SOME_ARGS.keys(), test_case.found_instance.keys(),
            'There are either extra fields or missing fields!')

        for key in SOME_ARGS:
            expected = SOME_ARGS.get(key)
            actual = test_case.found_instance.get(key)
            self.assertEqual(expected, actual, f'Failed to compare types for key: {key}')

    def test_maps(self):
        with sandbox(TEST_DAML) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(lambda *args, **kwargs: create(
                    'AllKindsOf.MappyContract', {
                        'operator': PARTY,
                        'value': {'Map_internal': []}
                    }))
                client.run_until_complete()


class AllTypesTestCase:
    def __init__(self):
        self.found_instance = None
        self.archive_done = False

    # noinspection PyUnusedLocal
    @staticmethod
    def create_one_of_everything(*args, **kwargs):
        return create(TEMPLATE, SOME_ARGS)

    def on_one_of_everything(self, cid, cdata):
        if cdata is not None:
            self.found_instance = cdata
            return cid.exercise('Accept')
        else:
            self.archive_done = True
