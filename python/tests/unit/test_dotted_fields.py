# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.testing import connect_with_new_party
import pytest

from .dars import DottedFields


@pytest.mark.asyncio
@pytest.mark.skip(
    "These tests are temporarily disabled because the new encoder does not support this."
)
async def test_record_dotted_fields_submit(sandbox):
    async with connect_with_new_party(url=sandbox, dar=DottedFields) as p:
        await p.connection.create(
            "DottedFields:American",
            {
                "person": p.party,
                "address.address": "1 Test Place",
                "address.city": "Somewhere",
                "address.state": "ZZ",
                "address.zip": "99999",
            },
        )

        items = []
        async with p.connection.query("DottedFields:American") as stream:
            async for event in stream.creates():
                items.append(event)

        assert len(items) == 1


@pytest.mark.asyncio
@pytest.mark.skip(
    "These tests are temporarily disabled because the new encoder does not support this."
)
async def test_variant_dotted_fields_submit(sandbox):
    async with connect_with_new_party(url=sandbox, dar=DottedFields) as p:
        await p.connection.create(
            "DottedFields:Person",
            {
                "person": p.party,
                "address.US.address": "1 Test Place",
                "address.US.city": "Somewhere",
                "address.US.state": "ZZ",
                "address.US.zip": "99999",
                "address.UK.address": "",
                "address.UK.locality": "",
                "address.UK.city": "",
                "address.UK.state": "",
                "address.UK.postcode": "",
            },
        )

        items = []
        async with p.connection.query("DottedFields:Person") as stream:
            async for event in stream.creates():
                items.append(event)

        assert len(items) == 1
