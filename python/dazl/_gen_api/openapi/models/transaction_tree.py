# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_transaction_tree import JsTransactionTree


T = TypeVar("T", bound="TransactionTree")


@_attrs_define
class TransactionTree:
    """Provided for backwards compatibility, it will be removed in the Canton version 3.5.0.
    Complete view of an on-ledger transaction.

        Attributes:
            value (JsTransactionTree): Provided for backwards compatibility, it will be removed in the Canton version 3.5.0.
                Complete view of an on-ledger transaction.
    """

    value: JsTransactionTree
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_transaction_tree import JsTransactionTree

        d = dict(src_dict)
        value = JsTransactionTree.from_dict(d.pop("value"))

        transaction_tree = cls(
            value=value,
        )

        transaction_tree.additional_properties = d
        return transaction_tree

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
