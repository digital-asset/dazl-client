# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from pathlib import Path
from unittest import TestCase

from dazl import sandbox, setup_default_logger
from dazl.client.api import simple_client

DAML_FILE = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'

setup_default_logger(logging.DEBUG)


class TestSimpleClientApi(TestCase):

    def test_simple_client_api(self):
        party = 'abc'
        print('creating sandbox')
        with sandbox(daml_path=DAML_FILE) as proc:
            print('creating client')
            with simple_client(url=proc.url, party=party) as client:
                client.ready()
                print('submitting')
                client.submit_create('Main.PostmanRole', {'postman': party})
                print('getting contracts')
                contracts = client.find_active('*')
                print('got the contracts')

        self.assertEqual(1, len(contracts))
