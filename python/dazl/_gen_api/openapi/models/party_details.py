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


T = TypeVar("T", bound="PartyDetails")


@_attrs_define
class PartyDetails:
    """
    Attributes:
        party (str): The stable unique identifier of a Daml party.
            Must be a valid PartyIdString (as described in ``value.proto``).
            Required
        is_local (bool): true if party is hosted by the participant and the party shares the same identity provider as
            the user issuing the request.
            Optional
        identity_provider_id (str): The id of the ``Identity Provider``
            Optional, if not set, there could be 3 options:

            1. the party is managed by the default identity provider.
            2. party is not hosted by the participant.
            3. party is hosted by the participant, but is outside of the user's identity provider.
        local_metadata (ObjectMeta | Unset): Represents metadata corresponding to a participant resource (e.g. a
            participant user or participant local information about a party).

            Based on ``ObjectMeta`` meta used in Kubernetes API.
            See https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/generated.proto#L640
    """

    party: str
    is_local: bool
    identity_provider_id: str
    local_metadata: ObjectMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party = self.party

        is_local = self.is_local

        identity_provider_id = self.identity_provider_id

        local_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_metadata, Unset):
            local_metadata = self.local_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "party": party,
                "isLocal": is_local,
                "identityProviderId": identity_provider_id,
            }
        )
        if local_metadata is not UNSET:
            field_dict["localMetadata"] = local_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_meta import ObjectMeta

        d = dict(src_dict)
        party = d.pop("party")

        is_local = d.pop("isLocal")

        identity_provider_id = d.pop("identityProviderId")

        _local_metadata = d.pop("localMetadata", UNSET)
        local_metadata: ObjectMeta | Unset
        if isinstance(_local_metadata, Unset):
            local_metadata = UNSET
        else:
            local_metadata = ObjectMeta.from_dict(_local_metadata)

        party_details = cls(
            party=party,
            is_local=is_local,
            identity_provider_id=identity_provider_id,
            local_metadata=local_metadata,
        )

        party_details.additional_properties = d
        return party_details

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
