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
    from ..models.party_details import PartyDetails


T = TypeVar("T", bound="ListKnownPartiesResponse")


@_attrs_define
class ListKnownPartiesResponse:
    """
    Attributes:
        party_details (list[PartyDetails]): The details of all Daml parties known by the participant.

            Required: must be non-empty
        next_page_token (str | Unset): Pagination token to retrieve the next page.
            Empty, if there are no further results.

            Optional
    """

    party_details: list[PartyDetails]
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_details = []
        for party_details_item_data in self.party_details:
            party_details_item = party_details_item_data.to_dict()
            party_details.append(party_details_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partyDetails": party_details,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_details import PartyDetails

        d = dict(src_dict)
        party_details = []
        _party_details = d.pop("partyDetails")
        for party_details_item_data in _party_details:
            party_details_item = PartyDetails.from_dict(party_details_item_data)

            party_details.append(party_details_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_known_parties_response = cls(
            party_details=party_details,
            next_page_token=next_page_token,
        )

        list_known_parties_response.additional_properties = d
        return list_known_parties_response

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
