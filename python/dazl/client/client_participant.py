# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains classes and methods for interacting with a participant node.
"""
import warnings
from datetime import datetime
from functools import wraps
from typing import Any, Awaitable, Callable, Optional, Tuple, Union

from ._party_client_impl import _PartyClientImpl
from ..model.core import ContractId, ContractData, ContractMatch, ContractsHistoricalState, \
    ContractsState, Party
from ..model.reading import EventKey, ContractCreateEvent
from ..model.types_store import PackageStore
from ..util.asyncio_util import await_then


class ParticipantLedgerClient:
    """
    This class is deprecated and will be removed in version 6.0.0. Prefer :class:`AIOPartyClient`
    if you want to use ``asyncio`` or :class:`SimplePartyClient` if you want to use a blocking model
    instead.
    """
    def __init__(self, party_impl: _PartyClientImpl):
        warnings.warn('ParticipantLedgerClient will be removed in version 6.0.0. Please switch to '
                      'AIOPartyClient (if you wish to continue to use asyncio) or '
                      'SimplePartyClient (if you wish to use a blocking model instead),',
                      DeprecationWarning)
        self._impl = party_impl

    @property
    def party(self) -> Party:
        return self._impl.party

    @property
    def party_name(self) -> Party:
        warnings.warn('`party_name` is a deprecated property name. Please us `party` instead.`',
                      DeprecationWarning)
        return self._impl.party

    def set_config(self, **kwargs):
        return self._impl.set_config(**kwargs)

    # region Read Methods (ACS)

    def find_one(self, template, match):
        return self.select_first(template, match)

    def find(self, *args, **kwargs):
        return self._impl.find(*args, **kwargs)

    def find_active(self, *args, **kwargs):
        return self._impl.find_active(*args, **kwargs)

    def find_historical(self, *args, **kwargs):
        return self._impl.find_historical(*args, **kwargs)

    def find_nonempty(self, *args, **kwargs):
        return self._impl.find_nonempty(*args, **kwargs)

    def select(self, template_name: str, match: ContractMatch = None, include_archived=False) \
            -> Union[ContractsState, ContractsHistoricalState]:
        """
        Immediately return data from the current active contract set.

        The contents of this ACS are guaranteed to be present (or removed) in the current
        transaction _before_ processing any corresponding ``on_created`` or ``on_archived``
        callbacks for this party. The ACS is populated _before_ processing any ``on_ready``
        callbacks.

        This method raises an error if ACS tracking has been disabled on this client.

        :param template_name:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :param include_archived:
            ``True`` to include values that have been archived. When this is set, the returned
            dictionary's values is a tuple of contract data and the active state (either ``True`` or
            ``False``).
        :return:
            A ``dict`` whose keys are :class:`ContractId` and values are corresponding contract
            data that match the current query.
        """
        if include_archived:
            return self._impl.find_historical(template_name, match)
        else:
            return self._impl.find_active(template_name, match)

    def select_first(self, template_name: str, match: ContractMatch = None) \
            -> Awaitable[Tuple[ContractId, ContractData]]:
        """
        Convenience method that returns the first occurrence of a matching contract.
        """
        def extract_state(contracts):
            return next(iter(contracts.items()))
        return await_then(self._impl.find_nonempty(template_name, match), extract_state)

    def select_nonempty(self, template_name: str, match: ContractMatch = None, min_count: int = 1) \
            -> Awaitable[ContractsState]:
        """
        Return data from the current active contract set when at least some amount of rows exist in
        the active contract set.

        :param template_name:
            The name of the template to fetch data from.
        :param match:
            An optional dictionary whose keys are matched against corresponding field values.
        :param min_count:
            The minimum number of rows to return. The default value is 1.
        :return:
            A ``Future`` that is resolved with a ``dict`` whose keys are :class:`ContractId` and
            values are corresponding contract data that match the current query.
        """
        return self._impl.find_nonempty(template_name, match, min_count=min_count)

    # endregion

    # region Write Methods

    def submit(self, commands, ignore_errors=False, workflow_id=None):
        """
        Submit the set of commands for processing.

        :param commands:
            A single command or a list of commands.
        :param ignore_errors:
            ``True`` if failure to submit a command should not prevent termination of the program.
        :return:
            A future that resolves when the commands have made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        return self._impl.write_commands(commands, ignore_errors, workflow_id=workflow_id)

    def submit_create(self, template_name: str, arguments: Optional[dict] = None, workflow_id=None):
        """
        Submit a single create command. Equivalent to calling :meth:`submit` with a single
        ``create``.

        :param template_name:
            The name of the template.
        :param arguments:
            The arguments to the create (as a ``dict``).
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        from .. import create
        return self.submit(create(template_name, arguments), workflow_id=workflow_id)

    def submit_exercise(self, cid: ContractId, choice_name: str, arguments: Optional[dict] = None, workflow_id=None):
        """
        Submit a single exercise choice. Equivalent to calling :meth:`submit` with a single
        ``exercise``.

        :param cid:
            The :class:`ContractId` on which a choice is being exercised.
        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            The arguments to the create (as a ``dict``). Can be omitted (``None``) for no-argument
            choices.
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        from .. import exercise
        return self.submit(exercise(cid, choice_name, arguments), workflow_id=workflow_id)

    # endregion

    # region Other Methods

    async def get_time(self) -> datetime:
        """
        Return the current time on the remote server. Also advances the local notion of time if
        required.
        """
        return await self._impl.get_time()

    def set_time(self, new_datetime: datetime) -> Awaitable[None]:
        """
        Set the current time on the ledger. This is only supported if the ledger supports time
        manipulation.
        """
        return self._impl.set_time(new_datetime)

    # endregion

    # region Event Handlers

    def ready(self) -> Awaitable[None]:
        """
        An Awaitable signaled once the ledger client has caught up to the current head and is
        ready to send commands.
        """
        return self._impl.ready()

    # noinspection PyShadowingBuiltins
    def add_event_handler(self, event_key, event_handler, filter=None) -> None:
        """
        Register an event handler.
        """
        self._impl.add_event_handler(event_key, event_handler, filter, self)

    def on_init(self, callback: 'Callable[[], Any]') -> None:
        """
        Called once the ledger client has been instructed to begin, but before any network activity
        is started.
        """
        # Historically on_init callbacks took no parameters
        for key in EventKey.init():
            self.add_event_handler(key, lambda _: callback())

    def on_init_metadata(self, callback: 'Callable[[PackageStore], Any]') -> None:
        """
        Called once metadata has been discovered.
        """
        # Historically on_init_metadata callbacks took a single parameter that is the metadata of
        # the ledger, and additionally was treated as a separate event from init.
        for key in EventKey.init():
            self.add_event_handler(key, lambda evt: callback(evt.package_store))

    def on_ready(self, callback: 'Callable[[str, ParticipantLedgerClient], Any]') -> None:
        """
        Called once the ledger client has caught up to the current head and is ready to send
        commands, or called immediately if the client is already ready.

        :param callback:
            Callback that takes two arguments (party name and the instance of this client). If this
            callback returns follow-up commands, they are submitted.
        """
        for key in EventKey.ready():
            self.add_event_handler(key, lambda evt: callback(evt.party, evt.client))

    def on_event(self, event_kind, callback, optional=False) -> None:
        """
        No longer supported.
        """
        raise RuntimeError(
            'generic event listeners are no longer supported. '
            'Please register for specific events instead')

    # noinspection PyUnusedLocal
    def on_created(self, template, match=None, callback=None, optional=False) -> None:
        """
        Called whenever a contract of the specified template is created.

        :param template:
            A template name to subscribe to, or '*' to subscribe on all templates.
        :param match:
            An (optional) parameter that filters the templates to be received by the callback.
        :param callback:
            The callback to invoke whenever a matching template is created.
        :param optional:
            This parameter is no longer used.
        """
        if match is not None and callback is None:
            callback = match
            match = None

        @wraps(callback)
        def implementation(event: ContractCreateEvent):
            return callback(event.cid, event.cdata)

        if match is not None:
            @wraps(match)
            def match_impl(event: ContractCreateEvent):
                return match(event.cid, event.cdata)
        else:
            match_impl = None

        for key in EventKey.contract_created(True, template):
            self.add_event_handler(key, implementation, filter=match_impl)

    # noinspection PyUnusedLocal
    def on_archived(self, template, callback, optional=False) -> None:
        """
        Called whenever a contract of the specified template is archived.
        """
        for key in EventKey.contract_archived(True, template):
            self.add_event_handler(key, lambda evt: callback(evt.cid, evt.cdata))

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def on_done(self, callback):
        """
        Add a listener that gets called when this :class:`ParticipantLedgerClient` is terminated.
        """
        warnings.warn('The done event is no longer raised and does nothing.', DeprecationWarning)

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def on_error(self, callback):
        """
        Called on any error from the ledger.
        """
        warnings.warn('The error event is no longer raised and does nothing.', DeprecationWarning)

    # endregion

    def __repr__(self):
        return f'<ParticipantLedgerClient(party_name={self.party}>)'
