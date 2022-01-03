# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from typing import Any, Callable, Collection, Iterator, TypeVar
import warnings

from ..damlast.lookup import matching_normalizations, normalize, validate_template
from ..protocols.events import (
    BaseEvent,
    ContractArchiveEvent,
    ContractCreateEvent,
    ContractExercisedEvent,
    InitEvent,
    OffsetEvent,
    PackagesAddedEvent,
    ReadyEvent,
    TransactionEndEvent,
    TransactionStartEvent,
)

__all__ = ["EventKey", "_template_reverse_globs"]

T = TypeVar("T")


def create_dispatch(
    on_init: "Callable[[InitEvent], T]",
    on_ready: "Callable[[ReadyEvent], T]",
    on_offset: "Callable[[OffsetEvent], T]",
    on_transaction_start: "Callable[[TransactionStartEvent], T]",
    on_transaction_end: "Callable[[TransactionEndEvent], T]",
    on_contract_created: "Callable[[ContractCreateEvent], T]",
    on_contract_exercised: "Callable[[ContractExercisedEvent], T]",
    on_contract_archived: "Callable[[ContractArchiveEvent], T]",
    on_packages_added: "Callable[[PackagesAddedEvent], T]",
) -> "Callable[[BaseEvent], T]":
    def handle(event: "BaseEvent") -> "T":
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


def _template_reverse_globs(primary_only: bool, package_id: str, type_name: str) -> "Iterator[str]":
    """
    Return an iterator over strings that glob to a specified type.

    This symbol is meant only for supporting the dazl v7 and is not a public API!
    """
    # support deprecated type identifiers for usages of this old API to preserve backwards
    # compatibility
    use_deprecated_form = False
    if type_name != "*" and ":" not in type_name:
        m, delim, e = type_name.rpartition(".")
        if delim:
            use_deprecated_form = True
            type_name = f"{m}:{e}"
    t = f"{package_id}:{type_name}"

    if primary_only:
        yield normalize(t)
    else:
        for form in matching_normalizations(t):
            yield form
            if use_deprecated_form and len(form.split(":")) == 3:
                s, _, e = form.rpartition(":")
                yield f"{s}.{e}"


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
    def _contract(primary_only: bool, prefix: str, template: "Any") -> Collection[str]:
        m, t = validate_template(template)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return tuple(f"{prefix}/{g}" for g in _template_reverse_globs(primary_only, m, t))
