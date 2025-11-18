from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.js_prepare_submission_response_hashing_scheme_version import (
    JsPrepareSubmissionResponseHashingSchemeVersion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="JsPrepareSubmissionResponse")


@_attrs_define
class JsPrepareSubmissionResponse:
    """[docs-entry-end: HashingSchemeVersion]

    Attributes:
        prepared_transaction_hash (str): Hash of the transaction, this is what needs to be signed by the party to
            authorize the transaction.
            Only provided for convenience, clients MUST recompute the hash from the raw transaction if the preparing
            participant is not trusted.
            May be removed in future versions
        hashing_scheme_version (JsPrepareSubmissionResponseHashingSchemeVersion): The hashing scheme version used when
            building the hash
        prepared_transaction (str | Unset): The interpreted transaction, it represents the ledger changes necessary to
            execute the commands specified in the request.
            Clients MUST display the content of the transaction to the user for them to validate before signing the hash if
            the preparing participant is not trusted.
        hashing_details (str | Unset): Optional additional details on how the transaction was encoded and hashed. Only
            set if verbose_hashing = true in the request
            Note that there are no guarantees on the stability of the format or content of this field.
            Its content should NOT be parsed and should only be used for troubleshooting purposes.
    """

    prepared_transaction_hash: str
    hashing_scheme_version: JsPrepareSubmissionResponseHashingSchemeVersion
    prepared_transaction: str | Unset = UNSET
    hashing_details: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prepared_transaction_hash = self.prepared_transaction_hash

        hashing_scheme_version = self.hashing_scheme_version.value

        prepared_transaction = self.prepared_transaction

        hashing_details = self.hashing_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preparedTransactionHash": prepared_transaction_hash,
                "hashingSchemeVersion": hashing_scheme_version,
            }
        )
        if prepared_transaction is not UNSET:
            field_dict["preparedTransaction"] = prepared_transaction
        if hashing_details is not UNSET:
            field_dict["hashingDetails"] = hashing_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prepared_transaction_hash = d.pop("preparedTransactionHash")

        hashing_scheme_version = JsPrepareSubmissionResponseHashingSchemeVersion(
            d.pop("hashingSchemeVersion")
        )

        prepared_transaction = d.pop("preparedTransaction", UNSET)

        hashing_details = d.pop("hashingDetails", UNSET)

        js_prepare_submission_response = cls(
            prepared_transaction_hash=prepared_transaction_hash,
            hashing_scheme_version=hashing_scheme_version,
            prepared_transaction=prepared_transaction,
            hashing_details=hashing_details,
        )

        js_prepare_submission_response.additional_properties = d
        return js_prepare_submission_response

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
