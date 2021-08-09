# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import logging

from dazl.testing import connect_with_new_party

from .dars import Simple


def test_ledger_conn_blocking(sandbox):
    with connect_with_new_party(url=sandbox, blocking=True, dar=Simple) as p:
        count = 0
        p.connection.create("Simple:OperatorRole", {"operator": p.party})
        with p.connection.stream("Simple:OperatorRole") as stream:
            for event in stream.creates():
                logging.info("Received an event: %s", event)
                count += 1
                break

        assert count == 1
