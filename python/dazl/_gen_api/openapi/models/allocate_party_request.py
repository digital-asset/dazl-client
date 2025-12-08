# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_meta import ObjectMeta


T = TypeVar("T", bound="AllocatePartyRequest")


@_attrs_define
class AllocatePartyRequest:
    """Required authorization: ``HasRight(ParticipantAdmin) OR IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``

    Attributes:
        party_id_hint (str): A hint to the participant which party ID to allocate. It can be
            ignored.
            Must be a valid PartyIdString (as described in ``value.proto``).
            Optional
        identity_provider_id (str): The id of the ``Identity Provider``
            Optional, if not set, assume the party is managed by the default identity provider or party is not hosted by the
            participant.
        synchronizer_id (str): The synchronizer, on which the party should be allocated.
            For backwards compatibility, this field may be omitted, if the participant is connected to only one
            synchronizer.
            Otherwise a synchronizer must be specified.
            Optional
        user_id (str): The user who will get the act_as rights to the newly allocated party.
            If set to an empty string (the default), no user will get rights to the party.
            Optional
        local_metadata (ObjectMeta | Unset): Represents metadata corresponding to a participant resource (e.g. a
            participant user or participant local information about a party).

            Based on ``ObjectMeta`` meta used in Kubernetes API.
            See https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/generated.proto#L640
    """

    party_id_hint: str
    identity_provider_id: str
    synchronizer_id: str
    user_id: str
    local_metadata: ObjectMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_id_hint = self.party_id_hint

        identity_provider_id = self.identity_provider_id

        synchronizer_id = self.synchronizer_id

        user_id = self.user_id

        local_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_metadata, Unset):
            local_metadata = self.local_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partyIdHint": party_id_hint,
                "identityProviderId": identity_provider_id,
                "synchronizerId": synchronizer_id,
                "userId": user_id,
            }
        )
        if local_metadata is not UNSET:
            field_dict["localMetadata"] = local_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_meta import ObjectMeta

        d = dict(src_dict)
        party_id_hint = d.pop("partyIdHint")

        identity_provider_id = d.pop("identityProviderId")

        synchronizer_id = d.pop("synchronizerId")

        user_id = d.pop("userId")

        _local_metadata = d.pop("localMetadata", UNSET)
        local_metadata: ObjectMeta | Unset
        if isinstance(_local_metadata, Unset):
            local_metadata = UNSET
        else:
            local_metadata = ObjectMeta.from_dict(_local_metadata)

        allocate_party_request = cls(
            party_id_hint=party_id_hint,
            identity_provider_id=identity_provider_id,
            synchronizer_id=synchronizer_id,
            user_id=user_id,
            local_metadata=local_metadata,
        )

        allocate_party_request.additional_properties = d
        return allocate_party_request

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
