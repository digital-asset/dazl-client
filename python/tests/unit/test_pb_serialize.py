# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import Generator

from dazl._gen.com.daml.ledger.api.v1 import (
    Command as G_Command,
    RecordField as G_RecordField,
    Value as G_Value,
)
from dazl.damlast import DarFile
from dazl.damlast.lookup import MultiPackageLookup
from dazl.damlast.protocols import SymbolLookup
from dazl.ledger import (
    CreateAndExerciseCommand,
    CreateCommand,
    ExerciseByKeyCommand,
    ExerciseCommand,
)
from dazl.ledger.grpc.codec_aio import Codec
from dazl.prim import ContractId, Party
from dazl.protocols.v1.pb_ser_command import ProtobufSerializer
import pytest

from .dars import Pending


@dataclass(frozen=True)
class DarFixture:
    dar: DarFile
    lookup: SymbolLookup

    def get_identifier(self, identifier: str):
        return Codec.encode_identifier(self.lookup.data_type_name(identifier))


@pytest.fixture(scope="module")
def dar_fixture() -> "Generator[DarFixture, None, None]":
    with DarFile(Pending) as dar:
        lookup = MultiPackageLookup(dar.archives())

        yield DarFixture(dar, lookup)


def test_serialize_create(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    command = CreateCommand("Pending:AccountRequest", dict(owner="SomeParty"))

    expected = G_Command()
    expected.create.template_id.MergeFrom(dar_fixture.get_identifier("Pending:AccountRequest"))
    expected.create.create_arguments.fields.append(
        G_RecordField(label="owner", value=G_Value(party=Party("SomeParty")))
    )
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_exercise(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    tref = dar_fixture.lookup.data_type_name("Pending:AccountRequest")
    cid = ContractId(tref, "#1:0")
    command = ExerciseCommand(cid, "CreateAccount", dict(accountId=42))

    expected = G_Command()
    expected.exercise.contract_id = "#1:0"
    expected.exercise.template_id.MergeFrom(dar_fixture.get_identifier("Pending:AccountRequest"))
    expected.exercise.choice = "CreateAccount"
    expected.exercise.choice_argument.record.fields.append(
        G_RecordField(label="accountId", value=G_Value(int64=42))
    )
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_exercise_by_key(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    command = ExerciseByKeyCommand("Pending:Counter", "SomeParty", "Increment", {})

    expected = G_Command()
    expected.exerciseByKey.template_id.MergeFrom(dar_fixture.get_identifier("Pending:Counter"))
    expected.exerciseByKey.contract_key.party = "SomeParty"
    expected.exerciseByKey.choice = "Increment"
    expected.exerciseByKey.choice_argument.record.SetInParent()
    actual = sut.serialize_command(command)

    assert expected == actual


def test_serialize_create_and_exercise(dar_fixture):
    sut = ProtobufSerializer(dar_fixture.lookup)

    command = CreateAndExerciseCommand(
        "Pending:AccountRequest", dict(owner="SomeParty"), "CreateAccount", dict(accountId=42)
    )

    expected = G_Command()
    expected.createAndExercise.template_id.MergeFrom(
        dar_fixture.get_identifier("Pending:AccountRequest")
    )
    expected.createAndExercise.create_arguments.fields.append(
        G_RecordField(label="owner", value=G_Value(party=Party("SomeParty")))
    )
    expected.createAndExercise.choice = "CreateAccount"
    expected.createAndExercise.choice_argument.record.fields.append(
        G_RecordField(label="accountId", value=G_Value(int64=42))
    )
    actual = sut.serialize_command(command)

    assert expected == actual
