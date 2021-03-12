# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import signal
from typing import AbstractSet, Any, Awaitable, Collection, Dict, NoReturn, Optional, Union
from uuid import uuid4
import warnings

from ..damlast.protocols import SymbolLookup
from ..prim import Party
from ..protocols.ledgerapi import connect
from ..protocols.pkgcache import SHARED_PACKAGE_DATABASE
from .v8 import ConnectionReuseWarning, NotSupportedError
from .v8_client_aio import AIOGlobalClient, AIOPartyClient

__all__ = ["Network"]

from ..scheduler import validate_install_signal_handlers

_NS_CONFIG_CHANGE = (
    "configuration is handled differently in the new API and introspection "
    "of configuration through resolved_config is no longer supported"
)
_NS_BOT_INTROSPECTION = "bot introspection is not supported with Network"
_NS_BLOCKING_CALLS = "blocking thread connections are not yet supported"


class Network:
    """
    A transitional replacement for :class:`Network` that keeps the same superficial API, but changes
    some of the semantics to match the newer API.

    This is an "almost" compatible implementation that can be used in place of :class:`Network` in
    most simple dazl applications, and can be used to help find potential issues when trying to
    transition to the new connection API with a small investment.
    """

    def __init__(self):
        super().__init__()
        self._async_clients = {}  # type: Dict[Party, AIOPartyClient]
        self._admin_client = None  # type: Optional[AIOGlobalClient]
        self._config = {"admin": True}  # type: Dict[str, Any]

    def set_config(
        self,
        url: "Optional[str]" = None,
        admin_url: "Optional[str]" = None,
        max_connection_count: "Optional[int]" = None,
        quiet_timeout: "Optional[float]" = None,
        use_acs_service: bool = True,
        ca_file: "Optional[str]" = None,
        cert_file: "Optional[str]" = None,
        cert_key_file: "Optional[str]" = None,
        verify_ssl: "Optional[str]" = None,
        max_consequence_depth: "Optional[int]" = None,
        party_groups: "Optional[Union[str, Party], Collection[Union[str, Party]]]" = None,
        package_ids: "Optional[Collection[str]]" = None,
        poll_interval: "Optional[float]" = None,
        connect_timeout: "Optional[float]" = None,
        eager_package_fetch: "Optional[bool]" = None,
        enable_http_proxy: "Optional[bool]" = None,
    ):
        """
        Sets configuration parameters that are shared among all the clients created from this
        configuration. Some of these configuration parameters behave differently in the
        v8 Network API; please pay close attention to the documentation of each flag for more
        information.

        :param url:
            The URL to use for all clients created from this ``Network``.
        :param admin_url:
            This parameter is unused.
        :param max_connection_count:
            This parameter is unused.
        :param quiet_timeout:
            This parameter is unused.
        :param use_acs_service:
            This value must be unspecified or True; the active contract set service is always used
            and this is not configurable.
        :param ca_file:
            Path to a certificate authority file.
        :param cert_file:
            Path to a public key cert file.
        :param cert_key_file:
            Path to a private key cert file.
        :param verify_ssl:
            This parameter is unused.
        :param max_consequence_depth:
            This parameter is unused, as dazl does not attempt to correlate the behavior of
            streams across parties.
        :param party_groups:
            A set of read-as parties to add to every connection created on this Network. This field
            behaves differently than in the old API, as _submissions_ take this read-as set into
            account in Daml Connect 1.9 and later.
        :param package_ids:
            This parameter is unused. Daml packages are always loaded on-demand with this
            implementation.
        :param poll_interval:
            This parameter is unused. In the new API, dazl does not internally poll for any
            reason.
        :param connect_timeout:
            Number of seconds before giving upon a connection.
        :param eager_package_fetch:
            This parameter is unused. Daml packages are always loaded on-demand with this
            implementation.
        :param enable_http_proxy:
            True to allow gRPC to use HTTP proxy server settings; False to disallow it.
        """
        # These parameters are obsoleted by the new API and ignored.
        if url:
            self._config["url"] = url
        if admin_url:
            warnings.warn("admin_url has no effect", DeprecationWarning, stacklevel=2)
        if max_connection_count:
            warnings.warn("max_connection_count has no effect", DeprecationWarning, stacklevel=2)
        if quiet_timeout:
            warnings.warn("quiet_timeout has no effect", DeprecationWarning, stacklevel=2)
        if poll_interval is not None:
            warnings.warn("poll_interval has no effect", DeprecationWarning, stacklevel=2)
        if max_consequence_depth is not None:
            warnings.warn("max_consequence_depth has no effect", DeprecationWarning, stacklevel=2)
        if package_ids:
            warnings.warn("package_ids has no effect", DeprecationWarning, stacklevel=2)
        if eager_package_fetch is not None or not eager_package_fetch:
            warnings.warn("eager_package_fetch has no effect", DeprecationWarning, stacklevel=2)
        if not use_acs_service:
            warnings.warn(
                "use_acs_service has no effect and cannot be disabled",
                DeprecationWarning,
                stacklevel=2,
            )
        if ca_file:
            self._config["ca_file"] = ca_file
        if cert_file:
            self._config["cert_file"] = cert_file
        if cert_key_file:
            self._config["cert_key_file"] = cert_key_file
        if verify_ssl:
            warnings.warn("verify_ssl has no effect", DeprecationWarning, stacklevel=2)
        if party_groups:
            self._config["read_as"] = party_groups
        if enable_http_proxy is not None:
            self._config["enable_http_proxy"] = enable_http_proxy
        if connect_timeout is not None:
            self._config["connect_timeout"] = connect_timeout

    @property
    def lookup(self) -> "SymbolLookup":
        """
        Return a :class:`SymbolLookup` that provides type and package information for known
        packages. Unlike :class:`Network`, this package database is globally shared and is NOT
        scoped only to this :class:`ConnectionFactory`.

        See the comments in :package:`dazl.protocols.pkgcache` for more information on why this is
        a globally shared database instead of being individually scoped.
        """
        return SHARED_PACKAGE_DATABASE

    def resolved_config(self) -> "NoReturn":
        """
        Reading configuration in this way is no longer supported.
        """
        raise NotSupportedError("resolved_config() is not supported")

    def simple_global(self) -> "NoReturn":
        """
        Thread-blocking implementations are not yet supported in :class:`ConnectionFactory`.
        Support for this method will be added in dazl v7.6.
        """
        raise NotSupportedError("blocking thread connections are not yet supported")

    def aio_global(self) -> "AIOGlobalClient":
        """
        Return a client that can be used to access globally-available information, such as package
        information.

        Unlike :class:`Network`, the returned object does _not_ attempt to reuse a connection from
        an existing party, and instead tries to create an explicit connection as an admin. But like
        :class:`Network`, invoking this function multiple times returns the same client.
        """
        if self._admin_client is None:
            self._admin_client = AIOGlobalClient(connect(**self._config))
        return self._admin_client

    def simple_party(self, party: "Union[str, Party]") -> "NoReturn":
        """
        Thread-blocking implementations are not yet supported in :class:`ConnectionFactory`.
        Support for this method will be added in dazl v7.6.
        """
        raise NotSupportedError("blocking thread connections are not yet supported")

    def simple_new_party(self) -> "NoReturn":
        """
        Thread-blocking implementations are not yet supported in :class:`Network`.
        Support for this method will be added in dazl v7.6.
        """
        raise NotSupportedError("blocking thread connections are not yet supported")

    def aio_party(self, party: "Union[str, Party]") -> "AIOPartyClient":
        """
        Return a party client that works on an asyncio event loop.

        :param party: The party to get a client for.
        """
        client = self._async_clients.get(party)
        if client is not None:
            warnings.warn(
                f"ConnectionFactory.aio_party({party!r}) called more than once",
                ConnectionReuseWarning,
                stacklevel=2,
            )
            return client

        client = AIOPartyClient(connect(act_as=party, **self._config))
        self._async_clients[party] = client
        return client

    def aio_new_party(self) -> "AIOPartyClient":
        """
        Return a :class:`PartyClient` for a random party that works on an asyncio event loop.
        This will never return the same object twice.
        """
        return self.aio_party(str(uuid4()))

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def party_bots(self, party: "Union[str, Party]", if_missing: int = 0) -> "NoReturn":
        """
        Bot introspection is not supported in :class:`ConnectionFactory`.
        """
        warnings.warn(_NS_BOT_INTROSPECTION, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(_NS_BOT_INTROSPECTION)

    # noinspection PyMethodMayBeStatic
    def bots(self) -> "NoReturn":
        """
        Bot introspection is not supported in :class:`ConnectionFactory`.
        """
        warnings.warn(_NS_BOT_INTROSPECTION, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(_NS_BOT_INTROSPECTION)

    # noinspection PyMethodMayBeStatic
    def start(self) -> None:
        """
        This method is not supported, as ``aio_run()`` can be used as an alternative:

        .. code-block:: python
            import asyncio

            # Python 3.6
            asyncio.ensure_future(network.aio_run())

            # Python 3.7 or later
            asyncio.create_task(network.aio_run())
        """
        warnings.warn("start() is not supported; use aio_run() instead")
        raise NotSupportedError()

    def start_in_background(self):
        """
        Thread-blocking implementations are not yet supported in :class:`Network`.
        Support for this method will be added in dazl v7.6.
        """
        raise NotSupportedError(_NS_BLOCKING_CALLS)

    def join(self):
        """
        Thread-blocking implementations are not yet supported in :class:`Network`.
        Support for this method will be added in dazl v7.6.
        """
        raise NotSupportedError(_NS_BLOCKING_CALLS)

    def shutdown(self) -> "asyncio.Future":
        # noinspection PyProtectedMember
        return asyncio.ensure_future(
            asyncio.gather(*(client._stop() for client in self._async_clients.values()))
        )

    async def aio_run(self, *coroutines, keep_open: bool = True) -> None:
        """
        Coroutine that can be used to schedule and run all connections.

        Note: Unlike the v5 Network API, there are no guarantees that parties are synchronized in
        any way! In particular, calling ``network.aio_run(keep_open=False)`` does NOT guarantee that
        all parties have read an active contract set up to the same transaction.

        If a consistent view across parties is required, you must either use the slower, deprecated
        dazl v5 API, or use a multi-party subscription using the new dazl v8 API (which was
        introduced in dazl v7.5).

        :param coroutines:
            Optional additional coroutines to run. ``aio_run`` is only considered complete once all
            of the additional coroutines are also finished.
        :param keep_open:
            ``True`` to use never-ending streams internally; ``False`` in order for all individual
            party clients to read up to their current ACS and quit. Note that this flag does not
            work exactly the same as the dazl v5 API, as it does not guarantee any consistency
            between individual Party streams.
        """
        # noinspection PyProtectedMember
        await asyncio.gather(*(client._open() for client in self._async_clients.values()))
        all_coroutines = [client._run(keep_open) for client in self._async_clients.values()]
        all_coroutines.extend(coroutines)
        await asyncio.gather(*all_coroutines)

    def run_until_complete(
        self, *coroutines: "Awaitable[None]", install_signal_handlers: "Optional[bool]" = None
    ) -> None:
        """
        Block the current thread and run the application in an event loop. The loop terminates when
        the given (optional) coroutines terminate OR :meth:`shutdown` is called.

        Note: Unlike the v5 Network API, there are no guarantees that parties are synchronized in
        any way! Follow-up commands are also not necessarily sent.

        If a consistent view across parties is required, you must either use the slower, deprecated
        dazl v5 API, or use a multi-party subscription using the new dazl v8 API (which was
        introduced in dazl v7.5).

        :param coroutines:
            Optional additional coroutines to run concurrently with dazl reading from Party streams.
        :param install_signal_handlers:
            ``True`` to install SIGINT and SIGQUIT event handlers (CTRL+C and CTRL+\\);
            ``False`` to skip installation. The default value is ``None``, which installs signal
            handlers only when called from the main thread (default). If signal handlers are
            requested to be installed and the thread is NOT the main thread, this method throws.
        """
        run(asyncio.get_event_loop(), self, coroutines, install_signal_handlers, False)

    def run_forever(
        self, *coroutines: "Awaitable[None]", install_signal_handlers: "Optional[bool]" = None
    ) -> None:
        """
        Block the current thread and run the application in an event loop.

        Note: Unlike the v5 Network API, there are no guarantees that parties are synchronized in
        any way!

        If a consistent view across parties is required, you must either use the slower, deprecated
        dazl v5 API, or use a multi-party subscription using the new dazl v8 API (which was
        introduced in dazl v7.5).

        :param coroutines:
            Optional additional coroutines to run concurrently with dazl reading from Party streams.
        :param install_signal_handlers:
            ``True`` to install SIGINT and SIGQUIT event handlers (CTRL+C and CTRL+\\);
            ``False`` to skip installation. The default value is ``None``, which installs signal
            handlers only when called from the main thread (default). If signal handlers are
            requested to be installed and the thread is NOT the main thread, this method throws.
        """
        run(asyncio.get_event_loop(), self, coroutines, install_signal_handlers, True)

    @property
    def bots(self):
        err_str = "introspection of event handlers is not supported in ConnectionFactory"
        warnings.warn(err_str, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(err_str)

    @property
    def party_bots(self):
        err_str = "introspection of event handlers is not supported in ConnectionFactory"
        warnings.warn(err_str, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(err_str)

    def parties(self) -> "AbstractSet[Party]":
        warnings.warn(
            "parties is deprecated and there is no planned replacement",
            DeprecationWarning,
            stacklevel=2,
        )
        return frozenset(self._async_clients.keys())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def run(
    loop: "asyncio.AbstractEventLoop",
    network: "Network",
    coroutines: "Collection[Awaitable[None]]",
    install_signal_handlers: "Optional[bool]" = None,
    keep_open: bool = False,
) -> None:
    if validate_install_signal_handlers(install_signal_handlers):
        loop.add_signal_handler(signal.SIGINT, network.shutdown)
        loop.add_signal_handler(signal.SIGQUIT, network.shutdown)
    loop.run_until_complete(network.aio_run(coroutines, keep_open=keep_open))
