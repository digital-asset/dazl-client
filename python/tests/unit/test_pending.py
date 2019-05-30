# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import asyncio
import logging
from asyncio import get_event_loop, wait_for, sleep, gather
from unittest import TestCase
from pathlib import Path

from dazl import sandbox, create_client, create, exercise, setup_default_logger
from dazl.util.events import EventHandlerTracker

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'Pending.daml'
PARTY = 'Operator'
Counter = 'Pending.Counter'
Account = 'Pending.Account'
AccountRequest = 'Pending.AccountRequest'

OperatorNotification = 'Simple.OperatorNotification'

setup_default_logger(logging.DEBUG)


class PendingTest(TestCase):
    def test_select_template_retrieves_contracts(self):
        number_of_contracts = 10

        with sandbox(DAML_FILE) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(lambda *args, **kwargs: [
                    create(Counter, {'owner': PARTY, 'value': 0}),
                    *[create(AccountRequest, {'owner': PARTY}) for i in range(number_of_contracts)],
                ])

                async def on_account_request(cid, _):
                    counter_cid, counter_cdata = await party_client.select_first(Counter)
                    return [
                        exercise(cid, 'CreateAccount', dict(accountId=counter_cdata['value'])),
                        exercise(counter_cid, 'Increment')
                    ]

                party_client.on_created(AccountRequest, on_account_request)
                client.run_until_complete()

                data = party_client.select(Account)

        self.assertEqual(len(data), number_of_contracts)

    def test_trackers(self):
        loop = get_event_loop()
        values = []

        number_of_elements = 10

        async def test_body():
            tracker = EventHandlerTracker(do_computation)
            futures = [tracker.invoke_eventually(i) for i in range(number_of_elements)]
            await wait_for(gather(*futures), timeout=number_of_elements)

        async def do_computation(value: int):
            # force this computation to wait for a duration of time inversely proportional to the
            # value passed in; if serializing of execution isn't being handled properly, then the
            # values will be added in the wrong order
            await sleep(max(1.0 / max(1, value), 0))
            values.append(value)

        try:
            loop.run_until_complete(test_body())
        except asyncio.TimeoutError:
            self.fail(f'Timed out instead of aborting normally; {values} finished so far')

        self.assertEqual(values, list(range(number_of_elements)))
