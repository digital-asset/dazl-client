# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from typing import Mapping

from dataclasses import dataclass

from dazl import CreateCommand, ExerciseCommand, CreateAndExerciseCommand, ExerciseByKeyCommand
from dazl.damlast import DarFile
from dazl.damlast.lookup import MultiPackageLookup
from dazl.damlast.protocols import SymbolLookup
from dazl.prim import ContractId
from dazl.protocols.v1.pb_ser_command import ProtobufSerializer, as_identifier
from dazl.protocols.v1 import model as G
from .dars import Pending


@dataclass(frozen=True)
class DarFixture:
    dar: DarFile
    lookup: SymbolLookup

    def get_identifier(self, identifier: str) -> 'Mapping[str, str]':
        return as_identifier(self.lookup.data_type_name(identifier))


@pytest.fixture(scope='module')
def dar_fixture() -> 'DarFixture':
    with DarFile(Pending) as dar:
        lookup = MultiPackageLookup(dar.archives())

        yield DarFixture(dar, lookup)


def test_serialize_create(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    command = CreateCommand('Pending:AccountRequest', dict(owner='SomeParty'))

    expected = G.Command()
    expected.create.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending:AccountRequest'))
    expected.create.create_arguments.fields.append(
        G.RecordField(label='owner', value=G.Value(party='SomeParty')))
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_exercise(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    tref = dar_fixture.lookup.data_type_name('Pending:AccountRequest')
    cid = ContractId(tref, '#1:0')
    command = ExerciseCommand(cid, 'CreateAccount', dict(accountId=42))

    expected = G.Command()
    expected.exercise.contract_id = '#1:0'
    expected.exercise.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending:AccountRequest'))
    expected.exercise.choice = 'CreateAccount'
    expected.exercise.choice_argument.record.fields.append(
        G.RecordField(label='accountId', value=G.Value(int64=42)))
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_exercise_by_key(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    command = ExerciseByKeyCommand('Pending:Counter', 'SomeParty', 'Increment', {})

    expected = G.Command()
    expected.exerciseByKey.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending:Counter'))
    expected.exerciseByKey.contract_key.party = 'SomeParty'
    expected.exerciseByKey.choice = 'Increment'
    expected.exerciseByKey.choice_argument.record.SetInParent()
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_create_and_exercise(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    command = CreateAndExerciseCommand(
        'Pending:AccountRequest', dict(owner='SomeParty'), 'CreateAccount', dict(accountId=42))

    expected = G.Command()
    expected.createAndExercise.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending:AccountRequest'))
    expected.createAndExercise.create_arguments.fields.append(
        G.RecordField(label='owner', value=G.Value(party='SomeParty')))
    expected.createAndExercise.choice = 'CreateAccount'
    expected.createAndExercise.choice_argument.record.fields.append(
        G.RecordField(label='accountId', value=G.Value(int64=42)))
    actual = sut.serialize_command(command)

    assert expected == actual
