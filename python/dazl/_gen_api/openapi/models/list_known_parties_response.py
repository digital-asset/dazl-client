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
        next_page_token (str): Pagination token to retrieve the next page.
            Empty, if there are no further results.
        party_details (list[PartyDetails] | Unset): The details of all Daml parties known by the participant.
            Required
    """

    next_page_token: str
    party_details: list[PartyDetails] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        party_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.party_details, Unset):
            party_details = []
            for party_details_item_data in self.party_details:
                party_details_item = party_details_item_data.to_dict()
                party_details.append(party_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nextPageToken": next_page_token,
            }
        )
        if party_details is not UNSET:
            field_dict["partyDetails"] = party_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_details import PartyDetails

        d = dict(src_dict)
        next_page_token = d.pop("nextPageToken")

        _party_details = d.pop("partyDetails", UNSET)
        party_details: list[PartyDetails] | Unset = UNSET
        if _party_details is not UNSET:
            party_details = []
            for party_details_item_data in _party_details:
                party_details_item = PartyDetails.from_dict(party_details_item_data)

                party_details.append(party_details_item)

        list_known_parties_response = cls(
            next_page_token=next_page_token,
            party_details=party_details,
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
