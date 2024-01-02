# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from asyncio import sleep

from dazl import connect, testing
from dazl.ledger import ActAs, Admin, User
from dazl.ledger.config.access import DamlLedgerApiNamespace
import pytest

from .config import daml_sdk_versions, known_version_2
from .dars import PostOffice


@pytest.mark.asyncio
@pytest.mark.parametrize("daml_sdk_version", daml_sdk_versions())
async def test_v1_token(daml_sdk_version: str) -> None:
    async with testing.sandbox(
        version=daml_sdk_version, use_auth=True, ledger_id="sandbox"
    ) as sandbox:
        token = sandbox.sign_token({DamlLedgerApiNamespace: {"admin": True, "ledgerId": "sandbox"}})
        async with connect(url=sandbox.url, oauth_token=token) as conn:
            # the result of this call is not particularly interesting;
            # we just need to make sure it doesn't crash
            await conn.list_package_ids()
            await sleep(1)


@pytest.mark.asyncio
async def test_v2_token() -> None:
    async with testing.sandbox(
        version=known_version_2, use_auth=True, ledger_id="sandbox"
    ) as sandbox:
        # use an anonymous admin Daml V1 token to bootstrap users, because that's unfortunately
        # the only way
        token = sandbox.sign_token({DamlLedgerApiNamespace: {"admin": True, "ledgerId": "sandbox"}})
        async with connect(url=sandbox.url, oauth_token=token) as conn:
            p = await conn.allocate_party(identifier_hint="alice", display_name="alice")
            await conn.create_user(User("alice", p.party), [Admin, ActAs(p.party)])
            await conn.upload_package(PostOffice.read_bytes())

        token = sandbox.sign_token({"sub": "alice", "scope": "daml_ledger_api"})
        async with connect(url=sandbox.url, oauth_token=token) as conn:
            # make sure we have admin rights
            await conn.allocate_party()

            # make sure we can create contracts
            await conn.create("Main:PostmanRole", {"postman": p.party})
