# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import datetime
from decimal import Decimal

import pytest

from dazl import create, async_network
from .dars import AllKindsOf


TEMPLATE = 'AllKindsOf:OneOfEverything'
SOME_ARGS = dict(
    operator=None,  # this is filled in by each of the tests because Party allocation is random
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


@pytest.mark.asyncio
async def test_all_types(sandbox):
    async with async_network(url=sandbox, dars=AllKindsOf) as network:
        client = network.aio_new_party()

        test_case = AllTypesTestCase(client.party)
        client.add_ledger_ready(test_case.create_one_of_everything)
        client.add_ledger_created(TEMPLATE, test_case.on_one_of_everything)

        network.start()

    assert test_case.found_instance is not None, \
        'Expected to find an instance of OneOfEverything!'

    assert SOME_ARGS.keys() == test_case.found_instance.keys(), \
        'There are either extra fields or missing fields!'

    for key in SOME_ARGS:
        if key != 'operator':
            expected = SOME_ARGS.get(key)
            actual = test_case.found_instance.get(key)
            assert expected == actual, f'Failed to compare types for key: {key}'


@pytest.mark.asyncio
async def test_maps(sandbox):
    async with async_network(url=sandbox, dars=AllKindsOf) as network:
        client = network.aio_new_party()

        network.start()

        await client.submit_create('AllKindsOf:MappyContract', {
            'operator': client.party,
            'value': {'Map_internal': []}
        })


class AllTypesTestCase:
    def __init__(self, operator):
        self.operator = operator
        self.found_instance = None
        self.archive_done = False

    def create_one_of_everything(self, _):
        return create(TEMPLATE, {**SOME_ARGS, "operator": self.operator})

    def on_one_of_everything(self, event):
        if event.cdata is not None:
            self.found_instance = event.cdata
            return event.cid.exercise('Accept')
        else:
            self.archive_done = True
