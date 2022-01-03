# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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
from typing import TYPE_CHECKING, Any, Collection, Optional, Sequence, Union

from ..damlast.daml_lf_1 import TypeConName
from ..damlast.protocols import SymbolLookup
from ..prim import ContractData, ContractId, Party

if TYPE_CHECKING:
    from ..client.state import ContractContextualData
    from ..model.types_store import PackageStore

__all__ = [
    "BaseEvent",
    "InitEvent",
    "OffsetEvent",
    "ReadyEvent",
    "ActiveContractSetEvent",
    "BaseTransactionEvent",
    "TransactionStartEvent",
    "TransactionEndEvent",
    "ContractEvent",
    "ContractCreateEvent",
    "ContractExercisedEvent",
    "ContractArchiveEvent",
    "PackagesAddedEvent",
    "ContractFilter",
    "TransactionFilter",
]


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

    def acs_find_active(self, template: "Union[str, TypeConName]", match=None):
        return self.client.find_active(template, match)

    def acs_find_by_id(self, cid: "Union[str, ContractId]") -> "Optional[ContractContextualData]":
        return self.client.find_by_id(cid)

    def acs_find_one(self, template: "Union[str, TypeConName]", match=None):
        return self.client.find_one(template, match=match)

    def acs_find_historical(self, template: "Union[str, TypeConName]", match=None):
        return self.client.find_historical(template, match)

    def acs_find_nonempty(self, template: "Union[str, TypeConName]", match=None):
        return self.client.find_nonempty(template, match=match)

    def __repr__(self):
        fields = ", ".join(
            f"{k}={v!r}"
            for k, v in self.__dict__.items()
            if not k.startswith("_") and k != "client" and k != "lookup" and k != "ledger_id"
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

    offset: Optional[str]


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
