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
    from ..models.js_transaction_tree import JsTransactionTree


T = TypeVar("T", bound="JsSubmitAndWaitForTransactionTreeResponse")


@_attrs_define
class JsSubmitAndWaitForTransactionTreeResponse:
    """Provided for backwards compatibility, it will be removed in the Canton version 3.5.0.

    Attributes:
        transaction_tree (JsTransactionTree | Unset): Provided for backwards compatibility, it will be removed in the
            Canton version 3.5.0.
            Complete view of an on-ledger transaction.
    """

    transaction_tree: JsTransactionTree | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_tree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transaction_tree, Unset):
            transaction_tree = self.transaction_tree.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_tree is not UNSET:
            field_dict["transactionTree"] = transaction_tree

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_transaction_tree import JsTransactionTree

        d = dict(src_dict)
        _transaction_tree = d.pop("transactionTree", UNSET)
        transaction_tree: JsTransactionTree | Unset
        if isinstance(_transaction_tree, Unset):
            transaction_tree = UNSET
        else:
            transaction_tree = JsTransactionTree.from_dict(_transaction_tree)

        js_submit_and_wait_for_transaction_tree_response = cls(
            transaction_tree=transaction_tree,
        )

        js_submit_and_wait_for_transaction_tree_response.additional_properties = d
        return js_submit_and_wait_for_transaction_tree_response

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
