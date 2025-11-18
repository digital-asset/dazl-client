from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyStateFilter")


@_attrs_define
class TopologyStateFilter:
    """Filter the vetted packages by the participant and synchronizer that they are
    hosted on.

    Empty fields are ignored, such that a ``TopologyStateFilter`` without
    participant_ids and without synchronizer_ids matches a vetted package hosted
    on any participant and synchronizer.

    Non-empty fields specify candidate values of which at least one must match.
    If both fields are set then at least one candidate value must match from each
    field.

        Attributes:
            participant_ids (list[str] | Unset): If this list is non-empty, only vetted packages hosted on participants
                listed in this field match the filter.
                Query the current Ledger API's participant's ID via the public
                ``GetParticipantId`` command in ``PartyManagementService``.
            synchronizer_ids (list[str] | Unset): If this list is non-empty, only vetted packages from the topology state of
                the synchronizers in this list match the filter.
    """

    participant_ids: list[str] | Unset = UNSET
    synchronizer_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        participant_ids: list[str] | Unset = UNSET
        if not isinstance(self.participant_ids, Unset):
            participant_ids = self.participant_ids

        synchronizer_ids: list[str] | Unset = UNSET
        if not isinstance(self.synchronizer_ids, Unset):
            synchronizer_ids = self.synchronizer_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if participant_ids is not UNSET:
            field_dict["participantIds"] = participant_ids
        if synchronizer_ids is not UNSET:
            field_dict["synchronizerIds"] = synchronizer_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        participant_ids = cast(list[str], d.pop("participantIds", UNSET))

        synchronizer_ids = cast(list[str], d.pop("synchronizerIds", UNSET))

        topology_state_filter = cls(
            participant_ids=participant_ids,
            synchronizer_ids=synchronizer_ids,
        )

        topology_state_filter.additional_properties = d
        return topology_state_filter

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
