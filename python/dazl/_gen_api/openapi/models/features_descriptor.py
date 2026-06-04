# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

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
        experimental (ExperimentalFeatures): See the feature message definitions for descriptions.
        user_management (UserManagementFeature):
        party_management (PartyManagementFeature):
        offset_checkpoint (OffsetCheckpointFeature):
        package_feature (PackageFeature):
    """

    experimental: ExperimentalFeatures
    user_management: UserManagementFeature
    party_management: PartyManagementFeature
    offset_checkpoint: OffsetCheckpointFeature
    package_feature: PackageFeature
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        experimental = self.experimental.to_dict()

        user_management = self.user_management.to_dict()

        party_management = self.party_management.to_dict()

        offset_checkpoint = self.offset_checkpoint.to_dict()

        package_feature = self.package_feature.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimental": experimental,
                "userManagement": user_management,
                "partyManagement": party_management,
                "offsetCheckpoint": offset_checkpoint,
                "packageFeature": package_feature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experimental_features import ExperimentalFeatures
        from ..models.offset_checkpoint_feature import OffsetCheckpointFeature
        from ..models.package_feature import PackageFeature
        from ..models.party_management_feature import PartyManagementFeature
        from ..models.user_management_feature import UserManagementFeature

        d = dict(src_dict)
        experimental = ExperimentalFeatures.from_dict(d.pop("experimental"))

        user_management = UserManagementFeature.from_dict(d.pop("userManagement"))

        party_management = PartyManagementFeature.from_dict(d.pop("partyManagement"))

        offset_checkpoint = OffsetCheckpointFeature.from_dict(d.pop("offsetCheckpoint"))

        package_feature = PackageFeature.from_dict(d.pop("packageFeature"))

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
