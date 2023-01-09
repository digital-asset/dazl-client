# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import ensure_future, wait_for
import datetime
from decimal import Decimal
from typing import Any, Mapping, Optional

from dazl.ledger import ArchiveEvent, CreateEvent
from dazl.ledger.aio import Connection
from dazl.prim import ContractData
from dazl.testing import SandboxLauncher, connect_with_new_party
import pytest

from .dars import AllKindsOf

TEMPLATE = "AllKindsOf:OneOfEverything"
SOME_ARGS: Mapping[str, Any] = dict(
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
    someUglyNesting=dict(
        Both=dict(Left=dict(left=dict(left=1, right=2), right=dict(left=3, right=4)))
    ),
    someMeasurement=Decimal(10.0),
    someEnum="Green",
    theUnit=dict(),
)


@pytest.mark.asyncio
async def test_all_types(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=AllKindsOf) as p:
        # start a reader that makes sure a create occurs, sends an archive choice,
        # and then waits for that archive event to appear.
        fut = ensure_future(consume_singular_event(p.connection))
        await p.connection.create(TEMPLATE, {**SOME_ARGS, "operator": p.party})

        # this really shouldn't take long
        cdata = await wait_for(fut, timeout=1)

    assert cdata is not None, "Expected to find an instance of OneOfEverything!"
    assert SOME_ARGS.keys() == cdata.keys(), "There are either extra fields or missing fields!"

    for key in SOME_ARGS:
        if key != "operator":
            expected = SOME_ARGS.get(key)
            actual = cdata.get(key)
            assert expected == actual, f"Failed to compare types for key: {key}"


@pytest.mark.asyncio
async def test_maps(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=AllKindsOf) as p:
        await p.connection.create(
            "AllKindsOf:MappyContract", {"operator": p.party, "value": {"Map_internal": []}}
        )


async def consume_singular_event(conn: Connection) -> Optional[ContractData]:
    cdata = None
    async with conn.stream(TEMPLATE) as stream:
        async for event in stream.items():
            if isinstance(event, CreateEvent):
                cdata = event.payload
                await conn.exercise(event.contract_id, "Accept")
            elif isinstance(event, ArchiveEvent):
                return cdata

    raise RuntimeError("didn't receive the events we expected")
