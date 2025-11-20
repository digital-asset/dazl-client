from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_preference import PackagePreference


T = TypeVar("T", bound="GetPreferredPackageVersionResponse")


@_attrs_define
class GetPreferredPackageVersionResponse:
    """
    Attributes:
        package_preference (PackagePreference | Unset):
    """

    package_preference: PackagePreference | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_preference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_preference, Unset):
            package_preference = self.package_preference.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_preference is not UNSET:
            field_dict["packagePreference"] = package_preference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_preference import PackagePreference

        d = dict(src_dict)
        _package_preference = d.pop("packagePreference", UNSET)
        package_preference: PackagePreference | Unset
        if isinstance(_package_preference, Unset):
            package_preference = UNSET
        else:
            package_preference = PackagePreference.from_dict(_package_preference)

        get_preferred_package_version_response = cls(
            package_preference=package_preference,
        )

        get_preferred_package_version_response.additional_properties = d
        return get_preferred_package_version_response

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
