# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from decimal import Decimal

from dazl.prim import decimal_to_str


def test_one():
    assert decimal_to_str(Decimal("1")) == "1"


def test_ten():
    assert decimal_to_str(Decimal("10")) == "10"


def test_one_tenth():
    assert decimal_to_str(Decimal("0.1")) == "0.1"


def test_one_trillionth():
    assert decimal_to_str(Decimal("0.000000000001")) == "0.000000000001"


def test_one_trillion():
    assert decimal_to_str(Decimal("1000000000000")) == "1000000000000"


def test_one_trillionth_and_a_bit():
    assert decimal_to_str(Decimal("0.0000000000011")) == "0.0000000000011"


def test_quarter_quadrillion():
    assert decimal_to_str(Decimal("250000000000000")) == "250000000000000"


def test_quarter_quadrillion_and_a_bit():
    assert (
        decimal_to_str(Decimal("250000000000000.0000000000011")) == "250000000000000.0000000000011"
    )
