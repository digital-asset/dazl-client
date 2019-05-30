# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import logging
import random
from pathlib import Path
from unittest import TestCase

from dazl import create, exercise, create_client, sandbox, setup_default_logger

NOTIFICATION_COUNT = 20
PARTY_COUNT = 10

OPERATOR_PARTY = 'Operator'
USER_PARTIES = frozenset(f'Party{i}' for i in range(0, PARTY_COUNT))
ALL_PARTIES = [OPERATOR_PARTY, *sorted(USER_PARTIES)]

SIMPLE_DAML = Path(__file__).parent.parent / 'resources' / 'Simple.daml'


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

    with sandbox(SIMPLE_DAML) as proc:
        stage1.run(proc.url)
        stage2.run(proc.url)

    for event, cid, _ in stage2.events:
        print(event, cid)


class Stage1LedgerInit:

    def run(self, url):
        with create_client(participant_url=url, parties=ALL_PARTIES) as client_manager:
            operator = client_manager.client(OPERATOR_PARTY)
            operator.on_ready(
                lambda *args, **kwargs: create(Simple.OperatorRole, {'operator': OPERATOR_PARTY}))
            operator.on_created(Simple.OperatorRole, self.on_operator)
            operator.on_created(Simple.OperatorNotification, self.on_notification)
            client_manager.run_until_complete(asyncio.sleep(15))

    @staticmethod
    def on_operator(cid, cdata):
        return [exercise(cid, 'Publish', {"text": n}) for n in range(0, NOTIFICATION_COUNT)]

    @staticmethod
    def on_notification(cid, cdata):
        missing_parties = USER_PARTIES.difference(cdata['theObservers'])
        if missing_parties:
            return exercise(cid, 'Share', {'sharingParty': random.choice(list(missing_parties))})


class Stage2LedgerVerify:

    def __init__(self):
        self.store = {}
        self.events = []

    def run(self, url):
        with create_client(participant_url=url, parties=ALL_PARTIES) as client_manager:
            operator = client_manager.client(OPERATOR_PARTY)
            operator.on_ready(self.on_ready)
            operator.on_created(Simple.OperatorNotification, self.on_notification_created)
            operator.on_archived(Simple.OperatorNotification, self.on_notification_archived)
            client_manager.run_until_complete()
        self.events.append(('finished', (), ()))

    def on_ready(self, *args, **kwargs):
        self.events.append(('ready', (), ()))

    def on_notification_created(self, cid, cdata):
        self.events.append(('created', cid, cdata))
        self.store[cid] = cdata

    def on_notification_archived(self, cid, _):
        self.events.append(('archived', cid, ()))
        del self.store[cid]


if __name__ == '__main__':
    some_sample_app()
