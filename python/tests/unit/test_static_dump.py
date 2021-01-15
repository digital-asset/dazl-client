# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from dazl import async_network, LOG
from .dars import PostOffice


@pytest.mark.asyncio
async def test_static_dump_and_tail(sandbox):
    async with async_network(url=sandbox, dars=PostOffice) as network:
        client = network.aio_new_party()
        seen_contracts = []

        @client.ledger_ready()
        def print_initial_state(event):
            LOG.info("Current ACS: %s", event.acs_find_active('*'))

        @client.ledger_created('*')
        def print_create(event):
            LOG.info("Seen cid: %s, cdata: %s", event.cid, event.cdata)
            seen_contracts.append(event.cid)

        network.start()

        await client.ready()

        for i in range(0, 5):
            await client.submit_create('Main:PostmanRole', {'postman': client.party})

    assert len(seen_contracts) == 5
