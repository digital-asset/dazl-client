# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import gather

import dazl
import pytest
from tests.unit import dars


@pytest.mark.asyncio
async def test_query_no_filter(sandbox):
    async with dazl.connect(url=sandbox, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(), conn.upload_package(dars.Simple.read_bytes())
        )

    async with dazl.connect(url=sandbox, act_as=party_info.party) as conn:
        for text in ["Red", "Red", "Green", "Blue", "Blue", "Blue"]:
            await conn.create(
                "Simple:OperatorNotification",
                {"operator": party_info.party, "theObservers": [], "text": text},
            )

        async with conn.query("Simple:OperatorNotification") as stream:
            events = []
            async for event in stream.creates():
                events.append(event)

        assert len(events) == 6

        async with conn.query("Simple:OperatorNotification", {"text": "Red"}) as stream:
            events = []
            async for event in stream.creates():
                events.append(event)

        assert len(events) == 2

        async with conn.query("Simple:OperatorNotification", {"text": "Green"}) as stream:
            events = []
            async for event in stream.creates():
                events.append(event)

        assert len(events) == 1

        async with conn.query("Simple:OperatorNotification", {"text": "Blue"}) as stream:
            events = []
            async for event in stream.creates():
                events.append(event)

        assert len(events) == 3
