from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exercised_event import ExercisedEvent


T = TypeVar("T", bound="EventType2")


@_attrs_define
class EventType2:
    """
    Attributes:
        exercised_event (ExercisedEvent): Records that a choice has been exercised on a target contract.
    """

    exercised_event: ExercisedEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercised_event = self.exercised_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ExercisedEvent": exercised_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercised_event import ExercisedEvent

        d = dict(src_dict)
        exercised_event = ExercisedEvent.from_dict(d.pop("ExercisedEvent"))

        event_type_2 = cls(
            exercised_event=exercised_event,
        )

        event_type_2.additional_properties = d
        return event_type_2

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
