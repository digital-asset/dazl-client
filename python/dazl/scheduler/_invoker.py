# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
The core scheduling of logic, managing the tricky interaction between the man asyncio event loop and
background threads.
"""
from asyncio import CancelledError, Future, InvalidStateError, gather, get_event_loop, wait_for
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
import signal
from typing import List
import warnings

from ..prim import TimeDeltaLike, to_timedelta
from ..util.asyncio_util import execute_in_loop, safe_create_future
from ._base import RunLevel

__all__ = ["Invoker", "DEFAULT_TIMEOUT"]

DEFAULT_TIMEOUT = timedelta(seconds=30)


class Invoker:
    """
    A generally thread-safe invoker that aids in coordination between event-loop driven events and
    background thread events.

    This serves a similar purpose to Akka's ExecutionContext in Scala.
    """

    def __init__(self) -> None:
        self.level = RunLevel.RUN_FOREVER
        self.loop = None
        self.executor = None
        self._futures = []  # type: List[Future]

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.shutdown(exception=exc_val)

    def _unhook_future(self, fut: Future):
        try:
            self._futures.remove(fut)
        except ValueError:
            pass

    def create_future(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            f = safe_create_future()
        f.add_done_callback(self._unhook_future)
        self._futures.append(f)
        return f

    async def shutdown(self, timeout=DEFAULT_TIMEOUT, exception=None) -> None:
        """
        Stop the event loop and executor. Outstanding futures will be terminated after the
        specified timeout, or if an error is provided, that error will be used to terminate all
        futures IMMEDIATELY.

        :param timeout:
            The maximum amount of time before outstanding Futures are terminated ungracefully.
        :param exception:
            If provided, is used to trigger all outstanding futures as failures.
        """
        t = to_timedelta(timeout)
        if exception is not None:
            for fut in self._futures:
                if not fut.done():
                    fut.set_exception(exception)
        else:
            if self._futures:
                if t.total_seconds() > 0:
                    try:
                        await wait_for(gather(*self._futures), timeout=t.total_seconds())
                    except CancelledError:
                        for fut in self._futures:
                            if not fut.done():
                                fut.cancel()
                else:
                    for fut in self._futures:
                        if not fut.done():
                            fut.cancel()

    def set_context_as_current(self) -> None:
        """
        Adopt the current event loop as the loop for this :class:`Invoker`, and additionally define
        a default executor if one has not yet been set.
        """
        self.loop = get_event_loop()
        if self.executor is None:
            self.executor = ThreadPoolExecutor()

    def run_in_loop(self, func, timeout: TimeDeltaLike = 30.0):
        """
        Schedule a normal function or coroutine function to be run on the event loop, and block
        until the function has returned.
        """
        # TODO: the awful awful witchcraft required to remove these checks
        if self.loop is None:
            raise InvalidStateError("loop must be set before calling these methods")
        return execute_in_loop(self.loop, func, timeout=timeout)

    def run_in_executor(self, func):
        """
        Schedule a normal function to be run on a background thread, and yield until the function
        has returned.
        """
        # TODO: the awful awful witchcraft required to remove these checks
        if self.loop is None or self.executor is None:
            raise InvalidStateError("loop must be set before calling these methods")

        return self.loop.run_in_executor(self.executor, func)

    def install_signal_handlers(self) -> None:
        try:
            if self.loop is not None:
                self.loop.add_signal_handler(signal.SIGINT, self.handle_sigint)
                self.loop.add_signal_handler(signal.SIGQUIT, self.handle_sigquit)
            else:
                signal.signal(signal.SIGINT, lambda *_: self.handle_sigint())
                signal.signal(signal.SIGQUIT, lambda *_: self.handle_sigquit())
        except (NotImplementedError, AttributeError, ValueError):
            # SIGINT and SIGQUIT are not supported on Windows.
            pass

    def handle_sigint(self) -> None:
        self.level = RunLevel.TERMINATE_GRACEFULLY

    def handle_sigquit(self) -> None:
        self.level = RunLevel.TERMINATE_IMMEDIATELY
