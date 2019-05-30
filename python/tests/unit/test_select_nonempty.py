# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from asyncio import wait_for
from unittest import TestCase
from pathlib import Path

from dazl import sandbox, create_client, exercise

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'Simple.daml'
PARTY = 'Operator'
OperatorRole = 'Simple.OperatorRole'
OperatorNotification = 'Simple.OperatorNotification'


class SelectNonEmptyTestCase(TestCase):
    def test_select_template_retrieves_contracts(self):
        seen_notifications = []
        with sandbox(DAML_FILE) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_created(OperatorNotification, lambda cid, cdata: seen_notifications.append(cid))
                client.run_until_complete(async_test_case(party_client))

                data = party_client.select(OperatorNotification)

        self.assertEqual(len(data), 5)
        self.assertEqual(len(seen_notifications), 8)


async def async_test_case(client):
    await client.ready()

    client.submit_create(OperatorRole, {'operator': PARTY})

    operator_cid, _ = await client.select_first(OperatorRole)

    client.submit_exercise(operator_cid, 'PublishMany', dict(count=5))

    # this should actually be a no-op; we're just making sure that calls to ready() that are
    # "too late" are not treated strangely
    await wait_for(client.ready(), timeout=0.1)

    notifications = await client.select_nonempty(OperatorNotification, {'operator': PARTY}, min_count=5)
    contracts_to_delete = []
    for cid, cdata in notifications.items():
        if int(cdata['text']) <= 3:
            contracts_to_delete.append(cid)

    client.submit([exercise(cid, 'Archive') for cid in contracts_to_delete])

    client.submit_exercise(operator_cid, 'PublishMany', dict(count=3))
