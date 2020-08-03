# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import sandbox, simple_client, LOG

from .dars import PostOffice


def test_simple_client_api():
    party = 'abc'

    LOG.info('Creating sandbox...')
    with sandbox(dar_path=PostOffice) as proc:
        LOG.info('Creating client...')
        with simple_client(url=proc.url, party=party) as client:
            client.ready()
            LOG.info('Submitting...')
            client.submit_create('Main.PostmanRole', {'postman': party})
            LOG.info('getting contracts')
            contracts = client.find_active('*')
            LOG.info('got the contracts')

    assert 1 == len(contracts)
