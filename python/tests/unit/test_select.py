# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import async_network
from dazl.client.errors import UnknownTemplateWarning
import pytest

from .dars import Simple

OperatorRole = "Simple:OperatorRole"
OperatorNotification = "Simple:OperatorNotification"


@pytest.mark.asyncio
async def test_select_star_retrieves_contracts(sandbox):
    async with async_network(url=sandbox, dars=Simple) as network:
        client = network.aio_new_party()

        network.start()

        await client.create(OperatorRole, {"operator": client.party})

        data = client.find_active("*")

    assert len(data) == 1


@pytest.mark.asyncio
async def test_select_star_on_empty_ledger_retrieves_nothing(sandbox):
    async with async_network(url=sandbox, dars=Simple) as network:
        client = network.aio_new_party()

        network.start()

        data = client.find_active("*")

    assert len(data) == 0


@pytest.mark.asyncio
async def test_select_template_retrieves_contracts(sandbox):
    async with async_network(url=sandbox, dars=Simple) as network:
        client = network.aio_new_party()

        network.start()

        await client.create(OperatorRole, {"operator": client.party})

        data = client.find_active(OperatorRole)

    assert len(data) == 1


@pytest.mark.asyncio
async def test_select_unknown_template_retrieves_empty_set(sandbox):
    async with async_network(url=sandbox, dars=Simple) as network:
        client = network.aio_new_party()

        network.start()

        await client.create(OperatorRole, {"operator": client.party})

        with pytest.warns(UnknownTemplateWarning):
            data = client.find_active("NonExistentModule:NonExistentTemplate")

    assert len(data) == 0


@pytest.mark.asyncio
async def test_select_operates_on_acs_before_event_handlers(sandbox):
    notification_count = 3

    # we expect that, upon each on_created notification of an OperatorNotification contract,
    # when we query the ACS, we get precisely the same number of contracts.
    expected_select_count = notification_count * notification_count
    actual_select_count = 0

    def on_notification_contract(_):
        nonlocal actual_select_count
        actual_select_count += len(client.find_active(OperatorNotification))

    async with async_network(url=sandbox, dars=Simple) as network:
        client = network.aio_new_party()
        client.add_ledger_ready(lambda e: client.create(OperatorRole, {"operator": client.party}))
        client.add_ledger_created(
            OperatorRole, lambda e: client.exercise(e.cid, "PublishMany", dict(count=3))
        )
        client.add_ledger_created(OperatorNotification, on_notification_contract)

        network.start()

    assert actual_select_count == expected_select_count


@pytest.mark.asyncio
async def test_select_reflects_archive_events(sandbox):
    notification_count = 3

    # we expect that, upon each on_created notification of an OperatorNotification contract,
    # when we query the ACS, we get precisely the same number of contracts.
    expected_select_count = notification_count * notification_count
    actual_select_count = 0

    def on_notification_contract(event):
        nonlocal actual_select_count
        actual_select_count += len(event.acs_find_active(OperatorNotification))

    async with async_network(url=sandbox, dars=Simple) as network:
        client = network.aio_new_party()
        client.add_ledger_ready(lambda e: client.create(OperatorRole, {"operator": client.party}))
        client.add_ledger_created(
            OperatorRole, lambda e: client.exercise(e.cid, "PublishMany", dict(count=3))
        )
        client.add_ledger_created(OperatorNotification, lambda e: client.exercise(e.cid, "Archive"))
        client.add_ledger_created(OperatorNotification, on_notification_contract)

        network.start()

        final_select_count = len(client.find_active(OperatorNotification))

    assert actual_select_count == expected_select_count
    assert 0 == final_select_count
