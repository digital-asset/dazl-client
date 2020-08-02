# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import sleep
from random import random

from dazl import Network, sandbox
from .dars import PostOffice


def test_static_dump_and_tail():
    with sandbox(dar_path=PostOffice) as proc:
        seen_contracts = []

        network = Network()
        network.set_config(url=proc.url)
        client = network.simple_party('PARTY')

        @client.ledger_ready()
        def print_initial_state(event):
            print(event.acs_find_active('*'))

        @client.ledger_created('*')
        def print_create(event):
            print(event.cid, event.cdata)
            seen_contracts.append(event.cid)

        async def publish_some_contracts():
            aclient = network.aio_party('PARTY')
            for i in range(0, 5):
                sleep_interval = random()
                print(f'Publishing contract {i}, then sleeping for {sleep_interval} seconds...')
                await aclient.submit_create('Main.PostmanRole', {'postman': 'PARTY'})
                await sleep(sleep_interval)
            network.shutdown()

        network.run_forever(publish_some_contracts())
