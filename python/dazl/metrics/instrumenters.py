# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from asyncio import AbstractEventLoop, get_event_loop
from datetime import datetime, timedelta
from typing import Callable, Optional


class AioLoopPerfMonitor:
    def __init__(
        self, callback: "Callable[[timedelta], None]", loop: "Optional[AbstractEventLoop]" = None
    ):
        self.callback = callback
        self.loop = loop
        self.started = False

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def start(self):
        loop = self.loop
        if loop is None:
            loop = get_event_loop()

        self.started = True
        loop.call_soon(self._tick, loop)

    def stop(self):
        self.started = False

    def _tick(self, loop: "AbstractEventLoop") -> None:
        """
        Schedule a _tock.

        :param loop: The loop to use.
        """
        if self.started:
            loop.call_soon(self._tock, loop, datetime.utcnow())

    def _tock(self, loop: "AbstractEventLoop", dt: "datetime") -> None:
        """
        Measure the length of time from the last _tick and record that time; then schedule a _tock
        in one second.

        :param loop: The loop to use.
        :param dt: The time when the _tock was scheduled.
        """
        if self.started:
            now = datetime.utcnow()
            self.callback(now - dt)
            loop.call_later(1, self._tick, loop)
