# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import simple_client, sandbox
from dazl.model.reading import ReadyEvent

from .dars import PostOffice


SAMPLE_PARTY = 'TestParty'


def test_event_handler_exceptions():
    with sandbox(dar_path=PostOffice) as proc:
        with simple_client(proc.url, SAMPLE_PARTY) as client:
            def throw_error(event: ReadyEvent):
                raise MagicException(event.ledger_id)

            client.add_ledger_ready(throw_error)
            client.ready()


class MagicException(Exception):
    pass

