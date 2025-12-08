# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exercise_command import ExerciseCommand


T = TypeVar("T", bound="CommandType3")


@_attrs_define
class CommandType3:
    """
    Attributes:
        exercise_command (ExerciseCommand): Exercise a choice on an existing contract.
    """

    exercise_command: ExerciseCommand
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercise_command = self.exercise_command.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ExerciseCommand": exercise_command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_command import ExerciseCommand

        d = dict(src_dict)
        exercise_command = ExerciseCommand.from_dict(d.pop("ExerciseCommand"))

        command_type_3 = cls(
            exercise_command=exercise_command,
        )

        command_type_3.additional_properties = d
        return command_type_3

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
