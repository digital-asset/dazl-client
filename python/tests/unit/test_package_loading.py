# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tests to ensure that packages can be loaded.
"""
from operator import setitem

import pytest

from dazl import async_network
from dazl.model.types_store import PackageStore
from dazl.util.dar import DarFile
from .dars import AllKindsOf


@pytest.mark.asyncio
async def test_package_loading(sandbox):
    d = {}
    with DarFile(AllKindsOf) as dar:
        expected_package_ids = dar.get_package_provider().get_package_ids()

    async with async_network(url=sandbox, dars=AllKindsOf) as network:
        client = network.aio_new_party()
        client.add_ledger_ready(lambda event: setitem(d, 'metadata', event.package_store))

        network.start()

    store: PackageStore = d['metadata']
    actual_package_ids = store.package_ids()

    assert set(expected_package_ids).issubset(set(actual_package_ids))
