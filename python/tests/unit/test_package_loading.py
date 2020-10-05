# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tests to ensure that packages can be loaded.
"""
import logging
import time
from operator import setitem

import pytest

from dazl import async_network
from dazl.damlast import DarFile
from dazl.model.types_store import PackageStore
from .dars import AllKindsOf


@pytest.mark.asyncio
@pytest.mark.skip('This test is no longer valid, as we do not force packages to be loaded on startup')
async def test_package_loading(sandbox):
    d = {}

    start_time = time.time()
    with DarFile(AllKindsOf) as dar:
        expected_package_ids = dar.get_package_provider().get_package_ids()
    end_time = time.time()

    logging.info("Total package load time: %0.2f ms", (end_time - start_time) * 1000)
    logging.info("Package IDs (%s total): %s", len(expected_package_ids), sorted(expected_package_ids))

    async with async_network(url=sandbox, dars=AllKindsOf) as network:
        client = network.aio_new_party()
        client.add_ledger_ready(lambda event: setitem(d, 'metadata', event.package_store))

        network.start()

    store: PackageStore = d['metadata']
    actual_package_ids = store.package_ids()

    assert set(expected_package_ids).issubset(set(actual_package_ids))
