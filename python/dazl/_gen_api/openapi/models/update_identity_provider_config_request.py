# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.field_mask import FieldMask
    from ..models.identity_provider_config import IdentityProviderConfig


T = TypeVar("T", bound="UpdateIdentityProviderConfigRequest")


@_attrs_define
class UpdateIdentityProviderConfigRequest:
    """
    Attributes:
        identity_provider_config (IdentityProviderConfig):
        update_mask (FieldMask):
    """

    identity_provider_config: IdentityProviderConfig
    update_mask: FieldMask
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity_provider_config = self.identity_provider_config.to_dict()

        update_mask = self.update_mask.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identityProviderConfig": identity_provider_config,
                "updateMask": update_mask,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_mask import FieldMask
        from ..models.identity_provider_config import IdentityProviderConfig

        d = dict(src_dict)
        identity_provider_config = IdentityProviderConfig.from_dict(d.pop("identityProviderConfig"))

        update_mask = FieldMask.from_dict(d.pop("updateMask"))

        update_identity_provider_config_request = cls(
            identity_provider_config=identity_provider_config,
            update_mask=update_mask,
        )

        update_identity_provider_config_request.additional_properties = d
        return update_identity_provider_config_request

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
