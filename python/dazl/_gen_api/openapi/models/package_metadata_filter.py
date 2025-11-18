from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageMetadataFilter")


@_attrs_define
class PackageMetadataFilter:
    """Filter the VettedPackages by package metadata.

    A PackageMetadataFilter without package_ids and without package_name_prefixes
    matches any vetted package.

    Non-empty fields specify candidate values of which at least one must match.
    If both fields are set, then a candidate is returned if it matches one of the fields.

        Attributes:
            package_ids (list[str] | Unset): If this list is non-empty, any vetted package with a package ID in this
                list will match the filter.
            package_name_prefixes (list[str] | Unset): If this list is non-empty, any vetted package with a name matching at
                least
                one prefix in this list will match the filter.
    """

    package_ids: list[str] | Unset = UNSET
    package_name_prefixes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_ids: list[str] | Unset = UNSET
        if not isinstance(self.package_ids, Unset):
            package_ids = self.package_ids

        package_name_prefixes: list[str] | Unset = UNSET
        if not isinstance(self.package_name_prefixes, Unset):
            package_name_prefixes = self.package_name_prefixes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_ids is not UNSET:
            field_dict["packageIds"] = package_ids
        if package_name_prefixes is not UNSET:
            field_dict["packageNamePrefixes"] = package_name_prefixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_ids = cast(list[str], d.pop("packageIds", UNSET))

        package_name_prefixes = cast(list[str], d.pop("packageNamePrefixes", UNSET))

        package_metadata_filter = cls(
            package_ids=package_ids,
            package_name_prefixes=package_name_prefixes,
        )

        package_metadata_filter.additional_properties = d
        return package_metadata_filter

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
