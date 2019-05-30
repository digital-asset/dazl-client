# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from unittest import TestCase
from pathlib import Path

from dazl import sandbox, create_client, create, exercise

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'Simple.daml'
PARTY = 'Operator'
OperatorRole = 'Simple.OperatorRole'
OperatorNotification = 'Simple.OperatorNotification'


from dazl import setup_default_logger
import logging
setup_default_logger(logging.DEBUG)


class SelectTest(TestCase):
    def test_select_template_retrieves_contracts(self):
        with sandbox(DAML_FILE) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(lambda *args, **kwargs: create(OperatorRole, {'operator': PARTY}))
                client.run_until_complete()

                data = party_client.select(OperatorRole)

        self.assertEqual(len(data), 1)

    def test_select_unknown_template_retrieves_empty_set(self):
        with sandbox(DAML_FILE) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(lambda *args, **kwargs: create(OperatorRole, {'operator': PARTY}))
                client.run_until_complete()

                data = party_client.select('NonExistentTemplate')

        self.assertEqual(len(data), 0)

    def test_select_operates_on_acs_before_event_handlers(self):
        notification_count = 3

        # we expect that, upon each on_created notification of an OperatorNotification contract,
        # when we query the ACS, we get precisely the same number of contracts.
        expected_select_count = notification_count * notification_count
        actual_select_count = 0

        def on_notification_contract(_, __):
            nonlocal actual_select_count
            actual_select_count += len(party_client.select(OperatorNotification))

        with sandbox(DAML_FILE) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(lambda *args, **kwargs: create(OperatorRole, {'operator': PARTY}))
                party_client.on_created(OperatorRole, lambda cid, cdata: exercise(cid, 'PublishMany', dict(count=3)))
                party_client.on_created(OperatorNotification, on_notification_contract)
                client.run_until_complete()

        self.assertEqual(actual_select_count, expected_select_count)

    def test_select_reflects_archive_events(self):
        notification_count = 3

        # we expect that, upon each on_created notification of an OperatorNotification contract,
        # when we query the ACS, we get precisely the same number of contracts.
        expected_select_count = notification_count * notification_count
        actual_select_count = 0

        def on_notification_contract(_, __):
            nonlocal actual_select_count
            actual_select_count += len(party_client.select(OperatorNotification))

        with sandbox(DAML_FILE) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(lambda *args, **kwargs: create(OperatorRole, {'operator': PARTY}))
                party_client.on_created(OperatorRole, lambda cid, cdata: exercise(cid, 'PublishMany', dict(count=3)))
                party_client.on_created(OperatorNotification, lambda cid, _: exercise(cid, 'Archive'))
                party_client.on_created(OperatorNotification, on_notification_contract)
                client.run_until_complete()

                final_select_count = len(party_client.select(OperatorNotification))

        self.assertEqual(actual_select_count, expected_select_count)
        self.assertEqual(0, final_select_count)
