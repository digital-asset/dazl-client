from asyncio import gather
import logging

import pytest

from dazl import connect
from dazl.ledgerutil import ACS

from .dars import PostOffice


@pytest.mark.asyncio
async def test_acs(sandbox):
    parties = []
    async with connect(url=sandbox, admin=True) as conn:
        await conn.upload_package(PostOffice.read_bytes())
        postman = (await conn.allocate_party()).party
        for _ in range(3):
            info = await conn.allocate_party()
            parties.append(info.party)

    async with connect(url=sandbox, act_as=postman) as conn:
        event = await conn.create("Main:PostmanRole", {"postman": postman})
        await gather(
            *[
                conn.exercise(
                    event.contract_id, "InviteParticipant", {"party": party, "address": "P1"}
                )
                for party in parties
            ]
        )
        logging.info("Accepting roles...")
        await gather(*[accept_roles(sandbox, party) for party in parties])
        logging.info("Roles accepted.")

        async with ACS(conn, {"Main:AuthorRole": {}, "Main:ReceiverRole": {}}) as acs:
            snapshot = acs.read_immediately()

            authors = snapshot.matching_contracts("Main:AuthorRole")
            receivers = snapshot.matching_contracts("Main:ReceiverRole")

            assert len(parties) == len(authors)
            assert len(parties) == len(receivers)
            logging.info("Authors: %r", authors)
            logging.info("Receivers: %r", receivers)


async def accept_roles(sandbox, party):
    async with connect(url=sandbox, act_as=party) as conn:
        async with conn.query("Main:InviteAuthorRole") as query:
            async for event in query.creates():
                await conn.exercise(event.contract_id, "AcceptInviteAuthorRole")

        async with conn.query("Main:InviteReceiverRole") as query:
            async for event in query.creates():
                await conn.exercise(event.contract_id, "AcceptInviteReceiverRole")
