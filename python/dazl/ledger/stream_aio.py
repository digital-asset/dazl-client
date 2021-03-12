# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
from inspect import iscoroutine
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    DefaultDict,
    List,
    TypeVar,
    Union,
    overload,
)
import warnings

from .api_types import ArchiveEvent, Boundary, CreateEvent
from .errors import CallbackReturnWarning

__all__ = ["QueryStreamBase"]

CREATE_EVENT = "create"
ARCHIVE_EVENT = "archive"
BOUNDARY = "boundary"

Self = TypeVar("Self")


class QueryStreamBase:
    @property
    def _callbacks(
        self,
    ) -> "DefaultDict[str, List[Union[Callable[[Any], None], Callable[[Any], Awaitable[None]]]]]":
        cb = getattr(self, "__cb", None)
        if cb is None:
            cb = defaultdict(list)
            object.__setattr__(self, "__cb", cb)
        return cb

    @overload
    def on_boundary(self, fn: "Callable[[Boundary], None]") -> "Callable[[Boundary], None]":
        ...

    @overload
    def on_boundary(
        self, fn: "Callable[[Boundary], Awaitable[None]]"
    ) -> "Callable[[Boundary], Awaitable[None]]":
        ...

    def on_boundary(self, fn):
        if not callable(fn):
            raise ValueError("fn must be a callable")

        self._callbacks[BOUNDARY].append(fn)

    @overload
    def on_create(self, fn: "Callable[[CreateEvent], None]") -> "Callable[[CreateEvent], None]":
        ...

    @overload
    def on_create(
        self, fn: "Callable[[CreateEvent], Awaitable[None]]"
    ) -> "Callable[[CreateEvent], Awaitable[None]]":
        ...

    def on_create(self, fn):
        if not callable(fn):
            raise ValueError("fn must be a callable")

        self._callbacks[CREATE_EVENT].append(fn)

    @overload
    def on_archive(self, fn: "Callable[[ArchiveEvent], None]") -> "Callable[[ArchiveEvent], None]":
        ...

    @overload
    def on_archive(
        self, fn: "Callable[[ArchiveEvent], Awaitable[None]]"
    ) -> "Callable[[ArchiveEvent], Awaitable[None]]":
        ...

    def on_archive(self, fn):
        if not callable(fn):
            raise ValueError("fn must be a callable")

        self._callbacks[ARCHIVE_EVENT].append(fn)

    async def __aenter__(self: Self) -> "Self":
        """
        Prepare the stream.
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Close the stream.
        """

    async def close(self) -> None:
        """
        Close and dispose of any resources used by this stream.
        """

    async def run(self) -> "None":
        """
        "Runs" the stream. This can be called as an alternative to :meth:`items` when using
        callback-based APIs.
        """
        async for _ in self:
            pass

    async def creates(self) -> "AsyncIterator[CreateEvent]":
        """
        Return a stream of :class:`CreateEvent`s. This will include the contracts of the
        Active Contract Set, as well as create events over subsequent transactions.
        """
        async for item in self.items():
            if isinstance(item, CreateEvent):
                yield item

    async def events(self) -> "AsyncIterator[Union[CreateEvent, ArchiveEvent]]":
        """
        Return a stream of :class:`CreateEvent`s. This will include the contracts of the
        Active Contract Set, as well as create and archive events over subsequent transactions.
        """
        async for item in self.items():
            if isinstance(item, CreateEvent) or isinstance(item, ArchiveEvent):
                yield item

    def items(self) -> "AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]":
        """
        Must be overridden by subclasses to provide a stream of events. The implementation is
        expected to call :meth:`_emit_create` and :meth:`_emit_archive` for every encountered event.
        """
        raise NotImplementedError

    def __aiter__(self) -> "AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]":
        """
        Returns :meth:`items`, which includes all create and archive events, and boundaries.
        """
        return self.items()

    async def _emit(self, name: str, obj: "Any"):
        for cb in self._callbacks[name]:
            result = cb(obj)
            if result is not None and iscoroutine(result):
                result = await result
            if result is not None:
                warnings.warn(
                    "callbacks should not return anything; the result will be ignored",
                    CallbackReturnWarning,
                )

    async def _emit_create(self, event: "CreateEvent"):
        await self._emit(CREATE_EVENT, event)

    async def _emit_archive(self, event: "ArchiveEvent"):
        await self._emit(ARCHIVE_EVENT, event)

    async def _emit_boundary(self, event: "Boundary"):
        await self._emit(BOUNDARY, event)
