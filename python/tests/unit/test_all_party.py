# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl import async_network, connect
from dazl.testing import SandboxLauncher
import pytest

from .dars import AllParty as AllPartyDar

PrivateContract = "AllParty:PrivateContract"
PublicContract = "AllParty:PublicContract"


@pytest.mark.asyncio
async def test_some_party_receives_public_contract(sandbox: SandboxLauncher) -> None:
    some_party_cids = []
    publisher_cids = []

    async with connect(url=sandbox.url, admin=True) as conn:
        all_party_info = await conn.allocate_party()
        some_party_info = await conn.allocate_party()
        publisher_party_info = await conn.allocate_party()

    async with async_network(url=sandbox.url, dars=AllPartyDar) as network:
        network.set_config(party_groups=[all_party_info.party])

        some_client = network.aio_party(some_party_info.party)
        some_client.add_ledger_ready(
            lambda _: some_client.create(PrivateContract, {"someParty": some_client.party})
        )

        publisher_client = network.aio_party(publisher_party_info.party)
        publisher_client.add_ledger_ready(
            lambda _: publisher_client.create(
                PublicContract,
                {"publisher": publisher_client.party, "allParty": all_party_info.party},
            )
        )

        some_client.add_ledger_created(PublicContract, lambda e: some_party_cids.append(e.cid))
        some_client.add_ledger_created(PrivateContract, lambda e: some_party_cids.append(e.cid))

        publisher_client.add_ledger_created(PublicContract, lambda e: publisher_cids.append(e.cid))
        publisher_client.add_ledger_created(PrivateContract, lambda e: publisher_cids.append(e.cid))

        network.start()

    logging.info(
        "got to the end with some_party contracts: %s and publisher contracts: %s",
        some_party_cids,
        publisher_cids,
    )

    assert len(some_party_cids) == 2
    assert len(publisher_cids) == 1
