from enum import IntEnum as _IntEnum
import builtins as _builtins
import sys

import typing as _typing

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L
_T = _typing.TypeVar("_T")

class PrimType(_IntEnum):
    UNIT = 0
    BOOL = 1
    INT64 = 2
    DECIMAL = 3
    TEXT = 5
    TIMESTAMP = 6
    PARTY = 8
    LIST = 9
    UPDATE = 10
    SCENARIO = 11
    DATE = 12
    CONTRACT_ID = 13
    OPTIONAL = 14
    ARROW = 15
    TEXTMAP = 16
    NUMERIC = 17
    ANY = 18
    TYPE_REP = 19
    GENMAP = 20
    BIGNUMERIC = 21
    ROUNDING_MODE = 22
    ANY_EXCEPTION = 23

class PrimCon(_IntEnum):
    CON_UNIT = 0
    CON_FALSE = 1
    CON_TRUE = 2

class BuiltinFunction(_IntEnum):
    ADD_DECIMAL = 0
    SUB_DECIMAL = 1
    MUL_DECIMAL = 2
    DIV_DECIMAL = 3
    ROUND_DECIMAL = 6
    ADD_NUMERIC = 107
    SUB_NUMERIC = 108
    MUL_NUMERIC = 109
    DIV_NUMERIC = 110
    ROUND_NUMERIC = 111
    CAST_NUMERIC = 121
    SHIFT_NUMERIC = 122
    ADD_INT64 = 7
    SUB_INT64 = 8
    MUL_INT64 = 9
    DIV_INT64 = 10
    MOD_INT64 = 11
    EXP_INT64 = 12
    FOLDL = 20
    FOLDR = 21
    TEXTMAP_EMPTY = 96
    TEXTMAP_INSERT = 97
    TEXTMAP_LOOKUP = 98
    TEXTMAP_DELETE = 99
    TEXTMAP_TO_LIST = 100
    TEXTMAP_SIZE = 101
    GENMAP_EMPTY = 124
    GENMAP_INSERT = 125
    GENMAP_LOOKUP = 126
    GENMAP_DELETE = 127
    GENMAP_KEYS = 128
    GENMAP_VALUES = 129
    GENMAP_SIZE = 130
    EXPLODE_TEXT = 23
    APPEND_TEXT = 24
    ERROR = 25
    ANY_EXCEPTION_MESSAGE = 147
    LEQ_INT64 = 33
    LEQ_DECIMAL = 34
    LEQ_NUMERIC = 112
    LEQ_TEXT = 36
    LEQ_TIMESTAMP = 37
    LEQ_DATE = 67
    LEQ_PARTY = 89
    LESS_INT64 = 39
    LESS_DECIMAL = 40
    LESS_NUMERIC = 113
    LESS_TEXT = 42
    LESS_TIMESTAMP = 43
    LESS_DATE = 68
    LESS_PARTY = 90
    GEQ_INT64 = 45
    GEQ_DECIMAL = 46
    GEQ_NUMERIC = 114
    GEQ_TEXT = 48
    GEQ_TIMESTAMP = 49
    GEQ_DATE = 69
    GEQ_PARTY = 91
    GREATER_INT64 = 51
    GREATER_DECIMAL = 52
    GREATER_NUMERIC = 115
    GREATER_TEXT = 54
    GREATER_TIMESTAMP = 55
    GREATER_DATE = 70
    GREATER_PARTY = 92
    INT64_TO_TEXT = 57
    DECIMAL_TO_TEXT = 58
    NUMERIC_TO_TEXT = 116
    TEXT_TO_TEXT = 60
    TIMESTAMP_TO_TEXT = 61
    DATE_TO_TEXT = 71
    PARTY_TO_QUOTED_TEXT = 63
    PARTY_TO_TEXT = 94
    TEXT_TO_PARTY = 95
    TEXT_TO_INT64 = 103
    TEXT_TO_DECIMAL = 104
    TEXT_TO_NUMERIC = 117
    CONTRACT_ID_TO_TEXT = 136
    SHA256_TEXT = 93
    DATE_TO_UNIX_DAYS = 72
    UNIX_DAYS_TO_DATE = 73
    TIMESTAMP_TO_UNIX_MICROSECONDS = 74
    UNIX_MICROSECONDS_TO_TIMESTAMP = 75
    INT64_TO_DECIMAL = 76
    DECIMAL_TO_INT64 = 77
    INT64_TO_NUMERIC = 118
    NUMERIC_TO_INT64 = 119
    IMPLODE_TEXT = 78
    EQUAL_INT64 = 79
    EQUAL_DECIMAL = 80
    EQUAL_NUMERIC = 120
    EQUAL_TEXT = 81
    EQUAL_TIMESTAMP = 82
    EQUAL_DATE = 83
    EQUAL_PARTY = 84
    EQUAL_BOOL = 85
    EQUAL_CONTRACT_ID = 86
    EQUAL_LIST = 87
    EQUAL_TYPE_REP = 123
    EQUAL = 131
    LESS_EQ = 132
    LESS = 133
    GREATER_EQ = 134
    GREATER = 135
    TRACE = 88
    COERCE_CONTRACT_ID = 102
    CODE_POINTS_TO_TEXT = 105
    TEXT_TO_CODE_POINTS = 106
    SCALE_BIGNUMERIC = 137
    PRECISION_BIGNUMERIC = 138
    ADD_BIGNUMERIC = 139
    SUB_BIGNUMERIC = 140
    MUL_BIGNUMERIC = 141
    DIV_BIGNUMERIC = 142
    SHIFT_RIGHT_BIGNUMERIC = 143
    BIGNUMERIC_TO_NUMERIC = 144
    NUMERIC_TO_BIGNUMERIC = 145
    BIGNUMERIC_TO_TEXT = 146

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Unit:
    __match_args__ = ()

    def __init__(self): ...

PackageRef = _typing.NewType("PackageRef", str)

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DottedName:
    __match_args__ = ("segments",)

    @property
    def segments(self) -> _typing.Tuple[str, ...]: ...
    def __init__(self, segments: _typing.Iterable[str]): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class ModuleRef:
    __match_args__ = ("package_ref", "module_name")

    @property
    def package_ref(self) -> PackageRef: ...
    @property
    def module_name(self) -> DottedName: ...
    def __init__(self, package_ref: PackageRef, module_name: DottedName): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class TypeConName:
    __match_args__ = ("module", "name")

    @property
    def module(self) -> ModuleRef: ...
    @property
    def name(self) -> DottedName: ...
    def __init__(self, module: ModuleRef, name: DottedName): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class TypeSynName:
    __match_args__ = ("module", "name")

    @property
    def module(self) -> ModuleRef: ...
    @property
    def name(self) -> DottedName: ...
    def __init__(self, module: ModuleRef, name: DottedName): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class ValName:
    __match_args__ = ("module", "name")

    @property
    def module(self) -> ModuleRef: ...
    @property
    def name(self) -> DottedName: ...
    def __init__(self, module: ModuleRef, name: DottedName): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class FieldWithType:
    __match_args__ = ("field", "type")

    @property
    def field(self) -> str: ...
    @property
    def type(self) -> Type: ...
    def __init__(self, field: str, type: Type): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class VarWithType:
    __match_args__ = ("var", "type")

    @property
    def var(self) -> str: ...
    @property
    def type(self) -> Type: ...
    def __init__(self, var: str, type: Type): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class TypeVarWithKind:
    __match_args__ = ("var", "kind")

    @property
    def var(self) -> str: ...
    @property
    def kind(self) -> Kind: ...
    def __init__(self, var: str, kind: Kind): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class FieldWithExpr:
    __match_args__ = ("field", "expr")

    @property
    def field(self) -> str: ...
    @property
    def expr(self) -> Expr: ...
    def __init__(self, field: str, expr: Expr): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Binding:
    __match_args__ = ("binder", "bound")

    @property
    def binder(self) -> VarWithType: ...
    @property
    def bound(self) -> Expr: ...
    def __init__(self, binder: VarWithType, bound: Expr): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Kind:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Arrow:
        __match_args__ = ("params", "result")

        @property
        def params(self) -> _typing.Tuple[Kind, ...]: ...
        @property
        def result(self) -> Kind: ...
        def __init__(self, params: _typing.Iterable[Kind], result: Kind): ...

    __match_args__ = ()

    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["star"], Unit],
        _typing.Tuple[_L["arrow"], Kind.Arrow],
        _typing.Tuple[_L["nat"], Unit],
    ]: ...
    @property
    def star(self) -> _typing.Optional[Unit]: ...
    @property
    def arrow(self) -> _typing.Optional[Kind.Arrow]: ...
    @property
    def nat(self) -> _typing.Optional[Unit]: ...
    @_typing.overload
    def __init__(self, *, star: Unit = ...): ...
    @_typing.overload
    def __init__(self, *, arrow: Kind.Arrow = ...): ...
    @_typing.overload
    def __init__(self, *, nat: Unit = ...): ...
    def Sum_match(
        self,
        star: _typing.Callable[[Unit], _T],
        arrow: _typing.Callable[[Kind.Arrow], _T],
        nat: _typing.Callable[[Unit], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Type:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Var:
        __match_args__ = ("var", "args")

        @property
        def var(self) -> str: ...
        @property
        def args(self) -> _typing.Tuple[Type, ...]: ...
        def __init__(self, var: str, args: _typing.Iterable[Type]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Con:
        __match_args__ = ("tycon", "args")

        @property
        def tycon(self) -> TypeConName: ...
        @property
        def args(self) -> _typing.Tuple[Type, ...]: ...
        def __init__(self, tycon: TypeConName, args: _typing.Iterable[Type]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Syn:
        __match_args__ = ("tysyn", "args")

        @property
        def tysyn(self) -> TypeSynName: ...
        @property
        def args(self) -> _typing.Tuple[Type, ...]: ...
        def __init__(self, tysyn: TypeSynName, args: _typing.Iterable[Type]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Prim:
        __match_args__ = ("prim", "args")

        @property
        def prim(self) -> PrimType: ...
        @property
        def args(self) -> _typing.Tuple[Type, ...]: ...
        def __init__(self, prim: PrimType, args: _typing.Iterable[Type]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Forall:
        __match_args__ = ("vars", "body")

        @property
        def vars(self) -> _typing.Tuple[TypeVarWithKind, ...]: ...
        @property
        def body(self) -> Type: ...
        def __init__(self, vars: _typing.Iterable[TypeVarWithKind], body: Type): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Struct:
        __match_args__ = ("fields",)

        @property
        def fields(self) -> _typing.Tuple[FieldWithType, ...]: ...
        def __init__(self, fields: _typing.Iterable[FieldWithType]): ...

    __match_args__ = ()

    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["var"], Type.Var],
        _typing.Tuple[_L["con"], Type.Con],
        _typing.Tuple[_L["prim"], Type.Prim],
        _typing.Tuple[_L["forall"], Type.Forall],
        _typing.Tuple[_L["struct"], Type.Struct],
        _typing.Tuple[_L["nat"], int],
        _typing.Tuple[_L["syn"], Type.Syn],
    ]: ...
    @property
    def var(self) -> _typing.Optional[Type.Var]: ...
    @property
    def con(self) -> _typing.Optional[Type.Con]: ...
    @property
    def prim(self) -> _typing.Optional[Type.Prim]: ...
    @property
    def forall(self) -> _typing.Optional[Type.Forall]: ...
    @property
    def struct(self) -> _typing.Optional[Type.Struct]: ...
    @property
    def nat(self) -> _typing.Optional[int]: ...
    @property
    def syn(self) -> _typing.Optional[Type.Syn]: ...
    @_typing.overload
    def __init__(self, *, var: Type.Var = ...): ...
    @_typing.overload
    def __init__(self, *, con: Type.Con = ...): ...
    @_typing.overload
    def __init__(self, *, prim: Type.Prim = ...): ...
    @_typing.overload
    def __init__(self, *, forall: Type.Forall = ...): ...
    @_typing.overload
    def __init__(self, *, struct: Type.Struct = ...): ...
    @_typing.overload
    def __init__(self, *, nat: int = ...): ...
    @_typing.overload
    def __init__(self, *, syn: Type.Syn = ...): ...
    def Sum_match(
        self,
        var: _typing.Callable[[Type.Var], _T],
        con: _typing.Callable[[Type.Con], _T],
        prim: _typing.Callable[[Type.Prim], _T],
        forall: _typing.Callable[[Type.Forall], _T],
        struct: _typing.Callable[[Type.Struct], _T],
        nat: _typing.Callable[[int], _T],
        syn: _typing.Callable[[Type.Syn], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class PrimLit:
    class RoundingMode(_IntEnum):
        UP = 0
        DOWN = 1
        CEILING = 2
        FLOOR = 3
        HALF_UP = 4
        HALF_DOWN = 5
        HALF_EVEN = 6
        UNNECESSARY = 7
    __match_args__ = ()

    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["int64"], int],
        _typing.Tuple[_L["decimal"], str],
        _typing.Tuple[_L["numeric"], str],
        _typing.Tuple[_L["text"], str],
        _typing.Tuple[_L["timestamp"], float],
        _typing.Tuple[_L["party"], str],
        _typing.Tuple[_L["date"], int],
        _typing.Tuple[_L["rounding_mode"], PrimLit.RoundingMode],
    ]: ...
    @property
    def int64(self) -> _typing.Optional[int]: ...
    @property
    def decimal(self) -> _typing.Optional[str]: ...
    @property
    def numeric(self) -> _typing.Optional[str]: ...
    @property
    def text(self) -> _typing.Optional[str]: ...
    @property
    def timestamp(self) -> _typing.Optional[float]: ...
    @property
    def party(self) -> _typing.Optional[str]: ...
    @property
    def date(self) -> _typing.Optional[int]: ...
    @property
    def rounding_mode(self) -> _typing.Optional[PrimLit.RoundingMode]: ...
    @_typing.overload
    def __init__(self, *, int64: int = ...): ...
    @_typing.overload
    def __init__(self, *, decimal: str = ...): ...
    @_typing.overload
    def __init__(self, *, numeric: str = ...): ...
    @_typing.overload
    def __init__(self, *, text: str = ...): ...
    @_typing.overload
    def __init__(self, *, timestamp: float = ...): ...
    @_typing.overload
    def __init__(self, *, party: str = ...): ...
    @_typing.overload
    def __init__(self, *, date: int = ...): ...
    @_typing.overload
    def __init__(self, *, rounding_mode: PrimLit.RoundingMode = ...): ...
    def Sum_match(
        self,
        int64: _typing.Callable[[int], _T],
        decimal: _typing.Callable[[str], _T],
        numeric: _typing.Callable[[str], _T],
        text: _typing.Callable[[str], _T],
        timestamp: _typing.Callable[[float], _T],
        party: _typing.Callable[[str], _T],
        date: _typing.Callable[[int], _T],
        rounding_mode: _typing.Callable[[PrimLit.RoundingMode], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Location:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Range:
        __match_args__ = ("start_line", "start_col", "end_line", "end_col")

        @property
        def start_line(self) -> int: ...
        @property
        def start_col(self) -> int: ...
        @property
        def end_line(self) -> int: ...
        @property
        def end_col(self) -> int: ...
        def __init__(
            self, start_line: int, start_col: int, end_line: int, end_col: int
        ): ...

    __match_args__ = ("module", "range")

    @property
    def module(self) -> ModuleRef: ...
    @property
    def range(self) -> Location.Range: ...
    def __init__(self, module: ModuleRef, range: Location.Range): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Expr:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecCon:
        __match_args__ = ("tycon", "fields")

        @property
        def tycon(self) -> Type.Con: ...
        @property
        def fields(self) -> _typing.Tuple[FieldWithExpr, ...]: ...
        def __init__(
            self, tycon: Type.Con, fields: _typing.Iterable[FieldWithExpr]
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecProj:
        __match_args__ = ("tycon", "field", "record")

        @property
        def tycon(self) -> Type.Con: ...
        @property
        def field(self) -> str: ...
        @property
        def record(self) -> Expr: ...
        def __init__(self, tycon: Type.Con, field: str, record: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecUpd:
        __match_args__ = ("tycon", "field", "record", "update")

        @property
        def tycon(self) -> Type.Con: ...
        @property
        def field(self) -> str: ...
        @property
        def record(self) -> Expr: ...
        @property
        def update(self) -> Expr: ...
        def __init__(self, tycon: Type.Con, field: str, record: Expr, update: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class VariantCon:
        __match_args__ = ("tycon", "variant_con", "variant_arg")

        @property
        def tycon(self) -> Type.Con: ...
        @property
        def variant_con(self) -> str: ...
        @property
        def variant_arg(self) -> Expr: ...
        def __init__(self, tycon: Type.Con, variant_con: str, variant_arg: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EnumCon:
        __match_args__ = ("tycon", "enum_con")

        @property
        def tycon(self) -> TypeConName: ...
        @property
        def enum_con(self) -> str: ...
        def __init__(self, tycon: TypeConName, enum_con: str): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class StructCon:
        __match_args__ = ("fields",)

        @property
        def fields(self) -> _typing.Tuple[FieldWithExpr, ...]: ...
        def __init__(self, fields: _typing.Iterable[FieldWithExpr]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class StructProj:
        __match_args__ = ("field", "struct")

        @property
        def field(self) -> str: ...
        @property
        def struct(self) -> Expr: ...
        def __init__(self, field: str, struct: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class StructUpd:
        __match_args__ = ("field", "struct", "update")

        @property
        def field(self) -> str: ...
        @property
        def struct(self) -> Expr: ...
        @property
        def update(self) -> Expr: ...
        def __init__(self, field: str, struct: Expr, update: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class App:
        __match_args__ = ("fun", "args")

        @property
        def fun(self) -> Expr: ...
        @property
        def args(self) -> _typing.Tuple[Expr, ...]: ...
        def __init__(self, fun: Expr, args: _typing.Iterable[Expr]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class TyApp:
        __match_args__ = ("expr", "types")

        @property
        def expr(self) -> Expr: ...
        @property
        def types(self) -> _typing.Tuple[Type, ...]: ...
        def __init__(self, expr: Expr, types: _typing.Iterable[Type]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Abs:
        __match_args__ = ("param", "body")

        @property
        def param(self) -> _typing.Tuple[VarWithType, ...]: ...
        @property
        def body(self) -> Expr: ...
        def __init__(self, param: _typing.Iterable[VarWithType], body: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class TyAbs:
        __match_args__ = ("param", "body")

        @property
        def param(self) -> _typing.Tuple[TypeVarWithKind, ...]: ...
        @property
        def body(self) -> Expr: ...
        def __init__(self, param: _typing.Iterable[TypeVarWithKind], body: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Nil:
        __match_args__ = ("type",)

        @property
        def type(self) -> Type: ...
        def __init__(self, type: Type): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Cons:
        __match_args__ = ("type", "front", "tail")

        @property
        def type(self) -> Type: ...
        @property
        def front(self) -> _typing.Tuple[Expr, ...]: ...
        @property
        def tail(self) -> Expr: ...
        def __init__(self, type: Type, front: _typing.Iterable[Expr], tail: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class OptionalNone:
        __match_args__ = ("type",)

        @property
        def type(self) -> Type: ...
        def __init__(self, type: Type): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class OptionalSome:
        __match_args__ = ("type", "body")

        @property
        def type(self) -> Type: ...
        @property
        def body(self) -> Expr: ...
        def __init__(self, type: Type, body: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ToAny:
        __match_args__ = ("type", "expr")

        @property
        def type(self) -> Type: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, type: Type, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromAny:
        __match_args__ = ("type", "expr")

        @property
        def type(self) -> Type: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, type: Type, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ToAnyException:
        __match_args__ = ("type", "expr")

        @property
        def type(self) -> Type: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, type: Type, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromAnyException:
        __match_args__ = ("type", "expr")

        @property
        def type(self) -> Type: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, type: Type, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Throw:
        __match_args__ = ("return_type", "exception_type", "exception_expr")

        @property
        def return_type(self) -> Type: ...
        @property
        def exception_type(self) -> Type: ...
        @property
        def exception_expr(self) -> Expr: ...
        def __init__(
            self, return_type: Type, exception_type: Type, exception_expr: Expr
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ToInterface:
        __match_args__ = ("interface_type", "template_type", "template_expr")

        @property
        def interface_type(self) -> TypeConName: ...
        @property
        def template_type(self) -> TypeConName: ...
        @property
        def template_expr(self) -> Expr: ...
        def __init__(
            self,
            interface_type: TypeConName,
            template_type: TypeConName,
            template_expr: Expr,
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromInterface:
        __match_args__ = ("interface_type", "template_type", "interface_expr")

        @property
        def interface_type(self) -> TypeConName: ...
        @property
        def template_type(self) -> TypeConName: ...
        @property
        def interface_expr(self) -> Expr: ...
        def __init__(
            self,
            interface_type: TypeConName,
            template_type: TypeConName,
            interface_expr: Expr,
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class CallInterface:
        __match_args__ = ("interface_type", "method_interned_name", "interface_expr")

        @property
        def interface_type(self) -> TypeConName: ...
        @property
        def method_interned_name(self) -> int: ...
        @property
        def interface_expr(self) -> Expr: ...
        def __init__(
            self,
            interface_type: TypeConName,
            method_interned_name: int,
            interface_expr: Expr,
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ViewInterface:
        __match_args__ = ("interface", "expr")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, interface: TypeConName, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class SignatoryInterface:
        __match_args__ = ("interface", "expr")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, interface: TypeConName, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ObserverInterface:
        __match_args__ = ("interface", "expr")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, interface: TypeConName, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class UnsafeFromInterface:
        __match_args__ = (
            "interface_type",
            "template_type",
            "contract_id_expr",
            "interface_expr",
        )

        @property
        def interface_type(self) -> TypeConName: ...
        @property
        def template_type(self) -> TypeConName: ...
        @property
        def contract_id_expr(self) -> Expr: ...
        @property
        def interface_expr(self) -> Expr: ...
        def __init__(
            self,
            interface_type: TypeConName,
            template_type: TypeConName,
            contract_id_expr: Expr,
            interface_expr: Expr,
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ToRequiredInterface:
        __match_args__ = ("required_interface", "requiring_interface", "expr")

        @property
        def required_interface(self) -> TypeConName: ...
        @property
        def requiring_interface(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(
            self,
            required_interface: TypeConName,
            requiring_interface: TypeConName,
            expr: Expr,
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromRequiredInterface:
        __match_args__ = ("required_interface", "requiring_interface", "expr")

        @property
        def required_interface(self) -> TypeConName: ...
        @property
        def requiring_interface(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(
            self,
            required_interface: TypeConName,
            requiring_interface: TypeConName,
            expr: Expr,
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class UnsafeFromRequiredInterface:
        __match_args__ = (
            "required_interface",
            "requiring_interface",
            "contract_id_expr",
            "interface_expr",
        )

        @property
        def required_interface(self) -> TypeConName: ...
        @property
        def requiring_interface(self) -> TypeConName: ...
        @property
        def contract_id_expr(self) -> Expr: ...
        @property
        def interface_expr(self) -> Expr: ...
        def __init__(
            self,
            required_interface: TypeConName,
            requiring_interface: TypeConName,
            contract_id_expr: Expr,
            interface_expr: Expr,
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class InterfaceTemplateTypeRep:
        __match_args__ = ("interface", "expr")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, interface: TypeConName, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Experimental:
        __match_args__ = ("name", "type")

        @property
        def name(self) -> str: ...
        @property
        def type(self) -> Type: ...
        def __init__(self, name: str, type: Type): ...

    __match_args__ = ()

    @property
    def location(self) -> _typing.Optional[Location]: ...
    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["var"], str],
        _typing.Tuple[_L["val"], ValName],
        _typing.Tuple[_L["builtin"], BuiltinFunction],
        _typing.Tuple[_L["prim_con"], PrimCon],
        _typing.Tuple[_L["prim_lit"], PrimLit],
        _typing.Tuple[_L["rec_con"], Expr.RecCon],
        _typing.Tuple[_L["rec_proj"], Expr.RecProj],
        _typing.Tuple[_L["rec_upd"], Expr.RecUpd],
        _typing.Tuple[_L["variant_con"], Expr.VariantCon],
        _typing.Tuple[_L["enum_con"], Expr.EnumCon],
        _typing.Tuple[_L["struct_con"], Expr.StructCon],
        _typing.Tuple[_L["struct_proj"], Expr.StructProj],
        _typing.Tuple[_L["struct_upd"], Expr.StructUpd],
        _typing.Tuple[_L["app"], Expr.App],
        _typing.Tuple[_L["ty_app"], Expr.TyApp],
        _typing.Tuple[_L["abs"], Expr.Abs],
        _typing.Tuple[_L["ty_abs"], Expr.TyAbs],
        _typing.Tuple[_L["case"], Case],
        _typing.Tuple[_L["let"], Block],
        _typing.Tuple[_L["nil"], Expr.Nil],
        _typing.Tuple[_L["cons"], Expr.Cons],
        _typing.Tuple[_L["update"], Update],
        _typing.Tuple[_L["scenario"], Scenario],
        _typing.Tuple[_L["optional_none"], Expr.OptionalNone],
        _typing.Tuple[_L["optional_some"], Expr.OptionalSome],
        _typing.Tuple[_L["to_any"], Expr.ToAny],
        _typing.Tuple[_L["from_any"], Expr.FromAny],
        _typing.Tuple[_L["type_rep"], Type],
        _typing.Tuple[_L["to_any_exception"], Expr.ToAnyException],
        _typing.Tuple[_L["from_any_exception"], Expr.FromAnyException],
        _typing.Tuple[_L["throw"], Expr.Throw],
        _typing.Tuple[_L["to_interface"], Expr.ToInterface],
        _typing.Tuple[_L["from_interface"], Expr.FromInterface],
        _typing.Tuple[_L["call_interface"], Expr.CallInterface],
        _typing.Tuple[_L["signatory_interface"], Expr.SignatoryInterface],
        _typing.Tuple[_L["observer_interface"], Expr.ObserverInterface],
        _typing.Tuple[_L["view_interface"], Expr.ViewInterface],
        _typing.Tuple[_L["unsafe_from_interface"], Expr.UnsafeFromInterface],
        _typing.Tuple[_L["interface_template_type_rep"], Expr.InterfaceTemplateTypeRep],
        _typing.Tuple[_L["to_required_interface"], Expr.ToRequiredInterface],
        _typing.Tuple[_L["from_required_interface"], Expr.FromRequiredInterface],
        _typing.Tuple[
            _L["unsafe_from_required_interface"], Expr.UnsafeFromRequiredInterface
        ],
        _typing.Tuple[_L["experimental"], Expr.Experimental],
    ]: ...
    @property
    def var(self) -> _typing.Optional[str]: ...
    @property
    def val(self) -> _typing.Optional[ValName]: ...
    @property
    def builtin(self) -> _typing.Optional[BuiltinFunction]: ...
    @property
    def prim_con(self) -> _typing.Optional[PrimCon]: ...
    @property
    def prim_lit(self) -> _typing.Optional[PrimLit]: ...
    @property
    def rec_con(self) -> _typing.Optional[Expr.RecCon]: ...
    @property
    def rec_proj(self) -> _typing.Optional[Expr.RecProj]: ...
    @property
    def rec_upd(self) -> _typing.Optional[Expr.RecUpd]: ...
    @property
    def variant_con(self) -> _typing.Optional[Expr.VariantCon]: ...
    @property
    def enum_con(self) -> _typing.Optional[Expr.EnumCon]: ...
    @property
    def struct_con(self) -> _typing.Optional[Expr.StructCon]: ...
    @property
    def struct_proj(self) -> _typing.Optional[Expr.StructProj]: ...
    @property
    def struct_upd(self) -> _typing.Optional[Expr.StructUpd]: ...
    @property
    def app(self) -> _typing.Optional[Expr.App]: ...
    @property
    def ty_app(self) -> _typing.Optional[Expr.TyApp]: ...
    @property
    def abs(self) -> _typing.Optional[Expr.Abs]: ...
    @property
    def ty_abs(self) -> _typing.Optional[Expr.TyAbs]: ...
    @property
    def case(self) -> _typing.Optional[Case]: ...
    @property
    def let(self) -> _typing.Optional[Block]: ...
    @property
    def nil(self) -> _typing.Optional[Expr.Nil]: ...
    @property
    def cons(self) -> _typing.Optional[Expr.Cons]: ...
    @property
    def update(self) -> _typing.Optional[Update]: ...
    @property
    def scenario(self) -> _typing.Optional[Scenario]: ...
    @property
    def optional_none(self) -> _typing.Optional[Expr.OptionalNone]: ...
    @property
    def optional_some(self) -> _typing.Optional[Expr.OptionalSome]: ...
    @property
    def to_any(self) -> _typing.Optional[Expr.ToAny]: ...
    @property
    def from_any(self) -> _typing.Optional[Expr.FromAny]: ...
    @property
    def type_rep(self) -> _typing.Optional[Type]: ...
    @property
    def to_any_exception(self) -> _typing.Optional[Expr.ToAnyException]: ...
    @property
    def from_any_exception(self) -> _typing.Optional[Expr.FromAnyException]: ...
    @property
    def throw(self) -> _typing.Optional[Expr.Throw]: ...
    @property
    def to_interface(self) -> _typing.Optional[Expr.ToInterface]: ...
    @property
    def from_interface(self) -> _typing.Optional[Expr.FromInterface]: ...
    @property
    def call_interface(self) -> _typing.Optional[Expr.CallInterface]: ...
    @property
    def signatory_interface(self) -> _typing.Optional[Expr.SignatoryInterface]: ...
    @property
    def observer_interface(self) -> _typing.Optional[Expr.ObserverInterface]: ...
    @property
    def view_interface(self) -> _typing.Optional[Expr.ViewInterface]: ...
    @property
    def unsafe_from_interface(self) -> _typing.Optional[Expr.UnsafeFromInterface]: ...
    @property
    def interface_template_type_rep(
        self,
    ) -> _typing.Optional[Expr.InterfaceTemplateTypeRep]: ...
    @property
    def to_required_interface(self) -> _typing.Optional[Expr.ToRequiredInterface]: ...
    @property
    def from_required_interface(
        self,
    ) -> _typing.Optional[Expr.FromRequiredInterface]: ...
    @property
    def unsafe_from_required_interface(
        self,
    ) -> _typing.Optional[Expr.UnsafeFromRequiredInterface]: ...
    @property
    def experimental(self) -> _typing.Optional[Expr.Experimental]: ...
    @_typing.overload
    def __init__(
        self, *, var: str = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, val: ValName = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        builtin: BuiltinFunction = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, prim_con: PrimCon = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, prim_lit: PrimLit = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, rec_con: Expr.RecCon = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        rec_proj: Expr.RecProj = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, rec_upd: Expr.RecUpd = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        variant_con: Expr.VariantCon = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        enum_con: Expr.EnumCon = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        struct_con: Expr.StructCon = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        struct_proj: Expr.StructProj = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        struct_upd: Expr.StructUpd = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, app: Expr.App = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, ty_app: Expr.TyApp = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, abs: Expr.Abs = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, ty_abs: Expr.TyAbs = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, case: Case = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, let: Block = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, nil: Expr.Nil = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, cons: Expr.Cons = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, update: Update = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, scenario: Scenario = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        optional_none: Expr.OptionalNone = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        optional_some: Expr.OptionalSome = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, to_any: Expr.ToAny = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        from_any: Expr.FromAny = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, type_rep: Type = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        to_any_exception: Expr.ToAnyException = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        from_any_exception: Expr.FromAnyException = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self, *, throw: Expr.Throw = ..., location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        to_interface: Expr.ToInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        from_interface: Expr.FromInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        call_interface: Expr.CallInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        signatory_interface: Expr.SignatoryInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        observer_interface: Expr.ObserverInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        view_interface: Expr.ViewInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        unsafe_from_interface: Expr.UnsafeFromInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        interface_template_type_rep: Expr.InterfaceTemplateTypeRep = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        to_required_interface: Expr.ToRequiredInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        from_required_interface: Expr.FromRequiredInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        unsafe_from_required_interface: Expr.UnsafeFromRequiredInterface = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        *,
        experimental: Expr.Experimental = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    def Sum_match(
        self,
        var: _typing.Callable[[str], _T],
        val: _typing.Callable[[ValName], _T],
        builtin: _typing.Callable[[BuiltinFunction], _T],
        prim_con: _typing.Callable[[PrimCon], _T],
        prim_lit: _typing.Callable[[PrimLit], _T],
        rec_con: _typing.Callable[[Expr.RecCon], _T],
        rec_proj: _typing.Callable[[Expr.RecProj], _T],
        rec_upd: _typing.Callable[[Expr.RecUpd], _T],
        variant_con: _typing.Callable[[Expr.VariantCon], _T],
        enum_con: _typing.Callable[[Expr.EnumCon], _T],
        struct_con: _typing.Callable[[Expr.StructCon], _T],
        struct_proj: _typing.Callable[[Expr.StructProj], _T],
        struct_upd: _typing.Callable[[Expr.StructUpd], _T],
        app: _typing.Callable[[Expr.App], _T],
        ty_app: _typing.Callable[[Expr.TyApp], _T],
        abs: _typing.Callable[[Expr.Abs], _T],
        ty_abs: _typing.Callable[[Expr.TyAbs], _T],
        case: _typing.Callable[[Case], _T],
        let: _typing.Callable[[Block], _T],
        nil: _typing.Callable[[Expr.Nil], _T],
        cons: _typing.Callable[[Expr.Cons], _T],
        update: _typing.Callable[[Update], _T],
        scenario: _typing.Callable[[Scenario], _T],
        optional_none: _typing.Callable[[Expr.OptionalNone], _T],
        optional_some: _typing.Callable[[Expr.OptionalSome], _T],
        to_any: _typing.Callable[[Expr.ToAny], _T],
        from_any: _typing.Callable[[Expr.FromAny], _T],
        type_rep: _typing.Callable[[Type], _T],
        to_any_exception: _typing.Callable[[Expr.ToAnyException], _T],
        from_any_exception: _typing.Callable[[Expr.FromAnyException], _T],
        throw: _typing.Callable[[Expr.Throw], _T],
        to_interface: _typing.Callable[[Expr.ToInterface], _T],
        from_interface: _typing.Callable[[Expr.FromInterface], _T],
        call_interface: _typing.Callable[[Expr.CallInterface], _T],
        signatory_interface: _typing.Callable[[Expr.SignatoryInterface], _T],
        observer_interface: _typing.Callable[[Expr.ObserverInterface], _T],
        view_interface: _typing.Callable[[Expr.ViewInterface], _T],
        unsafe_from_interface: _typing.Callable[[Expr.UnsafeFromInterface], _T],
        interface_template_type_rep: _typing.Callable[
            [Expr.InterfaceTemplateTypeRep], _T
        ],
        to_required_interface: _typing.Callable[[Expr.ToRequiredInterface], _T],
        from_required_interface: _typing.Callable[[Expr.FromRequiredInterface], _T],
        unsafe_from_required_interface: _typing.Callable[
            [Expr.UnsafeFromRequiredInterface], _T
        ],
        experimental: _typing.Callable[[Expr.Experimental], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class CaseAlt:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Variant:
        __match_args__ = ("con", "variant", "binder")

        @property
        def con(self) -> TypeConName: ...
        @property
        def variant(self) -> str: ...
        @property
        def binder(self) -> str: ...
        def __init__(self, con: TypeConName, variant: str, binder: str): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Enum:
        __match_args__ = ("con", "constructor")

        @property
        def con(self) -> TypeConName: ...
        @property
        def constructor(self) -> str: ...
        def __init__(self, con: TypeConName, constructor: str): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Cons:
        __match_args__ = ("var_head", "var_tail")

        @property
        def var_head(self) -> str: ...
        @property
        def var_tail(self) -> str: ...
        def __init__(self, var_head: str, var_tail: str): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class OptionalSome:
        __match_args__ = ("var_body",)

        @property
        def var_body(self) -> str: ...
        def __init__(self, var_body: str): ...

    __match_args__ = ("body",)

    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["default"], Unit],
        _typing.Tuple[_L["variant"], CaseAlt.Variant],
        _typing.Tuple[_L["prim_con"], PrimCon],
        _typing.Tuple[_L["nil"], Unit],
        _typing.Tuple[_L["cons"], CaseAlt.Cons],
        _typing.Tuple[_L["optional_none"], Unit],
        _typing.Tuple[_L["optional_some"], CaseAlt.OptionalSome],
        _typing.Tuple[_L["enum"], CaseAlt.Enum],
    ]: ...
    @property
    def default(self) -> _typing.Optional[Unit]: ...
    @property
    def variant(self) -> _typing.Optional[CaseAlt.Variant]: ...
    @property
    def prim_con(self) -> _typing.Optional[PrimCon]: ...
    @property
    def nil(self) -> _typing.Optional[Unit]: ...
    @property
    def cons(self) -> _typing.Optional[CaseAlt.Cons]: ...
    @property
    def optional_none(self) -> _typing.Optional[Unit]: ...
    @property
    def optional_some(self) -> _typing.Optional[CaseAlt.OptionalSome]: ...
    @property
    def enum(self) -> _typing.Optional[CaseAlt.Enum]: ...
    @property
    def body(self) -> Expr: ...
    @_typing.overload
    def __init__(self, body: Expr, *, default: Unit = ...): ...
    @_typing.overload
    def __init__(self, body: Expr, *, variant: CaseAlt.Variant = ...): ...
    @_typing.overload
    def __init__(self, body: Expr, *, prim_con: PrimCon = ...): ...
    @_typing.overload
    def __init__(self, body: Expr, *, nil: Unit = ...): ...
    @_typing.overload
    def __init__(self, body: Expr, *, cons: CaseAlt.Cons = ...): ...
    @_typing.overload
    def __init__(self, body: Expr, *, optional_none: Unit = ...): ...
    @_typing.overload
    def __init__(self, body: Expr, *, optional_some: CaseAlt.OptionalSome = ...): ...
    @_typing.overload
    def __init__(self, body: Expr, *, enum: CaseAlt.Enum = ...): ...
    def Sum_match(
        self,
        default: _typing.Callable[[Unit], _T],
        variant: _typing.Callable[[CaseAlt.Variant], _T],
        prim_con: _typing.Callable[[PrimCon], _T],
        nil: _typing.Callable[[Unit], _T],
        cons: _typing.Callable[[CaseAlt.Cons], _T],
        optional_none: _typing.Callable[[Unit], _T],
        optional_some: _typing.Callable[[CaseAlt.OptionalSome], _T],
        enum: _typing.Callable[[CaseAlt.Enum], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Case:
    __match_args__ = ("scrut", "alts")

    @property
    def scrut(self) -> Expr: ...
    @property
    def alts(self) -> _typing.Tuple[CaseAlt, ...]: ...
    def __init__(self, scrut: Expr, alts: _typing.Iterable[CaseAlt]): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Block:
    __match_args__ = ("bindings", "body")

    @property
    def bindings(self) -> _typing.Tuple[Binding, ...]: ...
    @property
    def body(self) -> Expr: ...
    def __init__(self, bindings: _typing.Iterable[Binding], body: Expr): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Pure:
    __match_args__ = ("type", "expr")

    @property
    def type(self) -> Type: ...
    @property
    def expr(self) -> Expr: ...
    def __init__(self, type: Type, expr: Expr): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Update:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Create:
        __match_args__ = ("template", "expr")

        @property
        def template(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, template: TypeConName, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class CreateInterface:
        __match_args__ = ("interface", "expr")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def expr(self) -> Expr: ...
        def __init__(self, interface: TypeConName, expr: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Exercise:
        __match_args__ = ("template", "choice", "cid", "arg")

        @property
        def template(self) -> TypeConName: ...
        @property
        def choice(self) -> str: ...
        @property
        def cid(self) -> Expr: ...
        @property
        def arg(self) -> Expr: ...
        def __init__(
            self, template: TypeConName, choice: str, cid: Expr, arg: Expr
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ExerciseInterface:
        __match_args__ = ("interface", "choice", "cid", "arg", "guard")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def choice(self) -> str: ...
        @property
        def cid(self) -> Expr: ...
        @property
        def arg(self) -> Expr: ...
        @property
        def guard(self) -> Expr: ...
        def __init__(
            self, interface: TypeConName, choice: str, cid: Expr, arg: Expr, guard: Expr
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ExerciseByKey:
        __match_args__ = ("template", "choice", "key", "arg")

        @property
        def template(self) -> TypeConName: ...
        @property
        def choice(self) -> str: ...
        @property
        def key(self) -> Expr: ...
        @property
        def arg(self) -> Expr: ...
        def __init__(
            self, template: TypeConName, choice: str, key: Expr, arg: Expr
        ): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Fetch:
        __match_args__ = ("template", "cid")

        @property
        def template(self) -> TypeConName: ...
        @property
        def cid(self) -> Expr: ...
        def __init__(self, template: TypeConName, cid: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FetchInterface:
        __match_args__ = ("interface", "cid")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def cid(self) -> Expr: ...
        def __init__(self, interface: TypeConName, cid: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EmbedExpr:
        __match_args__ = ("type", "body")

        @property
        def type(self) -> Type: ...
        @property
        def body(self) -> Expr: ...
        def __init__(self, type: Type, body: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RetrieveByKey:
        __match_args__ = ("template", "key")

        @property
        def template(self) -> TypeConName: ...
        @property
        def key(self) -> Expr: ...
        def __init__(self, template: TypeConName, key: Expr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class TryCatch:
        __match_args__ = ("return_type", "try_expr", "var", "catch_expr")

        @property
        def return_type(self) -> Type: ...
        @property
        def try_expr(self) -> Expr: ...
        @property
        def var(self) -> str: ...
        @property
        def catch_expr(self) -> Expr: ...
        def __init__(
            self, return_type: Type, try_expr: Expr, var: str, catch_expr: Expr
        ): ...

    __match_args__ = ()

    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["pure"], Pure],
        _typing.Tuple[_L["block"], Block],
        _typing.Tuple[_L["create"], Update.Create],
        _typing.Tuple[_L["exercise"], Update.Exercise],
        _typing.Tuple[_L["exercise_by_key"], Update.ExerciseByKey],
        _typing.Tuple[_L["fetch"], Update.Fetch],
        _typing.Tuple[_L["get_time"], Unit],
        _typing.Tuple[_L["lookup_by_key"], Update.RetrieveByKey],
        _typing.Tuple[_L["fetch_by_key"], Update.RetrieveByKey],
        _typing.Tuple[_L["embed_expr"], Update.EmbedExpr],
        _typing.Tuple[_L["try_catch"], Update.TryCatch],
        _typing.Tuple[_L["create_interface"], Update.CreateInterface],
        _typing.Tuple[_L["exercise_interface"], Update.ExerciseInterface],
        _typing.Tuple[_L["fetch_interface"], Update.FetchInterface],
    ]: ...
    @property
    def pure(self) -> _typing.Optional[Pure]: ...
    @property
    def block(self) -> _typing.Optional[Block]: ...
    @property
    def create(self) -> _typing.Optional[Update.Create]: ...
    @property
    def exercise(self) -> _typing.Optional[Update.Exercise]: ...
    @property
    def exercise_by_key(self) -> _typing.Optional[Update.ExerciseByKey]: ...
    @property
    def fetch(self) -> _typing.Optional[Update.Fetch]: ...
    @property
    def get_time(self) -> _typing.Optional[Unit]: ...
    @property
    def lookup_by_key(self) -> _typing.Optional[Update.RetrieveByKey]: ...
    @property
    def fetch_by_key(self) -> _typing.Optional[Update.RetrieveByKey]: ...
    @property
    def embed_expr(self) -> _typing.Optional[Update.EmbedExpr]: ...
    @property
    def try_catch(self) -> _typing.Optional[Update.TryCatch]: ...
    @property
    def create_interface(self) -> _typing.Optional[Update.CreateInterface]: ...
    @property
    def exercise_interface(self) -> _typing.Optional[Update.ExerciseInterface]: ...
    @property
    def fetch_interface(self) -> _typing.Optional[Update.FetchInterface]: ...
    @_typing.overload
    def __init__(self, *, pure: Pure = ...): ...
    @_typing.overload
    def __init__(self, *, block: Block = ...): ...
    @_typing.overload
    def __init__(self, *, create: Update.Create = ...): ...
    @_typing.overload
    def __init__(self, *, exercise: Update.Exercise = ...): ...
    @_typing.overload
    def __init__(self, *, exercise_by_key: Update.ExerciseByKey = ...): ...
    @_typing.overload
    def __init__(self, *, fetch: Update.Fetch = ...): ...
    @_typing.overload
    def __init__(self, *, get_time: Unit = ...): ...
    @_typing.overload
    def __init__(self, *, lookup_by_key: Update.RetrieveByKey = ...): ...
    @_typing.overload
    def __init__(self, *, fetch_by_key: Update.RetrieveByKey = ...): ...
    @_typing.overload
    def __init__(self, *, embed_expr: Update.EmbedExpr = ...): ...
    @_typing.overload
    def __init__(self, *, try_catch: Update.TryCatch = ...): ...
    @_typing.overload
    def __init__(self, *, create_interface: Update.CreateInterface = ...): ...
    @_typing.overload
    def __init__(self, *, exercise_interface: Update.ExerciseInterface = ...): ...
    @_typing.overload
    def __init__(self, *, fetch_interface: Update.FetchInterface = ...): ...
    def Sum_match(
        self,
        pure: _typing.Callable[[Pure], _T],
        block: _typing.Callable[[Block], _T],
        create: _typing.Callable[[Update.Create], _T],
        exercise: _typing.Callable[[Update.Exercise], _T],
        exercise_by_key: _typing.Callable[[Update.ExerciseByKey], _T],
        fetch: _typing.Callable[[Update.Fetch], _T],
        get_time: _typing.Callable[[Unit], _T],
        lookup_by_key: _typing.Callable[[Update.RetrieveByKey], _T],
        fetch_by_key: _typing.Callable[[Update.RetrieveByKey], _T],
        embed_expr: _typing.Callable[[Update.EmbedExpr], _T],
        try_catch: _typing.Callable[[Update.TryCatch], _T],
        create_interface: _typing.Callable[[Update.CreateInterface], _T],
        exercise_interface: _typing.Callable[[Update.ExerciseInterface], _T],
        fetch_interface: _typing.Callable[[Update.FetchInterface], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Scenario:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Commit:
        __match_args__ = ("party", "expr", "ret_type")

        @property
        def party(self) -> Expr: ...
        @property
        def expr(self) -> Expr: ...
        @property
        def ret_type(self) -> Type: ...
        def __init__(self, party: Expr, expr: Expr, ret_type: Type): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EmbedExpr:
        __match_args__ = ("type", "body")

        @property
        def type(self) -> Type: ...
        @property
        def body(self) -> Expr: ...
        def __init__(self, type: Type, body: Expr): ...

    __match_args__ = ()

    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["pure"], Pure],
        _typing.Tuple[_L["block"], Block],
        _typing.Tuple[_L["commit"], Scenario.Commit],
        _typing.Tuple[_L["mustFailAt"], Scenario.Commit],
        _typing.Tuple[_L["pass"], Expr],
        _typing.Tuple[_L["get_time"], Unit],
        _typing.Tuple[_L["get_party"], Expr],
        _typing.Tuple[_L["embed_expr"], Scenario.EmbedExpr],
    ]: ...
    @property
    def pure(self) -> _typing.Optional[Pure]: ...
    @property
    def block(self) -> _typing.Optional[Block]: ...
    @property
    def commit(self) -> _typing.Optional[Scenario.Commit]: ...
    @property
    def must_fail_at(self) -> _typing.Optional[Scenario.Commit]: ...
    @property
    def pass_(self) -> _typing.Optional[Expr]: ...
    @property
    def get_time(self) -> _typing.Optional[Unit]: ...
    @property
    def get_party(self) -> _typing.Optional[Expr]: ...
    @property
    def embed_expr(self) -> _typing.Optional[Scenario.EmbedExpr]: ...
    @_typing.overload
    def __init__(self, *, pure: Pure = ...): ...
    @_typing.overload
    def __init__(self, *, block: Block = ...): ...
    @_typing.overload
    def __init__(self, *, commit: Scenario.Commit = ...): ...
    @_typing.overload
    def __init__(self, *, must_fail_at: Scenario.Commit = ...): ...
    @_typing.overload
    def __init__(self, *, pass_: Expr = ...): ...
    @_typing.overload
    def __init__(self, *, get_time: Unit = ...): ...
    @_typing.overload
    def __init__(self, *, get_party: Expr = ...): ...
    @_typing.overload
    def __init__(self, *, embed_expr: Scenario.EmbedExpr = ...): ...
    def Sum_match(
        self,
        pure: _typing.Callable[[Pure], _T],
        block: _typing.Callable[[Block], _T],
        commit: _typing.Callable[[Scenario.Commit], _T],
        must_fail_at: _typing.Callable[[Scenario.Commit], _T],
        pass_: _typing.Callable[[Expr], _T],
        get_time: _typing.Callable[[Unit], _T],
        get_party: _typing.Callable[[Expr], _T],
        embed_expr: _typing.Callable[[Scenario.EmbedExpr], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class TemplateChoice:
    __match_args__ = (
        "name",
        "consuming",
        "controllers",
        "arg_binder",
        "ret_type",
        "update",
        "self_binder",
    )

    @property
    def name(self) -> str: ...
    @property
    def consuming(self) -> bool: ...
    @property
    def controllers(self) -> Expr: ...
    @property
    def observers(self) -> _typing.Optional[Expr]: ...
    @property
    def arg_binder(self) -> VarWithType: ...
    @property
    def ret_type(self) -> Type: ...
    @property
    def update(self) -> Expr: ...
    @property
    def self_binder(self) -> str: ...
    @property
    def location(self) -> _typing.Optional[Location]: ...
    def __init__(
        self,
        name: str,
        consuming: bool,
        controllers: Expr,
        observers: _typing.Optional[Expr],
        arg_binder: VarWithType,
        ret_type: Type,
        update: Expr,
        self_binder: str,
        location: _typing.Optional[Location],
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class KeyExpr:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Projection:
        __match_args__ = ("tycon", "field")

        @property
        def tycon(self) -> Type.Con: ...
        @property
        def field(self) -> str: ...
        def __init__(self, tycon: Type.Con, field: str): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Projections:
        __match_args__ = ("projections",)

        @property
        def projections(self) -> _typing.Tuple[KeyExpr.Projection, ...]: ...
        def __init__(self, projections: _typing.Iterable[KeyExpr.Projection]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecordField:
        __match_args__ = ("field", "expr")

        @property
        def field(self) -> str: ...
        @property
        def expr(self) -> KeyExpr: ...
        def __init__(self, field: str, expr: KeyExpr): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Record:
        __match_args__ = ("tycon", "fields")

        @property
        def tycon(self) -> Type.Con: ...
        @property
        def fields(self) -> _typing.Tuple[KeyExpr.RecordField, ...]: ...
        def __init__(
            self, tycon: Type.Con, fields: _typing.Iterable[KeyExpr.RecordField]
        ): ...

    __match_args__ = ()

    @property
    def Sum(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["projections"], KeyExpr.Projections],
        _typing.Tuple[_L["record"], KeyExpr.Record],
    ]: ...
    @property
    def projections(self) -> _typing.Optional[KeyExpr.Projections]: ...
    @property
    def record(self) -> _typing.Optional[KeyExpr.Record]: ...
    @_typing.overload
    def __init__(self, *, projections: KeyExpr.Projections = ...): ...
    @_typing.overload
    def __init__(self, *, record: KeyExpr.Record = ...): ...
    def Sum_match(
        self,
        projections: _typing.Callable[[KeyExpr.Projections], _T],
        record: _typing.Callable[[KeyExpr.Record], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class InterfaceInstanceBody:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class InterfaceInstanceMethod:
        __match_args__ = ("method_interned_name", "value")

        @property
        def method_interned_name(self) -> int: ...
        @property
        def value(self) -> Expr: ...
        def __init__(self, method_interned_name: int, value: Expr): ...

    __match_args__ = ("methods", "view")

    @property
    def methods(
        self,
    ) -> _typing.Tuple[InterfaceInstanceBody.InterfaceInstanceMethod, ...]: ...
    @property
    def view(self) -> Expr: ...
    def __init__(
        self,
        methods: _typing.Iterable[InterfaceInstanceBody.InterfaceInstanceMethod],
        view: Expr,
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefTemplate:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class DefKey:
        __match_args__ = ("type", "maintainers")

        @property
        def type(self) -> Type: ...
        @property
        def key_expr(
            self,
        ) -> _typing.Union[
            _typing.Tuple[_L["key"], KeyExpr],
            _typing.Tuple[_L["complex_key"], Expr],
        ]: ...
        @property
        def key(self) -> _typing.Optional[KeyExpr]: ...
        @property
        def complex_key(self) -> _typing.Optional[Expr]: ...
        @property
        def maintainers(self) -> Expr: ...
        @_typing.overload
        def __init__(self, type: Type, maintainers: Expr, *, key: KeyExpr = ...): ...
        @_typing.overload
        def __init__(
            self, type: Type, maintainers: Expr, *, complex_key: Expr = ...
        ): ...
        def key_expr_match(
            self,
            key: _typing.Callable[[KeyExpr], _T],
            complex_key: _typing.Callable[[Expr], _T],
        ) -> _T: ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Implements:
        __match_args__ = ("interface", "body")

        @property
        def interface(self) -> TypeConName: ...
        @property
        def body(self) -> InterfaceInstanceBody: ...
        def __init__(self, interface: TypeConName, body: InterfaceInstanceBody): ...

    __match_args__ = (
        "tycon",
        "param",
        "precond",
        "signatories",
        "agreement",
        "choices",
        "observers",
        "implements",
    )

    @property
    def tycon(self) -> DottedName: ...
    @property
    def param(self) -> str: ...
    @property
    def precond(self) -> Expr: ...
    @property
    def signatories(self) -> Expr: ...
    @property
    def agreement(self) -> Expr: ...
    @property
    def choices(self) -> _typing.Tuple[TemplateChoice, ...]: ...
    @property
    def observers(self) -> Expr: ...
    @property
    def location(self) -> _typing.Optional[Location]: ...
    @property
    def key(self) -> _typing.Optional[DefTemplate.DefKey]: ...
    @property
    def implements(self) -> _typing.Tuple[DefTemplate.Implements, ...]: ...
    def __init__(
        self,
        tycon: DottedName,
        param: str,
        precond: Expr,
        signatories: Expr,
        agreement: Expr,
        choices: _typing.Iterable[TemplateChoice],
        observers: Expr,
        location: _typing.Optional[Location],
        key: _typing.Optional[DefTemplate.DefKey],
        implements: _typing.Iterable[DefTemplate.Implements],
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class InterfaceMethod:
    __match_args__ = ("location", "method_interned_name", "type")

    @property
    def location(self) -> Location: ...
    @property
    def method_interned_name(self) -> int: ...
    @property
    def type(self) -> Type: ...
    def __init__(self, location: Location, method_interned_name: int, type: Type): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefInterface:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class CoImplements:
        __match_args__ = ("template", "body")

        @property
        def template(self) -> TypeConName: ...
        @property
        def body(self) -> InterfaceInstanceBody: ...
        def __init__(self, template: TypeConName, body: InterfaceInstanceBody): ...

    __match_args__ = (
        "location",
        "tycon",
        "methods",
        "param",
        "choices",
        "co_implements",
        "view",
        "requires",
    )

    @property
    def location(self) -> Location: ...
    @property
    def tycon(self) -> DottedName: ...
    @property
    def methods(self) -> _typing.Tuple[InterfaceMethod, ...]: ...
    @property
    def param(self) -> str: ...
    @property
    def choices(self) -> _typing.Tuple[TemplateChoice, ...]: ...
    @property
    def co_implements(self) -> _typing.Tuple[DefInterface.CoImplements, ...]: ...
    @property
    def view(self) -> Type: ...
    @property
    def requires(self) -> _typing.Tuple[TypeConName, ...]: ...
    def __init__(
        self,
        location: Location,
        tycon: DottedName,
        methods: _typing.Iterable[InterfaceMethod],
        param: str,
        choices: _typing.Iterable[TemplateChoice],
        co_implements: _typing.Iterable[DefInterface.CoImplements],
        view: Type,
        requires: _typing.Iterable[TypeConName],
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefException:
    __match_args__ = ("name", "message")

    @property
    def name(self) -> DottedName: ...
    @property
    def location(self) -> _typing.Optional[Location]: ...
    @property
    def message(self) -> Expr: ...
    def __init__(
        self, name: DottedName, location: _typing.Optional[Location], message: Expr
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefDataType:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Fields:
        __match_args__ = ("fields",)

        @property
        def fields(self) -> _typing.Tuple[FieldWithType, ...]: ...
        def __init__(self, fields: _typing.Iterable[FieldWithType]): ...

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EnumConstructors:
        __match_args__ = ("constructors",)

        @property
        def constructors(self) -> _typing.Tuple[str, ...]: ...
        def __init__(self, constructors: _typing.Iterable[str]): ...

    __match_args__ = ("params", "serializable")

    @property
    def name(self) -> _typing.Optional[DottedName]: ...
    @property
    def params(self) -> _typing.Tuple[TypeVarWithKind, ...]: ...
    @property
    def data_cons(
        self,
    ) -> _typing.Union[
        _typing.Tuple[_L["record"], DefDataType.Fields],
        _typing.Tuple[_L["variant"], DefDataType.Fields],
        _typing.Tuple[_L["enum"], DefDataType.EnumConstructors],
        _typing.Tuple[_L["interface"], Unit],
    ]: ...
    @property
    def record(self) -> _typing.Optional[DefDataType.Fields]: ...
    @property
    def variant(self) -> _typing.Optional[DefDataType.Fields]: ...
    @property
    def enum(self) -> _typing.Optional[DefDataType.EnumConstructors]: ...
    @property
    def interface(self) -> _typing.Optional[Unit]: ...
    @property
    def serializable(self) -> bool: ...
    @property
    def location(self) -> _typing.Optional[Location]: ...
    @_typing.overload
    def __init__(
        self,
        params: _typing.Iterable[TypeVarWithKind],
        serializable: bool,
        *,
        record: DefDataType.Fields = ...,
        name: _typing.Optional[DottedName] = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        params: _typing.Iterable[TypeVarWithKind],
        serializable: bool,
        *,
        variant: DefDataType.Fields = ...,
        name: _typing.Optional[DottedName] = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        params: _typing.Iterable[TypeVarWithKind],
        serializable: bool,
        *,
        enum: DefDataType.EnumConstructors = ...,
        name: _typing.Optional[DottedName] = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    @_typing.overload
    def __init__(
        self,
        params: _typing.Iterable[TypeVarWithKind],
        serializable: bool,
        *,
        interface: Unit = ...,
        name: _typing.Optional[DottedName] = ...,
        location: _typing.Optional[Location] = ...
    ): ...
    def data_cons_match(
        self,
        record: _typing.Callable[[DefDataType.Fields], _T],
        variant: _typing.Callable[[DefDataType.Fields], _T],
        enum: _typing.Callable[[DefDataType.EnumConstructors], _T],
        interface: _typing.Callable[[Unit], _T],
    ) -> _T: ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefTypeSyn:
    __match_args__ = ("name", "params", "type")

    @property
    def name(self) -> DottedName: ...
    @property
    def params(self) -> _typing.Tuple[TypeVarWithKind, ...]: ...
    @property
    def type(self) -> Type: ...
    @property
    def location(self) -> _typing.Optional[Location]: ...
    def __init__(
        self,
        name: DottedName,
        params: _typing.Iterable[TypeVarWithKind],
        type: Type,
        location: _typing.Optional[Location],
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefValue:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class NameWithType:
        __match_args__ = ("name", "type")

        @property
        def name(self) -> DottedName: ...
        @property
        def type(self) -> Type: ...
        def __init__(self, name: DottedName, type: Type): ...

    __match_args__ = ("name_with_type", "expr", "no_party_literals", "is_test")

    @property
    def name_with_type(self) -> DefValue.NameWithType: ...
    @property
    def expr(self) -> Expr: ...
    @property
    def no_party_literals(self) -> bool: ...
    @property
    def is_test(self) -> bool: ...
    @property
    def location(self) -> _typing.Optional[Location]: ...
    def __init__(
        self,
        name_with_type: DefValue.NameWithType,
        expr: Expr,
        no_party_literals: bool,
        is_test: bool,
        location: _typing.Optional[Location],
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class FeatureFlags:
    __match_args__ = (
        "forbid_party_literals",
        "dont_divulge_contract_ids_in_create_arguments",
        "dont_disclose_nonconsuming_choices_to_observers",
    )

    @property
    def forbid_party_literals(self) -> bool: ...
    @property
    def dont_divulge_contract_ids_in_create_arguments(self) -> bool: ...
    @property
    def dont_disclose_nonconsuming_choices_to_observers(self) -> bool: ...
    def __init__(
        self,
        forbid_party_literals: bool,
        dont_divulge_contract_ids_in_create_arguments: bool,
        dont_disclose_nonconsuming_choices_to_observers: bool,
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Module:
    __match_args__ = (
        "name",
        "flags",
        "synonyms",
        "data_types",
        "values",
        "templates",
        "exceptions",
        "interfaces",
    )

    @property
    def name(self) -> DottedName: ...
    @property
    def flags(self) -> FeatureFlags: ...
    @property
    def synonyms(self) -> _typing.Tuple[DefTypeSyn, ...]: ...
    @property
    def data_types(self) -> _typing.Tuple[DefDataType, ...]: ...
    @property
    def values(self) -> _typing.Tuple[DefValue, ...]: ...
    @property
    def templates(self) -> _typing.Tuple[DefTemplate, ...]: ...
    @property
    def exceptions(self) -> _typing.Tuple[DefException, ...]: ...
    @property
    def interfaces(self) -> _typing.Tuple[DefInterface, ...]: ...
    def __init__(
        self,
        name: DottedName,
        flags: FeatureFlags,
        synonyms: _typing.Iterable[DefTypeSyn],
        data_types: _typing.Iterable[DefDataType],
        values: _typing.Iterable[DefValue],
        templates: _typing.Iterable[DefTemplate],
        exceptions: _typing.Iterable[DefException],
        interfaces: _typing.Iterable[DefInterface],
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class PackageMetadata:
    __match_args__ = ("name", "version")

    @property
    def name(self) -> str: ...
    @property
    def version(self) -> str: ...
    def __init__(self, name: str, version: str): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Package:
    __match_args__ = ("modules",)

    @property
    def modules(self) -> _typing.Tuple[Module, ...]: ...
    @property
    def metadata(self) -> _typing.Optional[PackageMetadata]: ...
    def __init__(
        self,
        modules: _typing.Iterable[Module],
        metadata: _typing.Optional[PackageMetadata],
    ): ...

# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Archive:
    __match_args__ = ("hash", "package")

    @property
    def hash(self) -> PackageRef: ...
    @property
    def package(self) -> Package: ...
    def __init__(self, hash: PackageRef, package: Package): ...
