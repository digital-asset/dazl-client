# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from unittest import TestCase

from dazl.model.types_store import PackageStore, PackageProvider, MemoryPackageProvider
from dazl.protocols.v1.grpc import grpc_package_sync
from dazl.util.dar import DarFile
from .dars import AllKindsOf, Pending


class TestDynamicDarLoading(TestCase):
    def test_package_sync_multiple_loads(self):
        store = PackageStore.empty()

        pp1 = create_package_provider(AllKindsOf)
        grpc_package_sync(pp1, store)

        pp2 = create_package_provider(Pending)
        grpc_package_sync(pp2, store)

        print(store.package_ids())


def create_package_provider(dar_file: 'Path') -> 'PackageProvider':
    data = {}
    with DarFile(dar_file) as dar:
        data.update(dar.get_package_provider().get_all_packages())
    return MemoryPackageProvider(data)
