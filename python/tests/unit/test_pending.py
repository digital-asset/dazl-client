# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Sequence

from dazl import async_network, connect
from dazl.ledger import Command, CreateCommand, ExerciseCommand
from dazl.protocols.events import ContractCreateEvent
from dazl.testing import SandboxLauncher
import pytest

from .dars import Pending

Counter = "Pending:Counter"
Account = "Pending:Account"
AccountRequest = "Pending:AccountRequest"

OperatorNotification = "Simple:OperatorNotification"


@pytest.mark.asyncio
async def test_select_template_retrieves_contracts(sandbox: SandboxLauncher) -> None:
    number_of_contracts = 10

    async with connect(url=sandbox.url, admin=True) as conn:
        party = (await conn.allocate_party()).party

    async with async_network(url=sandbox.url, dars=Pending) as network:
        client = network.aio_party(party)
        client.add_ledger_ready(
            lambda _: [
                CreateCommand(Counter, {"owner": client.party, "value": 0}),
                *[
                    CreateCommand(AccountRequest, {"owner": client.party})
                    for _ in range(number_of_contracts)
                ],
            ]
        )

        @client.ledger_created(AccountRequest)
        async def on_account_request(event: ContractCreateEvent) -> Sequence[Command]:
            counter_cid, counter_cdata = await event.acs_find_one(Counter)
            return [
                ExerciseCommand(event.cid, "CreateAccount", dict(accountId=counter_cdata["value"])),
                ExerciseCommand(counter_cid, "Increment"),
            ]

        await network.aio_run(keep_open=False)

        data = client.find_active(Account)

    assert len(data) == number_of_contracts
