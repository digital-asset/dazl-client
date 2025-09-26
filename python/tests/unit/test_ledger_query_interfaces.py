# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import gather

import dazl
import pytest
from dazl.testing import SandboxLauncher
from tests.unit import dars
from pathlib import Path



@pytest.mark.asyncio
async def test_query_no_filter(sandbox: SandboxLauncher) -> None:
    async with dazl.connect(url=sandbox.url, admin=True) as conn:
        # party_info, _ = await gather(
        #     conn.allocate_party(), conn.upload_package(dars.KitchenSink.read_bytes())
        # )
        party_info, _ = await gather(
            conn.allocate_party(), conn.upload_package(Path("/Users/dtanabe/Downloads/gambyl-main-impl-3.4.0.dar").read_bytes())
        )

    async with dazl.connect(url=sandbox.url, act_as=party_info.party) as conn:

        async with conn.query('Gambyl.Interface.Gambling.Bet.Cancellation.Service:IBetCancellationService', {}) as stream:
            async for ev in stream.creates():
                print(ev)