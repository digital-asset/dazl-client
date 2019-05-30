# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from unittest import TestCase

from dazl.model.types_store import PackageStore, PackageProvider, MemoryPackageProvider
from dazl.protocols.v1.grpc import grpc_package_sync
from dazl.util.dar import TemporaryDar, DarFile

DAML_FILE_1 = Path(__file__).parent.parent / 'resources' / 'AllKindsOf.daml'
DAML_FILE_2 = Path(__file__).parent.parent / 'resources' / 'Pending.daml'


class TestDynamicDarLoading(TestCase):
    def test_package_sync_multiple_loads(self):
        store = PackageStore.empty()

        pp1 = create_package_provider(DAML_FILE_1)
        grpc_package_sync(pp1, store)

        pp2 = create_package_provider(DAML_FILE_2)
        grpc_package_sync(pp2, store)

        print(store.package_ids())


def create_package_provider(daml_file: 'Path') -> 'PackageProvider':
    data = {}
    with TemporaryDar(daml_file) as outputs:
        for output in outputs:
            if output.endswith('.dar'):
                with DarFile(output) as dar:
                    data.update(dar.get_package_provider().get_all_packages())
            elif output.endswith('.dalf'):
                from dazl._gen.da.daml_lf_pb2 import Archive
                a = Archive()
                with open(output, 'rb') as f:
                    a.ParseFromString(f.read())
                data[a.hash] = a.payload

    return MemoryPackageProvider(data)
