# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import gather

import dazl
import pytest
from tests.unit import dars


@pytest.mark.asyncio
async def test_ledger_exercise_interface(sandbox) -> None:
    async with dazl.connect(url=sandbox.url, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(),
            conn.upload_package(dars.KitchenSink.read_bytes()),
        )

    async with dazl.connect(url=sandbox.url, act_as=party_info.party) as conn:
        location = "Somewhere Cool, Awesometown"
        ev = await conn.create(
            "491fc00ca86a9119719c8501b88afe93759f803b9551e48840703413e83dadcd:KitchenSink.Warehouse:Warehouse",
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
            choice_interface_id="e7f1cd1bb268c47214b4c62ec70f11b7bbcbd601af4ca0bc03a3eb2a94cbb69c:KitchenSink.Interfaces.HasLocation:HasLocation",
        )
        assert location == response.result
