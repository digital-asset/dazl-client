# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from unittest import TestCase

from dazl.model.core import ContractId, Party
from dazl.model.types import UnresolvedTypeReference
from dazl.model.writing import create, CommandBuilder, CommandDefaults, CommandPayload, CreateCommand, \
    ExerciseCommand

SOME_PARTY = Party('SomeParty')
SOME_CONTRACT_ID = ContractId('#0:0', UnresolvedTypeReference('Sample.Untyped'))
DEFAULTS = CommandDefaults(
    default_party=SOME_PARTY,
    default_ledger_id='some_ledger',
    default_workflow_id='some_workflow',
    default_application_id='some_app',
    default_command_id='some_commands')


class TestCommandBuilderTest(TestCase):
    """
    Tests for the various ways that helper objects are converted to :class:`CommandPayload`.
    """

    def test_single_create_untyped(self):
        expr = create('Sample.Untyped', {"arg": 1})

        expected = [CommandPayload(
            party=SOME_PARTY,
            ledger_id=DEFAULTS.default_ledger_id,
            workflow_id=DEFAULTS.default_workflow_id,
            application_id=DEFAULTS.default_application_id,
            command_id=DEFAULTS.default_command_id,
            commands=[CreateCommand(UnresolvedTypeReference('Sample.Untyped'), dict(arg=1))]
        )]
        actual = CommandBuilder.coerce(expr).build(DEFAULTS)

        assert expected == actual

    def test_object_create_untyped(self):
        builder = CommandBuilder()
        builder.create('Sample.Untyped', {"arg": 1})

        expected = [CommandPayload(
            party=SOME_PARTY,
            ledger_id=DEFAULTS.default_ledger_id,
            workflow_id=DEFAULTS.default_workflow_id,
            application_id=DEFAULTS.default_application_id,
            command_id=DEFAULTS.default_command_id,
            commands=[CreateCommand(UnresolvedTypeReference('Sample.Untyped'), dict(arg=1))]
        )]
        actual = builder.build(DEFAULTS)

        assert expected == actual

    def test_object_atomic_default_false(self):
        builder = CommandBuilder(atomic_default=False)
        builder.create('Sample.Untyped', {"arg": 1})
        builder.exercise(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"})

        expected = [
            CommandPayload(
                party=SOME_PARTY,
                ledger_id=DEFAULTS.default_ledger_id,
                workflow_id=DEFAULTS.default_workflow_id,
                application_id=DEFAULTS.default_application_id,
                command_id=DEFAULTS.default_command_id,
                commands=[CreateCommand(UnresolvedTypeReference('Sample.Untyped'), dict(arg=1))]),
            CommandPayload(
                party=SOME_PARTY,
                ledger_id=DEFAULTS.default_ledger_id,
                workflow_id=DEFAULTS.default_workflow_id,
                application_id=DEFAULTS.default_application_id,
                command_id=DEFAULTS.default_command_id,
                commands=[ExerciseCommand(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"})])
        ]

        actual = builder.build(DEFAULTS)

        assert expected == actual

    def test_object_atomic_default_true(self):
        builder = CommandBuilder(atomic_default=True)
        builder.create('Sample.Untyped', {"arg": 1})
        builder.exercise(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"})

        expected = [CommandPayload(
            party=SOME_PARTY,
            ledger_id=DEFAULTS.default_ledger_id,
            workflow_id=DEFAULTS.default_workflow_id,
            application_id=DEFAULTS.default_application_id,
            command_id=DEFAULTS.default_command_id,
            commands=[
                CreateCommand(UnresolvedTypeReference('Sample.Untyped'), dict(arg=1)),
                ExerciseCommand(SOME_CONTRACT_ID, "SomeChoice", {"choiceArg": "value"})
            ]
        )]

        actual = builder.build(DEFAULTS)

        assert expected == actual
