# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import logging
import random
from unittest import TestCase

from dazl import create, exercise, sandbox, setup_default_logger, Network
from .dars import Simple as SimpleDar

NOTIFICATION_COUNT = 20
PARTY_COUNT = 10

OPERATOR_PARTY = 'Operator'
USER_PARTIES = frozenset(f'Party{i}' for i in range(0, PARTY_COUNT))
ALL_PARTIES = [OPERATOR_PARTY, *sorted(USER_PARTIES)]


class Simple:
    OperatorRole = 'Simple.OperatorRole'
    OperatorNotification = 'Simple.OperatorNotification'


class TestEventOrder(TestCase):
    def test_event_order(self):
        some_sample_app()


def some_sample_app():
    setup_default_logger(logging.INFO)
    stage1 = Stage1LedgerInit()
    stage2 = Stage2LedgerVerify()

    with sandbox(SimpleDar) as proc:
        stage1.run(proc.url)
        stage2.run(proc.url)

    for event, cid, _ in stage2.events:
        print(event, cid)


class Stage1LedgerInit:

    def run(self, url):
        network = Network()
        network.set_config(url=url)

        operator = network.aio_party(OPERATOR_PARTY)
        operator.add_ledger_ready(lambda _: create(Simple.OperatorRole, {'operator': OPERATOR_PARTY}))
        operator.add_ledger_created(Simple.OperatorRole, self.on_operator)
        operator.add_ledger_created(Simple.OperatorNotification, self.on_notification)
        network.run_until_complete(asyncio.sleep(15))

    @staticmethod
    def on_operator(event):
        return [exercise(event.cid, 'Publish', {"text": n}) for n in range(0, NOTIFICATION_COUNT)]

    @staticmethod
    def on_notification(event):
        missing_parties = USER_PARTIES.difference(event.cdata['theObservers'])
        if missing_parties:
            return exercise(event.cid, 'Share', {'sharingParty': random.choice(list(missing_parties))})


class Stage2LedgerVerify:

    def __init__(self):
        self.store = {}
        self.events = []

    def run(self, url):
        network = Network()
        network.set_config(url=url)

        operator = network.aio_party(OPERATOR_PARTY)
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


if __name__ == '__main__':
    some_sample_app()
