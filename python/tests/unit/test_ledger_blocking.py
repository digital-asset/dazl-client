# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
import threading

from dazl import Party, connect
from dazl.ledger import CreateEvent
from dazl.testing import SandboxLauncher

from .dars import PostOffice


def test_blocking_api(sandbox: SandboxLauncher) -> None:
    # allocate some parties
    with connect(url=sandbox.url, blocking=True, admin=True) as conn:
        conn.upload_package(PostOffice.read_bytes())
        operator = conn.allocate_party().party
        party = conn.allocate_party().party

    # connect as an operator, then create a contract
    logging.info("Connecting as the operator...")
    with connect(url=sandbox.url, blocking=True, act_as=operator) as conn:
        logging.info("Let's create some contracts!")
        conn.create("Main:PostmanRole", {"postman": operator})
        conn.exercise_by_key(
            "Main:PostmanRole",
            "InviteParticipant",
            operator,
            {"party": party, "address": "21 Jump Street"},
        )

    # now connect as the party, and verify that they can see the created contract
    logging.info("Connecting as the primary party...")
    with connect(url=sandbox.url, blocking=True, read_as=party) as conn:
        seen_contracts = list[CreateEvent]()
        logging.info("Looking for contracts...")
        with conn.query("Main:InviteAuthorRole") as stream:
            seen_contracts.extend(stream.creates())

    assert len(seen_contracts) == 1


def test_multiple_blocking_apis(sandbox: SandboxLauncher) -> None:
    """
    Ensure that two completely separate threads can use blocking dazl calls without stepping on
    each other.

    Note that this bug causes a LOT of scary noise in the logs, but otherwise seems to be harmless
    for dazl use cases (there are no stream-stream calls in the current gRPC Ledger API):
        https://github.com/grpc/grpc/issues/25364
    """
    # allocate some parties
    with connect(url=sandbox.url, blocking=True, admin=True) as conn:
        conn.upload_package(PostOffice.read_bytes())
        p1 = conn.allocate_party().party
        p2 = conn.allocate_party().party

    # we're going to wait for both threads to
    evt = threading.Event()

    def main(party: Party) -> None:
        with connect(url=sandbox.url, blocking=True, act_as=party) as conn:
            evt.wait()
            conn.create("Main:PrivateNote", {"party": party, "text": "note1"})
            conn.create("Main:PrivateNote", {"party": party, "text": "note2"})
            conn.create("Main:PrivateNote", {"party": party, "text": "note3"})

    t1 = threading.Thread(target=lambda: main(p1))
    t2 = threading.Thread(target=lambda: main(p2))
    t1.start()
    t2.start()
    evt.set()
    t1.join()
    t2.join()

    with connect(url=sandbox.url, blocking=True, read_as=[p1, p2]) as conn:
        with conn.query("Main:PrivateNote") as stream:
            assert sum(1 for _ in stream.creates()) == 6
