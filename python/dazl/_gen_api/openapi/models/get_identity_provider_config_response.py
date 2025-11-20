from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_config import IdentityProviderConfig


T = TypeVar("T", bound="GetIdentityProviderConfigResponse")


@_attrs_define
class GetIdentityProviderConfigResponse:
    """
    Attributes:
        identity_provider_config (IdentityProviderConfig | Unset):
    """

    identity_provider_config: IdentityProviderConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity_provider_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identity_provider_config, Unset):
            identity_provider_config = self.identity_provider_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity_provider_config is not UNSET:
            field_dict["identityProviderConfig"] = identity_provider_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_config import IdentityProviderConfig

        d = dict(src_dict)
        _identity_provider_config = d.pop("identityProviderConfig", UNSET)
        identity_provider_config: IdentityProviderConfig | Unset
        if isinstance(_identity_provider_config, Unset):
            identity_provider_config = UNSET
        else:
            identity_provider_config = IdentityProviderConfig.from_dict(_identity_provider_config)

        get_identity_provider_config_response = cls(
            identity_provider_config=identity_provider_config,
        )

        get_identity_provider_config_response.additional_properties = d
        return get_identity_provider_config_response

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
