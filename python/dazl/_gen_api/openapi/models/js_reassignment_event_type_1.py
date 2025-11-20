from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_unassigned_event import JsUnassignedEvent


T = TypeVar("T", bound="JsReassignmentEventType1")


@_attrs_define
class JsReassignmentEventType1:
    """
    Attributes:
        js_unassigned_event (JsUnassignedEvent): Records that a contract has been unassigned, and it becomes unusable on
            the source synchronizer
    """

    js_unassigned_event: JsUnassignedEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        js_unassigned_event = self.js_unassigned_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "JsUnassignedEvent": js_unassigned_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_unassigned_event import JsUnassignedEvent

        d = dict(src_dict)
        js_unassigned_event = JsUnassignedEvent.from_dict(d.pop("JsUnassignedEvent"))

        js_reassignment_event_type_1 = cls(
            js_unassigned_event=js_unassigned_event,
        )

        js_reassignment_event_type_1.additional_properties = d
        return js_reassignment_event_type_1

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
