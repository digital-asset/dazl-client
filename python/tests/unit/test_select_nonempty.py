# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import wait_for, ensure_future
from unittest import TestCase

from dazl import sandbox, exercise, Network, AIOPartyClient
from .dars import Simple


PARTY = 'Operator'
OperatorRole = 'Simple.OperatorRole'
OperatorNotification = 'Simple.OperatorNotification'


class SelectNonEmptyTestCase(TestCase):
    def test_select_template_retrieves_contracts(self):
        seen_notifications = []
        with sandbox(Simple) as proc:
            network = Network()
            network.set_config(url=proc.url)

            party_client = network.aio_party(PARTY)
            party_client.add_ledger_created(OperatorNotification, lambda event: seen_notifications.append(event.cid))
            network.run_until_complete(async_test_case(party_client))

            data = party_client.find_active(OperatorNotification)

        self.assertEqual(len(data), 5)
        self.assertEqual(len(seen_notifications), 8)


async def async_test_case(client: AIOPartyClient):
    await client.ready()

    ensure_future(client.submit_create(OperatorRole, {'operator': PARTY}))

    operator_cid, _ = await client.find_one(OperatorRole)

    ensure_future(client.submit_exercise(operator_cid, 'PublishMany', dict(count=5)))

    # this should actually be a no-op; we're just making sure that calls to ready() that are
    # "too late" are not treated strangely
    await wait_for(client.ready(), timeout=0.1)

    notifications = await client.find_nonempty(OperatorNotification, {'operator': PARTY}, min_count=5)
    contracts_to_delete = []
    for cid, cdata in notifications.items():
        if int(cdata['text']) <= 3:
            contracts_to_delete.append(cid)

    ensure_future(client.submit([exercise(cid, 'Archive') for cid in contracts_to_delete]))

    ensure_future(client.submit_exercise(operator_cid, 'PublishMany', dict(count=3)))
