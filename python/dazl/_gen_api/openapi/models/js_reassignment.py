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
    from ..models.js_reassignment_event_type_0 import JsReassignmentEventType0
    from ..models.js_reassignment_event_type_1 import JsReassignmentEventType1
    from ..models.trace_context import TraceContext


T = TypeVar("T", bound="JsReassignment")


@_attrs_define
class JsReassignment:
    """Complete view of an on-ledger reassignment.

    Attributes:
        update_id (str): Assigned by the server. Useful for correlating logs.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
        offset (int): The participant's offset. The details of this field are described in ``community/ledger-
            api/README.md``.
            Must be a valid absolute offset (positive integer).

            Required
        events (list[JsReassignmentEventType0 | JsReassignmentEventType1]): The collection of reassignment events.

            Required: must be non-empty
        record_time (str): The time at which the reassignment was recorded. The record time refers to the source/target
            synchronizer for an unassign/assign event respectively.

            Required
        synchronizer_id (str): A valid synchronizer id.
            Identifies the synchronizer that synchronized this Reassignment.

            Required
        command_id (str | Unset): The ID of the command which resulted in this reassignment. Missing for everyone except
            the submitting party on the submitting participant.
            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
        workflow_id (str | Unset): The workflow ID used in reassignment command submission. Only set if the
            ``workflow_id`` for the command was set.
            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
        trace_context (TraceContext | Unset):
        paid_traffic_cost (int | Unset): The traffic cost that this participant node paid for the corresponding
            (un)assignment request.

            Not set for transactions that were
            - initiated by another participant
            - initiated offline via the repair service
            - processed before the participant started serving traffic cost on the Ledger API
            - returned as part of a query filtering for a non submitting party

            Optional
    """

    update_id: str
    offset: int
    events: list[JsReassignmentEventType0 | JsReassignmentEventType1]
    record_time: str
    synchronizer_id: str
    command_id: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    trace_context: TraceContext | Unset = UNSET
    paid_traffic_cost: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.js_reassignment_event_type_0 import JsReassignmentEventType0

        update_id = self.update_id

        offset = self.offset

        events = []
        for events_item_data in self.events:
            events_item: dict[str, Any]
            if isinstance(events_item_data, JsReassignmentEventType0):
                events_item = events_item_data.to_dict()
            else:
                events_item = events_item_data.to_dict()

            events.append(events_item)

        record_time = self.record_time

        synchronizer_id = self.synchronizer_id

        command_id = self.command_id

        workflow_id = self.workflow_id

        trace_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace_context, Unset):
            trace_context = self.trace_context.to_dict()

        paid_traffic_cost = self.paid_traffic_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updateId": update_id,
                "offset": offset,
                "events": events,
                "recordTime": record_time,
                "synchronizerId": synchronizer_id,
            }
        )
        if command_id is not UNSET:
            field_dict["commandId"] = command_id
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if trace_context is not UNSET:
            field_dict["traceContext"] = trace_context
        if paid_traffic_cost is not UNSET:
            field_dict["paidTrafficCost"] = paid_traffic_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_reassignment_event_type_0 import JsReassignmentEventType0
        from ..models.js_reassignment_event_type_1 import JsReassignmentEventType1
        from ..models.trace_context import TraceContext

        d = dict(src_dict)
        update_id = d.pop("updateId")

        offset = d.pop("offset")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:

            def _parse_events_item(
                data: object,
            ) -> JsReassignmentEventType0 | JsReassignmentEventType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_js_reassignment_event_type_0 = (
                        JsReassignmentEventType0.from_dict(data)
                    )

                    return componentsschemas_js_reassignment_event_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_js_reassignment_event_type_1 = JsReassignmentEventType1.from_dict(
                    data
                )

                return componentsschemas_js_reassignment_event_type_1

            events_item = _parse_events_item(events_item_data)

            events.append(events_item)

        record_time = d.pop("recordTime")

        synchronizer_id = d.pop("synchronizerId")

        command_id = d.pop("commandId", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        _trace_context = d.pop("traceContext", UNSET)
        trace_context: TraceContext | Unset
        if isinstance(_trace_context, Unset):
            trace_context = UNSET
        else:
            trace_context = TraceContext.from_dict(_trace_context)

        paid_traffic_cost = d.pop("paidTrafficCost", UNSET)

        js_reassignment = cls(
            update_id=update_id,
            offset=offset,
            events=events,
            record_time=record_time,
            synchronizer_id=synchronizer_id,
            command_id=command_id,
            workflow_id=workflow_id,
            trace_context=trace_context,
            paid_traffic_cost=paid_traffic_cost,
        )

        js_reassignment.additional_properties = d
        return js_reassignment

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
