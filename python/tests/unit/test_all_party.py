# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from unittest import TestCase
from pathlib import Path

from dazl import sandbox, create_client, create, setup_default_logger

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'AllParty.daml'
SOME_PARTY = 'SomeParty'
PUBLISHER = 'Publisher'
ALL_PARTY = '000'
PrivateContract = 'AllParty.PrivateContract'
PublicContract = 'AllParty.PublicContract'

setup_default_logger(logging.DEBUG)


class AllPartyTest(TestCase):
    def test_some_party_receives_public_contract(self):
        some_party_cids = []
        publisher_cids = []
        with sandbox(DAML_FILE, extra_args=None) as proc:
            with create_client(participant_url=proc.url, parties=[SOME_PARTY, PUBLISHER], party_groups=[ALL_PARTY]) as client:
                some_client = client.client(SOME_PARTY)
                some_client.on_ready(lambda *args, **kwargs: create(PrivateContract, {'someParty': SOME_PARTY}))

                publisher_client = client.client(PUBLISHER)
                publisher_client.on_ready(lambda *args, **kwargs: create(PublicContract, {'publisher': PUBLISHER, 'allParty': ALL_PARTY}))

                some_client.on_created(PublicContract, lambda cid, cdata: some_party_cids.append(cid))
                some_client.on_created(PrivateContract, lambda cid, cdata: some_party_cids.append(cid))

                publisher_client.on_created(PublicContract, lambda cid, cdata: publisher_cids.append(cid))
                publisher_client.on_created(PrivateContract, lambda cid, cdata: publisher_cids.append(cid))

                client.run_until_complete()

        print(f'got to the end with some_party contracts: {some_party_cids} and publisher contracts: {publisher_cids}')
        self.assertEqual(len(some_party_cids), 2)
        self.assertEqual(len(publisher_cids), 1)
