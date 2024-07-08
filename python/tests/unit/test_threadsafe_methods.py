# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import simple_client
from dazl.ledger import ExerciseCommand
from dazl.testing import SandboxLauncher

from .blocking_setup import blocking_setup
from .dars import Simple

OperatorRole = "Simple:OperatorRole"
OperatorNotification = "Simple:OperatorNotification"


def test_threadsafe_methods(sandbox: SandboxLauncher) -> None:
    party = blocking_setup(sandbox.url, Simple)

    with simple_client(url=sandbox.url, party=party) as client:
        client.ready()
        client.create(OperatorRole, {"operator": party})

        operator_cid, _ = client.find_one(OperatorRole)

        client.exercise(operator_cid, "PublishMany", dict(count=5))

        notifications = client.find_nonempty(OperatorNotification, {"operator": party}, min_count=5)
        contracts_to_delete = []
        for cid, cdata in notifications.items():
            if int(cdata["text"]) <= 3:
                contracts_to_delete.append(cid)

        client.submit([ExerciseCommand(cid, "Archive") for cid in contracts_to_delete])

        client.exercise(operator_cid, "PublishMany", dict(count=3))

        print(client.find_active("*"))
