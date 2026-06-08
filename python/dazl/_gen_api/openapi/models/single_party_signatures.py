# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.signature import Signature


T = TypeVar("T", bound="SinglePartySignatures")


@_attrs_define
class SinglePartySignatures:
    """Signatures provided by a single party

    Attributes:
        party (str): Submitting party

            Required
        signatures (list[Signature]): Signatures

            Required: must be non-empty
    """

    party: str
    signatures: list[Signature]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party = self.party

        signatures = []
        for signatures_item_data in self.signatures:
            signatures_item = signatures_item_data.to_dict()
            signatures.append(signatures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "party": party,
                "signatures": signatures,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signature import Signature

        d = dict(src_dict)
        party = d.pop("party")

        signatures = []
        _signatures = d.pop("signatures")
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
