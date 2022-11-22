# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# NOTE TO IMPLEMENTORS
#
# This file contains only public API definitions, overloads, and documentation. (This file should
# be treated more like a C header file than anything else.) The bulk of the implementation is kept
# in _party_client.py.
#
# This file is repetitive and tedious, but written this way primarily so that static typing tools
# do the right thing. Python's ``typing`` library (and mypy) aren't quite expressive enough to allow
# for a more concise representation of the various flavors of the API. The unit test
# ``test_api_consistency.py`` verifies that these implementations are generally in sync with each
# other the way that the documentation says they are.
"""
This module contains the public API for interacting with the ledger from the perspective of a
specific party.
"""

from asyncio import Future, ensure_future, get_event_loop
from contextlib import contextmanager
from functools import partial, wraps
from logging import INFO
import os
from pathlib import Path
from typing import Any, Awaitable, BinaryIO, Collection, List, Optional, Tuple, Union
from uuid import uuid4
import warnings

from .. import LOG
from ..damlast import get_dar_package_ids
from ..damlast.daml_lf_1 import PackageRef, TypeConName
from ..damlast.pkgfile import Dar
from ..damlast.protocols import SymbolLookup
from ..ledger import (
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
)
from ..metrics import MetricEvents
from ..prim import ContractData, ContractId, Party, TimeDeltaLike, to_party
from ..protocols.events import (
    ContractArchiveEvent,
    ContractCreateEvent,
    ContractExercisedEvent,
    InitEvent,
    PackagesAddedEvent,
    ReadyEvent,
    TransactionEndEvent,
    TransactionStartEvent,
)
from ..query import ContractMatch, is_match
from ..scheduler import RunLevel, validate_install_signal_handlers
from ..util.asyncio_util import await_then
from ..util.io import get_bytes
from ..util.tools import as_list
from ._base_model import CREATE_IF_MISSING, IfMissingPartyBehavior
from ._events import (
    AEventHandler,
    AEventHandlerDecorator,
    EventHandler,
    EventHandlerDecorator,
    fluentize,
)
from ._network_client_impl import _NetworkImpl
from ._party_client_impl import _PartyClientImpl
from .bots import Bot, BotCollection
from .commands import EventHandlerResponse
from .config import AnonymousNetworkConfig, NetworkConfig, PartyConfig
from .events import EventKey
from .ledger import LedgerMetadata
from .state import ContractContextualData, ContractContextualDataCollection, ContractsState

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    from ..model.types import TemplateNameLike

__all__ = [
    "DEFAULT_TIMEOUT_SECONDS",
    "simple_client",
    "async_network",
    "Network",
    "GlobalClient",
    "AIOGlobalClient",
    "SimpleGlobalClient",
    "PartyClient",
    "AIOPartyClient",
    "SimplePartyClient",
]
DEFAULT_TIMEOUT_SECONDS = 30


@contextmanager
def simple_client(
    url: Optional[str] = None,
    party: Union[None, str, Party] = None,
    log_level: Optional[int] = INFO,
):
    """
    Start up a single client connecting to a single specific party.

    :param url:
        The URL of the client to connect to. Defaults to the value of the ``DAML_LEDGER_URL``
        environment variable (if set).
    :param party:
        The party to connect as. Defaults to the value of the ``DAML_LEDGER_PARTY`` environment
        variable if it is set.
    :param log_level:
        If non-``None``, configure a default logger that logs output at the specified level. The
        default value is ``INFO``.
    :return:
        A :class:`SimplePartyClient` that can be used in a completely blocking, synchronous
        fashion.
    """
    if log_level is not None:
        from .. import setup_default_logger

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            setup_default_logger(log_level)

    if url is None:
        url = os.getenv("DAML_LEDGER_URL")
    if not url:
        raise ValueError(
            "url must be specified, or the DAML_LEDGER_URL environment variable " "must be set"
        )
    if not party:
        raise ValueError(
            "party must be specified, or the DAML_LEDGER_PARTY environment variable " "must be set"
        )

    LOG.info("Starting a simple_client with to %s with party %r...", url, party)

    network = Network()
    network.set_config(url=url)
    client = network.simple_party(party) if party else network.simple_new_party()

    network.start_in_background()

    yield client

    network.shutdown()
    network.join()


# This class is intended to be used as a function.
# noinspection PyPep8Naming
class async_network:
    """
    Create a :class:`Network` and ensure that it has the given set of DARs loaded.
    """

    def __init__(
        self,
        url: Optional[str] = None,
        dars: Optional[Union[Dar, Collection[Dar]]] = None,
    ):
        LOG.debug("async_network.__init__")
        self.network = Network()
        if url:
            self.network.set_config(url=url)
        self.dars = as_list(dars)  # type: List[Dar]

        LOG.debug("Analyzing package_id config...")
        self.package_ids = (
            {pkg_id for dar in self.dars for pkg_id in get_dar_package_ids(dar)}
            if self.dars
            else None
        )
        LOG.debug("Package id analysis done.")

        if self.package_ids:
            self.network.set_config(package_ids=self.package_ids)

    async def __aenter__(self):
        LOG.debug("async_network.__aenter__")

        for dar in self.dars:
            await self.network.aio_global().ensure_dar(dar)
        return self.network

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        LOG.debug("async_network.__aexit__")
        fut = self.network.shutdown()
        if fut is not None:
            await fut


class Network:
    """
    Manages network connection/scheduling logic on behalf of one or more :class:`PartyClient`
    instances.
    """

    def __init__(self, metrics: Optional[MetricEvents] = None):
        self._impl = _NetworkImpl(metrics)
        self._main_fut = None  # type: Optional[Future]

    def set_config(
        self,
        *config: Union[NetworkConfig, AnonymousNetworkConfig],
        url: Optional[str] = None,
        admin_url: Optional[str] = None,
        **kwargs,
    ):
        self._impl.set_config(*config, url=url, admin_url=admin_url, **kwargs)

    @property
    def lookup(self) -> SymbolLookup:
        """
        Return a :class:`SymbolLookup` that provides type and package information for known
        packages.
        """
        return self._impl.lookup

    def resolved_config(self) -> NetworkConfig:
        """
        Calculate the configuration that will be used for this client when it is instantiated.
        """
        return self._impl.resolved_config()

    # <editor-fold desc="Global/Party client creation">

    def simple_global(self) -> "SimpleGlobalClient":
        """
        Return a :class:`GlobalClient` that exposes thread-safe, synchronous (blocking) methods for
        communicating with a ledger. Callbacks are dispatched to background threads.
        """
        return self._impl.global_impl(SimpleGlobalClient)

    def aio_global(self) -> "AIOGlobalClient":
        """
        Return a :class:`GlobalClient` that works on an asyncio event loop.

        Note that once this object can only be accessed from the asyncio event loop it is intended
        to be used on.
        """
        client = self._impl.global_impl(AIOGlobalClient)
        self._impl.freeze()
        return client

    def simple_party(self, party: Union[str, Party]) -> "SimplePartyClient":
        """
        Return a :class:`PartyClient` that exposes thread-safe, synchronous (blocking) methods for
        communicating with a ledger. Callbacks are dispatched to background threads.

        :param party: The party to get a client for.
        """
        return self._impl.party_impl_wrapper(to_party(party), SimplePartyClient)

    def simple_new_party(self) -> "SimplePartyClient":
        """
        Return a :class:`PartyClient` that exposes thread-safe, synchronous (blocking) methods for
        communicating with a ledger. Callbacks are dispatched to background threads.
        """
        return self.simple_party(str(uuid4()))

    def aio_party(self, party: Union[str, Party]) -> "AIOPartyClient":
        """
        Return a :class:`PartyClient` that works on an asyncio event loop.

        :param party: The party to get a client for.
        """
        return self._impl.party_impl_wrapper(Party(party), AIOPartyClient)

    def aio_new_party(self) -> "AIOPartyClient":
        """
        Return a :class:`PartyClient` for a random party that works on an asyncio event loop.
        This will never return the same object twice.
        """
        warnings.warn(
            "aio_new_party is deprecated and does not work on Daml 2.x ledgers", DeprecationWarning
        )
        return self.aio_party(str(uuid4()))

    def party_bots(
        self, party: Union[str, Party], if_missing: IfMissingPartyBehavior = CREATE_IF_MISSING
    ) -> BotCollection:
        """
        Return the collection of bots associated with a party.

        :param party: The party to get bots for.
        :param if_missing:
            Specify the behavior to use in the case where no client has been yet requested for this
            party. The default behavior is CREATE_IF_MISSING.
        """
        warnings.warn(
            "bot introspection is deprecated and will be removed in dazl v8",
            DeprecationWarning,
            stacklevel=2,
        )
        party_impl = self._impl.party_impl(party, if_missing=if_missing)
        return party_impl.bots if party_impl is not None else None

    # </editor-fold>

    # <editor-fold desc="Daemon thread-based scheduling API">

    def start_in_background(
        self, daemon: bool = True, install_signal_handlers: Optional[bool] = None
    ) -> None:
        """
        Connect to the ledger in a background thread.

        The current thread does NOT block. Operations on instances of :class:`SimplePartyClient`
        are allowed, and operations on instances of :class:`AIOPartyClient` are allowed as long as
        they are made from the correct thread.
        """
        if validate_install_signal_handlers(install_signal_handlers):
            self._impl.invoker.install_signal_handlers()
        return self._impl.start(daemon)

    def shutdown(self) -> Optional[Awaitable[None]]:
        """
        Gracefully shut down all network connections and notify all clients that they are about to
        be terminated.

        The current thread does NOT block.

        :return:
            ``None`` unless ``start()`` was called, in which case the coroutine that
            corresponds to dazl's "main" is returned.
        """
        self._impl.shutdown()
        if self._main_fut is not None:
            return self._main_fut
        else:
            return None

    def join(self, timeout: Optional[float] = None) -> None:
        """
        Block the current thread until the client is shut down.

        :param timeout:
            Number of seconds to wait before timing out the join, or ``None`` to wait indefinitely.
        """
        return self._impl.join(timeout=timeout)

    # </editor-fold>

    # <editor-fold desc="asyncio-based scheduling API">

    def start(self) -> None:
        """
        Start the coroutine that spawns callbacks for listeners on event streams.
        """
        self._main_fut = ensure_future(self.aio_run(keep_open=False))

    def run_until_complete(
        self, *coroutines: Awaitable[None], install_signal_handlers: Optional[bool] = None
    ) -> None:
        """
        Block the main thread and run the application in an event loop on the main thread. The loop
        terminates when the given (optional) coroutines terminate OR :meth:`shutdown` is called AND
        all active command submissions and event handlers' follow-ups have successfully returned.

        :param coroutines:
            Coroutines to run alongside event handlers and command submissions. When these
            coroutines are done running and the
        :param install_signal_handlers:
            ``True`` to install SIGINT and SIGQUIT event handlers (CTRL+C and CTRL+\\);
            ``False`` to skip installation. The default value is ``None``, which installs signal
            handlers only when called from the main thread (default). If signal handlers are
            requested to be installed and the thread is NOT the main thread, this method throws.
        """
        self._impl.invoker.level = RunLevel.RUN_UNTIL_IDLE
        self._impl.invoker.loop = get_event_loop()
        if validate_install_signal_handlers(install_signal_handlers):
            self._impl.invoker.install_signal_handlers()
        self._impl.invoker.loop.run_until_complete(self.aio_run(*coroutines))
        LOG.info("The internal run_until_complete event loop has now completed.")

    def run_forever(
        self, *coroutines: "Awaitable[None]", install_signal_handlers: "Optional[bool]" = None
    ) -> None:
        """
        Block the main thread and run the application in an event loop on the main thread. The loop
        terminates when :meth:`shutdown` is called AND all active command submissions and event
        handlers' follow-ups have successfully returned.
        """
        self._impl.invoker.loop = get_event_loop()
        if validate_install_signal_handlers(install_signal_handlers):
            self._impl.invoker.install_signal_handlers()
        self._impl.invoker.loop.run_until_complete(self.aio_run(*coroutines))
        LOG.info("The internal run_forever event loop has been shut down.")

    async def aio_run(self, *coroutines, keep_open: bool = True) -> None:
        """
        Coroutine where all network activity is scheduled from. This coroutine exits when
        :meth:`shutdown` is called, and can be used directly as an asyncio-native alternative to
        :meth:`start_in_background` and :meth:`join`.

        You would normally call this method directly only if you are trying to incorporate
        the client into an already-running event loop. Prefer :meth:`run_until_complete` or
        :meth:`run_forever` if you can block the current thread, or :meth:`start_in_background`
        with :meth:`join` if you wish to run the entire client on background threads.
        """
        if not keep_open:
            self._impl.invoker.level = RunLevel.RUN_UNTIL_IDLE
        await self._impl.aio_run(*coroutines)
        LOG.info("The aio_run coroutine has completed.")

    # </editor-fold>

    def parties(self) -> Collection[Party]:
        """
        Return a snapshot of the set of parties that exist right now.
        """
        return self._impl.parties()

    def bots(self) -> Collection[Bot]:
        """
        Return a collection of bots.

        Note that bot introspection will not be a part of the dazl v8 API.
        """
        warnings.warn(
            "bot introspection is deprecated and will be removed in dazl v8",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._impl.bots

    def __enter__(self):
        """
        Allows for use of a :class:`Network` as a context manager.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()


class GlobalClient:
    """
    Public interface for either an async-based or a thread-safe version of an API for interacting
    with a Ledger API implementation that manages global ledger data, such as package store
    management and current time.
    """

    def __init__(self, impl: _NetworkImpl):
        self._impl = impl


class AIOGlobalClient(GlobalClient):
    async def ensure_dar(
        self,
        contents: Union[str, Path, bytes, BinaryIO],
        timeout: TimeDeltaLike = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        """
        Validate that the ledger has the packages specified by the given contents (as a byte array).
        Throw an exception if the specified DARs do not exist within the specified timeout.

        :param contents: The DAR or DALF to ensure.
        :param timeout: The maximum length of time to wait before giving up.
        """
        raw_bytes = get_bytes(contents)
        return await self._impl.upload_package(raw_bytes, timeout)

    async def ensure_packages(
        self,
        package_ids: Collection[PackageRef],
        timeout: TimeDeltaLike = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        """
        Validate that packages with the specified package IDs exist on the ledger. Throw an
        exception if the specified packages do not exist within the specified timeout.

        :param package_ids: The set of package IDs to check for.
        :param timeout: The maximum length of time to wait before giving up.
        """
        return await self._impl.ensure_package_ids(package_ids, timeout)

    async def metadata(self) -> LedgerMetadata:
        """
        Return the current set of known packages.
        """
        return await self._impl.aio_metadata()


class SimpleGlobalClient(GlobalClient):
    def ensure_dar(
        self,
        contents: Union[str, Path, bytes, BinaryIO],
        timeout: TimeDeltaLike = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        """
        Validate that the ledger has the packages specified by the given contents (as a byte array).
        Throw an exception if the specified DARs do not exist within the specified timeout.

        :param contents: The DAR or DALF to ensure.
        :param timeout: The maximum length of time to wait before giving up.
        """
        raw_bytes = get_bytes(contents)
        return self._impl.invoker.run_in_loop(lambda: self._impl.upload_package(raw_bytes, timeout))

    def ensure_packages(
        self,
        package_ids: Collection[PackageRef],
        timeout: TimeDeltaLike = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        """
        Validate that packages with the specified package IDs exist on the ledger. Throw an
        exception if the specified packages do not exist within the specified timeout.

        :param package_ids: The set of package IDs to check for.
        :param timeout: The maximum length of time to wait before giving up.
        """
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.ensure_package_ids(package_ids, timeout)
        )

    def metadata(self, timeout: TimeDeltaLike = DEFAULT_TIMEOUT_SECONDS) -> LedgerMetadata:
        """
        Return the current set of known packages.
        """
        return self._impl.simple_metadata(timeout)


class PartyClient:
    """
    Public interface for either an async-based or a thread-safe version of an API for interacting
    with a Ledger API implementation from the perspective of a single client.
    """

    def __init__(self, impl: _PartyClientImpl):
        self._impl = impl

    # <editor-fold desc="Ledger/client metadata">

    @property
    def party(self) -> Party:
        """
        Return the party serviced by this client.
        """
        return self._impl.party

    def resolved_config(self) -> PartyConfig:
        """
        Calculate the configuration that will be used for this client when it is instantiated.
        """
        return self._impl.resolved_config()

    # </editor-fold>


class AIOPartyClient(PartyClient):
    """
    Implementation of a :class:`PartyClient` that exposes an `async`/`await`-style API that runs on
    an event loop.
    """

    # <editor-fold desc="Event handler registration">

    def ledger_init(self) -> AEventHandlerDecorator[InitEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` has been
        instructed to begin, but before any network activity is started.
        """
        return fluentize(self.add_ledger_init)

    def add_ledger_init(self, handler: AEventHandler[InitEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` has been instructed to
        begin, but before any network activity is started.

        :param handler:
            The handler to register. This can either be a coroutine or a normal function, and may
            return anything that can be successfully coerced into a :class:`CommandPayload`.
        """
        for key in EventKey.init():
            self._impl.add_event_handler(key, handler, None, self)

    def ledger_ready(self) -> AEventHandlerDecorator[ReadyEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` has caught
        up to the head of the ledger, but before any :meth:`ledger_create` or :meth:`ledger_archive`
        callbacks are invoked.
        """
        return fluentize(self.add_ledger_ready)

    def add_ledger_ready(self, handler: AEventHandler[ReadyEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` has caught up to the head of
        the ledger, but before any :meth:`ledger_create` or :meth:`ledger_archive` callbacks are
        invoked.

        :param handler:
            The handler to register. This can either be a coroutine or a normal function, and may
            return anything that can be successfully coerced into a :class:`CommandPayload`.
        """
        for key in EventKey.ready():
            self._impl.add_event_handler(key, handler, None, self)

    def ledger_packages_added(
        self, initial: bool = False
    ) -> AEventHandlerDecorator[PackagesAddedEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` has
        detected new packages added to the ledger.

        :param initial:
            ``True`` to call the handler when the client is ready. This can be useful if you want
            to handle package additions identically whether they were already in the ledger when
            the client started up or only after a package has been added. The default value is
            ``False``, which means that this handler is only called on NEW packages that have been
            uploaded after this client has started.
        :return:
        """
        return fluentize(self.add_ledger_packages_added, initial=initial)

    def add_ledger_packages_added(
        self, handler: AEventHandler[PackagesAddedEvent], initial: bool = False
    ) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` has detected new packages
        added to the ledger.

        :param handler:
            The handler to register. This can either be a coroutine or a normal function, and may
            return anything that can be successfully coerced into a :class:`CommandPayload`.
        :param initial:
            ``True`` to call the handler when the client is ready. This can be useful if you want
            to handle package additions identically whether they were already in the ledger when
            the client started up or only after a package has been added. The default value is
            ``False``, which means that this handler is only called on NEW packages that have been
            uploaded after this client has started.
        :return:
        """
        for key in EventKey.packages_added(initial=initial, changed=True):
            self._impl.add_event_handler(key, handler, None, self)

    def ledger_transaction_start(self) -> AEventHandlerDecorator[TransactionStartEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` receives a
        new transaction. Called before individual :meth:`ledger_create` and :meth:`ledger_archive`
        callbacks.
        """
        return fluentize(self.add_ledger_transaction_start)

    def add_ledger_transaction_start(self, handler: AEventHandler[TransactionStartEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` receives a new transaction.
        Called before individual :meth:`ledger_create` and :meth:`ledger_archive` callbacks.

        :param handler:
            The handler to register. This can either be a coroutine or a normal function, and may
            return anything that can be successfully coerced into a :class:`CommandPayload`.
        """
        for key in EventKey.transaction_start():
            self._impl.add_event_handler(key, handler, None, self)

    def ledger_transaction_end(self) -> AEventHandlerDecorator[TransactionEndEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` receives a
        new transaction. Called after individual :meth:`ledger_create` and :meth:`ledger_archive`
        callbacks.
        """
        return fluentize(self.add_ledger_transaction_end)

    def add_ledger_transaction_end(self, handler: AEventHandler[TransactionEndEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` receives a new transaction.
        Called after individual :meth:`ledger_create` and :meth:`ledger_archive` callbacks.

        :param handler:
            The handler to register. This can either be a coroutine or a normal function, and may
            return anything that can be successfully coerced into a :class:`CommandPayload`.
        """
        for key in EventKey.transaction_end():
            self._impl.add_event_handler(key, handler, None, self)

    def ledger_created(
        self, template: Any, match: Optional[ContractMatch] = None
    ) -> AEventHandlerDecorator[ContractCreateEvent]:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters a newly created
        template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """

        def _register_created(
            cb: AEventHandler[ContractCreateEvent],
        ) -> AEventHandler[ContractCreateEvent]:
            self.add_ledger_created(template, match=match, handler=cb)
            return cb

        return _register_created

    def add_ledger_created(
        self,
        template: Any,
        handler: AEventHandler[ContractCreateEvent],
        match: Optional[ContractMatch] = None,
    ) -> Bot:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters a newly created
        contract instance of a template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param handler:
            The callback to invoke whenever a matching template is created.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """
        filter_fn = (lambda evt: is_match(match, evt.cdata)) if match is not None else None

        bot = self._impl.bots.add_new(party_client=self, name=handler.__name__)
        bot.add_event_handler(EventKey.contract_created(True, template), handler, filter_fn)
        return bot

    def ledger_exercised(
        self, template: Any, choice: str
    ) -> AEventHandlerDecorator[ContractExercisedEvent]:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters an exercised
        choice event.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param choice:
            The name of the choice to listen for exercises on.
        """

        def _register_exercised(
            cb: AEventHandler[ContractExercisedEvent],
        ) -> AEventHandler[ContractExercisedEvent]:
            self.add_ledger_exercised(template, choice, handler=cb)
            return cb

        return _register_exercised

    def add_ledger_exercised(
        self, template: Any, choice: str, handler: AEventHandler[ContractExercisedEvent]
    ) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters an exercised
        choice event.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param choice:
            The name of the choice to listen for exercises on.
        :param handler:
            The callback to invoke whenever a matching template is exercised.
        """
        for key in EventKey.contract_exercised(True, template, choice):
            self._impl.add_event_handler(key, handler, None, self)

    def ledger_archived(
        self, template: Any, match: Optional[ContractMatch] = None
    ) -> AEventHandlerDecorator[ContractArchiveEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` encounters
        a newly archived contract instance of a template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """

        def _register_archived(
            cb: AEventHandler[ContractArchiveEvent],
        ) -> AEventHandler[ContractArchiveEvent]:
            self.add_ledger_archived(template, match=match, handler=cb)
            return cb

        return _register_archived

    def add_ledger_archived(
        self,
        template: Any,
        handler: AEventHandler[ContractArchiveEvent],
        match: Optional[ContractMatch] = None,
    ) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters a newly archived
        contract instance of a template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param handler:
            The callback to invoke whenever a matching template is created.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """
        filter_fn = (lambda evt: is_match(match, evt.cdata)) if match is not None else None

        for key in EventKey.contract_archived(True, template):
            self._impl.add_event_handler(key, handler, filter_fn, self)

    # </editor-fold>

    # <editor-fold desc="Command submission">

    def submit(
        self,
        commands: EventHandlerResponse,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
        *,
        command_id: Optional[str] = None,
    ) -> Awaitable[None]:
        """
        Submit commands to the ledger.

        :param commands:
            An object that can be converted to a command.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        return self._impl.write_commands(
            commands,
            workflow_id=workflow_id,
            command_id=command_id,
            deduplication_time=deduplication_time,
        )

    async def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> CreateEvent:
        """
        Create a contract for a given template.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The :class:`CreateEvent` that represents the contract that was successfully created.
        """
        return await self._impl.write_create(
            CreateCommand(template_id=__template_id, payload=__payload),
            workflow_id=workflow_id,
            command_id=command_id,
        )

    def submit_create(
        self,
        template_name: TemplateNameLike,
        arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> Awaitable[None]:
        """
        Submit a single create command. Equivalent to calling :meth:`submit` with a single
        ``create``.

        :param template_name:
            The name of the template.
        :param arguments:
            The arguments to the create (as a ``dict``).
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        warnings.warn(
            "submit_create is deprecated; use create instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import create

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = create(template_name, arguments)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    async def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        return await self._impl.write_exercise(
            ExerciseCommand(contract_id=__contract_id, choice=__choice_name, argument=__argument),
            workflow_id=workflow_id,
            command_id=command_id,
        )

    def submit_exercise(
        self,
        cid: ContractId,
        choice_name: str,
        arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> Awaitable[None]:
        """
        Submit a single exercise choice. Equivalent to calling :meth:`submit` with a single
        ``exercise``.

        :param cid:
            The :class:`ContractId` on which a choice is being exercised.
        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            The arguments to the exercise (as a ``dict``). Can be omitted (``None``) for no-argument
            choices.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        warnings.warn(
            "submit_exercise is deprecated; use exercise instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import exercise

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = exercise(cid, choice_name, arguments)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    async def exercise_by_key(
        self,
        __template_id: Union[str, TypeConName],
        __choice_name: str,
        __key: Any,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        return await self._impl.write_exercise(
            ExerciseByKeyCommand(
                template_id=__template_id, choice=__choice_name, key=__key, argument=__argument
            ),
            workflow_id=workflow_id,
            command_id=command_id,
        )

    def submit_exercise_by_key(
        self,
        template_name: TemplateNameLike,
        contract_key: Any,
        choice_name: str,
        arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> Awaitable[None]:
        """
        Synchronously submit a single exercise choice. Equivalent to calling :meth:`submit` with a
        single ``exercise_by_key``.

        :param template_name:
            The name of the template on which to do an exercise-by-key.
        :param contract_key:
            The value that should uniquely identify a contract for the specified template.
        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            The arguments to the create (as a ``dict``). Can be omitted (``None``) for no-argument
            choices.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        """
        warnings.warn(
            "submit_exercise_by_key is deprecated; use exercise_by_key instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import exercise_by_key

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = (exercise_by_key(template_name, contract_key, choice_name, arguments),)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    async def create_and_exercise(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a newly-created contract, in a single transaction.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument (positional
            argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        return await self._impl.write_exercise(
            CreateAndExerciseCommand(
                template_id=__template_id,
                payload=__payload,
                choice=__choice_name,
                argument=__argument,
            ),
            workflow_id=workflow_id,
            command_id=command_id,
        )

    def submit_create_and_exercise(
        self,
        template_name: TemplateNameLike,
        arguments: dict,
        choice_name: str,
        choice_arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> Awaitable[None]:
        """
        Synchronously submit a single create-and-exercise command. Equivalent to calling
        :meth:`submit` with a single ``create_and_exercise``.

        :param template_name:
            The name of the template on which to do an exercise-by-key.
        :param arguments:
            The arguments to the create (as a ``dict``).
        :param choice_name:
            The name of the choice to exercise.
        :param choice_arguments:
            The arguments to the exercise (as a ``dict``). Can be omitted (``None``) for no-argument
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        """
        warnings.warn(
            "submit_create_and_exercise is deprecated; use create_and_exercise instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import create_and_exercise

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = create_and_exercise(template_name, arguments, choice_name, choice_arguments)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    # </editor-fold>

    # <editor-fold desc="Active contract set">

    def find_by_id(self, cid: Union[str, ContractId]) -> Optional[ContractContextualData]:
        return self._impl.find_by_id(cid)

    def find(
        self, template: Any, match: ContractMatch = None, include_archived: bool = False
    ) -> ContractContextualDataCollection:
        return self._impl.find(template, match, include_archived=include_archived)

    def find_active(self, template: Any, match: ContractMatch = None) -> ContractsState:
        """
        Immediately return data from the current active contract set.

        The contents of this ACS are guaranteed to be present (or removed) in the current
        transaction _before_ processing any corresponding ``on_created`` or ``on_archived``
        callbacks for this party. The ACS is populated _before_ processing any ``on_ready``
        callbacks.

        This method raises an error if ACS tracking has been disabled on this client.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :return:
            A ``dict`` whose keys are :class:`ContractId` and values are corresponding contract
            data that match the current query.
        """
        return self._impl.find_active(template, match)

    def find_historical(
        self, template: Any, match: ContractMatch = None
    ) -> ContractContextualDataCollection:
        """
        Immediately return data from the current active and historical contract set as
        a contextual data collection

        The contents of this set are guaranteed to be up-to-date in the current transaction _before_
        processing any corresponding ``on_created`` or ``on_archived`` callbacks for this party. The
        set is up-to-date _before_ processing any ``on_ready`` callbacks.

        This method raises an error if historical tracking has been disabled on this client.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :return:
            A ``ContractContextualDataCollection`` whose values correspond to the contract
            data for active and archived contracts matching the current query.
        """
        return self._impl.find_historical(template, match)

    def find_one(
        self, template: Any, match: "ContractMatch" = None, timeout: float = DEFAULT_TIMEOUT_SECONDS
    ) -> Awaitable[Tuple[ContractId, ContractData]]:
        """
        Return data from the current active contract set when at least some amount of rows exist in
        the active contract set.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :param timeout:
            Number of seconds in which to time out the search.
        :return:
            A ``Future`` that is resolved with a ``dict`` whose keys are :class:`ContractId` and
            values are corresponding contract data that match the current query.
        """
        return await_then(
            self.find_nonempty(template, match, min_count=1, timeout=timeout),
            lambda state: next(iter(state.items())),
        )

    def find_nonempty(
        self,
        template: Any,
        match: ContractMatch,
        min_count: int = 1,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
    ) -> Awaitable[ContractsState]:
        """
        Return data from the current active contract set when at least some amount of rows exist in
        the active contract set.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :param min_count:
            The minimum number of rows to return. The default value is 1.
        :param timeout:
            Number of seconds in which to time out the search.
        :return:
            A ``Future`` that is resolved with a ``dict`` whose keys are :class:`ContractId` and
            values are corresponding contract data that match the current query.
        """
        return self._impl.find_nonempty(template, match, min_count, timeout)

    # </editor-fold>

    # <editor-fold desc="Ledger/client metadata">

    def set_config(self, url: "Optional[str]", **kwargs):
        self._impl.set_config(url=url, **kwargs)

    async def ensure_dar(
        self,
        contents: Union[str, Path, bytes, BinaryIO],
        timeout: TimeDeltaLike = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        """
        Validate that the ledger has the packages specified by the given contents (as a byte array).
        Throw an exception if the specified DARs do not exist within the specified timeout.

        :param contents: The DAR or DALF to ensure.
        :param timeout: The maximum length of time to wait before giving up.
        """
        raw_bytes = get_bytes(contents)
        return await self._impl.parent.upload_package(raw_bytes, timeout)

    def ready(self) -> "Awaitable[None]":
        """
        Block until the ledger client has caught up to the current head and is ready to send
        commands.
        """
        return self._impl.ready()

    # </editor-fold>


class SimplePartyClient(PartyClient):
    """
    Implementation of a :class:`PartyClient` that exposes blocking calls, but can be used from any
    thread.

    Use this implementation if any of these apply:
      * you wish to interact with libraries that do not natively support asyncio
      * you are comfortable with the trade-off of having to block threads in order to write code
    """

    # <editor-fold desc="Event handler registration">

    def ledger_init(self) -> "EventHandlerDecorator[InitEvent]":
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` has been
        instructed to begin, but before any network activity is started.
        """
        return fluentize(self.add_ledger_init)

    def add_ledger_init(self, handler: EventHandler[InitEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` has been instructed to
        begin, but before any network activity is started.

        :param handler:
            The handler to register. May return anything that can be successfully coerced into a
            :class:`CommandPayload`.
        """

        @wraps(handler)
        def _background_ledger_init(event: InitEvent) -> Awaitable[EventHandlerResponse]:
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        for key in EventKey.init():
            self._impl.add_event_handler(key, _background_ledger_init, None, self)

    def ledger_ready(self) -> EventHandlerDecorator[ReadyEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` has caught
        up to the head of the ledger, but before any :meth:`ledger_create` or :meth:`ledger_archive`
        callbacks are invoked.
        """
        return fluentize(self.add_ledger_ready)

    def add_ledger_ready(self, handler: EventHandler[ReadyEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` has caught up to the head of
        the ledger, but before any :meth:`ledger_create` or :meth:`ledger_archive` callbacks are
        invoked.

        :param handler:
            The handler to register. May return anything that can be successfully coerced into a
            :class:`CommandPayload`.
        """

        @wraps(handler)
        def _background_ledger_ready(event: ReadyEvent) -> Awaitable[EventHandlerResponse]:
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        for key in EventKey.ready():
            self._impl.add_event_handler(key, _background_ledger_ready, None, self)

    def ledger_packages_added(
        self, initial: bool = False
    ) -> EventHandlerDecorator[PackagesAddedEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` has
        detected new packages added to the ledger.

        :param initial:
            ``True`` to call the handler when the client is ready. This can be useful if you want
            to handle package additions identically whether they were already in the ledger when
            the client started up or only after a package has been added. The default value is
            ``False``, which means that this handler is only called on NEW packages that have been
            uploaded after this client has started.
        :return:
        """
        return fluentize(self.add_ledger_packages_added, initial=initial)

    def add_ledger_packages_added(
        self, handler: EventHandler[PackagesAddedEvent], initial: bool = False
    ) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` has detected new packages
        added to the ledger.

        :param handler:
            The handler to register. May return anything that can be successfully coerced into a
            :class:`CommandPayload`.
        :param initial:
            ``True`` to call the handler when the client is ready. This can be useful if you want
            to handle package additions identically whether they were already in the ledger when
            the client started up or only after a package has been added. The default value is
            ``False``, which means that this handler is only called on NEW packages that have been
            uploaded after this client has started.
        :return:
        """

        @wraps(handler)
        def _background_ledger_packages_added(
            event: PackagesAddedEvent,
        ) -> Awaitable[EventHandlerResponse]:
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        for key in EventKey.packages_added(initial=initial, changed=True):
            self._impl.add_event_handler(key, _background_ledger_packages_added, None, self)

    def ledger_transaction_start(self) -> EventHandlerDecorator[TransactionStartEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` receives a
        new transaction. Called before individual :meth:`ledger_create` and :meth:`ledger_archive`
        callbacks.
        """
        return fluentize(self.add_ledger_transaction_start)

    def add_ledger_transaction_start(self, handler: EventHandler[TransactionStartEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` receives a new transaction.
        Called before individual :meth:`ledger_create` and :meth:`ledger_archive` callbacks.

        :param handler:
            The handler to register. This can either be a coroutine or a normal function, and may
            return anything that can be successfully coerced into a :class:`CommandPayload`.
        """

        @wraps(handler)
        def _background_ledger_transaction_start(
            event: TransactionStartEvent,
        ) -> Awaitable[EventHandlerResponse]:
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        for key in EventKey.transaction_start():
            self._impl.add_event_handler(key, _background_ledger_transaction_start, None, self)

    def ledger_transaction_end(self) -> EventHandlerDecorator[TransactionEndEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` receives a
        new transaction. Called after individual :meth:`ledger_create` and :meth:`ledger_archive`
        callbacks.
        """

        def _register_transaction_end(
            cb: EventHandler[TransactionEndEvent],
        ) -> EventHandler[TransactionEndEvent]:
            self.add_ledger_transaction_end(cb)
            return cb

        return _register_transaction_end

    def add_ledger_transaction_end(self, handler: EventHandler[TransactionEndEvent]) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` receives a new transaction.
        Called after individual :meth:`ledger_create` and :meth:`ledger_archive` callbacks.

        :param handler:
            The handler to register. This can either be a coroutine or a normal function, and may
            return anything that can be successfully coerced into a :class:`CommandPayload`.
        """

        @wraps(handler)
        def _background_ledger_transaction_end(
            event: TransactionEndEvent,
        ) -> Awaitable[EventHandlerResponse]:
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        for key in EventKey.transaction_end():
            self._impl.add_event_handler(key, _background_ledger_transaction_end, None, self)

    def ledger_created(
        self, template: Any, match: Optional[ContractMatch] = None
    ) -> EventHandlerDecorator[ContractCreateEvent]:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters a newly created
        template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """

        def _register_created(
            cb: EventHandler[ContractCreateEvent],
        ) -> EventHandler[ContractCreateEvent]:
            self.add_ledger_created(template, match=match, handler=cb)
            return cb

        return _register_created

    def add_ledger_created(
        self,
        template: Any,
        handler: EventHandler[ContractCreateEvent],
        match: Optional[ContractMatch] = None,
    ) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters a newly created
        contract instance of a template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param handler:
            The callback to invoke whenever a matching template is created.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """

        @wraps(handler)
        def _background_ledger_contract_create(
            event: ContractCreateEvent,
        ) -> Awaitable[EventHandlerResponse]:
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        filter_fn = (lambda evt: is_match(match, evt.cdata)) if match is not None else None

        for key in EventKey.contract_created(True, template):
            self._impl.add_event_handler(key, _background_ledger_contract_create, filter_fn, self)

    def ledger_exercised(
        self, template: "Any", choice: str
    ) -> EventHandlerDecorator[ContractExercisedEvent]:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters an exercised
        choice event.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param choice:
            The name of the choice to listen for exercises on.
        """

        def _register_exercised(
            cb: EventHandler[ContractExercisedEvent],
        ) -> EventHandler[ContractExercisedEvent]:
            self.add_ledger_exercised(template, choice, handler=cb)
            return cb

        return _register_exercised

    def add_ledger_exercised(
        self, template: Any, choice: str, handler: EventHandler[ContractExercisedEvent]
    ) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters an exercised
        choice event.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param choice:
            The name of the choice to listen for exercises on.
        :param handler:
            The callback to invoke whenever a matching template is exercised.
        """

        @wraps(handler)
        def _background_ledger_contract_exercised(
            event: "ContractExercisedEvent",
        ) -> "Awaitable[EventHandlerResponse]":
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        for key in EventKey.contract_exercised(True, template, choice):
            self._impl.add_event_handler(key, _background_ledger_contract_exercised, None, self)

    def ledger_archived(
        self, template: Any, match: Optional[ContractMatch] = None
    ) -> EventHandlerDecorator[ContractArchiveEvent]:
        """
        Decorator for registering a callback to be invoked when the :class:`PartyClient` encounters
        a newly archived contract instance of a template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """

        def _register_archived(
            cb: EventHandler[ContractArchiveEvent],
        ) -> EventHandler[ContractArchiveEvent]:
            self.add_ledger_archived(template, match=match, handler=cb)
            return cb

        return _register_archived

    def add_ledger_archived(
        self,
        template: Any,
        handler: EventHandler[ContractArchiveEvent],
        match: Optional[ContractMatch] = None,
    ) -> None:
        """
        Register a callback to be invoked when the :class:`PartyClient` encounters a newly archived
        contract instance of a template.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param handler:
            The callback to invoke whenever a matching template is created.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        """

        @wraps(handler)
        def _background_ledger_contract_archived(
            event: ContractArchiveEvent,
        ) -> Awaitable[EventHandlerResponse]:
            return self._impl.invoker.run_in_executor(lambda: handler(event))

        filter_fn = (lambda evt: is_match(match, evt.cdata)) if match is not None else None

        for key in EventKey.contract_archived(True, template):
            self._impl.add_event_handler(key, _background_ledger_contract_archived, filter_fn, self)

    # </editor-fold>

    # region Command submission

    def submit(
        self,
        commands,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> None:
        """
        Submit commands to the ledger.

        :param commands:
            An object that can be converted to a command.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.write_commands(
                commands, workflow_id=workflow_id, deduplication_time=deduplication_time
            )
        )

    def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> CreateEvent:
        """
        Create a contract for a given template.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The :class:`CreateEvent` that represents the contract that was successfully created.
        """
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.write_create(
                CreateCommand(__template_id, __payload),
                workflow_id=workflow_id,
                command_id=command_id,
            )
        )

    def submit_create(
        self,
        template_name: TemplateNameLike,
        arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> None:
        """
        Synchronously submit a single create command. Equivalent to calling :meth:`submit` with a
        single ``create``.

        :param template_name:
            The name of the template.
        :param arguments:
            The arguments to the create (as a ``dict``).
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        """
        warnings.warn(
            "submit_create is deprecated; use create instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import create

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = create(template_name, arguments)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.write_exercise(
                ExerciseCommand(__contract_id, __choice_name, __argument),
                workflow_id=workflow_id,
                command_id=command_id,
            )
        )

    def submit_exercise(
        self,
        cid: ContractId,
        choice_name: str,
        arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> None:
        """
        Synchronously submit a single exercise choice. Equivalent to calling :meth:`submit` with a
        single ``exercise``.

        :param cid:
            The :class:`ContractId` on which a choice is being exercised.
        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            The arguments to the exercise (as a ``dict``). Can be omitted (``None``) for no-argument
            choices.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        """
        warnings.warn(
            "submit_exercise is deprecated; use exercise instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import exercise

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = exercise(cid, choice_name, arguments)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    def exercise_by_key(
        self,
        __template_id: Union[str, TypeConName],
        __choice_name: str,
        __key: Any,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.write_exercise(
                ExerciseByKeyCommand(__template_id, __choice_name, __key, __argument),
                workflow_id=workflow_id,
                command_id=command_id,
            )
        )

    def submit_exercise_by_key(
        self,
        template_name: TemplateNameLike,
        contract_key: Any,
        choice_name: str,
        arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> None:
        """
        Synchronously submit a single exercise choice. Equivalent to calling :meth:`submit` with a
        single ``exercise_by_key``.

        :param template_name:
            The name of the template on which to do an exercise-by-key.
        :param contract_key:
            The value that should uniquely identify a contract for the specified template.
        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            The arguments to the create (as a ``dict``). Can be omitted (``None``) for no-argument
            choices.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        """
        warnings.warn(
            "submit_exercise_by_key is deprecated; use exercise_by_key instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import exercise_by_key

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = exercise_by_key(template_name, contract_key, choice_name, arguments)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    def create_and_exercise(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a newly-created contract, in a single transaction.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument (positional
            argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.write_exercise(
                CreateAndExerciseCommand(__template_id, __payload, __choice_name, __argument),
                workflow_id=workflow_id,
                command_id=command_id,
            )
        )

    def submit_create_and_exercise(
        self,
        template_name: TemplateNameLike,
        arguments: dict,
        choice_name: str,
        choice_arguments: Optional[dict] = None,
        workflow_id: Optional[str] = None,
        deduplication_time: Optional[TimeDeltaLike] = None,
    ) -> None:
        """
        Synchronously submit a single create-and-exercise command. Equivalent to calling
        :meth:`submit` with a single ``create_and_exercise``.

        :param template_name:
            The name of the template on which to do an exercise-by-key.
        :param arguments:
            The arguments to the create (as a ``dict``).
        :param choice_name:
            The name of the choice to exercise.
        :param choice_arguments:
            The arguments to the exercise (as a ``dict``). Can be omitted (``None``) for no-argument
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :param deduplication_time:
            The length of the time window during which all commands with the same party and command
            ID will be deduplicated. Duplicate commands submitted before the end of this window
            return an ``ALREADY_EXISTS`` error.
        """
        warnings.warn(
            "submit_create_and_exercise is deprecated; use create_and_exercise instead",
            DeprecationWarning,
            stacklevel=2,
        )

        from .. import create_and_exercise

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            cmd = create_and_exercise(template_name, arguments, choice_name, choice_arguments)

        return self.submit(
            cmd,
            workflow_id=workflow_id,
            deduplication_time=deduplication_time,
        )

    # endregion

    # <editor-fold desc="Active contract set">

    def find_by_id(self, cid: Union[str, ContractId]) -> Optional[ContractContextualData]:
        return self._impl.invoker.run_in_loop(lambda: self._impl.find_by_id(cid))

    def find(
        self, template: Any, match: ContractMatch = None, include_archived: bool = False
    ) -> ContractContextualDataCollection:
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.find(template, match, include_archived=include_archived)
        )

    def find_active(self, template: Any, match: ContractMatch = None) -> "ContractsState":
        """
        Immediately return data from the current active contract set.

        The contents of this ACS are guaranteed to be present (or removed) in the current
        transaction _before_ processing any corresponding ``on_created`` or ``on_archived``
        callbacks for this party. The ACS is populated _before_ processing any ``on_ready``
        callbacks.

        This method raises an error if ACS tracking has been disabled on this client.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :return:
            A ``dict`` whose keys are :class:`ContractId` and values are corresponding contract
            data that match the current query.
        :return:
            A ``dict`` whose keys are :class:`ContractId` and values are corresponding contract
            data that match the current query.
        """
        return self._impl.invoker.run_in_loop(lambda: self._impl.find_active(template, match))

    def find_historical(
        self, template: Any, match: ContractMatch = None
    ) -> ContractContextualDataCollection:
        """
        Immediately return data from the current active and historical contract set.

        The contents of this set are guaranteed to be up-to-date in the current transaction _before_
        processing any corresponding ``on_created`` or ``on_archived`` callbacks for this party. The
        set is up-to-date _before_ processing any ``on_ready`` callbacks.

        This method raises an error if historical tracking has been disabled on this client.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :return:
            A ``dict`` whose keys are :class:`ContractId` and values are corresponding contract
            data that match the current query.
        :return:
            A ``dict`` whose keys are :class:`ContractId` and values are corresponding contract
            data that match the current query.
        """
        return self._impl.invoker.run_in_loop(lambda: self._impl.find_historical(template, match))

    def find_one(
        self, template: Any, match: ContractMatch = None, timeout: float = DEFAULT_TIMEOUT_SECONDS
    ) -> Tuple[ContractId, ContractData]:
        """
        Return data from the current active contract set when at least some amount of rows exist in
        the active contract set.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :param timeout:
            Number of seconds in which to time out the search.
        :return:
            A ``Future`` that is resolved with a ``dict`` whose keys are :class:`ContractId` and
            values are corresponding contract data that match the current query.
        """
        state = self.find_nonempty(template, match, min_count=1, timeout=timeout)
        return next(iter(state.items()))

    def find_nonempty(
        self,
        template: Any,
        match: ContractMatch,
        min_count: int = 1,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
    ) -> ContractsState:
        """
        Return data from the current active contract set when at least some amount of rows exist in
        the active contract set.

        :param template:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :param min_count:
            The minimum number of rows to return. The default value is 1.
        :param timeout:
            Number of seconds in which to time out the search.
        :return:
            A ``Future`` that is resolved with a ``dict`` whose keys are :class:`ContractId` and
            values are corresponding contract data that match the current query.
        """
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.find_nonempty(template, match, min_count=min_count, timeout=timeout)
        )

    # </editor-fold>

    # <editor-fold desc="Ledger/client metadata">

    def set_config(self, url: Optional[str], **kwargs):
        self._impl.set_config(url=url, **kwargs)

    def ensure_dar(
        self,
        contents: Union[str, Path, bytes, BinaryIO],
        timeout: TimeDeltaLike = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        """
        Validate that the ledger has the packages specified by the given contents (as a byte array).
        Throw an exception if the specified DARs do not exist within the specified timeout.

        :param contents: The DAR or DALF to ensure.
        :param timeout: The maximum length of time to wait before giving up.
        """
        raw_bytes = get_bytes(contents)
        return self._impl.invoker.run_in_loop(
            lambda: self._impl.parent.upload_package(raw_bytes, timeout)
        )

    def ready(self) -> None:
        """
        Block until the underlying infrastructure has connected to all necessary services.
        """
        # TODO: Improve on this implementation; this spin loop is unnecessarily ugly
        from time import sleep

        while self._impl.invoker.loop is None:
            sleep(0.1)

        LOG.debug("Waiting for the underlying implementation to be ready...")
        return self._impl.invoker.run_in_loop(lambda: self._impl.ready())

    # </editor-fold>
