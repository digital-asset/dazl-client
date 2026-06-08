# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserIdentityProviderIdRequest")


@_attrs_define
class UpdateUserIdentityProviderIdRequest:
    """Required authorization: ``HasRight(ParticipantAdmin)``

    Attributes:
        user_id (str): User to update

            Required
        source_identity_provider_id (str | Unset): Current identity provider ID of the user
            If omitted, the default IDP is assumed

            Optional
        target_identity_provider_id (str | Unset): Target identity provider ID of the user
            If omitted, the default IDP is assumed

            Optional
    """

    user_id: str
    source_identity_provider_id: str | Unset = UNSET
    target_identity_provider_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        source_identity_provider_id = self.source_identity_provider_id

        target_identity_provider_id = self.target_identity_provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
            }
        )
        if source_identity_provider_id is not UNSET:
            field_dict["sourceIdentityProviderId"] = source_identity_provider_id
        if target_identity_provider_id is not UNSET:
            field_dict["targetIdentityProviderId"] = target_identity_provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        source_identity_provider_id = d.pop("sourceIdentityProviderId", UNSET)

        target_identity_provider_id = d.pop("targetIdentityProviderId", UNSET)

        update_user_identity_provider_id_request = cls(
            user_id=user_id,
            source_identity_provider_id=source_identity_provider_id,
            target_identity_provider_id=target_identity_provider_id,
        )

        update_user_identity_provider_id_request.additional_properties = d
        return update_user_identity_provider_id_request

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
