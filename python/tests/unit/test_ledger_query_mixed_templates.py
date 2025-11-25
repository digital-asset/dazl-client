# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.damlast.errors import NameNotFoundError
from dazl.testing import SandboxLauncher
import pytest

from dazl import connect

from .dars import Simple

OperatorRole = "Simple:OperatorRole"
OperatorNotification = "Simple:OperatorNotification"


@pytest.mark.asyncio
async def test_select_star_retrieves_contracts(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        await conn.upload_package(Simple.read_bytes())
        party_info = await conn.allocate_party()

    async with connect(url=sandbox.url, act_as=party_info.party) as conn:
        await conn.create(OperatorRole, {"operator": party_info.party})

        data = []
        async with conn.query("*") as stream:
            async for event in stream.creates():
                data.append(event)

    assert len(data) == 1


@pytest.mark.asyncio
async def test_select_star_on_empty_ledger_retrieves_nothing(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        await conn.upload_package(Simple.read_bytes())
        party_info = await conn.allocate_party()

    async with connect(url=sandbox.url, act_as=party_info.party) as conn:
        data = []
        async with conn.query("*") as stream:
            async for event in stream.creates():
                data.append(event)

    assert len(data) == 0


@pytest.mark.asyncio
async def test_select_template_retrieves_contracts(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        await conn.upload_package(Simple.read_bytes())
        party_info = await conn.allocate_party()

    async with connect(url=sandbox.url, act_as=party_info.party) as conn:
        await conn.create(OperatorRole, {"operator": party_info.party})

        data = []
        async with conn.query(OperatorRole) as stream:
            async for event in stream.creates():
                data.append(event)

    assert len(data) == 1


@pytest.mark.asyncio
async def test_select_different_template_retrieves_no_contracts(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        await conn.upload_package(Simple.read_bytes())
        party_info = await conn.allocate_party()

    async with connect(url=sandbox.url, act_as=party_info.party) as conn:
        await conn.create(OperatorRole, {"operator": party_info.party})

        # intentionally query on a different template than the one we created a contract for
        # above; we expect this to be empty
        data = []
        async with conn.query(OperatorNotification) as stream:
            async for event in stream.creates():
                data.append(event)

    assert len(data) == 0


@pytest.mark.asyncio
async def test_select_unknown_template_throws_error(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        await conn.upload_package(Simple.read_bytes())
        party_info = await conn.allocate_party()

    async with connect(url=sandbox.url, act_as=party_info.party) as conn:
        await conn.create(OperatorRole, {"operator": party_info.party})

        data = []
        with pytest.raises(NameNotFoundError):
            async with conn.query("NonExistentModule:NonExistentTemplate") as stream:
                async for event in stream.creates():
                    data.append(event)

    assert len(data) == 0
