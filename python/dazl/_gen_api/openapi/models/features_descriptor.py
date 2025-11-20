from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experimental_features import ExperimentalFeatures
    from ..models.offset_checkpoint_feature import OffsetCheckpointFeature
    from ..models.package_feature import PackageFeature
    from ..models.party_management_feature import PartyManagementFeature
    from ..models.user_management_feature import UserManagementFeature


T = TypeVar("T", bound="FeaturesDescriptor")


@_attrs_define
class FeaturesDescriptor:
    """
    Attributes:
        experimental (ExperimentalFeatures | Unset): See the feature message definitions for descriptions.
        user_management (UserManagementFeature | Unset):
        party_management (PartyManagementFeature | Unset):
        offset_checkpoint (OffsetCheckpointFeature | Unset):
        package_feature (PackageFeature | Unset):
    """

    experimental: ExperimentalFeatures | Unset = UNSET
    user_management: UserManagementFeature | Unset = UNSET
    party_management: PartyManagementFeature | Unset = UNSET
    offset_checkpoint: OffsetCheckpointFeature | Unset = UNSET
    package_feature: PackageFeature | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        experimental: dict[str, Any] | Unset = UNSET
        if not isinstance(self.experimental, Unset):
            experimental = self.experimental.to_dict()

        user_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_management, Unset):
            user_management = self.user_management.to_dict()

        party_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.party_management, Unset):
            party_management = self.party_management.to_dict()

        offset_checkpoint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.offset_checkpoint, Unset):
            offset_checkpoint = self.offset_checkpoint.to_dict()

        package_feature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_feature, Unset):
            package_feature = self.package_feature.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if experimental is not UNSET:
            field_dict["experimental"] = experimental
        if user_management is not UNSET:
            field_dict["userManagement"] = user_management
        if party_management is not UNSET:
            field_dict["partyManagement"] = party_management
        if offset_checkpoint is not UNSET:
            field_dict["offsetCheckpoint"] = offset_checkpoint
        if package_feature is not UNSET:
            field_dict["packageFeature"] = package_feature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experimental_features import ExperimentalFeatures
        from ..models.offset_checkpoint_feature import OffsetCheckpointFeature
        from ..models.package_feature import PackageFeature
        from ..models.party_management_feature import PartyManagementFeature
        from ..models.user_management_feature import UserManagementFeature

        d = dict(src_dict)
        _experimental = d.pop("experimental", UNSET)
        experimental: ExperimentalFeatures | Unset
        if isinstance(_experimental, Unset):
            experimental = UNSET
        else:
            experimental = ExperimentalFeatures.from_dict(_experimental)

        _user_management = d.pop("userManagement", UNSET)
        user_management: UserManagementFeature | Unset
        if isinstance(_user_management, Unset):
            user_management = UNSET
        else:
            user_management = UserManagementFeature.from_dict(_user_management)

        _party_management = d.pop("partyManagement", UNSET)
        party_management: PartyManagementFeature | Unset
        if isinstance(_party_management, Unset):
            party_management = UNSET
        else:
            party_management = PartyManagementFeature.from_dict(_party_management)

        _offset_checkpoint = d.pop("offsetCheckpoint", UNSET)
        offset_checkpoint: OffsetCheckpointFeature | Unset
        if isinstance(_offset_checkpoint, Unset):
            offset_checkpoint = UNSET
        else:
            offset_checkpoint = OffsetCheckpointFeature.from_dict(_offset_checkpoint)

        _package_feature = d.pop("packageFeature", UNSET)
        package_feature: PackageFeature | Unset
        if isinstance(_package_feature, Unset):
            package_feature = UNSET
        else:
            package_feature = PackageFeature.from_dict(_package_feature)

        features_descriptor = cls(
            experimental=experimental,
            user_management=user_management,
            party_management=party_management,
            offset_checkpoint=offset_checkpoint,
            package_feature=package_feature,
        )

        features_descriptor.additional_properties = d
        return features_descriptor

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
