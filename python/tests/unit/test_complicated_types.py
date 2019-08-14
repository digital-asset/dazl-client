# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from operator import setitem
from unittest import TestCase

from dazl import sandbox, create, exercise, Network
from .dars import Complicated as ComplicatedDar

PARTY = 'Operator'


class Complicated:
    OperatorRole = 'Complicated.OperatorRole'
    OperatorFormulaNotification = 'Complicated.OperatorFormulaNotification'


class ComplicatedTypesTest(TestCase):
    def test_complicated_types(self):
        recorded_data = dict()
        with sandbox(ComplicatedDar) as proc:
            network = Network()
            network.set_config(url=proc.url)

            party_client = network.aio_party(PARTY)
            party_client.add_ledger_ready(lambda _: create(Complicated.OperatorRole, {'operator': PARTY}))
            party_client.add_ledger_created(Complicated.OperatorRole, _create_empty_notification)
            party_client.add_ledger_created(Complicated.OperatorRole, _create_complicated_notifications)
            party_client.add_ledger_created(Complicated.OperatorFormulaNotification, lambda e: setitem(recorded_data, e.cid, e.cdata))
            network.run_until_complete()

        print('got to the end with contracts: ', recorded_data)
        self.assertEqual(len(recorded_data), 4)


def _create_complicated_notifications(e) -> list:
    return [
        exercise(e.cid, 'PublishFormula', dict(formula={'Tautology': {}})),
        exercise(e.cid, 'PublishFormula', dict(formula={'Contradiction': {}})),
        exercise(e.cid, 'PublishFormula', dict(formula={'Proposition': 'something'})),
        exercise(e.cid, 'PublishFormula', dict(formula={'Conjunction': [{'Proposition': 'something_else'}]})),
    ]


def _create_empty_notification(e) -> list:
    return [exercise(e.cid, 'PublishEmpty')]
