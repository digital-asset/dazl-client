# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains base classes for the async- and blocking flavors of the gRPC connection
classes.

The translation from async connections to blocking connections is very mechanical; it generally just
means dropping the "async" and "await" keywords. The translations that are _not_ mechanical are
implemented in this module.
"""
from asyncio import gather
from typing import TYPE_CHECKING, Awaitable, Callable, Iterable, Optional, Sequence, TypeVar

from grpc import Channel as BlockingChannel, ChannelConnectivity
from grpc.aio import Channel as AioChannel, UnaryStreamCall

from ..aio import Connection as AioConnection
from ..blocking import Connection as BlockingConnection
from ..config import Config
from .channel import create_channel
from .codec_aio import Codec as AioCodec
from .codec_blocking import Codec as BlockingCodec

if TYPE_CHECKING:
    from grpc import CallIterator

__all__ = ["AioConnectionBase", "BlockingConnectionBase"]

T = TypeVar("T")
U = TypeVar("U")
AioSelf = TypeVar("AioSelf", bound="AioConnectionBase")
BlockingSelf = TypeVar("BlockingSelf", bound="BlockingConnectionBase")


class AioConnectionBase(AioConnection):
    def __init__(self, config: Config):
        self._config = config
        self._logger = config.logger
        self._channel = create_channel(config)
        self._codec = AioCodec(self)

    @property
    def config(self) -> Config:
        return self._config

    @property
    def channel(self) -> "AioChannel":
        """
        Provides access to the underlying gRPC channel.
        """
        return self._channel

    @property
    def codec(self) -> "AioCodec":
        return self._codec

    @property
    def is_closed(self) -> bool:
        return self._channel.get_state(try_to_connect=False) == ChannelConnectivity.SHUTDOWN

    async def __aenter__(self: "AioSelf") -> "AioSelf":
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    @staticmethod
    async def map(__func: "Callable[[T], Awaitable[U]]", __iter: "Iterable[T]") -> "Sequence[U]":
        return await gather(*map(__func, __iter))


class BlockingConnectionBase(BlockingConnection):
    def __init__(self, config: Config):
        self._config = config
        self._logger = config.logger
        self._channel = create_channel(config, blocking=True)
        self._channel.subscribe(self._monitor_state, try_to_connect=False)
        self._is_closed = False
        self._codec = BlockingCodec(self)

    @property
    def config(self) -> Config:
        return self._config

    @property
    def channel(self) -> "BlockingChannel":
        """
        Provides access to the underlying gRPC channel.
        """
        return self._channel

    @property
    def codec(self) -> "BlockingCodec":
        return self._codec

    @property
    def is_closed(self) -> bool:
        return self._is_closed

    def _monitor_state(self, state: "ChannelConnectivity"):
        if state == ChannelConnectivity.SHUTDOWN:
            self._is_closed = True

    def __enter__(self: "BlockingSelf") -> "BlockingSelf":
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    @staticmethod
    def map(__func: "Callable[[T], U]", __iter: "Iterable[U]") -> "Sequence[U]":
        return [__func(obj) for obj in __iter]


class AioQueryStreamBase:
    _response_stream: "Optional[UnaryStreamCall]" = None
    _closed: bool = False


class BlockingQueryStreamBase:
    _response_stream: "Optional[CallIterator]" = None
    _closed: bool = False
