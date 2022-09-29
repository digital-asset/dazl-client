# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl import async_network, connect
from dazl.ledger import CreateCommand
from dazl.testing import SandboxLauncher
import pytest

from .dars import AllParty, PostOffice


@pytest.mark.asyncio
async def test_template_filtering(sandbox: SandboxLauncher) -> None:
    # First, create a few contracts stretching across two DARs and validate that all of those
    # contracts show up in the active contract set. async_network will supply the list of DARs to
    # dazl.
    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()
        party = party_info.party

    async with async_network(url=sandbox.url, dars=[AllParty, PostOffice]) as network:
        client = network.aio_party(party)

        network.start()
        await client.submit(
            [
                CreateCommand("AllParty:PrivateContract", {"someParty": party}),
                CreateCommand("AllParty:PrivateContract", {"someParty": party}),
                CreateCommand("AllParty:PrivateContract", {"someParty": party}),
                CreateCommand("Main:PostmanRole", {"postman": party}),
            ]
        )

        # The ACS should only contain the five contracts we created: one from Post Office, and three
        # from AllKindsOf.
        contracts = client.find_active("*")
        assert len(contracts) == 4

    # Now create a new client to the same sandbox, but with less DARs
    async with async_network(url=sandbox.url, dars=[PostOffice]) as network:
        client = network.aio_party(party)
        network.start()

        await client.ready()

        # The ACS should only contain the two contracts we created that were part of the Post Office
        # model.
        contracts = client.find_active("*")
        assert len(contracts) == 1
