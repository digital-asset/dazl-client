# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from asyncio import sleep

from dazl import connect, testing
import pytest

from .config import daml_sdk_versions


@pytest.mark.asyncio
@pytest.mark.parametrize("daml_sdk_version", daml_sdk_versions())
async def test_tls(daml_sdk_version):
    with testing.sandbox(version=daml_sdk_version, use_tls=True) as sandbox:
        async with connect(url=sandbox.url, admin=True, cert=sandbox.public_cert) as conn:
            # the result of this call is not particularly interesting;
            # we just need to make sure it doesn't crash
            await conn.list_package_ids()
            await sleep(1)
