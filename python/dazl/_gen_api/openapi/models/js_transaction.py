from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        command_id (str): The ID of the command which resulted in this transaction. Missing for everyone except the
            submitting party.
            Must be a valid LedgerString (as described in ``value.proto``).
            Optional
        workflow_id (str): The workflow ID used in command submission.
            Must be a valid LedgerString (as described in ``value.proto``).
            Optional
        effective_at (str): Ledger effective time.
            Required
        offset (int): The absolute offset. The details of this field are described in ``community/ledger-
            api/README.md``.
            Required, it is a valid absolute offset (positive integer).
        synchronizer_id (str): A valid synchronizer id.
            Identifies the synchronizer that synchronized the transaction.
            Required
        record_time (str): The time at which the transaction was recorded. The record time refers to the synchronizer
            which synchronized the transaction.
            Required
        events (list[EventType0 | EventType1 | EventType2] | Unset): The collection of events.
            Contains:

            - ``CreatedEvent`` or ``ArchivedEvent`` in case of ACS_DELTA transaction shape
            - ``CreatedEvent`` or ``ExercisedEvent`` in case of LEDGER_EFFECTS transaction shape

            Required
        trace_context (TraceContext | Unset):
        external_transaction_hash (str | Unset): For transaction externally signed, contains the external transaction
            hash
            signed by the external party. Can be used to correlate an external submission with a committed transaction.
            Optional
    """

    update_id: str
    command_id: str
    workflow_id: str
    effective_at: str
    offset: int
    synchronizer_id: str
    record_time: str
    events: list[EventType0 | EventType1 | EventType2] | Unset = UNSET
    trace_context: TraceContext | Unset = UNSET
    external_transaction_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_type_0 import EventType0
        from ..models.event_type_1 import EventType1

        update_id = self.update_id

        command_id = self.command_id

        workflow_id = self.workflow_id

        effective_at = self.effective_at

        offset = self.offset

        synchronizer_id = self.synchronizer_id

        record_time = self.record_time

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
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

        trace_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace_context, Unset):
            trace_context = self.trace_context.to_dict()

        external_transaction_hash = self.external_transaction_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updateId": update_id,
                "commandId": command_id,
                "workflowId": workflow_id,
                "effectiveAt": effective_at,
                "offset": offset,
                "synchronizerId": synchronizer_id,
                "recordTime": record_time,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events
        if trace_context is not UNSET:
            field_dict["traceContext"] = trace_context
        if external_transaction_hash is not UNSET:
            field_dict["externalTransactionHash"] = external_transaction_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_type_0 import EventType0
        from ..models.event_type_1 import EventType1
        from ..models.event_type_2 import EventType2
        from ..models.trace_context import TraceContext

        d = dict(src_dict)
        update_id = d.pop("updateId")

        command_id = d.pop("commandId")

        workflow_id = d.pop("workflowId")

        effective_at = d.pop("effectiveAt")

        offset = d.pop("offset")

        synchronizer_id = d.pop("synchronizerId")

        record_time = d.pop("recordTime")

        _events = d.pop("events", UNSET)
        events: list[EventType0 | EventType1 | EventType2] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:

                def _parse_events_item(
                    data: object,
                ) -> EventType0 | EventType1 | EventType2:
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

        _trace_context = d.pop("traceContext", UNSET)
        trace_context: TraceContext | Unset
        if isinstance(_trace_context, Unset):
            trace_context = UNSET
        else:
            trace_context = TraceContext.from_dict(_trace_context)

        external_transaction_hash = d.pop("externalTransactionHash", UNSET)

        js_transaction = cls(
            update_id=update_id,
            command_id=command_id,
            workflow_id=workflow_id,
            effective_at=effective_at,
            offset=offset,
            synchronizer_id=synchronizer_id,
            record_time=record_time,
            events=events,
            trace_context=trace_context,
            external_transaction_hash=external_transaction_hash,
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
