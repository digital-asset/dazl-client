from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_vetting_requirement import PackageVettingRequirement


T = TypeVar("T", bound="GetPreferredPackagesRequest")


@_attrs_define
class GetPreferredPackagesRequest:
    """
    Attributes:
        synchronizer_id (str): The synchronizer whose vetting state should be used for resolving this query.
            If not specified, the vetting states of all synchronizers to which the participant is connected are used.
            Optional
        package_vetting_requirements (list[PackageVettingRequirement] | Unset): The package-name vetting requirements
            for which the preferred packages should be resolved.

            Generally it is enough to provide the requirements for the intended command's root package-names.
            Additional package-name requirements can be provided when additional Daml transaction informees need to use
            package dependencies of the command's root packages.

            Required
        vetting_valid_at (str | Unset): The timestamp at which the package vetting validity should be computed
            on the latest topology snapshot as seen by the participant.
            If not provided, the participant's current clock time is used.
            Optional
    """

    synchronizer_id: str
    package_vetting_requirements: list[PackageVettingRequirement] | Unset = UNSET
    vetting_valid_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer_id = self.synchronizer_id

        package_vetting_requirements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.package_vetting_requirements, Unset):
            package_vetting_requirements = []
            for (
                package_vetting_requirements_item_data
            ) in self.package_vetting_requirements:
                package_vetting_requirements_item = (
                    package_vetting_requirements_item_data.to_dict()
                )
                package_vetting_requirements.append(package_vetting_requirements_item)

        vetting_valid_at = self.vetting_valid_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizerId": synchronizer_id,
            }
        )
        if package_vetting_requirements is not UNSET:
            field_dict["packageVettingRequirements"] = package_vetting_requirements
        if vetting_valid_at is not UNSET:
            field_dict["vettingValidAt"] = vetting_valid_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_vetting_requirement import PackageVettingRequirement

        d = dict(src_dict)
        synchronizer_id = d.pop("synchronizerId")

        _package_vetting_requirements = d.pop("packageVettingRequirements", UNSET)
        package_vetting_requirements: list[PackageVettingRequirement] | Unset = UNSET
        if _package_vetting_requirements is not UNSET:
            package_vetting_requirements = []
            for package_vetting_requirements_item_data in _package_vetting_requirements:
                package_vetting_requirements_item = PackageVettingRequirement.from_dict(
                    package_vetting_requirements_item_data
                )

                package_vetting_requirements.append(package_vetting_requirements_item)

        vetting_valid_at = d.pop("vettingValidAt", UNSET)

        get_preferred_packages_request = cls(
            synchronizer_id=synchronizer_id,
            package_vetting_requirements=package_vetting_requirements,
            vetting_valid_at=vetting_valid_at,
        )

        get_preferred_packages_request.additional_properties = d
        return get_preferred_packages_request

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
