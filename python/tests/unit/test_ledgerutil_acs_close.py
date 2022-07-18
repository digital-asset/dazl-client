# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from dazl.ledger.errors import ConnectionClosedError
from dazl.ledgerutil.acs import RUNNING, Snapshot, snapshots
from dazl.testing import connect_with_new_party
import pytest
from tests.unit.dars import PostOffice


@pytest.mark.asyncio
async def test_acs(sandbox):
    async with connect_with_new_party(url=sandbox, dar=PostOffice) as p:
        await p.connection.create("Main:PostmanRole", {"postman": p.party})
        snapshot = None  # type: Optional[Snapshot]
        snapshot_loop_count = 0

        with pytest.raises(ConnectionClosedError):
            async for state, s in snapshots(p.connection, "Main:PostmanRole"):
                # once we get one snapshot successfully, remember that we did, and kill our connection
                if state == RUNNING:
                    snapshot_loop_count += 1
                    snapshot = s

                    # ok so now we got the snapshot; kill the connection
                    await p.connection.close()

        # we should have only run the loop once
        assert snapshot_loop_count == 1

        # the snapshot should also not be empty
        assert snapshot
