from asyncio import gather
import logging

import pytest

from dazl import connect
from dazl.ledger import Boundary
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
        await gather(*[accept_roles(sandbox, party) for party in parties])

        async with conn.stream_many({"Main:AuthorRole": {}, "Main:ReceiverRole": {}}) as stream:
            authors = ACS.from_stream(stream, "Main:AuthorRole")
            receivers = ACS.from_stream(stream, "Main:ReceiverRole")
            async for item in stream:
                if isinstance(item, Boundary):
                    asnap = authors.snapshot()
                    rsnap = receivers.snapshot()
                    assert len(parties) == len(asnap)
                    assert len(parties) == len(rsnap)
                    logging.info("Authors: %r", asnap)
                    logging.info("Receivers: %r", rsnap)
                    return


async def accept_roles(sandbox, party):
    async with connect(url=sandbox, act_as=party) as conn:
        async with conn.query("Main:InviteAuthorRole") as query:
            async for event in query.creates():
                await conn.exercise(event.contract_id, "AcceptInviteAuthorRole")

        async with conn.query("Main:InviteReceiverRole") as query:
            async for event in query.creates():
                await conn.exercise(event.contract_id, "AcceptInviteReceiverRole")
