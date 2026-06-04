# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VettedPackage")


@_attrs_define
class VettedPackage:
    """A package that is vetting on a given participant and synchronizer,
    modelled after ``VettedPackage`` in `topology.proto <https://github.com/digital-
    asset/canton/blob/main/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_,
    enriched with the package name and version.

        Attributes:
            package_id (str): Package ID of this package

                Required
            valid_from_inclusive (str | Unset): The time from which this package is vetted. Empty if vetting time has no
                lower bound.

                Optional
            valid_until_exclusive (str | Unset): The time until which this package is vetted. Empty if vetting time has no
                upper bound.

                Optional
            package_name (str | Unset): Name of this package.
                Only available if the package has been uploaded to the current participant.

                Optional
            package_version (str | Unset): Version of this package.
                Only available if the package has been uploaded to the current participant.

                Optional
    """

    package_id: str
    valid_from_inclusive: str | Unset = UNSET
    valid_until_exclusive: str | Unset = UNSET
    package_name: str | Unset = UNSET
    package_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        valid_from_inclusive = self.valid_from_inclusive

        valid_until_exclusive = self.valid_until_exclusive

        package_name = self.package_name

        package_version = self.package_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageId": package_id,
            }
        )
        if valid_from_inclusive is not UNSET:
            field_dict["validFromInclusive"] = valid_from_inclusive
        if valid_until_exclusive is not UNSET:
            field_dict["validUntilExclusive"] = valid_until_exclusive
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if package_version is not UNSET:
            field_dict["packageVersion"] = package_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("packageId")

        valid_from_inclusive = d.pop("validFromInclusive", UNSET)

        valid_until_exclusive = d.pop("validUntilExclusive", UNSET)

        package_name = d.pop("packageName", UNSET)

        package_version = d.pop("packageVersion", UNSET)

        vetted_package = cls(
            package_id=package_id,
            valid_from_inclusive=valid_from_inclusive,
            valid_until_exclusive=valid_until_exclusive,
            package_name=package_name,
            package_version=package_version,
        )

        vetted_package.additional_properties = d
        return vetted_package

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
