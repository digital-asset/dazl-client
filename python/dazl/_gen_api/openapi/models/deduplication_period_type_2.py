from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.empty import Empty


T = TypeVar("T", bound="DeduplicationPeriodType2")


@_attrs_define
class DeduplicationPeriodType2:
    """
    Attributes:
        empty (Empty):
    """

    empty: Empty
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Empty": empty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.empty import Empty

        d = dict(src_dict)
        empty = Empty.from_dict(d.pop("Empty"))

        deduplication_period_type_2 = cls(
            empty=empty,
        )

        deduplication_period_type_2.additional_properties = d
        return deduplication_period_type_2

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
