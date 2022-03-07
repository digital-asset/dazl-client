# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from asyncio import gather

from dazl import async_network, connect
import pytest

from .dars import PostOffice


@pytest.mark.asyncio
async def test_parties_can_be_added_after_run_forever(sandbox):
    async with connect(url=sandbox, admin=True) as conn:
        operator_info = await conn.allocate_party()
        party_a_info = await conn.allocate_party()
        party_b_info = await conn.allocate_party()
        party_c_info = await conn.allocate_party()

    async with async_network(url=sandbox, dars=PostOffice) as network:
        operator_client = network.aio_party(operator_info.party)
        party_a_client = network.aio_party(party_a_info.party)
        party_b_client = network.aio_party(party_b_info.party)

        @operator_client.ledger_ready()
        async def operator_ready(event):
            await operator_client.create("Main:PostmanRole", {"postman": event.party})

        @operator_client.ledger_created("Main:PostmanRole")
        async def operator_role_created(event):
            await gather(
                *[
                    operator_client.exercise(
                        event.cid, "InviteParticipant", {"party": party, "address": "whatevs"}
                    )
                    for party in (party_a_client.party, party_b_client.party, party_c_info.party)
                ]
            )

        @party_a_client.ledger_created("Main:InviteAuthorRole")
        async def party_a_accept_invite(_):
            party_c = network.aio_party(party_c_info.party)

            @party_c.ledger_created("Main:AuthorRole")
            def party_c_role_created(_):
                network.shutdown()

            cid, cdata = await party_c.find_one("Main:InviteAuthorRole")
            await party_c.exercise(cid, "AcceptInviteAuthorRole")

        network.start()
