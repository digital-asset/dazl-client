from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experimental_command_inspection_service import (
        ExperimentalCommandInspectionService,
    )
    from ..models.experimental_static_time import ExperimentalStaticTime


T = TypeVar("T", bound="ExperimentalFeatures")


@_attrs_define
class ExperimentalFeatures:
    """See the feature message definitions for descriptions.

    Attributes:
        static_time (ExperimentalStaticTime | Unset): Ledger is in the static time mode and exposes a time service.
        command_inspection_service (ExperimentalCommandInspectionService | Unset): Whether the Ledger API supports
            command inspection service
    """

    static_time: ExperimentalStaticTime | Unset = UNSET
    command_inspection_service: ExperimentalCommandInspectionService | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        static_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.static_time, Unset):
            static_time = self.static_time.to_dict()

        command_inspection_service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.command_inspection_service, Unset):
            command_inspection_service = self.command_inspection_service.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if static_time is not UNSET:
            field_dict["staticTime"] = static_time
        if command_inspection_service is not UNSET:
            field_dict["commandInspectionService"] = command_inspection_service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experimental_command_inspection_service import (
            ExperimentalCommandInspectionService,
        )
        from ..models.experimental_static_time import ExperimentalStaticTime

        d = dict(src_dict)
        _static_time = d.pop("staticTime", UNSET)
        static_time: ExperimentalStaticTime | Unset
        if isinstance(_static_time, Unset):
            static_time = UNSET
        else:
            static_time = ExperimentalStaticTime.from_dict(_static_time)

        _command_inspection_service = d.pop("commandInspectionService", UNSET)
        command_inspection_service: ExperimentalCommandInspectionService | Unset
        if isinstance(_command_inspection_service, Unset):
            command_inspection_service = UNSET
        else:
            command_inspection_service = ExperimentalCommandInspectionService.from_dict(
                _command_inspection_service
            )

        experimental_features = cls(
            static_time=static_time,
            command_inspection_service=command_inspection_service,
        )

        experimental_features.additional_properties = d
        return experimental_features

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
