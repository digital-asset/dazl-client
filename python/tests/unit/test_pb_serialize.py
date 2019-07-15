from pathlib import Path
from typing import ClassVar, Mapping
from unittest import TestCase

from dazl import CreateCommand, ExerciseCommand, CreateAndExerciseCommand, ExerciseByKeyCommand, \
    ContractId
from dazl.model.types import TypeReference
from dazl.model.types_store import PackageStore
from dazl.protocols.v1.pb_ser_command import ProtobufSerializer
from dazl.protocols.v1 import model as G
from dazl.util.dar import TemporaryDar

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'Pending.daml'


class TestProtobufSerialize(TestCase):

    dar: ClassVar[TemporaryDar]
    store: ClassVar[PackageStore]

    @classmethod
    def setUpClass(cls) -> None:
        cls.dar = TemporaryDar(DAML_FILE)
        cls.store = cls.dar.store()
        cls.sut = ProtobufSerializer(cls.store)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.dar.cleanup()

    @classmethod
    def get_template_type(cls, identifier: str) -> 'TypeReference':
        templates = cls.store.resolve_template(identifier)
        for template in templates:
            return template.data_type.name

        raise AssertionError(f'Unknown template name: {identifier!r}')

    @classmethod
    def get_identifier(cls, identifier: str) -> 'Mapping[str, str]':
        tref = TestProtobufSerialize.get_template_type(identifier)
        return G.Identifier(
            module_name='.'.join(tref.module.module_name),
            entity_name='.'.join(tref.name),
            name=tref.full_name,
            package_id=tref.module.package_id)

    def test_serialize_create(self):
        command = CreateCommand('Pending.AccountRequest', dict(owner='SomeParty'))

        expected = G.Command()
        expected.create.template_id.MergeFrom(
            TestProtobufSerialize.get_identifier('Pending.AccountRequest'))
        expected.create.create_arguments.fields.append(
            G.RecordField(label='owner', value=G.Value(party='SomeParty')))
        actual = self.sut.serialize_command(command)

        self.assertEqual(expected, actual)

    def test_serialize_exercise(self):
        tref = TestProtobufSerialize.get_template_type('Pending.AccountRequest')
        cid = ContractId('#1:0', tref)
        command = ExerciseCommand(cid, 'CreateAccount', dict(accountId=42))

        expected = G.Command()
        expected.exercise.contract_id = '#1:0'
        expected.exercise.template_id.MergeFrom(
            TestProtobufSerialize.get_identifier('Pending.AccountRequest'))
        expected.exercise.choice = 'CreateAccount'
        expected.exercise.choice_argument.record.fields.append(
            G.RecordField(label='accountId', value=G.Value(int64=42)))
        actual = self.sut.serialize_command(command)

        self.assertEqual(expected, actual)

    def test_serialize_exercise_by_key(self):
        command = ExerciseByKeyCommand('Pending.Counter', 'SomeParty', 'Increment', {})

        expected = G.Command()
        expected.exerciseByKey.template_id.MergeFrom(
            TestProtobufSerialize.get_identifier('Pending.Counter'))
        expected.exerciseByKey.contract_key.party = 'SomeParty'
        expected.exerciseByKey.choice = 'Increment'
        expected.exerciseByKey.choice_argument.record.SetInParent()
        actual = self.sut.serialize_command(command)

        self.assertEqual(expected, actual)

    def test_serialize_create_and_exercise(self):
        command = CreateAndExerciseCommand(
            'Pending.AccountRequest', dict(owner='SomeParty'), 'CreateAccount', dict(accountId=42))

        expected = G.Command()
        expected.createAndExercise.template_id.MergeFrom(
            TestProtobufSerialize.get_identifier('Pending.AccountRequest'))
        expected.createAndExercise.create_arguments.fields.append(
            G.RecordField(label='owner', value=G.Value(party='SomeParty')))
        expected.createAndExercise.choice = 'CreateAccount'
        expected.createAndExercise.choice_argument.record.fields.append(
            G.RecordField(label='accountId', value=G.Value(int64=42)))
        actual = self.sut.serialize_command(command)

        self.assertEqual(expected, actual)
