# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.ledger import ActAs, Admin, IdentityProviderAdmin, ReadAs, User
from dazl.testing import SandboxLauncher
import pytest

from dazl import connect


@pytest.mark.asyncio
async def test_ledger_create_user(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()
        await conn.create_user(User("testuser1", party_info.party))


@pytest.mark.asyncio
async def test_ledger_create_user_with_rights(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()
        await conn.create_user(
            User("testuser2", party_info.party),
            [ActAs(party_info.party), ReadAs(party_info.party), Admin, IdentityProviderAdmin],
        )


@pytest.mark.asyncio
async def test_ledger_get_and_create_user(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        user_id = "testuser3"
        party_info = await conn.allocate_party()
        await conn.create_user(User(user_id, party_info.party))
        users = {u.id: u for u in await conn.list_users() if u.id == user_id}
        assert user_id in users


@pytest.mark.asyncio
async def test_user_annotations(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        user_id = "testuser4"
        annotation_key = "annotation_key"
        annotation = "annotation"

        party_info = await conn.allocate_party()
        await conn.create_user(
            User(user_id, party_info.party, annotations={annotation_key: annotation})
        )

        users = {u.id: u for u in await conn.list_users() if u.id == user_id}
        assert user_id in users

        user = users[user_id]

        assert user.annotations is not None
        if user.annotations:
            assert user.annotations.get(annotation_key) == annotation
