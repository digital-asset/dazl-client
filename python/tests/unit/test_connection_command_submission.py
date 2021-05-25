# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl.testing import connect_with_new_party
import pytest
from tests.unit.dars import KitchenSink


@pytest.mark.asyncio
async def test_create(sandbox):
    async with connect_with_new_party(url=sandbox, dar=KitchenSink, admin=True) as p:
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
async def test_exercise_by_key(sandbox):
    async with connect_with_new_party(url=sandbox, dar=KitchenSink) as p:
        await p.connection.create(
            "KitchenSink.Retailer:Retailer",
            {
                "retailer": p.party,
                "name": "Kitchen Sinks R Us",
                "website": "kitchensinksrus.local",
            },
        )

        result = await p.connection.exercise_by_key(
            "KitchenSink.Retailer:Retailer",
            "UpdateWebsite",
            p.party,
            {"newWebsite": "kitchensinksrus.com"},
        )

        logging.info("Choice result: %r", result.result)
