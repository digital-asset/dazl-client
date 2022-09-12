# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import asyncio
from asyncio import Future, ensure_future, gather, sleep, wait_for
from collections import defaultdict
from dataclasses import asdict, fields
from datetime import timedelta
import logging
from threading import RLock, Thread, current_thread
from typing import (
    AbstractSet,
    Any,
    Awaitable,
    Callable,
    Collection,
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
)

from .. import LOG
from ..damlast.daml_lf_1 import PackageRef
from ..damlast.lookup import MultiPackageLookup
from ..damlast.pkgfile import get_dar_package_ids
from ..ledger.aio import PackageService
from ..ledger.grpc.codec_aio import Codec
from ..metrics import MetricEvents
from ..prim import Party, TimeDeltaLike, to_timedelta
from ..protocols import LedgerNetwork
from ..protocols.autodetect import AutodetectLedgerNetwork
from ..protocols.events import BaseEvent, InitEvent, ReadyEvent
from ..scheduler import Invoker, RunLevel
from ._base_model import CREATE_IF_MISSING, NONE_IF_MISSING, IfMissingPartyBehavior
from ._conn_settings import connection_settings
from ._party_client_impl import _PartyClientImpl
from .bots import Bot, BotCollection
from .config import AnonymousNetworkConfig, NetworkConfig, URLConfig
from .errors import DazlPartyMissingError
from .ledger import LedgerMetadata

__all__ = ["_NetworkImpl", "_NetworkRunner"]
T = TypeVar("T")


class _NetworkImpl:

    __slots__ = (
        "lookup",
        "invoker",
        "codec",
        "_lock",
        "_main_thread",
        "_party_clients",
        "_global_impls",
        "_party_impls",
        "bots",
        "_config",
        "_pool",
        "_pool_init",
        "_cached_metadata",
        "_metrics",
    )

    def __init__(self, metrics: "Optional[MetricEvents]" = None):
        self.lookup = MultiPackageLookup()
        self.invoker = Invoker()
        self.codec = Codec(self, self.lookup)

        self._lock = RLock()
        self._main_thread = None  # type: Optional[Thread]
        self._pool = None  # type: Optional[LedgerNetwork]
        self._pool_init = self.invoker.create_future()
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

        self._config = dict()  # type: Dict[str, Any]
        self.bots = BotCollection(None)

    def set_config(self, *configs: "Union[NetworkConfig, AnonymousNetworkConfig]", **kwargs):
        for config in configs:
            self._config.update({k: v for k, v in asdict(config).items() if v is not None})
        self._config.update({k: v for k, v in kwargs.items() if v is not None})
        LOG.debug("Configuration for this network: %r", self._config)

    def get_config_raw(self, key: str, default: Any) -> Any:
        return self._config.get(key, default)

    def resolved_config(self) -> "NetworkConfig":
        config = self.resolved_anonymous_config()
        return NetworkConfig(
            **asdict(config),
            parties=tuple(
                party_impl.resolved_config() for party_impl in self._party_impls.values()
            ),
        )

    def resolved_anonymous_config(self) -> "AnonymousNetworkConfig":
        return AnonymousNetworkConfig.parse_kwargs(**self._config)

    def freeze(self):
        """
        Freeze configuration, and assume the current run loop can be used to schedule dazl
        coroutines. Once this method is called, ``aio_run()`` must be called instead of ``start()``
        in order to run dazl.
        """
        with self._lock:
            self.invoker.set_context_as_current()
            config = self.resolved_config()
            LOG.debug("Resolved config: %s", config)

        # From this point on, we're assuming we're on an asyncio event loop so locking is no longer
        # required
        if self._pool is None:
            from ..protocols import LedgerConnectionOptions

            # If the connect timeout is non-positive, assume the user intended for there to not be
            # a timeout at all
            connect_timeout = to_timedelta(config.connect_timeout)
            if connect_timeout <= timedelta(0):
                connect_timeout = None

            package_lookup_timeout = to_timedelta(config.package_lookup_timeout)
            if package_lookup_timeout <= timedelta(0):
                package_lookup_timeout = None

            options = LedgerConnectionOptions(
                lookup=self.lookup,
                connect_timeout=connect_timeout,
                package_lookup_timeout=package_lookup_timeout,
                eager_package_fetch=config.eager_package_fetch,
            )

            self._pool = pool = AutodetectLedgerNetwork(self.invoker, options)
            self._pool_init.set_result(pool)

        return config

    async def aio_run(self, *coroutines) -> None:
        """
        Coroutine where all network activity is scheduled from.

        :param coroutines:
            Optional additional coroutines to run. ``aio_run`` is only considered complete once all
            of the additional coroutines are also finished.
        """
        from ..metrics.instrumenters import AioLoopPerfMonitor

        config = self.freeze()
        if self._pool is None:
            raise RuntimeError("freeze() did not kick off a network pool!")

        site = None
        with AioLoopPerfMonitor(self._metrics.loop_responsiveness):
            if config.server_port is not None:
                LOG.info("Opening port %s for metrics...", config.server_port)
                try:
                    from aiohttp import web

                    from ..server import get_app

                    app = get_app(self)
                    app_runner = web.AppRunner(app)
                    await app_runner.setup()
                    site = web.TCPSite(app_runner, config.server_host, config.server_port)
                    ensure_future(site.start())
                    LOG.info(
                        "Listening on %s:%s for metrics.", config.server_host, config.server_port
                    )
                except ImportError:
                    LOG.warning("Could not start metrics because aiohttp is not installed")
            else:
                LOG.info(
                    "No server_port configuration was specified, so metrics and other stats "
                    "will not be served."
                )

            try:
                runner = _NetworkRunner(self._pool, self, coroutines)
                await runner.run()
            finally:
                await self._pool.close()
                if site is not None:
                    await site.stop()
                await self.invoker.shutdown(0)
                self._pool = None

    def start(self, daemon: bool) -> None:
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

    def shutdown(self) -> None:
        """
        Indicate that the client and its connected parties should be stopped as soon as is cleanly
        possible.

        This method can safely be called from any thread, but it must be called after start().
        """
        with self._lock:
            LOG.info("Shutting down...")
            self.invoker.handle_sigint()

    def abort(self) -> None:
        """
        Indicate that the client and its connected parties should be stopped as immediately.

        This method can safely be called from any thread, but it must be called after start().
        """
        with self._lock:
            LOG.info("Aborting...")
            self.invoker.handle_sigquit()

    def join(self, timeout=None):
        """

        :param timeout:
        :return:
        """
        with self._lock:
            thread = self._main_thread

        if thread is not None:
            thread.join(timeout=timeout)

    def global_impl(self, ctor: "Callable[[_NetworkImpl], T]") -> T:
        with self._lock:
            inst = self._global_impls.get(ctor)  # type: ignore
            if inst is None:
                inst = ctor(self)
                self._global_impls[ctor] = inst  # type: ignore
            return inst

    def party_impl_wrapper(self, party: Party, ctor: "Callable[[_PartyClientImpl], T]") -> "T":
        return self.party_impl(party, ctor=ctor)

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

    def parties(self) -> "Collection[Party]":
        """
        Return a snapshot of the set of parties that exist right now.
        """
        with self._lock:
            return list(self._party_impls)

    def party_impls(self) -> "Collection[_PartyClientImpl]":
        with self._lock:
            return list(self._party_impls.values())

    def find_bot(self, bot_id) -> "Optional[Bot]":
        """
        Return the bot of the specified ID, or ``None`` if no matching bot is found.
        """
        for party_impl in self.party_impls():
            for bot in party_impl.bots:
                if bot.id == bot_id:
                    return bot
        return None

    def simple_metadata(self, timeout: "TimeDeltaLike") -> "LedgerMetadata":
        """
        Retrieve metadata about the ledger.

        If you are using the ``asyncio``-flavored version of the API, you _must_ use
        :meth:`aio_metadata` instead.
        """
        if self._cached_metadata is not None:
            return self._cached_metadata

        if self._pool is None:
            raise ValueError(
                "simple_metadata must be called only after the global connection has started"
            )

        with self._lock:
            return self.invoker.run_in_loop(self._pool.ledger, timeout=timeout)

    async def aio_metadata(self) -> "LedgerMetadata":
        """
        Coroutine version of :meth:`metadata`.
        """
        pool = await self._pool_init
        return await pool.ledger()

    async def get_package(
        self, package_id: "PackageRef", *, timeout: Optional[TimeDeltaLike] = None
    ) -> bytes:
        pkg_service = await self._package_service()
        return await pkg_service.get_package(package_id, timeout=timeout)

    async def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = None
    ) -> "AbstractSet[PackageRef]":
        pkg_service = await self._package_service()
        return await pkg_service.list_package_ids(timeout=timeout)

    async def upload_package(self, contents: bytes, timeout: "TimeDeltaLike") -> None:
        """
        Ensure packages specified by the given byte array are loaded on the remote server. This
        method only returns once packages are reported by the Package Service.

        :param contents: Contents to attempt to upload.
        :param timeout: Length of time before giving up.
        """
        pool = await self._pool_init
        await self.connect_anonymous()
        package_ids = await self.invoker.run_in_executor(lambda: get_dar_package_ids(contents))
        await pool.upload_package(contents)
        await self.ensure_package_ids(package_ids, timeout)

    async def ensure_package_ids(
        self, package_ids: "Collection[PackageRef]", timeout: "TimeDeltaLike"
    ):
        await wait_for(
            self.__ensure_package_ids(package_ids), to_timedelta(timeout).total_seconds()
        )

    async def __ensure_package_ids(self, package_ids: "Collection[PackageRef]"):
        metadata = await self.aio_metadata()
        await gather(*(metadata.package_loader.load(pkg_ref) for pkg_ref in package_ids))

    async def _package_service(self) -> PackageService:
        """
        Return an instance of :class:`PackageService`. Blocks until a connection has been
        established.
        """
        metadata = await self.aio_metadata()
        # noinspection PyProtectedMember
        conn = metadata.package_loader._conn

        # Sit here for a maximum of ten minutes. The only reason we would be stuck here is if the
        # first connection took a very long time to be established, or the user simply never called
        # run() / start() on the Network. In the former case, we give the upstream as much as 10
        # minutes before giving up.
        wait_seconds = 600
        while True:
            if conn is None:
                # This isn't the most efficient way to wait for a connection, but in the vast
                # majority of cases the connection will be immediately available, which means we
                # don't wait at all
                await sleep(1.0)
                wait_seconds -= 1
                if wait_seconds <= 0:
                    raise asyncio.TimeoutError(
                        "waited too long for a network to be alive while searching for packages"
                    )
            else:
                break

        return conn

    # region Event Handler Management

    # noinspection PyShadowingBuiltins

    def add_event_handler(self, key, handler: "Callable[[BaseEvent], None]") -> "Bot":
        """
        Add an event handler to a specific event. Unlike event listeners on party clients, these
        event handlers are not allowed to return anything in response to handling an event.
        """
        return self.bots.add_single(key, handler, None)

    def emit_event(self, data: BaseEvent) -> "Awaitable[Any]":
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
            cert_key_file=config.cert_key_file,
            enable_http_proxy=config.enable_http_proxy,
        )
        await self._pool.connect_anonymous(settings, url_prefix)


class _NetworkRunner:
    def __init__(self, pool: LedgerNetwork, network_impl: "_NetworkImpl", user_coroutines):
        self.pool = pool
        self.initialized_parties = set()  # type: Set[Party]
        self._network_impl = network_impl
        self._config = self._network_impl.resolved_config()
        self._read_completions = []  # type: List[Future]
        self._user_coroutines = [ensure_future(coro) for coro in user_coroutines]
        self._bot_coroutines = []  # type: List[Future]
        self._writers = []  # type: List[Future]

    async def run(self):
        LOG.debug("Running a Network with config: %r", self._config)
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
                await self._init(
                    [party_impls[party] for party in uninitialized_parties], prev_offset
                )
            self.initialized_parties |= uninitialized_parties

            current_offset, keep_running = await self.beat(list(party_impls.values()))
            if keep_running:
                if prev_offset == current_offset:
                    await sleep(0.5)
                else:
                    prev_offset = current_offset

        # prohibit any more command submissions
        LOG.debug("network_run: stopping bots gracefully...")
        for pi in self._network_impl.party_impls():
            pi.bots.stop_all()
        self._network_impl.bots.stop_all()

        LOG.debug("network_run: stopping its writers gracefully...")
        # TODO: This needs to be coordinated better among the list of writers we ACTUALLY started
        for pi in self._network_impl.party_impls():
            pi.stop_writer()

        # wait for writers to finish their writing
        await gather(*self._writers, return_exceptions=True)
        LOG.info("network_run: finished.")
        self._writers = []

    async def beat(self, party_impls: "Collection[_PartyClientImpl]") -> Tuple[Optional[str], bool]:
        """
        Called periodically to schedule reads and writes.
        """
        from ._reader_sync import run_iteration

        offset, completions = await run_iteration(party_impls)

        self._read_completions = [
            fut for fut in (*self._read_completions, *completions) if not fut.done()
        ]
        self._user_coroutines = [fut for fut in self._user_coroutines if not fut.done()]

        # If there are no more commands in flight, there is no more activity
        if self._network_impl.invoker.level >= RunLevel.TERMINATE_GRACEFULLY:
            LOG.info("network_run terminating on user request...")
            return offset, False
        elif self._network_impl.invoker.level >= RunLevel.RUN_UNTIL_IDLE:
            if not self._read_completions and not self._user_coroutines:
                if all(pi.writer_idle() for pi in party_impls):
                    LOG.info(
                        "network_run: terminating because all writers are idle and all "
                        "clients have caught up to offset %s",
                        offset,
                    )
                    return offset, False

        return offset, True

    async def _init(
        self, party_impls: "Collection[_PartyClientImpl]", first_offset: "Optional[str]"
    ) -> Optional[str]:
        # region log
        if LOG.isEnabledFor(logging.DEBUG):
            parties = [pi.party for pi in party_impls]
            if first_offset is None:
                LOG.debug("Starting first-time initialization for parties: %s", parties)
            else:
                LOG.debug(
                    "Starting initialization for parties: %s, advancing to offset: %s",
                    parties,
                    first_offset,
                )
        # endregion

        # establish ledger connections
        if party_impls:
            # noinspection PyProtectedMember
            self._bot_coroutines.extend(
                ensure_future(party_impl.bots._main()) for party_impl in party_impls
            )
            await gather(*(party_impl.connect_in(self.pool) for party_impl in party_impls))
        elif first_offset is None:
            # establish a single null connection that will be used only to ensure that metadata can be
            # fetched
            party_impl = _PartyClientImpl(self._network_impl, Party("\x00"))
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
        if first_offset is None:
            init_evt = InitEvent(
                None,
                None,
                None,
                metadata.ledger_id,
                self._network_impl.lookup,
                metadata._store,
            )
            init_futs.append(ensure_future(self._network_impl.emit_event(init_evt)))
        for party_impl in party_impls:
            init_futs.append(ensure_future(party_impl.initialize(None, metadata)))

        # TODO: Consider what should join on init_futs; we can't join here because otherwise this
        #  blocks the readers from reading transactions that would cause these events to fully
        #  resolve

        from ._reader_sync import read_initial_acs

        offset = await read_initial_acs(party_impls)

        LOG.debug('Preparing to raise the "ready" event...')
        # Raise the 'ready' event.
        ready_futs = []
        if first_offset is None:
            ready_evt = ReadyEvent(
                None,
                None,
                None,
                metadata.ledger_id,
                self._network_impl.lookup,
                metadata._store,
                offset,
            )
            ready_futs.append(ensure_future(self._network_impl.emit_event(ready_evt)))
        for party_impl in party_impls:
            ready_futs.append(ensure_future(party_impl.emit_ready(metadata, None, offset)))
        for party_impl in party_impls:
            party_impl.ready().set_result(None)

        # TODO: Consider what should join on ready_futs; we can't join here because otherwise this
        #  blocks the readers from reading transactions that would cause these events to fully
        #  resolve

        # Return the metadata offset for later
        LOG.debug("Raised the ready event, and caught up to %s.", offset)
        return offset
