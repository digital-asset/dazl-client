# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IdentityProviderConfig")


@_attrs_define
class IdentityProviderConfig:
    """
    Attributes:
        identity_provider_id (str): The identity provider identifier
            Must be a valid LedgerString (as describe in ``value.proto``).
            Required
        is_deactivated (bool): When set, the callers using JWT tokens issued by this identity provider are denied all
            access
            to the Ledger API.
            Optional,
            Modifiable
        issuer (str): Specifies the issuer of the JWT token.
            The issuer value is a case sensitive URL using the https scheme that contains scheme, host,
            and optionally, port number and path components and no query or fragment components.
            Required
            Modifiable
        jwks_url (str): The JWKS (JSON Web Key Set) URL.
            The Ledger API uses JWKs (JSON Web Keys) from the provided URL to verify that the JWT has been
            signed with the loaded JWK. Only RS256 (RSA Signature with SHA-256) signing algorithm is supported.
            Required
            Modifiable
        audience (str): Specifies the audience of the JWT token.
            When set, the callers using JWT tokens issued by this identity provider are allowed to get an access
            only if the "aud" claim includes the string specified here
            Optional,
            Modifiable
    """

    identity_provider_id: str
    is_deactivated: bool
    issuer: str
    jwks_url: str
    audience: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity_provider_id = self.identity_provider_id

        is_deactivated = self.is_deactivated

        issuer = self.issuer

        jwks_url = self.jwks_url

        audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identityProviderId": identity_provider_id,
                "isDeactivated": is_deactivated,
                "issuer": issuer,
                "jwksUrl": jwks_url,
                "audience": audience,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_provider_id = d.pop("identityProviderId")

        is_deactivated = d.pop("isDeactivated")

        issuer = d.pop("issuer")

        jwks_url = d.pop("jwksUrl")

        audience = d.pop("audience")

        identity_provider_config = cls(
            identity_provider_id=identity_provider_id,
            is_deactivated=is_deactivated,
            issuer=issuer,
            jwks_url=jwks_url,
            audience=audience,
        )

        identity_provider_config.additional_properties = d
        return identity_provider_config

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
