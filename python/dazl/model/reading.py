# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains models used on the read-side of the Ledger API.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Collection, Optional, TypeVar, Union

from .core import ContractId, ContractData, ContractContextualData, Party
from .lookup import template_reverse_globs, validate_template
from .types import Type, TypeReference
from .types_store import PackageStore
from ..util.typing import safe_cast, safe_optional_cast


T = TypeVar('T')


class BaseEvent:
    """
    Superclass of all dazl events.
    """
    def __init__(self, client, party, time, ledger_id, package_store):
        self.client = client
        self.party = safe_cast(str, party) if party is not None else None  # type: Optional[Party]
        self.time = safe_optional_cast(datetime, time)
        self.ledger_id = safe_cast(str, ledger_id)
        self.package_store = safe_cast(PackageStore, package_store)

    def acs_find_active(self, template: Union[TypeReference, str], match=None):
        return self.client.find_active(template, match)

    def acs_find_by_id(self, cid: Union[str, ContractId]) -> Optional[ContractContextualData]:
        return self.client.find_by_id(cid)

    def acs_find_one(self, template: Union[TypeReference, str], match=None):
        return self.client.find_one(template, match=match)

    def acs_find_historical(self, template: Union[TypeReference, str], match=None):
        return self.client.find_historical(template, match)

    def acs_find_nonempty(self, template: Union[TypeReference, str], match=None):
        return self.client.find_nonempty(template, match=match)

    def __repr__(self):
        fields = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items()
                           if not k.startswith('_') and k != 'client' and k != 'package_store' and
                           k != 'ledger_id')
        return f'{self.__class__.__name__}({fields})'


class InitEvent(BaseEvent):
    """
    Event raised when dazl is initialized, but before it has begun reading from the Active Contract
    Set (ACS).
    """


class OffsetEvent(BaseEvent):
    """
    Event raised when dazl is ready to begin processing new events. At this point, the Active
    Contract Set (ACS) is populated with the current state of the ledger.
    """
    def __init__(self, client, party, time, ledger_id, package_store, offset):
        super().__init__(client, party, time, ledger_id, package_store)
        self.offset = safe_cast(str, offset)


class ReadyEvent(OffsetEvent):
    """
    Event raised when dazl is ready to begin processing new events. At this point, the Active
    Contract Set (ACS) is populated with the current state of the ledger.
    """


class BaseTransactionEvent(OffsetEvent):
    """
    Event raised when dazl encounters a new transaction. This is raised before any corresponding
    :class:`ContractCreateEvent` or :class:`ContractArchiveEvent`.
    """
    def __init__(self, client, party, time, ledger_id, package_store, offset, command_id,
                 workflow_id):
        super().__init__(client, party, time, ledger_id, package_store, offset)
        self.command_id = safe_cast(str, command_id)
        self.workflow_id = safe_cast(str, workflow_id)


class TransactionStartEvent(BaseTransactionEvent):
    """
    Event raised when dazl encounters a new transaction. This is raised before any corresponding
    :class:`ContractCreateEvent` or :class:`ContractArchiveEvent`.
    """
    def __init__(self, client, party, time, ledger_id, package_store, offset, command_id,
                 workflow_id, contract_events):
        super().__init__(client, party, time, ledger_id, package_store, offset, command_id,
                         workflow_id)
        self.contract_events = contract_events


class TransactionEndEvent(BaseTransactionEvent):
    """
    Event raised when dazl encounters the end of a transaction. This is raised after any
    corresponding :class:`ContractCreateEvent` or :class:`ContractArchiveEvent`.
    """
    def __init__(self, client, party, time, ledger_id, package_store, offset, command_id,
                 workflow_id, contract_events):
        super().__init__(client, party, time, ledger_id, package_store, offset, command_id,
                         workflow_id)
        self.contract_events = contract_events


class ContractEvent(BaseTransactionEvent):
    """
    Event raised when dazl automation detects a new create or an archive. The Active Contract Set
    (ACS) reflects this event, as well as all other events that occurred in the same transaction.
    """
    def __init__(self, client, party, time, ledger_id, package_store, offset, cid, cdata,
                 command_id, workflow_id, event_id, witness_parties):
        super().__init__(client, party, time, ledger_id, package_store, offset, command_id,
                         workflow_id)
        self.cid = safe_cast(ContractId, cid)
        self.cdata = cdata  # type: ContractData
        self.command_id = command_id
        self.workflow_id = workflow_id
        self.event_id = event_id
        self.witness_parties = witness_parties


class ContractCreateEvent(ContractEvent):
    """
    Event raised when dazl automation detects a contract create. The Active Contract Set
    (ACS) reflects this event, as well as all other events that occurred in the same transaction.
    """


class ContractExercisedEvent(ContractEvent):
    """
    Event raised when dazl automation detects a contract exercised.
    """
    def __init__(self, client, party, time, ledger_id, package_store, offset, cid, cdata,
                 command_id, workflow_id, event_id, witness_parties, contract_creating_event_id,
                 choice, choice_args, acting_parties, consuming, child_event_ids):
        super().__init__(client, party, time, ledger_id, package_store, offset, cid, cdata,
                         command_id, workflow_id, event_id, witness_parties)
        self.contract_creating_event_id = contract_creating_event_id
        self.choice = choice
        self.choice_args = choice_args
        self.acting_parties = acting_parties
        self.consuming = consuming
        self.child_event_ids = child_event_ids


class ContractArchiveEvent(ContractEvent):
    """
    Event raised when dazl automation detects a contract archive. The Active Contract Set
    (ACS) reflects this event, as well as all other events that occurred in the same transaction.
    """


def create_dispatch(
        on_init: Callable[[InitEvent], T],
        on_ready: Callable[[ReadyEvent], T],
        on_offset: Callable[[OffsetEvent], T],
        on_transaction_start: Callable[[TransactionStartEvent], T],
        on_transaction_end: Callable[[TransactionEndEvent], T],
        on_contract_created: Callable[[ContractCreateEvent], T],
        on_contract_exercised: Callable[[ContractExercisedEvent], T],
        on_contract_archived: Callable[[ContractArchiveEvent], T]) -> Callable[[BaseEvent], T]:
    def handle(event: BaseEvent) -> T:
        if isinstance(event, ContractCreateEvent):
            return on_contract_created(event)
        elif isinstance(event, ContractExercisedEvent):
            return on_contract_exercised(event)
        elif isinstance(event, ContractArchiveEvent):
            return on_contract_archived(event)
        elif isinstance(event, TransactionStartEvent):
            return on_transaction_start(event)
        elif isinstance(event, TransactionEndEvent):
            return on_transaction_end(event)
        elif isinstance(event, ReadyEvent):
            return on_ready(event)
        elif isinstance(event, InitEvent):
            return on_init(event)
        elif isinstance(event, OffsetEvent):
            return on_offset(event)
        else:
            raise ValueError(f'unknown subclass of BaseEvent: {event!r}')

    return handle


@dataclass(frozen=True)
class TransactionFilter:
    ledger_id: str
    current_offset: Optional[str]
    destination_offset: Optional[str]
    templates: Optional[Collection[Type]]
    max_blocks: Optional[int]
    party_groups: Optional[Collection[str]]


class EventKey:

    from_event = create_dispatch(
        on_init=lambda _: EventKey.init(),
        on_ready=lambda _: EventKey.ready(),
        on_offset=lambda _: EventKey.offset(),
        on_transaction_start=lambda _: EventKey.transaction_start(),
        on_transaction_end=lambda _: EventKey.transaction_end(),
        on_contract_created=lambda event: EventKey.contract_created(False, event.cid.template_id),
        on_contract_exercised=lambda event: EventKey.contract_exercised(
            False, event.cid.template_id, event.choice),
        on_contract_archived=lambda event: EventKey.contract_archived(False, event.cid.template_id))

    @staticmethod
    def init() -> Collection[str]:
        """
        Return the names of events that get raised in response to an :class:`InitEvent`. This is
        currently only ``'init'``.
        """
        return ('init',)

    @staticmethod
    def ready() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ReadyEvent`. This is
        currently only ``'ready'``.
        """
        return ('ready',)

    @staticmethod
    def offset() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`OffsetEvent`. This is
        currently only ``'offset'``.
        """
        return ('offset',)

    @staticmethod
    def transaction_start() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`TransactionStartEvent`.
        This is currently only ``'transaction-start'``.
        """
        return ('transaction-start',)

    @staticmethod
    def transaction_end() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`TransactionEndEvent`.
        This is currently only ``'transaction-end'``.
        """
        return ('transaction-end',)

    @staticmethod
    def contract_created(primary_only: bool, template: Any) -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ContractCreateEvent`
        of the specified template type.
        """
        return EventKey._contract(primary_only, 'create', template)

    @staticmethod
    def contract_exercised(primary_only: bool, template: Any, choice: Any) -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ContractExercisedEvent`
        of the specified choice.
        """
        return [f'{key}/{choice}'
                for key in EventKey._contract(primary_only, 'exercised', template)]

    @staticmethod
    def contract_archived(primary_only: bool, template: Any) -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ContractCreateEvent`
        of the specified template type.
        """
        return EventKey._contract(primary_only, 'archive', template)

    @staticmethod
    def _contract(primary_only: bool, prefix: str, template: Any) -> Collection[str]:
        m, t = validate_template(template)
        return tuple(f'{prefix}/{g}' for g in template_reverse_globs(primary_only, m, t))


def sortable_offset_height(value: str) -> int:
    if value:
        components = value.split('-', 3)
        if len(components) == 1:
            return int(value)
        elif len(components) >= 1:
            return int(components[1])
    return 0
