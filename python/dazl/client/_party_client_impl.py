# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import ensure_future, gather, get_event_loop, wait, Future
from concurrent.futures import ALL_COMPLETED

from dataclasses import replace, dataclass, field, fields, asdict
from datetime import datetime, timedelta
from io import StringIO
from typing import Any, Awaitable, Collection, List, Optional, Sequence, Set, Tuple, \
    TypeVar, TYPE_CHECKING
import reprlib
import uuid

from .. import LOG
from .bots import Bot, BotCollection, BotCallback, BotFilter
from .config import NetworkConfig, PartyConfig
from .state import ActiveContractSet
from ._writer_verify import ValidateSerializer
from ..model.core import ContractMatch, ContractsState, ContractId, \
    CommandTimeoutError, ContractContextualData, ContractContextualDataCollection, Party
from ..model.ledger import LedgerMetadata
from ..model.network import connection_settings
from ..model.reading import BaseEvent, TransactionStartEvent, TransactionEndEvent, OffsetEvent, \
    TransactionFilter, ContractCreateEvent, ContractArchiveEvent, \
    InitEvent, ReadyEvent, ActiveContractSetEvent, PackagesAddedEvent
from ..model.writing import CommandBuilder, CommandDefaults, CommandPayload, EventHandlerResponse
from ..protocols import LedgerNetwork, LedgerClient
from ..util.asyncio_util import ServiceQueue, await_then, completed, safe_create_future, \
    named_gather
from ..util.prim_natural import n_things
from ..util.typing import safe_cast

if TYPE_CHECKING:
    from .api import PartyClient
    from ._network_client_impl import _NetworkImpl


T = TypeVar('T')


class _PartyClientImpl:
    def __init__(self, parent: '_NetworkImpl', party: 'Party'):
        self.parent = parent
        self.metrics = parent._metrics
        self.invoker = parent.invoker
        self.party = party

        self._config_values = dict()
        self._config = None  # type: Optional[NetworkConfig]
        self._pool = None  # type: Optional[LedgerNetwork]
        self._pool_fut = None  # type: Optional[Awaitable[LedgerNetwork]]
        self._client_fut = None  # type: Optional[Awaitable[LedgerClient]]
        self._ready_fut = safe_create_future()
        self._known_packages = set()  # type: Set[str]

        self._acs = ActiveContractSet()
        self.bots = BotCollection(party)
        self._reader = _PartyClientReaderState()
        self._writer = _PartyClientWriterState()

    def connect_in(self, pool: 'LedgerNetwork') -> 'Future':
        self._config = config = self.resolved_config()
        settings, url_prefix = connection_settings(
            config.url,
            self.party,
            verify_ssl=config.verify_ssl,
            ca_file=config.ca_file,
            cert_file=config.cert_file,
            cert_key_file=config.cert_key_file)

        self._pool = pool
        self._client_fut = ensure_future(pool.connect(self.party, settings, url_prefix))
        return self._client_fut

    def set_config(self, **kwargs):
        self._config_values.update(kwargs)

    def resolved_config(self) -> 'PartyConfig':
        parent_base_config = asdict(self.parent.resolved_anonymous_config())
        parent_party_config = _find_party_config(self.parent.get_config_raw('parties', ()), self.party) or {}

        config_names = {f.name for f in fields(PartyConfig)}
        all_config = dict()
        all_config.update(parent_base_config)
        all_config.update(parent_party_config)
        all_config.update(self._config_values)
        return PartyConfig(**{k: v for k, v in all_config.items() if k in config_names})

    def initialize(self, current_time: datetime, metadata: LedgerMetadata) -> Awaitable[None]:
        """
        Initialize the state of the ledger.

        :param current_time:
            The ledger time to publish as part of the :class:`InitEvent`.
        :param metadata:
            Information about the connected ledger.
        :return:
        """
        self._acs.metadata_future.set_result(metadata.store)
        evt = InitEvent(self, self.party, current_time, metadata.ledger_id, metadata.store)
        return self.emit_event(evt)

    def ready(self) -> Awaitable[None]:
        return self._ready_fut

    def get_time(self) -> Awaitable[datetime]:
        return await_then(self._pool.ledger(), lambda metadata: metadata.time_model.get_time())

    def set_time(self, new_datetime) -> Awaitable[None]:
        return await_then(self._pool_fut, lambda pool: pool.set_time(new_datetime))

    # region Event Handler Management

    # noinspection PyShadowingBuiltins
    def add_event_handler(
            self, key: str, handler: 'BotCallback', filter: 'Optional[BotFilter]',
            party_client: 'PartyClient') \
            -> 'Bot':
        if party_client is None:
            raise ValueError('a party_client is required here')
        return self.bots.add_single(key, handler, filter, party_client=party_client)

    def emit_event(self, data: BaseEvent) -> 'Awaitable[Any]':
        """
        Emit an event.

        :param data:
            The event to raise.
        :return:
            An Awaitable that is resolved when the commands that resulted from event callbacks
            have been completed either successfully or unsuccessfully.
        """
        return self.bots.notify(data)

    async def emit_ready(self, metadata: LedgerMetadata, time: datetime, offset: str) -> None:
        """
        Emit a ready event specific to this client. This may also emit initial create events and
        initial package added events.

        :param metadata:
            The :class:`LedgerMetadata` at the network level.
        :param time:
            The current time.
        :param offset:
            The ledger offset.
        :return:
            Nothing. This method "returns" when all events have been raised and their follow-ups
            have been processed.
        """
        ready_event = ReadyEvent(self, self.party, time, metadata.ledger_id, metadata.store, offset)
        self._known_packages.update(metadata.store.package_ids())
        await self.emit_event(ready_event)

        pkg_event = PackagesAddedEvent(self, self.party, time, metadata.ledger_id, metadata.store, True)
        await self.emit_event(pkg_event)

    # endregion

    # region Active/Historical Contract Set management

    def find_by_id(self, cid: ContractId) -> ContractContextualData:
        return self._acs.get(cid)

    def find(self,
             template: Any,
             match: ContractMatch = None,
             include_archived: bool = False) \
            -> ContractContextualDataCollection:
        return self._acs.read_full(template, match, include_archived=include_archived)

    def find_active(self, template: Any, match: ContractMatch = None) -> ContractsState:
        return self._acs.read_active(template, match)

    def find_historical(self, template: Any, match: ContractMatch = None) \
            -> ContractContextualDataCollection:
        return self._acs.read_full(template, match, include_archived=True)

    def find_nonempty(self, template: Any, match: ContractMatch, min_count: int = 1,
                      timeout: float = 30):
        return self._acs.read_async(template, match, min_count=min_count)

    # endregion

    # region Read Path

    async def read_acs(self, until_offset: 'Optional[str]', raise_events: bool) \
            -> 'Tuple[str, Future]':
        """
        Initial bootstrap of events from the read side. Only one instance of this coroutine
        should be active at a time per client. An initial block of events is read using the
        Active Contract Set service, and the transaction stream is then subscribed to in order to
        ensure that this client is caught up to the specified offset.

        :param until_offset:
            The destination ledger offset to read up until to. If not included, then the client
            attempts to read as many transactions as is currently available.
        :param raise_events:
            ``True`` to raise transaction- and contract-related events to event handlers;
            ``False`` to suppress this behavior and only update local state within the client
            (offset information and active contract set).
        :return:
            The ledger offset that the reader ended at and a Future that is resolved when all event
            handlers' follow-ups have either successfully or unsuccessfully completed.
        """
        LOG.info('Calling read_acs(%r, %r)', until_offset, raise_events)
        client = await self._client_fut
        acs = await client.active_contracts()
        for acs_evt in acs:
            await self._process_transaction_stream_event(acs_evt, False)

        return await self.read_transactions(until_offset, raise_events)

    async def read_transactions(self, until_offset: 'Optional[str]', raise_events: bool) \
            -> 'Tuple[str, Future]':
        """
        Main processing method of events from the read side. Only one instance of this coroutine
        should be active at a time per client.

        :param until_offset:
            The destination ledger offset to read up until to. If not included, then the client
            attempts to read as many transactions as is currently available.
        :param raise_events:
            ``True`` to raise transaction- and contract-related events to event handlers;
            ``False`` to suppress this behavior and only update local state within the client
            (offset information and active contract set).
        :return:
            The ledger offset that the reader ended at and a Future that is resolved when all event
            handlers' follow-ups have either successfully or unsuccessfully completed.
        """
        LOG.verbose('  read_transactions(%s, %s) with party %s | (groups %s), reader offset %s',
                    until_offset, raise_events, self.party, self._config.party_groups,
                    self._reader.offset)
        client = await self._client_fut
        metadata = await self._pool.ledger()

        event_count = 0
        futs = []

        while (until_offset is None or
               self._reader.offset is None or
               self._reader.offset != until_offset):
            LOG.verbose('  read_transactions(%s, %s) with party %s | current offset: %s; '
                        'destination offset: %s',
                        until_offset, raise_events, self.party, self._reader.offset, until_offset)

            # TODO: Find a more appropriate place to raise these events (or change the name of this
            #  method to make it clearer that it has a bigger mandate than simply transaction
            #  events)
            all_packages = set(metadata.store.package_ids())
            new_package_ids = all_packages - self._known_packages
            if new_package_ids:
                pkg_event = PackagesAddedEvent(
                    self, self.party, None, metadata.ledger_id, metadata.store, False)
                self._known_packages.update(all_packages)
                await self.emit_event(pkg_event)

            # prepare a call to /events
            transaction_filter = TransactionFilter(
                ledger_id=metadata.ledger_id,
                current_offset=self._reader.offset,
                destination_offset=until_offset,
                templates=None,
                max_blocks=None,
                party_groups=self._config.party_groups)

            transaction_events = await client.events(transaction_filter)
            for event in transaction_events:
                futs.append(self._process_transaction_stream_event(event, raise_events))
            event_count += len(transaction_events)

            # if a destination offset is not specified, then only read one pass of transaction
            # events before exiting
            if until_offset is None:
                break

        self.metrics.party_offset(self.party, self._reader.offset)
        LOG.verbose('  read_transactions(%s, %s) with party %s | reader offset %s',
                    until_offset, raise_events, self.party, self._reader.offset)
        futs = [fut for fut in futs if not fut.done()]
        if len(futs) == 0:
            return self._reader.offset, completed(None)
        elif len(futs) == 1:
            return self._reader.offset, futs[0]
        else:
            return self._reader.offset, gather(*futs, return_exceptions=True)

    async def read_end(self) -> str:
        client = await self._client_fut
        return await client.events_end()

    def _process_transaction_stream_event(self, event: Any, raise_events: bool) -> Future:
        """

        :param event:
        :param raise_events:
        """
        if isinstance(event, TransactionStartEvent):
            # Update the ACS before sharing this information with interested parties
            LOG.info('Processing transaction: %s, %s, %s', event.offset, event.workflow_id, event.command_id)
            for contract_event in event.contract_events:
                if isinstance(contract_event, ContractCreateEvent):
                    self._acs.handle_create(contract_event)
                elif isinstance(contract_event, ContractArchiveEvent):
                    self._acs.handle_archive(contract_event)

        elif isinstance(event, TransactionEndEvent):
            # Notify anything waiting on commands to complete that some of them will have
            # completed as a consequence of this transaction.
            for cmd in self._writer.inflight_commands:
                cmd.notify_read_done(event.command_id, event.time)

            LOG.debug('evt recv: party %s, BIM %r (%s events)',
                      self.party, event.command_id[0:7], len(event.contract_events))

        elif isinstance(event, ActiveContractSetEvent):
            for contract_event in event.contract_events:
                self._acs.handle_create(contract_event)

        if raise_events:
            fut = self.emit_event(event)
        else:
            fut = completed(None)

        if isinstance(event, OffsetEvent):
            self._reader.offset = event.offset

        return fut

    # endregion

    # region Write path

    def write_commands(
            self,
            commands: EventHandlerResponse,
            ignore_errors: bool = False,
            workflow_id: 'Optional[str]' = None) \
            -> Awaitable[None]:
        """
        Submit a command or list of commands.

        :param commands:
            The commands to send to the server.
        :param ignore_errors:
            Whether errors should be ignored for purposes of terminating the client. If ``True``,
            then a failure to send this command does not necessarily end the client.
        :param workflow_id:
            The workflow ID to use to tag submitted commands.
        :return:
            An ``asyncio.Future`` that is resolved right before the corresponding side effects have
            hit the event stream for this party. Synchronous errors are reported back immediately
            and not failed through this mechanism.
        """
        if workflow_id is None:
            workflow_id = uuid.uuid4().hex
        cb = CommandBuilder.coerce(commands, atomic_default=True)
        cb.defaults(workflow_id=workflow_id)

        p = _PendingCommand(cb)
        p.future.add_done_callback(lambda _: self._process_command_finished(p, ignore_errors))
        self._writer.pending_commands.put(p)
        LOG.debug('write_commands(%s)', p)
        return p.future

    def _process_command_finished(self, pending_command, ignore_errors):
        try:
            if pending_command.future.exception() is None:
                LOG.debug('Command finished: %s', pending_command)
            self._writer.inflight_commands.remove(pending_command)
        except ValueError:
            LOG.warning('Tried to remove %s even though it was already removed.', pending_command)

        if pending_command.future.exception() is not None:
            # TODO: more with this; maybe let the user respond to this
            LOG.exception('A command submission failed!',
                          exc_info=pending_command.future.exception())

    async def main_writer(self):
        """
        Main coroutine for submitting commands.
        """
        LOG.info('Writer loop for party %s is starting...', self.party)
        ledger_fut = ensure_future(self._pool.ledger())

        client = self._client_fut.result()  # type: LedgerClient
        metadata = ledger_fut.result()  # type: LedgerMetadata
        validator = ValidateSerializer(metadata.store)

        self._writer.pending_commands.start()

        # Asynchronously iterate over all pending commands that a user has (or will) send.
        # This asynchronous loop "blocks" when pending_commands is empty and is "woken up"
        # immediately when new data is added to it. The loop terminates when the pending_commands
        # ServiceQueue is stopped.
        async for p in self._writer.pending_commands:
            LOG.debug('Sending a command: %s', p)
            ledger_effective_time = metadata.time_model.get_time()
            command_payloads = []  # type: List[Tuple[_PendingCommand, Sequence[CommandPayload]]]

            self._writer.inflight_commands.append(p)
            try:
                defaults = CommandDefaults(
                    default_party=self.party,
                    default_ledger_id=metadata.ledger_id,
                    default_workflow_id=None,
                    default_application_id=self._config.application_name,
                    default_command_id=None,
                    default_ttl=timedelta(seconds=30))
                cps = p.command.build(defaults, ledger_effective_time)
                if cps:
                    commands = [replace(cp, commands=validator.serialize_commands(cp.commands))
                                for cp in cps]  # type: Sequence[CommandPayload]
                    command_payloads.append((p, commands))
                    await submit_command_async(client, p, commands)
                else:
                    # This is a "null command"; don't even bother sending to the server. Immediately
                    # resolve the future successfully and discard
                    p.future.set_result(None)
            except Exception as ex:
                LOG.exception("Tried to send a command and failed!")
                p.notify_read_fail(ex)

        LOG.info('Writer loop for party %s is winding down.', self.party)

        # After the pending command list is fully empty (and never to be filled again), wait for
        # all outstanding commands.
        done, pending = await wait([pc.future for pc in self._writer.inflight_commands],
                                   timeout=5, return_when=ALL_COMPLETED)

        if pending:
            LOG.warning('Writer loop for party %s has NOT fully finished, '
                        'but will be terminated anyway (%d futures still pending).',
                        self.party, len(pending))
        else:
            LOG.info('Writer loop for party %s is finished.', self.party)

    def writer_idle(self):
        return not bool(self._writer.pending_commands) and not self._writer.inflight_commands

    def stop_writer(self):
        """
        Prohibit future command submissions from being accepted.
        """
        self._writer.pending_commands.stop()

    # endregion


@dataclass
class _PartyClientReaderState:
    offset: Optional[str] = field(default=None)


@dataclass
class _PartyClientWriterState:
    pending_commands: 'ServiceQueue[_PendingCommand]' = field(default_factory=ServiceQueue)
    inflight_commands: 'List[_PendingCommand]' = field(default_factory=list)


class _PendingCommand:
    """
    Track the status of a set of commands in-flight.
    """

    __slots__ = ('command', 'command_ids', 'max_record_time', 'future')

    def __init__(self, command: CommandBuilder):
        self.command = safe_cast(CommandBuilder, command)
        self.command_ids = None  # type: Optional[Set[str]]
        self.max_record_time = None  # type: Optional[datetime]
        self.future = get_event_loop().create_future()

    def notify_write(self, command_ids: Collection[str], max_record_time: datetime):
        if self.max_record_time is not None:
            raise Exception('cannot send an already in-progress command')
        self.command_ids = set(command_ids)
        self.max_record_time = max_record_time

    def notify_read_done(self, command_id: str, ledger_time: Optional[datetime]):
        """
        Trigger an appropriate response given the receipt of a transaction.
        """
        if self.command_ids is not None:
            if command_id not in self.command_ids:
                return

            self.command_ids.discard(command_id)
            if not self.command_ids:
                # the command is finished
                self.future.set_result(None)
                return

        if self.max_record_time is not None and ledger_time is not None and \
                self.max_record_time < ledger_time:
            self.future.set_exception(CommandTimeoutError())

    def notify_read_fail(self, ex: Exception):
        self.future.set_exception(ex)

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return id(self)

    def __repr__(self):
        with StringIO() as buf:
            buf.write('<_PendingCommand(command=')
            buf.write(format(self.command, 'c'))
            if self.command_ids is not None:
                buf.write(', command_ids=')
                buf.write(format(self.command_ids))
            if self.max_record_time is not None:
                buf.write(', max_record_time="')
                buf.write(format(self.max_record_time.isoformat()))
                buf.write('"')
            buf.write(', future=')
            buf.write(format(self.future))
            buf.write('>')
            return buf.getvalue()


def submit_command_async(
        client: LedgerClient, p: '_PendingCommand', commands: Sequence[CommandPayload]) \
        -> Awaitable[None]:
    """
    Submit a command asynchronously.

    The returned future is resolved when all commands have successfully completed their network
    operations, but not necessarily when the ledger has committed the results of that command to the
    ledger.

    :param client:
    :param p:
    :param commands:
    :return:
    """
    coros = []
    command_ids = []
    maximum_record_time = commands[0].maximum_record_time

    for payload in commands:
        coro = None
        command_ids.append(payload.command_id)
        try:
            coro = ensure_future(client.commands(payload))

            LOG.info('cmd submit: party %s, workflow_id %r, command_id %r, %s: %r',
                     payload.party, payload.workflow_id[0:7], payload.command_id[0:7],
                     n_things(len(payload.commands), 'commands'), reprlib.repr(payload.commands))
        except Exception as ex:
            # TODO: consider what to do in this case
            p.notify_read_fail(ex)

        if coro is not None:
            coros.append(coro)

    p.notify_write(command_ids, maximum_record_time)
    if len(coros) == 0:
        return completed(None)
    elif len(coros) == 1:
        return coros[0]
    else:
        return named_gather('SubmitCommandAsync()', *coros, return_exceptions=True)


def _find_party_config(party_configs: 'Collection[dict]', party: Party) -> 'Optional[dict]':
    """
    Look within a config dictionary (as specified by FlatConfig) for a configuration object that is
    specific to this party.
    """
    if party_configs is not None:
        for party_config in party_configs:
            local_party = party_config.get('party')
            if local_party == party:
                return party_config
    return None
