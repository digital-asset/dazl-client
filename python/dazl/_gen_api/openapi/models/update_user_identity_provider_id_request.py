from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateUserIdentityProviderIdRequest")


@_attrs_define
class UpdateUserIdentityProviderIdRequest:
    """Required authorization: ``HasRight(ParticipantAdmin)``

    Attributes:
        user_id (str): User to update
        source_identity_provider_id (str): Current identity provider ID of the user
        target_identity_provider_id (str): Target identity provider ID of the user
    """

    user_id: str
    source_identity_provider_id: str
    target_identity_provider_id: str
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
                "sourceIdentityProviderId": source_identity_provider_id,
                "targetIdentityProviderId": target_identity_provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        source_identity_provider_id = d.pop("sourceIdentityProviderId")

        target_identity_provider_id = d.pop("targetIdentityProviderId")

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
