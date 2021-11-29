# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import new_event_loop, set_event_loop
from threading import Thread

from dazl import Network, Party
from dazl.damlast.pkgfile import Dar


def blocking_setup(url: str, dar: Dar) -> "Party":
    """
    Set up a ledger for a test in a completely blocking fashion.

    Used by the tests that test the thread-safe variants of the dazl API where
    avoiding contamination of the current async context is more important than
    the performance ramifications of calling this function.

    :param url:
        The URL of the remote Ledger API implementation to connect to.
    :param dar:
        A DAR file.
    :return:
        A newly allocated ``Party`` that is guaranteed to be used by no other
        client.
    """
    return Setup(url, dar).run()


class Setup:
    def __init__(self, url, dar):
        self.url = url
        self.party = None
        self.dar = dar
        self.network = None

    def run(self):
        # upload our DAR and allocate our Party in a completely separate thread as to try to avoid
        # polluting the current context
        t = Thread(target=self._main)
        t.start()
        t.join()
        return self.party

    def _main(self):
        # create a private event loop just for us
        set_event_loop(new_event_loop())

        self.network = Network()
        self.network.set_config(url=self.url)

        client = self.network.aio_new_party()

        self.party = client.party

        self.network.run_until_complete(self.upload_dar())

    async def upload_dar(self):
        await self.network.aio_global().ensure_dar(self.dar)
