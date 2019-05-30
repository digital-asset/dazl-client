# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from functools import partial
from operator import setitem
from unittest import TestCase
from pathlib import Path

from dazl import sandbox, create_client, create, exercise
from dazl.model.core import ContractId

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'Complicated.daml'
PARTY = 'Operator'


class Complicated:
    OperatorRole = 'Complicated.OperatorRole'
    OperatorFormulaNotification = 'Complicated.OperatorFormulaNotification'


class ComplicatedTypesTest(TestCase):
    def test_complicated_types(self):
        recorded_data = dict()
        with sandbox(DAML_FILE) as proc:
            with create_client(participant_url=proc.url, parties=[PARTY]) as client:
                party_client = client.client(PARTY)
                party_client.on_ready(lambda *args, **kwargs: create(Complicated.OperatorRole, {'operator': PARTY}))
                party_client.on_created(Complicated.OperatorRole, _create_empty_notification)
                party_client.on_created(Complicated.OperatorRole, _create_complicated_notifications)
                party_client.on_created(Complicated.OperatorFormulaNotification, partial(setitem, recorded_data))
                client.run_until_complete()

        print('got to the end with contracts: ', recorded_data)
        self.assertEqual(len(recorded_data), 4)


def _create_complicated_notifications(cid: ContractId, cdata: dict) -> list:
    return [
        exercise(cid, 'PublishFormula', dict(formula={'Tautology': {}})),
        exercise(cid, 'PublishFormula', dict(formula={'Contradiction': {}})),
        exercise(cid, 'PublishFormula', dict(formula={'Proposition': 'something'})),
        exercise(cid, 'PublishFormula', dict(formula={'Conjunction': [{'Proposition': 'something_else'}]})),
    ]


def _create_empty_notification(cid: ContractId, cdata: dict) -> list:
    return [ exercise(cid, 'PublishEmpty') ]
