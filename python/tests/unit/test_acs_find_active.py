# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import ensure_future, wait_for

from dazl import AIOPartyClient, async_network, connect
from dazl.ledger import ExerciseCommand
from dazl.testing import SandboxLauncher
import pytest

from .dars import Simple

OperatorRole = "Simple:OperatorRole"
OperatorNotification = "Simple:OperatorNotification"


@pytest.mark.asyncio
async def test_acs_find_active_retrieves_contracts(sandbox: SandboxLauncher) -> None:
    seen_notifications = []

    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()

    async with async_network(url=sandbox.url, dars=Simple) as network:
        client = network.aio_party(party_info.party)
        client.add_ledger_created(
            OperatorNotification, lambda event: seen_notifications.append(event.cid)
        )

        await network.aio_run(async_test_case(client), keep_open=False)

        data = client.find_active(OperatorNotification)

    assert len(data) == 5
    assert len(seen_notifications) == 8


async def async_test_case(client: AIOPartyClient):
    await client.ready()

    ensure_future(client.create(OperatorRole, {"operator": client.party}))

    operator_cid, _ = await client.find_one(OperatorRole)

    ensure_future(client.exercise(operator_cid, "PublishMany", dict(count=5)))

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

    ensure_future(client.submit([ExerciseCommand(cid, "Archive") for cid in contracts_to_delete]))

    ensure_future(client.exercise(operator_cid, "PublishMany", dict(count=3)))
