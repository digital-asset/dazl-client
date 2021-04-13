# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# TODO: `automodule reading` directive doesn't appear to work here, have to list each class individually.
"""
Read-Side Types
---------------

This module contains models used on the read-side of the Ledger API.

.. autoclass:: InitEvent
  :members:

.. autoclass::  InitEvent
  :members:

.. autoclass::  OffsetEvent
  :members:

.. autoclass::  ReadyEvent
  :members:

.. autoclass::  ActiveContractSetEvent
  :members:

.. autoclass::  BaseTransactionEvent
  :members:

.. autoclass::  TransactionStartEvent
  :members:

.. autoclass::  TransactionEndEvent
  :members:

.. autoclass::  ContractEvent
  :members:

.. autoclass::  ContractCreateEvent
  :members:

.. autoclass::  ContractExercisedEvent
  :members:

.. autoclass::  ContractArchiveEvent
  :members:

.. autoclass::  PackagesAddedEvent
  :members:

.. autoclass::  TransactionFilter
  :members:

.. autoclass::  EventKey
  :members:

"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Collection, Optional, Sequence, TypeVar, Union
import warnings

from ..damlast.daml_lf_1 import TypeConName
from ..damlast.lookup import validate_template
from ..damlast.protocols import SymbolLookup
from .core import ContractContextualData, ContractData, ContractId, Party
from .lookup import template_reverse_globs

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)

    from .types import TypeReference
    from .types_store import PackageStore

T = TypeVar("T")


@dataclass(frozen=True)
class BaseEvent:
    """
    Superclass of all dazl events.
    """

    client: "Any"
    party: "Optional[Party]"
    time: "Optional[datetime]"
    ledger_id: str
    lookup: "SymbolLookup"
    package_store: "PackageStore"

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
        fields = ", ".join(
            f"{k}={v!r}"
            for k, v in self.__dict__.items()
            if not k.startswith("_") and k != "client" and k != "package_store" and k != "ledger_id"
        )
        return f"{self.__class__.__name__}({fields})"


@dataclass(frozen=True)
class InitEvent(BaseEvent):
    """
    Event raised when dazl is initialized, but before it has begun reading from the Active Contract
    Set (ACS).
    """


@dataclass(frozen=True)
class OffsetEvent(BaseEvent):
    """
    Event raised when dazl is ready to begin processing new events. At this point, the Active
    Contract Set (ACS) is populated with the current state of the ledger.
    """

    offset: "Optional[str]"


@dataclass(frozen=True)
class ReadyEvent(OffsetEvent):
    """
    Event raised when dazl is ready to begin processing new events. At this point, the Active
    Contract Set (ACS) is populated with the current state of the ledger.
    """


@dataclass(frozen=True)
class ActiveContractSetEvent(OffsetEvent):
    """
    Event raised on initial read of the active contract set.
    """

    contract_events: "Sequence[ContractCreateEvent]"


@dataclass(frozen=True)
class BaseTransactionEvent(OffsetEvent):
    """
    Event raised when dazl encounters a new transaction. This is raised before any corresponding
    :class:`ContractCreateEvent` or :class:`ContractArchiveEvent`.
    """

    command_id: str
    workflow_id: str


@dataclass(frozen=True)
class TransactionStartEvent(BaseTransactionEvent):
    """
    Event raised when dazl encounters a new transaction. This is raised before any corresponding
    :class:`ContractCreateEvent` or :class:`ContractArchiveEvent`.
    """

    contract_events: "Sequence[ContractEvent]"


@dataclass(frozen=True)
class TransactionEndEvent(BaseTransactionEvent):
    """
    Event raised when dazl encounters the end of a transaction. This is raised after any
    corresponding :class:`ContractCreateEvent` or :class:`ContractArchiveEvent`.
    """

    contract_events: "Sequence[ContractEvent]"


@dataclass(frozen=True)
class ContractEvent(BaseTransactionEvent):
    """
    Event raised when dazl automation detects a new create or an archive. The Active Contract Set
    (ACS) reflects this event, as well as all other events that occurred in the same transaction.
    """

    cid: ContractId
    cdata: ContractData
    command_id: str
    workflow_id: str
    event_id: str
    witness_parties: Sequence[str]


@dataclass(frozen=True)
class ContractCreateEvent(ContractEvent):
    """
    Event raised when dazl automation detects a contract create. The Active Contract Set
    (ACS) reflects this event, as well as all other events that occurred in the same transaction.
    """


@dataclass(frozen=True)
class ContractExercisedEvent(ContractEvent):
    """
    Event raised when dazl automation detects a contract exercised.
    """

    contract_creating_event_id: None
    choice: str
    choice_args: Any
    acting_parties: Sequence[str]
    consuming: bool
    child_event_ids: Sequence[str]
    exercise_result: Any


@dataclass(frozen=True)
class ContractArchiveEvent(ContractEvent):
    """
    Event raised when dazl automation detects a contract archive. The Active Contract Set
    (ACS) reflects this event, as well as all other events that occurred in the same transaction.
    """


@dataclass(frozen=True)
class PackagesAddedEvent(BaseEvent):
    """
    Event raised when new packages have been detected.
    """

    initial: bool


def create_dispatch(
    on_init: Callable[[InitEvent], T],
    on_ready: Callable[[ReadyEvent], T],
    on_offset: Callable[[OffsetEvent], T],
    on_transaction_start: Callable[[TransactionStartEvent], T],
    on_transaction_end: Callable[[TransactionEndEvent], T],
    on_contract_created: Callable[[ContractCreateEvent], T],
    on_contract_exercised: Callable[[ContractExercisedEvent], T],
    on_contract_archived: Callable[[ContractArchiveEvent], T],
    on_packages_added: Callable[[PackagesAddedEvent], T],
) -> Callable[[BaseEvent], T]:
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
        elif isinstance(event, PackagesAddedEvent):
            return on_packages_added(event)
        else:
            raise ValueError(f"unknown subclass of BaseEvent: {event!r}")

    return handle


@dataclass(frozen=True)
class ContractFilter:
    templates: "Optional[Collection[TypeConName]]" = None
    party_groups: "Optional[Collection[Party]]" = None


@dataclass(frozen=True)
class TransactionFilter(ContractFilter):
    current_offset: "Optional[str]" = None
    destination_offset: "Optional[str]" = None

    def __post_init__(self):
        if self.current_offset is not None and self.destination_offset is not None:
            if self.current_offset > self.destination_offset:
                raise ValueError(
                    "current_offset must be before destination_offset if both are specified"
                )


class EventKey:
    from_event = create_dispatch(
        on_init=lambda _: EventKey.init(),
        on_ready=lambda _: EventKey.ready(),
        on_offset=lambda _: EventKey.offset(),
        on_transaction_start=lambda _: EventKey.transaction_start(),
        on_transaction_end=lambda _: EventKey.transaction_end(),
        on_contract_created=lambda event: EventKey.contract_created(False, event.cid.value_type),
        on_contract_exercised=lambda event: EventKey.contract_exercised(
            False, event.cid.value_type, event.choice
        ),
        on_contract_archived=lambda event: EventKey.contract_archived(False, event.cid.value_type),
        on_packages_added=lambda event: EventKey.packages_added(
            initial=event.initial, changed=not event.initial
        ),
    )

    @staticmethod
    def init() -> Collection[str]:
        """
        Return the names of events that get raised in response to an :class:`InitEvent`. This is
        currently only ``'init'``.
        """
        return ("init",)

    @staticmethod
    def ready() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ReadyEvent`. This is
        currently only ``'ready'``.
        """
        return ("ready",)

    @staticmethod
    def offset() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`OffsetEvent`. This is
        currently only ``'offset'``.
        """
        return ("offset",)

    @staticmethod
    def transaction_start() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`TransactionStartEvent`.
        This is currently only ``'transaction-start'``.
        """
        return ("transaction-start",)

    @staticmethod
    def transaction_end() -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`TransactionEndEvent`.
        This is currently only ``'transaction-end'``.
        """
        return ("transaction-end",)

    @staticmethod
    def contract_created(primary_only: bool, template: Any) -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ContractCreateEvent`
        of the specified template type.
        """
        return EventKey._contract(primary_only, "create", template)

    @staticmethod
    def contract_exercised(primary_only: bool, template: Any, choice: Any) -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ContractExercisedEvent`
        of the specified choice.
        """
        return [
            f"{key}/{choice}" for key in EventKey._contract(primary_only, "exercised", template)
        ]

    @staticmethod
    def contract_archived(primary_only: bool, template: Any) -> Collection[str]:
        """
        Return the names of events that get raised in response to a :class:`ContractCreateEvent`
        of the specified template type.
        """
        return EventKey._contract(primary_only, "archive", template)

    @staticmethod
    def packages_added(initial: bool, changed: bool) -> "Collection[str]":
        keys = []
        if initial:
            keys.append("packages-added/initial")
        if changed:
            keys.append("packages-added/changed")
        return tuple(keys)

    @staticmethod
    def _contract(primary_only: bool, prefix: str, template: Any) -> Collection[str]:
        m, t = validate_template(template, allow_deprecated_identifiers=True)
        return tuple(f"{prefix}/{g}" for g in template_reverse_globs(primary_only, m, t))


def max_offset(offsets: "Collection[Optional[str]]") -> "Optional[str]":
    """
    Return the most "recent" offset from a collection of offsets.

    :param offsets: A collection of offsets to examine.
    :return: The largest offset, or ``None`` if unknown.
    """
    non_none_offsets = [offset for offset in offsets if offset is not None]
    return max(non_none_offsets) if non_none_offsets else None
