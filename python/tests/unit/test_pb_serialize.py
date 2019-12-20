# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from typing import Mapping

from dataclasses import dataclass

from dazl import CreateCommand, ExerciseCommand, CreateAndExerciseCommand, ExerciseByKeyCommand, \
    ContractId
from dazl.model.types import TypeReference
from dazl.model.types_store import PackageStore
from dazl.protocols.v1.pb_ser_command import ProtobufSerializer
from dazl.protocols.v1 import model as G
from dazl.util.dar import DarFile
from .dars import Pending


@dataclass(frozen=True)
class DarFixture:
    dar: DarFile
    store: PackageStore

    def get_template_type(self, identifier: str) -> 'TypeReference':
        templates = self.store.resolve_template(identifier)
        for template in templates:
            return template.data_type.name

        raise AssertionError(f'Unknown template name: {identifier!r}')

    def get_identifier(self, identifier: str) -> 'Mapping[str, str]':
        tref = self.get_template_type(identifier)
        return G.Identifier(
            module_name='.'.join(tref.module.module_name),
            entity_name='.'.join(tref.name),
            package_id=tref.module.package_id)


@pytest.fixture(scope='module')
def dar_fixture() -> 'DarFixture':
    with DarFile(Pending) as dar:
        store = dar.read_metadata()

        yield DarFixture(dar, store)


def test_serialize_create(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.store)

    command = CreateCommand('Pending.AccountRequest', dict(owner='SomeParty'))

    expected = G.Command()
    expected.create.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending.AccountRequest'))
    expected.create.create_arguments.fields.append(
        G.RecordField(label='owner', value=G.Value(party='SomeParty')))
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_exercise(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.store)

    tref = dar_fixture.get_template_type('Pending.AccountRequest')
    cid = ContractId('#1:0', tref)
    command = ExerciseCommand(cid, 'CreateAccount', dict(accountId=42))

    expected = G.Command()
    expected.exercise.contract_id = '#1:0'
    expected.exercise.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending.AccountRequest'))
    expected.exercise.choice = 'CreateAccount'
    expected.exercise.choice_argument.record.fields.append(
        G.RecordField(label='accountId', value=G.Value(int64=42)))
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_exercise_by_key(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.store)

    command = ExerciseByKeyCommand('Pending.Counter', 'SomeParty', 'Increment', {})

    expected = G.Command()
    expected.exerciseByKey.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending.Counter'))
    expected.exerciseByKey.contract_key.party = 'SomeParty'
    expected.exerciseByKey.choice = 'Increment'
    expected.exerciseByKey.choice_argument.record.SetInParent()
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_create_and_exercise(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.store)

    command = CreateAndExerciseCommand(
        'Pending.AccountRequest', dict(owner='SomeParty'), 'CreateAccount', dict(accountId=42))

    expected = G.Command()
    expected.createAndExercise.template_id.MergeFrom(
        dar_fixture.get_identifier('Pending.AccountRequest'))
    expected.createAndExercise.create_arguments.fields.append(
        G.RecordField(label='owner', value=G.Value(party='SomeParty')))
    expected.createAndExercise.choice = 'CreateAccount'
    expected.createAndExercise.choice_argument.record.fields.append(
        G.RecordField(label='accountId', value=G.Value(int64=42)))
    actual = sut.serialize_command(command)

    assert expected == actual
