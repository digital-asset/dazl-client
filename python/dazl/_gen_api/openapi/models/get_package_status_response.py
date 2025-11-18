from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_package_status_response_package_status import (
    GetPackageStatusResponsePackageStatus,
)

T = TypeVar("T", bound="GetPackageStatusResponse")


@_attrs_define
class GetPackageStatusResponse:
    """
    Attributes:
        package_status (GetPackageStatusResponsePackageStatus): The status of the package.
    """

    package_status: GetPackageStatusResponsePackageStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_status = self.package_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageStatus": package_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_status = GetPackageStatusResponsePackageStatus(d.pop("packageStatus"))

        get_package_status_response = cls(
            package_status=package_status,
        )

        get_package_status_response.additional_properties = d
        return get_package_status_response

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
