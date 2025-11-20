from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_meta import ObjectMeta


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Users and rights
    /////////////////
     Users are used to dynamically manage the rights given to Daml applications.
     They are stored and managed per participant node.

        Attributes:
            id (str): The user identifier, which must be a non-empty string of at most 128
                characters that are either alphanumeric ASCII characters or one of the symbols "@^$.!`-#+'~_|:".
                Required
            primary_party (str): The primary party as which this user reads and acts by default on the ledger
                *provided* it has the corresponding ``CanReadAs(primary_party)`` or
                ``CanActAs(primary_party)`` rights.
                Ledger API clients SHOULD set this field to a non-empty value for all users to
                enable the users to act on the ledger using their own Daml party.
                Users for participant administrators MAY have an associated primary party.
                Optional,
                Modifiable
            is_deactivated (bool): When set, then the user is denied all access to the Ledger API.
                Otherwise, the user has access to the Ledger API as per the user's rights.
                Optional,
                Modifiable
            identity_provider_id (str): The ID of the identity provider configured by ``Identity Provider Config``
                Optional, if not set, assume the user is managed by the default identity provider.
            metadata (ObjectMeta | Unset): Represents metadata corresponding to a participant resource (e.g. a participant
                user or participant local information about a party).

                Based on ``ObjectMeta`` meta used in Kubernetes API.
                See https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/generated.proto#L640
    """

    id: str
    primary_party: str
    is_deactivated: bool
    identity_provider_id: str
    metadata: ObjectMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        primary_party = self.primary_party

        is_deactivated = self.is_deactivated

        identity_provider_id = self.identity_provider_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "primaryParty": primary_party,
                "isDeactivated": is_deactivated,
                "identityProviderId": identity_provider_id,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_meta import ObjectMeta

        d = dict(src_dict)
        id = d.pop("id")

        primary_party = d.pop("primaryParty")

        is_deactivated = d.pop("isDeactivated")

        identity_provider_id = d.pop("identityProviderId")

        _metadata = d.pop("metadata", UNSET)
        metadata: ObjectMeta | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ObjectMeta.from_dict(_metadata)

        user = cls(
            id=id,
            primary_party=primary_party,
            is_deactivated=is_deactivated,
            identity_provider_id=identity_provider_id,
            metadata=metadata,
        )

        user.additional_properties = d
        return user

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
