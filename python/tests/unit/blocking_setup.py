# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import new_event_loop, set_event_loop
from pathlib import Path
from threading import Thread
from typing import Optional

from dazl import connect
from dazl.prim import Party

__all__ = ["blocking_setup"]


def blocking_setup(url: str, dar: "Path") -> "Party":
    """
    Set up a ledger for a test in a completely blocking fashion.

    Used by the tests that test the thread-safe variants of the dazl API where
    avoiding contamination of the current async context is more important than
    the performance ramifications of calling this function.

    :param url:
        The URL of the remote Ledger API implementation to connect to.
    :param dar:
        Path to a DAR file.
    :return:
        A newly allocated ``Party`` that is guaranteed to be used by no other
        client.
    """
    return Setup(url, dar).run()


class Setup:
    def __init__(self, url: str, dar: "Path"):
        self.url = url
        self.dar = dar
        self.party = None  # type: Optional[Party]

    def run(self) -> "Party":
        # upload our DAR and allocate our Party in a completely separate thread as to try to avoid
        # polluting the current context
        t = Thread(target=self._main)
        t.start()
        t.join()
        if self.party is None:
            raise RuntimeError("party failed to be allocated!")
        return self.party

    def _main(self):
        # create a private event loop just for us
        loop = new_event_loop()
        set_event_loop(loop)
        self.party = loop.run_until_complete(self.__main())

    async def __main(self) -> "Party":
        async with connect(url=self.url, admin=True) as conn:
            party_info = await conn.allocate_party()
            await conn.upload_package(self.dar.read_bytes())

        return party_info.party
