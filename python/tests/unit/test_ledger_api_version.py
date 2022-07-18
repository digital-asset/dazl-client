# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

from dazl import connect
import pytest


@pytest.mark.asyncio
async def test_ledger_api_version(sandbox):
    async with connect(url=sandbox, admin=True) as conn:
        version = await conn.get_version()

        logging.info("Ledger API version: %s", version.version)
        logging.info(
            "User management API supported: %s", version.features.user_management.supported
        )
