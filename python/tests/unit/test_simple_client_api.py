# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dazl import sandbox, simple_client, LOG

DAML_FILE = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'


def test_simple_client_api():
    party = 'abc'

    LOG.info('Creating sandbox...')
    with sandbox(daml_path=DAML_FILE) as proc:
        LOG.info('Creating client...')
        with simple_client(url=proc.url, party=party) as client:
            client.ready()
            LOG.info('Submitting...')
            client.submit_create('Main.PostmanRole', {'postman': party})
            LOG.info('getting contracts')
            contracts = client.find_active('*')
            LOG.info('got the contracts')

    assert 1 == len(contracts)
