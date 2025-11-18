from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_reference import PackageReference


T = TypeVar("T", bound="PackagePreference")


@_attrs_define
class PackagePreference:
    """
    Attributes:
        synchronizer_id (str): The synchronizer for which the preferred package was computed.
            If the synchronizer_id was specified in the request, then it matches the request synchronizer_id.
            Required
        package_reference (PackageReference | Unset):
    """

    synchronizer_id: str
    package_reference: PackageReference | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer_id = self.synchronizer_id

        package_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_reference, Unset):
            package_reference = self.package_reference.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizerId": synchronizer_id,
            }
        )
        if package_reference is not UNSET:
            field_dict["packageReference"] = package_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_reference import PackageReference

        d = dict(src_dict)
        synchronizer_id = d.pop("synchronizerId")

        _package_reference = d.pop("packageReference", UNSET)
        package_reference: PackageReference | Unset
        if isinstance(_package_reference, Unset):
            package_reference = UNSET
        else:
            package_reference = PackageReference.from_dict(_package_reference)

        package_preference = cls(
            synchronizer_id=synchronizer_id,
            package_reference=package_reference,
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
