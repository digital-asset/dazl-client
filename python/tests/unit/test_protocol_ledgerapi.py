# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl import connect
import pytest

from .dars import PostOffice


@pytest.mark.asyncio
async def test_protocol_ledger_api(sandbox):
    # first, administrative stuff--upload the DAR and allocate two parties that we'll use later
    async with connect(url=sandbox, admin=True) as conn:
        await conn.upload_package(PostOffice.read_bytes())
        postman = (await conn.allocate_party()).party
        participant = (await conn.allocate_party()).party

    async with connect(url=sandbox, act_as=postman) as conn:
        event = await conn.create("Main:PostmanRole", {"postman": postman})
        result = await conn.exercise(
            event.contract_id, "InviteParticipant", {"party": participant, "address": "Somewhere!"}
        )
        logging.info("Result of inviting a participant: %s", result)

    async with connect(url=sandbox, act_as=participant) as conn:
        # Stream results for Main:InviteAuthorRole, and then Main:InviteReceiverRole. Then break the
        # stream once we find the first contract.
        #
        # We do NOT use query() here, because in a distributed ledger setting, the result of the
        # postman inviting participants may not yet have been observed by the clients. Instead, use
        # stream() since it remains open until explicitly closed. We break the never-ending iterator
        # as soon as we see one of each contract.
        async with conn.stream("Main:InviteAuthorRole") as query:
            async for event in query:
                result = await conn.exercise(event.contract_id, "AcceptInviteAuthorRole")
                logging.info("The result of AcceptInviteAuthorRole: %s", result)
                break

        async with conn.stream("Main:InviteReceiverRole") as query:
            async for event in query:
                result = await conn.exercise(event.contract_id, "AcceptInviteReceiverRole")
                logging.info("The result of AcceptInviteReceiverRole: %s", result)
                break

    logging.info("Done!")
