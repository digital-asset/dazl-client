from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signature import Signature


T = TypeVar("T", bound="SinglePartySignatures")


@_attrs_define
class SinglePartySignatures:
    """Signatures provided by a single party

    Attributes:
        party (str): Submitting party
            Required
        signatures (list[Signature] | Unset): Signatures
            Required
    """

    party: str
    signatures: list[Signature] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party = self.party

        signatures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.signatures, Unset):
            signatures = []
            for signatures_item_data in self.signatures:
                signatures_item = signatures_item_data.to_dict()
                signatures.append(signatures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "party": party,
            }
        )
        if signatures is not UNSET:
            field_dict["signatures"] = signatures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signature import Signature

        d = dict(src_dict)
        party = d.pop("party")

        _signatures = d.pop("signatures", UNSET)
        signatures: list[Signature] | Unset = UNSET
        if _signatures is not UNSET:
            signatures = []
            for signatures_item_data in _signatures:
                signatures_item = Signature.from_dict(signatures_item_data)

                signatures.append(signatures_item)

        single_party_signatures = cls(
            party=party,
            signatures=signatures,
        )

        single_party_signatures.additional_properties = d
        return single_party_signatures

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
