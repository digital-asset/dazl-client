# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vetted_package import VettedPackage


T = TypeVar("T", bound="VettedPackages")


@_attrs_define
class VettedPackages:
    """The list of packages vetted on a given participant and synchronizer, modelled
    after ``VettedPackages`` in `topology.proto <https://github.com/digital-
    asset/canton/blob/main/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_.
    The list only contains packages that matched a filter in the query that
    originated it.

        Attributes:
            participant_id (str): Participant on which these packages are vetted. Always present.
            synchronizer_id (str): Synchronizer on which these packages are vetted. Always present.
            topology_serial (int): Serial of last ``VettedPackages`` topology transaction of this participant
                and on this synchronizer. Always present.
            packages (list[VettedPackage] | Unset): Sorted by package_name and package_version where known, and package_id
                as a
                last resort.
    """

    participant_id: str
    synchronizer_id: str
    topology_serial: int
    packages: list[VettedPackage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        participant_id = self.participant_id

        synchronizer_id = self.synchronizer_id

        topology_serial = self.topology_serial

        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "participantId": participant_id,
                "synchronizerId": synchronizer_id,
                "topologySerial": topology_serial,
            }
        )
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vetted_package import VettedPackage

        d = dict(src_dict)
        participant_id = d.pop("participantId")

        synchronizer_id = d.pop("synchronizerId")

        topology_serial = d.pop("topologySerial")

        _packages = d.pop("packages", UNSET)
        packages: list[VettedPackage] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = VettedPackage.from_dict(packages_item_data)

                packages.append(packages_item)

        vetted_packages = cls(
            participant_id=participant_id,
            synchronizer_id=synchronizer_id,
            topology_serial=topology_serial,
            packages=packages,
        )

        vetted_packages.additional_properties = d
        return vetted_packages

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
