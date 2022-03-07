# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import sleep

from dazl import connect, testing
import pytest


@pytest.mark.asyncio
async def test_tls_connect_1_18():
    with testing.sandbox(version="1.18.1", use_tls=True) as sandbox:
        async with connect(url=sandbox.url, admin=True, cert=sandbox.public_cert) as conn:
            # the result of this call is not particularly interesting;
            # we just need to make sure it doesn't crash
            await conn.list_package_ids()
            await sleep(1)
