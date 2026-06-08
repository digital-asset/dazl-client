# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signing_public_key import SigningPublicKey


T = TypeVar("T", bound="GenerateExternalPartyTopologyRequest")


@_attrs_define
class GenerateExternalPartyTopologyRequest:
    """
    Attributes:
        synchronizer (str): Synchronizer-id for which we are building this request.
            TODO(#27670) support synchronizer aliases

            Required
        party_hint (str): The actual party id will be constructed from this hint and a fingerprint of the public key

            Required
        public_key (SigningPublicKey):
        local_participant_observation_only (bool | Unset): If true, then the local participant will only be observing,
            not confirming. Default false.

            Optional
        other_confirming_participant_uids (list[str] | Unset): Other participant ids which should be confirming for this
            party

            Optional: can be empty
        confirmation_threshold (int | Unset): Confirmation threshold >= 1 for the party. Defaults to all available
            confirmers (or if set to 0).

            Optional
        observing_participant_uids (list[str] | Unset): Other observing participant ids for this party

            Optional: can be empty
    """

    synchronizer: str
    party_hint: str
    public_key: SigningPublicKey
    local_participant_observation_only: bool | Unset = UNSET
    other_confirming_participant_uids: list[str] | Unset = UNSET
    confirmation_threshold: int | Unset = UNSET
    observing_participant_uids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer = self.synchronizer

        party_hint = self.party_hint

        public_key = self.public_key.to_dict()

        local_participant_observation_only = self.local_participant_observation_only

        other_confirming_participant_uids: list[str] | Unset = UNSET
        if not isinstance(self.other_confirming_participant_uids, Unset):
            other_confirming_participant_uids = self.other_confirming_participant_uids

        confirmation_threshold = self.confirmation_threshold

        observing_participant_uids: list[str] | Unset = UNSET
        if not isinstance(self.observing_participant_uids, Unset):
            observing_participant_uids = self.observing_participant_uids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizer": synchronizer,
                "partyHint": party_hint,
                "publicKey": public_key,
            }
        )
        if local_participant_observation_only is not UNSET:
            field_dict["localParticipantObservationOnly"] = local_participant_observation_only
        if other_confirming_participant_uids is not UNSET:
            field_dict["otherConfirmingParticipantUids"] = other_confirming_participant_uids
        if confirmation_threshold is not UNSET:
            field_dict["confirmationThreshold"] = confirmation_threshold
        if observing_participant_uids is not UNSET:
            field_dict["observingParticipantUids"] = observing_participant_uids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signing_public_key import SigningPublicKey

        d = dict(src_dict)
        synchronizer = d.pop("synchronizer")

        party_hint = d.pop("partyHint")

        public_key = SigningPublicKey.from_dict(d.pop("publicKey"))

        local_participant_observation_only = d.pop("localParticipantObservationOnly", UNSET)

        other_confirming_participant_uids = cast(
            list[str], d.pop("otherConfirmingParticipantUids", UNSET)
        )

        confirmation_threshold = d.pop("confirmationThreshold", UNSET)

        observing_participant_uids = cast(list[str], d.pop("observingParticipantUids", UNSET))

        generate_external_party_topology_request = cls(
            synchronizer=synchronizer,
            party_hint=party_hint,
            public_key=public_key,
            local_participant_observation_only=local_participant_observation_only,
            other_confirming_participant_uids=other_confirming_participant_uids,
            confirmation_threshold=confirmation_threshold,
            observing_participant_uids=observing_participant_uids,
        )

        generate_external_party_topology_request.additional_properties = d
        return generate_external_party_topology_request

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
