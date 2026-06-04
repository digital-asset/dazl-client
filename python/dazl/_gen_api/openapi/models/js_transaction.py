# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_type_0 import EventType0
    from ..models.event_type_1 import EventType1
    from ..models.event_type_2 import EventType2
    from ..models.trace_context import TraceContext


T = TypeVar("T", bound="JsTransaction")


@_attrs_define
class JsTransaction:
    """Filtered view of an on-ledger transaction's create and archive events.

    Attributes:
        update_id (str): Assigned by the server. Useful for correlating logs.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
        effective_at (str): Ledger effective time.

            Required
        events (list[EventType0 | EventType1 | EventType2]): The collection of events.
            Contains:

            - ``CreatedEvent`` or ``ArchivedEvent`` in case of ACS_DELTA transaction shape
            - ``CreatedEvent`` or ``ExercisedEvent`` in case of LEDGER_EFFECTS transaction shape

            Required: must be non-empty
        offset (int): The absolute offset. The details of this field are described in ``community/ledger-
            api/README.md``.
            It is a valid absolute offset (positive integer).

            Required
        synchronizer_id (str): A valid synchronizer id.
            Identifies the synchronizer that synchronized the transaction.

            Required
        record_time (str): The time at which the transaction was recorded. The record time refers to the synchronizer
            which synchronized the transaction.

            Required
        command_id (str | Unset): The ID of the command which resulted in this transaction. Missing for everyone except
            the submitting party.
            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
        workflow_id (str | Unset): The workflow ID used in command submission.
            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
        trace_context (TraceContext | Unset):
        external_transaction_hash (str | Unset): For transaction externally signed, contains the external transaction
            hash
            signed by the external party. Can be used to correlate an external submission with a committed transaction.

            Optional: can be empty
        paid_traffic_cost (int | Unset): The traffic cost that this participant node paid for the confirmation
            request for this transaction.

            Not set for transactions that were
            - initiated by another participant
            - initiated offline via the repair service
            - processed before the participant started serving traffic cost on the Ledger API
            - returned as part of a query filtering for a non submitting party

            Optional
    """

    update_id: str
    effective_at: str
    events: list[EventType0 | EventType1 | EventType2]
    offset: int
    synchronizer_id: str
    record_time: str
    command_id: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    trace_context: TraceContext | Unset = UNSET
    external_transaction_hash: str | Unset = UNSET
    paid_traffic_cost: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_type_0 import EventType0
        from ..models.event_type_1 import EventType1

        update_id = self.update_id

        effective_at = self.effective_at

        events = []
        for events_item_data in self.events:
            events_item: dict[str, Any]
            if isinstance(events_item_data, EventType0):
                events_item = events_item_data.to_dict()
            elif isinstance(events_item_data, EventType1):
                events_item = events_item_data.to_dict()
            else:
                events_item = events_item_data.to_dict()

            events.append(events_item)

        offset = self.offset

        synchronizer_id = self.synchronizer_id

        record_time = self.record_time

        command_id = self.command_id

        workflow_id = self.workflow_id

        trace_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace_context, Unset):
            trace_context = self.trace_context.to_dict()

        external_transaction_hash = self.external_transaction_hash

        paid_traffic_cost = self.paid_traffic_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updateId": update_id,
                "effectiveAt": effective_at,
                "events": events,
                "offset": offset,
                "synchronizerId": synchronizer_id,
                "recordTime": record_time,
            }
        )
        if command_id is not UNSET:
            field_dict["commandId"] = command_id
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if trace_context is not UNSET:
            field_dict["traceContext"] = trace_context
        if external_transaction_hash is not UNSET:
            field_dict["externalTransactionHash"] = external_transaction_hash
        if paid_traffic_cost is not UNSET:
            field_dict["paidTrafficCost"] = paid_traffic_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_type_0 import EventType0
        from ..models.event_type_1 import EventType1
        from ..models.event_type_2 import EventType2
        from ..models.trace_context import TraceContext

        d = dict(src_dict)
        update_id = d.pop("updateId")

        effective_at = d.pop("effectiveAt")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:

            def _parse_events_item(data: object) -> EventType0 | EventType1 | EventType2:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_event_type_0 = EventType0.from_dict(data)

                    return componentsschemas_event_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_event_type_1 = EventType1.from_dict(data)

                    return componentsschemas_event_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_event_type_2 = EventType2.from_dict(data)

                return componentsschemas_event_type_2

            events_item = _parse_events_item(events_item_data)

            events.append(events_item)

        offset = d.pop("offset")

        synchronizer_id = d.pop("synchronizerId")

        record_time = d.pop("recordTime")

        command_id = d.pop("commandId", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        _trace_context = d.pop("traceContext", UNSET)
        trace_context: TraceContext | Unset
        if isinstance(_trace_context, Unset):
            trace_context = UNSET
        else:
            trace_context = TraceContext.from_dict(_trace_context)

        external_transaction_hash = d.pop("externalTransactionHash", UNSET)

        paid_traffic_cost = d.pop("paidTrafficCost", UNSET)

        js_transaction = cls(
            update_id=update_id,
            effective_at=effective_at,
            events=events,
            offset=offset,
            synchronizer_id=synchronizer_id,
            record_time=record_time,
            command_id=command_id,
            workflow_id=workflow_id,
            trace_context=trace_context,
            external_transaction_hash=external_transaction_hash,
            paid_traffic_cost=paid_traffic_cost,
        )

        js_transaction.additional_properties = d
        return js_transaction

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
