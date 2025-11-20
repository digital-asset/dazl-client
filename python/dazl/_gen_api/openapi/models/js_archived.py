from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.archived_event import ArchivedEvent


T = TypeVar("T", bound="JsArchived")


@_attrs_define
class JsArchived:
    """
    Attributes:
        archived_event (ArchivedEvent): Records that a contract has been archived, and choices may no longer be
            exercised on it.
        synchronizer_id (str): Required
            The synchronizer which sequenced the archival of the contract
    """

    archived_event: ArchivedEvent
    synchronizer_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived_event = self.archived_event.to_dict()

        synchronizer_id = self.synchronizer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archivedEvent": archived_event,
                "synchronizerId": synchronizer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archived_event import ArchivedEvent

        d = dict(src_dict)
        archived_event = ArchivedEvent.from_dict(d.pop("archivedEvent"))

        synchronizer_id = d.pop("synchronizerId")

        js_archived = cls(
            archived_event=archived_event,
            synchronizer_id=synchronizer_id,
        )

        js_archived.additional_properties = d
        return js_archived

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
