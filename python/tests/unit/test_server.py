# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from asyncio import sleep

import pytest
from aiohttp import ClientSession

from dazl import async_network, create, exercise_by_key, Network
from dazl.model.core import Party
from .dars import TestServer as TestServerDar


LOG = logging.getLogger('test_server')


@pytest.mark.asyncio
async def test_server_endpoint(sandbox):
    SERVER_PORT = 53390
    async with async_network(url=sandbox, dars=TestServerDar) as network:
        network.set_config(server_port=SERVER_PORT)

        alice_client = network.aio_new_party()
        alice = alice_client.party

        bob_client = network.aio_new_party()
        bob = bob_client.party

        carol_client = network.aio_new_party()
        carol = carol_client.party

        # create Person contracts for each party
        for party in [alice, bob, carol]:
            ensure_person_contract(network, party)

        # have Bob start up "suspended"; we'll start up Bob from the outside
        bob_bot = bob_client._impl.bots.add_new("Bob's Bot")
        bob_bot.pause()

        @bob_bot.ledger_created('TestServer:Person')
        def bob_sends_a_message(_):
            return exercise_by_key(
                'TestServer:Person', bob, 'SayHello', {'receiver': alice, 'text': "Bob's ultra secret message"})

        @carol_client.ledger_created('TestServer:Person')
        def carol_sends_a_message(_):
            return exercise_by_key(
                'TestServer:Person', carol, 'SayHello', {'receiver': alice, 'text': "Carol's gonna Carol"})

        # Carol will start Bob only once Alice has processed three events
        await network.aio_run(client_main(network, SERVER_PORT, alice, bob, carol), keep_open=False)


def ensure_person_contract(network: Network, party: Party):
    network.aio_party(party).add_ledger_ready(lambda _: create('TestServer:Person', dict(party=party)))


async def client_main(
        network: Network, server_port: int,
        alice: 'Party', bob: 'Party', carol: 'Party'):
    """
    The main method of a client running against the server endpoint exposed by the dazl app above.
    """
    LOG.info('client_main: started.')
    try:
        async with ClientSession() as session:
            await wait_for_ready(session, server_port, [alice, bob, carol])

            # start Bob from the administration endpoint
            bots_response = await session.get(f'http://localhost:{server_port}/bots')
            bots = await bots_response.json()
            bobs_bots = [bot for bot in bots['bots'] if bot['party'] == bob]
            for bobs_bot in bobs_bots:
                await session.post(f'http://localhost:{server_port}/bots/{bobs_bot["id"]}/state/resume')

            # now make sure Alice received Bob's message, and not Carol's (because Carol was never started)
            alice_client = network.aio_party(alice)
            _, cdata = await alice_client.find_one('TestServer:Message')
            LOG.info('Received message from %r: %r', cdata['sender'], cdata['text'])

            all_messages = alice_client.find('TestServer:Message')
            LOG.info('Alice has a total of %d message(s).', len(all_messages))

            if len(all_messages) > 1:
                raise AssertionError('Alice was only supposed to have one message')

        LOG.info('client_main: finished.')
    except Exception:
        LOG.exception('client_main: failed.')


async def wait_for_ready(session, server_port, parties):
    """
    Block until the dazl server reports these parties as all being ready.
    """
    while True:
        response = await session.get(f'http://localhost:{server_port}/readyz')
        if response.status == 200:
            body = await response.json()
            ready_parties = [key for key, value in body['parties'].items() if value['ready']]
            if set(ready_parties) == set(parties):
                LOG.info('Everyone is now ready.')
                return
        else:
            LOG.warning('readyz returned a non-200 error code: %r', response.status)
        await sleep(0.2)
