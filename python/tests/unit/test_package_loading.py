# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tests to ensure that packages can be loaded.
"""
from operator import setitem

from dazl import sandbox, Network
from dazl.model.types_store import PackageStore
from dazl.util.dar import DarFile
from .dars import AllKindsOf


def test_package_loading():
    d = {}
    with DarFile(AllKindsOf) as dar:
        expected_package_ids = dar.get_package_provider().get_package_ids()

    with sandbox(AllKindsOf) as proc:
        network = Network()
        network.set_config(url=proc.url)
        client = network.aio_party('TestParty')
        client.add_ledger_ready(lambda event: setitem(d, 'metadata', event.package_store))
        network.run_until_complete()

    store: PackageStore = d['metadata']
    actual_package_ids = store.package_ids()

    assert set(expected_package_ids) == set(actual_package_ids)
