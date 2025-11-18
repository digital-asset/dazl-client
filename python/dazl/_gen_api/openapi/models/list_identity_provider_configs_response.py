from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identity_provider_config import IdentityProviderConfig


T = TypeVar("T", bound="ListIdentityProviderConfigsResponse")


@_attrs_define
class ListIdentityProviderConfigsResponse:
    """
    Attributes:
        identity_provider_configs (list[IdentityProviderConfig] | Unset):
    """

    identity_provider_configs: list[IdentityProviderConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identity_provider_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identity_provider_configs, Unset):
            identity_provider_configs = []
            for identity_provider_configs_item_data in self.identity_provider_configs:
                identity_provider_configs_item = (
                    identity_provider_configs_item_data.to_dict()
                )
                identity_provider_configs.append(identity_provider_configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identity_provider_configs is not UNSET:
            field_dict["identityProviderConfigs"] = identity_provider_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_config import IdentityProviderConfig

        d = dict(src_dict)
        _identity_provider_configs = d.pop("identityProviderConfigs", UNSET)
        identity_provider_configs: list[IdentityProviderConfig] | Unset = UNSET
        if _identity_provider_configs is not UNSET:
            identity_provider_configs = []
            for identity_provider_configs_item_data in _identity_provider_configs:
                identity_provider_configs_item = IdentityProviderConfig.from_dict(
                    identity_provider_configs_item_data
                )

                identity_provider_configs.append(identity_provider_configs_item)

        list_identity_provider_configs_response = cls(
            identity_provider_configs=identity_provider_configs,
        )

        list_identity_provider_configs_response.additional_properties = d
        return list_identity_provider_configs_response

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
