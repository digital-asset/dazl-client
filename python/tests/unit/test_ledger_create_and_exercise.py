# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl import connect
from dazl.testing import SandboxLauncher
import pytest

from .dars import PostOffice


@pytest.mark.asyncio
async def test_ledger_create_and_exercise(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        await conn.upload_package(PostOffice.read_bytes())

        party_info = await conn.allocate_party()
        operator = party_info.party
        await conn.create_and_exercise(
            "Main:PostmanRole",
            {"postman": operator},
            "InviteParticipant",
            {"party": operator, "address": "21 Jump Street"},
            act_as=operator,
        )
