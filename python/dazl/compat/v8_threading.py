"""
This module contains threading/asyncio code that is intended to be dropped once
:class:`dazl.client.api.Network` and associated symbols are fully removed.
"""
from threading import RLock, Thread, current_thread
from typing import Optional
import warnings

from .. import LOG
from ..scheduler import Invoker

__all__ = ["ThreadManager"]


class ThreadManager:
    """
    Enforces the complex thread policy in the dazl v5 API.
    """

    def __init__(self):
        self._lock = RLock()
        self._invoker = Invoker()
        self._main_thread = None  # type: Optional[Thread]

    def start_in_background(
        self, daemon: bool, install_signal_handlers: "Optional[bool]"
    ) -> "None":
        """
        Create a background thread, start an event loop, and run the application.
        """
        from asyncio import new_event_loop, set_event_loop

        def background_main():
            LOG.info("Starting an event loop on a background thread %r...", current_thread().name)

            try:
                loop = new_event_loop()
                set_event_loop(loop)

                loop.run_until_complete(self.aio_run())
            except:
                LOG.exception("The main event loop died!")

            LOG.info("The main event loop has finished.")

        with self._lock:
            if self._main_thread is not None:
                raise RuntimeError("start() called more than once")
            self._main_thread = Thread(
                target=background_main, daemon=daemon, name=f"dazl:main-{id(self):016x}"
            )

        self._main_thread.start()

    def join(self, timeout: "Optional[float]" = None) -> None:
        """
        Wait for the background thread started by :meth:`start` to finish.

        This method does nothing if :meth:`start` has not yet been called.
        """
        with self._lock:
            thread = self._main_thread

        if thread is not None:
            thread.join(timeout=timeout)

    async def aio_run(self, *coroutines) -> None:
        raise NotImplementedError
