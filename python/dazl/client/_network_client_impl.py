# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from asyncio import gather, ensure_future, sleep
from collections import defaultdict
from dataclasses import fields
from datetime import timedelta, datetime
from threading import RLock, Thread, current_thread
from typing import Any, Callable, Dict, Optional, TypeVar, Collection, Awaitable, Set, Tuple, \
    Union, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from dataclasses import asdict

from .. import LOG
from ._base_model import IfMissingPartyBehavior, CREATE_IF_MISSING, NONE_IF_MISSING, \
    EXCEPTION_IF_MISSING
from ._party_client_impl import _PartyClientImpl
from ._run_level import RunState
from .bots import Bot, BotCollection
from .config import AnonymousNetworkConfig, NetworkConfig, URLConfig, \
    DEFAULT_CONNECT_TIMEOUT_SECONDS
from ..metrics import MetricEvents
from ..model.core import Party, RunLevel, DazlPartyMissingError
from ..model.ledger import LedgerMetadata
from ..model.network import connection_settings
from ..model.reading import InitEvent, ReadyEvent, BaseEvent
from ..protocols import LedgerNetwork
from ..protocols.autodetect import AutodetectLedgerNetwork
from ..util.asyncio_util import execute_in_loop, Invoker, safe_create_future
from ..util.dar import get_dar_package_ids
from ..util.prim_types import to_timedelta, TimeDeltaConvertible

T = TypeVar('T')


class _NetworkImpl:

    __slots__ = ('_lock', '_main_thread', 'invoker', '_party_clients', '_global_impls',
                 '_party_impls', '_run_state', 'bots', '_config', '_pool', '_pool_init',
                 '_cached_metadata', '_metrics')

    def __init__(self, metrics: 'Optional[MetricEvents]' = None):
        self.invoker = Invoker()
        self._lock = RLock()
        self._main_thread = None  # type: Optional[Thread]
        self._run_state = None  # type: Optional[RunState]
        self._pool = None  # type: Optional[LedgerNetwork]
        self._pool_init = safe_create_future()
        if metrics is None:
            # create a default set of metrics
            try:
                # noinspection PyUnresolvedReferences
                from ..metrics.prometheus import PrometheusMetricEvents
                self._metrics = PrometheusMetricEvents.default()
            except ImportError:
                self._metrics = MetricEvents()

        # Separately, keep a reference to metadata because it's accessed quite frequently and it is
        # useful for this to be available even when the pool is closed
        self._cached_metadata = None  # type: Optional[LedgerMetadata]

        self._party_clients = defaultdict(dict)  # type: Dict[type, Dict[Party, Any]]
        self._global_impls = dict()  # type: Dict[type, Any]
        self._party_impls = dict()  # type: Dict[Party, _PartyClientImpl]

        self._config = dict()
        self.bots = BotCollection(None)

    @overload
    def run_in_loop_threadsafe(self,
                               cb: Callable[[], Union[None, Awaitable[None]]],
                               timeout: float = 30) -> None: ...

    @overload
    def run_in_loop_threadsafe(self,
                               cb: Callable[[], Union[Awaitable[T], T]],
                               timeout: float = 30) -> T: ...

    def run_in_loop_threadsafe(self, cb, timeout=30):
        """
        Schedule a callback to be run on the event loop. This can either be a normal function or a
        coroutine.

        :param cb: The callback to invoke.
        :param timeout: The timeout, in seconds, to abort.
        :return: The returned value from the function or coroutine.
        """
        return self.invoker.run_in_loop(cb, timeout=timeout)

    def set_config(self, *configs: 'Union[NetworkConfig, AnonymousNetworkConfig]', **kwargs):
        for config in configs:
            self._config.update({k: v for k, v in asdict(config).items() if v is not None})
        self._config.update({k: v for k, v in kwargs.items() if v is not None})
        LOG.debug('Configuration for this network: %r', self._config)

    def get_config_raw(self, key: str, default: Any) -> Any:
        return self._config.get(key, default)

    def resolved_config(self) -> 'NetworkConfig':
        config = self.resolved_anonymous_config()
        return NetworkConfig(
            **asdict(config),
            parties=tuple(party_impl.resolved_config()
                          for party_impl in self._party_impls.values()))

    def resolved_anonymous_config(self) -> 'AnonymousNetworkConfig':
        return AnonymousNetworkConfig.parse_kwargs(**self._config)

    async def aio_run(self, *coroutines, run_state: Optional[RunState] = None) -> None:
        """
        Coroutine where all network activity is scheduled from.

        :param coroutines:
            Optional additional coroutines to run. ``aio_run`` is only considered complete once all
            of the additional coroutines are also finished.
        :param run_state:
            :class:`RunState` that specifies when the loop is to be terminated. If ``None`` is
            supplied, a default :class:`RunState` that runs until explicitly stopped is assigned.
        """
        from ..metrics.instrumenters import AioLoopPerfMonitor
        from ..protocols import LedgerConnectionOptions

        if run_state is None:
            run_state = RunState(RunLevel.RUN_FOREVER)

        with self._lock:
            self._run_state = run_state
            self.invoker.set_context_as_current()
            config = self.resolved_config()

        site = None
        with AioLoopPerfMonitor(self._metrics.loop_responsiveness):
            if config.server_port is not None:
                LOG.info('Opening port %s for metrics...', config.server_port)
                from aiohttp import web
                from ..server import get_app
                app = get_app(self)
                runner = web.AppRunner(app)
                await runner.setup()
                site = web.TCPSite(runner, config.server_host, config.server_port)
                ensure_future(site.start())
                LOG.info('Listening on %s:%s for metrics.', config.server_host, config.server_port)
            else:
                LOG.info('No server_port configuration was specified, so metrics and other stats '
                         'will not be served.')

            # If the connect timeout is non-positive, assume the user intended for there to not be
            # a timeout at all
            connect_timeout = to_timedelta(config.connect_timeout)
            if connect_timeout <= timedelta(0):
                connect_timeout = None

            options = LedgerConnectionOptions(connect_timeout=connect_timeout)

            self._pool = pool = AutodetectLedgerNetwork(
                options=options, loop=self.invoker.get_loop(), executor=self.invoker.get_executor(),
                run_state=self._run_state)
            self._pool_init.set_result(pool)

            try:
                runner = _NetworkRunner(pool, run_state, self, coroutines)
                await runner.run()
            finally:
                await self._pool.close()
                if site is not None:
                    await site.stop()
                self._pool = None

    def start(self, run_state: RunState, daemon: bool) -> None:
        """
        Create a background thread, start an event loop, and run the application.
        """
        from asyncio import new_event_loop, set_event_loop

        def background_main():
            LOG.info('Starting an event loop on a background thread %r...', current_thread().name)

            try:
                loop = new_event_loop()
                set_event_loop(loop)

                loop.run_until_complete(self.aio_run(run_state=run_state))
            except:
                LOG.exception('The main event loop died!')

            LOG.info('The main event loop has finished.')

        with self._lock:
            if self._main_thread is not None:
                raise RuntimeError('start() called more than once')
            self._main_thread = Thread(
                target=background_main, daemon=daemon, name=f'dazl:main-{id(self):016x}')

        self._main_thread.start()

    def shutdown(self) -> None:
        """
        Indicate that the client and its connected parties should be stopped as soon as is cleanly
        possible.

        This method can safely be called from any thread, but it must be called after start().
        """
        with self._lock:
            LOG.info('Shutting down...')
            loop = self.invoker.get_loop()
            run_state = self._run_state
            if loop is None:
                raise RuntimeError('shutdown() called on a non-stopped Network')
        loop.call_soon_threadsafe(run_state.handle_sigint)

    def abort(self) -> None:
        """
        Indicate that the client and its connected parties should be stopped as immediately.

        This method can safely be called from any thread, but it must be called after start().
        """
        with self._lock:
            LOG.info('Aborting...')
            loop = self.invoker.get_loop()
            run_state = self._run_state
            if loop is None:
                raise RuntimeError('abort() called on a non-stopped Network')
        loop.call_soon_threadsafe(run_state.handle_sigquit)

    def join(self, timeout=None):
        """

        :param timeout:
        :return:
        """
        with self._lock:
            thread = self._main_thread

        if thread is not None:
            thread.join(timeout=timeout)

    def global_impl(self, ctor: 'Callable[[_NetworkImpl], T]') -> T:
        with self._lock:
            inst = self._global_impls.get(ctor)
            if inst is None:
                inst = ctor(self)
                self._global_impls[ctor] = inst
            return inst

    @overload
    def party_impl(
            self, party: Party, ctor: None = None,
            if_missing: Literal[CREATE_IF_MISSING, EXCEPTION_IF_MISSING] = CREATE_IF_MISSING) -> \
        _PartyClientImpl: ...

    @overload
    def party_impl(
            self, party: Party, ctor: None = None,
            if_missing: NONE_IF_MISSING = CREATE_IF_MISSING) -> \
        Optional[_PartyClientImpl]: ...

    @overload
    def party_impl(
            self, party: Party, ctor: 'Callable[[_PartyClientImpl], T]',
            if_missing: Literal[CREATE_IF_MISSING, EXCEPTION_IF_MISSING] = CREATE_IF_MISSING) -> \
        T: ...

    @overload
    def party_impl(
            self, party: Party, ctor: 'Callable[[_PartyClientImpl], T]',
            if_missing: NONE_IF_MISSING = CREATE_IF_MISSING) -> \
        Optional[T]: ...

    def party_impl(self, party, ctor=None, if_missing: IfMissingPartyBehavior = CREATE_IF_MISSING):
        """
        Return a :class:`_PartyClientImpl` object for the specified party, possibly wrapping it in a
        more high-level friendly API.

        :param party:
            The party to get (or create) a connection for.
        :param ctor:
            The constructor function to use to create a wrapper, or ``None`` to return a raw
            :class:`_PartyClientImpl`.
        :param if_missing:
            The behavior of this method in the case that an entry for the Party does not yet exist:
            ``CREATE_IF_MISSING``: if the party does not yet exist, create an implementation for it.
            ``NONE_IF_MISSING``: if the party does not yet exist, return ``None``.
            ``EXCEPTION_IF_MISSING``: if the party does not yet exist, throw an exception.
        :return:
            Either a :class:`_PartyClientImpl`, the specified wrapper type, or ``None``.
        """
        with self._lock:
            impl = self._party_impls.get(party)
            if impl is None:
                if if_missing == CREATE_IF_MISSING:
                    impl = _PartyClientImpl(self, party)
                    self._party_impls[party] = impl
                elif if_missing == NONE_IF_MISSING:
                    return None
                else:
                    raise DazlPartyMissingError(party)

            if ctor is None:
                return impl

            mm = self._party_clients[ctor]
            inst = mm.get(party)
            if inst is None:
                inst = ctor(impl)
                mm[party] = inst
            return inst

    def parties(self) -> 'Collection[Party]':
        """
        Return a snapshot of the set of parties that exist right now.
        """
        with self._lock:
            return list(self._party_impls)

    def party_impls(self) -> 'Collection[_PartyClientImpl]':
        with self._lock:
            return list(self._party_impls.values())

    def find_bot(self, bot_id) -> 'Optional[Bot]':
        """
        Return the bot of the specified ID, or ``None`` if no matching bot is found.
        """
        for party_impl in self.party_impls():
            for bot in party_impl.bots:
                if bot.id == bot_id:
                    return bot
        return None

    def simple_metadata(self, timeout: 'TimeDeltaConvertible') -> LedgerMetadata:
        """
        Retrieve metadata about the ledger.

        If you are using the ``asyncio``-flavored version of the API, you _must_ use
        :meth:`aio_metadata` instead.
        """
        if self._cached_metadata is not None:
            return self._cached_metadata

        with self._lock:
            return execute_in_loop(self.invoker.get_loop(), self._pool.ledger, timeout=timeout)

    async def aio_metadata(self) -> LedgerMetadata:
        """
        Coroutine version of :meth:`metadata`.
        """
        pool = await self._pool_init
        return await pool.ledger()

    async def upload_package(self, contents: bytes, timeout: 'TimeDeltaConvertible') -> None:
        """
        Ensure packages specified by the given byte array are loaded on the remote server. This
        method only returns once packages are reported by the package services.

        If an admin URL is specified, dazl will attempt to upload packages to that URL, and wait
        for the package to be reported by the package service.

        :param contents: Contents to attempt to upload.
        :param timeout: Length of time before giving up.
        """
        pool = await self._pool_init
        package_ids = get_dar_package_ids(contents)
        await pool.upload_package(contents)
        await self.ensure_package_ids(package_ids, timeout)

    async def ensure_package_ids(
            self, package_ids: 'Collection[str]', timeout: 'TimeDeltaConvertible'):
        from asyncio import wait_for, TimeoutError
        timeout = to_timedelta(timeout)
        expire_time = datetime.max #datetime.utcnow() + timeout
        metadata = await wait_for(self.aio_metadata(), timeout.total_seconds())
        package_id_set = set(package_ids)
        while datetime.utcnow() < expire_time:
            if package_id_set.issubset(set(metadata.store.package_ids())):
                return
        raise TimeoutError()

    async def get_time(self) -> datetime:
        metadata = await self._pool.ledger()
        await self._pool.sync_time()
        return metadata.time_model.get_time()

    def set_time(self, new_datetime: datetime) -> Awaitable[None]:
        return self._pool.set_time(new_datetime)

    # region Event Handler Management

    # noinspection PyShadowingBuiltins

    def add_event_handler(self, key, handler: 'Callable[[BaseEvent], None]') -> 'Bot':
        """
        Add an event handler to a specific event. Unlike event listeners on party clients, these
        event handlers are not allowed to return anything in response to handling an event.
        """
        return self.bots.add_single(key, handler, None)

    def emit_event(self, data: BaseEvent) -> 'Awaitable[Any]':
        return self.bots.notify(data)

    # endregion

    async def connect_anonymous(self):
        config_names = {f.name for f in fields(URLConfig)}
        config = URLConfig(**{k: v for k, v in self._config.items() if k in config_names})
        settings, url_prefix = connection_settings(
            config.url,
            None,
            verify_ssl=config.verify_ssl,
            ca_file=config.ca_file,
            cert_file=config.cert_file,
            cert_key_file=config.cert_key_file)
        await self._pool.connect_anonymous(settings, url_prefix)


class _NetworkRunner:
    def __init__(self, pool: LedgerNetwork, run_state: RunState, network_impl: '_NetworkImpl', user_coroutines):
        self.pool = pool
        self.run_state = run_state
        self.initialized_parties = set()  # type: Set[Party]
        self._network_impl = network_impl
        self._config = self._network_impl.resolved_config()
        self._read_completions = []
        self._user_coroutines = [ensure_future(coro) for coro in user_coroutines]
        self._bot_coroutines = []
        self._writers = []

    async def run(self):
        LOG.debug('Running a Network with config: %r', self._config)
        prev_offset = None
        keep_running = True

        self._bot_coroutines.append(ensure_future(self._network_impl.bots._main()))

        while keep_running:
            party_impls = {pi.party: pi for pi in self._network_impl.party_impls()}
            if not party_impls:
                await self._network_impl.connect_anonymous()

            # make sure that all parties are initialized; we do this on EVERY tick because new
            # parties might come later and they'll need to be initialized too
            uninitialized_parties = set(party_impls) - self.initialized_parties
            # TODO: Also handle removed parties at some point
            if uninitialized_parties:
                await self._init([party_impls[party] for party in uninitialized_parties], prev_offset)
            self.initialized_parties |= uninitialized_parties

            current_offset, keep_running = await self.beat(list(party_impls.values()))
            if keep_running:
                if prev_offset == current_offset:
                    await sleep(0.5)
                else:
                    prev_offset = current_offset

        # prohibit any more command submissions
        LOG.debug('network_run: stopping bots gracefully...')
        for pi in self._network_impl.party_impls():
            pi.bots.stop_all()
        self._network_impl.bots.stop_all()

        LOG.debug('network_run: stopping its writers gracefully...')
        # TODO: This needs to be coordinated better among the list of writers we ACTUALLY started
        for pi in self._network_impl.party_impls():
            pi.stop_writer()

        # wait for writers to finish their writing
        await gather(*self._writers, return_exceptions=True)
        LOG.info('network_run: finished.')
        self._writers = []

    async def beat(self, party_impls: 'Collection[_PartyClientImpl]') -> Tuple[str, bool]:
        """
        Called periodically to schedule reads and writes.
        """
        from ._reader_sync import run_iteration
        offset, completions = await run_iteration(party_impls)

        self._read_completions = [fut for fut in (*self._read_completions, *completions)
                                  if not fut.done()]
        self._user_coroutines = [fut for fut in self._user_coroutines if not fut.done()]

        # If there are no more commands in flight, there is no more activity
        if self.run_state.level >= RunLevel.TERMINATE_GRACEFULLY:
            LOG.info('network_run terminating on user request...')
            return offset, False
        elif self.run_state.level >= RunLevel.RUN_UNTIL_IDLE:
            if not self._read_completions and not self._user_coroutines:
                if all(pi.writer_idle() for pi in party_impls):
                    LOG.info('network_run: terminating because all writers are idle and all '
                             'clients have caught up to offset %s', offset)
                    return offset, False

        return offset, True

    async def _init(
            self, party_impls: 'Collection[_PartyClientImpl]',
            first_offset: 'Optional[str]') -> Optional[str]:
        # region log
        if LOG.isEnabledFor(logging.DEBUG):
            parties = [pi.party for pi in party_impls]
            if first_offset is None:
                LOG.debug('Starting first-time initialization for parties: %s', parties)
            else:
                LOG.debug('Starting initialization for parties: %s, advancing to offset: %s', parties, first_offset)
        # endregion

        # establish ledger connections
        if party_impls:
            # noinspection PyProtectedMember
            self._bot_coroutines.extend(ensure_future(party_impl.bots._main())
                                        for party_impl in party_impls)
            await gather(*(party_impl.connect_in(self.pool) for party_impl in party_impls))
        elif first_offset is None:
            # establish a single null connection that will be used only to ensure that metadata can be
            # fetched
            party_impl = _PartyClientImpl(self._network_impl, Party('\x00'))
            await party_impl.connect_in(self.pool)
        else:
            # trivially, there is nothing to do for init because there are no parties to initialize
            # and this isn't our first rodeo
            return first_offset

        # get metadata about the ledger
        metadata = await self.pool.ledger()
        self._network_impl._cached_metadata = metadata

        # start writers early to potentially service commands off the back of these events
        self._writers.extend(ensure_future(party_impl.main_writer()) for party_impl in party_impls)

        # Raise the 'init' event.
        init_futs = []
        current_time = metadata.time_model.get_time()
        if first_offset is None:
            evt = InitEvent(None, None, current_time, metadata.ledger_id, metadata.store)
            init_futs.append(ensure_future(self._network_impl.emit_event(evt)))
        for party_impl in party_impls:
            init_futs.append(ensure_future(party_impl.initialize(current_time, metadata)))

        # TODO: Consider what should join on init_futs; we can't join here because otherwise this
        #  blocks the readers from reading transactions that would cause these events to fully
        #  resolve

        from ._reader_sync import read_initial_acs
        use_acs_service = self._config.use_acs_service
        offset = await read_initial_acs(party_impls, use_acs_service)

        LOG.debug('Preparing to raise the "ready" event...')
        # Raise the 'ready' event.
        ready_futs = []
        current_time = metadata.time_model.get_time()
        if first_offset is None:
            evt = ReadyEvent(None, None, current_time, metadata.ledger_id, metadata.store, offset)
            ready_futs.append(ensure_future(self._network_impl.emit_event(evt)))
        for party_impl in party_impls:
            ready_futs.append(ensure_future(party_impl.emit_ready(metadata, current_time, offset)))
        for party_impl in party_impls:
            party_impl.ready().set_result(None)

        # TODO: Consider what should join on ready_futs; we can't join here because otherwise this
        #  blocks the readers from reading transactions that would cause these events to fully
        #  resolve

        # Return the metadata offset for later
        LOG.debug('Raised the ready event, and caught up to %s.', offset)
        return offset
