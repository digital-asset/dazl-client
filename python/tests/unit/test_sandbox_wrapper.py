# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from unittest import TestCase
from pathlib import Path

from dazl import sandbox, create, Network
from dazl.model.core import ProcessDiedException

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'Simple.daml'
PARTY = 'Operator'
OperatorRole = 'Simple.OperatorRole'


class SandboxWrapperTest(TestCase):
    def _sandbox_test(self, extra_args=None):
        cids = []
        with sandbox(DAML_FILE, extra_args=extra_args) as proc:
            network = Network()
            network.set_config(url=proc.url)

            party_client = network.aio_party(PARTY)
            party_client.add_ledger_ready(lambda _: create(OperatorRole, {'operator': PARTY}))
            party_client.add_ledger_created(OperatorRole, lambda e: cids.append(e.cid))
            network.run_until_complete()

        print('got to the end with contracts: ', cids)
        self.assertEqual(len(cids), 1)

    def test_nice_sandbox_allows_test(self):
        self._sandbox_test()

    def test_dead_sandbox_aborts_test(self):
        self.failUnlessRaises(
            ProcessDiedException,
            lambda: self._sandbox_test(extra_args=['--please-crash']))
