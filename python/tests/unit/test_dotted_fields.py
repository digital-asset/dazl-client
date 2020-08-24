# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from dazl import async_network
from .dars import DottedFields


@pytest.mark.asyncio
async def test_record_dotted_fields_submit(sandbox):
    async with async_network(url=sandbox, dars=DottedFields) as network:
        client = network.aio_new_party()

        network.start()

        await client.ready()
        await client.submit_create('DottedFields:American', {
            'person': client.party,
            'address.address': '1 Test Place',
            'address.city': 'Somewhere',
            'address.state': 'ZZ',
            'address.zip': '99999'
        })

        items = client.find_active('DottedFields:American')
        assert len(items) == 1


@pytest.mark.asyncio
async def test_variant_dotted_fields_submit(sandbox):
    async with async_network(url=sandbox, dars=DottedFields) as network:
        client = network.aio_new_party()

        network.start()

        await client.ready()
        await client.submit_create('DottedFields:Person', {
            'person': client.party,
            'address.US.address': '1 Test Place',
            'address.US.city': 'Somewhere',
            'address.US.state': 'ZZ',
            'address.US.zip': '99999',
            'address.UK.address': '',
            'address.UK.locality': '',
            'address.UK.city': '',
            'address.UK.state': '',
            'address.UK.postcode': '',
        })

        items = client.find_active('DottedFields:Person')
        assert len(items) == 1
