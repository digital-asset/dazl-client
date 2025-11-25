# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.ledger import CreateCommand, ExerciseCommand
from dazl.ledger.aio import Connection
from dazl.prim import ContractData, ContractId
from dazl.testing import SandboxLauncher
import pytest

from dazl import connect

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
        await conn.upload_package(Pending.read_bytes())

    async with connect(url=sandbox.url, act_as=party) as conn:
        await conn.submit(
            [
                CreateCommand(Counter, {"owner": party, "value": 0}),
                *[
                    CreateCommand(AccountRequest, {"owner": party})
                    for _ in range(number_of_contracts)
                ],
            ]
        )

        async with conn.query(AccountRequest) as stream:
            async for create in stream.creates():
                counter_cid, counter_cdata = await get_counter(conn)
                await conn.submit(
                    [
                        ExerciseCommand(
                            create.contract_id,
                            "CreateAccount",
                            dict(accountId=counter_cdata["value"]),
                        ),
                        ExerciseCommand(counter_cid, "Increment"),
                    ]
                )

        data = []
        async with conn.query(Account) as stream:
            async for payload in stream.creates():
                data.append(payload.contract_id)

    assert len(data) == number_of_contracts


async def get_counter(conn: Connection) -> tuple[ContractId, ContractData]:
    async with conn.query(Counter) as stream:
        async for create in stream.creates():
            return create.contract_id, create.payload
    raise AssertionError("could not find a Counter contract")
