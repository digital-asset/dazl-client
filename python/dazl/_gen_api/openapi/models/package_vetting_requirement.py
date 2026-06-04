# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="PackageVettingRequirement")


@_attrs_define
class PackageVettingRequirement:
    """Defines a package-name for which the commonly vetted package with the highest version must be found.

    Attributes:
        parties (list[str]): The parties whose participants' vetting state should be considered when resolving the
            preferred package.

            Required: must be non-empty
        package_name (str): The package-name for which the preferred package should be resolved.

            Required
    """

    parties: list[str]
    package_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parties = self.parties

        package_name = self.package_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parties": parties,
                "packageName": package_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parties = cast(list[str], d.pop("parties"))

        package_name = d.pop("packageName")

        package_vetting_requirement = cls(
            parties=parties,
            package_name=package_name,
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
