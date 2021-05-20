from typing import Optional

from dazl import connect
from dazl.ledger.errors import ConnectionClosedError
from dazl.ledgerutil.acs import RUNNING, Snapshot, snapshots
import pytest
from tests.unit.dars import PostOffice


@pytest.mark.asyncio
async def test_acs(sandbox):
    # we need a sandbox that we can close, so we create our own
    async with connect(url=sandbox, admin=True) as conn:
        await conn.upload_package(PostOffice.read_bytes())
        party = (await conn.allocate_party()).party

    async with connect(url=sandbox, act_as=party) as conn:
        await conn.create("Main:PostmanRole", {"postman": party})
        snapshot = None  # type: Optional[Snapshot]
        snapshot_loop_count = 0

        with pytest.raises(ConnectionClosedError):
            async for state, s in snapshots(conn, "Main:PostmanRole"):
                # once we get one snapshot successfully, remember that we did, and kill our connection
                if state == RUNNING:
                    snapshot_loop_count += 1
                    snapshot = s

                    # ok so now we got the snapshot; kill the connection
                    await conn.close()

        # we should have only run the loop once
        assert snapshot_loop_count == 1

        # the snapshot should also not be empty
        assert snapshot
