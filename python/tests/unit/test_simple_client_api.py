# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

from dazl import simple_client

from .blocking_setup import blocking_setup
from .dars import PostOffice


def test_simple_client_api(sandbox):
    party = blocking_setup(sandbox, PostOffice)

    logging.info("Creating client...")
    with simple_client(url=sandbox, party=party) as client:
        client.ready()
        logging.info("Submitting...")
        client.create("Main:PostmanRole", {"postman": party})
        logging.info("getting contracts")
        contracts = client.find_active("*")
        logging.info("got the contracts")

    assert 1 == len(contracts)
