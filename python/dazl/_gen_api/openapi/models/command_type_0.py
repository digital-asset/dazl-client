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
    from ..models.create_and_exercise_command import CreateAndExerciseCommand


T = TypeVar("T", bound="CommandType0")


@_attrs_define
class CommandType0:
    """
    Attributes:
        create_and_exercise_command (CreateAndExerciseCommand): Create a contract and exercise a choice on it in the
            same transaction.
    """

    create_and_exercise_command: CreateAndExerciseCommand
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_and_exercise_command = self.create_and_exercise_command.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CreateAndExerciseCommand": create_and_exercise_command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_and_exercise_command import CreateAndExerciseCommand

        d = dict(src_dict)
        create_and_exercise_command = CreateAndExerciseCommand.from_dict(
            d.pop("CreateAndExerciseCommand")
        )

        command_type_0 = cls(
            create_and_exercise_command=create_and_exercise_command,
        )

        command_type_0.additional_properties = d
        return command_type_0

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
