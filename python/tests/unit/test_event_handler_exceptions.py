# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import pytest

from dazl import async_network
from dazl.model.reading import ReadyEvent

from .dars import PostOffice


@pytest.mark.asyncio
async def test_event_handler_exceptions(sandbox):
    async with async_network(url=sandbox, dars=PostOffice) as network:
        client = network.aio_new_party()

        def throw_error(event: ReadyEvent):
            raise MagicException(event.ledger_id)

        client.add_ledger_ready(throw_error)

        network.start()


class MagicException(Exception):
    pass

