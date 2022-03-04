# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from asyncio import sleep

from dazl import connect, testing
from dazl.ledger.config.access import DamlLedgerApiNamespace
import pytest

from .config import daml_sdk_versions


@pytest.mark.asyncio
@pytest.mark.parametrize("daml_sdk_version", daml_sdk_versions())
async def test_v1_token(daml_sdk_version):
    with testing.sandbox(version=daml_sdk_version, use_auth=True, ledger_id="sandbox") as sandbox:
        token = sandbox.sign_token({DamlLedgerApiNamespace: {"admin": True, "ledgerId": "sandbox"}})
        async with connect(url=sandbox.url, oauth_token=token) as conn:
            # the result of this call is not particularly interesting;
            # we just need to make sure it doesn't crash
            await conn.list_package_ids()
            await sleep(1)
