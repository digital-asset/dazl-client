# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VettedPackagesRef")


@_attrs_define
class VettedPackagesRef:
    """A reference to identify one or more packages.

    A reference matches a package if its ``package_id`` matches the package's ID,
    its ``package_name`` matches the package's name, and its ``package_version``
    matches the package's version. If an attribute in the reference is left
    unspecified (i.e. as an empty string), that attribute is treated as a
    wildcard. At a minimum, ``package_id`` or the ``package_name`` must be
    specified.

    If a reference does not match any package, the reference is considered
    unresolved and the entire update request is rejected.

        Attributes:
            package_id (str | Unset): Package's package id must be the same as this field.

                Optional
            package_name (str | Unset): Package's name must be the same as this field.

                Optional
            package_version (str | Unset): Package's version must be the same as this field.

                Optional
    """

    package_id: str | Unset = UNSET
    package_name: str | Unset = UNSET
    package_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        package_name = self.package_name

        package_version = self.package_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_id is not UNSET:
            field_dict["packageId"] = package_id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if package_version is not UNSET:
            field_dict["packageVersion"] = package_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("packageId", UNSET)

        package_name = d.pop("packageName", UNSET)

        package_version = d.pop("packageVersion", UNSET)

        vetted_packages_ref = cls(
            package_id=package_id,
            package_name=package_name,
            package_version=package_version,
        )

        vetted_packages_ref.additional_properties = d
        return vetted_packages_ref

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
