# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageVettingRequirement")


@_attrs_define
class PackageVettingRequirement:
    """Defines a package-name for which the commonly vetted package with the highest version must be found.

    Attributes:
        package_name (str): The package-name for which the preferred package should be resolved.
            Required
        parties (list[str] | Unset): The parties whose participants' vetting state should be considered when resolving
            the preferred package.
            Required
    """

    package_name: str
    parties: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_name = self.package_name

        parties: list[str] | Unset = UNSET
        if not isinstance(self.parties, Unset):
            parties = self.parties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageName": package_name,
            }
        )
        if parties is not UNSET:
            field_dict["parties"] = parties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_name = d.pop("packageName")

        parties = cast(list[str], d.pop("parties", UNSET))

        package_vetting_requirement = cls(
            package_name=package_name,
            parties=parties,
        )

        package_vetting_requirement.additional_properties = d
        return package_vetting_requirement

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
