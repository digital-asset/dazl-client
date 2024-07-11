# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from unittest import TestCase

from dazl.client.commands import CommandBuilder, CommandDefaults, CommandPayload, create
from dazl.damlast.lookup import parse_type_con_name
from dazl.ledger import CreateCommand, ExerciseCommand
from dazl.prim import ContractId, Party
import pytest

SOME_TEMPLATE_NAME = parse_type_con_name("Sample:Untyped")
SOME_PARTY = Party("SomeParty")
SOME_CONTRACT_ID = ContractId(SOME_TEMPLATE_NAME, "#0:0")
DEFAULTS = CommandDefaults(
    default_party=SOME_PARTY,
    default_ledger_id="some_ledger",
    default_workflow_id="some_workflow",
    default_application_id="some_app",
    default_command_id="some_commands",
)


class TestCommandBuilderTest(TestCase):
    """
    Tests for the various ways that helper objects are converted to :class:`CommandPayload`.
    """

    def test_single_create_untyped(self):
        with pytest.warns(DeprecationWarning):
            expr = create("Sample:Untyped", {"arg": 1})

        expected = [
            CommandPayload(
                party=SOME_PARTY,
                ledger_id=DEFAULTS.default_ledger_id,
                workflow_id=DEFAULTS.default_workflow_id,
                application_id=DEFAULTS.default_application_id,
                command_id=DEFAULTS.default_command_id,
                commands=[CreateCommand(SOME_TEMPLATE_NAME, dict(arg=1))],
            )
        ]

        with pytest.warns(DeprecationWarning):
            actual = CommandBuilder.coerce(expr).build(DEFAULTS)

        assert expected == actual

    def test_object_create_untyped(self):
        with pytest.warns(DeprecationWarning):
            builder = CommandBuilder()
        builder.create("Sample:Untyped", {"arg": 1})

        expected = [
            CommandPayload(
                party=SOME_PARTY,
                ledger_id=DEFAULTS.default_ledger_id,
                workflow_id=DEFAULTS.default_workflow_id,
                application_id=DEFAULTS.default_application_id,
                command_id=DEFAULTS.default_command_id,
                commands=[CreateCommand(SOME_TEMPLATE_NAME, dict(arg=1))],
            )
        ]
        actual = builder.build(DEFAULTS)

        assert expected == actual

    def test_object_atomic_default_false(self):
        with pytest.warns(DeprecationWarning):
            builder = CommandBuilder(atomic_default=False)
        builder.create("Sample:Untyped", {"arg": 1})
        builder.exercise(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"})

        expected = [
            CommandPayload(
                party=SOME_PARTY,
                ledger_id=DEFAULTS.default_ledger_id,
                workflow_id=DEFAULTS.default_workflow_id,
                application_id=DEFAULTS.default_application_id,
                command_id=DEFAULTS.default_command_id,
                commands=[CreateCommand(SOME_TEMPLATE_NAME, dict(arg=1))],
            ),
            CommandPayload(
                party=SOME_PARTY,
                ledger_id=DEFAULTS.default_ledger_id,
                workflow_id=DEFAULTS.default_workflow_id,
                application_id=DEFAULTS.default_application_id,
                command_id=DEFAULTS.default_command_id,
                commands=[ExerciseCommand(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"})],
            ),
        ]

        actual = builder.build(DEFAULTS)

        assert expected == actual

    def test_object_atomic_default_true(self):
        with pytest.warns(DeprecationWarning):
            builder = CommandBuilder(atomic_default=True)
        builder.create("Sample:Untyped", {"arg": 1})
        builder.exercise(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"})

        expected = [
            CommandPayload(
                party=SOME_PARTY,
                ledger_id=DEFAULTS.default_ledger_id,
                workflow_id=DEFAULTS.default_workflow_id,
                application_id=DEFAULTS.default_application_id,
                command_id=DEFAULTS.default_command_id,
                commands=[
                    CreateCommand(SOME_TEMPLATE_NAME, dict(arg=1)),
                    ExerciseCommand(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"}),
                ],
            )
        ]

        actual = builder.build(DEFAULTS)

        assert expected == actual
