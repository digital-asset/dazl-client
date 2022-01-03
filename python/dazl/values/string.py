# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
from typing import Any

from ..damlast.daml_lf_1 import DefDataType, Type
from ..damlast.util import find_variant_type
from ..prim import (
    date_to_str,
    datetime_to_str,
    decimal_to_str,
    to_bool,
    to_decimal,
    to_int,
    to_party,
    to_str,
    to_variant,
)
from .context import Context
from .mapper import ValueMapper

__all__ = ["FlatStringMapper", "ArrayStringMapper"]


def maybe_parenthesize(value: str) -> str:
    return "(" + value + ")" if " " in value else value


class StringMapperBase(ValueMapper):
    """
    Return string representations of all types in a format that looks closest to their
    representation in DAML.
    """

    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        raise NotImplementedError("StringMapperBase.data_record has no implementation")

    def data_variant(
        self, context: "Context", dt: "DefDataType", variant: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        ctor, value = to_variant(obj)
        obj_type = find_variant_type(dt, variant, ctor)

        value_str = context.append_path(ctor, mapper=FLAT).convert(obj_type, value)
        return f"{ctor} ({maybe_parenthesize(value_str)})"

    def data_enum(
        self,
        context: "Context",
        dt: "DefDataType",
        enum: "DefDataType.EnumConstructors",
        obj: "Any",
    ) -> "Any":
        return context.value_validate_enum(obj, enum)

    def prim_unit(self, context: "Context", obj: "Any") -> "Any":
        return "()"

    def prim_bool(self, context: "Context", obj: "Any") -> "Any":
        return "true" if to_bool(obj) else "false"

    def prim_int64(self, context: "Context", obj: "Any") -> "Any":
        return str(to_int(obj))

    def prim_text(self, context: "Context", obj: "Any") -> "Any":
        """
        Return text formatted as a string, with double quotes.
        """
        return json.dumps(to_str(obj))

    def prim_timestamp(self, context: "Context", obj: "Any") -> "Any":
        return datetime_to_str(obj)

    def prim_party(self, context: "Context", obj: "Any") -> "Any":
        """
        Return a Party literal formatted as a string, with single quotes.
        """
        return repr(to_party(obj))

    def prim_list(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return "[" + ", ".join(context.convert_list(item_type, obj, mapper=FLAT)) + "]"

    def prim_date(self, context: "Context", obj: "Any") -> "Any":
        return date_to_str(obj)

    def prim_contract_id(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return context.convert_contract_id(item_type, obj).value

    def prim_optional(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        if obj is not None:
            value_str = context.convert_optional(item_type, obj, mapper=FLAT)
            if " " in value_str:
                return f"Some ({value_str})"
            else:
                return f"Some {value_str}"
        else:
            return "None"

    def prim_text_map(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return (
            "{"
            + ", ".join(
                json.dumps(key) + ": " + value
                for key, value in context.convert_text_map(item_type, obj, mapper=FLAT).items()
            )
            + "}"
        )

    def prim_numeric(self, context: "Context", nat: int, obj: "Any") -> "Any":
        d = to_decimal(obj)
        return decimal_to_str(d) if d is not None else None

    def prim_gen_map(
        self, context: "Context", key_type: "Type", value_type: "Type", obj: "Any"
    ) -> "Any":
        return (
            "{"
            + ", ".join(
                key + ": " + value
                for key, value in context.convert_gen_map(
                    key_type, value_type, obj, mapper=FLAT
                ).items()
            )
            + "}"
        )


class ArrayStringMapper(StringMapperBase):
    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        """
        Return the fields of this record as an array of strings.
        """
        elems = []
        for field in record.fields:
            val = context.convert(field.type, obj[field.field])
            if isinstance(val, str):
                elems.append(val)
            else:
                elems.extend(val)
        return elems


class FlatStringMapper(StringMapperBase):
    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        if record.fields:
            return "... with " + "; ".join(
                f"{field.field}: {context.convert(field.type, obj[field.field])}"
                for field in record.fields
            )
        else:
            return "..."


FLAT = FlatStringMapper()
