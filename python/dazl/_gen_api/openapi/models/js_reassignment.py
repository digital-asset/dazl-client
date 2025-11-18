from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        command_id (str): The ID of the command which resulted in this reassignment. Missing for everyone except the
            submitting party on the submitting participant.
            Must be a valid LedgerString (as described in ``value.proto``).
            Optional
        workflow_id (str): The workflow ID used in reassignment command submission. Only set if the ``workflow_id`` for
            the command was set.
            Must be a valid LedgerString (as described in ``value.proto``).
            Optional
        offset (int): The participant's offset. The details of this field are described in ``community/ledger-
            api/README.md``.
            Required, must be a valid absolute offset (positive integer).
        record_time (str): The time at which the reassignment was recorded. The record time refers to the source/target
            synchronizer for an unassign/assign event respectively.
            Required
        synchronizer_id (str): A valid synchronizer id.
            Identifies the synchronizer that synchronized this Reassignment.
            Required
        events (list[JsReassignmentEventType0 | JsReassignmentEventType1] | Unset): The collection of reassignment
            events. Required.
        trace_context (TraceContext | Unset):
    """

    update_id: str
    command_id: str
    workflow_id: str
    offset: int
    record_time: str
    synchronizer_id: str
    events: list[JsReassignmentEventType0 | JsReassignmentEventType1] | Unset = UNSET
    trace_context: TraceContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.js_reassignment_event_type_0 import JsReassignmentEventType0

        update_id = self.update_id

        command_id = self.command_id

        workflow_id = self.workflow_id

        offset = self.offset

        record_time = self.record_time

        synchronizer_id = self.synchronizer_id

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item: dict[str, Any]
                if isinstance(events_item_data, JsReassignmentEventType0):
                    events_item = events_item_data.to_dict()
                else:
                    events_item = events_item_data.to_dict()

                events.append(events_item)

        trace_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace_context, Unset):
            trace_context = self.trace_context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updateId": update_id,
                "commandId": command_id,
                "workflowId": workflow_id,
                "offset": offset,
                "recordTime": record_time,
                "synchronizerId": synchronizer_id,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events
        if trace_context is not UNSET:
            field_dict["traceContext"] = trace_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_reassignment_event_type_0 import JsReassignmentEventType0
        from ..models.js_reassignment_event_type_1 import JsReassignmentEventType1
        from ..models.trace_context import TraceContext

        d = dict(src_dict)
        update_id = d.pop("updateId")

        command_id = d.pop("commandId")

        workflow_id = d.pop("workflowId")

        offset = d.pop("offset")

        record_time = d.pop("recordTime")

        synchronizer_id = d.pop("synchronizerId")

        _events = d.pop("events", UNSET)
        events: list[JsReassignmentEventType0 | JsReassignmentEventType1] | Unset = (
            UNSET
        )
        if _events is not UNSET:
            events = []
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
                    componentsschemas_js_reassignment_event_type_1 = (
                        JsReassignmentEventType1.from_dict(data)
                    )

                    return componentsschemas_js_reassignment_event_type_1

                events_item = _parse_events_item(events_item_data)

                events.append(events_item)

        _trace_context = d.pop("traceContext", UNSET)
        trace_context: TraceContext | Unset
        if isinstance(_trace_context, Unset):
            trace_context = UNSET
        else:
            trace_context = TraceContext.from_dict(_trace_context)

        js_reassignment = cls(
            update_id=update_id,
            command_id=command_id,
            workflow_id=workflow_id,
            offset=offset,
            record_time=record_time,
            synchronizer_id=synchronizer_id,
            events=events,
            trace_context=trace_context,
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
