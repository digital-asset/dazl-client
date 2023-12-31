# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrimType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    UNIT: _ClassVar[PrimType]
    BOOL: _ClassVar[PrimType]
    INT64: _ClassVar[PrimType]
    DECIMAL: _ClassVar[PrimType]
    TEXT: _ClassVar[PrimType]
    TIMESTAMP: _ClassVar[PrimType]
    PARTY: _ClassVar[PrimType]
    LIST: _ClassVar[PrimType]
    UPDATE: _ClassVar[PrimType]
    SCENARIO: _ClassVar[PrimType]
    DATE: _ClassVar[PrimType]
    CONTRACT_ID: _ClassVar[PrimType]
    OPTIONAL: _ClassVar[PrimType]
    ARROW: _ClassVar[PrimType]
    TEXTMAP: _ClassVar[PrimType]
    NUMERIC: _ClassVar[PrimType]
    ANY: _ClassVar[PrimType]
    TYPE_REP: _ClassVar[PrimType]
    GENMAP: _ClassVar[PrimType]
    BIGNUMERIC: _ClassVar[PrimType]
    ROUNDING_MODE: _ClassVar[PrimType]
    ANY_EXCEPTION: _ClassVar[PrimType]

class PrimCon(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    CON_UNIT: _ClassVar[PrimCon]
    CON_FALSE: _ClassVar[PrimCon]
    CON_TRUE: _ClassVar[PrimCon]

class BuiltinFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    ADD_DECIMAL: _ClassVar[BuiltinFunction]
    SUB_DECIMAL: _ClassVar[BuiltinFunction]
    MUL_DECIMAL: _ClassVar[BuiltinFunction]
    DIV_DECIMAL: _ClassVar[BuiltinFunction]
    ROUND_DECIMAL: _ClassVar[BuiltinFunction]
    ADD_NUMERIC: _ClassVar[BuiltinFunction]
    SUB_NUMERIC: _ClassVar[BuiltinFunction]
    MUL_NUMERIC: _ClassVar[BuiltinFunction]
    DIV_NUMERIC: _ClassVar[BuiltinFunction]
    ROUND_NUMERIC: _ClassVar[BuiltinFunction]
    CAST_NUMERIC: _ClassVar[BuiltinFunction]
    SHIFT_NUMERIC: _ClassVar[BuiltinFunction]
    ADD_INT64: _ClassVar[BuiltinFunction]
    SUB_INT64: _ClassVar[BuiltinFunction]
    MUL_INT64: _ClassVar[BuiltinFunction]
    DIV_INT64: _ClassVar[BuiltinFunction]
    MOD_INT64: _ClassVar[BuiltinFunction]
    EXP_INT64: _ClassVar[BuiltinFunction]
    FOLDL: _ClassVar[BuiltinFunction]
    FOLDR: _ClassVar[BuiltinFunction]
    TEXTMAP_EMPTY: _ClassVar[BuiltinFunction]
    TEXTMAP_INSERT: _ClassVar[BuiltinFunction]
    TEXTMAP_LOOKUP: _ClassVar[BuiltinFunction]
    TEXTMAP_DELETE: _ClassVar[BuiltinFunction]
    TEXTMAP_TO_LIST: _ClassVar[BuiltinFunction]
    TEXTMAP_SIZE: _ClassVar[BuiltinFunction]
    GENMAP_EMPTY: _ClassVar[BuiltinFunction]
    GENMAP_INSERT: _ClassVar[BuiltinFunction]
    GENMAP_LOOKUP: _ClassVar[BuiltinFunction]
    GENMAP_DELETE: _ClassVar[BuiltinFunction]
    GENMAP_KEYS: _ClassVar[BuiltinFunction]
    GENMAP_VALUES: _ClassVar[BuiltinFunction]
    GENMAP_SIZE: _ClassVar[BuiltinFunction]
    EXPLODE_TEXT: _ClassVar[BuiltinFunction]
    APPEND_TEXT: _ClassVar[BuiltinFunction]
    ERROR: _ClassVar[BuiltinFunction]
    ANY_EXCEPTION_MESSAGE: _ClassVar[BuiltinFunction]
    LEQ_INT64: _ClassVar[BuiltinFunction]
    LEQ_DECIMAL: _ClassVar[BuiltinFunction]
    LEQ_NUMERIC: _ClassVar[BuiltinFunction]
    LEQ_TEXT: _ClassVar[BuiltinFunction]
    LEQ_TIMESTAMP: _ClassVar[BuiltinFunction]
    LEQ_DATE: _ClassVar[BuiltinFunction]
    LEQ_PARTY: _ClassVar[BuiltinFunction]
    LESS_INT64: _ClassVar[BuiltinFunction]
    LESS_DECIMAL: _ClassVar[BuiltinFunction]
    LESS_NUMERIC: _ClassVar[BuiltinFunction]
    LESS_TEXT: _ClassVar[BuiltinFunction]
    LESS_TIMESTAMP: _ClassVar[BuiltinFunction]
    LESS_DATE: _ClassVar[BuiltinFunction]
    LESS_PARTY: _ClassVar[BuiltinFunction]
    GEQ_INT64: _ClassVar[BuiltinFunction]
    GEQ_DECIMAL: _ClassVar[BuiltinFunction]
    GEQ_NUMERIC: _ClassVar[BuiltinFunction]
    GEQ_TEXT: _ClassVar[BuiltinFunction]
    GEQ_TIMESTAMP: _ClassVar[BuiltinFunction]
    GEQ_DATE: _ClassVar[BuiltinFunction]
    GEQ_PARTY: _ClassVar[BuiltinFunction]
    GREATER_INT64: _ClassVar[BuiltinFunction]
    GREATER_DECIMAL: _ClassVar[BuiltinFunction]
    GREATER_NUMERIC: _ClassVar[BuiltinFunction]
    GREATER_TEXT: _ClassVar[BuiltinFunction]
    GREATER_TIMESTAMP: _ClassVar[BuiltinFunction]
    GREATER_DATE: _ClassVar[BuiltinFunction]
    GREATER_PARTY: _ClassVar[BuiltinFunction]
    INT64_TO_TEXT: _ClassVar[BuiltinFunction]
    DECIMAL_TO_TEXT: _ClassVar[BuiltinFunction]
    NUMERIC_TO_TEXT: _ClassVar[BuiltinFunction]
    TEXT_TO_TEXT: _ClassVar[BuiltinFunction]
    TIMESTAMP_TO_TEXT: _ClassVar[BuiltinFunction]
    DATE_TO_TEXT: _ClassVar[BuiltinFunction]
    PARTY_TO_QUOTED_TEXT: _ClassVar[BuiltinFunction]
    PARTY_TO_TEXT: _ClassVar[BuiltinFunction]
    TEXT_TO_PARTY: _ClassVar[BuiltinFunction]
    TEXT_TO_INT64: _ClassVar[BuiltinFunction]
    TEXT_TO_DECIMAL: _ClassVar[BuiltinFunction]
    TEXT_TO_NUMERIC: _ClassVar[BuiltinFunction]
    CONTRACT_ID_TO_TEXT: _ClassVar[BuiltinFunction]
    SHA256_TEXT: _ClassVar[BuiltinFunction]
    DATE_TO_UNIX_DAYS: _ClassVar[BuiltinFunction]
    UNIX_DAYS_TO_DATE: _ClassVar[BuiltinFunction]
    TIMESTAMP_TO_UNIX_MICROSECONDS: _ClassVar[BuiltinFunction]
    UNIX_MICROSECONDS_TO_TIMESTAMP: _ClassVar[BuiltinFunction]
    INT64_TO_DECIMAL: _ClassVar[BuiltinFunction]
    DECIMAL_TO_INT64: _ClassVar[BuiltinFunction]
    INT64_TO_NUMERIC: _ClassVar[BuiltinFunction]
    NUMERIC_TO_INT64: _ClassVar[BuiltinFunction]
    IMPLODE_TEXT: _ClassVar[BuiltinFunction]
    EQUAL_INT64: _ClassVar[BuiltinFunction]
    EQUAL_DECIMAL: _ClassVar[BuiltinFunction]
    EQUAL_NUMERIC: _ClassVar[BuiltinFunction]
    EQUAL_TEXT: _ClassVar[BuiltinFunction]
    EQUAL_TIMESTAMP: _ClassVar[BuiltinFunction]
    EQUAL_DATE: _ClassVar[BuiltinFunction]
    EQUAL_PARTY: _ClassVar[BuiltinFunction]
    EQUAL_BOOL: _ClassVar[BuiltinFunction]
    EQUAL_CONTRACT_ID: _ClassVar[BuiltinFunction]
    EQUAL_LIST: _ClassVar[BuiltinFunction]
    EQUAL_TYPE_REP: _ClassVar[BuiltinFunction]
    EQUAL: _ClassVar[BuiltinFunction]
    LESS_EQ: _ClassVar[BuiltinFunction]
    LESS: _ClassVar[BuiltinFunction]
    GREATER_EQ: _ClassVar[BuiltinFunction]
    GREATER: _ClassVar[BuiltinFunction]
    TRACE: _ClassVar[BuiltinFunction]
    COERCE_CONTRACT_ID: _ClassVar[BuiltinFunction]
    CODE_POINTS_TO_TEXT: _ClassVar[BuiltinFunction]
    TEXT_TO_CODE_POINTS: _ClassVar[BuiltinFunction]
    SCALE_BIGNUMERIC: _ClassVar[BuiltinFunction]
    PRECISION_BIGNUMERIC: _ClassVar[BuiltinFunction]
    ADD_BIGNUMERIC: _ClassVar[BuiltinFunction]
    SUB_BIGNUMERIC: _ClassVar[BuiltinFunction]
    MUL_BIGNUMERIC: _ClassVar[BuiltinFunction]
    DIV_BIGNUMERIC: _ClassVar[BuiltinFunction]
    SHIFT_RIGHT_BIGNUMERIC: _ClassVar[BuiltinFunction]
    BIGNUMERIC_TO_NUMERIC: _ClassVar[BuiltinFunction]
    NUMERIC_TO_BIGNUMERIC: _ClassVar[BuiltinFunction]
    BIGNUMERIC_TO_TEXT: _ClassVar[BuiltinFunction]
UNIT: PrimType
BOOL: PrimType
INT64: PrimType
DECIMAL: PrimType
TEXT: PrimType
TIMESTAMP: PrimType
PARTY: PrimType
LIST: PrimType
UPDATE: PrimType
SCENARIO: PrimType
DATE: PrimType
CONTRACT_ID: PrimType
OPTIONAL: PrimType
ARROW: PrimType
TEXTMAP: PrimType
NUMERIC: PrimType
ANY: PrimType
TYPE_REP: PrimType
GENMAP: PrimType
BIGNUMERIC: PrimType
ROUNDING_MODE: PrimType
ANY_EXCEPTION: PrimType
CON_UNIT: PrimCon
CON_FALSE: PrimCon
CON_TRUE: PrimCon
ADD_DECIMAL: BuiltinFunction
SUB_DECIMAL: BuiltinFunction
MUL_DECIMAL: BuiltinFunction
DIV_DECIMAL: BuiltinFunction
ROUND_DECIMAL: BuiltinFunction
ADD_NUMERIC: BuiltinFunction
SUB_NUMERIC: BuiltinFunction
MUL_NUMERIC: BuiltinFunction
DIV_NUMERIC: BuiltinFunction
ROUND_NUMERIC: BuiltinFunction
CAST_NUMERIC: BuiltinFunction
SHIFT_NUMERIC: BuiltinFunction
ADD_INT64: BuiltinFunction
SUB_INT64: BuiltinFunction
MUL_INT64: BuiltinFunction
DIV_INT64: BuiltinFunction
MOD_INT64: BuiltinFunction
EXP_INT64: BuiltinFunction
FOLDL: BuiltinFunction
FOLDR: BuiltinFunction
TEXTMAP_EMPTY: BuiltinFunction
TEXTMAP_INSERT: BuiltinFunction
TEXTMAP_LOOKUP: BuiltinFunction
TEXTMAP_DELETE: BuiltinFunction
TEXTMAP_TO_LIST: BuiltinFunction
TEXTMAP_SIZE: BuiltinFunction
GENMAP_EMPTY: BuiltinFunction
GENMAP_INSERT: BuiltinFunction
GENMAP_LOOKUP: BuiltinFunction
GENMAP_DELETE: BuiltinFunction
GENMAP_KEYS: BuiltinFunction
GENMAP_VALUES: BuiltinFunction
GENMAP_SIZE: BuiltinFunction
EXPLODE_TEXT: BuiltinFunction
APPEND_TEXT: BuiltinFunction
ERROR: BuiltinFunction
ANY_EXCEPTION_MESSAGE: BuiltinFunction
LEQ_INT64: BuiltinFunction
LEQ_DECIMAL: BuiltinFunction
LEQ_NUMERIC: BuiltinFunction
LEQ_TEXT: BuiltinFunction
LEQ_TIMESTAMP: BuiltinFunction
LEQ_DATE: BuiltinFunction
LEQ_PARTY: BuiltinFunction
LESS_INT64: BuiltinFunction
LESS_DECIMAL: BuiltinFunction
LESS_NUMERIC: BuiltinFunction
LESS_TEXT: BuiltinFunction
LESS_TIMESTAMP: BuiltinFunction
LESS_DATE: BuiltinFunction
LESS_PARTY: BuiltinFunction
GEQ_INT64: BuiltinFunction
GEQ_DECIMAL: BuiltinFunction
GEQ_NUMERIC: BuiltinFunction
GEQ_TEXT: BuiltinFunction
GEQ_TIMESTAMP: BuiltinFunction
GEQ_DATE: BuiltinFunction
GEQ_PARTY: BuiltinFunction
GREATER_INT64: BuiltinFunction
GREATER_DECIMAL: BuiltinFunction
GREATER_NUMERIC: BuiltinFunction
GREATER_TEXT: BuiltinFunction
GREATER_TIMESTAMP: BuiltinFunction
GREATER_DATE: BuiltinFunction
GREATER_PARTY: BuiltinFunction
INT64_TO_TEXT: BuiltinFunction
DECIMAL_TO_TEXT: BuiltinFunction
NUMERIC_TO_TEXT: BuiltinFunction
TEXT_TO_TEXT: BuiltinFunction
TIMESTAMP_TO_TEXT: BuiltinFunction
DATE_TO_TEXT: BuiltinFunction
PARTY_TO_QUOTED_TEXT: BuiltinFunction
PARTY_TO_TEXT: BuiltinFunction
TEXT_TO_PARTY: BuiltinFunction
TEXT_TO_INT64: BuiltinFunction
TEXT_TO_DECIMAL: BuiltinFunction
TEXT_TO_NUMERIC: BuiltinFunction
CONTRACT_ID_TO_TEXT: BuiltinFunction
SHA256_TEXT: BuiltinFunction
DATE_TO_UNIX_DAYS: BuiltinFunction
UNIX_DAYS_TO_DATE: BuiltinFunction
TIMESTAMP_TO_UNIX_MICROSECONDS: BuiltinFunction
UNIX_MICROSECONDS_TO_TIMESTAMP: BuiltinFunction
INT64_TO_DECIMAL: BuiltinFunction
DECIMAL_TO_INT64: BuiltinFunction
INT64_TO_NUMERIC: BuiltinFunction
NUMERIC_TO_INT64: BuiltinFunction
IMPLODE_TEXT: BuiltinFunction
EQUAL_INT64: BuiltinFunction
EQUAL_DECIMAL: BuiltinFunction
EQUAL_NUMERIC: BuiltinFunction
EQUAL_TEXT: BuiltinFunction
EQUAL_TIMESTAMP: BuiltinFunction
EQUAL_DATE: BuiltinFunction
EQUAL_PARTY: BuiltinFunction
EQUAL_BOOL: BuiltinFunction
EQUAL_CONTRACT_ID: BuiltinFunction
EQUAL_LIST: BuiltinFunction
EQUAL_TYPE_REP: BuiltinFunction
EQUAL: BuiltinFunction
LESS_EQ: BuiltinFunction
LESS: BuiltinFunction
GREATER_EQ: BuiltinFunction
GREATER: BuiltinFunction
TRACE: BuiltinFunction
COERCE_CONTRACT_ID: BuiltinFunction
CODE_POINTS_TO_TEXT: BuiltinFunction
TEXT_TO_CODE_POINTS: BuiltinFunction
SCALE_BIGNUMERIC: BuiltinFunction
PRECISION_BIGNUMERIC: BuiltinFunction
ADD_BIGNUMERIC: BuiltinFunction
SUB_BIGNUMERIC: BuiltinFunction
MUL_BIGNUMERIC: BuiltinFunction
DIV_BIGNUMERIC: BuiltinFunction
SHIFT_RIGHT_BIGNUMERIC: BuiltinFunction
BIGNUMERIC_TO_NUMERIC: BuiltinFunction
NUMERIC_TO_BIGNUMERIC: BuiltinFunction
BIGNUMERIC_TO_TEXT: BuiltinFunction

class Unit(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class PackageRef(_message.Message):
    __slots__ = ["self", "package_id_str", "package_id_interned_str"]
    SELF_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_STR_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    self: Unit
    package_id_str: str
    package_id_interned_str: int
    def __init__(self, self_: _Optional[_Union[Unit, _Mapping]] = ..., package_id_str: _Optional[str] = ..., package_id_interned_str: _Optional[int] = ...) -> None: ...

class DottedName(_message.Message):
    __slots__ = ["segments"]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, segments: _Optional[_Iterable[str]] = ...) -> None: ...

class ModuleRef(_message.Message):
    __slots__ = ["package_ref", "module_name_dname", "module_name_interned_dname"]
    PACKAGE_REF_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    package_ref: PackageRef
    module_name_dname: DottedName
    module_name_interned_dname: int
    def __init__(self, package_ref: _Optional[_Union[PackageRef, _Mapping]] = ..., module_name_dname: _Optional[_Union[DottedName, _Mapping]] = ..., module_name_interned_dname: _Optional[int] = ...) -> None: ...

class TypeConName(_message.Message):
    __slots__ = ["module", "name_dname", "name_interned_dname"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    module: ModuleRef
    name_dname: DottedName
    name_interned_dname: int
    def __init__(self, module: _Optional[_Union[ModuleRef, _Mapping]] = ..., name_dname: _Optional[_Union[DottedName, _Mapping]] = ..., name_interned_dname: _Optional[int] = ...) -> None: ...

class TypeSynName(_message.Message):
    __slots__ = ["module", "name_dname", "name_interned_dname"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    module: ModuleRef
    name_dname: DottedName
    name_interned_dname: int
    def __init__(self, module: _Optional[_Union[ModuleRef, _Mapping]] = ..., name_dname: _Optional[_Union[DottedName, _Mapping]] = ..., name_interned_dname: _Optional[int] = ...) -> None: ...

class ValName(_message.Message):
    __slots__ = ["module", "name_dname", "name_interned_dname"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    module: ModuleRef
    name_dname: _containers.RepeatedScalarFieldContainer[str]
    name_interned_dname: int
    def __init__(self, module: _Optional[_Union[ModuleRef, _Mapping]] = ..., name_dname: _Optional[_Iterable[str]] = ..., name_interned_dname: _Optional[int] = ...) -> None: ...

class FieldWithType(_message.Message):
    __slots__ = ["field_str", "field_interned_str", "type"]
    FIELD_STR_FIELD_NUMBER: _ClassVar[int]
    FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    field_str: str
    field_interned_str: int
    type: Type
    def __init__(self, field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ..., type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...

class VarWithType(_message.Message):
    __slots__ = ["var_str", "var_interned_str", "type"]
    VAR_STR_FIELD_NUMBER: _ClassVar[int]
    VAR_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    var_str: str
    var_interned_str: int
    type: Type
    def __init__(self, var_str: _Optional[str] = ..., var_interned_str: _Optional[int] = ..., type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...

class TypeVarWithKind(_message.Message):
    __slots__ = ["var_str", "var_interned_str", "kind"]
    VAR_STR_FIELD_NUMBER: _ClassVar[int]
    VAR_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    var_str: str
    var_interned_str: int
    kind: Kind
    def __init__(self, var_str: _Optional[str] = ..., var_interned_str: _Optional[int] = ..., kind: _Optional[_Union[Kind, _Mapping]] = ...) -> None: ...

class FieldWithExpr(_message.Message):
    __slots__ = ["field_str", "field_interned_str", "expr"]
    FIELD_STR_FIELD_NUMBER: _ClassVar[int]
    FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    field_str: str
    field_interned_str: int
    expr: Expr
    def __init__(self, field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class Binding(_message.Message):
    __slots__ = ["binder", "bound"]
    BINDER_FIELD_NUMBER: _ClassVar[int]
    BOUND_FIELD_NUMBER: _ClassVar[int]
    binder: VarWithType
    bound: Expr
    def __init__(self, binder: _Optional[_Union[VarWithType, _Mapping]] = ..., bound: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class Kind(_message.Message):
    __slots__ = ["star", "arrow", "nat"]
    class Arrow(_message.Message):
        __slots__ = ["params", "result"]
        PARAMS_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        params: _containers.RepeatedCompositeFieldContainer[Kind]
        result: Kind
        def __init__(self, params: _Optional[_Iterable[_Union[Kind, _Mapping]]] = ..., result: _Optional[_Union[Kind, _Mapping]] = ...) -> None: ...
    STAR_FIELD_NUMBER: _ClassVar[int]
    ARROW_FIELD_NUMBER: _ClassVar[int]
    NAT_FIELD_NUMBER: _ClassVar[int]
    star: Unit
    arrow: Kind.Arrow
    nat: Unit
    def __init__(self, star: _Optional[_Union[Unit, _Mapping]] = ..., arrow: _Optional[_Union[Kind.Arrow, _Mapping]] = ..., nat: _Optional[_Union[Unit, _Mapping]] = ...) -> None: ...

class Type(_message.Message):
    __slots__ = ["var", "con", "prim", "forall", "struct", "nat", "syn", "interned"]
    class Var(_message.Message):
        __slots__ = ["var_str", "var_interned_str", "args"]
        VAR_STR_FIELD_NUMBER: _ClassVar[int]
        VAR_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        var_str: str
        var_interned_str: int
        args: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, var_str: _Optional[str] = ..., var_interned_str: _Optional[int] = ..., args: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class Con(_message.Message):
        __slots__ = ["tycon", "args"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        tycon: TypeConName
        args: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, tycon: _Optional[_Union[TypeConName, _Mapping]] = ..., args: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class Syn(_message.Message):
        __slots__ = ["tysyn", "args"]
        TYSYN_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        tysyn: TypeSynName
        args: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, tysyn: _Optional[_Union[TypeSynName, _Mapping]] = ..., args: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class Prim(_message.Message):
        __slots__ = ["prim", "args"]
        PRIM_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        prim: PrimType
        args: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, prim: _Optional[_Union[PrimType, str]] = ..., args: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class Forall(_message.Message):
        __slots__ = ["vars", "body"]
        VARS_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        vars: _containers.RepeatedCompositeFieldContainer[TypeVarWithKind]
        body: Type
        def __init__(self, vars: _Optional[_Iterable[_Union[TypeVarWithKind, _Mapping]]] = ..., body: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    class Struct(_message.Message):
        __slots__ = ["fields"]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedCompositeFieldContainer[FieldWithType]
        def __init__(self, fields: _Optional[_Iterable[_Union[FieldWithType, _Mapping]]] = ...) -> None: ...
    VAR_FIELD_NUMBER: _ClassVar[int]
    CON_FIELD_NUMBER: _ClassVar[int]
    PRIM_FIELD_NUMBER: _ClassVar[int]
    FORALL_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_NUMBER: _ClassVar[int]
    NAT_FIELD_NUMBER: _ClassVar[int]
    SYN_FIELD_NUMBER: _ClassVar[int]
    INTERNED_FIELD_NUMBER: _ClassVar[int]
    var: Type.Var
    con: Type.Con
    prim: Type.Prim
    forall: Type.Forall
    struct: Type.Struct
    nat: int
    syn: Type.Syn
    interned: int
    def __init__(self, var: _Optional[_Union[Type.Var, _Mapping]] = ..., con: _Optional[_Union[Type.Con, _Mapping]] = ..., prim: _Optional[_Union[Type.Prim, _Mapping]] = ..., forall: _Optional[_Union[Type.Forall, _Mapping]] = ..., struct: _Optional[_Union[Type.Struct, _Mapping]] = ..., nat: _Optional[int] = ..., syn: _Optional[_Union[Type.Syn, _Mapping]] = ..., interned: _Optional[int] = ...) -> None: ...

class PrimLit(_message.Message):
    __slots__ = ["int64", "decimal_str", "numeric_interned_str", "text_str", "text_interned_str", "timestamp", "party_str", "party_interned_str", "date", "rounding_mode"]
    class RoundingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        UP: _ClassVar[PrimLit.RoundingMode]
        DOWN: _ClassVar[PrimLit.RoundingMode]
        CEILING: _ClassVar[PrimLit.RoundingMode]
        FLOOR: _ClassVar[PrimLit.RoundingMode]
        HALF_UP: _ClassVar[PrimLit.RoundingMode]
        HALF_DOWN: _ClassVar[PrimLit.RoundingMode]
        HALF_EVEN: _ClassVar[PrimLit.RoundingMode]
        UNNECESSARY: _ClassVar[PrimLit.RoundingMode]
    UP: PrimLit.RoundingMode
    DOWN: PrimLit.RoundingMode
    CEILING: PrimLit.RoundingMode
    FLOOR: PrimLit.RoundingMode
    HALF_UP: PrimLit.RoundingMode
    HALF_DOWN: PrimLit.RoundingMode
    HALF_EVEN: PrimLit.RoundingMode
    UNNECESSARY: PrimLit.RoundingMode
    INT64_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_STR_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    TEXT_STR_FIELD_NUMBER: _ClassVar[int]
    TEXT_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PARTY_STR_FIELD_NUMBER: _ClassVar[int]
    PARTY_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ROUNDING_MODE_FIELD_NUMBER: _ClassVar[int]
    int64: int
    decimal_str: str
    numeric_interned_str: int
    text_str: str
    text_interned_str: int
    timestamp: int
    party_str: str
    party_interned_str: int
    date: int
    rounding_mode: PrimLit.RoundingMode
    def __init__(self, int64: _Optional[int] = ..., decimal_str: _Optional[str] = ..., numeric_interned_str: _Optional[int] = ..., text_str: _Optional[str] = ..., text_interned_str: _Optional[int] = ..., timestamp: _Optional[int] = ..., party_str: _Optional[str] = ..., party_interned_str: _Optional[int] = ..., date: _Optional[int] = ..., rounding_mode: _Optional[_Union[PrimLit.RoundingMode, str]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["module", "range"]
    class Range(_message.Message):
        __slots__ = ["start_line", "start_col", "end_line", "end_col"]
        START_LINE_FIELD_NUMBER: _ClassVar[int]
        START_COL_FIELD_NUMBER: _ClassVar[int]
        END_LINE_FIELD_NUMBER: _ClassVar[int]
        END_COL_FIELD_NUMBER: _ClassVar[int]
        start_line: int
        start_col: int
        end_line: int
        end_col: int
        def __init__(self, start_line: _Optional[int] = ..., start_col: _Optional[int] = ..., end_line: _Optional[int] = ..., end_col: _Optional[int] = ...) -> None: ...
    MODULE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    module: ModuleRef
    range: Location.Range
    def __init__(self, module: _Optional[_Union[ModuleRef, _Mapping]] = ..., range: _Optional[_Union[Location.Range, _Mapping]] = ...) -> None: ...

class Expr(_message.Message):
    __slots__ = ["location", "var_str", "var_interned_str", "val", "builtin", "prim_con", "prim_lit", "rec_con", "rec_proj", "rec_upd", "variant_con", "enum_con", "struct_con", "struct_proj", "struct_upd", "app", "ty_app", "abs", "ty_abs", "case", "let", "nil", "cons", "update", "scenario", "optional_none", "optional_some", "to_any", "from_any", "type_rep", "to_any_exception", "from_any_exception", "throw", "to_interface", "from_interface", "call_interface", "signatory_interface", "observer_interface", "view_interface", "unsafe_from_interface", "interface_template_type_rep", "to_required_interface", "from_required_interface", "unsafe_from_required_interface", "experimental"]
    class RecCon(_message.Message):
        __slots__ = ["tycon", "fields"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        tycon: Type.Con
        fields: _containers.RepeatedCompositeFieldContainer[FieldWithExpr]
        def __init__(self, tycon: _Optional[_Union[Type.Con, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[FieldWithExpr, _Mapping]]] = ...) -> None: ...
    class RecProj(_message.Message):
        __slots__ = ["tycon", "field_str", "field_interned_str", "record"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        FIELD_STR_FIELD_NUMBER: _ClassVar[int]
        FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        RECORD_FIELD_NUMBER: _ClassVar[int]
        tycon: Type.Con
        field_str: str
        field_interned_str: int
        record: Expr
        def __init__(self, tycon: _Optional[_Union[Type.Con, _Mapping]] = ..., field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ..., record: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class RecUpd(_message.Message):
        __slots__ = ["tycon", "field_str", "field_interned_str", "record", "update"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        FIELD_STR_FIELD_NUMBER: _ClassVar[int]
        FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        RECORD_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        tycon: Type.Con
        field_str: str
        field_interned_str: int
        record: Expr
        update: Expr
        def __init__(self, tycon: _Optional[_Union[Type.Con, _Mapping]] = ..., field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ..., record: _Optional[_Union[Expr, _Mapping]] = ..., update: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class VariantCon(_message.Message):
        __slots__ = ["tycon", "variant_con_str", "variant_con_interned_str", "variant_arg"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        VARIANT_CON_STR_FIELD_NUMBER: _ClassVar[int]
        VARIANT_CON_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        VARIANT_ARG_FIELD_NUMBER: _ClassVar[int]
        tycon: Type.Con
        variant_con_str: str
        variant_con_interned_str: int
        variant_arg: Expr
        def __init__(self, tycon: _Optional[_Union[Type.Con, _Mapping]] = ..., variant_con_str: _Optional[str] = ..., variant_con_interned_str: _Optional[int] = ..., variant_arg: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class EnumCon(_message.Message):
        __slots__ = ["tycon", "enum_con_str", "enum_con_interned_str"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        ENUM_CON_STR_FIELD_NUMBER: _ClassVar[int]
        ENUM_CON_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        tycon: TypeConName
        enum_con_str: str
        enum_con_interned_str: int
        def __init__(self, tycon: _Optional[_Union[TypeConName, _Mapping]] = ..., enum_con_str: _Optional[str] = ..., enum_con_interned_str: _Optional[int] = ...) -> None: ...
    class StructCon(_message.Message):
        __slots__ = ["fields"]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedCompositeFieldContainer[FieldWithExpr]
        def __init__(self, fields: _Optional[_Iterable[_Union[FieldWithExpr, _Mapping]]] = ...) -> None: ...
    class StructProj(_message.Message):
        __slots__ = ["field_str", "field_interned_str", "struct"]
        FIELD_STR_FIELD_NUMBER: _ClassVar[int]
        FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        STRUCT_FIELD_NUMBER: _ClassVar[int]
        field_str: str
        field_interned_str: int
        struct: Expr
        def __init__(self, field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ..., struct: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class StructUpd(_message.Message):
        __slots__ = ["field_str", "field_interned_str", "struct", "update"]
        FIELD_STR_FIELD_NUMBER: _ClassVar[int]
        FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        STRUCT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        field_str: str
        field_interned_str: int
        struct: Expr
        update: Expr
        def __init__(self, field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ..., struct: _Optional[_Union[Expr, _Mapping]] = ..., update: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class App(_message.Message):
        __slots__ = ["fun", "args"]
        FUN_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        fun: Expr
        args: _containers.RepeatedCompositeFieldContainer[Expr]
        def __init__(self, fun: _Optional[_Union[Expr, _Mapping]] = ..., args: _Optional[_Iterable[_Union[Expr, _Mapping]]] = ...) -> None: ...
    class TyApp(_message.Message):
        __slots__ = ["expr", "types"]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        TYPES_FIELD_NUMBER: _ClassVar[int]
        expr: Expr
        types: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, expr: _Optional[_Union[Expr, _Mapping]] = ..., types: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class Abs(_message.Message):
        __slots__ = ["param", "body"]
        PARAM_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        param: _containers.RepeatedCompositeFieldContainer[VarWithType]
        body: Expr
        def __init__(self, param: _Optional[_Iterable[_Union[VarWithType, _Mapping]]] = ..., body: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class TyAbs(_message.Message):
        __slots__ = ["param", "body"]
        PARAM_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        param: _containers.RepeatedCompositeFieldContainer[TypeVarWithKind]
        body: Expr
        def __init__(self, param: _Optional[_Iterable[_Union[TypeVarWithKind, _Mapping]]] = ..., body: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class Nil(_message.Message):
        __slots__ = ["type"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: Type
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    class Cons(_message.Message):
        __slots__ = ["type", "front", "tail"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        FRONT_FIELD_NUMBER: _ClassVar[int]
        TAIL_FIELD_NUMBER: _ClassVar[int]
        type: Type
        front: _containers.RepeatedCompositeFieldContainer[Expr]
        tail: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., front: _Optional[_Iterable[_Union[Expr, _Mapping]]] = ..., tail: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class OptionalNone(_message.Message):
        __slots__ = ["type"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: Type
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    class OptionalSome(_message.Message):
        __slots__ = ["type", "body"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        type: Type
        body: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., body: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ToAny(_message.Message):
        __slots__ = ["type", "expr"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        type: Type
        expr: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class FromAny(_message.Message):
        __slots__ = ["type", "expr"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        type: Type
        expr: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ToAnyException(_message.Message):
        __slots__ = ["type", "expr"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        type: Type
        expr: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class FromAnyException(_message.Message):
        __slots__ = ["type", "expr"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        type: Type
        expr: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class Throw(_message.Message):
        __slots__ = ["return_type", "exception_type", "exception_expr"]
        RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
        EXCEPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        EXCEPTION_EXPR_FIELD_NUMBER: _ClassVar[int]
        return_type: Type
        exception_type: Type
        exception_expr: Expr
        def __init__(self, return_type: _Optional[_Union[Type, _Mapping]] = ..., exception_type: _Optional[_Union[Type, _Mapping]] = ..., exception_expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ToInterface(_message.Message):
        __slots__ = ["interface_type", "template_type", "template_expr"]
        INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_EXPR_FIELD_NUMBER: _ClassVar[int]
        interface_type: TypeConName
        template_type: TypeConName
        template_expr: Expr
        def __init__(self, interface_type: _Optional[_Union[TypeConName, _Mapping]] = ..., template_type: _Optional[_Union[TypeConName, _Mapping]] = ..., template_expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class FromInterface(_message.Message):
        __slots__ = ["interface_type", "template_type", "interface_expr"]
        INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_EXPR_FIELD_NUMBER: _ClassVar[int]
        interface_type: TypeConName
        template_type: TypeConName
        interface_expr: Expr
        def __init__(self, interface_type: _Optional[_Union[TypeConName, _Mapping]] = ..., template_type: _Optional[_Union[TypeConName, _Mapping]] = ..., interface_expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class CallInterface(_message.Message):
        __slots__ = ["interface_type", "method_interned_name", "interface_expr"]
        INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
        METHOD_INTERNED_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_EXPR_FIELD_NUMBER: _ClassVar[int]
        interface_type: TypeConName
        method_interned_name: int
        interface_expr: Expr
        def __init__(self, interface_type: _Optional[_Union[TypeConName, _Mapping]] = ..., method_interned_name: _Optional[int] = ..., interface_expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ViewInterface(_message.Message):
        __slots__ = ["interface", "expr"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        expr: Expr
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class SignatoryInterface(_message.Message):
        __slots__ = ["interface", "expr"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        expr: Expr
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ObserverInterface(_message.Message):
        __slots__ = ["interface", "expr"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        expr: Expr
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class UnsafeFromInterface(_message.Message):
        __slots__ = ["interface_type", "template_type", "contract_id_expr", "interface_expr"]
        INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ID_EXPR_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_EXPR_FIELD_NUMBER: _ClassVar[int]
        interface_type: TypeConName
        template_type: TypeConName
        contract_id_expr: Expr
        interface_expr: Expr
        def __init__(self, interface_type: _Optional[_Union[TypeConName, _Mapping]] = ..., template_type: _Optional[_Union[TypeConName, _Mapping]] = ..., contract_id_expr: _Optional[_Union[Expr, _Mapping]] = ..., interface_expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ToRequiredInterface(_message.Message):
        __slots__ = ["required_interface", "requiring_interface", "expr"]
        REQUIRED_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        REQUIRING_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        required_interface: TypeConName
        requiring_interface: TypeConName
        expr: Expr
        def __init__(self, required_interface: _Optional[_Union[TypeConName, _Mapping]] = ..., requiring_interface: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class FromRequiredInterface(_message.Message):
        __slots__ = ["required_interface", "requiring_interface", "expr"]
        REQUIRED_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        REQUIRING_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        required_interface: TypeConName
        requiring_interface: TypeConName
        expr: Expr
        def __init__(self, required_interface: _Optional[_Union[TypeConName, _Mapping]] = ..., requiring_interface: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class UnsafeFromRequiredInterface(_message.Message):
        __slots__ = ["required_interface", "requiring_interface", "contract_id_expr", "interface_expr"]
        REQUIRED_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        REQUIRING_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ID_EXPR_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_EXPR_FIELD_NUMBER: _ClassVar[int]
        required_interface: TypeConName
        requiring_interface: TypeConName
        contract_id_expr: Expr
        interface_expr: Expr
        def __init__(self, required_interface: _Optional[_Union[TypeConName, _Mapping]] = ..., requiring_interface: _Optional[_Union[TypeConName, _Mapping]] = ..., contract_id_expr: _Optional[_Union[Expr, _Mapping]] = ..., interface_expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class InterfaceTemplateTypeRep(_message.Message):
        __slots__ = ["interface", "expr"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        expr: Expr
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class Experimental(_message.Message):
        __slots__ = ["name", "type"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: Type
        def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VAR_STR_FIELD_NUMBER: _ClassVar[int]
    VAR_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    BUILTIN_FIELD_NUMBER: _ClassVar[int]
    PRIM_CON_FIELD_NUMBER: _ClassVar[int]
    PRIM_LIT_FIELD_NUMBER: _ClassVar[int]
    REC_CON_FIELD_NUMBER: _ClassVar[int]
    REC_PROJ_FIELD_NUMBER: _ClassVar[int]
    REC_UPD_FIELD_NUMBER: _ClassVar[int]
    VARIANT_CON_FIELD_NUMBER: _ClassVar[int]
    ENUM_CON_FIELD_NUMBER: _ClassVar[int]
    STRUCT_CON_FIELD_NUMBER: _ClassVar[int]
    STRUCT_PROJ_FIELD_NUMBER: _ClassVar[int]
    STRUCT_UPD_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    TY_APP_FIELD_NUMBER: _ClassVar[int]
    ABS_FIELD_NUMBER: _ClassVar[int]
    TY_ABS_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    LET_FIELD_NUMBER: _ClassVar[int]
    NIL_FIELD_NUMBER: _ClassVar[int]
    CONS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NONE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SOME_FIELD_NUMBER: _ClassVar[int]
    TO_ANY_FIELD_NUMBER: _ClassVar[int]
    FROM_ANY_FIELD_NUMBER: _ClassVar[int]
    TYPE_REP_FIELD_NUMBER: _ClassVar[int]
    TO_ANY_EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    FROM_ANY_EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    THROW_FIELD_NUMBER: _ClassVar[int]
    TO_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    FROM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    CALL_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    SIGNATORY_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    OBSERVER_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    VIEW_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    UNSAFE_FROM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TEMPLATE_TYPE_REP_FIELD_NUMBER: _ClassVar[int]
    TO_REQUIRED_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    FROM_REQUIRED_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    UNSAFE_FROM_REQUIRED_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_FIELD_NUMBER: _ClassVar[int]
    location: Location
    var_str: str
    var_interned_str: int
    val: ValName
    builtin: BuiltinFunction
    prim_con: PrimCon
    prim_lit: PrimLit
    rec_con: Expr.RecCon
    rec_proj: Expr.RecProj
    rec_upd: Expr.RecUpd
    variant_con: Expr.VariantCon
    enum_con: Expr.EnumCon
    struct_con: Expr.StructCon
    struct_proj: Expr.StructProj
    struct_upd: Expr.StructUpd
    app: Expr.App
    ty_app: Expr.TyApp
    abs: Expr.Abs
    ty_abs: Expr.TyAbs
    case: Case
    let: Block
    nil: Expr.Nil
    cons: Expr.Cons
    update: Update
    scenario: Scenario
    optional_none: Expr.OptionalNone
    optional_some: Expr.OptionalSome
    to_any: Expr.ToAny
    from_any: Expr.FromAny
    type_rep: Type
    to_any_exception: Expr.ToAnyException
    from_any_exception: Expr.FromAnyException
    throw: Expr.Throw
    to_interface: Expr.ToInterface
    from_interface: Expr.FromInterface
    call_interface: Expr.CallInterface
    signatory_interface: Expr.SignatoryInterface
    observer_interface: Expr.ObserverInterface
    view_interface: Expr.ViewInterface
    unsafe_from_interface: Expr.UnsafeFromInterface
    interface_template_type_rep: Expr.InterfaceTemplateTypeRep
    to_required_interface: Expr.ToRequiredInterface
    from_required_interface: Expr.FromRequiredInterface
    unsafe_from_required_interface: Expr.UnsafeFromRequiredInterface
    experimental: Expr.Experimental
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., var_str: _Optional[str] = ..., var_interned_str: _Optional[int] = ..., val: _Optional[_Union[ValName, _Mapping]] = ..., builtin: _Optional[_Union[BuiltinFunction, str]] = ..., prim_con: _Optional[_Union[PrimCon, str]] = ..., prim_lit: _Optional[_Union[PrimLit, _Mapping]] = ..., rec_con: _Optional[_Union[Expr.RecCon, _Mapping]] = ..., rec_proj: _Optional[_Union[Expr.RecProj, _Mapping]] = ..., rec_upd: _Optional[_Union[Expr.RecUpd, _Mapping]] = ..., variant_con: _Optional[_Union[Expr.VariantCon, _Mapping]] = ..., enum_con: _Optional[_Union[Expr.EnumCon, _Mapping]] = ..., struct_con: _Optional[_Union[Expr.StructCon, _Mapping]] = ..., struct_proj: _Optional[_Union[Expr.StructProj, _Mapping]] = ..., struct_upd: _Optional[_Union[Expr.StructUpd, _Mapping]] = ..., app: _Optional[_Union[Expr.App, _Mapping]] = ..., ty_app: _Optional[_Union[Expr.TyApp, _Mapping]] = ..., abs: _Optional[_Union[Expr.Abs, _Mapping]] = ..., ty_abs: _Optional[_Union[Expr.TyAbs, _Mapping]] = ..., case: _Optional[_Union[Case, _Mapping]] = ..., let: _Optional[_Union[Block, _Mapping]] = ..., nil: _Optional[_Union[Expr.Nil, _Mapping]] = ..., cons: _Optional[_Union[Expr.Cons, _Mapping]] = ..., update: _Optional[_Union[Update, _Mapping]] = ..., scenario: _Optional[_Union[Scenario, _Mapping]] = ..., optional_none: _Optional[_Union[Expr.OptionalNone, _Mapping]] = ..., optional_some: _Optional[_Union[Expr.OptionalSome, _Mapping]] = ..., to_any: _Optional[_Union[Expr.ToAny, _Mapping]] = ..., from_any: _Optional[_Union[Expr.FromAny, _Mapping]] = ..., type_rep: _Optional[_Union[Type, _Mapping]] = ..., to_any_exception: _Optional[_Union[Expr.ToAnyException, _Mapping]] = ..., from_any_exception: _Optional[_Union[Expr.FromAnyException, _Mapping]] = ..., throw: _Optional[_Union[Expr.Throw, _Mapping]] = ..., to_interface: _Optional[_Union[Expr.ToInterface, _Mapping]] = ..., from_interface: _Optional[_Union[Expr.FromInterface, _Mapping]] = ..., call_interface: _Optional[_Union[Expr.CallInterface, _Mapping]] = ..., signatory_interface: _Optional[_Union[Expr.SignatoryInterface, _Mapping]] = ..., observer_interface: _Optional[_Union[Expr.ObserverInterface, _Mapping]] = ..., view_interface: _Optional[_Union[Expr.ViewInterface, _Mapping]] = ..., unsafe_from_interface: _Optional[_Union[Expr.UnsafeFromInterface, _Mapping]] = ..., interface_template_type_rep: _Optional[_Union[Expr.InterfaceTemplateTypeRep, _Mapping]] = ..., to_required_interface: _Optional[_Union[Expr.ToRequiredInterface, _Mapping]] = ..., from_required_interface: _Optional[_Union[Expr.FromRequiredInterface, _Mapping]] = ..., unsafe_from_required_interface: _Optional[_Union[Expr.UnsafeFromRequiredInterface, _Mapping]] = ..., experimental: _Optional[_Union[Expr.Experimental, _Mapping]] = ...) -> None: ...

class CaseAlt(_message.Message):
    __slots__ = ["default", "variant", "prim_con", "nil", "cons", "optional_none", "optional_some", "enum", "body"]
    class Variant(_message.Message):
        __slots__ = ["con", "variant_str", "variant_interned_str", "binder_str", "binder_interned_str"]
        CON_FIELD_NUMBER: _ClassVar[int]
        VARIANT_STR_FIELD_NUMBER: _ClassVar[int]
        VARIANT_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        BINDER_STR_FIELD_NUMBER: _ClassVar[int]
        BINDER_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        con: TypeConName
        variant_str: str
        variant_interned_str: int
        binder_str: str
        binder_interned_str: int
        def __init__(self, con: _Optional[_Union[TypeConName, _Mapping]] = ..., variant_str: _Optional[str] = ..., variant_interned_str: _Optional[int] = ..., binder_str: _Optional[str] = ..., binder_interned_str: _Optional[int] = ...) -> None: ...
    class Enum(_message.Message):
        __slots__ = ["con", "constructor_str", "constructor_interned_str"]
        CON_FIELD_NUMBER: _ClassVar[int]
        CONSTRUCTOR_STR_FIELD_NUMBER: _ClassVar[int]
        CONSTRUCTOR_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        con: TypeConName
        constructor_str: str
        constructor_interned_str: int
        def __init__(self, con: _Optional[_Union[TypeConName, _Mapping]] = ..., constructor_str: _Optional[str] = ..., constructor_interned_str: _Optional[int] = ...) -> None: ...
    class Cons(_message.Message):
        __slots__ = ["var_head_str", "var_head_interned_str", "var_tail_str", "var_tail_interned_str"]
        VAR_HEAD_STR_FIELD_NUMBER: _ClassVar[int]
        VAR_HEAD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        VAR_TAIL_STR_FIELD_NUMBER: _ClassVar[int]
        VAR_TAIL_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        var_head_str: str
        var_head_interned_str: int
        var_tail_str: str
        var_tail_interned_str: int
        def __init__(self, var_head_str: _Optional[str] = ..., var_head_interned_str: _Optional[int] = ..., var_tail_str: _Optional[str] = ..., var_tail_interned_str: _Optional[int] = ...) -> None: ...
    class OptionalSome(_message.Message):
        __slots__ = ["var_body_str", "var_body_interned_str"]
        VAR_BODY_STR_FIELD_NUMBER: _ClassVar[int]
        VAR_BODY_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        var_body_str: str
        var_body_interned_str: int
        def __init__(self, var_body_str: _Optional[str] = ..., var_body_interned_str: _Optional[int] = ...) -> None: ...
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    PRIM_CON_FIELD_NUMBER: _ClassVar[int]
    NIL_FIELD_NUMBER: _ClassVar[int]
    CONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NONE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SOME_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    default: Unit
    variant: CaseAlt.Variant
    prim_con: PrimCon
    nil: Unit
    cons: CaseAlt.Cons
    optional_none: Unit
    optional_some: CaseAlt.OptionalSome
    enum: CaseAlt.Enum
    body: Expr
    def __init__(self, default: _Optional[_Union[Unit, _Mapping]] = ..., variant: _Optional[_Union[CaseAlt.Variant, _Mapping]] = ..., prim_con: _Optional[_Union[PrimCon, str]] = ..., nil: _Optional[_Union[Unit, _Mapping]] = ..., cons: _Optional[_Union[CaseAlt.Cons, _Mapping]] = ..., optional_none: _Optional[_Union[Unit, _Mapping]] = ..., optional_some: _Optional[_Union[CaseAlt.OptionalSome, _Mapping]] = ..., enum: _Optional[_Union[CaseAlt.Enum, _Mapping]] = ..., body: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class Case(_message.Message):
    __slots__ = ["scrut", "alts"]
    SCRUT_FIELD_NUMBER: _ClassVar[int]
    ALTS_FIELD_NUMBER: _ClassVar[int]
    scrut: Expr
    alts: _containers.RepeatedCompositeFieldContainer[CaseAlt]
    def __init__(self, scrut: _Optional[_Union[Expr, _Mapping]] = ..., alts: _Optional[_Iterable[_Union[CaseAlt, _Mapping]]] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ["bindings", "body"]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    bindings: _containers.RepeatedCompositeFieldContainer[Binding]
    body: Expr
    def __init__(self, bindings: _Optional[_Iterable[_Union[Binding, _Mapping]]] = ..., body: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class Pure(_message.Message):
    __slots__ = ["type", "expr"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    type: Type
    expr: Expr
    def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class Update(_message.Message):
    __slots__ = ["pure", "block", "create", "exercise", "exercise_by_key", "fetch", "get_time", "lookup_by_key", "fetch_by_key", "embed_expr", "try_catch", "create_interface", "exercise_interface", "fetch_interface"]
    class Create(_message.Message):
        __slots__ = ["template", "expr"]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        template: TypeConName
        expr: Expr
        def __init__(self, template: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class CreateInterface(_message.Message):
        __slots__ = ["interface", "expr"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        expr: Expr
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class Exercise(_message.Message):
        __slots__ = ["template", "choice_str", "choice_interned_str", "cid", "arg"]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        CHOICE_STR_FIELD_NUMBER: _ClassVar[int]
        CHOICE_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        CID_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        template: TypeConName
        choice_str: str
        choice_interned_str: int
        cid: Expr
        arg: Expr
        def __init__(self, template: _Optional[_Union[TypeConName, _Mapping]] = ..., choice_str: _Optional[str] = ..., choice_interned_str: _Optional[int] = ..., cid: _Optional[_Union[Expr, _Mapping]] = ..., arg: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ExerciseInterface(_message.Message):
        __slots__ = ["interface", "choice_interned_str", "cid", "arg", "guard"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        CHOICE_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        CID_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        GUARD_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        choice_interned_str: int
        cid: Expr
        arg: Expr
        guard: Expr
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., choice_interned_str: _Optional[int] = ..., cid: _Optional[_Union[Expr, _Mapping]] = ..., arg: _Optional[_Union[Expr, _Mapping]] = ..., guard: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class ExerciseByKey(_message.Message):
        __slots__ = ["template", "choice_interned_str", "key", "arg"]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        CHOICE_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        template: TypeConName
        choice_interned_str: int
        key: Expr
        arg: Expr
        def __init__(self, template: _Optional[_Union[TypeConName, _Mapping]] = ..., choice_interned_str: _Optional[int] = ..., key: _Optional[_Union[Expr, _Mapping]] = ..., arg: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class Fetch(_message.Message):
        __slots__ = ["template", "cid"]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        CID_FIELD_NUMBER: _ClassVar[int]
        template: TypeConName
        cid: Expr
        def __init__(self, template: _Optional[_Union[TypeConName, _Mapping]] = ..., cid: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class FetchInterface(_message.Message):
        __slots__ = ["interface", "cid"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        CID_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        cid: Expr
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., cid: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class EmbedExpr(_message.Message):
        __slots__ = ["type", "body"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        type: Type
        body: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., body: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class RetrieveByKey(_message.Message):
        __slots__ = ["template", "key"]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        template: TypeConName
        key: Expr
        def __init__(self, template: _Optional[_Union[TypeConName, _Mapping]] = ..., key: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class TryCatch(_message.Message):
        __slots__ = ["return_type", "try_expr", "var_interned_str", "catch_expr"]
        RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRY_EXPR_FIELD_NUMBER: _ClassVar[int]
        VAR_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        CATCH_EXPR_FIELD_NUMBER: _ClassVar[int]
        return_type: Type
        try_expr: Expr
        var_interned_str: int
        catch_expr: Expr
        def __init__(self, return_type: _Optional[_Union[Type, _Mapping]] = ..., try_expr: _Optional[_Union[Expr, _Mapping]] = ..., var_interned_str: _Optional[int] = ..., catch_expr: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    PURE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    GET_TIME_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    FETCH_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    EMBED_EXPR_FIELD_NUMBER: _ClassVar[int]
    TRY_CATCH_FIELD_NUMBER: _ClassVar[int]
    CREATE_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    FETCH_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    pure: Pure
    block: Block
    create: Update.Create
    exercise: Update.Exercise
    exercise_by_key: Update.ExerciseByKey
    fetch: Update.Fetch
    get_time: Unit
    lookup_by_key: Update.RetrieveByKey
    fetch_by_key: Update.RetrieveByKey
    embed_expr: Update.EmbedExpr
    try_catch: Update.TryCatch
    create_interface: Update.CreateInterface
    exercise_interface: Update.ExerciseInterface
    fetch_interface: Update.FetchInterface
    def __init__(self, pure: _Optional[_Union[Pure, _Mapping]] = ..., block: _Optional[_Union[Block, _Mapping]] = ..., create: _Optional[_Union[Update.Create, _Mapping]] = ..., exercise: _Optional[_Union[Update.Exercise, _Mapping]] = ..., exercise_by_key: _Optional[_Union[Update.ExerciseByKey, _Mapping]] = ..., fetch: _Optional[_Union[Update.Fetch, _Mapping]] = ..., get_time: _Optional[_Union[Unit, _Mapping]] = ..., lookup_by_key: _Optional[_Union[Update.RetrieveByKey, _Mapping]] = ..., fetch_by_key: _Optional[_Union[Update.RetrieveByKey, _Mapping]] = ..., embed_expr: _Optional[_Union[Update.EmbedExpr, _Mapping]] = ..., try_catch: _Optional[_Union[Update.TryCatch, _Mapping]] = ..., create_interface: _Optional[_Union[Update.CreateInterface, _Mapping]] = ..., exercise_interface: _Optional[_Union[Update.ExerciseInterface, _Mapping]] = ..., fetch_interface: _Optional[_Union[Update.FetchInterface, _Mapping]] = ...) -> None: ...

class Scenario(_message.Message):
    __slots__ = ["pure", "block", "commit", "mustFailAt", "get_time", "get_party", "embed_expr"]
    class Commit(_message.Message):
        __slots__ = ["party", "expr", "ret_type"]
        PARTY_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        RET_TYPE_FIELD_NUMBER: _ClassVar[int]
        party: Expr
        expr: Expr
        ret_type: Type
        def __init__(self, party: _Optional[_Union[Expr, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ..., ret_type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    class EmbedExpr(_message.Message):
        __slots__ = ["type", "body"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        type: Type
        body: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., body: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    PURE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    MUSTFAILAT_FIELD_NUMBER: _ClassVar[int]
    PASS_FIELD_NUMBER: _ClassVar[int]
    GET_TIME_FIELD_NUMBER: _ClassVar[int]
    GET_PARTY_FIELD_NUMBER: _ClassVar[int]
    EMBED_EXPR_FIELD_NUMBER: _ClassVar[int]
    pure: Pure
    block: Block
    commit: Scenario.Commit
    mustFailAt: Scenario.Commit
    get_time: Unit
    get_party: Expr
    embed_expr: Scenario.EmbedExpr
    def __init__(self, pure: _Optional[_Union[Pure, _Mapping]] = ..., block: _Optional[_Union[Block, _Mapping]] = ..., commit: _Optional[_Union[Scenario.Commit, _Mapping]] = ..., mustFailAt: _Optional[_Union[Scenario.Commit, _Mapping]] = ..., get_time: _Optional[_Union[Unit, _Mapping]] = ..., get_party: _Optional[_Union[Expr, _Mapping]] = ..., embed_expr: _Optional[_Union[Scenario.EmbedExpr, _Mapping]] = ..., **kwargs) -> None: ...

class TemplateChoice(_message.Message):
    __slots__ = ["name_str", "name_interned_str", "consuming", "controllers", "observers", "arg_binder", "ret_type", "update", "self_binder_str", "self_binder_interned_str", "location"]
    NAME_STR_FIELD_NUMBER: _ClassVar[int]
    NAME_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    CONSUMING_FIELD_NUMBER: _ClassVar[int]
    CONTROLLERS_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    ARG_BINDER_FIELD_NUMBER: _ClassVar[int]
    RET_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    SELF_BINDER_STR_FIELD_NUMBER: _ClassVar[int]
    SELF_BINDER_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name_str: str
    name_interned_str: int
    consuming: bool
    controllers: Expr
    observers: Expr
    arg_binder: VarWithType
    ret_type: Type
    update: Expr
    self_binder_str: str
    self_binder_interned_str: int
    location: Location
    def __init__(self, name_str: _Optional[str] = ..., name_interned_str: _Optional[int] = ..., consuming: bool = ..., controllers: _Optional[_Union[Expr, _Mapping]] = ..., observers: _Optional[_Union[Expr, _Mapping]] = ..., arg_binder: _Optional[_Union[VarWithType, _Mapping]] = ..., ret_type: _Optional[_Union[Type, _Mapping]] = ..., update: _Optional[_Union[Expr, _Mapping]] = ..., self_binder_str: _Optional[str] = ..., self_binder_interned_str: _Optional[int] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class KeyExpr(_message.Message):
    __slots__ = ["projections", "record"]
    class Projection(_message.Message):
        __slots__ = ["tycon", "field_str", "field_interned_str"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        FIELD_STR_FIELD_NUMBER: _ClassVar[int]
        FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        tycon: Type.Con
        field_str: str
        field_interned_str: int
        def __init__(self, tycon: _Optional[_Union[Type.Con, _Mapping]] = ..., field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ...) -> None: ...
    class Projections(_message.Message):
        __slots__ = ["projections"]
        PROJECTIONS_FIELD_NUMBER: _ClassVar[int]
        projections: _containers.RepeatedCompositeFieldContainer[KeyExpr.Projection]
        def __init__(self, projections: _Optional[_Iterable[_Union[KeyExpr.Projection, _Mapping]]] = ...) -> None: ...
    class RecordField(_message.Message):
        __slots__ = ["field_str", "field_interned_str", "expr"]
        FIELD_STR_FIELD_NUMBER: _ClassVar[int]
        FIELD_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        EXPR_FIELD_NUMBER: _ClassVar[int]
        field_str: str
        field_interned_str: int
        expr: KeyExpr
        def __init__(self, field_str: _Optional[str] = ..., field_interned_str: _Optional[int] = ..., expr: _Optional[_Union[KeyExpr, _Mapping]] = ...) -> None: ...
    class Record(_message.Message):
        __slots__ = ["tycon", "fields"]
        TYCON_FIELD_NUMBER: _ClassVar[int]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        tycon: Type.Con
        fields: _containers.RepeatedCompositeFieldContainer[KeyExpr.RecordField]
        def __init__(self, tycon: _Optional[_Union[Type.Con, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[KeyExpr.RecordField, _Mapping]]] = ...) -> None: ...
    PROJECTIONS_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    projections: KeyExpr.Projections
    record: KeyExpr.Record
    def __init__(self, projections: _Optional[_Union[KeyExpr.Projections, _Mapping]] = ..., record: _Optional[_Union[KeyExpr.Record, _Mapping]] = ...) -> None: ...

class InterfaceInstanceBody(_message.Message):
    __slots__ = ["methods", "view"]
    class InterfaceInstanceMethod(_message.Message):
        __slots__ = ["method_interned_name", "value"]
        METHOD_INTERNED_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        method_interned_name: int
        value: Expr
        def __init__(self, method_interned_name: _Optional[int] = ..., value: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    METHODS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    methods: _containers.RepeatedCompositeFieldContainer[InterfaceInstanceBody.InterfaceInstanceMethod]
    view: Expr
    def __init__(self, methods: _Optional[_Iterable[_Union[InterfaceInstanceBody.InterfaceInstanceMethod, _Mapping]]] = ..., view: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class DefTemplate(_message.Message):
    __slots__ = ["tycon_dname", "tycon_interned_dname", "param_str", "param_interned_str", "precond", "signatories", "agreement", "choices", "observers", "location", "key", "implements"]
    class DefKey(_message.Message):
        __slots__ = ["type", "key", "complex_key", "maintainers"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        COMPLEX_KEY_FIELD_NUMBER: _ClassVar[int]
        MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        type: Type
        key: KeyExpr
        complex_key: Expr
        maintainers: Expr
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., key: _Optional[_Union[KeyExpr, _Mapping]] = ..., complex_key: _Optional[_Union[Expr, _Mapping]] = ..., maintainers: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class Implements(_message.Message):
        __slots__ = ["interface", "body"]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        interface: TypeConName
        body: InterfaceInstanceBody
        def __init__(self, interface: _Optional[_Union[TypeConName, _Mapping]] = ..., body: _Optional[_Union[InterfaceInstanceBody, _Mapping]] = ...) -> None: ...
    TYCON_DNAME_FIELD_NUMBER: _ClassVar[int]
    TYCON_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    PARAM_STR_FIELD_NUMBER: _ClassVar[int]
    PARAM_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    PRECOND_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTS_FIELD_NUMBER: _ClassVar[int]
    tycon_dname: DottedName
    tycon_interned_dname: int
    param_str: str
    param_interned_str: int
    precond: Expr
    signatories: Expr
    agreement: Expr
    choices: _containers.RepeatedCompositeFieldContainer[TemplateChoice]
    observers: Expr
    location: Location
    key: DefTemplate.DefKey
    implements: _containers.RepeatedCompositeFieldContainer[DefTemplate.Implements]
    def __init__(self, tycon_dname: _Optional[_Union[DottedName, _Mapping]] = ..., tycon_interned_dname: _Optional[int] = ..., param_str: _Optional[str] = ..., param_interned_str: _Optional[int] = ..., precond: _Optional[_Union[Expr, _Mapping]] = ..., signatories: _Optional[_Union[Expr, _Mapping]] = ..., agreement: _Optional[_Union[Expr, _Mapping]] = ..., choices: _Optional[_Iterable[_Union[TemplateChoice, _Mapping]]] = ..., observers: _Optional[_Union[Expr, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., key: _Optional[_Union[DefTemplate.DefKey, _Mapping]] = ..., implements: _Optional[_Iterable[_Union[DefTemplate.Implements, _Mapping]]] = ...) -> None: ...

class InterfaceMethod(_message.Message):
    __slots__ = ["location", "method_interned_name", "type"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    METHOD_INTERNED_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    location: Location
    method_interned_name: int
    type: Type
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., method_interned_name: _Optional[int] = ..., type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...

class DefInterface(_message.Message):
    __slots__ = ["location", "tycon_interned_dname", "methods", "param_interned_str", "choices", "coImplements", "view", "requires"]
    class CoImplements(_message.Message):
        __slots__ = ["template", "body"]
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        template: TypeConName
        body: InterfaceInstanceBody
        def __init__(self, template: _Optional[_Union[TypeConName, _Mapping]] = ..., body: _Optional[_Union[InterfaceInstanceBody, _Mapping]] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYCON_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    PARAM_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    COIMPLEMENTS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_FIELD_NUMBER: _ClassVar[int]
    location: Location
    tycon_interned_dname: int
    methods: _containers.RepeatedCompositeFieldContainer[InterfaceMethod]
    param_interned_str: int
    choices: _containers.RepeatedCompositeFieldContainer[TemplateChoice]
    coImplements: _containers.RepeatedCompositeFieldContainer[DefInterface.CoImplements]
    view: Type
    requires: _containers.RepeatedCompositeFieldContainer[TypeConName]
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., tycon_interned_dname: _Optional[int] = ..., methods: _Optional[_Iterable[_Union[InterfaceMethod, _Mapping]]] = ..., param_interned_str: _Optional[int] = ..., choices: _Optional[_Iterable[_Union[TemplateChoice, _Mapping]]] = ..., coImplements: _Optional[_Iterable[_Union[DefInterface.CoImplements, _Mapping]]] = ..., view: _Optional[_Union[Type, _Mapping]] = ..., requires: _Optional[_Iterable[_Union[TypeConName, _Mapping]]] = ...) -> None: ...

class DefException(_message.Message):
    __slots__ = ["name_interned_dname", "location", "message"]
    NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    name_interned_dname: int
    location: Location
    message: Expr
    def __init__(self, name_interned_dname: _Optional[int] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., message: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class DefDataType(_message.Message):
    __slots__ = ["name_dname", "name_interned_dname", "params", "record", "variant", "enum", "interface", "serializable", "location"]
    class Fields(_message.Message):
        __slots__ = ["fields"]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedCompositeFieldContainer[FieldWithType]
        def __init__(self, fields: _Optional[_Iterable[_Union[FieldWithType, _Mapping]]] = ...) -> None: ...
    class EnumConstructors(_message.Message):
        __slots__ = ["constructors_str", "constructors_interned_str"]
        CONSTRUCTORS_STR_FIELD_NUMBER: _ClassVar[int]
        CONSTRUCTORS_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
        constructors_str: _containers.RepeatedScalarFieldContainer[str]
        constructors_interned_str: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, constructors_str: _Optional[_Iterable[str]] = ..., constructors_interned_str: _Optional[_Iterable[int]] = ...) -> None: ...
    NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZABLE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name_dname: DottedName
    name_interned_dname: int
    params: _containers.RepeatedCompositeFieldContainer[TypeVarWithKind]
    record: DefDataType.Fields
    variant: DefDataType.Fields
    enum: DefDataType.EnumConstructors
    interface: Unit
    serializable: bool
    location: Location
    def __init__(self, name_dname: _Optional[_Union[DottedName, _Mapping]] = ..., name_interned_dname: _Optional[int] = ..., params: _Optional[_Iterable[_Union[TypeVarWithKind, _Mapping]]] = ..., record: _Optional[_Union[DefDataType.Fields, _Mapping]] = ..., variant: _Optional[_Union[DefDataType.Fields, _Mapping]] = ..., enum: _Optional[_Union[DefDataType.EnumConstructors, _Mapping]] = ..., interface: _Optional[_Union[Unit, _Mapping]] = ..., serializable: bool = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class DefTypeSyn(_message.Message):
    __slots__ = ["name_dname", "name_interned_dname", "params", "type", "location"]
    NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name_dname: DottedName
    name_interned_dname: int
    params: _containers.RepeatedCompositeFieldContainer[TypeVarWithKind]
    type: Type
    location: Location
    def __init__(self, name_dname: _Optional[_Union[DottedName, _Mapping]] = ..., name_interned_dname: _Optional[int] = ..., params: _Optional[_Iterable[_Union[TypeVarWithKind, _Mapping]]] = ..., type: _Optional[_Union[Type, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class DefValue(_message.Message):
    __slots__ = ["name_with_type", "expr", "no_party_literals", "is_test", "location"]
    class NameWithType(_message.Message):
        __slots__ = ["name_dname", "name_interned_dname", "type"]
        NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
        NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name_dname: _containers.RepeatedScalarFieldContainer[str]
        name_interned_dname: int
        type: Type
        def __init__(self, name_dname: _Optional[_Iterable[str]] = ..., name_interned_dname: _Optional[int] = ..., type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    NAME_WITH_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    NO_PARTY_LITERALS_FIELD_NUMBER: _ClassVar[int]
    IS_TEST_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name_with_type: DefValue.NameWithType
    expr: Expr
    no_party_literals: bool
    is_test: bool
    location: Location
    def __init__(self, name_with_type: _Optional[_Union[DefValue.NameWithType, _Mapping]] = ..., expr: _Optional[_Union[Expr, _Mapping]] = ..., no_party_literals: bool = ..., is_test: bool = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class FeatureFlags(_message.Message):
    __slots__ = ["forbidPartyLiterals", "dontDivulgeContractIdsInCreateArguments", "dontDiscloseNonConsumingChoicesToObservers"]
    FORBIDPARTYLITERALS_FIELD_NUMBER: _ClassVar[int]
    DONTDIVULGECONTRACTIDSINCREATEARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    DONTDISCLOSENONCONSUMINGCHOICESTOOBSERVERS_FIELD_NUMBER: _ClassVar[int]
    forbidPartyLiterals: bool
    dontDivulgeContractIdsInCreateArguments: bool
    dontDiscloseNonConsumingChoicesToObservers: bool
    def __init__(self, forbidPartyLiterals: bool = ..., dontDivulgeContractIdsInCreateArguments: bool = ..., dontDiscloseNonConsumingChoicesToObservers: bool = ...) -> None: ...

class Module(_message.Message):
    __slots__ = ["name_dname", "name_interned_dname", "flags", "synonyms", "data_types", "values", "templates", "exceptions", "interfaces"]
    NAME_DNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_INTERNED_DNAME_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    SYNONYMS_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPES_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONS_FIELD_NUMBER: _ClassVar[int]
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    name_dname: DottedName
    name_interned_dname: int
    flags: FeatureFlags
    synonyms: _containers.RepeatedCompositeFieldContainer[DefTypeSyn]
    data_types: _containers.RepeatedCompositeFieldContainer[DefDataType]
    values: _containers.RepeatedCompositeFieldContainer[DefValue]
    templates: _containers.RepeatedCompositeFieldContainer[DefTemplate]
    exceptions: _containers.RepeatedCompositeFieldContainer[DefException]
    interfaces: _containers.RepeatedCompositeFieldContainer[DefInterface]
    def __init__(self, name_dname: _Optional[_Union[DottedName, _Mapping]] = ..., name_interned_dname: _Optional[int] = ..., flags: _Optional[_Union[FeatureFlags, _Mapping]] = ..., synonyms: _Optional[_Iterable[_Union[DefTypeSyn, _Mapping]]] = ..., data_types: _Optional[_Iterable[_Union[DefDataType, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[DefValue, _Mapping]]] = ..., templates: _Optional[_Iterable[_Union[DefTemplate, _Mapping]]] = ..., exceptions: _Optional[_Iterable[_Union[DefException, _Mapping]]] = ..., interfaces: _Optional[_Iterable[_Union[DefInterface, _Mapping]]] = ...) -> None: ...

class InternedDottedName(_message.Message):
    __slots__ = ["segments_interned_str"]
    SEGMENTS_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    segments_interned_str: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, segments_interned_str: _Optional[_Iterable[int]] = ...) -> None: ...

class PackageMetadata(_message.Message):
    __slots__ = ["name_interned_str", "version_interned_str"]
    NAME_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    VERSION_INTERNED_STR_FIELD_NUMBER: _ClassVar[int]
    name_interned_str: int
    version_interned_str: int
    def __init__(self, name_interned_str: _Optional[int] = ..., version_interned_str: _Optional[int] = ...) -> None: ...

class Package(_message.Message):
    __slots__ = ["modules", "interned_strings", "interned_dotted_names", "metadata", "interned_types"]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    INTERNED_STRINGS_FIELD_NUMBER: _ClassVar[int]
    INTERNED_DOTTED_NAMES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    INTERNED_TYPES_FIELD_NUMBER: _ClassVar[int]
    modules: _containers.RepeatedCompositeFieldContainer[Module]
    interned_strings: _containers.RepeatedScalarFieldContainer[str]
    interned_dotted_names: _containers.RepeatedCompositeFieldContainer[InternedDottedName]
    metadata: PackageMetadata
    interned_types: _containers.RepeatedCompositeFieldContainer[Type]
    def __init__(self, modules: _Optional[_Iterable[_Union[Module, _Mapping]]] = ..., interned_strings: _Optional[_Iterable[str]] = ..., interned_dotted_names: _Optional[_Iterable[_Union[InternedDottedName, _Mapping]]] = ..., metadata: _Optional[_Union[PackageMetadata, _Mapping]] = ..., interned_types: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
