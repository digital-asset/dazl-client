from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantAuthorizationTopologyFormat")


@_attrs_define
class ParticipantAuthorizationTopologyFormat:
    """A format specifying which participant authorization topology transactions to include and how to render them.

    Attributes:
        parties (list[str] | Unset): List of parties for which the topology transactions should be sent.
            Empty means: for all parties.
    """

    parties: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parties: list[str] | Unset = UNSET
        if not isinstance(self.parties, Unset):
            parties = self.parties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parties is not UNSET:
            field_dict["parties"] = parties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parties = cast(list[str], d.pop("parties", UNSET))

        participant_authorization_topology_format = cls(
            parties=parties,
        )

        participant_authorization_topology_format.additional_properties = d
        return participant_authorization_topology_format

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
