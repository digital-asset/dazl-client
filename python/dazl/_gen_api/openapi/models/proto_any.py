# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ProtoAny")


@_attrs_define
class ProtoAny:
    """
    Attributes:
        type_url (str):
        value (str):
        unknown_fields (UnknownFieldSet):
        value_decoded (str | Unset):
    """

    type_url: str
    value: str
    unknown_fields: UnknownFieldSet
    value_decoded: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_url = self.type_url

        value = self.value

        unknown_fields = self.unknown_fields.to_dict()

        value_decoded = self.value_decoded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeUrl": type_url,
                "value": value,
                "unknownFields": unknown_fields,
            }
        )
        if value_decoded is not UNSET:
            field_dict["valueDecoded"] = value_decoded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        type_url = d.pop("typeUrl")

        value = d.pop("value")

        unknown_fields = UnknownFieldSet.from_dict(d.pop("unknownFields"))

        value_decoded = d.pop("valueDecoded", UNSET)

        proto_any = cls(
            type_url=type_url,
            value=value,
            unknown_fields=unknown_fields,
            value_decoded=value_decoded,
        )

        proto_any.additional_properties = d
        return proto_any

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
