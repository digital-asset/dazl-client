# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FieldMask")


@_attrs_define
class FieldMask:
    """
    Attributes:
        unknown_fields (UnknownFieldSet):
        paths (list[str] | Unset):
    """

    unknown_fields: UnknownFieldSet
    paths: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields = self.unknown_fields.to_dict()

        paths: list[str] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unknownFields": unknown_fields,
            }
        )
        if paths is not UNSET:
            field_dict["paths"] = paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        unknown_fields = UnknownFieldSet.from_dict(d.pop("unknownFields"))

        paths = cast(list[str], d.pop("paths", UNSET))

        field_mask = cls(
            unknown_fields=unknown_fields,
            paths=paths,
        )

        field_mask.additional_properties = d
        return field_mask

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
