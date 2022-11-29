# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Ensure that v7 Commands and v8 Commands behave as expected, particularly with respect to
deprecations.
"""

from __future__ import annotations

from dazl.client import commands as v7
from dazl.damlast.lookup import parse_type_con_name
from dazl.ledger import api_types as v8
from dazl.prim import ContractId, Party
import pytest

Operator = Party("Operator")


def test_create_command():
    cmd_v8 = v8.CreateCommand("Mod:Tmpl", {"operator": Operator})

    with pytest.warns(DeprecationWarning):
        cmd_v7 = v7.CreateCommand("Mod:Tmpl", {"operator": Operator})
    with pytest.warns(DeprecationWarning):
        c_payload = cmd_v7.arguments
    with pytest.warns(DeprecationWarning):
        c_deprecated_tt = cmd_v7.template_type

    assert cmd_v8.template_id == cmd_v7.template_id
    assert cmd_v8.payload == cmd_v7.payload == c_payload

    assert str(c_deprecated_tt) == str(cmd_v8.template_id)


def test_create_and_exercise_command_with_implied_unit_arg():
    cmd_v8 = v8.CreateAndExerciseCommand("Mod:Tmpl", {"operator": Operator}, "DoSomething")

    with pytest.warns(DeprecationWarning):
        cmd_v7 = v7.CreateAndExerciseCommand("Mod:Tmpl", {"operator": Operator}, "DoSomething")
    with pytest.warns(DeprecationWarning):
        c_payload = cmd_v7.arguments
    with pytest.warns(DeprecationWarning):
        c_argument_deprecated = cmd_v7.choice_argument
    with pytest.warns(DeprecationWarning):
        c_deprecated_tt = cmd_v7.template_type

    assert cmd_v8.template_id == cmd_v7.template_id
    assert cmd_v8.payload == cmd_v7.payload == c_payload
    assert cmd_v8.choice == cmd_v7.choice
    assert cmd_v8.argument == cmd_v7.argument == c_argument_deprecated == {}
    assert cmd_v8 == cmd_v7

    assert str(c_deprecated_tt) == str(cmd_v8.template_id)


def test_create_and_exercise_command_with_provided_arg():
    cmd_v8 = v8.CreateAndExerciseCommand(
        "Mod:Tmpl", {"operator": Operator}, "DoSomethingWithArg", {"ok": True}
    )

    with pytest.warns(DeprecationWarning):
        cmd_v7 = v7.CreateAndExerciseCommand(
            "Mod:Tmpl", {"operator": Operator}, "DoSomethingWithArg", {"ok": True}
        )
    with pytest.warns(DeprecationWarning):
        c_payload = cmd_v7.arguments
    with pytest.warns(DeprecationWarning):
        c_argument_deprecated = cmd_v7.choice_argument
    with pytest.warns(DeprecationWarning):
        c_deprecated_tt = cmd_v7.template_type

    assert cmd_v8.template_id == cmd_v7.template_id
    assert cmd_v8.payload == cmd_v7.payload == c_payload
    assert cmd_v8.choice == cmd_v7.choice
    assert cmd_v8.argument == cmd_v7.argument == c_argument_deprecated
    assert cmd_v8 == cmd_v7

    assert str(c_deprecated_tt) == str(cmd_v8.template_id)


def test_exercise_command_with_implied_unit_arg():
    cid = ContractId(parse_type_con_name("Mod:Tmpl"), "#0:0")

    cmd_v8 = v8.ExerciseCommand(cid, "DoSomething")

    with pytest.warns(DeprecationWarning):
        cmd_v7 = v7.ExerciseCommand(cid, "DoSomething")
    with pytest.warns(DeprecationWarning):
        c_argument_deprecated = cmd_v7.arguments

    assert cmd_v8.contract_id == cmd_v7.contract_id
    assert cmd_v8.choice == cmd_v7.choice
    assert cmd_v8.argument == cmd_v7.argument == c_argument_deprecated == {}
    assert cmd_v8 == cmd_v7


def test_exercise_command_with_provided_arg():
    cid = ContractId(parse_type_con_name("Mod:Tmpl"), "#0:0")

    cmd_v8 = v8.ExerciseCommand(cid, "DoSomethingWithArg", {"ok": True})

    with pytest.warns(DeprecationWarning):
        cmd_v7 = v7.ExerciseCommand(cid, "DoSomethingWithArg", {"ok": True})
    with pytest.warns(DeprecationWarning):
        c_argument_deprecated = cmd_v7.arguments

    assert cmd_v8.contract_id == cmd_v7.contract_id
    assert cmd_v8.choice == cmd_v7.choice
    assert cmd_v8.argument == cmd_v7.argument == c_argument_deprecated
    assert cmd_v8 == cmd_v7


def test_exercise_by_key_command_with_implied_unit_arg():
    cmd_v8 = v8.ExerciseByKeyCommand("Mod:Tmpl", {"operator": Operator}, "DoSomething")

    with pytest.warns(DeprecationWarning):
        cmd_v7 = v7.ExerciseByKeyCommand("Mod:Tmpl", {"operator": Operator}, "DoSomething")
    with pytest.warns(DeprecationWarning):
        c_key_deprecated = cmd_v7.contract_key
    with pytest.warns(DeprecationWarning):
        c_argument_deprecated = cmd_v7.choice_argument
    with pytest.warns(DeprecationWarning):
        c_deprecated_tt = cmd_v7.template_type

    assert cmd_v8.template_id == cmd_v7.template_id
    assert cmd_v8.key == cmd_v7.key == c_key_deprecated
    assert cmd_v8.choice == cmd_v7.choice
    assert cmd_v8.argument == cmd_v7.argument == c_argument_deprecated == {}
    assert cmd_v8 == cmd_v7

    assert str(c_deprecated_tt) == str(cmd_v8.template_id)


def test_exercise_by_key_command_with_provided_arg():
    cmd_v8 = v8.ExerciseByKeyCommand(
        "Mod:Tmpl", {"operator": Operator}, "DoSomethingWithArg", {"ok": True}
    )

    with pytest.warns(DeprecationWarning):
        cmd_v7 = v7.ExerciseByKeyCommand(
            "Mod:Tmpl", {"operator": Operator}, "DoSomethingWithArg", {"ok": True}
        )
    with pytest.warns(DeprecationWarning):
        c_key_deprecated = cmd_v7.contract_key
    with pytest.warns(DeprecationWarning):
        c_argument_deprecated = cmd_v7.choice_argument
    with pytest.warns(DeprecationWarning):
        c_deprecated_tt = cmd_v7.template_type

    assert cmd_v8.template_id == cmd_v7.template_id
    assert cmd_v8.key == cmd_v7.key == c_key_deprecated
    assert cmd_v8.choice == cmd_v7.choice
    assert cmd_v8.argument == cmd_v7.argument == c_argument_deprecated
    assert cmd_v8 == cmd_v7

    assert str(c_deprecated_tt) == str(cmd_v8.template_id)
