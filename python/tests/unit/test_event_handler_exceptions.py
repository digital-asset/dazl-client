# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dazl import simple_client, sandbox
from dazl.model.reading import ReadyEvent


DAML_PATH = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'
SAMPLE_PARTY = 'TestParty'


def test_event_handler_exceptions():
    with sandbox(daml_path=DAML_PATH) as proc:
        with simple_client(proc.url, SAMPLE_PARTY) as client:
            def throw_error(event: ReadyEvent):
                raise MagicException(event.ledger_id)

            client.add_ledger_ready(throw_error)
            client.ready()


class MagicException(Exception):
    pass

