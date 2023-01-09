# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import async_network, connect
from dazl.protocols.events import ReadyEvent
from dazl.testing import SandboxLauncher
import pytest

from .dars import PostOffice


@pytest.mark.asyncio
async def test_event_handler_exceptions(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        party = (await conn.allocate_party()).party

    async with async_network(url=sandbox.url, dars=PostOffice) as network:
        client = network.aio_party(party)

        def throw_error(event: ReadyEvent):
            raise MagicException(event.ledger_id)

        client.add_ledger_ready(throw_error)

        network.start()


class MagicException(Exception):
    pass
