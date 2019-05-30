# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains classes and methods for managing a collection of clients.
"""

from asyncio import get_event_loop
from datetime import datetime
from functools import wraps
from typing import Collection, Union

from dataclasses import asdict

from .client_participant import ParticipantLedgerClient
from .config import get_config, parse_kwargs, validate_config, NetworkConfig
from ._base_model import ExitCode, LedgerRun
from ._run_level import RunState
from ._network_client_impl import _NetworkImpl
from ..model.core import RunLevel, Party
from ..model.reading import InitEvent
from ..plugins.plugins_base import Plugin
from ..util.prim_types import PrimitiveTypeConverter


def create_client(*config, **kwargs):
    """
    Create a :class:`LedgerClientManager` for the configuration settings.

    :param config:
        Instances of :class:`LedgerConfiguration`` objects to merge together.
    :param kwargs:
        Configuration options that are accepted either at the global level or at the party level.
    :return:
        An instance of :class:`LedgerClientManager`.
    """
    cfg = parse_kwargs(*config, **kwargs)
    return LedgerClientManager(cfg)


class LedgerClientManager:
    """
    Keep-alive manager for open client instances. This is the primary entry point for interacting
    with the Ledger.
    """

    @classmethod
    def for_args(cls, args):
        return cls(get_config(args))

    def __init__(self, config: 'NetworkConfig'):
        # import warnings
        # warnings.warn('LedgerClientManager will be removed in version 6.0.0. Please switch to '
        #               'LedgerNetwork for managing instances of clients for parties that are '
        #               'connected to the ledger.', DeprecationWarning)
        self._config = validate_config(config)
        self._primitive_type_converter = PrimitiveTypeConverter()
        self._impl = _NetworkImpl()

        for party_config in config.parties:
            self.new_client(**asdict(party_config))

    def __enter__(self):
        """
        Attempt to initialize the committer node. Otherwise do nothing.
        """
        return self

    def __exit__(self, typ, value, traceback):
        """
        Attempt to stop the client manager and all connected clients.
        """

    def register(self, plugin, keep_alive=True):
        """
        Register a plugin with the client.

        If the plugin implements Plugin, then its methods are called as documented. Otherwise, the
        plugin is immediately called with this :class:`LedgerClientManager` as its only argument.
        It should take this opportunity to register event handlers as required to do its work.

        Additionally, if an ``asyncio.Future`` or a coroutine is returned, it is expected to
        indicate the lifetime of the extension:

          - If the future is resolved successfully, the extension is expected to no longer
            interact with the ledger, nor does it require any more "time" to run. If ``keep_alive``
            is ``True``, this pending ``Future`` will additionally prevent the ledger client from
            completing.

          - If the future is resolved with a failure, the entire application is considered to be in
            an error state, and the client is shut down as quickly as is reasonably possible.
        """
        if plugin is not None:
            if isinstance(plugin, Plugin):
                plugin.install(self)
            else:
                raise ValueError('must be a Plugin')

    def stop(self) -> None:
        """
        Wait for all managed clients to finish any outstanding work, and then stops them.
        """
        self._impl.shutdown()

    def terminate(self) -> None:
        """
        Fairly rudely kill the application.
        """
        import sys
        self._impl.abort()
        sys.exit(3)

    def client(self, party_name: Union[str, Party]) -> ParticipantLedgerClient:
        """
        Return an existing client for a party. If none does not exist, :class:`KeyError` is thrown.
        """
        client = self._impl.party_impl(party_name, ParticipantLedgerClient)
        if client is None:
            raise KeyError(party_name)
        return client

    def new_client(self, party: Union[str, Party], **config) -> 'ParticipantLedgerClient':
        """
        Create a new client for the specified party, or if one already exists, augment the provided
        configuration parameters to the existing client.

        :param party: The party.
        :param config: Key-value pairs that represent configuration parameters.
        :return: An instance of :class:`LedgerClientManager`.
        """
        client = self._impl.party_impl(party, ParticipantLedgerClient)
        client.set_config(**config)
        return client

    def _handle_client_init_metadata(self, metadata):
        # TODO: This needs to be thought through more carefully; each cilent fetches its own
        # metadata and this just gets run when the "first" one gets its metadata. Should we wait
        # until all readers have heard their metadata, and then compare? We already block pending
        # writes until all clients are signaled...
        local_init_metadata_callbacks = self._init_metadata_callbacks[:]
        self._init_metadata_callbacks = []
        for init_metadata_callback in local_init_metadata_callbacks:
            init_metadata_callback(metadata)

    def _handle_client_error(self, error):
        for err_callback in self._error_callbacks:
            err_callback(error)

    async def get_time(self) -> datetime:
        return await self._impl.get_time()

    async def set_time(self, new_datetime):
        return await self._impl.set_time(new_datetime)

    def on_init(self, callback):
        # TODO: Probably need to rewrite this event
        self._impl.add_event_handler('init', callback, self)

    def on_init_metadata(self, callback):
        @wraps(callback)
        def rewrite(event: InitEvent) -> None:
            callback(event.package_store)
        self._impl.add_event_handler('init', rewrite, self)

    def on_done(self, callback):
        # TODO: Add deprecation warning
        pass

    def on_error(self, callback):
        # TODO: Add deprecation warning
        pass

    def run_until_complete(self, *futures) -> LedgerRun:
        """
        Start all clients, and terminate the event loop once work is done. This is primarily meant
        to be used when writing a script that is intended to do a specific thing and terminate (such
        as initialization scripts, run a test, or perform some specific action), as opposed to a
        long-lived application that continually acts on contracts that appear on the ledger.

        Specifically, the following is done:

        * First, submit all commands that have been queued up, either by prior calls to
          :meth:`ParticipantLedgerClient.submit` or as commands returned via an
          :meth:`ParticipantLedgerClient.on_ready`
        * Wait for those commands to have been fully acted on by the ledger (either success or
          failure). In the case of success, commands will typically cause contract created or
          contract archived events.
        * If there are callbacks registered to handle those events, they can, in turn, also produce
          commands to be sent to the ledger as well. If so, additionally wait for those commands to
          be completed as well.
        * Once there are no more commands awaiting completion, stop the client.

        If you need to control the event loop yourself, call the :meth:`main` coroutine method
        instead.
        """
        loop = get_event_loop()
        return loop.run_until_complete(self.main(False, *futures))

    def run_forever(self) -> LedgerRun:
        """
        Start all clients. Run until the process is sent a SIGINT signal or CTRL-C is pressed on
        the keyboard. This is primarily meant to be used when writing a long-lived application that
        continually acts on contracts that appear on the ledger, as opposed to a script that is
        intended to do a specific thing and terminate (such as initialization scripts, run a test,
        or perform some specific action).

        If you need to control the event loop yourself, call the :meth:`main` coroutine instead.
        """
        loop = get_event_loop()
        return loop.run_until_complete(self.main(True))

    def parties(self) -> Collection[Party]:
        """
        Return a snapshot of the set of parties that exist right now.
        """
        return self._impl.parties()

    ################################################################################################
    # CORE COROUTINES

    async def main(self, keep_alive: bool = True, *futures) -> LedgerRun:
        """
        The main coroutine that originates all client activity. This method can be used as an
        alternative to starting and stopping the client through ``run_until_complete`` and/or
        ``run_forever``.

        :param keep_alive:
            If ``True``, keep the coroutine running until :meth:`stop` is explicitly called;
            otherwise ``False`` to end the coroutine when all commands and their follow-ups have
            been processed.
        """
        run_state = RunState(RunLevel.RUN_FOREVER if keep_alive else RunLevel.RUN_UNTIL_IDLE)
        await self._impl.aio_run(*futures, run_state=run_state)
        return LedgerRun(
            exit_code=ExitCode.SUCCESS,
            block_start_height=None,
            block_end_height=None)

