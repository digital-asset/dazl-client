# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
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

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

__all__ = ["QueryStreamBase"]

from ..damlast.daml_lf_1 import TypeConName
from .api_types import ArchiveEvent, Boundary, CreateEvent

AnyHandler = Callable[[Any], None]
AAnyHandler = Callable[[Any], Awaitable[None]]

BoundaryHandler = Callable[[Boundary], None]
ABoundaryHandler = Callable[[Boundary], Awaitable[None]]

CreateEventHandler = Callable[[CreateEvent], None]
ACreateEventHandler = Callable[[CreateEvent], Awaitable[None]]

ArchiveEventHandler = Callable[[ArchiveEvent], None]
AArchiveEventHandler = Callable[[ArchiveEvent], Awaitable[None]]

Self = TypeVar("Self")

class QueryStreamBase:
    @property
    def _callbacks(self) -> DefaultDict[str, List[Union[AnyHandler, AAnyHandler]]]: ...
    @overload
    def on_boundary(self, fn: BoundaryHandler) -> BoundaryHandler: ...
    @overload
    def on_boundary(self, fn: ABoundaryHandler) -> ABoundaryHandler: ...
    @overload
    def on_create(self) -> _CreateEventDecorator: ...
    @overload
    def on_create(self, fn: CreateEventHandler) -> CreateEventHandler: ...
    @overload
    def on_create(self, fn: ACreateEventHandler) -> ACreateEventHandler: ...
    @overload
    def on_create(self, template_id: Union[str, TypeConName]) -> _CreateEventDecorator: ...
    @overload
    def on_create(
        self, template_id: Union[str, TypeConName], fn: CreateEventHandler
    ) -> CreateEventHandler: ...
    @overload
    def on_create(
        self, template_id: Union[str, TypeConName], fn: ACreateEventHandler
    ) -> ACreateEventHandler: ...
    @overload
    def on_archive(self) -> _ArchiveEventDecorator: ...
    @overload
    def on_archive(self, fn: ArchiveEventHandler) -> ArchiveEventHandler: ...
    @overload
    def on_archive(self, fn: AArchiveEventHandler) -> AArchiveEventHandler: ...
    @overload
    def on_archive(self, template_id: Union[str, TypeConName]) -> _ArchiveEventDecorator: ...
    @overload
    def on_archive(
        self, template_id: Union[str, TypeConName], fn: ArchiveEventHandler
    ) -> ArchiveEventHandler: ...
    @overload
    def on_archive(
        self, template_id: Union[str, TypeConName], fn: AArchiveEventHandler
    ) -> AArchiveEventHandler: ...
    async def __aenter__(self: Self) -> Self: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def creates(self) -> AsyncIterator[CreateEvent]: ...
    def events(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent]]: ...
    def items(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    def __aiter__(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    async def close(self) -> None: ...
    async def run(self) -> None: ...
    async def _emit(self, name: str, obj: Any) -> None: ...
    async def _emit_create(self, event: CreateEvent) -> None: ...
    async def _emit_archive(self, event: ArchiveEvent) -> None: ...
    async def _emit_boundary(self, boundary: Boundary) -> None: ...

class _CreateEventDecorator(Protocol):
    @overload
    def __call__(self, fn: CreateEventHandler) -> CreateEventHandler: ...
    @overload
    def __call__(self, fn: ACreateEventHandler) -> AArchiveEventHandler: ...

class _ArchiveEventDecorator(Protocol):
    @overload
    def __call__(self, fn: ArchiveEventHandler) -> ArchiveEventHandler: ...
    @overload
    def __call__(self, fn: AArchiveEventHandler) -> AArchiveEventHandler: ...