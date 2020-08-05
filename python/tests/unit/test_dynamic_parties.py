# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import logging
import uuid

import pytest

from dazl import async_network, create, exercise

from .dars import PostOffice


@pytest.mark.asyncio
async def test_parties_can_be_added_after_run_forever(sandbox):
    async with async_network(url=sandbox, dars=PostOffice) as network:
        operator_client = network.aio_new_party()
        party_a_client = network.aio_new_party()
        party_b_client = network.aio_new_party()
        # TODO: Introduce a Party allocation API separate from client creation
        party_c_party = str(uuid.uuid4())

        @operator_client.ledger_ready()
        def operator_ready(event):
            return create('Main.PostmanRole', {'postman': event.party})

        @operator_client.ledger_created('Main.PostmanRole')
        def operator_role_created(event):
            return [exercise(event.cid, 'InviteParticipant', {'party': party, 'address': 'whatevs'})
                    for party in (party_a_client.party, party_b_client.party, party_c_party)]

        @party_a_client.ledger_created('Main.InviteAuthorRole')
        async def party_a_accept_invite(_):
            party_c = network.aio_party(party_c_party)

            @party_c.ledger_created('Main.AuthorRole')
            def party_c_role_created(_):
                network.shutdown()

            cid, cdata = await party_c.find_one('Main.InviteAuthorRole')
            party_c.submit_exercise(cid, 'AcceptInviteAuthorRole')

        network.start()

