# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signing_public_key import SigningPublicKey


T = TypeVar("T", bound="GenerateExternalPartyTopologyRequest")


@_attrs_define
class GenerateExternalPartyTopologyRequest:
    """
    Attributes:
        synchronizer (str): TODO(#27670) support synchronizer aliases
            Required: synchronizer-id for which we are building this request.
        party_hint (str): Required: the actual party id will be constructed from this hint and a fingerprint of the
            public key
        local_participant_observation_only (bool): Optional: if true, then the local participant will only be observing,
            not confirming. Default false.
        confirmation_threshold (int): Optional: Confirmation threshold >= 1 for the party. Defaults to all available
            confirmers (or if set to 0).
        public_key (SigningPublicKey | Unset):
        other_confirming_participant_uids (list[str] | Unset): Optional: other participant ids which should be
            confirming for this party
        observing_participant_uids (list[str] | Unset): Optional: other observing participant ids for this party
    """

    synchronizer: str
    party_hint: str
    local_participant_observation_only: bool
    confirmation_threshold: int
    public_key: SigningPublicKey | Unset = UNSET
    other_confirming_participant_uids: list[str] | Unset = UNSET
    observing_participant_uids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer = self.synchronizer

        party_hint = self.party_hint

        local_participant_observation_only = self.local_participant_observation_only

        confirmation_threshold = self.confirmation_threshold

        public_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_key, Unset):
            public_key = self.public_key.to_dict()

        other_confirming_participant_uids: list[str] | Unset = UNSET
        if not isinstance(self.other_confirming_participant_uids, Unset):
            other_confirming_participant_uids = self.other_confirming_participant_uids

        observing_participant_uids: list[str] | Unset = UNSET
        if not isinstance(self.observing_participant_uids, Unset):
            observing_participant_uids = self.observing_participant_uids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizer": synchronizer,
                "partyHint": party_hint,
                "localParticipantObservationOnly": local_participant_observation_only,
                "confirmationThreshold": confirmation_threshold,
            }
        )
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if other_confirming_participant_uids is not UNSET:
            field_dict["otherConfirmingParticipantUids"] = (
                other_confirming_participant_uids
            )
        if observing_participant_uids is not UNSET:
            field_dict["observingParticipantUids"] = observing_participant_uids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signing_public_key import SigningPublicKey

        d = dict(src_dict)
        synchronizer = d.pop("synchronizer")

        party_hint = d.pop("partyHint")

        local_participant_observation_only = d.pop("localParticipantObservationOnly")

        confirmation_threshold = d.pop("confirmationThreshold")

        _public_key = d.pop("publicKey", UNSET)
        public_key: SigningPublicKey | Unset
        if isinstance(_public_key, Unset):
            public_key = UNSET
        else:
            public_key = SigningPublicKey.from_dict(_public_key)

        other_confirming_participant_uids = cast(
            list[str], d.pop("otherConfirmingParticipantUids", UNSET)
        )

        observing_participant_uids = cast(
            list[str], d.pop("observingParticipantUids", UNSET)
        )

        generate_external_party_topology_request = cls(
            synchronizer=synchronizer,
            party_hint=party_hint,
            local_participant_observation_only=local_participant_observation_only,
            confirmation_threshold=confirmation_threshold,
            public_key=public_key,
            other_confirming_participant_uids=other_confirming_participant_uids,
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
