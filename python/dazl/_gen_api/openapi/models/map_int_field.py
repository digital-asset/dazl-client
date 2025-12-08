# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.field import Field


T = TypeVar("T", bound="MapIntField")


@_attrs_define
class MapIntField:
    """ """

    additional_properties: dict[str, Field] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field import Field

        d = dict(src_dict)
        map_int_field = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Field.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        map_int_field.additional_properties = additional_properties
        return map_int_field

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Field:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Field) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
