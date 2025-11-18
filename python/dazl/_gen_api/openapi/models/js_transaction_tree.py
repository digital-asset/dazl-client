from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_int_tree_event import MapIntTreeEvent
    from ..models.trace_context import TraceContext


T = TypeVar("T", bound="JsTransactionTree")


@_attrs_define
class JsTransactionTree:
    """Provided for backwards compatibility, it will be removed in the Canton version 3.5.0.
    Complete view of an on-ledger transaction.

        Attributes:
            update_id (str): Assigned by the server. Useful for correlating logs.
                Must be a valid LedgerString (as described in ``value.proto``).
                Required
            command_id (str): The ID of the command which resulted in this transaction. Missing for everyone except the
                submitting party.
                Must be a valid LedgerString (as described in ``value.proto``).
                Optional
            workflow_id (str): The workflow ID used in command submission. Only set if the ``workflow_id`` for the command
                was set.
                Must be a valid LedgerString (as described in ``value.proto``).
                Optional
            offset (int): The absolute offset. The details of this field are described in ``community/ledger-
                api/README.md``.
                Required, it is a valid absolute offset (positive integer).
            events_by_id (MapIntTreeEvent):
            synchronizer_id (str): A valid synchronizer id.
                Identifies the synchronizer that synchronized the transaction.
                Required
            record_time (str): The time at which the transaction was recorded. The record time refers to the synchronizer
                which synchronized the transaction.
                Required
            effective_at (str | Unset): Ledger effective time.
                Required
            trace_context (TraceContext | Unset):
    """

    update_id: str
    command_id: str
    workflow_id: str
    offset: int
    events_by_id: MapIntTreeEvent
    synchronizer_id: str
    record_time: str
    effective_at: str | Unset = UNSET
    trace_context: TraceContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update_id = self.update_id

        command_id = self.command_id

        workflow_id = self.workflow_id

        offset = self.offset

        events_by_id = self.events_by_id.to_dict()

        synchronizer_id = self.synchronizer_id

        record_time = self.record_time

        effective_at = self.effective_at

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
                "eventsById": events_by_id,
                "synchronizerId": synchronizer_id,
                "recordTime": record_time,
            }
        )
        if effective_at is not UNSET:
            field_dict["effectiveAt"] = effective_at
        if trace_context is not UNSET:
            field_dict["traceContext"] = trace_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_int_tree_event import MapIntTreeEvent
        from ..models.trace_context import TraceContext

        d = dict(src_dict)
        update_id = d.pop("updateId")

        command_id = d.pop("commandId")

        workflow_id = d.pop("workflowId")

        offset = d.pop("offset")

        events_by_id = MapIntTreeEvent.from_dict(d.pop("eventsById"))

        synchronizer_id = d.pop("synchronizerId")

        record_time = d.pop("recordTime")

        effective_at = d.pop("effectiveAt", UNSET)

        _trace_context = d.pop("traceContext", UNSET)
        trace_context: TraceContext | Unset
        if isinstance(_trace_context, Unset):
            trace_context = UNSET
        else:
            trace_context = TraceContext.from_dict(_trace_context)

        js_transaction_tree = cls(
            update_id=update_id,
            command_id=command_id,
            workflow_id=workflow_id,
            offset=offset,
            events_by_id=events_by_id,
            synchronizer_id=synchronizer_id,
            record_time=record_time,
            effective_at=effective_at,
            trace_context=trace_context,
        )

        js_transaction_tree.additional_properties = d
        return js_transaction_tree

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
