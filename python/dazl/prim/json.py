# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import date, datetime
from decimal import Decimal
import json

from .contracts import ContractId
from .datetime import date_to_str, datetime_to_str

__all__ = ["JSONEncoder"]


class JSONEncoder(json.JSONEncoder):
    """
    Convert some known Ledger API primitive types into their appropriate JSON representations.
    """

    def default(self, o):
        if isinstance(o, datetime):
            return datetime_to_str(o)
        elif isinstance(o, date):
            return date_to_str(o)
        elif isinstance(o, ContractId):
            return o.value
        elif isinstance(o, Decimal):
            return str(o)
        elif isinstance(o, UnquotedDecimal):
            return UnquotedDecimal(o)

        return json.JSONEncoder.default(self, o)


class UnquotedDecimal(float):
    """
    A specialized number that is used just for JSON serialization; it suppresses quotes that would
    otherwise appear if ``JSONEncoder.default`` returned a string where it intended to use a number.
    """

    def __new__(cls, decimal_value):
        # noinspection PyArgumentList
        return float.__new__(cls, float(decimal_value))

    def __init__(self, decimal_value):
        float.__init__(float(decimal_value))
        self.decimal_value = decimal_value

    def __repr__(self):
        return str(self.decimal_value)
