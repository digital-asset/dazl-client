# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys

from dazl import (
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    ExerciseByKeyCommand,
    ExerciseCommand,
)

if sys.version_info >= (3, 11):
    from typing import assert_never
else:
    from typing_extensions import assert_never

from .test_command import choice, cid, key, payload, template_id


def test_match() -> None:
    commands = list[Command](
        [
            CreateCommand(template_id, payload),
            ExerciseCommand(cid, choice),
            CreateAndExerciseCommand(template_id, payload, choice),
            ExerciseByKeyCommand(template_id, key, choice),
        ]
    )

    found_create = False
    found_exercise = False
    found_create_and_exercise = False
    found_exercise_by_key = False
    for cmd in commands:
        match cmd:
            case CreateCommand(matched_template_id):
                assert template_id == matched_template_id
                found_create = True
            case ExerciseCommand(matched_cid, matched_choice, matched_argument):
                assert cid == matched_cid
                assert choice == matched_choice
                assert matched_argument == {}
                found_exercise = True
            case CreateAndExerciseCommand(matched_template_id, matched_payload, matched_choice):
                assert template_id == matched_template_id
                assert payload == matched_payload
                assert choice == matched_choice
                found_create_and_exercise = True
            case ExerciseByKeyCommand(
                matched_template_id, matched_key, matched_choice, matched_arg
            ):
                assert template_id == matched_template_id
                assert key == matched_key
                assert choice == matched_choice
                assert matched_arg == {}
                found_exercise_by_key = True
            case _:
                assert_never(cmd)

    assert found_create
    assert found_exercise
    assert found_create_and_exercise
    assert found_exercise_by_key
