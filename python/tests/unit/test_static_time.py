# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Test of two clients operating simultaneously.
"""

import logging
import unittest

from asyncio import gather, get_event_loop, ensure_future
from datetime import datetime
from pathlib import Path

from dazl import create, exercise, sandbox, Network, setup_default_logger

TEMPLATE_DAML_FILE = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'

LOG = logging.getLogger('test_static_time')

setup_default_logger(logging.DEBUG)
PARTY = 'POSTMAN'


class TestStaticTime(unittest.TestCase):
    def test_set_static_time(self):
        """
        Run a simple test involving manipulation of static time:
         * Send a command at ledger startup.
         * Upon receipt of a corresponding event, advance the time and submit a new command
         * Observe a corresponding event has been received.
        """
        with sandbox(TEMPLATE_DAML_FILE) as damli_proc:
            network = Network()
            network.set_config(url=damli_proc.url)

            async def _handle_postman_role(event):
                try:
                    LOG.info('Received the postman role contract.')
                    await network.aio_global().set_time(datetime(1980, 1, 1))
                    return exercise(event.cid, 'InviteParticipant', dict(party=PARTY, address='something'))
                except BaseException as ex:
                    LOG.exception(ex)

            def _invitation_seen(event):
                LOG.info('Invitation seen, so the app will be terminating now.')
                network.shutdown()

            LOG.info('Adding event listeners to the application...')
            client = network.aio_party(PARTY)
            client.add_ledger_ready(lambda _: create('Main.PostmanRole', dict(postman=PARTY)))
            client.add_ledger_created('Main.PostmanRole', _handle_postman_role)

            # run the manager "forever"; we'll stop ourselves manually when we see an author role
            # because that means our call to invite an author was successful
            client.add_ledger_created('Main.InviteAuthorRole', _invitation_seen)
            network.run_forever()

            LOG.info('Application finished.')

    def test_set_static_time_two_clients(self):
        """
        Run a slightly complicated test involving manipulation of static time and multiple clients:
         * Client 1 sends a command at ledger startup.
         * Client 2 also listens for the command.
         * When both Client 1 and Client 2 have heard the original command, Client 1 advances the
           time and shuts down WITHOUT producing a new command.
         * After Client 1 is shut down, Client 2 manually syncs its local time and submits a command
           to the Sandbox.
         * Observe Client 2 receives its corresponding event.
        """
        event_loop = get_event_loop()
        with sandbox(TEMPLATE_DAML_FILE) as damli_proc:
            test = _TestSetStaticTimeTwoClients(damli_proc.url)
            event_loop.run_until_complete(test.main())


class _TestSetStaticTimeTwoClients:

    def __init__(self, url):
        self.manager1 = Network()
        self.manager1.set_config(url=url)

        self.manager2 = Network()
        self.manager2.set_config(url=url)

        self.manager1.aio_party(PARTY).add_ledger_ready(self._handle_ready_1)
        self.manager2.aio_party(PARTY).add_ledger_ready(self._handle_ready_2)
        self.manager1.aio_party(PARTY).add_ledger_created('Main.PostmanRole', self._handle_postman_role_1)
        self.manager2.aio_party(PARTY).add_ledger_created('Main.PostmanRole', self._handle_postman_role_2)

    async def main(self):
        # begin both clients
        m1 = ensure_future(self.manager1.aio_run())
        m2 = ensure_future(self.manager2.aio_run())

        # wait for the first manager to shut itself down; this will have happened in
        # the _handle_postman_role_1 callback
        await gather(m1, self.manager2.aio_party(PARTY).ready())

        # now ensure that the second client's time is in sync with the Sandbox
        await self.manager2.aio_global().get_time()
        # TODO: Come up with a better signal to be ABSOLUTELY sure that the second client is
        #  "caught up" with the current time
        from asyncio import sleep
        await sleep(1.0)

        # this call can only succeed if the second client knows of the time as it was set by the
        # first party
        await self.manager2.aio_party(PARTY).submit(
            exercise(self.postman_cid, 'InviteParticipant', dict(party=PARTY, address='something')))

        # shut down the second client
        self.manager2.shutdown()

        # wait for it to stop cleanly
        await m2

    def _handle_ready_1(self, _):
        LOG.info('Client 1 is now ready: sending the initial postman role contract...')
        return create('Main.PostmanRole', dict(postman=PARTY))

    def _handle_ready_2(self, _):
        LOG.info('Client 2 is now ready.')

    async def _handle_postman_role_1(self, _):
        LOG.info('Received the postman role contract; advancing time and shutting down.')
        await self.manager1.aio_global().set_time(datetime(1980, 1, 1))
        self.manager1.shutdown()

    async def _handle_postman_role_2(self, event):
        LOG.info('Received the postman role contract; ')
        self.postman_cid = event.cid
