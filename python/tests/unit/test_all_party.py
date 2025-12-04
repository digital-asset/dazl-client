# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Sequence

from dazl import connect
from dazl.ledger.aio import Connection
from dazl.prim import ContractId
from dazl.testing import SandboxLauncher
import pytest

from .dars import AllParty as AllPartyDar

PrivateContract = "AllParty:PrivateContract"
PublicContract = "AllParty:PublicContract"


@pytest.mark.asyncio
async def test_some_party_receives_public_contract(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        all_party_info = await conn.allocate_party()
        some_party_info = await conn.allocate_party()
        publisher_party_info = await conn.allocate_party()

        await conn.upload_package(AllPartyDar.read_bytes())

    async with connect(url=sandbox.url, act_as=[some_party_info.party]) as conn:
        await conn.create(PrivateContract, {"someParty": some_party_info.party})
    async with connect(url=sandbox.url, act_as=[publisher_party_info.party]) as conn:
        await conn.create(
            PublicContract,
            {"publisher": publisher_party_info.party, "allParty": all_party_info.party},
            act_as=publisher_party_info.party,
        )

    async with connect(
        url=sandbox.url, read_as=[some_party_info.party, publisher_party_info.party]
    ) as conn:
        some_party_cids = await get_contract_ids(conn)

    async with connect(
        url=sandbox.url, read_as=[all_party_info.party, publisher_party_info.party]
    ) as conn:
        publisher_cids = await get_contract_ids(conn)

    logging.info(
        "got to the end with some_party contracts: %s and publisher contracts: %s",
        some_party_cids,
        publisher_cids,
    )

    assert len(some_party_cids) == 2
    assert len(publisher_cids) == 1


async def get_contract_ids(conn: Connection) -> Sequence[ContractId]:
    cids = []
    async with conn.query(PublicContract) as stream:
        async for create in stream.creates():
            cids.append(create.contract_id)
    async with conn.query(PrivateContract) as stream:
        async for create in stream.creates():
            cids.append(create.contract_id)

    return cids
