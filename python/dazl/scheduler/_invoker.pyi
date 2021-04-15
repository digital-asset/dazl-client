# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# Type definitions for _scheduler.py.
#
# These type definitions live in a separate file instead of in _scheduler.py because
#  * The overloads for run_in_loop visually pollute the run_in_loop implementation.
#  * The typing module defines Awaitable[T], but the asyncio module defines a non-generic Future.
#    "Properly" typing the signatures of these functions would result in a bit of unnecessary and
#    inaccurate casting in the bodies of these methods.
#    (See https://github.com/python/typing/issues/446 for more information on this.)

from asyncio import AbstractEventLoop, Future
from concurrent.futures import Executor
from typing import Awaitable, Callable, List, Optional, TypeVar, overload

from . import RunLevel
from ..prim import TimeDeltaLike

T = TypeVar("T", covariant=True)

__all__ = ["Invoker"]

class Invoker:
    level: RunLevel
    loop: Optional[AbstractEventLoop]
    executor: Optional[Executor]
    _futures: List[Future]
    def __init__(self): ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb): ...
    def create_future(self) -> Future: ...
    def _unhook_future(self, fut: Future) -> None: ...
    async def shutdown(
        self, timeout: "TimeDeltaLike" = ..., exception: "Optional[Exception]" = None
    ) -> None: ...
    def set_context_as_current(self) -> None: ...
    @overload
    def run_in_loop(self, func: Callable[[], None], timeout: TimeDeltaLike = 30) -> None: ...
    @overload
    def run_in_loop(self, func: Callable[[], Awaitable[T]], timeout: TimeDeltaLike = 30) -> T: ...
    @overload
    def run_in_loop(self, func: Callable[[], T], timeout: TimeDeltaLike = 30) -> T: ...
    def run_in_executor(self, func: "Callable[[], T]") -> Awaitable[T]: ...
    def install_signal_handlers(self) -> None: ...
    def handle_sigint(self) -> None: ...
    def handle_sigquit(self) -> None: ...
