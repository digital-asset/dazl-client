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
    from ..models.vetted_packages import VettedPackages


T = TypeVar("T", bound="UpdateVettedPackagesResponse")


@_attrs_define
class UpdateVettedPackagesResponse:
    """
    Attributes:
        past_vetted_packages (VettedPackages | Unset): The list of packages vetted on a given participant and
            synchronizer, modelled
            after ``VettedPackages`` in `topology.proto <https://github.com/digital-asset/canton/blob/main/community/base/sr
            c/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_.
            The list only contains packages that matched a filter in the query that
            originated it.
        new_vetted_packages (VettedPackages | Unset): The list of packages vetted on a given participant and
            synchronizer, modelled
            after ``VettedPackages`` in `topology.proto <https://github.com/digital-asset/canton/blob/main/community/base/sr
            c/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_.
            The list only contains packages that matched a filter in the query that
            originated it.
    """

    past_vetted_packages: VettedPackages | Unset = UNSET
    new_vetted_packages: VettedPackages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        past_vetted_packages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.past_vetted_packages, Unset):
            past_vetted_packages = self.past_vetted_packages.to_dict()

        new_vetted_packages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_vetted_packages, Unset):
            new_vetted_packages = self.new_vetted_packages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if past_vetted_packages is not UNSET:
            field_dict["pastVettedPackages"] = past_vetted_packages
        if new_vetted_packages is not UNSET:
            field_dict["newVettedPackages"] = new_vetted_packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vetted_packages import VettedPackages

        d = dict(src_dict)
        _past_vetted_packages = d.pop("pastVettedPackages", UNSET)
        past_vetted_packages: VettedPackages | Unset
        if isinstance(_past_vetted_packages, Unset):
            past_vetted_packages = UNSET
        else:
            past_vetted_packages = VettedPackages.from_dict(_past_vetted_packages)

        _new_vetted_packages = d.pop("newVettedPackages", UNSET)
        new_vetted_packages: VettedPackages | Unset
        if isinstance(_new_vetted_packages, Unset):
            new_vetted_packages = UNSET
        else:
            new_vetted_packages = VettedPackages.from_dict(_new_vetted_packages)

        update_vetted_packages_response = cls(
            past_vetted_packages=past_vetted_packages,
            new_vetted_packages=new_vetted_packages,
        )

        update_vetted_packages_response.additional_properties = d
        return update_vetted_packages_response

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
