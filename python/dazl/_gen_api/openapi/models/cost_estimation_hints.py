# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..models.cost_estimation_hints_expected_signatures_item import (
    CostEstimationHintsExpectedSignaturesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimationHints")


@_attrs_define
class CostEstimationHints:
    """Hints to improve cost estimation precision of a prepared transaction

    Attributes:
        disabled (bool | Unset): Disable cost estimation
            Default (not set) is false

            Optional
        expected_signatures (list[CostEstimationHintsExpectedSignaturesItem] | Unset): Details on the keys that will be
            used to sign the transaction (how many and of which type).
            Signature size impacts the cost of the transaction.
            If empty, the signature sizes will be approximated with threshold-many signatures (where threshold is defined
            in the PartyToParticipant of the external party), using keys in the order they are registered.
            Empty list is equivalent to not providing this field

            Optional: can be empty
    """

    disabled: bool | Unset = UNSET
    expected_signatures: list[CostEstimationHintsExpectedSignaturesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disabled = self.disabled

        expected_signatures: list[str] | Unset = UNSET
        if not isinstance(self.expected_signatures, Unset):
            expected_signatures = []
            for expected_signatures_item_data in self.expected_signatures:
                expected_signatures_item = expected_signatures_item_data.value
                expected_signatures.append(expected_signatures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if expected_signatures is not UNSET:
            field_dict["expectedSignatures"] = expected_signatures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disabled = d.pop("disabled", UNSET)

        _expected_signatures = d.pop("expectedSignatures", UNSET)
        expected_signatures: list[CostEstimationHintsExpectedSignaturesItem] | Unset = UNSET
        if _expected_signatures is not UNSET:
            expected_signatures = []
            for expected_signatures_item_data in _expected_signatures:
                expected_signatures_item = CostEstimationHintsExpectedSignaturesItem(
                    expected_signatures_item_data
                )

                expected_signatures.append(expected_signatures_item)

        cost_estimation_hints = cls(
            disabled=disabled,
            expected_signatures=expected_signatures,
        )

        cost_estimation_hints.additional_properties = d
        return cost_estimation_hints

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
