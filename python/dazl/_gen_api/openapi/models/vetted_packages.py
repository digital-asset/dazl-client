# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

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
            packages (list[VettedPackage]): Sorted by package_name and package_version where known, and package_id as a
                last resort.

                Required: must be non-empty
            participant_id (str): Participant on which these packages are vetted.

                Required
            synchronizer_id (str): Synchronizer on which these packages are vetted.

                Required
            topology_serial (int): Serial of last ``VettedPackages`` topology transaction of this participant
                and on this synchronizer.

                Required
    """

    packages: list[VettedPackage]
    participant_id: str
    synchronizer_id: str
    topology_serial: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)

        participant_id = self.participant_id

        synchronizer_id = self.synchronizer_id

        topology_serial = self.topology_serial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packages": packages,
                "participantId": participant_id,
                "synchronizerId": synchronizer_id,
                "topologySerial": topology_serial,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vetted_package import VettedPackage

        d = dict(src_dict)
        packages = []
        _packages = d.pop("packages")
        for packages_item_data in _packages:
            packages_item = VettedPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        participant_id = d.pop("participantId")

        synchronizer_id = d.pop("synchronizerId")

        topology_serial = d.pop("topologySerial")

        vetted_packages = cls(
            packages=packages,
            participant_id=participant_id,
            synchronizer_id=synchronizer_id,
            topology_serial=topology_serial,
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
