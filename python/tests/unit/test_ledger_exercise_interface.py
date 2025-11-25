# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import gather

import dazl
import pytest
from tests.unit import dars

PKG_ID = "ba10f9b4f711f1528384d2caba51c1a38c1f155f1db1de7d7e9153d42f54d54d"


@pytest.mark.asyncio
async def test_ledger_exercise_interface(sandbox_v2) -> None:
    async with dazl.connect(url=sandbox_v2.url, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(),
            conn.upload_package(dars.KitchenSink2_6.read_bytes()),
        )

    async with dazl.connect(url=sandbox_v2.url, act_as=party_info.party) as conn:
        location = "Somewhere Cool, Awesometown"
        ev = await conn.create(
            PKG_ID + ":KitchenSink.Warehouse:Warehouse",
            {
                "warehouse": party_info.party,
                "suppliers": party_info.party,
                "location": location,
            },
        )

        response = await conn.exercise(
            ev.contract_id,
            "GetLocation",
            {"party": party_info.party},
            choice_interface_id=PKG_ID + ":KitchenSink.Warehouse:HasLocation",
        )
        assert location == response.result
