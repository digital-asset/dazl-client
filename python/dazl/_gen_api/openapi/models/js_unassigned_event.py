from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unassigned_event import UnassignedEvent


T = TypeVar("T", bound="JsUnassignedEvent")


@_attrs_define
class JsUnassignedEvent:
    """Records that a contract has been unassigned, and it becomes unusable on the source synchronizer

    Attributes:
        value (UnassignedEvent): Records that a contract has been unassigned, and it becomes unusable on the source
            synchronizer
    """

    value: UnassignedEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unassigned_event import UnassignedEvent

        d = dict(src_dict)
        value = UnassignedEvent.from_dict(d.pop("value"))

        js_unassigned_event = cls(
            value=value,
        )

        js_unassigned_event.additional_properties = d
        return js_unassigned_event

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
