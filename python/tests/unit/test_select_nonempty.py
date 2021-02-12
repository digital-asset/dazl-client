# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import ensure_future, wait_for

import pytest

from dazl import AIOPartyClient, async_network, exercise

from .dars import Simple

OperatorRole = "Simple:OperatorRole"
OperatorNotification = "Simple:OperatorNotification"


@pytest.mark.asyncio
async def test_select_template_retrieves_contracts(sandbox):
    seen_notifications = []

    async with async_network(url=sandbox, dars=Simple) as network:
        client = network.aio_new_party()
        client.add_ledger_created(
            OperatorNotification, lambda event: seen_notifications.append(event.cid)
        )

        await network.aio_run(async_test_case(client), keep_open=False)

        data = client.find_active(OperatorNotification)

    assert len(data) == 5
    assert len(seen_notifications) == 8


async def async_test_case(client: AIOPartyClient):
    await client.ready()

    ensure_future(client.submit_create(OperatorRole, {"operator": client.party}))

    operator_cid, _ = await client.find_one(OperatorRole)

    ensure_future(client.submit_exercise(operator_cid, "PublishMany", dict(count=5)))

    # this should actually be a no-op; we're just making sure that calls to ready() that are
    # "too late" are not treated strangely
    await wait_for(client.ready(), timeout=0.1)

    notifications = await client.find_nonempty(
        OperatorNotification, {"operator": client.party}, min_count=5
    )
    contracts_to_delete = []
    for cid, cdata in notifications.items():
        if int(cdata["text"]) <= 3:
            contracts_to_delete.append(cid)

    ensure_future(client.submit([exercise(cid, "Archive") for cid in contracts_to_delete]))

    ensure_future(client.submit_exercise(operator_cid, "PublishMany", dict(count=3)))
