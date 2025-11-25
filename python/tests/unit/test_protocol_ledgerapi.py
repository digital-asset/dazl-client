# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl.testing import SandboxLauncher, connect_with_new_party
import pytest

from .dars import PostOffice


@pytest.mark.asyncio
async def test_protocol_ledger_api(sandbox: SandboxLauncher) -> None:
    # first, administrative stuff--upload the DAR and allocate two parties that we'll use later
    async with connect_with_new_party(url=sandbox.url, dar=PostOffice, party_count=2) as (
        postman,
        p1,
    ):
        event = await postman.connection.create("Main:PostmanRole", {"postman": postman.party})
        result = await postman.connection.exercise(
            event.contract_id, "InviteParticipant", {"party": p1.party, "address": "Somewhere!"}
        )
        logging.info("Result of inviting a participant: %s", result)

        # Stream results for Main:InviteAuthorRole, and then Main:InviteReceiverRole. Then break the
        # stream once we find the first contract.
        #
        # We do NOT use query() here, because in a distributed ledger setting, the result of the
        # postman inviting participants may not yet have been observed by the clients. Instead, use
        # stream() since it remains open until explicitly closed. We break the never-ending iterator
        # as soon as we see one of each contract.
        async with p1.connection.stream("Main:InviteAuthorRole") as stream:
            async for event in stream.creates():
                result = await p1.connection.exercise(event.contract_id, "AcceptInviteAuthorRole")
                logging.info("The result of AcceptInviteAuthorRole: %s", result)
                break

        async with p1.connection.stream("Main:InviteReceiverRole") as stream:
            async for event in stream.creates():
                result = await p1.connection.exercise(event.contract_id, "AcceptInviteReceiverRole")
                logging.info("The result of AcceptInviteReceiverRole: %s", result)
                break

    logging.info("Done!")
