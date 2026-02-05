# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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
            "d569ba2714c454798962a9d0f587ffaacb09c3678a35976ba0c6795e2de5849a:KitchenSink.Warehouse:Warehouse",
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
            choice_interface_id="fd14df1934c157b3f9a2cc0c1f70a3f12019538314d08cb7bd7c60e73079db04:KitchenSink.Interfaces.HasLocation:HasLocation",
        )
        assert location == response.result
