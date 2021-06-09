from asyncio import gather
import logging

from dazl import connect
from dazl.ledgerutil import ACS
from dazl.testing import connect_with_new_party
import pytest

from .dars import PostOffice


@pytest.mark.asyncio
async def test_acs(sandbox):
    async with connect_with_new_party(url=sandbox, dar=PostOffice, party_count=4) as (
        postman,
        p1,
        p2,
        p3,
    ):
        event = await postman.connection.create("Main:PostmanRole", {"postman": postman.party})
        await postman.connection.exercise(
            event.contract_id, "InviteParticipant", {"party": p1.party, "address": "P1"}
        )
        await postman.connection.exercise(
            event.contract_id, "InviteParticipant", {"party": p2.party, "address": "P2"}
        )
        await postman.connection.exercise(
            event.contract_id, "InviteParticipant", {"party": p3.party, "address": "P3"}
        )

        logging.info("Accepting roles...")
        await gather(*[accept_roles(sandbox, party) for party in (p1.party, p2.party, p3.party)])
        logging.info("Roles accepted.")

        async with ACS(postman.connection, {"Main:AuthorRole": {}, "Main:ReceiverRole": {}}) as acs:
            snapshot = acs.read_immediately()

            authors = snapshot.matching_contracts("Main:AuthorRole")
            receivers = snapshot.matching_contracts("Main:ReceiverRole")

            assert 3 == len(authors)
            assert 3 == len(receivers)
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


@pytest.mark.asyncio
async def test_acs_can_async_read(sandbox):
    async with connect_with_new_party(url=sandbox, dar=PostOffice) as p:
        async with ACS(p.connection, {"Main:PostmanRole"}) as acs:
            await acs.read()

    assert True
