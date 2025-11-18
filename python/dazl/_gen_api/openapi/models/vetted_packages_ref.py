from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
            package_id (str): Package's package id must be the same as this field.
                Optional
            package_name (str): Package's name must be the same as this field.
                Optional
            package_version (str): Package's version must be the same as this field.
                Optional
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
