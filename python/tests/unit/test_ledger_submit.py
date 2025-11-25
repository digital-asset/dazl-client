# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import gather

from dazl.damlast.lookup import MultiPackageLookup
from dazl.ledger.aio import PackageLoader
from dazl.testing import SandboxLauncher
import pytest
from tests.unit import dars

import dazl


@pytest.mark.asyncio
async def test_command_submission_with_stdlib_values(sandbox: SandboxLauncher) -> None:
    async with dazl.connect(url=sandbox.url, admin=True) as conn:
        party_info, _ = await gather(
            conn.allocate_party(), conn.upload_package(dars.KitchenSink.read_bytes())
        )

        # remember the appropriate template ID, because we'll need it soon
        lookup = MultiPackageLookup()
        loader = PackageLoader(lookup, conn)
        result = await loader.do_with_retry(lambda: lookup.search("KitchenSink.Retailer:Retailer"))
        tmpl_id = next(iter(result.templates))

    # override lookup intentionally to make sure this test is not polluted with cached state from other tests
    async with dazl.connect(
        url=sandbox.url, act_as=party_info.party, lookup=MultiPackageLookup()
    ) as conn:
        # bare create a contract with a specific package ID; this should have the side-effect of resolving
        # dependent packages (in this case, stdlib itself)
        await conn.create(
            tmpl_id,
            {
                "retailer": party_info.party,
                "name": "Cats R Us",
                "website": "https://cats.nowhere",
                "tags": {"map": {}},
            },
        )
