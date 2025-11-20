from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListPackagesResponse")


@_attrs_define
class ListPackagesResponse:
    """
    Attributes:
        package_ids (list[str] | Unset): The IDs of all Daml-LF packages supported by the server.
            Each element must be a valid PackageIdString (as described in ``value.proto``).
            Required
    """

    package_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_ids: list[str] | Unset = UNSET
        if not isinstance(self.package_ids, Unset):
            package_ids = self.package_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_ids is not UNSET:
            field_dict["packageIds"] = package_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_ids = cast(list[str], d.pop("packageIds", UNSET))

        list_packages_response = cls(
            package_ids=package_ids,
        )

        list_packages_response.additional_properties = d
        return list_packages_response

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
