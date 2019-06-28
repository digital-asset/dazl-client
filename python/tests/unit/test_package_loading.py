# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tests to ensure that packages can be loaded.
"""
import logging
from operator import setitem
from pathlib import Path
from unittest import TestCase, skip
from zipfile import ZipFile

from dazl import sandbox, Network, setup_default_logger
from dazl.model.types_store import PackageStore
from dazl.util.dar import build_dar, DarFile
from dazl.util.io import find_nearest_ancestor

CACHE_DIR = find_nearest_ancestor('.dazl-root', __file__).parent / '.cache' / 'test-dars'

DAR_FILE: Path = CACHE_DIR / 'AllKindsOf.dar'
DALF_FILE: Path = CACHE_DIR / 'AllKindsOf.dalf'
DAML_FILE: Path = Path(__file__).parent.parent / 'resources' / 'AllKindsOf.daml'


class PackageLoadingTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Intentionally create a DAR with missing dependencies
        build_dar(DAML_FILE, DAR_FILE, allow_caching=True)
        with ZipFile(DAR_FILE) as z:
            DALF_FILE.write_bytes(z.read('package-name.dalf'))

    @skip("Sandbox 100.13.10 does not currently accept DALFs as command-line parameters, so this "
          "test cannot be run.")
    def test_incomplete_package_loading(self):
        # Attempt to load only the DALF into the Sandbox; this will cause the PackageService to
        # return a nonsensical result, the lack of an exception being thrown signals that we can
        # tolerate this condition
        d = {}

        setup_default_logger(logging.INFO)

        with sandbox(DALF_FILE) as proc:
            network = Network()
            network.set_config(url=proc.url)
            client = network.aio_party('TestParty')
            client.add_ledger_ready(lambda event: setitem(d, 'metadata', event.package_store))
            network.run_until_complete()

        store: PackageStore = d['metadata']
        actual_package_ids = store.package_ids()

        # When the only package has no dependencies, the PackageStore should remain empty
        self.assertFalse(set(), set(actual_package_ids))

    def test_complete_package_loading(self):
        # Attempt to load only the DALF into the Sandbox; this will cause the PackageService to
        # return a nonsensical result, the lack of an exception being thrown signals that we can
        # tolerate this condition
        d = {}
        with DarFile(DAR_FILE) as dar:
            expected_package_ids = dar.get_package_provider().get_package_ids()

        with sandbox(DAR_FILE) as proc:
            network = Network()
            network.set_config(url=proc.url)
            client = network.aio_party('TestParty')
            client.add_ledger_ready(lambda event: setitem(d, 'metadata', event.package_store))
            network.run_until_complete()

        store: PackageStore = d['metadata']
        actual_package_ids = store.package_ids()

        self.assertEqual(set(expected_package_ids), set(actual_package_ids))
