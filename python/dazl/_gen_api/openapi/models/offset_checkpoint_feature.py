from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration


T = TypeVar("T", bound="OffsetCheckpointFeature")


@_attrs_define
class OffsetCheckpointFeature:
    """
    Attributes:
        max_offset_checkpoint_emission_delay (Duration | Unset):
    """

    max_offset_checkpoint_emission_delay: Duration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_offset_checkpoint_emission_delay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_offset_checkpoint_emission_delay, Unset):
            max_offset_checkpoint_emission_delay = (
                self.max_offset_checkpoint_emission_delay.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_offset_checkpoint_emission_delay is not UNSET:
            field_dict["maxOffsetCheckpointEmissionDelay"] = max_offset_checkpoint_emission_delay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration import Duration

        d = dict(src_dict)
        _max_offset_checkpoint_emission_delay = d.pop("maxOffsetCheckpointEmissionDelay", UNSET)
        max_offset_checkpoint_emission_delay: Duration | Unset
        if isinstance(_max_offset_checkpoint_emission_delay, Unset):
            max_offset_checkpoint_emission_delay = UNSET
        else:
            max_offset_checkpoint_emission_delay = Duration.from_dict(
                _max_offset_checkpoint_emission_delay
            )

        offset_checkpoint_feature = cls(
            max_offset_checkpoint_emission_delay=max_offset_checkpoint_emission_delay,
        )

        offset_checkpoint_feature.additional_properties = d
        return offset_checkpoint_feature

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
