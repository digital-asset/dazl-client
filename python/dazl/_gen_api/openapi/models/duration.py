from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="Duration")


@_attrs_define
class Duration:
    """
    Attributes:
        seconds (int):
        nanos (int):
        unknown_fields (UnknownFieldSet | Unset):
    """

    seconds: int
    nanos: int
    unknown_fields: UnknownFieldSet | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seconds = self.seconds

        nanos = self.nanos

        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seconds": seconds,
                "nanos": nanos,
            }
        )
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        seconds = d.pop("seconds")

        nanos = d.pop("nanos")

        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        duration = cls(
            seconds=seconds,
            nanos=nanos,
            unknown_fields=unknown_fields,
        )

        duration.additional_properties = d
        return duration

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
