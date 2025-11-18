from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.created_event import CreatedEvent


T = TypeVar("T", bound="EventType1")


@_attrs_define
class EventType1:
    """
    Attributes:
        created_event (CreatedEvent): Records that a contract has been created, and choices may now be exercised on it.
    """

    created_event: CreatedEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_event = self.created_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CreatedEvent": created_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_event import CreatedEvent

        d = dict(src_dict)
        created_event = CreatedEvent.from_dict(d.pop("CreatedEvent"))

        event_type_1 = cls(
            created_event=created_event,
        )

        event_type_1.additional_properties = d
        return event_type_1

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
