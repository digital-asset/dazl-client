# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from dazl import async_network, frozendict

from .dars import MapSupport


@pytest.mark.asyncio
async def test_map_support(sandbox):
    async with async_network(url=sandbox, dars=MapSupport) as network:
        client = network.aio_new_party()

        network.start()

        await client.ready()
        await client.create(
            "MapSupport:Sample",
            {"party": client.party, "mappings": {"65": "A", "97": "a"}, "text": None},
        )

        assert len(client.find_active("*")) == 1


@pytest.mark.skip(
    "Keys with arbitrary types are no longer supported. See the comments in MapSupport.daml."
)
async def test_complicated_map_support(sandbox):
    # This test will be re-enabled when GenMap support lands in DAML-LF 1.9
    async with async_network(url=sandbox, dars=MapSupport) as network:
        client = network.aio_new_party()

        await client.ready()
        await client.create(
            "MapSupport:ComplicatedSample",
            {
                "party": "Test",
                # Note: Python `dict`s are not hashable, so the only way to write this out
                # is to create a special dict as a key
                "keyIsMap": {frozendict(A="b"): "mmm"},
                "keyIsRecord": {frozendict(x=2, y=4): "rrr"},
                "keyIsRecordWithTypeParam": {frozendict(x=2, y=4): "rrr"},
                "keyIsVariant": {frozendict(Apple=""): "ttt"},
            },
        )

        assert len(client.find_active("*")) == 1
