# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import aiohttp
from aiohttp import ClientSession

from ..config import Config

__all__ = ["Connection"]


class Connection:

    def __init__(self, config: "Config"):
        self.config = config
        self.session = ClientSession()

    async def open(self) -> None:
        pass

    async def close(self) -> None:
        await self.session.close()


class QueryStream:
    def __init__(self, session: "ClientSession"):
        self.session = session

    async def items(self):
        async with self.session.ws_connect() as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == '':

