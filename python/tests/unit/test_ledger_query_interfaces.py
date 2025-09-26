# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import gather
from pathlib import Path

import dazl
from dazl.damlast.lookup import MultiPackageLookup
from dazl.testing import SandboxLauncher
import pytest
from tests.unit import dars


@pytest.mark.asyncio
async def test_query_no_package_cache(sandbox: SandboxLauncher) -> None:
    async with dazl.connect(url=sandbox.url, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(), conn.upload_package(dars.KitchenSink.read_bytes())
        )

    # specify an explicit lookup to make sure that we are properly reading packages
    # from the ledger
    async with dazl.connect(
        url=sandbox.url, act_as=party_info.party, lookup=MultiPackageLookup()
    ) as conn:
        async with conn.query("KitchenSink.Interfaces.HasLocation:HasLocation", {}) as stream:
            async for ev in stream.creates():
                print(ev)
