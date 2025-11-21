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
    from ..models.participant_authorization_topology_format import (
        ParticipantAuthorizationTopologyFormat,
    )


T = TypeVar("T", bound="TopologyFormat")


@_attrs_define
class TopologyFormat:
    """A format specifying which topology transactions to include and how to render them.

    Attributes:
        include_participant_authorization_events (ParticipantAuthorizationTopologyFormat | Unset): A format specifying
            which participant authorization topology transactions to include and how to render them.
    """

    include_participant_authorization_events: (
        ParticipantAuthorizationTopologyFormat | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_participant_authorization_events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.include_participant_authorization_events, Unset):
            include_participant_authorization_events = (
                self.include_participant_authorization_events.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_participant_authorization_events is not UNSET:
            field_dict["includeParticipantAuthorizationEvents"] = (
                include_participant_authorization_events
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.participant_authorization_topology_format import (
            ParticipantAuthorizationTopologyFormat,
        )

        d = dict(src_dict)
        _include_participant_authorization_events = d.pop(
            "includeParticipantAuthorizationEvents", UNSET
        )
        include_participant_authorization_events: (
            ParticipantAuthorizationTopologyFormat | Unset
        )
        if isinstance(_include_participant_authorization_events, Unset):
            include_participant_authorization_events = UNSET
        else:
            include_participant_authorization_events = (
                ParticipantAuthorizationTopologyFormat.from_dict(
                    _include_participant_authorization_events
                )
            )

        topology_format = cls(
            include_participant_authorization_events=include_participant_authorization_events,
        )

        topology_format.additional_properties = d
        return topology_format

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
