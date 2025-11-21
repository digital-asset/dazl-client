# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.party_details import PartyDetails


T = TypeVar("T", bound="AllocatePartyResponse")


@_attrs_define
class AllocatePartyResponse:
    """
    Attributes:
        party_details (PartyDetails | Unset):
    """

    party_details: PartyDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.party_details, Unset):
            party_details = self.party_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if party_details is not UNSET:
            field_dict["partyDetails"] = party_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_details import PartyDetails

        d = dict(src_dict)
        _party_details = d.pop("partyDetails", UNSET)
        party_details: PartyDetails | Unset
        if isinstance(_party_details, Unset):
            party_details = UNSET
        else:
            party_details = PartyDetails.from_dict(_party_details)

        allocate_party_response = cls(
            party_details=party_details,
        )

        allocate_party_response.additional_properties = d
        return allocate_party_response

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
