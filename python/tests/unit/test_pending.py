# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import pytest

from dazl import async_network, create, exercise
from .dars import Pending

Counter = 'Pending.Counter'
Account = 'Pending.Account'
AccountRequest = 'Pending.AccountRequest'

OperatorNotification = 'Simple.OperatorNotification'


@pytest.mark.asyncio
async def test_select_template_retrieves_contracts(sandbox):
    number_of_contracts = 10

    async with async_network(url=sandbox, dars=Pending) as network:
        client = network.aio_new_party()
        client.add_ledger_ready(lambda _: [
            create(Counter, {'owner': client.party, 'value': 0}),
            *[create(AccountRequest, {'owner': client.party}) for i in range(number_of_contracts)],
        ])

        @client.ledger_created(AccountRequest)
        async def on_account_request(event):
            counter_cid, counter_cdata = await event.acs_find_one(Counter)
            return [
                exercise(event.cid, 'CreateAccount', dict(accountId=counter_cdata['value'])),
                exercise(counter_cid, 'Increment')
            ]

        await network.aio_run(keep_open=False)

        data = client.find_active(Account)

    assert len(data) == number_of_contracts
