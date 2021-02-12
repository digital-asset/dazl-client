# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from operator import setitem

import pytest

from dazl import async_network, create, exercise

from .dars import Complicated as ComplicatedDar


class Complicated:
    OperatorRole = "Complicated:OperatorRole"
    OperatorFormulaNotification = "Complicated:OperatorFormulaNotification"


@pytest.mark.asyncio
async def test_complicated_types(sandbox):
    recorded_data = dict()

    async with async_network(url=sandbox, dars=ComplicatedDar) as network:
        party_client = network.aio_new_party()
        party_client.add_ledger_ready(
            lambda event: create(Complicated.OperatorRole, {"operator": event.party})
        )
        party_client.add_ledger_created(Complicated.OperatorRole, _create_empty_notification)
        party_client.add_ledger_created(Complicated.OperatorRole, _create_complicated_notifications)
        party_client.add_ledger_created(
            Complicated.OperatorFormulaNotification,
            lambda e: setitem(recorded_data, e.cid, e.cdata),
        )

        network.start()

    logging.info("got to the end with contracts: %s", recorded_data)
    assert len(recorded_data) == 4


def _create_complicated_notifications(e) -> list:
    return [
        exercise(e.cid, "PublishFormula", dict(formula={"Tautology": {}})),
        exercise(e.cid, "PublishFormula", dict(formula={"Contradiction": {}})),
        exercise(e.cid, "PublishFormula", dict(formula={"Proposition": "something"})),
        exercise(
            e.cid,
            "PublishFormula",
            dict(formula={"Conjunction": [{"Proposition": "something_else"}]}),
        ),
    ]


def _create_empty_notification(e) -> list:
    return [exercise(e.cid, "PublishEmpty")]
