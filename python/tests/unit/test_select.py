# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import sandbox, create, exercise, Network
from .dars import Simple


PARTY = 'Operator'
OperatorRole = 'Simple.OperatorRole'
OperatorNotification = 'Simple.OperatorNotification'


def test_select_template_retrieves_contracts():
    with sandbox(Simple) as proc:
        network = Network()
        network.set_config(url=proc.url)

        party_client = network.aio_party(PARTY)
        party_client.add_ledger_ready(lambda e: create(OperatorRole, {'operator': PARTY}))
        network.run_until_complete()

        data = party_client.find_active(OperatorRole)

    assert len(data) == 1


def test_select_unknown_template_retrieves_empty_set():
    with sandbox(Simple) as proc:
        network = Network()
        network.set_config(url=proc.url)

        party_client = network.aio_party(PARTY)
        party_client.add_ledger_ready(lambda e: create(OperatorRole, {'operator': PARTY}))
        network.run_until_complete()

        data = party_client.find_active('NonExistentTemplate')

    assert len(data) == 0


def test_select_operates_on_acs_before_event_handlers():
    notification_count = 3

    # we expect that, upon each on_created notification of an OperatorNotification contract,
    # when we query the ACS, we get precisely the same number of contracts.
    expected_select_count = notification_count * notification_count
    actual_select_count = 0

    def on_notification_contract(e):
        nonlocal actual_select_count
        actual_select_count += len(party_client.find_active(OperatorNotification))

    with sandbox(Simple) as proc:
        network = Network()
        network.set_config(url=proc.url)

        party_client = network.aio_party(PARTY)
        party_client.add_ledger_ready(lambda e: create(OperatorRole, {'operator': PARTY}))
        party_client.add_ledger_created(OperatorRole, lambda e: exercise(e.cid, 'PublishMany', dict(count=3)))
        party_client.add_ledger_created(OperatorNotification, on_notification_contract)
        network.run_until_complete()

    assert actual_select_count == expected_select_count


def test_select_reflects_archive_events():
    notification_count = 3

    # we expect that, upon each on_created notification of an OperatorNotification contract,
    # when we query the ACS, we get precisely the same number of contracts.
    expected_select_count = notification_count * notification_count
    actual_select_count = 0

    def on_notification_contract(event):
        nonlocal actual_select_count
        actual_select_count += len(event.acs_find_active(OperatorNotification))

    with sandbox(Simple) as proc:
        network = Network()
        network.set_config(url=proc.url)

        party_client = network.aio_party(PARTY)
        party_client.add_ledger_ready(lambda e: create(OperatorRole, {'operator': PARTY}))
        party_client.add_ledger_created(OperatorRole, lambda e: exercise(e.cid, 'PublishMany', dict(count=3)))
        party_client.add_ledger_created(OperatorNotification, lambda e: exercise(e.cid, 'Archive'))
        party_client.add_ledger_created(OperatorNotification, on_notification_contract)
        network.run_until_complete()

        final_select_count = len(party_client.find_active(OperatorNotification))

    assert actual_select_count == expected_select_count
    assert 0 == final_select_count
