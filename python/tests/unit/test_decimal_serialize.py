from decimal import Decimal

from dazl.util.prim_types import to_ledger_api_decimal


def test_one():
    assert to_ledger_api_decimal(Decimal("1")) == "1"


def test_ten():
    assert to_ledger_api_decimal(Decimal("10")) == "10"


def test_one_tenth():
    assert to_ledger_api_decimal(Decimal("0.1")) == "0.1"


def test_one_trillionth():
    assert to_ledger_api_decimal(Decimal("0.000000000001")) == "0.000000000001"


def test_one_trillion():
    assert to_ledger_api_decimal(Decimal("1000000000000")) == "1000000000000"


def test_one_trillionth_and_a_bit():
    assert to_ledger_api_decimal(Decimal("0.0000000000011")) == "0.0000000000011"


def test_quarter_quadrillion():
    assert to_ledger_api_decimal(Decimal("250000000000000")) == "250000000000000"


def test_quarter_quadrillion_and_a_bit():
    assert to_ledger_api_decimal(Decimal("250000000000000.0000000000011")) == "250000000000000.0000000000011"

