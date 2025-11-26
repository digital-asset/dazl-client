# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import asyncio
from datetime import timedelta
import random
from typing import Any

from dazl import Party, connect
from dazl.ledger.aio import Connection
from dazl.testing import SandboxLauncher, sandbox
import pytest

from .dars import Simple


@pytest.mark.asyncio
async def test_early_stream_abort(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url) as conn:
        await conn.upload_package(Simple.read_bytes())
        alice = await conn.allocate_party(identifier_hint="Alice")
        for i in range(100):
            await conn.create(
                "Simple:OperatorNotification",
                {
                    "operator": alice.party,
                    "theObservers": [],
                    "text": f"{random.random()}",
                },
                act_as=alice.party,
            )

        for i in range(10):
            payload = await find_one(conn, alice.party, str(i / 10))


async def find_one(conn: Connection, party: Party, prefix: str) -> Any:
    async with conn.stream("Simple:OperatorNotification", read_as=party) as stream:
        async for ev in stream.creates():
            if ev.payload["text"].startswith(prefix):
                return ev.payload

    return None
