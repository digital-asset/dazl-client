# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

from dazl.testing import SandboxLauncher, connect_with_new_party
import pytest
from tests.unit.dars import KitchenSink1, KitchenSink2


@pytest.mark.asyncio
async def test_create(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink1, admin=True) as p:
        suppliers_party_info = await p.connection.allocate_party()
        await p.connection.create(
            "KitchenSink1.Warehouse:Warehouse",
            {
                "warehouse": p.party,
                "suppliers": suppliers_party_info.party,
                "location": "Somewhere",
            },
        )


@pytest.mark.asyncio
async def test_exercise_by_key(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink1) as p:
        await p.connection.create(
            "KitchenSink1.Retailer:Retailer",
            {
                "retailer": p.party,
                "name": "Kitchen Sinks R Us",
                "website": "kitchensinksrus.local",
                "tags": {"map": {}},
            },
        )

        result = await p.connection.exercise_by_key(
            "KitchenSink1.Retailer:Retailer",
            "UpdateWebsite",
            p.party,
            {"newWebsite": "kitchensinksrus.com"},
        )

        logging.info("Choice result: %r", result.result)


@pytest.mark.asyncio
async def test_exercise_interface(sandbox_v2: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox_v2.url, dar=KitchenSink2) as p:
        await p.connection.create(
            "KitchenSink2.Warehouse:Warehouse",
            {
                "warehouse": p.party,
                "suppliers": p.party,
                "location": "Somewhere Great",
            },
        )

        async with p.connection.query("KitchenSink2.Interfaces.HasLocation:HasLocation") as stream:
            async for event in stream.creates():
                cid = event.contract_id

        response = await p.connection.exercise(
            cid.to_interface("KitchenSink2.Interfaces.HasLocation:HasLocation"),
            "GetLocation",
            {"party": p.party},
        )

        assert response.result == "Somewhere Great"


@pytest.mark.asyncio
async def test_create_and_exercise(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink1) as p:
        result = await p.connection.create_and_exercise(
            "KitchenSink1.Retailer:Retailer",
            {
                "retailer": p.party,
                "name": "Kitchen Sinks R Us",
                "website": "kitchensinksrus.local",
                "tags": {"map": {}},
            },
            "UpdateWebsite",
            {"newWebsite": "kitchensinksrus.com"},
        )

        logging.info("Choice result: %r", result.result)


@pytest.mark.asyncio
async def test_create_and_exercise_unit_arg(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink1) as p:
        result = await p.connection.create_and_exercise(
            "KitchenSink1.Retailer:Order",
            {
                "customer": p.party,
                "payment": 0,
                "retailer": p.party,
                "expedite": False,
            },
            "MarkAsShipped",
        )

        logging.info("Choice result: %r", result.result)
