# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from asyncio import sleep
from unittest import TestCase

from aiohttp import ClientSession

from dazl import Network, sandbox, create, exercise_by_key
from dazl.model.core import Party
from .dars import TestServer as TestServerDar


Alice = Party("Alice")
Bob = Party("Bob")
Carol = Party("Carol")


LOG = logging.getLogger('test_server')


class TestServer(TestCase):
    def test_server_endpoint(self):
        SERVER_PORT = 53390
        with sandbox(TestServerDar) as proc:
            bot_main(sandbox_url=proc.url, server_port=SERVER_PORT)


def ensure_person_contract(network: Network, party: Party):
    network.aio_party(party).add_ledger_ready(lambda _: create('TestServer:Person', dict(party=party)))


def bot_main(sandbox_url, server_port):
    """
    The 'dazl app' being tested.
    """

    network = Network()
    network.set_config(url=sandbox_url, server_port=server_port)

    network.aio_party(Alice)
    bob = network.aio_party(Bob)
    carol = network.aio_party(Carol)

    # create Person contracts for each party
    for party in [Alice, Bob, Carol]:
        ensure_person_contract(network, party)

    # have Bob start up "suspended"; we'll start up Bob from the outside
    bob_bot = bob._impl.bots.add_new("Bob's Bot")
    bob_bot.pause()
    @bob_bot.ledger_created('TestServer.Person')
    def bob_sends_a_message(_):
        return exercise_by_key(
            'TestServer:Person', Bob, 'SayHello', {'receiver': Alice, 'text': "Bob's ultra secret message"})

    @carol.ledger_created('TestServer.Person')
    def carol_sends_a_message(_):
        return exercise_by_key(
            'TestServer:Person', Carol, 'SayHello', {'receiver': Alice, 'text': "Carol's gonna Carol"})

    # Carol will start Bob only once Alice has processed three events
    network.run_until_complete(client_main(network, server_port))


async def client_main(network: Network, server_port: int):
    """
    The main method of a client running against the server endpoint exposed by the dazl app above.
    """
    LOG.info('client_main: started.')
    try:
        async with ClientSession() as session:
            await wait_for_ready(session, server_port, [Alice, Bob, Carol])

            # start Bob from the administration endpoint
            bots_response = await session.get(f'http://localhost:{server_port}/bots')
            bots = await bots_response.json()
            bobs_bots = [bot for bot in bots['bots'] if bot['party'] == Bob]
            for bobs_bot in bobs_bots:
                await session.post(f'http://localhost:{server_port}/bots/{bobs_bot["id"]}/state/resume')

            # now make sure Alice received Bob's message, and not Carol's (because Carol was never started)
            alice = network.aio_party(Alice)
            _, cdata = await alice.find_one('TestServer:Message')
            LOG.info('Received message from %r: %r', cdata['sender'], cdata['text'])

            all_messages = alice.find('TestServer:Message')
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
