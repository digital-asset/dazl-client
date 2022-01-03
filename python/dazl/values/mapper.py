# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
from typing import TYPE_CHECKING, Any

from ..damlast.daml_lf_1 import DefDataType, Type

if TYPE_CHECKING:
    from .context import Context

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

__all__ = ["ValueMapper"]


class ValueMapper(Protocol):
    """
    Protocol for an object that can map one representation of DAML-LF values to another
    representation. This is the protocol that wire encoders/decoders adhere to, as well as certain
    types of validators.

    To use an instance of a :class:`ValueMapper` to transform an object, create a :class:`Context`
    with an instance of a :class:`ValueMapper`; then call :meth:`Context.convert`.
    """

    def data_record(
        self, context: "Context", dt: "DefDataType", record: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        raise NotImplementedError("data_record requires an implementation")

    def data_variant(
        self, context: "Context", dt: "DefDataType", variant: "DefDataType.Fields", obj: "Any"
    ) -> "Any":
        raise NotImplementedError("data_variant requires an implementation")

    def data_enum(
        self,
        context: "Context",
        dt: "DefDataType",
        enum: "DefDataType.EnumConstructors",
        obj: "Any",
    ) -> "Any":
        raise NotImplementedError("data_variant requires an implementation")

    def prim_unit(self, context: "Context", obj: "Any") -> "Any":
        raise NotImplementedError("prim_unit requires an implementation")

    def prim_bool(self, context: "Context", obj: "Any") -> "Any":
        raise NotImplementedError("prim_bool requires an implementation")

    def prim_int64(self, context: "Context", obj: "Any") -> "Any":
        raise NotImplementedError("prim_int64 requires an implementation")

    def prim_text(self, context: "Context", obj: "Any") -> "Any":
        raise NotImplementedError("prim_text requires an implementation")

    def prim_timestamp(self, context: "Context", obj: "Any") -> "Any":
        raise NotImplementedError("prim_timestamp requires an implementation")

    def prim_party(self, context: "Context", obj: "Any") -> "Any":
        raise NotImplementedError("prim_party requires an implementation")

    def prim_list(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        raise NotImplementedError("prim_list requires an implementation")

    def prim_date(self, context: "Context", obj: "Any") -> "Any":
        raise NotImplementedError("prim_date requires an implementation")

    def prim_contract_id(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        raise NotImplementedError("prim_contract_id requires an implementation")

    def prim_optional(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        raise NotImplementedError("prim_optional requires an implementation")

    def prim_text_map(self, context: "Context", item_type: "Type", obj: "Any") -> "Any":
        raise NotImplementedError("prim_text_map requires an implementation")

    def prim_numeric(self, context: "Context", nat: int, obj: "Any") -> "Any":
        raise NotImplementedError("prim_numeric requires an implementation")

    def prim_gen_map(
        self, context: "Context", key_type: "Type", value_type: "Type", obj: "Any"
    ) -> "Any":
        raise NotImplementedError("prim_gen_map requires an implementation")
