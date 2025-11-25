# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import gather, wait_for
import logging

import dazl
from dazl.ledger import Boundary, CreateEvent
from dazl.ledger.aio import Connection
from dazl.ledger.grpc import Connection as GrpcConnection
from dazl.prim import ContractData, Party
from dazl.testing import SandboxLauncher
import pytest
from tests.unit import dars

TEMPLATE = "Simple:OperatorNotification"


def payload(operator: Party, text: str) -> ContractData:
    return {"operator": operator, "theObservers": [], "text": text}


@pytest.mark.asyncio
async def test_query_no_filter(sandbox: SandboxLauncher) -> None:
    async with dazl.connect(url=sandbox.url, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(), conn.upload_package(dars.Simple.read_bytes())
        )

    async with dazl.connect(url=sandbox.url, act_as=party_info.party) as conn:
        texts = ["Red", "Red", "Green", "Blue", "Blue", "Blue"]
        for text in texts:
            await conn.create(TEMPLATE, payload(party_info.party, text))

        # it could be possible for the creates to succeed, but not yet be reflected on the
        # read side; we'll give it as much as 30 seconds before we fail this test
        boundary = await wait_for(wait_for_n_notifications(conn, len(texts)), timeout=30)
        logging.info("Created %s contracts, and our offset is now %s.", len(texts), boundary.offset)

        await conn.create(TEMPLATE, payload(party_info.party, "Yellow"))

        async with conn.query(TEMPLATE, {"text": "Red"}) as stream:
            events = []
            async for event in stream.creates():
                events.append(event)

        assert len(events) == 2

        async with conn.query(TEMPLATE, {"text": "Green"}) as stream:
            events = []
            async for event in stream.creates():
                events.append(event)

        assert len(events) == 1

        async with conn.query(TEMPLATE, {"text": "Blue"}) as stream:
            events = []
            async for event in stream.creates():
                events.append(event)

        assert len(events) == 3

        logging.info("Making sure that our last event made it in...")
        final_offset = await wait_for(wait_for_n_notifications(conn, len(texts) + 1), timeout=30)

        logging.info("Yep it's there, and the final offset is %s", final_offset.offset)

        # offset-based queries only work over the gRPC API
        assert isinstance(conn, GrpcConnection)

        async with conn.query(TEMPLATE, begin_offset=boundary.offset) as stream:
            async for event in stream.creates():
                # only one create is supposed to come after this part in the stream, and that is
                # "Yellow"
                assert event.payload["text"] == "Yellow"


async def wait_for_n_notifications(conn: Connection, n: int) -> Boundary:
    async with conn.stream("Simple:OperatorNotification") as stream:
        event_count = 0
        async for obj in stream:
            if isinstance(obj, CreateEvent):
                event_count += 1
            elif isinstance(obj, Boundary):
                # return the first Boundary object we see after the expected number of CreateEvents
                if event_count >= n:
                    return obj

        raise Exception("unexpected end of stream")
