from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_assigned_event import JsAssignedEvent


T = TypeVar("T", bound="JsIncompleteAssigned")


@_attrs_define
class JsIncompleteAssigned:
    """
    Attributes:
        assigned_event (JsAssignedEvent): Records that a contract has been assigned, and it can be used on the target
            synchronizer.
    """

    assigned_event: JsAssignedEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_event = self.assigned_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignedEvent": assigned_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_assigned_event import JsAssignedEvent

        d = dict(src_dict)
        assigned_event = JsAssignedEvent.from_dict(d.pop("assignedEvent"))

        js_incomplete_assigned = cls(
            assigned_event=assigned_event,
        )

        js_incomplete_assigned.additional_properties = d
        return js_incomplete_assigned

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
