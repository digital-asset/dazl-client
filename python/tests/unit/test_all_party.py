# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import asyncio
import logging
import uuid

import pytest

from dazl import Party, async_network, connect, create
from dazl.util.io import get_bytes

from .dars import AllParty as AllPartyDar

PrivateContract = "AllParty:PrivateContract"
PublicContract = "AllParty:PublicContract"


@pytest.mark.asyncio
@pytest.mark.parametrize("future_api", [False, True])
async def test_some_party_receives_public_contract(sandbox, future_api):
    some_party_cids = []
    publisher_cids = []

    # TODO: Switch to a Party allocation API when available.
    all_party = Party(str(uuid.uuid4()))

    async with async_network(url=sandbox, dars=AllPartyDar, future_api=future_api) as network:
        network.set_config(party_groups=[all_party])

        some_client = network.aio_new_party()
        some_client.add_ledger_ready(
            lambda _: create(PrivateContract, {"someParty": some_client.party})
        )

        publisher_client = network.aio_new_party()
        publisher_client.add_ledger_ready(
            lambda _: create(
                PublicContract, {"publisher": publisher_client.party, "allParty": all_party}
            )
        )

        some_client.add_ledger_created(PublicContract, lambda e: some_party_cids.append(e.cid))
        some_client.add_ledger_created(PrivateContract, lambda e: some_party_cids.append(e.cid))

        publisher_client.add_ledger_created(PublicContract, lambda e: publisher_cids.append(e.cid))
        publisher_client.add_ledger_created(PrivateContract, lambda e: publisher_cids.append(e.cid))

        if future_api:
            # the new API can't make guarantees that events and consequence commands are correlated
            # any more, so the caller now has to do this
            async def wait_for_contracts():
                while not (some_party_cids == 2 and publisher_cids == 1):
                    await asyncio.sleep(1.0)

            await asyncio.wait_for(
                network.aio_run(wait_for_contracts(), keep_open=False), timeout=5.0
            )
        else:
            # the old API tracks follow-up commands and subsequent events that those commands have
            # triggered, but at a higher implementation cost and less flexibility
            network.start()

    logging.info(
        "got to the end with some_party contracts: %s and publisher contracts: %s",
        some_party_cids,
        publisher_cids,
    )

    assert len(some_party_cids) == 2
    assert len(publisher_cids) == 1


@pytest.mark.asyncio
async def test_multi_party_receives_all_contracts(sandbox):
    async with connect(url=sandbox, admin=True) as conn:
        await conn.upload_package(get_bytes(AllPartyDar))
        some_party = await conn.allocate_party("someParty")
        all_party = await conn.allocate_party("allParty")
        publisher = await conn.allocate_party("publisher")

    async with connect(url=sandbox, act_as=publisher.party) as publisher_conn, connect(
        url=sandbox, act_as=some_party.party, read_as=all_party.party
    ) as some_conn:
        # create two contracts; the underlying submit call is guaranteed to block so from the
        # perspective of the caller, waiting for these calls to complete is enough to ensure these
        # contracts are actually there
        await some_conn.create(PrivateContract, {"someParty": some_party.party})
        await publisher_conn.create(
            PublicContract, {"publisher": publisher.party, "allParty": all_party.party}
        )

        assert await count_contracts(some_conn, PublicContract) == 1
        assert await count_contracts(some_conn, PrivateContract) == 1
        assert await count_contracts(publisher_conn, PublicContract) == 1
        assert await count_contracts(publisher_conn, PrivateContract) == 0


async def count_contracts(conn, template_name) -> int:
    async with conn.query(template_name) as stream:
        count = 0
        async for _ in stream:
            count += 1
    return count
