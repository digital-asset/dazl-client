from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_transaction import JsTransaction


T = TypeVar("T", bound="JsExecuteSubmissionAndWaitForTransactionResponse")


@_attrs_define
class JsExecuteSubmissionAndWaitForTransactionResponse:
    """
    Attributes:
        transaction (JsTransaction): Filtered view of an on-ledger transaction's create and archive events.
    """

    transaction: JsTransaction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction = self.transaction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction": transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_transaction import JsTransaction

        d = dict(src_dict)
        transaction = JsTransaction.from_dict(d.pop("transaction"))

        js_execute_submission_and_wait_for_transaction_response = cls(
            transaction=transaction,
        )

        js_execute_submission_and_wait_for_transaction_response.additional_properties = d
        return js_execute_submission_and_wait_for_transaction_response

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
