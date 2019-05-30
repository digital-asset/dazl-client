# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from pathlib import Path
from unittest import TestCase

from dazl import simple_client, sandbox, setup_default_logger
from dazl.model.reading import ReadyEvent


DAML_PATH = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'
SAMPLE_PARTY = 'TestParty'

setup_default_logger(logging.INFO)


class TestEventHandlerExceptions(TestCase):
    def test_event_handler_exceptions(self):
        with sandbox(daml_path=DAML_PATH) as proc:
            with simple_client(proc.url, SAMPLE_PARTY) as client:
                def throw_error(event: ReadyEvent):
                    raise MagicException(event.ledger_id)

                client.add_ledger_ready(throw_error)
                client.ready()


class MagicException(Exception):
    pass

