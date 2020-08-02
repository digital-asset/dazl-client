# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl import sandbox, simple_client
from .dars import DottedFields


def test_record_dotted_fields_submit():
    with sandbox(dar_path=DottedFields) as proc:
        with simple_client(url=proc.url, party='Test') as client:
            client.ready()
            client.submit_create('DottedFields.American', {
                'person': 'Test',
                'address.address': '1 Test Place',
                'address.city': 'Somewhere',
                'address.state': 'ZZ',
                'address.zip': '99999'
            })

            logging.info(client.find_active('DottedFields.American'))


def test_variant_dotted_fields_submit():
    with sandbox(dar_path=DottedFields) as proc:
        with simple_client(url=proc.url, party='Test') as client:
            client.ready()
            client.submit_create('DottedFields.Person', {
                'person': 'Test',
                'address.US.address': '1 Test Place',
                'address.US.city': 'Somewhere',
                'address.US.state': 'ZZ',
                'address.US.zip': '99999',
                'address.UK.address': '',
                'address.UK.locality': '',
                'address.UK.city': '',
                'address.UK.state': '',
                'address.UK.postcode': '',

            })

            logging.info(client.find_active('DottedFields.Person'))
