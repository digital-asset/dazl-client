# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any

from ..damlast.daml_lf_1 import DefDataType, Type as DamlType
from .context import Context
from .mapper import ValueMapper


class PythonSampleEncoder(ValueMapper):
    def __init__(self, max_depth: int = 6):
        self.max_depth = max_depth

    def _recurse(self, context: "Context", key, item_type):
        if context.depth <= self.max_depth:
            return "..."
        else:
            return context.append_path(key).convert(item_type, None)

    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        return {fld.field: self._recurse(context, fld.field, fld.type) for fld in record.fields}
        pass

    def data_variant(
        self, context: "Context", dt: "DefDataType", variant: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        return {fld.field: self._recurse(context, fld.field, fld.type) for fld in variant.fields}

    def data_enum(
        self,
        context: "Context",
        dt: "DefDataType",
        enum: "DefDataType.EnumConstructors",
        obj: "Any",
    ) -> "Any":
        return " | ".join(enum.constructors)

    def prim_unit(self, context: "Context", obj: "Any") -> "Any":
        return "{}"

    def prim_bool(self, context: "Context", obj: "Any") -> "Any":
        return "true | false"

    def prim_int64(self, context: "Context", obj: "Any") -> "Any":
        return "int-value"

    def prim_text(self, context: "Context", obj: "Any") -> "Any":
        return "text-value"

    def prim_timestamp(self, context: "Context", obj: "Any") -> "Any":
        return "timestamp-value"

    def prim_party(self, context: "Context", obj: "Any") -> "Any":
        return "party-value"

    def prim_list(self, context: "Context", item_type: "DamlType", obj: "Any") -> "Any":
        return [self._recurse(context, "[]", item_type)]

    def prim_date(self, context: "Context", obj: "Any") -> "Any":
        return "date-value"

    def prim_contract_id(self, context: "Context", item_type: "DamlType", obj: "Any") -> "Any":
        return "contract-id"

    def prim_optional(self, context: "Context", item_type: "DamlType", obj: "Any") -> "Any":
        return ""

    def prim_text_map(self, context: "Context", item_type: "DamlType", obj: "Any") -> "Any":
        return [self._recurse(context, "[]", item_type)]

    def prim_numeric(self, context: "Context", nat: int, obj: "Any") -> "Any":
        pass

    def prim_gen_map(
        self, context: "Context", key_type: "DamlType", value_type: "DamlType", obj: "Any"
    ) -> "Any":
        return {self._recurse(context, "[]", key_type): self._recurse(context, "[]", value_type)}
