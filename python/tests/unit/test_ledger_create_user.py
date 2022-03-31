# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from dazl import connect
from dazl.ledger import ActAs, Admin, ReadAs, User
import pytest


@pytest.mark.asyncio
async def test_ledger_create_user(sandbox_v2) -> None:
    async with connect(url=sandbox_v2, admin=True) as conn:
        party_info = await conn.allocate_party()
        await conn.create_user(User("testuser1", party_info.party))


@pytest.mark.asyncio
async def test_ledger_create_user_with_rights(sandbox_v2) -> None:
    async with connect(url=sandbox_v2, admin=True) as conn:
        party_info = await conn.allocate_party()
        await conn.create_user(
            User("testuser2", party_info.party),
            [ActAs(party_info.party), ReadAs(party_info.party), Admin],
        )
