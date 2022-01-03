# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Mappers for translating to and from native Python types.

Documentation for this encoding format can be found at:
https://docs.daml.com/json-api/lf-value-specification.html
"""

from typing import Any

from ..damlast.daml_lf_1 import DefDataType, Type as DamlType
from ..prim import date_to_str, datetime_to_str, decimal_to_str, to_date, to_datetime, to_decimal
from .canonical import CanonicalMapper
from .context import Context

__all__ = ["JsonDecoder", "JsonEncoder"]


class JsonDecoder(CanonicalMapper):
    """
    Convert DAML-LF JSON encoded types into native Python types.

    Note that currently, objects that come back from the HTTP JSON API, so canonicalization is
    completely sufficient.
    """


class JsonEncoder(CanonicalMapper):
    """
    Convert native Python types to DAML-LF JSON encoded types.
    """

    def prim_timestamp(self, context: "Context", obj: "Any") -> "Any":
        return datetime_to_str(to_datetime(obj))

    def prim_date(self, context: "Context", obj: "Any") -> "Any":
        return date_to_str(to_date(obj))

    def prim_contract_id(self, context: "Context", item_type: "DamlType", obj: "Any") -> "Any":
        return obj.contract_id

    def prim_numeric(self, context: "Context", nat: int, obj: "Any") -> "Any":
        d = to_decimal(obj)
        return decimal_to_str(d) if d is not None else None

    def _ctor_value_to_variant(
        self,
        context: "Context",
        dt: "DefDataType",
        variant: "DefDataType.Fields",
        ctor: str,
        value: "Any",
    ) -> "Any":
        """
        Format a variant according to the DAML-LF JSON spec (an object with a "tag" and "value"
        field).
        """
        return {"tag": ctor, "value": value}
