# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.package_reference import PackageReference


T = TypeVar("T", bound="PackagePreference")


@_attrs_define
class PackagePreference:
    """
    Attributes:
        package_reference (PackageReference):
        synchronizer_id (str): The synchronizer for which the preferred package was computed.
            If the synchronizer_id was specified in the request, then it matches the request synchronizer_id.

            Required
    """

    package_reference: PackageReference
    synchronizer_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_reference = self.package_reference.to_dict()

        synchronizer_id = self.synchronizer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageReference": package_reference,
                "synchronizerId": synchronizer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_reference import PackageReference

        d = dict(src_dict)
        package_reference = PackageReference.from_dict(d.pop("packageReference"))

        synchronizer_id = d.pop("synchronizerId")

        package_preference = cls(
            package_reference=package_reference,
            synchronizer_id=synchronizer_id,
        )

        package_preference.additional_properties = d
        return package_preference

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
