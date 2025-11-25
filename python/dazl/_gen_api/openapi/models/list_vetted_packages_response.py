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
    from ..models.vetted_package import VettedPackage


T = TypeVar("T", bound="ListVettedPackagesResponse")


@_attrs_define
class ListVettedPackagesResponse:
    """
    Attributes:
        next_page_token (str): Pagination token to fetch the next page.
        vetted_packages (list[VettedPackage]): List of vetted packages.
    """

    next_page_token: str
    vetted_packages: list[VettedPackage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        vetted_packages = []
        for vetted_packages_item_data in self.vetted_packages:
            vetted_packages_item = vetted_packages_item_data.to_dict()
            vetted_packages.append(vetted_packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nextPageToken": next_page_token,
                "vettedPackages": vetted_packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vetted_package import VettedPackage

        d = dict(src_dict)
        next_page_token = d.pop("nextPageToken", "")

        vetted_packages = []
        _vetted_packages = d.pop("vettedPackages", [])
        for vetted_packages_item_data in _vetted_packages:
            vetted_packages_item = VettedPackage.from_dict(vetted_packages_item_data)
            vetted_packages.append(vetted_packages_item)

        list_vetted_packages_response = cls(
            next_page_token=next_page_token,
            vetted_packages=vetted_packages,
        )

        list_vetted_packages_response.additional_properties = d
        return list_vetted_packages_response

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
