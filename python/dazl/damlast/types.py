# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Callable

from ._base import T
from ..model.types import Type as OldType
from ..util.typing import safe_cast
from .daml_lf_1 import Type, PrimType


STRING = Type(prim=Type.Prim(prim=PrimType.TEXT, args=()))


def var(var_: str) -> 'Type':
    return Type(var=Type.Var(var_, ()))


def match_prim_type(
        prim_type: 'Type.Prim',
        on_unit: 'Callable[[], T]',
        on_bool: 'Callable[[], T]',
        on_int: 'Callable[[], T]',
        on_decimal: 'Callable[[], T]',
        on_text: 'Callable[[], T]',
        on_datetime: 'Callable[[], T]',
        on_timedelta: 'Callable[[], T]',
        on_party: 'Callable[[], T]',
        on_list: 'Callable[[Type], T]',
        on_update: 'Callable[[Type], T]',
        on_scenario: 'Callable[[Type], T]',
        on_date: 'Callable[[], T]',
        on_contract_id: 'Callable[[Type], T]',
        on_optional: 'Callable[[Type], T]',
        on_arrow: 'Callable[[Type, Type], T]',
        on_text_map: 'Callable[[Type], T]',
        on_numeric: 'Callable[[int], T]',
        on_any: 'Callable[[], T]',
        on_type_rep: 'Callable[[], T]',
        on_gen_map: 'Callable[[Type, Type], T]') -> 'T':
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
    else:
        raise ValueError(f'undefined PrimType: {prim_type}')


def get_old_type(daml_type: 'Type') -> 'OldType':
    from ..model.types import UnsupportedType

    return safe_cast(Type, daml_type).Sum_match(
        _old_type_var, _old_type_con, _old_type_prim, _old_forall_type,
        lambda tuple_: UnsupportedType('Tuple'),
        lambda nat: UnsupportedType('Nat'))


def _old_type_var(var_: 'Type.Var') -> 'OldType':
    from ..model.types import TypeApp, TypeVariable
    core_type = TypeVariable(var_.var)
    return TypeApp(core_type, [get_old_type(var_) for var_ in var_.args]) if var_.args else core_type


def _old_type_con(con: 'Type.Con') -> 'OldType':
    from ..model.types import TypeApp
    core_type = con.tycon
    return TypeApp(core_type, [get_old_type(var) for var in con.args]) if con.args else core_type


def _old_type_prim(prim: 'Type.Prim') -> 'OldType':
    from ..model.types import UnsupportedType
    return match_prim_type(
        prim,
        _old_scalar_type_unit,
        _old_scalar_type_bool,
        _old_scalar_type_integer,
        _old_scalar_type_decimal,
        _old_scalar_type_text,
        _old_scalar_type_datetime,
        _old_scalar_type_reltime,
        _old_scalar_type_party,
        _old_list_type,
        _old_update_type,
        lambda *args: UnsupportedType('Scenario'),
        _old_scalar_type_date,
        _old_scalar_contract_id_type,
        _old_optional_type,
        lambda *args: UnsupportedType('Arrow'),
        _old_textmap_type,
        _old_scalar_type_numeric,
        _old_scalar_type_any,
        _old_scalar_type_type_rep,
        _old_genmap_type)


def _old_forall_type(forall: 'Type.Forall') -> 'OldType':
    from ..model.types import ForAllType
    return ForAllType(forall.vars, get_old_type(forall.body))


def _old_scalar_type_unit() -> 'OldType':
    from ..model.types import SCALAR_TYPE_UNIT
    return SCALAR_TYPE_UNIT


def _old_scalar_type_bool() -> 'OldType':
    from ..model.types import SCALAR_TYPE_BOOL
    return SCALAR_TYPE_BOOL


def _old_scalar_type_integer() -> 'OldType':
    from ..model.types import SCALAR_TYPE_INTEGER
    return SCALAR_TYPE_INTEGER


def _old_scalar_type_decimal() -> 'OldType':
    from ..model.types import SCALAR_TYPE_DECIMAL
    return SCALAR_TYPE_DECIMAL


def _old_scalar_type_numeric(nat: int = 10) -> 'OldType':
    from ..model.types import SCALAR_TYPE_NUMERIC
    return SCALAR_TYPE_NUMERIC


def _old_scalar_type_text() -> 'OldType':
    from ..model.types import SCALAR_TYPE_TEXT
    return SCALAR_TYPE_TEXT


def _old_scalar_type_datetime() -> 'OldType':
    from ..model.types import SCALAR_TYPE_DATETIME
    return SCALAR_TYPE_DATETIME


def _old_scalar_type_reltime() -> 'OldType':
    from ..model.types import SCALAR_TYPE_RELTIME
    return SCALAR_TYPE_RELTIME


def _old_scalar_type_party() -> 'OldType':
    from ..model.types import SCALAR_TYPE_PARTY
    return SCALAR_TYPE_PARTY


def _old_scalar_type_any() -> 'OldType':
    from ..model.types import SCALAR_TYPE_ANY
    return SCALAR_TYPE_ANY


def _old_list_type(arg: 'Type') -> 'OldType':
    from ..model.types import ListType
    return ListType(get_old_type(arg))


def _old_update_type(arg: 'Type') -> 'OldType':
    from ..model.types import UpdateType
    return UpdateType(get_old_type(arg))


def _old_scalar_type_date() -> 'OldType':
    from ..model.types import SCALAR_TYPE_DATE
    return SCALAR_TYPE_DATE


def _old_scalar_contract_id_type(arg: 'Type') -> 'OldType':
    from ..model.types import ContractIdType
    return ContractIdType(get_old_type(arg))


def _old_optional_type(arg: 'Type') -> 'OldType':
    from ..model.types import OptionalType
    return OptionalType(get_old_type(arg))


def _old_textmap_type(value_type: 'Type') -> 'OldType':
    from ..model.types import TextMapType
    return TextMapType(get_old_type(value_type))


def _old_scalar_type_type_rep(arg: 'Optional[Type]' = None) -> 'OldType':
    from ..model.types import TypeRefType, UnsupportedType
    if arg is not None:
        return TypeRefType(get_old_type(arg))
    else:
        return UnsupportedType('TypeRef')


def _old_genmap_type(key_type: 'Type', value_type: 'Type') -> 'OldType':
    from ..model.types import GenMapType
    return GenMapType(get_old_type(key_type), get_old_type(value_type))
