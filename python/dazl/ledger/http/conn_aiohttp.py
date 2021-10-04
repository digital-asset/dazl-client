# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Implementation of :class:`Connection` that uses ``aiohttp`` under the hood.
"""

import asyncio
from asyncio import run_coroutine_threadsafe
from threading import Thread
from typing import Awaitable, Callable, Optional, Sequence, TypeVar, Union

from aiohttp import ClientSession

from ..api_types import Command, CreateCommand, CreateEvent, ExerciseCommand
from ..blocking import Connection as BlockingConnection
from ..config import Config
from .codec_aio import Codec
from ...damlast import TypeConName
from ...prim import ContractData

R = TypeVar('R')

class Connection:
    def __init__(self, config: "Config"):
        self.session = ClientSession()
        self.config = config
        self.codec = Codec(self)

    async def submit(self, __commands: "Union[Command, Sequence[Command]]", *, workflow_id: "Optional[str]" = None, command_id: "Optional[str]" = None):
        if isinstance(__commands, Command):
            __commands = (__commands,)

        if command_id and len(__commands) > 1:
            raise ValueError('cannot submit a command ID with the HTTP JSON API when more than one command is specified')

        for cmd in __commands:
            if isinstance(cmd, CreateCommand):
                await self.create(cmd, workflow_id=workflow_id, command_id=command_id)
            elif isinstance(cmd, ExerciseCommand):
                await self.exercise(cmd, workflow_id=workflow_id, command_id=command_id)

    async def create(self, __template_id: "Union[str, TypeConName]", __payload: "ContractData", *, workflow_id: "Optional[str]" = None, command_id: "Optional[str]" = None):
        path, body = self.codec.encode_create_command(__template_id, __payload)
        if command_id:
            body["meta"] = {"commandId": command_id}
        async with self.session.post(f"{self.config.url.url}/{path}", data=body)  as response:
            return await self.codec.decode_create_event(await response.json())



def blocking(config: "Config") -> "BlockingConnection":
    loop = asyncio.get_event_loop()


class BC:
    def __init__(self):
        self._thread = Thread(target=self._main)

    def open(self):
        self._thread.run()

    def close(self):
        self._thread.join()

    def _main(self):
        self._loop = asyncio.new_event_loop()
        self._loop.run_until_complete(self.__main())

    async def __main(self):
        self._conn = Connection()

    def submit(self, *args, **kwargs) -> "None":
        fut = run_coroutine_threadsafe(self._conn.submit(*args, **kwargs), self._loop)
        fut.result()

    def create(self, *args, **kwargs) -> "CreateEvent":
        fut = run_coroutine_threadsafe(self._conn.create(*args, **kwargs), self._loop)
        return fut.result()
