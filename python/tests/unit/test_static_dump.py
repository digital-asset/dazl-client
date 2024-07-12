# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl import connect
from dazl.testing import SandboxLauncher
import pytest

from .dars import Simple


@pytest.mark.asyncio
async def test_static_dump_and_tail(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()
        await conn.upload_package(Simple.read_bytes())

    async with connect(url=sandbox.url, act_as=party_info.party) as conn:
        seen_contracts = []

        for i in range(0, 5):
            await conn.create(
                "Simple:OperatorNotification",
                {"operator": party_info.party, "theObservers": [], "text": "Something"},
            )

        async with conn.query("Simple:OperatorNotification") as stream:
            async for create in stream.creates():
                seen_contracts.append(create.payload)

    assert len(seen_contracts) == 5
