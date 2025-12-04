# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl import frozendict
from dazl.testing import SandboxLauncher, connect_with_new_party
import pytest

from .dars import MapSupport


@pytest.mark.asyncio
async def test_map_support(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=MapSupport, admin=True) as p:
        await p.connection.create(
            "MapSupport:Sample",
            {"party": p.party, "mappings": {"65": "A", "97": "a"}, "text": None},
        )

        count = 0
        async with p.connection.query("MapSupport:Sample") as stream:
            async for _ in stream.creates():
                count += 1

        assert count == 1


@pytest.mark.asyncio
async def test_complicated_map_support(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=MapSupport, admin=True) as p:
        await p.connection.create(
            "MapSupport:ComplicatedSample",
            {
                "party": p.party,
                # Note: Python `dict`s are not hashable, so the only way to write this out
                # is to create a special dict as a key
                "keyIsMap": {frozendict(A="b"): "mmm"},
                "keyIsRecord": {frozendict(x=2, y=4): "rrr"},
                "keyIsRecordWithTypeParam": {frozendict(x=2, y=4): "rrr"},
                "keyIsVariant": {frozendict(Apple=""): "ttt"},
            },
        )

        count = 0
        async with p.connection.query("MapSupport:ComplicatedSample") as stream:
            async for _ in stream.creates():
                count += 1

        assert count == 1
