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
    from ..models.exercise_by_key_command import ExerciseByKeyCommand


T = TypeVar("T", bound="CommandType2")


@_attrs_define
class CommandType2:
    """
    Attributes:
        exercise_by_key_command (ExerciseByKeyCommand): Exercise a choice on an existing contract specified by its key.
    """

    exercise_by_key_command: ExerciseByKeyCommand
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercise_by_key_command = self.exercise_by_key_command.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ExerciseByKeyCommand": exercise_by_key_command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_by_key_command import ExerciseByKeyCommand

        d = dict(src_dict)
        exercise_by_key_command = ExerciseByKeyCommand.from_dict(
            d.pop("ExerciseByKeyCommand")
        )

        command_type_2 = cls(
            exercise_by_key_command=exercise_by_key_command,
        )

        command_type_2.additional_properties = d
        return command_type_2

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
