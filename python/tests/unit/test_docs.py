# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Note: These tests are not currently run since they hardcode URLs for documentation purposes.
# But at the very least, they _are_ typechecked.

from __future__ import annotations

import pytest


@pytest.mark.asyncio
@pytest.mark.skip("typecheck only")
async def test_send_single_command() -> None:
    import dazl

    async with dazl.connect(url="http://localhost:6865", act_as=dazl.Party("Alice")) as conn:
        payload = {"issuer": "Alice", "owner": "Alice", "name": "hello world!"}
        await conn.create("Main:Asset", payload)


@pytest.mark.asyncio
@pytest.mark.skip("typecheck only")
async def test_read() -> None:
    import dazl

    async with dazl.connect(url="http://localhost:6865", read_as=dazl.Party("Alice")) as conn:
        contracts = {}
        async with conn.query("Main:Asset") as stream:
            async for event in stream.creates():
                contracts[event.contract_id] = event.payload
    print(contracts)


@pytest.mark.asyncio
@pytest.mark.skip("typecheck only")
async def test_read_using_callback() -> None:
    import dazl

    async with dazl.connect(url="http://localhost:6865", read_as=dazl.Party("Alice")) as conn:
        contracts = {}
        async with conn.query("Main:Asset") as stream:

            @stream.on_create
            def _(event):
                contracts[event.contract_id] = event.payload

            await stream.run()
    print(contracts)
