# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import dazl
import pytest


@pytest.mark.asyncio
async def test_ledger_end(sandbox) -> None:
    async with dazl.connect(url=sandbox, admin=True) as conn:
        actual = await conn.get_ledger_end()

    # the actual offset is unpredictable, but it will always be defined and non-empty
    assert actual
