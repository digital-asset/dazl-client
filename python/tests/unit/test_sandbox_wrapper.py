# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl import sandbox, create, Network
from dazl.model.core import ProcessDiedException
from .dars import Simple

PARTY = 'Operator'
OperatorRole = 'Simple.OperatorRole'


def test_nice_sandbox_allows_test():
    _sandbox_test()


def test_dead_sandbox_aborts_test():
    try:
        _sandbox_test(extra_args=['--please-crash'])
    except ProcessDiedException:
        return

    assert False, "Should have raised an exception"


def _sandbox_test(extra_args=None):
    cids = []
    with sandbox(Simple, extra_args=extra_args) as proc:
        network = Network()
        network.set_config(url=proc.url)

        party_client = network.aio_party(PARTY)
        party_client.add_ledger_ready(lambda _: create(OperatorRole, {'operator': PARTY}))
        party_client.add_ledger_created(OperatorRole, lambda e: cids.append(e.cid))
        network.run_until_complete()

    logging.info('got to the end with contracts: %s', cids)
    assert len(cids) == 1
