from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PackageFeature")


@_attrs_define
class PackageFeature:
    """
    Attributes:
        max_vetted_packages_page_size (int): The maximum number of vetted packages the server can return in a single
            response (page) when listing them.
    """

    max_vetted_packages_page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_vetted_packages_page_size = self.max_vetted_packages_page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxVettedPackagesPageSize": max_vetted_packages_page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_vetted_packages_page_size = d.pop("maxVettedPackagesPageSize")

        package_feature = cls(
            max_vetted_packages_page_size=max_vetted_packages_page_size,
        )

        package_feature.additional_properties = d
        return package_feature

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
