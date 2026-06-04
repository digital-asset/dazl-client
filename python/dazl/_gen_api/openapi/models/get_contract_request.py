# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetContractRequest")


@_attrs_define
class GetContractRequest:
    """
    Attributes:
        contract_id (str): The ID of the contract.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
        querying_parties (list[str] | Unset): The list of querying parties
            The stakeholders of the referenced contract must have an intersection with any of these parties
            to return the result.
            If no querying_parties specified, all possible contracts could be returned.

            Optional: can be empty
    """

    contract_id: str
    querying_parties: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_id = self.contract_id

        querying_parties: list[str] | Unset = UNSET
        if not isinstance(self.querying_parties, Unset):
            querying_parties = self.querying_parties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contractId": contract_id,
            }
        )
        if querying_parties is not UNSET:
            field_dict["queryingParties"] = querying_parties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_id = d.pop("contractId")

        querying_parties = cast(list[str], d.pop("queryingParties", UNSET))

        get_contract_request = cls(
            contract_id=contract_id,
            querying_parties=querying_parties,
        )

        get_contract_request.additional_properties = d
        return get_contract_request

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
