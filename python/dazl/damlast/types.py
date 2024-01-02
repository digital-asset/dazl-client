# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Callable

from ._base import T
from .daml_lf_1 import PrimType, Type

__all__ = ["match_prim_type"]


def match_prim_type(
    prim_type: "Type.Prim",
    on_unit: "Callable[[], T]",
    on_bool: "Callable[[], T]",
    on_int: "Callable[[], T]",
    on_decimal: "Callable[[], T]",
    on_text: "Callable[[], T]",
    on_datetime: "Callable[[], T]",
    on_timedelta: "Callable[[], T]",
    on_party: "Callable[[], T]",
    on_list: "Callable[[Type], T]",
    on_update: "Callable[[Type], T]",
    on_scenario: "Callable[[Type], T]",
    on_date: "Callable[[], T]",
    on_contract_id: "Callable[[Type], T]",
    on_optional: "Callable[[Type], T]",
    on_arrow: "Callable[[Type, Type], T]",
    on_text_map: "Callable[[Type], T]",
    on_numeric: "Callable[[int], T]",
    on_any: "Callable[[], T]",
    on_type_rep: "Callable[[], T]",
    on_gen_map: "Callable[[Type, Type], T]",
    on_any_exception: "Callable[[], T]",
) -> "T":
    if prim_type.prim == PrimType.UNIT:
        return on_unit()
    elif prim_type.prim == PrimType.BOOL:
        return on_bool()
    elif prim_type.prim == PrimType.INT64:
        return on_int()
    elif prim_type.prim == PrimType.DECIMAL:
        return on_decimal()
    elif prim_type.prim == PrimType.TEXT or prim_type.prim == PrimType.CHAR:
        return on_text()
    elif prim_type.prim == PrimType.TIMESTAMP:
        return on_datetime()
    elif prim_type.prim == PrimType.RELTIME:
        return on_timedelta()
    elif prim_type.prim == PrimType.PARTY:
        return on_party()
    elif prim_type.prim == PrimType.LIST:
        return on_list(prim_type.args[0])
    elif prim_type.prim == PrimType.UPDATE:
        return on_update(prim_type.args[0])
    elif prim_type.prim == PrimType.SCENARIO:
        return on_scenario(prim_type.args[0])
    elif prim_type.prim == PrimType.DATE:
        return on_date()
    elif prim_type.prim == PrimType.CONTRACT_ID:
        return on_contract_id(prim_type.args[0])
    elif prim_type.prim == PrimType.OPTIONAL:
        return on_optional(prim_type.args[0])
    elif prim_type.prim == PrimType.ARROW:
        return on_arrow(prim_type.args[0], prim_type.args[1])
    elif prim_type.prim == PrimType.TEXTMAP:
        return on_text_map(prim_type.args[0])
    elif prim_type.prim == PrimType.NUMERIC:
        return on_numeric(prim_type.args[0].nat)
    elif prim_type.prim == PrimType.ANY:
        return on_any()
    elif prim_type.prim == PrimType.TYPE_REP:
        return on_type_rep()
    elif prim_type.prim == PrimType.GENMAP:
        return on_gen_map(prim_type.args[0], prim_type.args[1])
    elif prim_type.prim == PrimType.ANY_EXCEPTION:
        return on_any_exception()
    else:
        raise ValueError(f"undefined PrimType: {prim_type}")
