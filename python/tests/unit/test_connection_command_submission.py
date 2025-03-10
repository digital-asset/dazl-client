# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

from dazl.ledger import CreateEvent
from dazl.testing import SandboxLauncher, connect_with_new_party
import pytest
from tests.unit.dars import KitchenSink, SCUModels1, SCUModels2


@pytest.mark.asyncio
async def test_create(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink, admin=True) as p:
        suppliers_party_info = await p.connection.allocate_party()
        await p.connection.create(
            "KitchenSink.Warehouse:Warehouse",
            {
                "warehouse": p.party,
                "suppliers": suppliers_party_info.party,
                "location": "Somewhere",
            },
        )


@pytest.mark.asyncio
async def test_scu_create_and_query(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=SCUModels1, admin=True) as p:
        issuer_party_info = await p.connection.allocate_party()
        await p.connection.create(
            "#AssetModels:Assets:Asset",
            {
                "issuer": issuer_party_info.party,
                "owner": p.party,
                "name": "Someone",
            },
            act_as=[issuer_party_info.party, p.party],
        )

        events_1 = list[CreateEvent]()
        async with p.connection.query("#AssetModels:Assets:Asset") as stream:
            async for event in stream.creates():
                events_1.append(event)
                logging.info("Found a contract after uploading 0.0.1: %s", event.payload)

        await p.connection.upload_package(SCUModels2.read_bytes())

        await p.connection.create(
            "#AssetModels:Assets:Asset",
            {
                "issuer": issuer_party_info.party,
                "owner": p.party,
                "name": "Someone Else",
                "desc": "A description",
            },
            act_as=[issuer_party_info.party, p.party],
        )

        events_2 = list[CreateEvent]()
        async with p.connection.query("#AssetModels:Assets:Asset") as stream:
            async for event in stream.creates():
                events_2.append(event)
                logging.info("Found a contract after uploading 0.0.2: %s", event.payload)

        # we should now have two contracts
        assert len(events_2) == 2


@pytest.mark.asyncio
async def test_exercise_by_key(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink) as p:
        await p.connection.create(
            "KitchenSink.Retailer:Retailer",
            {
                "retailer": p.party,
                "name": "Kitchen Sinks R Us",
                "website": "kitchensinksrus.local",
                "tags": {"map": {}},
            },
        )

        result = await p.connection.exercise_by_key(
            "KitchenSink.Retailer:Retailer",
            "UpdateWebsite",
            p.party,
            {"newWebsite": "kitchensinksrus.com"},
        )

        logging.info("Choice result: %r", result.result)


@pytest.mark.asyncio
async def test_exercise_interface(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink) as p:
        await p.connection.create(
            "KitchenSink.Warehouse:Warehouse",
            {
                "warehouse": p.party,
                "suppliers": p.party,
                "location": "Somewhere Great",
            },
        )

        async with p.connection.query("KitchenSink.Interfaces.HasLocation:HasLocation") as stream:
            async for event in stream.creates():
                cid = event.contract_id

        response = await p.connection.exercise(
            cid.to_interface("KitchenSink.Interfaces.HasLocation:HasLocation"),
            "GetLocation",
            {"party": p.party},
        )

        assert response.result == "Somewhere Great"


@pytest.mark.asyncio
async def test_create_and_exercise(sandbox: SandboxLauncher) -> None:
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink) as p:
        result = await p.connection.create_and_exercise(
            "KitchenSink.Retailer:Retailer",
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
    async with connect_with_new_party(url=sandbox.url, dar=KitchenSink) as p:
        result = await p.connection.create_and_exercise(
            "KitchenSink.Retailer:Order",
            {
                "customer": p.party,
                "payment": 0,
                "retailer": p.party,
                "expedite": False,
            },
            "MarkAsShipped",
        )

        logging.info("Choice result: %r", result.result)
