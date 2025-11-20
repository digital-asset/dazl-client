from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="UserManagementFeature")


@_attrs_define
class UserManagementFeature:
    """
    Attributes:
        supported (bool): Whether the Ledger API server provides the user management service.
        max_rights_per_user (int): The maximum number of rights that can be assigned to a single user.
            Servers MUST support at least 100 rights per user.
            A value of 0 means that the server enforces no rights per user limit.
        max_users_page_size (int): The maximum number of users the server can return in a single response (page).
            Servers MUST support at least a 100 users per page.
            A value of 0 means that the server enforces no page size limit.
    """

    supported: bool
    max_rights_per_user: int
    max_users_page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        supported = self.supported

        max_rights_per_user = self.max_rights_per_user

        max_users_page_size = self.max_users_page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supported": supported,
                "maxRightsPerUser": max_rights_per_user,
                "maxUsersPageSize": max_users_page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supported = d.pop("supported")

        max_rights_per_user = d.pop("maxRightsPerUser")

        max_users_page_size = d.pop("maxUsersPageSize")

        user_management_feature = cls(
            supported=supported,
            max_rights_per_user=max_rights_per_user,
            max_users_page_size=max_users_page_size,
        )

        user_management_feature.additional_properties = d
        return user_management_feature

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
