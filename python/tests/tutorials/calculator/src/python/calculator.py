# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import logging
from csv import DictReader
from pathlib import Path
from typing import List

from dazl import sandbox, create_client, create, exercise, setup_default_logger
from dazl.client import ParticipantLedgerClient


LOG = logging.getLogger('calculator')
SRC_ROOT = Path(__file__).parent.parent

DAML_PATH = SRC_ROOT / 'daml' / 'Calculator.daml'
CLIENTS_PATH = SRC_ROOT / 'data' / 'clients.csv'

ClientRole = 'Calculator.ClientRole'


def get_client_role_data() -> List[dict]:
    with CLIENTS_PATH.open('r') as f:
        return list(DictReader(f))


def run_sandbox_and_app() -> None:
    with sandbox(dar_path=DAML_PATH) as proc:
        run_app(proc.url)


def run_app(url: str):
    client_role_dicts = get_client_role_data()
    all_parties = tuple(c['client'] for c in client_role_dicts) + ('Processor',)

    with create_client(participant_url=url, parties=all_parties) as client_mgr:
        for client_role_dict in client_role_dicts:
            client = client_mgr.client(client_role_dict['client'])
            client.on_ready(lambda *args, **kwargs: create(ClientRole, client_role_dict))

        register_processor_callbacks('Processor', client_mgr.client('Processor'))


def register_processor_callbacks(processor_party: str, processor: ParticipantLedgerClient) -> None:
    def accept_request(cid, cdata):
        if cdata['relationship']['processor'] == processor_party:
            return exercise(cid, 'AcceptRequest')

    processor.on_created(ClientRole, accept_request)


def register():
    pass


if __name__ == '__main__':
    setup_default_logger()
    run_sandbox_and_app()
