# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import collections.abc
from typing import Any, Optional, Type as PyType, TypeVar

from google.protobuf import timestamp_pb2
from google.protobuf.empty_pb2 import Empty

from .._gen.com.daml.ledger.api import v1 as lapipb
from ..damlast.daml_lf_1 import DefDataType, Type
from ..damlast.util import find_variant_type
from ..prim import (
    FrozenDict,
    date_to_int,
    datetime_to_epoch_microseconds,
    decimal_to_str,
    to_bool,
    to_date,
    to_datetime,
    to_decimal,
    to_int,
    to_party,
    to_str,
    to_variant,
)
from .context import Context
from .mapper import ValueMapper

__all__ = ["ProtobufDecoder", "ProtobufEncoder", "get_value", "set_value"]

T = TypeVar("T")


class ProtobufDecoder(ValueMapper):
    """
    Convert value_pb2.Value (or any of its cases) to a native Python type.

    This mapper also handles:
     * re-typing ContractIds (they come over the Ledger API without their type parameter)
     * non-verbose Ledger API record values (field names are omitted for message brevity, meaning
       they can only be understood in a generic way by knowing the metadata associated with the
       object ahead of time)
    """

    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        msg = get_value(obj, "record", lapipb.Record)

        d = dict()
        for fld_metadata, fld_data in zip(record.fields, msg.fields):
            name = fld_metadata.field
            value = context.append_path(name).convert(fld_metadata.type, fld_data.value)
            d[name] = value

        return d

    def data_variant(
        self, context: "Context", dt: "DefDataType", variant: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        msg = get_value(obj, "variant", lapipb.Variant)
        obj_ctor = msg.constructor
        obj_value = msg.value
        obj_type = find_variant_type(dt, variant, obj_ctor)

        d_value = context.append_path(obj_ctor).convert(obj_type, obj_value)

        return {obj_ctor: d_value}

    def data_enum(
        self,
        context: "Context",
        dt: "DefDataType",
        enum: "DefDataType.EnumConstructors",
        obj: "Any",
    ) -> "Any":
        msg = get_value(obj, "enum", lapipb.Enum)
        return context.value_validate_enum(msg.constructor, enum)

    def prim_unit(self, context: "Context", obj: "Any") -> "Any":
        return {}

    def prim_bool(self, context: "Context", obj: "Any") -> "Any":
        return get_value(obj, "bool", bool)

    def prim_int64(self, context: "Context", obj: "Any") -> "Any":
        return get_value(obj, "int64", int)

    def prim_text(self, context: "Context", obj: "Any") -> "Any":
        return get_value(obj, "text", str)

    def prim_timestamp(self, context: "Context", obj: "Any") -> "Any":
        return to_datetime(get_value(obj, "timestamp", timestamp_pb2.Timestamp))

    def prim_party(self, context: "Context", obj: "Any") -> "Any":
        return to_party(get_value(obj, "party", str))

    def prim_list(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        msg = get_value(obj, "list", lapipb.List)
        return context.convert_list(item_type, msg.elements)

    def prim_date(self, context: "Context", obj: "Any") -> "Any":
        msg = get_value(obj, "date", str)
        return to_date(msg)

    def prim_contract_id(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        msg = get_value(obj, "contract_id", str)
        return context.convert_contract_id(item_type, msg)

    def prim_optional(self, context: "Context", t: "Type", obj: "Any") -> "Any":
        msg = get_value(obj, "optional", lapipb.Optional)
        maybe_val = msg.value if msg.HasField("value") else None
        return context.convert_optional(t, maybe_val)

    def prim_text_map(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        msg = get_value(obj, "map", lapipb.Map)
        mapping = {entry_pb.key: entry_pb.value for entry_pb in msg.entries}
        return context.convert_text_map(item_type, mapping)

    def prim_numeric(self, context: "Context", nat: int, obj: "Any") -> "Any":
        msg = get_value(obj, "numeric", str)
        return to_decimal(msg)

    def prim_gen_map(
        self, context: "Context", key_type: "Type", value_type: "Type", obj: "Any"
    ) -> "Any":
        msg = get_value(obj, "gen_map", lapipb.GenMap)

        obj = {}
        for i, entry in enumerate(msg.entries):
            key = context.append_path(f"[key: {i}]").convert(key_type, entry.key)
            value = context.append_path(f"[{key}]").convert(value_type, entry.value)
            if isinstance(key, collections.abc.Mapping):
                # Python dicts cannot be the keys of a dict because they are not hashable;
                # FrozenDict wraps a dict with a trivial hashing implementation to avoid
                # problems
                obj[FrozenDict(key)] = value
            else:
                obj[key] = value

        return obj


class ProtobufEncoder(ValueMapper):
    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        msg = lapipb.Record()

        for fld in record.fields:
            entry = msg.fields.add()
            entry.label = fld.field
            ctor, val = context.append_path(fld.field).convert(fld.type, obj[fld.field])
            set_value(entry.value, ctor, val)

        return "record", msg

    def data_variant(
        self, context: "Context", dt: "DefDataType", variant: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        obj_ctor, obj_value = to_variant(obj)
        obj_type = find_variant_type(dt, variant, obj_ctor)

        msg_case, msg_value = context.append_path(obj_ctor).convert(obj_type, obj_value)

        msg = lapipb.Variant()
        msg.constructor = obj_ctor
        set_value(msg.value, msg_case, msg_value)

        return "variant", msg

    def data_enum(
        self,
        context: "Context",
        dt: "DefDataType",
        enum: "DefDataType.EnumConstructors",
        obj: "Any",
    ) -> "Any":
        msg = lapipb.Enum()
        msg.constructor = context.value_validate_enum(obj, enum)
        return "enum", msg

    def prim_unit(self, context: "Context", obj: "Any") -> "Any":
        return "unit", Empty()

    def prim_bool(self, context: "Context", obj: "Any") -> "Any":
        return "bool", to_bool(obj)

    def prim_int64(self, context: "Context", obj: "Any") -> "Any":
        return "int64", to_int(obj)

    def prim_text(self, context: "Context", obj: "Any") -> "Any":
        return "text", to_str(obj)

    def prim_timestamp(self, context: "Context", obj: "Any") -> "Any":
        return "timestamp", datetime_to_epoch_microseconds(to_datetime(obj))

    def prim_party(self, context: "Context", obj: "Any") -> "Any":
        return "party", to_str(obj)

    def prim_list(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        msg = lapipb.List()
        for i, item in enumerate(obj):
            value = msg.elements.add()
            ctor, val = context.append_path(f"[{i}").convert(item_type, item)
            set_value(value, ctor, val)
        return "list", msg

    def prim_date(self, context: "Context", obj: "Any") -> "Any":
        return "date", date_to_int(to_date(obj))

    def prim_contract_id(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        return "contract_id", to_str(obj)

    def prim_optional(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        msg = lapipb.Optional()
        if obj is not None:
            ctor, val = context.append_path("?").convert(item_type, obj)
            set_value(msg.value, ctor, val)
        return "optional", msg

    def prim_text_map(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        msg = lapipb.Map()
        for key, value in obj.items():
            entry = msg.entries.add()
            entry.key = key
            ctor, val = context.append_path(f"[{key}]").convert(item_type, value)
            set_value(entry.value, ctor, val)
        return "map", msg

    def prim_numeric(self, context: "Context", nat: int, obj: "Any") -> "Any":
        d = to_decimal(obj)
        return "numeric", decimal_to_str(d) if d is not None else None

    def prim_gen_map(
        self, context: "Context", key_type: "Type", value_type: "Type", obj: "Any"
    ) -> "Any":
        msg = lapipb.GenMap()
        for i, (key, value) in enumerate(obj.items()):
            entry = msg.entries.add()
            key_ctor, key_val = context.append_path(f"[key: {i}]").convert(key_type, key)
            val_ctor, val_val = context.append_path(f"[{key}]").convert(value_type, value)
            set_value(entry.key, key_ctor, key_val)
            set_value(entry.value, val_ctor, val_val)
        return "gen_map", msg


def get_value(obj: "Any", field: str, pb_type: "PyType[T]") -> "T":
    return obj if isinstance(obj, pb_type) else getattr(obj, field)


def set_value(message: "lapipb.Value", ctor: "Optional[str]", value: "Any") -> None:
    """
    Work around the somewhat crazy API of Python's gRPC library to apply a known value to a
    :class:`Value`.

    :param message:
        The :class:`Value` object to modify.
    :param ctor:
        The actual field to apply to, or ``None`` to interpret the entire message as a ``Record``
        instead.
    :param value:
        The actual value to set. Must be compatible with the appropriate field.
    """
    try:
        if ctor is None:
            message.MergeFrom(value)
        elif ctor == "unit":
            message.unit.SetInParent()
        elif ctor in ("record", "variant", "list", "optional", "enum", "map", "gen_map"):
            getattr(message, ctor).MergeFrom(value)
        else:
            setattr(message, ctor, value)
    except:  # noqa
        from .. import LOG

        LOG.error("Failed to set a value %s, %s", ctor, value)
        raise
