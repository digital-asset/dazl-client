import builtins as _builtins
from enum import IntEnum as _IntEnum
import sys


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
    TEXT_POINTS_TO_CODE = 106
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

    __slots__ = ()

    def __init__(self):
        pass

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(())

    def __eq__(self, __other):
        return self is __other

    def __ne__(self, __other):
        return self is not __other

    def __lt__(self, __other):
        return False

    def __le__(self, __other):
        return self is __other

    def __gt__(self, __other):
        return False

    def __ge__(self, __other):
        return self is __other

    def __repr__(self):
        return f"Unit()"


def PackageRef(s):
    return s


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DottedName:
    __match_args__ = ("segments",)

    __slots__ = ("segments",)

    def __init__(self, segments):
        object.__setattr__(self, "segments", _builtins.tuple(segments))

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.segments))

    def __eq__(self, __other):
        return self.segments == __other.segments

    def __ne__(self, __other):
        return self.segments != __other.segments

    def __lt__(self, __other):
        return (self.segments) < (__other.segments)

    def __le__(self, __other):
        return (self.segments) <= (__other.segments)

    def __gt__(self, __other):
        return (self.segments) > (__other.segments)

    def __ge__(self, __other):
        return (self.segments) >= (__other.segments)

    def __repr__(self):
        return f"DottedName(segments={self.segments!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class ModuleRef:
    __match_args__ = ("package_ref", "module_name")

    __slots__ = ("package_ref", "module_name")

    def __init__(self, package_ref, module_name):
        object.__setattr__(self, "package_ref", package_ref)
        object.__setattr__(self, "module_name", module_name)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.package_ref, self.module_name))

    def __eq__(self, __other):
        return self.package_ref == __other.package_ref and self.module_name == __other.module_name

    def __ne__(self, __other):
        return self.package_ref != __other.package_ref or self.module_name != __other.module_name

    def __lt__(self, __other):
        return (self.package_ref, self.module_name) < (
            __other.package_ref,
            __other.module_name,
        )

    def __le__(self, __other):
        return (self.package_ref, self.module_name) <= (
            __other.package_ref,
            __other.module_name,
        )

    def __gt__(self, __other):
        return (self.package_ref, self.module_name) > (
            __other.package_ref,
            __other.module_name,
        )

    def __ge__(self, __other):
        return (self.package_ref, self.module_name) >= (
            __other.package_ref,
            __other.module_name,
        )

    def __repr__(self):
        return f"ModuleRef(package_ref={self.package_ref!r}, module_name={self.module_name!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class TypeConName:
    __match_args__ = ("module", "name")

    __slots__ = ("module", "name")

    def __init__(self, module, name):
        object.__setattr__(self, "module", module)
        object.__setattr__(self, "name", name)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.module, self.name))

    def __eq__(self, __other):
        return self.module == __other.module and self.name == __other.name

    def __ne__(self, __other):
        return self.module != __other.module or self.name != __other.name

    def __lt__(self, __other):
        return (self.module, self.name) < (__other.module, __other.name)

    def __le__(self, __other):
        return (self.module, self.name) <= (__other.module, __other.name)

    def __gt__(self, __other):
        return (self.module, self.name) > (__other.module, __other.name)

    def __ge__(self, __other):
        return (self.module, self.name) >= (__other.module, __other.name)

    def __repr__(self):
        return f"TypeConName(module={self.module!r}, name={self.name!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class TypeSynName:
    __match_args__ = ("module", "name")

    __slots__ = ("module", "name")

    def __init__(self, module, name):
        object.__setattr__(self, "module", module)
        object.__setattr__(self, "name", name)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.module, self.name))

    def __eq__(self, __other):
        return self.module == __other.module and self.name == __other.name

    def __ne__(self, __other):
        return self.module != __other.module or self.name != __other.name

    def __lt__(self, __other):
        return (self.module, self.name) < (__other.module, __other.name)

    def __le__(self, __other):
        return (self.module, self.name) <= (__other.module, __other.name)

    def __gt__(self, __other):
        return (self.module, self.name) > (__other.module, __other.name)

    def __ge__(self, __other):
        return (self.module, self.name) >= (__other.module, __other.name)

    def __repr__(self):
        return f"TypeSynName(module={self.module!r}, name={self.name!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class ValName:
    __match_args__ = ("module", "name")

    __slots__ = ("module", "name")

    def __init__(self, module, name):
        object.__setattr__(self, "module", module)
        object.__setattr__(self, "name", name)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.module, self.name))

    def __eq__(self, __other):
        return self.module == __other.module and self.name == __other.name

    def __ne__(self, __other):
        return self.module != __other.module or self.name != __other.name

    def __lt__(self, __other):
        return (self.module, self.name) < (__other.module, __other.name)

    def __le__(self, __other):
        return (self.module, self.name) <= (__other.module, __other.name)

    def __gt__(self, __other):
        return (self.module, self.name) > (__other.module, __other.name)

    def __ge__(self, __other):
        return (self.module, self.name) >= (__other.module, __other.name)

    def __repr__(self):
        return f"ValName(module={self.module!r}, name={self.name!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class FieldWithType:
    __match_args__ = ("field", "type")

    __slots__ = ("field", "type")

    def __init__(self, field, type):
        object.__setattr__(self, "field", field)
        object.__setattr__(self, "type", type)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.field, self.type))

    def __eq__(self, __other):
        return self.field == __other.field and self.type == __other.type

    def __ne__(self, __other):
        return self.field != __other.field or self.type != __other.type

    def __lt__(self, __other):
        return (self.field, self.type) < (__other.field, __other.type)

    def __le__(self, __other):
        return (self.field, self.type) <= (__other.field, __other.type)

    def __gt__(self, __other):
        return (self.field, self.type) > (__other.field, __other.type)

    def __ge__(self, __other):
        return (self.field, self.type) >= (__other.field, __other.type)

    def __repr__(self):
        return f"FieldWithType(field={self.field!r}, type={self.type!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class VarWithType:
    __match_args__ = ("var", "type")

    __slots__ = ("var", "type")

    def __init__(self, var, type):
        object.__setattr__(self, "var", var)
        object.__setattr__(self, "type", type)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.var, self.type))

    def __eq__(self, __other):
        return self.var == __other.var and self.type == __other.type

    def __ne__(self, __other):
        return self.var != __other.var or self.type != __other.type

    def __lt__(self, __other):
        return (self.var, self.type) < (__other.var, __other.type)

    def __le__(self, __other):
        return (self.var, self.type) <= (__other.var, __other.type)

    def __gt__(self, __other):
        return (self.var, self.type) > (__other.var, __other.type)

    def __ge__(self, __other):
        return (self.var, self.type) >= (__other.var, __other.type)

    def __repr__(self):
        return f"VarWithType(var={self.var!r}, type={self.type!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class TypeVarWithKind:
    __match_args__ = ("var", "kind")

    __slots__ = ("var", "kind")

    def __init__(self, var, kind):
        object.__setattr__(self, "var", var)
        object.__setattr__(self, "kind", kind)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.var, self.kind))

    def __eq__(self, __other):
        return self.var == __other.var and self.kind == __other.kind

    def __ne__(self, __other):
        return self.var != __other.var or self.kind != __other.kind

    def __lt__(self, __other):
        return (self.var, self.kind) < (__other.var, __other.kind)

    def __le__(self, __other):
        return (self.var, self.kind) <= (__other.var, __other.kind)

    def __gt__(self, __other):
        return (self.var, self.kind) > (__other.var, __other.kind)

    def __ge__(self, __other):
        return (self.var, self.kind) >= (__other.var, __other.kind)

    def __repr__(self):
        return f"TypeVarWithKind(var={self.var!r}, kind={self.kind!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class FieldWithExpr:
    __match_args__ = ("field", "expr")

    __slots__ = ("field", "expr")

    def __init__(self, field, expr):
        object.__setattr__(self, "field", field)
        object.__setattr__(self, "expr", expr)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.field, self.expr))

    def __eq__(self, __other):
        return self.field == __other.field and self.expr == __other.expr

    def __ne__(self, __other):
        return self.field != __other.field or self.expr != __other.expr

    def __lt__(self, __other):
        return (self.field, self.expr) < (__other.field, __other.expr)

    def __le__(self, __other):
        return (self.field, self.expr) <= (__other.field, __other.expr)

    def __gt__(self, __other):
        return (self.field, self.expr) > (__other.field, __other.expr)

    def __ge__(self, __other):
        return (self.field, self.expr) >= (__other.field, __other.expr)

    def __repr__(self):
        return f"FieldWithExpr(field={self.field!r}, expr={self.expr!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Binding:
    __match_args__ = ("binder", "bound")

    __slots__ = ("binder", "bound")

    def __init__(self, binder, bound):
        object.__setattr__(self, "binder", binder)
        object.__setattr__(self, "bound", bound)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.binder, self.bound))

    def __eq__(self, __other):
        return self.binder == __other.binder and self.bound == __other.bound

    def __ne__(self, __other):
        return self.binder != __other.binder or self.bound != __other.bound

    def __lt__(self, __other):
        return (self.binder, self.bound) < (__other.binder, __other.bound)

    def __le__(self, __other):
        return (self.binder, self.bound) <= (__other.binder, __other.bound)

    def __gt__(self, __other):
        return (self.binder, self.bound) > (__other.binder, __other.bound)

    def __ge__(self, __other):
        return (self.binder, self.bound) >= (__other.binder, __other.bound)

    def __repr__(self):
        return f"Binding(binder={self.binder!r}, bound={self.bound!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Kind:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Arrow:
        __match_args__ = ("params", "result")

        __slots__ = ("params", "result")

        def __init__(self, params, result):
            object.__setattr__(self, "params", _builtins.tuple(params))
            object.__setattr__(self, "result", result)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.params, self.result))

        def __eq__(self, __other):
            return self.params == __other.params and self.result == __other.result

        def __ne__(self, __other):
            return self.params != __other.params or self.result != __other.result

        def __lt__(self, __other):
            return (self.params, self.result) < (__other.params, __other.result)

        def __le__(self, __other):
            return (self.params, self.result) <= (__other.params, __other.result)

        def __gt__(self, __other):
            return (self.params, self.result) > (__other.params, __other.result)

        def __ge__(self, __other):
            return (self.params, self.result) >= (__other.params, __other.result)

        def __repr__(self):
            return f"Kind.Arrow(params={self.params!r}, result={self.result!r}, )"

    __match_args__ = ()

    __slots__ = ("Sum",)

    def __init__(self, *, star=None, arrow=None, nat=None):
        Sum = []
        if star is not None:
            object.__setattr__(self, "Sum", ("star", star))
            Sum.append("star")
        if arrow is not None:
            object.__setattr__(self, "Sum", ("arrow", arrow))
            Sum.append("arrow")
        if nat is not None:
            object.__setattr__(self, "Sum", ("nat", nat))
            Sum.append("nat")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(self, star, arrow, nat):
        if self.Sum[0] == "star":
            return star(self.Sum[1])
        elif self.Sum[0] == "arrow":
            return arrow(self.Sum[1])
        elif self.Sum[0] == "nat":
            return nat(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.Sum))

    def __eq__(self, __other):
        return self.Sum == __other.Sum

    def __ne__(self, __other):
        return self.Sum != __other.Sum

    def __lt__(self, __other):
        return (self.Sum) < (__other.Sum)

    def __le__(self, __other):
        return (self.Sum) <= (__other.Sum)

    def __gt__(self, __other):
        return (self.Sum) > (__other.Sum)

    def __ge__(self, __other):
        return (self.Sum) >= (__other.Sum)

    def __repr__(self):
        return f"Kind({self.Sum[0]}={self.Sum[1]!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Type:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Var:
        __match_args__ = ("var", "args")

        __slots__ = ("var", "args")

        def __init__(self, var, args):
            object.__setattr__(self, "var", var)
            object.__setattr__(self, "args", _builtins.tuple(args))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.var, self.args))

        def __eq__(self, __other):
            return self.var == __other.var and self.args == __other.args

        def __ne__(self, __other):
            return self.var != __other.var or self.args != __other.args

        def __lt__(self, __other):
            return (self.var, self.args) < (__other.var, __other.args)

        def __le__(self, __other):
            return (self.var, self.args) <= (__other.var, __other.args)

        def __gt__(self, __other):
            return (self.var, self.args) > (__other.var, __other.args)

        def __ge__(self, __other):
            return (self.var, self.args) >= (__other.var, __other.args)

        def __repr__(self):
            return f"Type.Var(var={self.var!r}, args={self.args!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Con:
        __match_args__ = ("tycon", "args")

        __slots__ = ("tycon", "args")

        def __init__(self, tycon, args):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "args", _builtins.tuple(args))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.args))

        def __eq__(self, __other):
            return self.tycon == __other.tycon and self.args == __other.args

        def __ne__(self, __other):
            return self.tycon != __other.tycon or self.args != __other.args

        def __lt__(self, __other):
            return (self.tycon, self.args) < (__other.tycon, __other.args)

        def __le__(self, __other):
            return (self.tycon, self.args) <= (__other.tycon, __other.args)

        def __gt__(self, __other):
            return (self.tycon, self.args) > (__other.tycon, __other.args)

        def __ge__(self, __other):
            return (self.tycon, self.args) >= (__other.tycon, __other.args)

        def __repr__(self):
            return f"Type.Con(tycon={self.tycon!r}, args={self.args!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Syn:
        __match_args__ = ("tysyn", "args")

        __slots__ = ("tysyn", "args")

        def __init__(self, tysyn, args):
            object.__setattr__(self, "tysyn", tysyn)
            object.__setattr__(self, "args", _builtins.tuple(args))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tysyn, self.args))

        def __eq__(self, __other):
            return self.tysyn == __other.tysyn and self.args == __other.args

        def __ne__(self, __other):
            return self.tysyn != __other.tysyn or self.args != __other.args

        def __lt__(self, __other):
            return (self.tysyn, self.args) < (__other.tysyn, __other.args)

        def __le__(self, __other):
            return (self.tysyn, self.args) <= (__other.tysyn, __other.args)

        def __gt__(self, __other):
            return (self.tysyn, self.args) > (__other.tysyn, __other.args)

        def __ge__(self, __other):
            return (self.tysyn, self.args) >= (__other.tysyn, __other.args)

        def __repr__(self):
            return f"Type.Syn(tysyn={self.tysyn!r}, args={self.args!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Prim:
        __match_args__ = ("prim", "args")

        __slots__ = ("prim", "args")

        def __init__(self, prim, args):
            object.__setattr__(self, "prim", prim)
            object.__setattr__(self, "args", _builtins.tuple(args))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.prim, self.args))

        def __eq__(self, __other):
            return self.prim == __other.prim and self.args == __other.args

        def __ne__(self, __other):
            return self.prim != __other.prim or self.args != __other.args

        def __lt__(self, __other):
            return (self.prim, self.args) < (__other.prim, __other.args)

        def __le__(self, __other):
            return (self.prim, self.args) <= (__other.prim, __other.args)

        def __gt__(self, __other):
            return (self.prim, self.args) > (__other.prim, __other.args)

        def __ge__(self, __other):
            return (self.prim, self.args) >= (__other.prim, __other.args)

        def __repr__(self):
            return f"Type.Prim(prim={self.prim!r}, args={self.args!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Fun:
        __match_args__ = ("params", "result")

        __slots__ = ("params", "result")

        def __init__(self, params, result):
            object.__setattr__(self, "params", _builtins.tuple(params))
            object.__setattr__(self, "result", result)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.params, self.result))

        def __eq__(self, __other):
            return self.params == __other.params and self.result == __other.result

        def __ne__(self, __other):
            return self.params != __other.params or self.result != __other.result

        def __lt__(self, __other):
            return (self.params, self.result) < (__other.params, __other.result)

        def __le__(self, __other):
            return (self.params, self.result) <= (__other.params, __other.result)

        def __gt__(self, __other):
            return (self.params, self.result) > (__other.params, __other.result)

        def __ge__(self, __other):
            return (self.params, self.result) >= (__other.params, __other.result)

        def __repr__(self):
            return f"Type.Fun(params={self.params!r}, result={self.result!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Forall:
        __match_args__ = ("vars", "body")

        __slots__ = ("vars", "body")

        def __init__(self, vars, body):
            object.__setattr__(self, "vars", _builtins.tuple(vars))
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.vars, self.body))

        def __eq__(self, __other):
            return self.vars == __other.vars and self.body == __other.body

        def __ne__(self, __other):
            return self.vars != __other.vars or self.body != __other.body

        def __lt__(self, __other):
            return (self.vars, self.body) < (__other.vars, __other.body)

        def __le__(self, __other):
            return (self.vars, self.body) <= (__other.vars, __other.body)

        def __gt__(self, __other):
            return (self.vars, self.body) > (__other.vars, __other.body)

        def __ge__(self, __other):
            return (self.vars, self.body) >= (__other.vars, __other.body)

        def __repr__(self):
            return f"Type.Forall(vars={self.vars!r}, body={self.body!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Struct:
        __match_args__ = ("fields",)

        __slots__ = ("fields",)

        def __init__(self, fields):
            object.__setattr__(self, "fields", _builtins.tuple(fields))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.fields))

        def __eq__(self, __other):
            return self.fields == __other.fields

        def __ne__(self, __other):
            return self.fields != __other.fields

        def __lt__(self, __other):
            return (self.fields) < (__other.fields)

        def __le__(self, __other):
            return (self.fields) <= (__other.fields)

        def __gt__(self, __other):
            return (self.fields) > (__other.fields)

        def __ge__(self, __other):
            return (self.fields) >= (__other.fields)

        def __repr__(self):
            return f"Type.Struct(fields={self.fields!r}, )"

    __match_args__ = ()

    __slots__ = ("Sum",)

    def __init__(
        self,
        *,
        var=None,
        con=None,
        prim=None,
        forall=None,
        struct=None,
        nat=None,
        syn=None,
    ):
        Sum = []
        if var is not None:
            object.__setattr__(self, "Sum", ("var", var))
            Sum.append("var")
        if con is not None:
            object.__setattr__(self, "Sum", ("con", con))
            Sum.append("con")
        if prim is not None:
            object.__setattr__(self, "Sum", ("prim", prim))
            Sum.append("prim")
        if forall is not None:
            object.__setattr__(self, "Sum", ("forall", forall))
            Sum.append("forall")
        if struct is not None:
            object.__setattr__(self, "Sum", ("struct", struct))
            Sum.append("struct")
        if nat is not None:
            object.__setattr__(self, "Sum", ("nat", nat))
            Sum.append("nat")
        if syn is not None:
            object.__setattr__(self, "Sum", ("syn", syn))
            Sum.append("syn")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(self, var, con, prim, forall, struct, nat, syn):
        if self.Sum[0] == "var":
            return var(self.Sum[1])
        elif self.Sum[0] == "con":
            return con(self.Sum[1])
        elif self.Sum[0] == "prim":
            return prim(self.Sum[1])
        elif self.Sum[0] == "forall":
            return forall(self.Sum[1])
        elif self.Sum[0] == "struct":
            return struct(self.Sum[1])
        elif self.Sum[0] == "nat":
            return nat(self.Sum[1])
        elif self.Sum[0] == "syn":
            return syn(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.Sum))

    def __eq__(self, __other):
        return self.Sum == __other.Sum

    def __ne__(self, __other):
        return self.Sum != __other.Sum

    def __lt__(self, __other):
        return (self.Sum) < (__other.Sum)

    def __le__(self, __other):
        return (self.Sum) <= (__other.Sum)

    def __gt__(self, __other):
        return (self.Sum) > (__other.Sum)

    def __ge__(self, __other):
        return (self.Sum) >= (__other.Sum)

    def __repr__(self):
        return f"Type({self.Sum[0]}={self.Sum[1]!r}, )"


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

    __slots__ = ("Sum",)

    def __init__(
        self,
        *,
        int64=None,
        decimal=None,
        numeric=None,
        text=None,
        timestamp=None,
        party=None,
        date=None,
        rounding_mode=None,
    ):
        Sum = []
        if int64 is not None:
            object.__setattr__(self, "Sum", ("int64", int64))
            Sum.append("int64")
        if decimal is not None:
            object.__setattr__(self, "Sum", ("decimal", decimal))
            Sum.append("decimal")
        if numeric is not None:
            object.__setattr__(self, "Sum", ("numeric", numeric))
            Sum.append("numeric")
        if text is not None:
            object.__setattr__(self, "Sum", ("text", text))
            Sum.append("text")
        if timestamp is not None:
            object.__setattr__(self, "Sum", ("timestamp", timestamp))
            Sum.append("timestamp")
        if party is not None:
            object.__setattr__(self, "Sum", ("party", party))
            Sum.append("party")
        if date is not None:
            object.__setattr__(self, "Sum", ("date", date))
            Sum.append("date")
        if rounding_mode is not None:
            object.__setattr__(self, "Sum", ("rounding_mode", rounding_mode))
            Sum.append("rounding_mode")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(self, int64, decimal, numeric, text, timestamp, party, date, rounding_mode):
        if self.Sum[0] == "int64":
            return int64(self.Sum[1])
        elif self.Sum[0] == "decimal":
            return decimal(self.Sum[1])
        elif self.Sum[0] == "numeric":
            return numeric(self.Sum[1])
        elif self.Sum[0] == "text":
            return text(self.Sum[1])
        elif self.Sum[0] == "timestamp":
            return timestamp(self.Sum[1])
        elif self.Sum[0] == "party":
            return party(self.Sum[1])
        elif self.Sum[0] == "date":
            return date(self.Sum[1])
        elif self.Sum[0] == "rounding_mode":
            return rounding_mode(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.Sum))

    def __eq__(self, __other):
        return self.Sum == __other.Sum

    def __ne__(self, __other):
        return self.Sum != __other.Sum

    def __lt__(self, __other):
        return (self.Sum) < (__other.Sum)

    def __le__(self, __other):
        return (self.Sum) <= (__other.Sum)

    def __gt__(self, __other):
        return (self.Sum) > (__other.Sum)

    def __ge__(self, __other):
        return (self.Sum) >= (__other.Sum)

    def __repr__(self):
        return f"PrimLit({self.Sum[0]}={self.Sum[1]!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Location:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Range:
        __match_args__ = ("start_line", "start_col", "end_line", "end_col")

        __slots__ = ("start_line", "start_col", "end_line", "end_col")

        def __init__(self, start_line, start_col, end_line, end_col):
            object.__setattr__(self, "start_line", start_line)
            object.__setattr__(self, "start_col", start_col)
            object.__setattr__(self, "end_line", end_line)
            object.__setattr__(self, "end_col", end_col)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.start_line, self.start_col, self.end_line, self.end_col))

        def __eq__(self, __other):
            return (
                self.start_line == __other.start_line
                and self.start_col == __other.start_col
                and self.end_line == __other.end_line
                and self.end_col == __other.end_col
            )

        def __ne__(self, __other):
            return (
                self.start_line != __other.start_line
                or self.start_col != __other.start_col
                or self.end_line != __other.end_line
                or self.end_col != __other.end_col
            )

        def __lt__(self, __other):
            return (self.start_line, self.start_col, self.end_line, self.end_col) < (
                __other.start_line,
                __other.start_col,
                __other.end_line,
                __other.end_col,
            )

        def __le__(self, __other):
            return (self.start_line, self.start_col, self.end_line, self.end_col) <= (
                __other.start_line,
                __other.start_col,
                __other.end_line,
                __other.end_col,
            )

        def __gt__(self, __other):
            return (self.start_line, self.start_col, self.end_line, self.end_col) > (
                __other.start_line,
                __other.start_col,
                __other.end_line,
                __other.end_col,
            )

        def __ge__(self, __other):
            return (self.start_line, self.start_col, self.end_line, self.end_col) >= (
                __other.start_line,
                __other.start_col,
                __other.end_line,
                __other.end_col,
            )

        def __repr__(self):
            return f"Location.Range(start_line={self.start_line!r}, start_col={self.start_col!r}, end_line={self.end_line!r}, end_col={self.end_col!r}, )"

    __match_args__ = ("module", "range")

    __slots__ = ("module", "range")

    def __init__(self, module, range):
        object.__setattr__(self, "module", module)
        object.__setattr__(self, "range", range)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.module, self.range))

    def __eq__(self, __other):
        return self.module == __other.module and self.range == __other.range

    def __ne__(self, __other):
        return self.module != __other.module or self.range != __other.range

    def __lt__(self, __other):
        return (self.module, self.range) < (__other.module, __other.range)

    def __le__(self, __other):
        return (self.module, self.range) <= (__other.module, __other.range)

    def __gt__(self, __other):
        return (self.module, self.range) > (__other.module, __other.range)

    def __ge__(self, __other):
        return (self.module, self.range) >= (__other.module, __other.range)

    def __repr__(self):
        return f"Location(module={self.module!r}, range={self.range!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Expr:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecCon:
        __match_args__ = ("tycon", "fields")

        __slots__ = ("tycon", "fields")

        def __init__(self, tycon, fields):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "fields", _builtins.tuple(fields))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.fields))

        def __eq__(self, __other):
            return self.tycon == __other.tycon and self.fields == __other.fields

        def __ne__(self, __other):
            return self.tycon != __other.tycon or self.fields != __other.fields

        def __lt__(self, __other):
            return (self.tycon, self.fields) < (__other.tycon, __other.fields)

        def __le__(self, __other):
            return (self.tycon, self.fields) <= (__other.tycon, __other.fields)

        def __gt__(self, __other):
            return (self.tycon, self.fields) > (__other.tycon, __other.fields)

        def __ge__(self, __other):
            return (self.tycon, self.fields) >= (__other.tycon, __other.fields)

        def __repr__(self):
            return f"Expr.RecCon(tycon={self.tycon!r}, fields={self.fields!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecProj:
        __match_args__ = ("tycon", "field", "record")

        __slots__ = ("tycon", "field", "record")

        def __init__(self, tycon, field, record):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "field", field)
            object.__setattr__(self, "record", record)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.field, self.record))

        def __eq__(self, __other):
            return (
                self.tycon == __other.tycon
                and self.field == __other.field
                and self.record == __other.record
            )

        def __ne__(self, __other):
            return (
                self.tycon != __other.tycon
                or self.field != __other.field
                or self.record != __other.record
            )

        def __lt__(self, __other):
            return (self.tycon, self.field, self.record) < (
                __other.tycon,
                __other.field,
                __other.record,
            )

        def __le__(self, __other):
            return (self.tycon, self.field, self.record) <= (
                __other.tycon,
                __other.field,
                __other.record,
            )

        def __gt__(self, __other):
            return (self.tycon, self.field, self.record) > (
                __other.tycon,
                __other.field,
                __other.record,
            )

        def __ge__(self, __other):
            return (self.tycon, self.field, self.record) >= (
                __other.tycon,
                __other.field,
                __other.record,
            )

        def __repr__(self):
            return f"Expr.RecProj(tycon={self.tycon!r}, field={self.field!r}, record={self.record!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecUpd:
        __match_args__ = ("tycon", "field", "record", "update")

        __slots__ = ("tycon", "field", "record", "update")

        def __init__(self, tycon, field, record, update):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "field", field)
            object.__setattr__(self, "record", record)
            object.__setattr__(self, "update", update)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.field, self.record, self.update))

        def __eq__(self, __other):
            return (
                self.tycon == __other.tycon
                and self.field == __other.field
                and self.record == __other.record
                and self.update == __other.update
            )

        def __ne__(self, __other):
            return (
                self.tycon != __other.tycon
                or self.field != __other.field
                or self.record != __other.record
                or self.update != __other.update
            )

        def __lt__(self, __other):
            return (self.tycon, self.field, self.record, self.update) < (
                __other.tycon,
                __other.field,
                __other.record,
                __other.update,
            )

        def __le__(self, __other):
            return (self.tycon, self.field, self.record, self.update) <= (
                __other.tycon,
                __other.field,
                __other.record,
                __other.update,
            )

        def __gt__(self, __other):
            return (self.tycon, self.field, self.record, self.update) > (
                __other.tycon,
                __other.field,
                __other.record,
                __other.update,
            )

        def __ge__(self, __other):
            return (self.tycon, self.field, self.record, self.update) >= (
                __other.tycon,
                __other.field,
                __other.record,
                __other.update,
            )

        def __repr__(self):
            return f"Expr.RecUpd(tycon={self.tycon!r}, field={self.field!r}, record={self.record!r}, update={self.update!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class VariantCon:
        __match_args__ = ("tycon", "variant_con", "variant_arg")

        __slots__ = ("tycon", "variant_con", "variant_arg")

        def __init__(self, tycon, variant_con, variant_arg):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "variant_con", variant_con)
            object.__setattr__(self, "variant_arg", variant_arg)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.variant_con, self.variant_arg))

        def __eq__(self, __other):
            return (
                self.tycon == __other.tycon
                and self.variant_con == __other.variant_con
                and self.variant_arg == __other.variant_arg
            )

        def __ne__(self, __other):
            return (
                self.tycon != __other.tycon
                or self.variant_con != __other.variant_con
                or self.variant_arg != __other.variant_arg
            )

        def __lt__(self, __other):
            return (self.tycon, self.variant_con, self.variant_arg) < (
                __other.tycon,
                __other.variant_con,
                __other.variant_arg,
            )

        def __le__(self, __other):
            return (self.tycon, self.variant_con, self.variant_arg) <= (
                __other.tycon,
                __other.variant_con,
                __other.variant_arg,
            )

        def __gt__(self, __other):
            return (self.tycon, self.variant_con, self.variant_arg) > (
                __other.tycon,
                __other.variant_con,
                __other.variant_arg,
            )

        def __ge__(self, __other):
            return (self.tycon, self.variant_con, self.variant_arg) >= (
                __other.tycon,
                __other.variant_con,
                __other.variant_arg,
            )

        def __repr__(self):
            return f"Expr.VariantCon(tycon={self.tycon!r}, variant_con={self.variant_con!r}, variant_arg={self.variant_arg!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EnumCon:
        __match_args__ = ("tycon", "enum_con")

        __slots__ = ("tycon", "enum_con")

        def __init__(self, tycon, enum_con):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "enum_con", enum_con)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.enum_con))

        def __eq__(self, __other):
            return self.tycon == __other.tycon and self.enum_con == __other.enum_con

        def __ne__(self, __other):
            return self.tycon != __other.tycon or self.enum_con != __other.enum_con

        def __lt__(self, __other):
            return (self.tycon, self.enum_con) < (__other.tycon, __other.enum_con)

        def __le__(self, __other):
            return (self.tycon, self.enum_con) <= (__other.tycon, __other.enum_con)

        def __gt__(self, __other):
            return (self.tycon, self.enum_con) > (__other.tycon, __other.enum_con)

        def __ge__(self, __other):
            return (self.tycon, self.enum_con) >= (__other.tycon, __other.enum_con)

        def __repr__(self):
            return f"Expr.EnumCon(tycon={self.tycon!r}, enum_con={self.enum_con!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class StructCon:
        __match_args__ = ("fields",)

        __slots__ = ("fields",)

        def __init__(self, fields):
            object.__setattr__(self, "fields", _builtins.tuple(fields))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.fields))

        def __eq__(self, __other):
            return self.fields == __other.fields

        def __ne__(self, __other):
            return self.fields != __other.fields

        def __lt__(self, __other):
            return (self.fields) < (__other.fields)

        def __le__(self, __other):
            return (self.fields) <= (__other.fields)

        def __gt__(self, __other):
            return (self.fields) > (__other.fields)

        def __ge__(self, __other):
            return (self.fields) >= (__other.fields)

        def __repr__(self):
            return f"Expr.StructCon(fields={self.fields!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class StructProj:
        __match_args__ = ("field", "struct")

        __slots__ = ("field", "struct")

        def __init__(self, field, struct):
            object.__setattr__(self, "field", field)
            object.__setattr__(self, "struct", struct)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.field, self.struct))

        def __eq__(self, __other):
            return self.field == __other.field and self.struct == __other.struct

        def __ne__(self, __other):
            return self.field != __other.field or self.struct != __other.struct

        def __lt__(self, __other):
            return (self.field, self.struct) < (__other.field, __other.struct)

        def __le__(self, __other):
            return (self.field, self.struct) <= (__other.field, __other.struct)

        def __gt__(self, __other):
            return (self.field, self.struct) > (__other.field, __other.struct)

        def __ge__(self, __other):
            return (self.field, self.struct) >= (__other.field, __other.struct)

        def __repr__(self):
            return f"Expr.StructProj(field={self.field!r}, struct={self.struct!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class StructUpd:
        __match_args__ = ("field", "struct", "update")

        __slots__ = ("field", "struct", "update")

        def __init__(self, field, struct, update):
            object.__setattr__(self, "field", field)
            object.__setattr__(self, "struct", struct)
            object.__setattr__(self, "update", update)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.field, self.struct, self.update))

        def __eq__(self, __other):
            return (
                self.field == __other.field
                and self.struct == __other.struct
                and self.update == __other.update
            )

        def __ne__(self, __other):
            return (
                self.field != __other.field
                or self.struct != __other.struct
                or self.update != __other.update
            )

        def __lt__(self, __other):
            return (self.field, self.struct, self.update) < (
                __other.field,
                __other.struct,
                __other.update,
            )

        def __le__(self, __other):
            return (self.field, self.struct, self.update) <= (
                __other.field,
                __other.struct,
                __other.update,
            )

        def __gt__(self, __other):
            return (self.field, self.struct, self.update) > (
                __other.field,
                __other.struct,
                __other.update,
            )

        def __ge__(self, __other):
            return (self.field, self.struct, self.update) >= (
                __other.field,
                __other.struct,
                __other.update,
            )

        def __repr__(self):
            return f"Expr.StructUpd(field={self.field!r}, struct={self.struct!r}, update={self.update!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class App:
        __match_args__ = ("fun", "args")

        __slots__ = ("fun", "args")

        def __init__(self, fun, args):
            object.__setattr__(self, "fun", fun)
            object.__setattr__(self, "args", _builtins.tuple(args))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.fun, self.args))

        def __eq__(self, __other):
            return self.fun == __other.fun and self.args == __other.args

        def __ne__(self, __other):
            return self.fun != __other.fun or self.args != __other.args

        def __lt__(self, __other):
            return (self.fun, self.args) < (__other.fun, __other.args)

        def __le__(self, __other):
            return (self.fun, self.args) <= (__other.fun, __other.args)

        def __gt__(self, __other):
            return (self.fun, self.args) > (__other.fun, __other.args)

        def __ge__(self, __other):
            return (self.fun, self.args) >= (__other.fun, __other.args)

        def __repr__(self):
            return f"Expr.App(fun={self.fun!r}, args={self.args!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class TyApp:
        __match_args__ = ("expr", "types")

        __slots__ = ("expr", "types")

        def __init__(self, expr, types):
            object.__setattr__(self, "expr", expr)
            object.__setattr__(self, "types", _builtins.tuple(types))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.expr, self.types))

        def __eq__(self, __other):
            return self.expr == __other.expr and self.types == __other.types

        def __ne__(self, __other):
            return self.expr != __other.expr or self.types != __other.types

        def __lt__(self, __other):
            return (self.expr, self.types) < (__other.expr, __other.types)

        def __le__(self, __other):
            return (self.expr, self.types) <= (__other.expr, __other.types)

        def __gt__(self, __other):
            return (self.expr, self.types) > (__other.expr, __other.types)

        def __ge__(self, __other):
            return (self.expr, self.types) >= (__other.expr, __other.types)

        def __repr__(self):
            return f"Expr.TyApp(expr={self.expr!r}, types={self.types!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Abs:
        __match_args__ = ("param", "body")

        __slots__ = ("param", "body")

        def __init__(self, param, body):
            object.__setattr__(self, "param", _builtins.tuple(param))
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.param, self.body))

        def __eq__(self, __other):
            return self.param == __other.param and self.body == __other.body

        def __ne__(self, __other):
            return self.param != __other.param or self.body != __other.body

        def __lt__(self, __other):
            return (self.param, self.body) < (__other.param, __other.body)

        def __le__(self, __other):
            return (self.param, self.body) <= (__other.param, __other.body)

        def __gt__(self, __other):
            return (self.param, self.body) > (__other.param, __other.body)

        def __ge__(self, __other):
            return (self.param, self.body) >= (__other.param, __other.body)

        def __repr__(self):
            return f"Expr.Abs(param={self.param!r}, body={self.body!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class TyAbs:
        __match_args__ = ("param", "body")

        __slots__ = ("param", "body")

        def __init__(self, param, body):
            object.__setattr__(self, "param", _builtins.tuple(param))
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.param, self.body))

        def __eq__(self, __other):
            return self.param == __other.param and self.body == __other.body

        def __ne__(self, __other):
            return self.param != __other.param or self.body != __other.body

        def __lt__(self, __other):
            return (self.param, self.body) < (__other.param, __other.body)

        def __le__(self, __other):
            return (self.param, self.body) <= (__other.param, __other.body)

        def __gt__(self, __other):
            return (self.param, self.body) > (__other.param, __other.body)

        def __ge__(self, __other):
            return (self.param, self.body) >= (__other.param, __other.body)

        def __repr__(self):
            return f"Expr.TyAbs(param={self.param!r}, body={self.body!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Nil:
        __match_args__ = ("type",)

        __slots__ = ("type",)

        def __init__(self, type):
            object.__setattr__(self, "type", type)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type))

        def __eq__(self, __other):
            return self.type == __other.type

        def __ne__(self, __other):
            return self.type != __other.type

        def __lt__(self, __other):
            return (self.type) < (__other.type)

        def __le__(self, __other):
            return (self.type) <= (__other.type)

        def __gt__(self, __other):
            return (self.type) > (__other.type)

        def __ge__(self, __other):
            return (self.type) >= (__other.type)

        def __repr__(self):
            return f"Expr.Nil(type={self.type!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Cons:
        __match_args__ = ("type", "front", "tail")

        __slots__ = ("type", "front", "tail")

        def __init__(self, type, front, tail):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "front", _builtins.tuple(front))
            object.__setattr__(self, "tail", tail)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.front, self.tail))

        def __eq__(self, __other):
            return (
                self.type == __other.type
                and self.front == __other.front
                and self.tail == __other.tail
            )

        def __ne__(self, __other):
            return (
                self.type != __other.type
                or self.front != __other.front
                or self.tail != __other.tail
            )

        def __lt__(self, __other):
            return (self.type, self.front, self.tail) < (
                __other.type,
                __other.front,
                __other.tail,
            )

        def __le__(self, __other):
            return (self.type, self.front, self.tail) <= (
                __other.type,
                __other.front,
                __other.tail,
            )

        def __gt__(self, __other):
            return (self.type, self.front, self.tail) > (
                __other.type,
                __other.front,
                __other.tail,
            )

        def __ge__(self, __other):
            return (self.type, self.front, self.tail) >= (
                __other.type,
                __other.front,
                __other.tail,
            )

        def __repr__(self):
            return f"Expr.Cons(type={self.type!r}, front={self.front!r}, tail={self.tail!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class OptionalNone:
        __match_args__ = ("type",)

        __slots__ = ("type",)

        def __init__(self, type):
            object.__setattr__(self, "type", type)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type))

        def __eq__(self, __other):
            return self.type == __other.type

        def __ne__(self, __other):
            return self.type != __other.type

        def __lt__(self, __other):
            return (self.type) < (__other.type)

        def __le__(self, __other):
            return (self.type) <= (__other.type)

        def __gt__(self, __other):
            return (self.type) > (__other.type)

        def __ge__(self, __other):
            return (self.type) >= (__other.type)

        def __repr__(self):
            return f"Expr.OptionalNone(type={self.type!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class OptionalSome:
        __match_args__ = ("type", "body")

        __slots__ = ("type", "body")

        def __init__(self, type, body):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.body))

        def __eq__(self, __other):
            return self.type == __other.type and self.body == __other.body

        def __ne__(self, __other):
            return self.type != __other.type or self.body != __other.body

        def __lt__(self, __other):
            return (self.type, self.body) < (__other.type, __other.body)

        def __le__(self, __other):
            return (self.type, self.body) <= (__other.type, __other.body)

        def __gt__(self, __other):
            return (self.type, self.body) > (__other.type, __other.body)

        def __ge__(self, __other):
            return (self.type, self.body) >= (__other.type, __other.body)

        def __repr__(self):
            return f"Expr.OptionalSome(type={self.type!r}, body={self.body!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ToAny:
        __match_args__ = ("type", "expr")

        __slots__ = ("type", "expr")

        def __init__(self, type, expr):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.expr))

        def __eq__(self, __other):
            return self.type == __other.type and self.expr == __other.expr

        def __ne__(self, __other):
            return self.type != __other.type or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.type, self.expr) < (__other.type, __other.expr)

        def __le__(self, __other):
            return (self.type, self.expr) <= (__other.type, __other.expr)

        def __gt__(self, __other):
            return (self.type, self.expr) > (__other.type, __other.expr)

        def __ge__(self, __other):
            return (self.type, self.expr) >= (__other.type, __other.expr)

        def __repr__(self):
            return f"Expr.ToAny(type={self.type!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromAny:
        __match_args__ = ("type", "expr")

        __slots__ = ("type", "expr")

        def __init__(self, type, expr):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.expr))

        def __eq__(self, __other):
            return self.type == __other.type and self.expr == __other.expr

        def __ne__(self, __other):
            return self.type != __other.type or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.type, self.expr) < (__other.type, __other.expr)

        def __le__(self, __other):
            return (self.type, self.expr) <= (__other.type, __other.expr)

        def __gt__(self, __other):
            return (self.type, self.expr) > (__other.type, __other.expr)

        def __ge__(self, __other):
            return (self.type, self.expr) >= (__other.type, __other.expr)

        def __repr__(self):
            return f"Expr.FromAny(type={self.type!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ToAnyException:
        __match_args__ = ("type", "expr")

        __slots__ = ("type", "expr")

        def __init__(self, type, expr):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.expr))

        def __eq__(self, __other):
            return self.type == __other.type and self.expr == __other.expr

        def __ne__(self, __other):
            return self.type != __other.type or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.type, self.expr) < (__other.type, __other.expr)

        def __le__(self, __other):
            return (self.type, self.expr) <= (__other.type, __other.expr)

        def __gt__(self, __other):
            return (self.type, self.expr) > (__other.type, __other.expr)

        def __ge__(self, __other):
            return (self.type, self.expr) >= (__other.type, __other.expr)

        def __repr__(self):
            return f"Expr.ToAnyException(type={self.type!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromAnyException:
        __match_args__ = ("type", "expr")

        __slots__ = ("type", "expr")

        def __init__(self, type, expr):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.expr))

        def __eq__(self, __other):
            return self.type == __other.type and self.expr == __other.expr

        def __ne__(self, __other):
            return self.type != __other.type or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.type, self.expr) < (__other.type, __other.expr)

        def __le__(self, __other):
            return (self.type, self.expr) <= (__other.type, __other.expr)

        def __gt__(self, __other):
            return (self.type, self.expr) > (__other.type, __other.expr)

        def __ge__(self, __other):
            return (self.type, self.expr) >= (__other.type, __other.expr)

        def __repr__(self):
            return f"Expr.FromAnyException(type={self.type!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Throw:
        __match_args__ = ("return_type", "exception_type", "exception_expr")

        __slots__ = ("return_type", "exception_type", "exception_expr")

        def __init__(self, return_type, exception_type, exception_expr):
            object.__setattr__(self, "return_type", return_type)
            object.__setattr__(self, "exception_type", exception_type)
            object.__setattr__(self, "exception_expr", exception_expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.return_type, self.exception_type, self.exception_expr))

        def __eq__(self, __other):
            return (
                self.return_type == __other.return_type
                and self.exception_type == __other.exception_type
                and self.exception_expr == __other.exception_expr
            )

        def __ne__(self, __other):
            return (
                self.return_type != __other.return_type
                or self.exception_type != __other.exception_type
                or self.exception_expr != __other.exception_expr
            )

        def __lt__(self, __other):
            return (self.return_type, self.exception_type, self.exception_expr) < (
                __other.return_type,
                __other.exception_type,
                __other.exception_expr,
            )

        def __le__(self, __other):
            return (self.return_type, self.exception_type, self.exception_expr) <= (
                __other.return_type,
                __other.exception_type,
                __other.exception_expr,
            )

        def __gt__(self, __other):
            return (self.return_type, self.exception_type, self.exception_expr) > (
                __other.return_type,
                __other.exception_type,
                __other.exception_expr,
            )

        def __ge__(self, __other):
            return (self.return_type, self.exception_type, self.exception_expr) >= (
                __other.return_type,
                __other.exception_type,
                __other.exception_expr,
            )

        def __repr__(self):
            return f"Expr.Throw(return_type={self.return_type!r}, exception_type={self.exception_type!r}, exception_expr={self.exception_expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Experimental:
        __match_args__ = ("name", "type")

        __slots__ = ("name", "type")

        def __init__(self, name, type):
            object.__setattr__(self, "name", name)
            object.__setattr__(self, "type", type)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.name, self.type))

        def __eq__(self, __other):
            return self.name == __other.name and self.type == __other.type

        def __ne__(self, __other):
            return self.name != __other.name or self.type != __other.type

        def __lt__(self, __other):
            return (self.name, self.type) < (__other.name, __other.type)

        def __le__(self, __other):
            return (self.name, self.type) <= (__other.name, __other.type)

        def __gt__(self, __other):
            return (self.name, self.type) > (__other.name, __other.type)

        def __ge__(self, __other):
            return (self.name, self.type) >= (__other.name, __other.type)

        def __repr__(self):
            return f"Expr.Experimental(name={self.name!r}, type={self.type!r}, )"

    __match_args__ = ()

    __slots__ = ("location", "Sum")

    def __init__(
        self,
        *,
        var=None,
        val=None,
        builtin=None,
        prim_con=None,
        prim_lit=None,
        rec_con=None,
        rec_proj=None,
        rec_upd=None,
        variant_con=None,
        enum_con=None,
        struct_con=None,
        struct_proj=None,
        struct_upd=None,
        app=None,
        ty_app=None,
        abs=None,
        ty_abs=None,
        case=None,
        let=None,
        nil=None,
        cons=None,
        update=None,
        scenario=None,
        optional_none=None,
        optional_some=None,
        to_any=None,
        from_any=None,
        type_rep=None,
        to_any_exception=None,
        from_any_exception=None,
        throw=None,
        experimental=None,
        location=None,
    ):
        object.__setattr__(self, "location", location)
        Sum = []
        if var is not None:
            object.__setattr__(self, "Sum", ("var", var))
            Sum.append("var")
        if val is not None:
            object.__setattr__(self, "Sum", ("val", val))
            Sum.append("val")
        if builtin is not None:
            object.__setattr__(self, "Sum", ("builtin", builtin))
            Sum.append("builtin")
        if prim_con is not None:
            object.__setattr__(self, "Sum", ("prim_con", prim_con))
            Sum.append("prim_con")
        if prim_lit is not None:
            object.__setattr__(self, "Sum", ("prim_lit", prim_lit))
            Sum.append("prim_lit")
        if rec_con is not None:
            object.__setattr__(self, "Sum", ("rec_con", rec_con))
            Sum.append("rec_con")
        if rec_proj is not None:
            object.__setattr__(self, "Sum", ("rec_proj", rec_proj))
            Sum.append("rec_proj")
        if rec_upd is not None:
            object.__setattr__(self, "Sum", ("rec_upd", rec_upd))
            Sum.append("rec_upd")
        if variant_con is not None:
            object.__setattr__(self, "Sum", ("variant_con", variant_con))
            Sum.append("variant_con")
        if enum_con is not None:
            object.__setattr__(self, "Sum", ("enum_con", enum_con))
            Sum.append("enum_con")
        if struct_con is not None:
            object.__setattr__(self, "Sum", ("struct_con", struct_con))
            Sum.append("struct_con")
        if struct_proj is not None:
            object.__setattr__(self, "Sum", ("struct_proj", struct_proj))
            Sum.append("struct_proj")
        if struct_upd is not None:
            object.__setattr__(self, "Sum", ("struct_upd", struct_upd))
            Sum.append("struct_upd")
        if app is not None:
            object.__setattr__(self, "Sum", ("app", app))
            Sum.append("app")
        if ty_app is not None:
            object.__setattr__(self, "Sum", ("ty_app", ty_app))
            Sum.append("ty_app")
        if abs is not None:
            object.__setattr__(self, "Sum", ("abs", abs))
            Sum.append("abs")
        if ty_abs is not None:
            object.__setattr__(self, "Sum", ("ty_abs", ty_abs))
            Sum.append("ty_abs")
        if case is not None:
            object.__setattr__(self, "Sum", ("case", case))
            Sum.append("case")
        if let is not None:
            object.__setattr__(self, "Sum", ("let", let))
            Sum.append("let")
        if nil is not None:
            object.__setattr__(self, "Sum", ("nil", nil))
            Sum.append("nil")
        if cons is not None:
            object.__setattr__(self, "Sum", ("cons", cons))
            Sum.append("cons")
        if update is not None:
            object.__setattr__(self, "Sum", ("update", update))
            Sum.append("update")
        if scenario is not None:
            object.__setattr__(self, "Sum", ("scenario", scenario))
            Sum.append("scenario")
        if optional_none is not None:
            object.__setattr__(self, "Sum", ("optional_none", optional_none))
            Sum.append("optional_none")
        if optional_some is not None:
            object.__setattr__(self, "Sum", ("optional_some", optional_some))
            Sum.append("optional_some")
        if to_any is not None:
            object.__setattr__(self, "Sum", ("to_any", to_any))
            Sum.append("to_any")
        if from_any is not None:
            object.__setattr__(self, "Sum", ("from_any", from_any))
            Sum.append("from_any")
        if type_rep is not None:
            object.__setattr__(self, "Sum", ("type_rep", type_rep))
            Sum.append("type_rep")
        if to_any_exception is not None:
            object.__setattr__(self, "Sum", ("to_any_exception", to_any_exception))
            Sum.append("to_any_exception")
        if from_any_exception is not None:
            object.__setattr__(self, "Sum", ("from_any_exception", from_any_exception))
            Sum.append("from_any_exception")
        if throw is not None:
            object.__setattr__(self, "Sum", ("throw", throw))
            Sum.append("throw")
        if experimental is not None:
            object.__setattr__(self, "Sum", ("experimental", experimental))
            Sum.append("experimental")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(
        self,
        var,
        val,
        builtin,
        prim_con,
        prim_lit,
        rec_con,
        rec_proj,
        rec_upd,
        variant_con,
        enum_con,
        struct_con,
        struct_proj,
        struct_upd,
        app,
        ty_app,
        abs,
        ty_abs,
        case,
        let,
        nil,
        cons,
        update,
        scenario,
        optional_none,
        optional_some,
        to_any,
        from_any,
        type_rep,
        to_any_exception,
        from_any_exception,
        throw,
        experimental,
    ):
        if self.Sum[0] == "var":
            return var(self.Sum[1])
        elif self.Sum[0] == "val":
            return val(self.Sum[1])
        elif self.Sum[0] == "builtin":
            return builtin(self.Sum[1])
        elif self.Sum[0] == "prim_con":
            return prim_con(self.Sum[1])
        elif self.Sum[0] == "prim_lit":
            return prim_lit(self.Sum[1])
        elif self.Sum[0] == "rec_con":
            return rec_con(self.Sum[1])
        elif self.Sum[0] == "rec_proj":
            return rec_proj(self.Sum[1])
        elif self.Sum[0] == "rec_upd":
            return rec_upd(self.Sum[1])
        elif self.Sum[0] == "variant_con":
            return variant_con(self.Sum[1])
        elif self.Sum[0] == "enum_con":
            return enum_con(self.Sum[1])
        elif self.Sum[0] == "struct_con":
            return struct_con(self.Sum[1])
        elif self.Sum[0] == "struct_proj":
            return struct_proj(self.Sum[1])
        elif self.Sum[0] == "struct_upd":
            return struct_upd(self.Sum[1])
        elif self.Sum[0] == "app":
            return app(self.Sum[1])
        elif self.Sum[0] == "ty_app":
            return ty_app(self.Sum[1])
        elif self.Sum[0] == "abs":
            return abs(self.Sum[1])
        elif self.Sum[0] == "ty_abs":
            return ty_abs(self.Sum[1])
        elif self.Sum[0] == "case":
            return case(self.Sum[1])
        elif self.Sum[0] == "let":
            return let(self.Sum[1])
        elif self.Sum[0] == "nil":
            return nil(self.Sum[1])
        elif self.Sum[0] == "cons":
            return cons(self.Sum[1])
        elif self.Sum[0] == "update":
            return update(self.Sum[1])
        elif self.Sum[0] == "scenario":
            return scenario(self.Sum[1])
        elif self.Sum[0] == "optional_none":
            return optional_none(self.Sum[1])
        elif self.Sum[0] == "optional_some":
            return optional_some(self.Sum[1])
        elif self.Sum[0] == "to_any":
            return to_any(self.Sum[1])
        elif self.Sum[0] == "from_any":
            return from_any(self.Sum[1])
        elif self.Sum[0] == "type_rep":
            return type_rep(self.Sum[1])
        elif self.Sum[0] == "to_any_exception":
            return to_any_exception(self.Sum[1])
        elif self.Sum[0] == "from_any_exception":
            return from_any_exception(self.Sum[1])
        elif self.Sum[0] == "throw":
            return throw(self.Sum[1])
        elif self.Sum[0] == "experimental":
            return experimental(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.location, self.Sum))

    def __eq__(self, __other):
        return self.location == __other.location and self.Sum == __other.Sum

    def __ne__(self, __other):
        return self.location != __other.location or self.Sum != __other.Sum

    def __lt__(self, __other):
        return (self.location, self.Sum) < (__other.location, __other.Sum)

    def __le__(self, __other):
        return (self.location, self.Sum) <= (__other.location, __other.Sum)

    def __gt__(self, __other):
        return (self.location, self.Sum) > (__other.location, __other.Sum)

    def __ge__(self, __other):
        return (self.location, self.Sum) >= (__other.location, __other.Sum)

    def __repr__(self):
        return f"Expr(location={self.location!r}, {self.Sum[0]}={self.Sum[1]!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class CaseAlt:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Variant:
        __match_args__ = ("con", "variant", "binder")

        __slots__ = ("con", "variant", "binder")

        def __init__(self, con, variant, binder):
            object.__setattr__(self, "con", con)
            object.__setattr__(self, "variant", variant)
            object.__setattr__(self, "binder", binder)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.con, self.variant, self.binder))

        def __eq__(self, __other):
            return (
                self.con == __other.con
                and self.variant == __other.variant
                and self.binder == __other.binder
            )

        def __ne__(self, __other):
            return (
                self.con != __other.con
                or self.variant != __other.variant
                or self.binder != __other.binder
            )

        def __lt__(self, __other):
            return (self.con, self.variant, self.binder) < (
                __other.con,
                __other.variant,
                __other.binder,
            )

        def __le__(self, __other):
            return (self.con, self.variant, self.binder) <= (
                __other.con,
                __other.variant,
                __other.binder,
            )

        def __gt__(self, __other):
            return (self.con, self.variant, self.binder) > (
                __other.con,
                __other.variant,
                __other.binder,
            )

        def __ge__(self, __other):
            return (self.con, self.variant, self.binder) >= (
                __other.con,
                __other.variant,
                __other.binder,
            )

        def __repr__(self):
            return f"CaseAlt.Variant(con={self.con!r}, variant={self.variant!r}, binder={self.binder!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Enum:
        __match_args__ = ("con", "constructor")

        __slots__ = ("con", "constructor")

        def __init__(self, con, constructor):
            object.__setattr__(self, "con", con)
            object.__setattr__(self, "constructor", constructor)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.con, self.constructor))

        def __eq__(self, __other):
            return self.con == __other.con and self.constructor == __other.constructor

        def __ne__(self, __other):
            return self.con != __other.con or self.constructor != __other.constructor

        def __lt__(self, __other):
            return (self.con, self.constructor) < (__other.con, __other.constructor)

        def __le__(self, __other):
            return (self.con, self.constructor) <= (__other.con, __other.constructor)

        def __gt__(self, __other):
            return (self.con, self.constructor) > (__other.con, __other.constructor)

        def __ge__(self, __other):
            return (self.con, self.constructor) >= (__other.con, __other.constructor)

        def __repr__(self):
            return f"CaseAlt.Enum(con={self.con!r}, constructor={self.constructor!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Cons:
        __match_args__ = ("var_head", "var_tail")

        __slots__ = ("var_head", "var_tail")

        def __init__(self, var_head, var_tail):
            object.__setattr__(self, "var_head", var_head)
            object.__setattr__(self, "var_tail", var_tail)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.var_head, self.var_tail))

        def __eq__(self, __other):
            return self.var_head == __other.var_head and self.var_tail == __other.var_tail

        def __ne__(self, __other):
            return self.var_head != __other.var_head or self.var_tail != __other.var_tail

        def __lt__(self, __other):
            return (self.var_head, self.var_tail) < (__other.var_head, __other.var_tail)

        def __le__(self, __other):
            return (self.var_head, self.var_tail) <= (
                __other.var_head,
                __other.var_tail,
            )

        def __gt__(self, __other):
            return (self.var_head, self.var_tail) > (__other.var_head, __other.var_tail)

        def __ge__(self, __other):
            return (self.var_head, self.var_tail) >= (
                __other.var_head,
                __other.var_tail,
            )

        def __repr__(self):
            return f"CaseAlt.Cons(var_head={self.var_head!r}, var_tail={self.var_tail!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class OptionalSome:
        __match_args__ = ("var_body",)

        __slots__ = ("var_body",)

        def __init__(self, var_body):
            object.__setattr__(self, "var_body", var_body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.var_body))

        def __eq__(self, __other):
            return self.var_body == __other.var_body

        def __ne__(self, __other):
            return self.var_body != __other.var_body

        def __lt__(self, __other):
            return (self.var_body) < (__other.var_body)

        def __le__(self, __other):
            return (self.var_body) <= (__other.var_body)

        def __gt__(self, __other):
            return (self.var_body) > (__other.var_body)

        def __ge__(self, __other):
            return (self.var_body) >= (__other.var_body)

        def __repr__(self):
            return f"CaseAlt.OptionalSome(var_body={self.var_body!r}, )"

    __match_args__ = ("body",)

    __slots__ = ("Sum", "body")

    def __init__(
        self,
        body,
        *,
        default=None,
        variant=None,
        prim_con=None,
        nil=None,
        cons=None,
        optional_none=None,
        optional_some=None,
        enum=None,
    ):
        object.__setattr__(self, "body", body)
        Sum = []
        if default is not None:
            object.__setattr__(self, "Sum", ("default", default))
            Sum.append("default")
        if variant is not None:
            object.__setattr__(self, "Sum", ("variant", variant))
            Sum.append("variant")
        if prim_con is not None:
            object.__setattr__(self, "Sum", ("prim_con", prim_con))
            Sum.append("prim_con")
        if nil is not None:
            object.__setattr__(self, "Sum", ("nil", nil))
            Sum.append("nil")
        if cons is not None:
            object.__setattr__(self, "Sum", ("cons", cons))
            Sum.append("cons")
        if optional_none is not None:
            object.__setattr__(self, "Sum", ("optional_none", optional_none))
            Sum.append("optional_none")
        if optional_some is not None:
            object.__setattr__(self, "Sum", ("optional_some", optional_some))
            Sum.append("optional_some")
        if enum is not None:
            object.__setattr__(self, "Sum", ("enum", enum))
            Sum.append("enum")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(self, default, variant, prim_con, nil, cons, optional_none, optional_some, enum):
        if self.Sum[0] == "default":
            return default(self.Sum[1])
        elif self.Sum[0] == "variant":
            return variant(self.Sum[1])
        elif self.Sum[0] == "prim_con":
            return prim_con(self.Sum[1])
        elif self.Sum[0] == "nil":
            return nil(self.Sum[1])
        elif self.Sum[0] == "cons":
            return cons(self.Sum[1])
        elif self.Sum[0] == "optional_none":
            return optional_none(self.Sum[1])
        elif self.Sum[0] == "optional_some":
            return optional_some(self.Sum[1])
        elif self.Sum[0] == "enum":
            return enum(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.Sum, self.body))

    def __eq__(self, __other):
        return self.Sum == __other.Sum and self.body == __other.body

    def __ne__(self, __other):
        return self.Sum != __other.Sum or self.body != __other.body

    def __lt__(self, __other):
        return (self.Sum, self.body) < (__other.Sum, __other.body)

    def __le__(self, __other):
        return (self.Sum, self.body) <= (__other.Sum, __other.body)

    def __gt__(self, __other):
        return (self.Sum, self.body) > (__other.Sum, __other.body)

    def __ge__(self, __other):
        return (self.Sum, self.body) >= (__other.Sum, __other.body)

    def __repr__(self):
        return f"CaseAlt({self.Sum[0]}={self.Sum[1]!r}, body={self.body!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Case:
    __match_args__ = ("scrut", "alts")

    __slots__ = ("scrut", "alts")

    def __init__(self, scrut, alts):
        object.__setattr__(self, "scrut", scrut)
        object.__setattr__(self, "alts", _builtins.tuple(alts))

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.scrut, self.alts))

    def __eq__(self, __other):
        return self.scrut == __other.scrut and self.alts == __other.alts

    def __ne__(self, __other):
        return self.scrut != __other.scrut or self.alts != __other.alts

    def __lt__(self, __other):
        return (self.scrut, self.alts) < (__other.scrut, __other.alts)

    def __le__(self, __other):
        return (self.scrut, self.alts) <= (__other.scrut, __other.alts)

    def __gt__(self, __other):
        return (self.scrut, self.alts) > (__other.scrut, __other.alts)

    def __ge__(self, __other):
        return (self.scrut, self.alts) >= (__other.scrut, __other.alts)

    def __repr__(self):
        return f"Case(scrut={self.scrut!r}, alts={self.alts!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Block:
    __match_args__ = ("bindings", "body")

    __slots__ = ("bindings", "body")

    def __init__(self, bindings, body):
        object.__setattr__(self, "bindings", _builtins.tuple(bindings))
        object.__setattr__(self, "body", body)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.bindings, self.body))

    def __eq__(self, __other):
        return self.bindings == __other.bindings and self.body == __other.body

    def __ne__(self, __other):
        return self.bindings != __other.bindings or self.body != __other.body

    def __lt__(self, __other):
        return (self.bindings, self.body) < (__other.bindings, __other.body)

    def __le__(self, __other):
        return (self.bindings, self.body) <= (__other.bindings, __other.body)

    def __gt__(self, __other):
        return (self.bindings, self.body) > (__other.bindings, __other.body)

    def __ge__(self, __other):
        return (self.bindings, self.body) >= (__other.bindings, __other.body)

    def __repr__(self):
        return f"Block(bindings={self.bindings!r}, body={self.body!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Pure:
    __match_args__ = ("type", "expr")

    __slots__ = ("type", "expr")

    def __init__(self, type, expr):
        object.__setattr__(self, "type", type)
        object.__setattr__(self, "expr", expr)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.type, self.expr))

    def __eq__(self, __other):
        return self.type == __other.type and self.expr == __other.expr

    def __ne__(self, __other):
        return self.type != __other.type or self.expr != __other.expr

    def __lt__(self, __other):
        return (self.type, self.expr) < (__other.type, __other.expr)

    def __le__(self, __other):
        return (self.type, self.expr) <= (__other.type, __other.expr)

    def __gt__(self, __other):
        return (self.type, self.expr) > (__other.type, __other.expr)

    def __ge__(self, __other):
        return (self.type, self.expr) >= (__other.type, __other.expr)

    def __repr__(self):
        return f"Pure(type={self.type!r}, expr={self.expr!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Update:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Create:
        __match_args__ = ("template", "expr")

        __slots__ = ("template", "expr")

        def __init__(self, template, expr):
            object.__setattr__(self, "template", template)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.template, self.expr))

        def __eq__(self, __other):
            return self.template == __other.template and self.expr == __other.expr

        def __ne__(self, __other):
            return self.template != __other.template or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.template, self.expr) < (__other.template, __other.expr)

        def __le__(self, __other):
            return (self.template, self.expr) <= (__other.template, __other.expr)

        def __gt__(self, __other):
            return (self.template, self.expr) > (__other.template, __other.expr)

        def __ge__(self, __other):
            return (self.template, self.expr) >= (__other.template, __other.expr)

        def __repr__(self):
            return f"Update.Create(template={self.template!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Exercise:
        __match_args__ = ("template", "choice", "cid", "arg")

        __slots__ = ("template", "choice", "cid", "arg")

        def __init__(self, template, choice, cid, arg):
            object.__setattr__(self, "template", template)
            object.__setattr__(self, "choice", choice)
            object.__setattr__(self, "cid", cid)
            object.__setattr__(self, "arg", arg)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.template, self.choice, self.cid, self.arg))

        def __eq__(self, __other):
            return (
                self.template == __other.template
                and self.choice == __other.choice
                and self.cid == __other.cid
                and self.arg == __other.arg
            )

        def __ne__(self, __other):
            return (
                self.template != __other.template
                or self.choice != __other.choice
                or self.cid != __other.cid
                or self.arg != __other.arg
            )

        def __lt__(self, __other):
            return (self.template, self.choice, self.cid, self.arg) < (
                __other.template,
                __other.choice,
                __other.cid,
                __other.arg,
            )

        def __le__(self, __other):
            return (self.template, self.choice, self.cid, self.arg) <= (
                __other.template,
                __other.choice,
                __other.cid,
                __other.arg,
            )

        def __gt__(self, __other):
            return (self.template, self.choice, self.cid, self.arg) > (
                __other.template,
                __other.choice,
                __other.cid,
                __other.arg,
            )

        def __ge__(self, __other):
            return (self.template, self.choice, self.cid, self.arg) >= (
                __other.template,
                __other.choice,
                __other.cid,
                __other.arg,
            )

        def __repr__(self):
            return f"Update.Exercise(template={self.template!r}, choice={self.choice!r}, cid={self.cid!r}, arg={self.arg!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ExerciseByKey:
        __match_args__ = ("template", "choice", "key", "arg")

        __slots__ = ("template", "choice", "key", "arg")

        def __init__(self, template, choice, key, arg):
            object.__setattr__(self, "template", template)
            object.__setattr__(self, "choice", choice)
            object.__setattr__(self, "key", key)
            object.__setattr__(self, "arg", arg)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.template, self.choice, self.key, self.arg))

        def __eq__(self, __other):
            return (
                self.template == __other.template
                and self.choice == __other.choice
                and self.key == __other.key
                and self.arg == __other.arg
            )

        def __ne__(self, __other):
            return (
                self.template != __other.template
                or self.choice != __other.choice
                or self.key != __other.key
                or self.arg != __other.arg
            )

        def __lt__(self, __other):
            return (self.template, self.choice, self.key, self.arg) < (
                __other.template,
                __other.choice,
                __other.key,
                __other.arg,
            )

        def __le__(self, __other):
            return (self.template, self.choice, self.key, self.arg) <= (
                __other.template,
                __other.choice,
                __other.key,
                __other.arg,
            )

        def __gt__(self, __other):
            return (self.template, self.choice, self.key, self.arg) > (
                __other.template,
                __other.choice,
                __other.key,
                __other.arg,
            )

        def __ge__(self, __other):
            return (self.template, self.choice, self.key, self.arg) >= (
                __other.template,
                __other.choice,
                __other.key,
                __other.arg,
            )

        def __repr__(self):
            return f"Update.ExerciseByKey(template={self.template!r}, choice={self.choice!r}, key={self.key!r}, arg={self.arg!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Fetch:
        __match_args__ = ("template", "cid")

        __slots__ = ("template", "cid")

        def __init__(self, template, cid):
            object.__setattr__(self, "template", template)
            object.__setattr__(self, "cid", cid)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.template, self.cid))

        def __eq__(self, __other):
            return self.template == __other.template and self.cid == __other.cid

        def __ne__(self, __other):
            return self.template != __other.template or self.cid != __other.cid

        def __lt__(self, __other):
            return (self.template, self.cid) < (__other.template, __other.cid)

        def __le__(self, __other):
            return (self.template, self.cid) <= (__other.template, __other.cid)

        def __gt__(self, __other):
            return (self.template, self.cid) > (__other.template, __other.cid)

        def __ge__(self, __other):
            return (self.template, self.cid) >= (__other.template, __other.cid)

        def __repr__(self):
            return f"Update.Fetch(template={self.template!r}, cid={self.cid!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EmbedExpr:
        __match_args__ = ("type", "body")

        __slots__ = ("type", "body")

        def __init__(self, type, body):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.body))

        def __eq__(self, __other):
            return self.type == __other.type and self.body == __other.body

        def __ne__(self, __other):
            return self.type != __other.type or self.body != __other.body

        def __lt__(self, __other):
            return (self.type, self.body) < (__other.type, __other.body)

        def __le__(self, __other):
            return (self.type, self.body) <= (__other.type, __other.body)

        def __gt__(self, __other):
            return (self.type, self.body) > (__other.type, __other.body)

        def __ge__(self, __other):
            return (self.type, self.body) >= (__other.type, __other.body)

        def __repr__(self):
            return f"Update.EmbedExpr(type={self.type!r}, body={self.body!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RetrieveByKey:
        __match_args__ = ("template", "key")

        __slots__ = ("template", "key")

        def __init__(self, template, key):
            object.__setattr__(self, "template", template)
            object.__setattr__(self, "key", key)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.template, self.key))

        def __eq__(self, __other):
            return self.template == __other.template and self.key == __other.key

        def __ne__(self, __other):
            return self.template != __other.template or self.key != __other.key

        def __lt__(self, __other):
            return (self.template, self.key) < (__other.template, __other.key)

        def __le__(self, __other):
            return (self.template, self.key) <= (__other.template, __other.key)

        def __gt__(self, __other):
            return (self.template, self.key) > (__other.template, __other.key)

        def __ge__(self, __other):
            return (self.template, self.key) >= (__other.template, __other.key)

        def __repr__(self):
            return f"Update.RetrieveByKey(template={self.template!r}, key={self.key!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class TryCatch:
        __match_args__ = ("return_type", "try_expr", "var", "catch_expr")

        __slots__ = ("return_type", "try_expr", "var", "catch_expr")

        def __init__(self, return_type, try_expr, var, catch_expr):
            object.__setattr__(self, "return_type", return_type)
            object.__setattr__(self, "try_expr", try_expr)
            object.__setattr__(self, "var", var)
            object.__setattr__(self, "catch_expr", catch_expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.return_type, self.try_expr, self.var, self.catch_expr))

        def __eq__(self, __other):
            return (
                self.return_type == __other.return_type
                and self.try_expr == __other.try_expr
                and self.var == __other.var
                and self.catch_expr == __other.catch_expr
            )

        def __ne__(self, __other):
            return (
                self.return_type != __other.return_type
                or self.try_expr != __other.try_expr
                or self.var != __other.var
                or self.catch_expr != __other.catch_expr
            )

        def __lt__(self, __other):
            return (self.return_type, self.try_expr, self.var, self.catch_expr) < (
                __other.return_type,
                __other.try_expr,
                __other.var,
                __other.catch_expr,
            )

        def __le__(self, __other):
            return (self.return_type, self.try_expr, self.var, self.catch_expr) <= (
                __other.return_type,
                __other.try_expr,
                __other.var,
                __other.catch_expr,
            )

        def __gt__(self, __other):
            return (self.return_type, self.try_expr, self.var, self.catch_expr) > (
                __other.return_type,
                __other.try_expr,
                __other.var,
                __other.catch_expr,
            )

        def __ge__(self, __other):
            return (self.return_type, self.try_expr, self.var, self.catch_expr) >= (
                __other.return_type,
                __other.try_expr,
                __other.var,
                __other.catch_expr,
            )

        def __repr__(self):
            return f"Update.TryCatch(return_type={self.return_type!r}, try_expr={self.try_expr!r}, var={self.var!r}, catch_expr={self.catch_expr!r}, )"

    __match_args__ = ()

    __slots__ = ("Sum",)

    def __init__(
        self,
        *,
        pure=None,
        block=None,
        create=None,
        exercise=None,
        exercise_by_key=None,
        fetch=None,
        get_time=None,
        lookup_by_key=None,
        fetch_by_key=None,
        embed_expr=None,
        try_catch=None,
    ):
        Sum = []
        if pure is not None:
            object.__setattr__(self, "Sum", ("pure", pure))
            Sum.append("pure")
        if block is not None:
            object.__setattr__(self, "Sum", ("block", block))
            Sum.append("block")
        if create is not None:
            object.__setattr__(self, "Sum", ("create", create))
            Sum.append("create")
        if exercise is not None:
            object.__setattr__(self, "Sum", ("exercise", exercise))
            Sum.append("exercise")
        if exercise_by_key is not None:
            object.__setattr__(self, "Sum", ("exercise_by_key", exercise_by_key))
            Sum.append("exercise_by_key")
        if fetch is not None:
            object.__setattr__(self, "Sum", ("fetch", fetch))
            Sum.append("fetch")
        if get_time is not None:
            object.__setattr__(self, "Sum", ("get_time", get_time))
            Sum.append("get_time")
        if lookup_by_key is not None:
            object.__setattr__(self, "Sum", ("lookup_by_key", lookup_by_key))
            Sum.append("lookup_by_key")
        if fetch_by_key is not None:
            object.__setattr__(self, "Sum", ("fetch_by_key", fetch_by_key))
            Sum.append("fetch_by_key")
        if embed_expr is not None:
            object.__setattr__(self, "Sum", ("embed_expr", embed_expr))
            Sum.append("embed_expr")
        if try_catch is not None:
            object.__setattr__(self, "Sum", ("try_catch", try_catch))
            Sum.append("try_catch")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(
        self,
        pure,
        block,
        create,
        exercise,
        exercise_by_key,
        fetch,
        get_time,
        lookup_by_key,
        fetch_by_key,
        embed_expr,
        try_catch,
    ):
        if self.Sum[0] == "pure":
            return pure(self.Sum[1])
        elif self.Sum[0] == "block":
            return block(self.Sum[1])
        elif self.Sum[0] == "create":
            return create(self.Sum[1])
        elif self.Sum[0] == "exercise":
            return exercise(self.Sum[1])
        elif self.Sum[0] == "exercise_by_key":
            return exercise_by_key(self.Sum[1])
        elif self.Sum[0] == "fetch":
            return fetch(self.Sum[1])
        elif self.Sum[0] == "get_time":
            return get_time(self.Sum[1])
        elif self.Sum[0] == "lookup_by_key":
            return lookup_by_key(self.Sum[1])
        elif self.Sum[0] == "fetch_by_key":
            return fetch_by_key(self.Sum[1])
        elif self.Sum[0] == "embed_expr":
            return embed_expr(self.Sum[1])
        elif self.Sum[0] == "try_catch":
            return try_catch(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.Sum))

    def __eq__(self, __other):
        return self.Sum == __other.Sum

    def __ne__(self, __other):
        return self.Sum != __other.Sum

    def __lt__(self, __other):
        return (self.Sum) < (__other.Sum)

    def __le__(self, __other):
        return (self.Sum) <= (__other.Sum)

    def __gt__(self, __other):
        return (self.Sum) > (__other.Sum)

    def __ge__(self, __other):
        return (self.Sum) >= (__other.Sum)

    def __repr__(self):
        return f"Update({self.Sum[0]}={self.Sum[1]!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Scenario:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Commit:
        __match_args__ = ("party", "expr", "ret_type")

        __slots__ = ("party", "expr", "ret_type")

        def __init__(self, party, expr, ret_type):
            object.__setattr__(self, "party", party)
            object.__setattr__(self, "expr", expr)
            object.__setattr__(self, "ret_type", ret_type)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.party, self.expr, self.ret_type))

        def __eq__(self, __other):
            return (
                self.party == __other.party
                and self.expr == __other.expr
                and self.ret_type == __other.ret_type
            )

        def __ne__(self, __other):
            return (
                self.party != __other.party
                or self.expr != __other.expr
                or self.ret_type != __other.ret_type
            )

        def __lt__(self, __other):
            return (self.party, self.expr, self.ret_type) < (
                __other.party,
                __other.expr,
                __other.ret_type,
            )

        def __le__(self, __other):
            return (self.party, self.expr, self.ret_type) <= (
                __other.party,
                __other.expr,
                __other.ret_type,
            )

        def __gt__(self, __other):
            return (self.party, self.expr, self.ret_type) > (
                __other.party,
                __other.expr,
                __other.ret_type,
            )

        def __ge__(self, __other):
            return (self.party, self.expr, self.ret_type) >= (
                __other.party,
                __other.expr,
                __other.ret_type,
            )

        def __repr__(self):
            return f"Scenario.Commit(party={self.party!r}, expr={self.expr!r}, ret_type={self.ret_type!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EmbedExpr:
        __match_args__ = ("type", "body")

        __slots__ = ("type", "body")

        def __init__(self, type, body):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.body))

        def __eq__(self, __other):
            return self.type == __other.type and self.body == __other.body

        def __ne__(self, __other):
            return self.type != __other.type or self.body != __other.body

        def __lt__(self, __other):
            return (self.type, self.body) < (__other.type, __other.body)

        def __le__(self, __other):
            return (self.type, self.body) <= (__other.type, __other.body)

        def __gt__(self, __other):
            return (self.type, self.body) > (__other.type, __other.body)

        def __ge__(self, __other):
            return (self.type, self.body) >= (__other.type, __other.body)

        def __repr__(self):
            return f"Scenario.EmbedExpr(type={self.type!r}, body={self.body!r}, )"

    __match_args__ = ()

    __slots__ = ("Sum",)

    def __init__(
        self,
        *,
        pure=None,
        block=None,
        commit=None,
        must_fail_at=None,
        pass_=None,
        get_time=None,
        get_party=None,
        embed_expr=None,
    ):
        Sum = []
        if pure is not None:
            object.__setattr__(self, "Sum", ("pure", pure))
            Sum.append("pure")
        if block is not None:
            object.__setattr__(self, "Sum", ("block", block))
            Sum.append("block")
        if commit is not None:
            object.__setattr__(self, "Sum", ("commit", commit))
            Sum.append("commit")
        if must_fail_at is not None:
            object.__setattr__(self, "Sum", ("must_fail_at", must_fail_at))
            Sum.append("must_fail_at")
        if pass_ is not None:
            object.__setattr__(self, "Sum", ("pass_", pass_))
            Sum.append("pass_")
        if get_time is not None:
            object.__setattr__(self, "Sum", ("get_time", get_time))
            Sum.append("get_time")
        if get_party is not None:
            object.__setattr__(self, "Sum", ("get_party", get_party))
            Sum.append("get_party")
        if embed_expr is not None:
            object.__setattr__(self, "Sum", ("embed_expr", embed_expr))
            Sum.append("embed_expr")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(self, pure, block, commit, must_fail_at, pass_, get_time, get_party, embed_expr):
        if self.Sum[0] == "pure":
            return pure(self.Sum[1])
        elif self.Sum[0] == "block":
            return block(self.Sum[1])
        elif self.Sum[0] == "commit":
            return commit(self.Sum[1])
        elif self.Sum[0] == "mustFailAt":
            return must_fail_at(self.Sum[1])
        elif self.Sum[0] == "pass":
            return pass_(self.Sum[1])
        elif self.Sum[0] == "get_time":
            return get_time(self.Sum[1])
        elif self.Sum[0] == "get_party":
            return get_party(self.Sum[1])
        elif self.Sum[0] == "embed_expr":
            return embed_expr(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.Sum))

    def __eq__(self, __other):
        return self.Sum == __other.Sum

    def __ne__(self, __other):
        return self.Sum != __other.Sum

    def __lt__(self, __other):
        return (self.Sum) < (__other.Sum)

    def __le__(self, __other):
        return (self.Sum) <= (__other.Sum)

    def __gt__(self, __other):
        return (self.Sum) > (__other.Sum)

    def __ge__(self, __other):
        return (self.Sum) >= (__other.Sum)

    def __repr__(self):
        return f"Scenario({self.Sum[0]}={self.Sum[1]!r}, )"


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

    __slots__ = (
        "name",
        "consuming",
        "controllers",
        "observers",
        "arg_binder",
        "ret_type",
        "update",
        "self_binder",
        "location",
    )

    def __init__(
        self,
        name,
        consuming,
        controllers,
        arg_binder,
        ret_type,
        update,
        self_binder,
        observers=None,
        location=None,
    ):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "consuming", consuming)
        object.__setattr__(self, "controllers", controllers)
        object.__setattr__(self, "arg_binder", arg_binder)
        object.__setattr__(self, "ret_type", ret_type)
        object.__setattr__(self, "update", update)
        object.__setattr__(self, "self_binder", self_binder)
        object.__setattr__(self, "observers", observers)
        object.__setattr__(self, "location", location)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (
                self.name,
                self.consuming,
                self.controllers,
                self.observers,
                self.arg_binder,
                self.ret_type,
                self.update,
                self.self_binder,
                self.location,
            )
        )

    def __eq__(self, __other):
        return (
            self.name == __other.name
            and self.consuming == __other.consuming
            and self.controllers == __other.controllers
            and self.observers == __other.observers
            and self.arg_binder == __other.arg_binder
            and self.ret_type == __other.ret_type
            and self.update == __other.update
            and self.self_binder == __other.self_binder
            and self.location == __other.location
        )

    def __ne__(self, __other):
        return (
            self.name != __other.name
            or self.consuming != __other.consuming
            or self.controllers != __other.controllers
            or self.observers != __other.observers
            or self.arg_binder != __other.arg_binder
            or self.ret_type != __other.ret_type
            or self.update != __other.update
            or self.self_binder != __other.self_binder
            or self.location != __other.location
        )

    def __lt__(self, __other):
        return (
            self.name,
            self.consuming,
            self.controllers,
            self.observers,
            self.arg_binder,
            self.ret_type,
            self.update,
            self.self_binder,
            self.location,
        ) < (
            __other.name,
            __other.consuming,
            __other.controllers,
            __other.observers,
            __other.arg_binder,
            __other.ret_type,
            __other.update,
            __other.self_binder,
            __other.location,
        )

    def __le__(self, __other):
        return (
            self.name,
            self.consuming,
            self.controllers,
            self.observers,
            self.arg_binder,
            self.ret_type,
            self.update,
            self.self_binder,
            self.location,
        ) <= (
            __other.name,
            __other.consuming,
            __other.controllers,
            __other.observers,
            __other.arg_binder,
            __other.ret_type,
            __other.update,
            __other.self_binder,
            __other.location,
        )

    def __gt__(self, __other):
        return (
            self.name,
            self.consuming,
            self.controllers,
            self.observers,
            self.arg_binder,
            self.ret_type,
            self.update,
            self.self_binder,
            self.location,
        ) > (
            __other.name,
            __other.consuming,
            __other.controllers,
            __other.observers,
            __other.arg_binder,
            __other.ret_type,
            __other.update,
            __other.self_binder,
            __other.location,
        )

    def __ge__(self, __other):
        return (
            self.name,
            self.consuming,
            self.controllers,
            self.observers,
            self.arg_binder,
            self.ret_type,
            self.update,
            self.self_binder,
            self.location,
        ) >= (
            __other.name,
            __other.consuming,
            __other.controllers,
            __other.observers,
            __other.arg_binder,
            __other.ret_type,
            __other.update,
            __other.self_binder,
            __other.location,
        )

    def __repr__(self):
        return f"TemplateChoice(name={self.name!r}, consuming={self.consuming!r}, controllers={self.controllers!r}, observers={self.observers!r}, arg_binder={self.arg_binder!r}, ret_type={self.ret_type!r}, update={self.update!r}, self_binder={self.self_binder!r}, location={self.location!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class KeyExpr:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Projection:
        __match_args__ = ("tycon", "field")

        __slots__ = ("tycon", "field")

        def __init__(self, tycon, field):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "field", field)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.field))

        def __eq__(self, __other):
            return self.tycon == __other.tycon and self.field == __other.field

        def __ne__(self, __other):
            return self.tycon != __other.tycon or self.field != __other.field

        def __lt__(self, __other):
            return (self.tycon, self.field) < (__other.tycon, __other.field)

        def __le__(self, __other):
            return (self.tycon, self.field) <= (__other.tycon, __other.field)

        def __gt__(self, __other):
            return (self.tycon, self.field) > (__other.tycon, __other.field)

        def __ge__(self, __other):
            return (self.tycon, self.field) >= (__other.tycon, __other.field)

        def __repr__(self):
            return f"KeyExpr.Projection(tycon={self.tycon!r}, field={self.field!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Projections:
        __match_args__ = ("projections",)

        __slots__ = ("projections",)

        def __init__(self, projections):
            object.__setattr__(self, "projections", _builtins.tuple(projections))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.projections))

        def __eq__(self, __other):
            return self.projections == __other.projections

        def __ne__(self, __other):
            return self.projections != __other.projections

        def __lt__(self, __other):
            return (self.projections) < (__other.projections)

        def __le__(self, __other):
            return (self.projections) <= (__other.projections)

        def __gt__(self, __other):
            return (self.projections) > (__other.projections)

        def __ge__(self, __other):
            return (self.projections) >= (__other.projections)

        def __repr__(self):
            return f"KeyExpr.Projections(projections={self.projections!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class RecordField:
        __match_args__ = ("field", "expr")

        __slots__ = ("field", "expr")

        def __init__(self, field, expr):
            object.__setattr__(self, "field", field)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.field, self.expr))

        def __eq__(self, __other):
            return self.field == __other.field and self.expr == __other.expr

        def __ne__(self, __other):
            return self.field != __other.field or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.field, self.expr) < (__other.field, __other.expr)

        def __le__(self, __other):
            return (self.field, self.expr) <= (__other.field, __other.expr)

        def __gt__(self, __other):
            return (self.field, self.expr) > (__other.field, __other.expr)

        def __ge__(self, __other):
            return (self.field, self.expr) >= (__other.field, __other.expr)

        def __repr__(self):
            return f"KeyExpr.RecordField(field={self.field!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Record:
        __match_args__ = ("tycon", "fields")

        __slots__ = ("tycon", "fields")

        def __init__(self, tycon, fields):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "fields", _builtins.tuple(fields))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.tycon, self.fields))

        def __eq__(self, __other):
            return self.tycon == __other.tycon and self.fields == __other.fields

        def __ne__(self, __other):
            return self.tycon != __other.tycon or self.fields != __other.fields

        def __lt__(self, __other):
            return (self.tycon, self.fields) < (__other.tycon, __other.fields)

        def __le__(self, __other):
            return (self.tycon, self.fields) <= (__other.tycon, __other.fields)

        def __gt__(self, __other):
            return (self.tycon, self.fields) > (__other.tycon, __other.fields)

        def __ge__(self, __other):
            return (self.tycon, self.fields) >= (__other.tycon, __other.fields)

        def __repr__(self):
            return f"KeyExpr.Record(tycon={self.tycon!r}, fields={self.fields!r}, )"

    __match_args__ = ()

    __slots__ = ("Sum",)

    def __init__(self, *, projections=None, record=None):
        Sum = []
        if projections is not None:
            object.__setattr__(self, "Sum", ("projections", projections))
            Sum.append("projections")
        if record is not None:
            object.__setattr__(self, "Sum", ("record", record))
            Sum.append("record")
        if len(Sum) == 0:
            raise ValueError("one of must be specified")
        elif len(Sum) > 1:
            raise ValueError("cannot specify at the same time")

    def Sum_match(self, projections, record):
        if self.Sum[0] == "projections":
            return projections(self.Sum[1])
        elif self.Sum[0] == "record":
            return record(self.Sum[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.Sum[0] == name:
            return self.Sum[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.Sum))

    def __eq__(self, __other):
        return self.Sum == __other.Sum

    def __ne__(self, __other):
        return self.Sum != __other.Sum

    def __lt__(self, __other):
        return (self.Sum) < (__other.Sum)

    def __le__(self, __other):
        return (self.Sum) <= (__other.Sum)

    def __gt__(self, __other):
        return (self.Sum) > (__other.Sum)

    def __ge__(self, __other):
        return (self.Sum) >= (__other.Sum)

    def __repr__(self):
        return f"KeyExpr({self.Sum[0]}={self.Sum[1]!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefTemplate:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class DefKey:
        __match_args__ = ("type", "maintainers")

        __slots__ = ("type", "key_expr", "maintainers")

        def __init__(self, type, maintainers, *, key=None, complex_key=None):
            object.__setattr__(self, "type", type)
            object.__setattr__(self, "maintainers", maintainers)
            key_expr = []
            if key is not None:
                object.__setattr__(self, "key_expr", ("key", key))
                key_expr.append("key")
            if complex_key is not None:
                object.__setattr__(self, "key_expr", ("complex_key", complex_key))
                key_expr.append("complex_key")
            if len(key_expr) == 0:
                raise ValueError("one of must be specified")
            elif len(key_expr) > 1:
                raise ValueError("cannot specify at the same time")

        def key_expr_match(self, key, complex_key):
            if self.key_expr[0] == "key":
                return key(self.key_expr[1])
            elif self.key_expr[0] == "complex_key":
                return complex_key(self.key_expr[1])
            else:
                raise Exception("invalid case")

        def __getattr__(self, name):
            if self.key_expr[0] == name:
                return self.key_expr[1]
            raise AttributeError

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.type, self.key_expr, self.maintainers))

        def __eq__(self, __other):
            return (
                self.type == __other.type
                and self.key_expr == __other.key_expr
                and self.maintainers == __other.maintainers
            )

        def __ne__(self, __other):
            return (
                self.type != __other.type
                or self.key_expr != __other.key_expr
                or self.maintainers != __other.maintainers
            )

        def __lt__(self, __other):
            return (self.type, self.key_expr, self.maintainers) < (
                __other.type,
                __other.key_expr,
                __other.maintainers,
            )

        def __le__(self, __other):
            return (self.type, self.key_expr, self.maintainers) <= (
                __other.type,
                __other.key_expr,
                __other.maintainers,
            )

        def __gt__(self, __other):
            return (self.type, self.key_expr, self.maintainers) > (
                __other.type,
                __other.key_expr,
                __other.maintainers,
            )

        def __ge__(self, __other):
            return (self.type, self.key_expr, self.maintainers) >= (
                __other.type,
                __other.key_expr,
                __other.maintainers,
            )

        def __repr__(self):
            return f"DefTemplate.DefKey(type={self.type!r}, {self.key_expr[0]}={self.key_expr[1]!r}, maintainers={self.maintainers!r}, )"

    __match_args__ = (
        "tycon",
        "param",
        "precond",
        "signatories",
        "agreement",
        "choices",
        "observers",
    )

    __slots__ = (
        "tycon",
        "param",
        "precond",
        "signatories",
        "agreement",
        "choices",
        "observers",
        "location",
        "key",
    )

    def __init__(
        self,
        tycon,
        param,
        precond,
        signatories,
        agreement,
        choices,
        observers,
        location=None,
        key=None,
    ):
        object.__setattr__(self, "tycon", tycon)
        object.__setattr__(self, "param", param)
        object.__setattr__(self, "precond", precond)
        object.__setattr__(self, "signatories", signatories)
        object.__setattr__(self, "agreement", agreement)
        object.__setattr__(self, "choices", _builtins.tuple(choices))
        object.__setattr__(self, "observers", observers)
        object.__setattr__(self, "location", location)
        object.__setattr__(self, "key", key)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (
                self.tycon,
                self.param,
                self.precond,
                self.signatories,
                self.agreement,
                self.choices,
                self.observers,
                self.location,
                self.key,
            )
        )

    def __eq__(self, __other):
        return (
            self.tycon == __other.tycon
            and self.param == __other.param
            and self.precond == __other.precond
            and self.signatories == __other.signatories
            and self.agreement == __other.agreement
            and self.choices == __other.choices
            and self.observers == __other.observers
            and self.location == __other.location
            and self.key == __other.key
        )

    def __ne__(self, __other):
        return (
            self.tycon != __other.tycon
            or self.param != __other.param
            or self.precond != __other.precond
            or self.signatories != __other.signatories
            or self.agreement != __other.agreement
            or self.choices != __other.choices
            or self.observers != __other.observers
            or self.location != __other.location
            or self.key != __other.key
        )

    def __lt__(self, __other):
        return (
            self.tycon,
            self.param,
            self.precond,
            self.signatories,
            self.agreement,
            self.choices,
            self.observers,
            self.location,
            self.key,
        ) < (
            __other.tycon,
            __other.param,
            __other.precond,
            __other.signatories,
            __other.agreement,
            __other.choices,
            __other.observers,
            __other.location,
            __other.key,
        )

    def __le__(self, __other):
        return (
            self.tycon,
            self.param,
            self.precond,
            self.signatories,
            self.agreement,
            self.choices,
            self.observers,
            self.location,
            self.key,
        ) <= (
            __other.tycon,
            __other.param,
            __other.precond,
            __other.signatories,
            __other.agreement,
            __other.choices,
            __other.observers,
            __other.location,
            __other.key,
        )

    def __gt__(self, __other):
        return (
            self.tycon,
            self.param,
            self.precond,
            self.signatories,
            self.agreement,
            self.choices,
            self.observers,
            self.location,
            self.key,
        ) > (
            __other.tycon,
            __other.param,
            __other.precond,
            __other.signatories,
            __other.agreement,
            __other.choices,
            __other.observers,
            __other.location,
            __other.key,
        )

    def __ge__(self, __other):
        return (
            self.tycon,
            self.param,
            self.precond,
            self.signatories,
            self.agreement,
            self.choices,
            self.observers,
            self.location,
            self.key,
        ) >= (
            __other.tycon,
            __other.param,
            __other.precond,
            __other.signatories,
            __other.agreement,
            __other.choices,
            __other.observers,
            __other.location,
            __other.key,
        )

    def __repr__(self):
        return f"DefTemplate(tycon={self.tycon!r}, param={self.param!r}, precond={self.precond!r}, signatories={self.signatories!r}, agreement={self.agreement!r}, choices={self.choices!r}, observers={self.observers!r}, location={self.location!r}, key={self.key!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefException:
    __match_args__ = ("name", "message")

    __slots__ = ("name", "location", "message")

    def __init__(self, name, message, location=None):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "message", message)
        object.__setattr__(self, "location", location)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.name, self.location, self.message))

    def __eq__(self, __other):
        return (
            self.name == __other.name
            and self.location == __other.location
            and self.message == __other.message
        )

    def __ne__(self, __other):
        return (
            self.name != __other.name
            or self.location != __other.location
            or self.message != __other.message
        )

    def __lt__(self, __other):
        return (self.name, self.location, self.message) < (
            __other.name,
            __other.location,
            __other.message,
        )

    def __le__(self, __other):
        return (self.name, self.location, self.message) <= (
            __other.name,
            __other.location,
            __other.message,
        )

    def __gt__(self, __other):
        return (self.name, self.location, self.message) > (
            __other.name,
            __other.location,
            __other.message,
        )

    def __ge__(self, __other):
        return (self.name, self.location, self.message) >= (
            __other.name,
            __other.location,
            __other.message,
        )

    def __repr__(self):
        return f"DefException(name={self.name!r}, location={self.location!r}, message={self.message!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefDataType:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Fields:
        __match_args__ = ("fields",)

        __slots__ = ("fields",)

        def __init__(self, fields):
            object.__setattr__(self, "fields", _builtins.tuple(fields))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.fields))

        def __eq__(self, __other):
            return self.fields == __other.fields

        def __ne__(self, __other):
            return self.fields != __other.fields

        def __lt__(self, __other):
            return (self.fields) < (__other.fields)

        def __le__(self, __other):
            return (self.fields) <= (__other.fields)

        def __gt__(self, __other):
            return (self.fields) > (__other.fields)

        def __ge__(self, __other):
            return (self.fields) >= (__other.fields)

        def __repr__(self):
            return f"DefDataType.Fields(fields={self.fields!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class EnumConstructors:
        __match_args__ = ("constructors",)

        __slots__ = ("constructors",)

        def __init__(self, constructors):
            object.__setattr__(self, "constructors", _builtins.tuple(constructors))

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.constructors))

        def __eq__(self, __other):
            return self.constructors == __other.constructors

        def __ne__(self, __other):
            return self.constructors != __other.constructors

        def __lt__(self, __other):
            return (self.constructors) < (__other.constructors)

        def __le__(self, __other):
            return (self.constructors) <= (__other.constructors)

        def __gt__(self, __other):
            return (self.constructors) > (__other.constructors)

        def __ge__(self, __other):
            return (self.constructors) >= (__other.constructors)

        def __repr__(self):
            return f"DefDataType.EnumConstructors(constructors={self.constructors!r}, )"

    __match_args__ = ("params", "serializable")

    __slots__ = ("name", "params", "DataCons", "serializable", "location")

    def __init__(
        self,
        params,
        serializable,
        *,
        record=None,
        variant=None,
        enum=None,
        name=None,
        location=None,
    ):
        object.__setattr__(self, "params", _builtins.tuple(params))
        object.__setattr__(self, "serializable", serializable)
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "location", location)
        data_cons = []
        if record is not None:
            object.__setattr__(self, "DataCons", ("record", record))
            data_cons.append("record")
        if variant is not None:
            object.__setattr__(self, "DataCons", ("variant", variant))
            data_cons.append("variant")
        if enum is not None:
            object.__setattr__(self, "DataCons", ("enum", enum))
            data_cons.append("enum")
        if len(data_cons) == 0:
            raise ValueError("one of must be specified")
        elif len(data_cons) > 1:
            raise ValueError("cannot specify at the same time")

    def data_cons_match(self, record, variant, enum):
        if self.data_cons[0] == "record":
            return record(self.data_cons[1])
        elif self.data_cons[0] == "variant":
            return variant(self.data_cons[1])
        elif self.data_cons[0] == "enum":
            return enum(self.data_cons[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.DataCons[0] == name:
            return self.DataCons[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.name, self.params, self.data_cons, self.serializable, self.location))

    def __eq__(self, __other):
        return (
            self.name == __other.name
            and self.params == __other.params
            and self.data_cons == __other.data_cons
            and self.serializable == __other.serializable
            and self.location == __other.location
        )

    def __ne__(self, __other):
        return (
            self.name != __other.name
            or self.params != __other.params
            or self.data_cons != __other.data_cons
            or self.serializable != __other.serializable
            or self.location != __other.location
        )

    def __lt__(self, __other):
        return (self.name, self.params, self.data_cons, self.serializable, self.location,) < (
            __other.name,
            __other.params,
            __other.data_cons,
            __other.serializable,
            __other.location,
        )

    def __le__(self, __other):
        return (self.name, self.params, self.data_cons, self.serializable, self.location,) <= (
            __other.name,
            __other.params,
            __other.data_cons,
            __other.serializable,
            __other.location,
        )

    def __gt__(self, __other):
        return (self.name, self.params, self.data_cons, self.serializable, self.location,) > (
            __other.name,
            __other.params,
            __other.data_cons,
            __other.serializable,
            __other.location,
        )

    def __ge__(self, __other):
        return (self.name, self.params, self.data_cons, self.serializable, self.location,) >= (
            __other.name,
            __other.params,
            __other.data_cons,
            __other.serializable,
            __other.location,
        )

    def __repr__(self):
        return f"DefDataType(name={self.name!r}, params={self.params!r}, {self.DataCons[0]}={self.DataCons[1]!r}, serializable={self.serializable!r}, location={self.location!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefTypeSyn:
    __match_args__ = ("name", "params", "type")

    __slots__ = ("name", "params", "type", "location")

    def __init__(self, name, params, type, location=None):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "params", _builtins.tuple(params))
        object.__setattr__(self, "type", type)
        object.__setattr__(self, "location", location)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.name, self.params, self.type, self.location))

    def __eq__(self, __other):
        return (
            self.name == __other.name
            and self.params == __other.params
            and self.type == __other.type
            and self.location == __other.location
        )

    def __ne__(self, __other):
        return (
            self.name != __other.name
            or self.params != __other.params
            or self.type != __other.type
            or self.location != __other.location
        )

    def __lt__(self, __other):
        return (self.name, self.params, self.type, self.location) < (
            __other.name,
            __other.params,
            __other.type,
            __other.location,
        )

    def __le__(self, __other):
        return (self.name, self.params, self.type, self.location) <= (
            __other.name,
            __other.params,
            __other.type,
            __other.location,
        )

    def __gt__(self, __other):
        return (self.name, self.params, self.type, self.location) > (
            __other.name,
            __other.params,
            __other.type,
            __other.location,
        )

    def __ge__(self, __other):
        return (self.name, self.params, self.type, self.location) >= (
            __other.name,
            __other.params,
            __other.type,
            __other.location,
        )

    def __repr__(self):
        return f"DefTypeSyn(name={self.name!r}, params={self.params!r}, type={self.type!r}, location={self.location!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefValue:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class NameWithType:
        __match_args__ = ("name", "type")

        __slots__ = ("name", "type")

        def __init__(self, name, type):
            object.__setattr__(self, "name", name)
            object.__setattr__(self, "type", type)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.name, self.type))

        def __eq__(self, __other):
            return self.name == __other.name and self.type == __other.type

        def __ne__(self, __other):
            return self.name != __other.name or self.type != __other.type

        def __lt__(self, __other):
            return (self.name, self.type) < (__other.name, __other.type)

        def __le__(self, __other):
            return (self.name, self.type) <= (__other.name, __other.type)

        def __gt__(self, __other):
            return (self.name, self.type) > (__other.name, __other.type)

        def __ge__(self, __other):
            return (self.name, self.type) >= (__other.name, __other.type)

        def __repr__(self):
            return f"DefValue.NameWithType(name={self.name!r}, type={self.type!r}, )"

    __match_args__ = ("name_with_type", "expr", "no_party_literals", "is_test")

    __slots__ = ("name_with_type", "expr", "no_party_literals", "is_test", "location")

    def __init__(self, name_with_type, expr, no_party_literals, is_test, location=None):
        object.__setattr__(self, "name_with_type", name_with_type)
        object.__setattr__(self, "expr", expr)
        object.__setattr__(self, "no_party_literals", no_party_literals)
        object.__setattr__(self, "is_test", is_test)
        object.__setattr__(self, "location", location)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (
                self.name_with_type,
                self.expr,
                self.no_party_literals,
                self.is_test,
                self.location,
            )
        )

    def __eq__(self, __other):
        return (
            self.name_with_type == __other.name_with_type
            and self.expr == __other.expr
            and self.no_party_literals == __other.no_party_literals
            and self.is_test == __other.is_test
            and self.location == __other.location
        )

    def __ne__(self, __other):
        return (
            self.name_with_type != __other.name_with_type
            or self.expr != __other.expr
            or self.no_party_literals != __other.no_party_literals
            or self.is_test != __other.is_test
            or self.location != __other.location
        )

    def __lt__(self, __other):
        return (
            self.name_with_type,
            self.expr,
            self.no_party_literals,
            self.is_test,
            self.location,
        ) < (
            __other.name_with_type,
            __other.expr,
            __other.no_party_literals,
            __other.is_test,
            __other.location,
        )

    def __le__(self, __other):
        return (
            self.name_with_type,
            self.expr,
            self.no_party_literals,
            self.is_test,
            self.location,
        ) <= (
            __other.name_with_type,
            __other.expr,
            __other.no_party_literals,
            __other.is_test,
            __other.location,
        )

    def __gt__(self, __other):
        return (
            self.name_with_type,
            self.expr,
            self.no_party_literals,
            self.is_test,
            self.location,
        ) > (
            __other.name_with_type,
            __other.expr,
            __other.no_party_literals,
            __other.is_test,
            __other.location,
        )

    def __ge__(self, __other):
        return (
            self.name_with_type,
            self.expr,
            self.no_party_literals,
            self.is_test,
            self.location,
        ) >= (
            __other.name_with_type,
            __other.expr,
            __other.no_party_literals,
            __other.is_test,
            __other.location,
        )

    def __repr__(self):
        return f"DefValue(name_with_type={self.name_with_type!r}, expr={self.expr!r}, no_party_literals={self.no_party_literals!r}, is_test={self.is_test!r}, location={self.location!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class FeatureFlags:
    __match_args__ = (
        "forbid_party_literals",
        "dont_divulge_contract_ids_in_create_arguments",
        "dont_disclose_nonconsuming_choices_to_observers",
    )

    __slots__ = (
        "forbid_party_literals",
        "dont_divulge_contract_ids_in_create_arguments",
        "dont_disclose_nonconsuming_choices_to_observers",
    )

    def __init__(
        self,
        forbid_party_literals,
        dont_divulge_contract_ids_in_create_arguments,
        dont_disclose_nonconsuming_choices_to_observers,
    ):
        object.__setattr__(self, "forbid_party_literals", forbid_party_literals)
        object.__setattr__(
            self,
            "dont_divulge_contract_ids_in_create_arguments",
            dont_divulge_contract_ids_in_create_arguments,
        )
        object.__setattr__(
            self,
            "dont_disclose_nonconsuming_choices_to_observers",
            dont_disclose_nonconsuming_choices_to_observers,
        )

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (
                self.forbid_party_literals,
                self.dont_divulge_contract_ids_in_create_arguments,
                self.dont_disclose_nonconsuming_choices_to_observers,
            )
        )

    def __eq__(self, __other):
        return (
            self.forbid_party_literals == __other.forbid_party_literals
            and self.dont_divulge_contract_ids_in_create_arguments
            == __other.dont_divulge_contract_ids_in_create_arguments
            and self.dont_disclose_nonconsuming_choices_to_observers
            == __other.dont_disclose_nonconsuming_choices_to_observers
        )

    def __ne__(self, __other):
        return (
            self.forbid_party_literals != __other.forbid_party_literals
            or self.dont_divulge_contract_ids_in_create_arguments
            != __other.dont_divulge_contract_ids_in_create_arguments
            or self.dont_disclose_nonconsuming_choices_to_observers
            != __other.dont_disclose_nonconsuming_choices_to_observers
        )

    def __lt__(self, __other):
        return (
            self.forbid_party_literals,
            self.dont_divulge_contract_ids_in_create_arguments,
            self.dont_disclose_nonconsuming_choices_to_observers,
        ) < (
            __other.forbid_party_literals,
            __other.dont_divulge_contract_ids_in_create_arguments,
            __other.dont_disclose_nonconsuming_choices_to_observers,
        )

    def __le__(self, __other):
        return (
            self.forbid_party_literals,
            self.dont_divulge_contract_ids_in_create_arguments,
            self.dont_disclose_nonconsuming_choices_to_observers,
        ) <= (
            __other.forbid_party_literals,
            __other.dont_divulge_contract_ids_in_create_arguments,
            __other.dont_disclose_nonconsuming_choices_to_observers,
        )

    def __gt__(self, __other):
        return (
            self.forbid_party_literals,
            self.dont_divulge_contract_ids_in_create_arguments,
            self.dont_disclose_nonconsuming_choices_to_observers,
        ) > (
            __other.forbid_party_literals,
            __other.dont_divulge_contract_ids_in_create_arguments,
            __other.dont_disclose_nonconsuming_choices_to_observers,
        )

    def __ge__(self, __other):
        return (
            self.forbid_party_literals,
            self.dont_divulge_contract_ids_in_create_arguments,
            self.dont_disclose_nonconsuming_choices_to_observers,
        ) >= (
            __other.forbid_party_literals,
            __other.dont_divulge_contract_ids_in_create_arguments,
            __other.dont_disclose_nonconsuming_choices_to_observers,
        )

    def __repr__(self):
        return f"FeatureFlags(forbid_party_literals={self.forbid_party_literals!r}, dont_divulge_contract_ids_in_create_arguments={self.dont_divulge_contract_ids_in_create_arguments!r}, dont_disclose_nonconsuming_choices_to_observers={self.dont_disclose_nonconsuming_choices_to_observers!r}, )"


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
    )

    __slots__ = (
        "name",
        "flags",
        "synonyms",
        "data_types",
        "values",
        "templates",
        "exceptions",
    )

    def __init__(self, name, flags, synonyms, data_types, values, templates, exceptions):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "flags", flags)
        object.__setattr__(self, "synonyms", _builtins.tuple(synonyms))
        object.__setattr__(self, "data_types", _builtins.tuple(data_types))
        object.__setattr__(self, "values", _builtins.tuple(values))
        object.__setattr__(self, "templates", _builtins.tuple(templates))
        object.__setattr__(self, "exceptions", _builtins.tuple(exceptions))

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (
                self.name,
                self.flags,
                self.synonyms,
                self.data_types,
                self.values,
                self.templates,
                self.exceptions,
            )
        )

    def __eq__(self, __other):
        return (
            self.name == __other.name
            and self.flags == __other.flags
            and self.synonyms == __other.synonyms
            and self.data_types == __other.data_types
            and self.values == __other.values
            and self.templates == __other.templates
            and self.exceptions == __other.exceptions
        )

    def __ne__(self, __other):
        return (
            self.name != __other.name
            or self.flags != __other.flags
            or self.synonyms != __other.synonyms
            or self.data_types != __other.data_types
            or self.values != __other.values
            or self.templates != __other.templates
            or self.exceptions != __other.exceptions
        )

    def __lt__(self, __other):
        return (
            self.name,
            self.flags,
            self.synonyms,
            self.data_types,
            self.values,
            self.templates,
            self.exceptions,
        ) < (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
        )

    def __le__(self, __other):
        return (
            self.name,
            self.flags,
            self.synonyms,
            self.data_types,
            self.values,
            self.templates,
            self.exceptions,
        ) <= (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
        )

    def __gt__(self, __other):
        return (
            self.name,
            self.flags,
            self.synonyms,
            self.data_types,
            self.values,
            self.templates,
            self.exceptions,
        ) > (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
        )

    def __ge__(self, __other):
        return (
            self.name,
            self.flags,
            self.synonyms,
            self.data_types,
            self.values,
            self.templates,
            self.exceptions,
        ) >= (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
        )

    def __repr__(self):
        return f"Module(name={self.name!r}, flags={self.flags!r}, synonyms={self.synonyms!r}, data_types={self.data_types!r}, values={self.values!r}, templates={self.templates!r}, exceptions={self.exceptions!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class PackageMetadata:
    __match_args__ = ("name", "version")

    __slots__ = ("name", "version")

    def __init__(self, name, version):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "version", version)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.name, self.version))

    def __eq__(self, __other):
        return self.name == __other.name and self.version == __other.version

    def __ne__(self, __other):
        return self.name != __other.name or self.version != __other.version

    def __lt__(self, __other):
        return (self.name, self.version) < (__other.name, __other.version)

    def __le__(self, __other):
        return (self.name, self.version) <= (__other.name, __other.version)

    def __gt__(self, __other):
        return (self.name, self.version) > (__other.name, __other.version)

    def __ge__(self, __other):
        return (self.name, self.version) >= (__other.name, __other.version)

    def __repr__(self):
        return f"PackageMetadata(name={self.name!r}, version={self.version!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Package:
    __match_args__ = ("modules",)

    __slots__ = ("modules", "metadata")

    def __init__(self, modules, metadata=None):
        object.__setattr__(self, "modules", _builtins.tuple(modules))
        object.__setattr__(self, "metadata", metadata)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.modules, self.metadata))

    def __eq__(self, __other):
        return self.modules == __other.modules and self.metadata == __other.metadata

    def __ne__(self, __other):
        return self.modules != __other.modules or self.metadata != __other.metadata

    def __lt__(self, __other):
        return (self.modules, self.metadata) < (__other.modules, __other.metadata)

    def __le__(self, __other):
        return (self.modules, self.metadata) <= (__other.modules, __other.metadata)

    def __gt__(self, __other):
        return (self.modules, self.metadata) > (__other.modules, __other.metadata)

    def __ge__(self, __other):
        return (self.modules, self.metadata) >= (__other.modules, __other.metadata)

    def __repr__(self):
        return f"Package(modules={self.modules!r}, metadata={self.metadata!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class Archive:
    __match_args__ = ("hash", "package")

    __slots__ = ("hash", "package")

    def __init__(self, hash, package):
        object.__setattr__(self, "hash", hash)
        object.__setattr__(self, "package", package)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.hash, self.package))

    def __eq__(self, __other):
        return self.hash == __other.hash and self.package == __other.package

    def __ne__(self, __other):
        return self.hash != __other.hash or self.package != __other.package

    def __lt__(self, __other):
        return (self.hash, self.package) < (__other.hash, __other.package)

    def __le__(self, __other):
        return (self.hash, self.package) <= (__other.hash, __other.package)

    def __gt__(self, __other):
        return (self.hash, self.package) > (__other.hash, __other.package)

    def __ge__(self, __other):
        return (self.hash, self.package) >= (__other.hash, __other.package)

    def __repr__(self):
        return f"Archive(hash={self.hash!r}, package={self.package!r}, )"
