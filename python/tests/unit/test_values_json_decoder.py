# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import date, datetime

from dazl.damlast import daml_types as daml
from dazl.damlast.daml_types import con
from dazl.damlast.lookup import MultiPackageLookup
from dazl.damlast.pkgfile import CachedDarFile
from dazl.values import Context, JsonDecoder, JsonEncoder
from tests.unit import dars


def test_basic_json_text():
    ctx = Context(JsonDecoder())
    actual = ctx.convert(daml.Text, "some-text")
    assert actual == "some-text"


def test_json_all_kinds_of():
    """
    Serialize a JSON payload of all kinds of fields.
    """
    lookup = MultiPackageLookup(CachedDarFile(dars.AllKindsOf).archives())
    tt = con(lookup.data_type_name("AllKindsOf:OneOfEverything"))
    ctx = Context(JsonEncoder(), lookup)

    expected = {
        "operator": "Operator",
        "someBoolean": True,
        "someInteger": 10,
        "someDecimal": "10",
        "someMaybe": 10,
        "someMaybeNot": None,
        "someText": "text",
        "someDate": "2000-01-01",
        "someDatetime": "2000-01-01T00:00:00Z",
        "someSimpleList": [1],
        "someSimplePair": {"left": 4, "right": 5},
        "someNestedPair": {"left": {"left": 4, "right": 5}, "right": {"left": 10, "right": 4}},
        "someUglyNesting": {
            "tag": "Both",
            "value": {
                "tag": "Right",
                "value": {"left": {"left": 10, "right": 20}, "right": {"left": 30, "right": 40}},
            },
        },
        "someMeasurement": "5",
        "someEnum": "Green",
        "theUnit": {},
    }

    actual = ctx.convert(
        tt,
        {
            "operator": "Operator",
            "someBoolean": True,
            "someInteger": 10,
            "someDecimal": 10,
            "someMaybe": 10,
            "someMaybeNot": None,
            "someText": "text",
            "someDate": date(2000, 1, 1),
            "someDatetime": datetime(2000, 1, 1),
            "someSimpleList": [1],
            "someSimplePair": {"left": 4, "right": 5},
            "someNestedPair": {"left": {"left": 4, "right": 5}, "right": {"left": 10, "right": 4}},
            "someUglyNesting": {
                "Both": {
                    "Right": {"left": {"left": 10, "right": 20}, "right": {"left": 30, "right": 40}}
                }
            },
            "someMeasurement": 5,
            "someEnum": "Green",
            "theUnit": {},
        },
    )

    assert expected == actual
