# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import datetime
from asyncio import AbstractEventLoop
from concurrent.futures import Executor
from threading import Event, Thread, RLock
from typing import Awaitable, Dict, Iterable, Optional, Union

from .. import LOG
from ._base import LedgerNetwork, LedgerClient, LedgerConnectionOptions, _LedgerConnectionContext
from ..client._run_level import RunState
from .v1.grpc import GRPCv1Connection
from .oauth import oauth_flow
from ..model.core import Party, UserTerminateRequest, ConnectionTimeoutError
from ..model.ledger import LedgerMetadata
from ..model.network import HTTPConnectionSettings


class AutodetectLedgerNetwork(LedgerNetwork):
    """
    Auto-detecting pool implementation that automatically routes to the correct pool
    implementation based on the scheme specified in the URL.
    """

    def __init__(self,
                 run_state: RunState,
                 options: LedgerConnectionOptions,
                 loop: Optional[AbstractEventLoop] = None,
                 executor: Optional[Executor] = None):
        self._options = options
        self._context = _LedgerConnectionContext(run_state, options, loop, executor)

        self._closed = False
        self._first_connection_evt = Event()
        self._first_connection = None  # type: Optional[AutodetectConnection]
        self._connections = dict()  # type: Dict[HTTPConnectionSettings, AutodetectConnection]
        self._lock = RLock()
        self._ledger_future = self._context.loop.create_future()
        self._admin_url = None  # type: Optional[str]
        self._main_thread = Thread(target=self._main, daemon=True)
        self._main_thread.start()

    def ledger(self) -> 'Awaitable[LedgerMetadata]':
        return self._ledger_future

    async def connect_anonymous(
            self, settings: 'HTTPConnectionSettings', context_path: 'Optional[str]') -> None:
        """
        Establish a single no-Party connection (but only if no other connections have already been
        established). This is used by specialized setups that do not require Parties to be supplied
        for any reason (such as fetching initial ledger metadata).
        """
        self._get_connection(settings, context_path)
        await self.ledger()

    async def connect(self,
                      party: 'Union[str, Party]',
                      settings: 'HTTPConnectionSettings',
                      context_path: 'Optional[str]' = None,
                      admin_url: 'Optional[str]' = None) -> LedgerClient:
        LOG.info('Establishing a connection to %s on party %s...', settings, party)
        if admin_url is not None:
            self._admin_url = admin_url
        if settings.oauth:
            new_oauth_settings = await oauth_flow(settings.oauth)
            settings = settings._replace(oauth=new_oauth_settings)
        conn = self._get_connection(settings, context_path)
        ledger = await self.ledger()
        if ledger.protocol_version == 'v1':
            from .v1.grpc import GRPCv1LedgerClient
            return GRPCv1LedgerClient(conn, ledger, party)
        elif ledger.protocol_version == 'v0':
            raise RuntimeError(f'Unsupported protocol version: {ledger.protocol_version}')
        else:
            raise RuntimeError(f'Unknown protocol version: {ledger.protocol_version}')

    async def upload_package(self, dar_contents: bytes) -> None:
        from .v1.grpc import grpc_upload_package
        return await self._context.run_in_background(
            lambda: grpc_upload_package(self._first_connection, dar_contents))

    async def set_time(self, new_time: datetime):
        ledger = await self.ledger()
        if ledger.protocol_version == 'v1':
            from .v1.grpc import grpc_set_time
            return await self._context.run_in_background(
                lambda: grpc_set_time(self._first_connection, ledger.ledger_id, new_time))
        elif ledger.protocol_version == 'v0':
            raise RuntimeError(f'Unsupported protocol version: {ledger.protocol_version}')
        else:
            raise RuntimeError(f'Unknown protocol version: {ledger.protocol_version}')

    async def close(self) -> None:
        with self._lock:
            connections = list(self._connections.values())
            self._connections.clear()

        for connection in connections:
            try:
                connection.close()
            except:
                LOG.exception('Had trouble closing a connection.')

    def _close_all(self) -> None:
        LOG.debug('Closing all connections...')
        try:
            with self._lock:
                connections = list(self._connections.values())
                self._connections.clear()

            for connection in connections:
                # noinspection PyBroadException
                try:
                    connection.close()
                except Exception:  # noqa
                    LOG.exception('Had trouble closing a connection.')
        finally:
            LOG.debug('Marked the connection pool as closed.')
            self._closed = True

    @property
    def closed(self):
        return self._closed

    def _get_connection(self, settings: HTTPConnectionSettings, context_path: Optional[str]) \
            -> 'AutodetectConnection':

        if not self._lock.acquire(timeout=5):
            raise TimeoutError('Could not acquire an internal lock quickly enough.')
        try:
            if self._closed:
                raise IOError('LedgerNetwork.close() has already been called')

            if not self._connections:
                LOG.debug('Initializing the first connection to %s...', settings)
                self._first_connection = AutodetectConnection(self._context, settings, context_path)
                self._connections[settings] = self._first_connection
                self._first_connection_evt.set()
                return self._first_connection
            else:
                LOG.debug('Initializing a connection to %s...', settings)
                stub = self._connections.get(settings)
                if stub is None:
                    stub = AutodetectConnection(self._context, settings, context_path)
                    self._connections[settings] = stub
                return stub
        except:  # noqa
            LOG.exception('An error occurred trying to create a connection.')
            raise
        finally:
            self._lock.release()

    def _main(self) -> None:
        timeout = self._options.connect_timeout
        try:
            LOG.debug('Waiting for the first connection to be established (timeout: %s)...', timeout)
            if not self._first_connection_evt.wait(timeout=timeout.total_seconds() if timeout is not None else None):
                LOG.error('Waited %s for the first connection but it never came. Aborting...', timeout)
                raise Exception('first connection timeout')

            LOG.debug('Starting ledger detection.')
            conn = self._first_connection
            if conn is not None:
                for i, metadata in enumerate(_monitor_ledger_network(conn)):
                    if i == 0:
                        self._context.run_on_loop(lambda: self._ledger_future.set_result(metadata))
                    elif metadata is not None:
                        LOG.warning('The network monitor thread emitted multiple metadata!')
        except (UserTerminateRequest, ConnectionTimeoutError) as ex:
            # re-raise these, but they are "known" errors so a stack trace in the logs would just
            # create clutter
            self._context.run_on_loop(lambda: self._ledger_future.set_exception(ex))

        except Exception as ex:
            # unexpected exception raised, so provide lots of information that might help debug
            LOG.exception('The main monitoring thread died.')

            def _maybe_apply_error():
                if not self._ledger_future.done():
                    LOG.error('The above error was propagated as an initialization error.')
                    self._ledger_future.set_exception(ex)

            # if we haven't even been able to initialize, propagate this error to the init future
            self._context.run_on_loop(_maybe_apply_error)

        finally:
            self._close_all()


class AutodetectConnection(GRPCv1Connection):
    pass


def _monitor_ledger_network(connection: AutodetectConnection) -> Iterable[LedgerMetadata]:
    """
    Monitor the very first connection established and provide general information about
    the ledger to other parties.
    """
    from .v1.grpc import grpc_detect_ledger_id

    ledger_id = grpc_detect_ledger_id(connection)
    if ledger_id is not None:
        LOG.info('Ledger ID: %s', ledger_id)
        from .v1.grpc import grpc_main_thread
        return grpc_main_thread(connection=connection, ledger_id=ledger_id)
    elif connection.settings.scheme in ('grpc', 'grpcs'):
        raise Exception('The protocol was specified as gRPC, but the backend does not support it.')
    else:
        LOG.error("Couldn't connect over gRPC.")
        raise Exception('Connection to the v0 REST API is no longer supported.')
