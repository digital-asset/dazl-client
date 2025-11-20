from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_mask import FieldMask
    from ..models.user import User


T = TypeVar("T", bound="UpdateUserRequest")


@_attrs_define
class UpdateUserRequest:
    """Required authorization: ``HasRight(ParticipantAdmin) OR
    IsAuthenticatedIdentityProviderAdmin(user.identity_provider_id)``

        Attributes:
            user (User | Unset):  Users and rights
                /////////////////
                 Users are used to dynamically manage the rights given to Daml applications.
                 They are stored and managed per participant node.
            update_mask (FieldMask | Unset):
    """

    user: User | Unset = UNSET
    update_mask: FieldMask | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        update_mask: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_mask, Unset):
            update_mask = self.update_mask.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if update_mask is not UNSET:
            field_dict["updateMask"] = update_mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_mask import FieldMask
        from ..models.user import User

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _update_mask = d.pop("updateMask", UNSET)
        update_mask: FieldMask | Unset
        if isinstance(_update_mask, Unset):
            update_mask = UNSET
        else:
            update_mask = FieldMask.from_dict(_update_mask)

        update_user_request = cls(
            user=user,
            update_mask=update_mask,
        )

        update_user_request.additional_properties = d
        return update_user_request

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
