from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.created_tree_event import CreatedTreeEvent


T = TypeVar("T", bound="TreeEventType0")


@_attrs_define
class TreeEventType0:
    """
    Attributes:
        created_tree_event (CreatedTreeEvent):
    """

    created_tree_event: CreatedTreeEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_tree_event = self.created_tree_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CreatedTreeEvent": created_tree_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_tree_event import CreatedTreeEvent

        d = dict(src_dict)
        created_tree_event = CreatedTreeEvent.from_dict(d.pop("CreatedTreeEvent"))

        tree_event_type_0 = cls(
            created_tree_event=created_tree_event,
        )

        tree_event_type_0.additional_properties = d
        return tree_event_type_0

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
