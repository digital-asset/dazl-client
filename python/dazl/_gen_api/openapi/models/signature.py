from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="Signature")


@_attrs_define
class Signature:
    """
    Attributes:
        format_ (str):
        signature (str):
        signed_by (str): The fingerprint/id of the keypair used to create this signature and needed to verify.
        signing_algorithm_spec (str): The signing algorithm specification used to produce this signature
    """

    format_: str
    signature: str
    signed_by: str
    signing_algorithm_spec: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        signature = self.signature

        signed_by = self.signed_by

        signing_algorithm_spec = self.signing_algorithm_spec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "signature": signature,
                "signedBy": signed_by,
                "signingAlgorithmSpec": signing_algorithm_spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format")

        signature = d.pop("signature")

        signed_by = d.pop("signedBy")

        signing_algorithm_spec = d.pop("signingAlgorithmSpec")

        signature = cls(
            format_=format_,
            signature=signature,
            signed_by=signed_by,
            signing_algorithm_spec=signing_algorithm_spec,
        )

        signature.additional_properties = d
        return signature

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
