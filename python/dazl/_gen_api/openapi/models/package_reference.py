from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PackageReference")


@_attrs_define
class PackageReference:
    """
    Attributes:
        package_id (str): Required
        package_name (str): Required
        package_version (str): Required
    """

    package_id: str
    package_name: str
    package_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        package_name = self.package_name

        package_version = self.package_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageId": package_id,
                "packageName": package_name,
                "packageVersion": package_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("packageId")

        package_name = d.pop("packageName")

        package_version = d.pop("packageVersion")

        package_reference = cls(
            package_id=package_id,
            package_name=package_name,
            package_version=package_version,
        )

        package_reference.additional_properties = d
        return package_reference

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
