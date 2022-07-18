# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

from dazl.ledger import ExerciseCommand
from dazl.testing import connect_with_new_party
import pytest

from .dars import Complicated as ComplicatedDar


class Complicated:
    OperatorRole = "Complicated:OperatorRole"
    OperatorFormulaNotification = "Complicated:OperatorFormulaNotification"


@pytest.mark.asyncio
async def test_complicated_types(sandbox):
    async with connect_with_new_party(url=sandbox, dar=ComplicatedDar) as p:
        await p.connection.create(Complicated.OperatorRole, {"operator": p.party})

        async with p.connection.query(Complicated.OperatorRole) as stream:
            async for event in stream.creates():
                await p.connection.exercise(event.contract_id, "PublishEmpty")
                await p.connection.submit(
                    [
                        ExerciseCommand(
                            event.contract_id, "PublishFormula", dict(formula={"Tautology": {}})
                        ),
                        ExerciseCommand(
                            event.contract_id, "PublishFormula", dict(formula={"Contradiction": {}})
                        ),
                        ExerciseCommand(
                            event.contract_id,
                            "PublishFormula",
                            dict(formula={"Proposition": "something"}),
                        ),
                        ExerciseCommand(
                            event.contract_id,
                            "PublishFormula",
                            dict(formula={"Conjunction": [{"Proposition": "something_else"}]}),
                        ),
                    ]
                )

        payloads = []
        async with p.connection.query(Complicated.OperatorFormulaNotification) as stream:
            async for event in stream.creates():
                payloads.append(event.payload)

    logging.info("got to the end with contracts: %s", payloads)
    assert len(payloads) == 4
