# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from unittest import TestCase

from dazl import frozendict, sandbox, simple_client

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'MapSupport.daml'


class TestMapSupport(TestCase):
    def test_map_support(self):
        with sandbox(daml_path=DAML_FILE) as proc:
            with simple_client(url=proc.url, party='Test') as client:
                client.ready()
                client.submit_create('MapSupport.Sample', {
                    'party': 'Test',
                    'mappings': {
                        65: 'A',
                        97: 'a'
                    },
                    'text': None
                })
                print(client.find_active('*'))

    def test_complicated_map_support(self):
        with sandbox(daml_path=DAML_FILE) as proc:
            with simple_client(url=proc.url, party='Test') as client:
                client.ready()
                client.submit_create('MapSupport.ComplicatedSample', {
                    'party': 'Test',
                    # Note: Python `dict`s are not hashable, so the only way to write this out
                    # is to create a special dict as a key
                    'keyIsMap': {frozendict(A='b'): 'mmm'},
                    'keyIsRecord': {frozendict(x=2, y=4): 'rrr'},
                    'keyIsRecordWithTypeParam': {frozendict(x=2, y=4): 'rrr'},
                    'keyIsVariant': {frozendict(Apple=''): 'ttt'}
                })
                print(client.find_active('*'))
