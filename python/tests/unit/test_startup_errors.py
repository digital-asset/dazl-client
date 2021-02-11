import asyncio
from asyncio import CancelledError, ensure_future, wait_for

import pytest

from dazl import LOG, Network


@pytest.mark.asyncio
async def test_startup_errors_should_halt_ready():
    """
    Ensure that a failure to connect aborts ready futures.
    """
    network = Network()
    network.set_config(url="http://nowhere.at.all.localdomain:6865/", connect_timeout=1)

    client = network.aio_party("SillyParty")

    # place the ready() call BEFORE the run
    f = ensure_future(wait_for(client.ready(), 2))

    try:
        await network.aio_run(keep_open=False)
    except Exception:
        pass

    try:
        await f
        raise AssertionError(
            "client.ready() should not have ended because there is nothing to connect to"
        )
    except asyncio.TimeoutError:
        raise AssertionError(
            "client.ready() did not abort with an appropriate exception and was killed because "
            "it was taking too long"
        )
    except CancelledError:
        LOG.info("Successfully terminated because ready() was cancelled.")
