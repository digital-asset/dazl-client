# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass
from typing import Generator

from dazl._gen.com.daml.ledger.api import v1 as lapipb
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
import pytest

from .dars import Pending


@dataclass(frozen=True)
class DarFixture:
    dar: DarFile
    lookup: MultiPackageLookup

    def get_identifier(self, identifier: str) -> lapipb.Identifier:
        symbols = self.lookup.search(identifier)
        dt = symbols.data_types.single().package_id_ref
        return Codec.encode_identifier(dt)


@pytest.fixture(scope="module")
def dar_fixture() -> Generator[DarFixture, None, None]:
    with DarFile(Pending) as dar:
        lookup = MultiPackageLookup(dar.archives())

        yield DarFixture(dar, lookup)


@pytest.mark.asyncio
async def test_serialize_create(dar_fixture: DarFixture) -> None:
    sut = Codec(lookup=dar_fixture.lookup)

    command = CreateCommand("Pending:AccountRequest", dict(owner="SomeParty"))

    expected = lapipb.Command()
    expected.create.template_id.MergeFrom(dar_fixture.get_identifier("Pending:AccountRequest"))
    expected.create.create_arguments.fields.append(
        lapipb.RecordField(label="owner", value=lapipb.Value(party=Party("SomeParty")))
    )
    actual = await sut.encode_command(command)

    assert expected == actual


@pytest.mark.asyncio
async def test_serialize_exercise(dar_fixture: DarFixture) -> None:
    sut = Codec(lookup=dar_fixture.lookup)

    symbols = dar_fixture.lookup.search("Pending:AccountRequest")
    tref = symbols.data_types.single().package_id_ref
    cid = ContractId(tref, "#1:0")
    command = ExerciseCommand(cid, "CreateAccount", dict(accountId=42))

    expected = lapipb.Command()
    expected.exercise.contract_id = "#1:0"
    expected.exercise.template_id.MergeFrom(dar_fixture.get_identifier("Pending:AccountRequest"))
    expected.exercise.choice = "CreateAccount"
    expected.exercise.choice_argument.record.fields.append(
        lapipb.RecordField(label="accountId", value=lapipb.Value(int64=42))
    )
    actual = await sut.encode_command(command)

    assert expected == actual


@pytest.mark.asyncio
async def test_serialize_exercise_by_key(dar_fixture: DarFixture) -> None:
    sut = Codec(lookup=dar_fixture.lookup)

    command = ExerciseByKeyCommand("Pending:Counter", "SomeParty", "Increment", {})

    expected = lapipb.Command()
    expected.exerciseByKey.template_id.MergeFrom(dar_fixture.get_identifier("Pending:Counter"))
    expected.exerciseByKey.contract_key.party = "SomeParty"
    expected.exerciseByKey.choice = "Increment"
    expected.exerciseByKey.choice_argument.record.SetInParent()
    actual = await sut.encode_command(command)

    assert expected == actual


@pytest.mark.asyncio
async def test_serialize_create_and_exercise(dar_fixture: DarFixture) -> None:
    sut = Codec(lookup=dar_fixture.lookup)

    command = CreateAndExerciseCommand(
        "Pending:AccountRequest", dict(owner="SomeParty"), "CreateAccount", dict(accountId=42)
    )

    expected = lapipb.Command()
    expected.createAndExercise.template_id.MergeFrom(
        dar_fixture.get_identifier("Pending:AccountRequest")
    )
    expected.createAndExercise.create_arguments.fields.append(
        lapipb.RecordField(label="owner", value=lapipb.Value(party=Party("SomeParty")))
    )
    expected.createAndExercise.choice = "CreateAccount"
    expected.createAndExercise.choice_argument.record.fields.append(
        lapipb.RecordField(label="accountId", value=lapipb.Value(int64=42))
    )
    actual = await sut.encode_command(command)

    assert expected == actual
