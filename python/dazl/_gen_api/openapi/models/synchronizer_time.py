from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SynchronizerTime")


@_attrs_define
class SynchronizerTime:
    """
    Attributes:
        synchronizer_id (str): The id of the synchronizer.
            Required
        record_time (str | Unset): All commands with a maximum record time below this value MUST be considered lost if
            their completion has not arrived before this checkpoint.
            Required
    """

    synchronizer_id: str
    record_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer_id = self.synchronizer_id

        record_time = self.record_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizerId": synchronizer_id,
            }
        )
        if record_time is not UNSET:
            field_dict["recordTime"] = record_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        synchronizer_id = d.pop("synchronizerId")

        record_time = d.pop("recordTime", UNSET)

        synchronizer_time = cls(
            synchronizer_id=synchronizer_id,
            record_time=record_time,
        )

        synchronizer_time.additional_properties = d
        return synchronizer_time

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
