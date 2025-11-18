from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.created_event import CreatedEvent


T = TypeVar("T", bound="JsCreated")


@_attrs_define
class JsCreated:
    """
    Attributes:
        created_event (CreatedEvent): Records that a contract has been created, and choices may now be exercised on it.
        synchronizer_id (str): The synchronizer which sequenced the creation of the contract
            Required
    """

    created_event: CreatedEvent
    synchronizer_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_event = self.created_event.to_dict()

        synchronizer_id = self.synchronizer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdEvent": created_event,
                "synchronizerId": synchronizer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_event import CreatedEvent

        d = dict(src_dict)
        created_event = CreatedEvent.from_dict(d.pop("createdEvent"))

        synchronizer_id = d.pop("synchronizerId")

        js_created = cls(
            created_event=created_event,
            synchronizer_id=synchronizer_id,
        )

        js_created.additional_properties = d
        return js_created

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
