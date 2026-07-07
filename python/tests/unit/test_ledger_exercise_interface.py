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
            "b63a45646c1a1ecbaf7bf44fd43e09912ac55b35f6251f94de1aaf4857b36cef:KitchenSink.Warehouse:Warehouse",
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
            choice_interface_id="12d68fcdc815c7953a4275121b703b1d4d7e2199e0f8026ff69506efbe630c2b:KitchenSink.Interfaces.HasLocation:HasLocation",
        )
        assert location == response.result
