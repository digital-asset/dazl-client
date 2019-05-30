# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the abstract base class that defines the protocol for interacting with a
process that implements the Ledger API.
"""
from asyncio import AbstractEventLoop, get_event_loop, Future, ensure_future
from concurrent.futures import Executor, ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any, Optional, Sequence
import threading

from .. import LOG
from ..model.ledger import LedgerMetadata
from ..model.network import HTTPConnectionSettings
from ..model.reading import BaseEvent, TransactionFilter
from ..model.writing import CommandPayload
from ..util.typing import safe_optional_cast, safe_cast


@dataclass(frozen=True)
class LedgerConnectionOptions:
    connect_timeout: timedelta


class LedgerNetwork:
    """
    Abstract base class for creating connections to the ledger.
    """

    async def connect(
            self,
            party: str,
            settings: HTTPConnectionSettings,
            context_path: 'Optional[str]',
            admin_url: 'Optional[str]') -> 'LedgerClient':
        raise NotImplementedError('connect must be implemented')

    async def ledger(self) -> LedgerMetadata:
        """
        Return information about the entire ledger.
        """
        raise NotImplementedError('ledger must be implemented')

    async def set_time(self, new_datetime: datetime) -> None:
        """
        Advance the time on the Sandbox (static time model only).

        To access the current time, use the time_model returned from :meth:`ledger`.

        :param new_datetime: The new time to set.
        """
        raise NotImplementedError('set_time must be implemented')

    async def sync_time(self) -> None:
        """
        Ensure that the local notion of time is in sync with the remote server. This method is only
        relevant for static-time implementations on the REST-based API, as the gRPC API pushes time
        updates through the TimeService. In these contexts, this method is a no-op.
        """

    async def close(self):
        """
        Shut down all connections and transition the pool to the closed state.
        """

    @property
    def closed(self) -> bool:
        """
        Determine whether the underlying network connections to the LedgerNetwork are closed. This
        property should start as ``False`` when the pool is constructed, and ``True`` some time
        after ``close()`` is called.
        """
        raise NotImplementedError('closed must be implemented')


class LedgerClient:
    """
    Abstract base class that defines the required methods to define a protocol over the Ledger API.
    """

    async def commands(self, command_payload: CommandPayload) -> None:
        """
        Submit a command to the ledger.

        The coroutine returns when the implementation has accepted the command for processing, but
        not necessarily committed to the ledger.

        :param command_payload: Payload of data to submit asynchronously.
        """
        raise NotImplementedError('commands must be implemented')

    async def events(self, transaction_filter: TransactionFilter) -> Sequence[BaseEvent]:
        """
        Return events from a certain offset in the ledger. The number of blocks
        returned is implementation-defined.
        """
        raise NotImplementedError('events must be implemented')


class _LedgerConnectionContext:
    def __init__(self,
                 options: LedgerConnectionOptions,
                 loop: Optional[AbstractEventLoop] = None,
                 executor: Optional[Executor] = None):
        self.options = options
        self.loop = loop if loop is not None else get_event_loop()
        self.executor = executor if executor is not None else ThreadPoolExecutor(max_workers=25)

    def run_in_background(self, func, *args) -> Future:
        return ensure_future(self.loop.run_in_executor(self.executor, func, *args))

    def run_on_loop(self, func, *args) -> Any:
        """
        Called from a background thread to invoke a function on the event loop. This method blocks
        until the function has returned.
        """
        evt = threading.Event()
        result, ex = None, None

        def _invoke():
            nonlocal result
            try:
                result = func(*args)
            finally:
                evt.set()

        self.loop.call_soon_threadsafe(_invoke)
        evt.wait()
        return result


class _LedgerConnection:
    def __init__(self,
                 context: _LedgerConnectionContext,
                 settings: HTTPConnectionSettings,
                 context_path: Optional[str]):
        LOG.debug('Creating a gRPC channel for %s...', settings)
        import threading

        self.context = safe_cast(_LedgerConnectionContext, context)
        self.settings = safe_cast(HTTPConnectionSettings, settings)
        self.context_path = safe_optional_cast(str, context_path)
        self.close_evt = threading.Event()

    def close(self):
        self.close_evt.set()
