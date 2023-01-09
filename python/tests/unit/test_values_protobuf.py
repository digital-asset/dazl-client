# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

from dazl._gen.com.daml.ledger.api import v1 as lapipb
from dazl.damlast import CachedDarFile, daml_types as daml
from dazl.damlast.lookup import MultiPackageLookup
from dazl.values import Context, ProtobufDecoder, ProtobufEncoder
import pytest
from tests.unit import dars

ARBITRARY_DATETIME = datetime(1989, 7, 5, 21, 30, tzinfo=timezone(-timedelta(hours=4)))
ARBITRARY_DATETIME_TIMESTAMP = 615691800000000


@pytest.fixture(scope="package")
def lookup():
    return MultiPackageLookup(CachedDarFile(dars.AllKindsOf).archives())


@pytest.fixture(scope="package")
def encode_context(lookup):
    return Context(ProtobufEncoder(), lookup)


@pytest.fixture(scope="package")
def decode_context(lookup):
    return Context(ProtobufDecoder(), lookup)


def test_values_protobuf_encode_bool_true(encode_context):
    actual = encode_context.convert(daml.Bool, True)
    assert actual == ("bool", True)


def test_values_protobuf_encode_bool_false(encode_context):
    actual = encode_context.convert(daml.Bool, False)
    assert actual == ("bool", False)


def test_values_protobuf_encode_enum(encode_context, lookup):
    color_enum_type = daml.con(lookup.data_type_name("*:AllKindsOf:Color"))
    actual = encode_context.convert(color_enum_type, "Red")
    assert actual == ("enum", lapipb.Enum(constructor="Red"))


def test_values_protobuf_encode_enum_invalid(encode_context, lookup):
    color_enum_type = daml.con(lookup.data_type_name("*:AllKindsOf:Color"))
    try:
        encode_context.convert(color_enum_type, "imagination")
        assert False, "we were supported to fail!"
    except ValueError:
        pass


def test_values_protobuf_encode_numeric(encode_context):
    actual = encode_context.convert(daml.Decimal, "1E+20")
    assert actual == ("numeric", "100000000000000000000")


def test_values_protobuf_encode_numeric_zero(encode_context):
    actual = encode_context.convert(daml.Numeric(0), "1E+20")
    assert actual == ("numeric", "100000000000000000000")


def test_values_protobuf_encode_date(encode_context):
    actual = encode_context.convert(daml.Date, "2020-01-01")
    assert actual == ("date", 18262)


def test_values_protobuf_encode_date_far_in_the_past(encode_context):
    actual = encode_context.convert(daml.Date, "1969-12-31")
    assert actual == ("date", -1)


def test_values_protobuf_encode_datetime(encode_context):
    actual = encode_context.convert(daml.Time, ARBITRARY_DATETIME)
    assert actual == ("timestamp", ARBITRARY_DATETIME_TIMESTAMP)


def test_values_protobuf_decode_date(decode_context):
    value = lapipb.Value()
    value.date = 18262

    actual = decode_context.convert(daml.Date, value)
    assert actual == date(2020, 1, 1)


def test_values_protobuf_decode_date_far_in_the_past(decode_context):
    value = lapipb.Value()
    value.date = -1

    actual = decode_context.convert(daml.Date, value)
    assert actual == date(1969, 12, 31)


def test_values_protobuf_decode_datetime(decode_context):
    value = lapipb.Value()
    value.timestamp = ARBITRARY_DATETIME_TIMESTAMP

    actual = decode_context.convert(daml.Time, value)
    assert actual == ARBITRARY_DATETIME
