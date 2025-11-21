# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SigningPublicKey")


@_attrs_define
class SigningPublicKey:
    """
    Attributes:
        format_ (str): The serialization format of the public key Example:
            CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO.
        key_data (str): Serialized public key in the format specified above
        key_spec (str): The key specification Example: SIGNING_KEY_SPEC_EC_CURVE25519.
    """

    format_: str
    key_data: str
    key_spec: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        key_data = self.key_data

        key_spec = self.key_spec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "keyData": key_data,
                "keySpec": key_spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format")

        key_data = d.pop("keyData")

        key_spec = d.pop("keySpec")

        signing_public_key = cls(
            format_=format_,
            key_data=key_data,
            key_spec=key_spec,
        )

        signing_public_key.additional_properties = d
        return signing_public_key

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
