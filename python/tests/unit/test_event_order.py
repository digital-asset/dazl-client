# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import random
import uuid
from asyncio import sleep, new_event_loop, set_event_loop

from dazl import create, exercise, Network, Party
from .dars import Simple as SimpleDar

NOTIFICATION_COUNT = 20
PARTY_COUNT = 10


class Simple:
    OperatorRole = 'Simple:OperatorRole'
    OperatorNotification = 'Simple:OperatorNotification'


def test_event_order(sandbox):
    stage1 = Stage1LedgerInit()
    stage2 = Stage2LedgerVerify()

    stage1.run(sandbox)
    stage2.run(sandbox, stage1.operator_party)

    for event, cid, _ in stage2.events:
        print(event, cid)


class Stage1LedgerInit:

    def __init__(self):
        self.network = Network()
        self.operator_party = None
        self.user_parties = None
        self.done = None
        self.evt_count = 0

    def run(self, url):
        set_event_loop(new_event_loop())
        self.done = asyncio.Event()

        self.network.set_config(url=url)

        # TODO: These should be party allocations instead of just random strings.
        self.user_parties = frozenset(Party(str(uuid.uuid4())) for _ in range(0, PARTY_COUNT))

        operator = self.network.aio_new_party()
        operator.add_ledger_ready(self.on_ready)
        operator.add_ledger_created(Simple.OperatorRole, self.on_operator)
        operator.add_ledger_created(Simple.OperatorNotification, self.on_notification)

        self.operator_party = operator.party
        self.network.run_until_complete(self.done.wait())

    async def on_ready(self, event):
        await self.network.aio_global().ensure_dar(SimpleDar)
        while not event.package_store.resolve_template(Simple.OperatorRole):
            await sleep(1)

        return create(Simple.OperatorRole, {'operator': event.party})

    @staticmethod
    def on_operator(event):
        return [exercise(event.cid, 'Publish', {"text": n}) for n in range(0, NOTIFICATION_COUNT)]

    def on_notification(self, event):
        if self.evt_count == 25:
            self.done.set()
        else:
            self.evt_count += 1
            missing_parties = self.user_parties.difference(event.cdata['theObservers'])
            if missing_parties:
                return exercise(event.cid, 'Share', {'sharingParty': random.choice(list(missing_parties))})


class Stage2LedgerVerify:

    def __init__(self):
        self.store = {}
        self.events = []

    def run(self, url, operator_party):
        set_event_loop(new_event_loop())

        network = Network()
        network.set_config(url=url)

        operator = network.aio_party(operator_party)
        operator.add_ledger_ready(self.on_ready)
        operator.add_ledger_created(Simple.OperatorNotification, self.on_notification_created)
        operator.add_ledger_archived(Simple.OperatorNotification, self.on_notification_archived)
        network.run_until_complete()
        self.events.append(('finished', (), ()))

    def on_ready(self, _):
        self.events.append(('ready', (), ()))

    def on_notification_created(self, event):
        self.events.append(('created', event.cid, event.cdata))
        self.store[event.cid] = event.cdata

    def on_notification_archived(self, event):
        self.events.append(('archived', event.cid, ()))
        del self.store[event.cid]
