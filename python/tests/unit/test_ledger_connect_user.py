# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl import connect
from dazl.ledger import ActAs, ReadAs, User
from dazl.testing import SandboxLauncher
import pytest

from .dars import AllParty


@pytest.mark.asyncio
async def test_connect_as_user(sandbox: SandboxLauncher) -> None:
    # Set up an initial connection, and create some contracts. This test uses a sandbox with
    # auth off, which allows us to set up users, parties, and contracts exactly the way we want
    async with connect(url=sandbox.url) as conn:
        await conn.upload_package(AllParty.read_bytes())

        primary_party_info = await conn.allocate_party()
        public_party_info = await conn.allocate_party()
        user = await conn.create_user(
            User("some-user@digitalasset.com", primary_party_info.party),
            [ActAs(primary_party_info.party), ReadAs(public_party_info.party)],
        )

        # specify explicit act-as so we can create a contract with a party that our user
        # will later only have read access on
        await conn.create(
            "AllParty:PrivateContract",
            {"someParty": public_party_info.party},
            act_as=public_party_info.party,
        )

    # make sure that default act-as/read-as rights from the User are picked up
    async with connect(url=sandbox.url, user_id=user.id) as conn:
        contracts = []
        async with conn.query("AllParty:PrivateContract") as stream:
            async for event in stream.creates():
                contracts.append(event.payload)

        # expect to find a contract with our "public party"
        assert len(contracts) == 1

        # expect to be able to create a contract with our primary party,
        # getting the default act-as from our current user
        await conn.create("AllParty:PrivateContract", {"someParty": primary_party_info.party})
