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


T = TypeVar("T", bound="GetPreferredPackagesResponse")


@_attrs_define
class GetPreferredPackagesResponse:
    """
    Attributes:
        package_references (list[PackageReference]): The package references of the preferred packages.
            Must contain one package reference for each requested package-name.

            If you build command submissions whose content depends on the returned
            preferred packages, then we recommend submitting the preferred package-ids
            in the ``package_id_selection_preference`` of the command submission to
            avoid race conditions with concurrent changes of the on-ledger package vetting state.

            Required: must be non-empty
        synchronizer_id (str): The synchronizer for which the package preferences are computed.
            If the synchronizer_id was specified in the request, then it matches the request synchronizer_id.

            Required
    """

    package_references: list[PackageReference]
    synchronizer_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_references = []
        for package_references_item_data in self.package_references:
            package_references_item = package_references_item_data.to_dict()
            package_references.append(package_references_item)

        synchronizer_id = self.synchronizer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageReferences": package_references,
                "synchronizerId": synchronizer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_reference import PackageReference

        d = dict(src_dict)
        package_references = []
        _package_references = d.pop("packageReferences")
        for package_references_item_data in _package_references:
            package_references_item = PackageReference.from_dict(package_references_item_data)

            package_references.append(package_references_item)

        synchronizer_id = d.pop("synchronizerId")

        get_preferred_packages_response = cls(
            package_references=package_references,
            synchronizer_id=synchronizer_id,
        )

        get_preferred_packages_response.additional_properties = d
        return get_preferred_packages_response

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
