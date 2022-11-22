# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Mapping, Tuple

from ..damlast.daml_lf_1 import DefDataType, Type
from ..prim import (
    to_bool,
    to_date,
    to_datetime,
    to_decimal,
    to_int,
    to_party,
    to_record,
    to_str,
    to_variant,
)
from .context import Context
from .mapper import ValueMapper

__all__ = ["CanonicalMapper"]


class CanonicalMapper(ValueMapper):
    """
    A mapper that canonicalizes values. If values are already in canonical form, this is essentially
    the identity mapper.

    For container primitives (Optional, List, Map, etc), records, and variants, values are recursed
    and walked through, so subclasses that override :class:`CanonicalMapper` can typically just
    override the primitive methods in order to get slightly different behavior.

    The canonical format of DAML-LF values in dazl was designed specifically to conform as closely
    as possible to simple JSON representations, so the :class:`CanonicalMapper` can also be used to
    decode DAML-LF JSON.
    """

    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        orig_mapping = self._record_to_dict(context, dt, record, obj)

        expected_keys = frozenset(fld.field for fld in record.fields)
        actual_keys = frozenset(orig_mapping)
        if actual_keys.issuperset(expected_keys):
            if actual_keys != expected_keys:
                # Earlier versions were more tolerant of extra fields. To keep backwards
                # compatibility, we'll emit a warning, though this may become an exception
                # eventually.
                context.value_warn(
                    obj, f'extra fields: {", ".join(sorted(actual_keys - expected_keys))}'
                )
        else:
            context.value_error(
                obj, f'missing fields: {", ".join(sorted(expected_keys - actual_keys))}'
            )

        new_mapping = {
            fld.field: context.append_path(fld.field).convert(fld.type, orig_mapping[fld.field])
            for fld in record.fields
        }
        return self._dict_to_record(context, dt, record, new_mapping)

    def data_variant(
        self, context: "Context", dt: "DefDataType", variant: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        ctor, orig_val = self._variant_to_ctor_value(context, dt, variant, obj)
        for fld in variant.fields:
            if fld.field == ctor:
                new_val = context.append_path(fld.field).convert(fld.type, orig_val)
                return self._ctor_value_to_variant(context, dt, variant, ctor, new_val)

        # searched through all fields, and did not find the constructor
        raise ValueError(f"could not find a variant constructor for {ctor}")

    def data_enum(
        self,
        context: "Context",
        dt: "DefDataType",
        enum: "DefDataType.EnumConstructors",
        obj: "Any",
    ) -> "Any":
        return context.value_validate_enum(obj, enum)

    def prim_unit(self, context: "Context", obj: "Any") -> "Any":
        return {}

    def prim_bool(self, context: "Context", obj: "Any") -> "Any":
        return to_bool(obj)

    def prim_int64(self, context: "Context", obj: "Any") -> "Any":
        return to_int(obj)

    def prim_text(self, context: "Context", obj: "Any") -> "Any":
        return to_str(obj)

    def prim_timestamp(self, context: "Context", obj: "Any") -> "Any":
        return to_datetime(obj)

    def prim_party(self, context: "Context", obj: "Any") -> "Any":
        return to_party(obj)

    def prim_list(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return context.convert_list(item_type, obj)

    def prim_date(self, context: "Context", obj: "Any") -> "Any":
        return to_date(obj)

    def prim_contract_id(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return context.convert_contract_id(item_type, obj)

    def prim_optional(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return context.convert_optional(item_type, obj)

    def prim_text_map(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return context.convert_text_map(item_type, obj)

    def prim_numeric(self, context: "Context", nat: int, obj: "Any") -> "Any":
        return to_decimal(obj)

    def prim_gen_map(
        self, context: "Context", key_type: "Type", value_type: "Type", obj: "Any"
    ) -> "Any":
        return obj

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def _record_to_dict(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Mapping[str, Any]":
        """
        Convert a record object to a Python dict. Should be overridden by subclasses to convert a
        record to a dict whose keys are field names and values are associated field values if record
        objects are not always understood to be dicts.

        The default implementation assumes that ``obj`` is already a ``dict`` that matches this
        contract and simply returns it (though this is verified first).
        """
        return to_record(obj)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def _dict_to_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ):
        return obj

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def _variant_to_ctor_value(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Tuple[str, Any]":
        """
        Convert a variant object to a constructor and a value. Should be overridden by subclasses to
        convert a variant that is not formatted in a recognized way.
        """
        return to_variant(obj)

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def _ctor_value_to_variant(
        self,
        context: "Context",
        dt: "DefDataType",
        variant: "DefDataType.Fields",
        ctor: str,
        value: "Any",
    ) -> "Any":
        return {ctor: value}
