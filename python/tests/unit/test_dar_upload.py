# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import new_event_loop, set_event_loop, sleep
from unittest import TestCase

from dazl import Network, sandbox
from .dars import AllKindsOf


class TestDarUpload(TestCase):
    def test_dar_uploads_near_startup(self):
        set_event_loop(new_event_loop())

        package_ids = []

        with sandbox([]) as proc:
            network = Network()
            network.set_config(url=proc.url)

            async def upload_dars_and_verify():
                await upload_test_dars(network)
                metadata = await network.aio_global().metadata()
                package_ids.extend(metadata.store.package_ids())

            network.run_until_complete(upload_dars_and_verify())

        self.assertGreater(len(package_ids), 0)

    def test_package_events(self):
        set_event_loop(new_event_loop())

        initial_events = []
        follow_up_events = []

        with sandbox([]) as proc:
            network = Network()
            network.set_config(url=proc.url)
            client = network.aio_party('TestParty')

            async def upload_dars_and_verify():
                # make sure the client is "ready" before uploading DARs, because we are explicitly
                # checking to make sure proper reporting of packages that are uploaded after a
                # client is running and # operational
                await client.ready()
                await upload_test_dars(network)

                # give the client some time to pick up the new packages; unfortunately there isn't
                # much more to do here except wait
                await sleep(10)

            client.add_ledger_packages_added(initial_events.append, initial=True)
            client.add_ledger_packages_added(follow_up_events.append)
            network.run_until_complete(upload_dars_and_verify())

        self.assertEqual(len(initial_events), 2)
        self.assertEqual(len(follow_up_events), 1)


async def upload_test_dars(network: 'Network'):
    g = network.aio_global()
    await g.ensure_dar(AllKindsOf.read_bytes())
