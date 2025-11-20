from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Field")


@_attrs_define
class Field:
    """
    Attributes:
        varint (list[int] | Unset):
        fixed64 (list[int] | Unset):
        fixed32 (list[int] | Unset):
        length_delimited (list[str] | Unset):
    """

    varint: list[int] | Unset = UNSET
    fixed64: list[int] | Unset = UNSET
    fixed32: list[int] | Unset = UNSET
    length_delimited: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        varint: list[int] | Unset = UNSET
        if not isinstance(self.varint, Unset):
            varint = self.varint

        fixed64: list[int] | Unset = UNSET
        if not isinstance(self.fixed64, Unset):
            fixed64 = self.fixed64

        fixed32: list[int] | Unset = UNSET
        if not isinstance(self.fixed32, Unset):
            fixed32 = self.fixed32

        length_delimited: list[str] | Unset = UNSET
        if not isinstance(self.length_delimited, Unset):
            length_delimited = self.length_delimited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if varint is not UNSET:
            field_dict["varint"] = varint
        if fixed64 is not UNSET:
            field_dict["fixed64"] = fixed64
        if fixed32 is not UNSET:
            field_dict["fixed32"] = fixed32
        if length_delimited is not UNSET:
            field_dict["lengthDelimited"] = length_delimited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        varint = cast(list[int], d.pop("varint", UNSET))

        fixed64 = cast(list[int], d.pop("fixed64", UNSET))

        fixed32 = cast(list[int], d.pop("fixed32", UNSET))

        length_delimited = cast(list[str], d.pop("lengthDelimited", UNSET))

        field = cls(
            varint=varint,
            fixed64=fixed64,
            fixed32=fixed32,
            length_delimited=length_delimited,
        )

        field.additional_properties = d
        return field

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
