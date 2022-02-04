# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import ensure_future, gather, sleep

import dazl
from dazl.prim import ContractData, Party
import pytest
from tests.unit import dars

TEMPLATE = "Simple:OperatorNotification"


def payload(operator: Party, text: str) -> ContractData:
    return {"operator": operator, "theObservers": [], "text": text}


@pytest.mark.asyncio
async def test_stream_with_initial_state_and_early_punchout(sandbox) -> None:
    async with dazl.connect(url=sandbox, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(), conn.upload_package(dars.Simple.read_bytes())
        )

    # start a separate coroutine for injecting data into the ledger
    async with dazl.connect(url=sandbox, act_as=party_info.party) as conn:
        texts = ["Red", "Red", "Green", "Blue", "Blue", "Blue"]
        for text in texts:
            await conn.create(TEMPLATE, payload(party_info.party, text))

        some_texts = await first_three(conn)
        assert some_texts == texts[:3]


@pytest.mark.asyncio
async def test_stream_with_no_initial_state_and_early_punchout(sandbox) -> None:
    async with dazl.connect(url=sandbox, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(), conn.upload_package(dars.Simple.read_bytes())
        )

    async with dazl.connect(url=sandbox, act_as=party_info.party) as conn:
        # kick off the scanning of three elements _before_ the ledger has any data in it
        fut = ensure_future(first_three(conn))

        # continue onwards, injecting data into the ledger
        texts = ["Red", "Red", "Green", "Blue", "Blue", "Blue"]
        for text in texts:
            await conn.create(TEMPLATE, payload(party_info.party, text))
            await sleep(0.1)

    some_texts = await fut
    assert some_texts == texts[:3]


async def first_three(conn):
    events = []
    async with conn.stream(TEMPLATE) as stream:
        async for event in stream.creates():
            events.append(event.payload["text"])
            if len(events) == 3:
                # punch out of the stream before we've consumed everything;
                # this should cleanly abort the stream
                return events
