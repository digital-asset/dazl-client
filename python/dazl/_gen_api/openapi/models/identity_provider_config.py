# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderConfig")


@_attrs_define
class IdentityProviderConfig:
    """
    Attributes:
        identity_provider_id (str): The identity provider identifier
            Must be a valid LedgerString (as describe in ``value.proto``).

            Required
        issuer (str): Specifies the issuer of the JWT token.
            The issuer value is a case sensitive URL using the https scheme that contains scheme, host,
            and optionally, port number and path components and no query or fragment components.
            Modifiable

            Can be left empty when used in `UpdateIdentityProviderConfigRequest` if the issuer is not being updated.

            Required
        jwks_url (str): The JWKS (JSON Web Key Set) URL.
            The Ledger API uses JWKs (JSON Web Keys) from the provided URL to verify that the JWT has been
            signed with the loaded JWK. Only RS256 (RSA Signature with SHA-256) signing algorithm is supported.
            Modifiable

            Required
        is_deactivated (bool | Unset): When set, the callers using JWT tokens issued by this identity provider are
            denied all access
            to the Ledger API.
            Modifiable

            Optional
        audience (str | Unset): Specifies the audience of the JWT token.
            When set, the callers using JWT tokens issued by this identity provider are allowed to get an access
            only if the "aud" claim includes the string specified here
            Modifiable

            Optional
    """

    identity_provider_id: str
    issuer: str
    jwks_url: str
    is_deactivated: bool | Unset = UNSET
    audience: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity_provider_id = self.identity_provider_id

        issuer = self.issuer

        jwks_url = self.jwks_url

        is_deactivated = self.is_deactivated

        audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identityProviderId": identity_provider_id,
                "issuer": issuer,
                "jwksUrl": jwks_url,
            }
        )
        if is_deactivated is not UNSET:
            field_dict["isDeactivated"] = is_deactivated
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identity_provider_id = d.pop("identityProviderId")

        issuer = d.pop("issuer")

        jwks_url = d.pop("jwksUrl")

        is_deactivated = d.pop("isDeactivated", UNSET)

        audience = d.pop("audience", UNSET)

        identity_provider_config = cls(
            identity_provider_id=identity_provider_id,
            issuer=issuer,
            jwks_url=jwks_url,
            is_deactivated=is_deactivated,
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
