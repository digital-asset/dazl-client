# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
DAML-LF Archive types
---------------------
"""

# NOTE TO IMPLEMENTORS: A future version of this file is intended to be code-generated instead of
# manually maintained. The makeup of this file is intentionally highly formulaic in order to
# facilitate a smooth transition to automatically-generated data structures.
#
# On a similar note, it is important to be careful about imports in this file; it is simpler to
# validate an automatically generated file with no dependencies. Also, this file is imported in a
# lot of places in the dazl codebase, so imports in this file could frequently lead to import
# cycles.
#
# The few local imports in this file should be inlined by a codegen process instead to keep this
# file self-contained.

from dataclasses import dataclass
from enum import IntEnum as _IntEnum
from io import StringIO
import threading
from typing import Any, Callable, NewType, Optional, Sequence, Tuple, Union
import typing as _typing

from ._base import MISSING, T, _Missing

__all__ = [
    "Archive",
    "Binding",
    "Block",
    "BuiltinFunction",
    "Case",
    "CaseAlt",
    "DefDataType",
    "DefTemplate",
    "DefTypeSyn",
    "DefValue",
    "DottedName",
    "Expr",
    "FeatureFlags",
    "FieldWithExpr",
    "FieldWithType",
    "KeyExpr",
    "Kind",
    "Location",
    "Module",
    "ModuleRef",
    "Package",
    "PackageMetadata",
    "PackageRef",
    "PrimCon",
    "PrimLit",
    "PrimType",
    "Pure",
    "Scenario",
    "TemplateChoice",
    "Type",
    "TypeConName",
    "TypeSynName",
    "TypeVarWithKind",
    "UNIT",
    "Unit",
    "Update",
    "ValName",
    "VarWithType",
]

_T = _typing.TypeVar("_T")


class Unit:
    __slots__ = ()


UNIT = Unit()

# Reference to a package via a package identifier. The identifier is the ascii7
# lowercase hex-encoded hash of the package contents found in the DAML LF Archive.
PackageRef = NewType("PackageRef", str)


class DottedName:
    __slots__ = ("segments",)

    segments: Sequence[str]

    def __init__(self, segments: Sequence[str] = ()):
        object.__setattr__(self, "segments", tuple(segments))

    def __str__(self):
        return ".".join(self.segments)

    def __bool__(self):
        return bool(self.segments)

    def __eq__(self, other):
        return isinstance(other, DottedName) and self.segments == other.segments

    def __lt__(self, other):
        return self.segments < other.segments

    def __le__(self, other):
        return self.segments <= other.segments

    def __gt__(self, other):
        return self.segments > other.segments

    def __ge__(self, other):
        return self.segments >= other.segments

    def __hash__(self):
        return hash(self.segments)


class ModuleRef:
    """
    A reference to a module.

    In dazl v8.0.0, ModuleRef will become a `NewType(str)`, so making assumptions about the
    structure of this type should be avoided, and accessor methods should be instead used for
    callers that care about the structure of these names.
    """

    __slots__ = "_package_id", "_module_name"

    def __init__(self, package_id: "PackageRef", module_name: "DottedName"):
        from ..util.typing import safe_cast

        self._package_id = PackageRef(safe_cast(str, package_id))
        self._module_name = safe_cast(DottedName, module_name)

    def __eq__(self, other):
        return (
            isinstance(other, ModuleRef)
            and self._package_id == other._package_id
            and self._module_name == other._module_name
        )

    def __lt__(self, other):
        return self._package_id < other._package_id or (
            self._package_id == other._package_id and self._module_name < other._module_name
        )

    def __le__(self, other):
        return self._package_id < other._package_id or (
            self._package_id == other._package_id and self._module_name <= other._module_name
        )

    def __gt__(self, other):
        return self._package_id > other._package_id or (
            self._package_id == other._package_id and self._module_name > other._module_name
        )

    def __ge__(self, other):
        return self._package_id > other._package_id or (
            self._package_id == other._package_id and self._module_name >= other._module_name
        )

    def __hash__(self):
        return hash(self._package_id) ^ hash(self._module_name)

    def __str__(self):
        if self._module_name:
            return f"{self._package_id}:{self._module_name}"
        else:
            return self._package_id

    def __repr__(self):
        return f"ModuleRef(package_id={self._package_id!r}, " f"module_name={self._module_name})"


class _Name:
    """
    A reference by name to another object.

    This implementation powers all of a TypeConName, TypeSynName, and ValName.

    In dazl 7.0.0, these will become `NewType(str)`, so making assumptions about the structure of
    this type should be avoided, and accessor methods should be instead used for callers that care
    about the structure of these names.
    """

    __slots__ = "_module", "_name"

    def __init__(self, module: "ModuleRef", name: "Sequence[str]"):
        from collections.abc import Collection

        from ..util.typing import safe_cast

        if not isinstance(name, Collection):
            raise TypeError(f"Tuple of strings required here (got {name!r} instead)")

        self._module = safe_cast(ModuleRef, module)
        self._name = tuple(name)  # type: Tuple[str, ...]

    def __eq__(self, other):
        return (
            isinstance(other, type(self))
            and self._module == other._module
            and self._name == other._name
        )

    def __ne__(self, other):
        return (
            not isinstance(other, type(self))
            or self._module != other._module
            or self._name != other._name
        )

    def __lt__(self, other):
        if not isinstance(other, _Name):
            raise TypeError("must compare Name to other names")

        return self._module < other._module or (
            self._module == other._module and self._name < other._name
        )

    def __le__(self, other):
        if not isinstance(other, _Name):
            raise TypeError("must compare Name to other names")
        return self._module <= other._module or (
            self._module == other._module and self._name <= other._name
        )

    def __gt__(self, other):
        if not isinstance(other, _Name):
            raise TypeError("must compare Name to other names")
        return self._module > other._module or (
            self._module == other._module and self._name > other._name
        )

    def __ge__(self, other):
        if not isinstance(other, _Name):
            raise TypeError("must compare Name to other names")

        return self._module >= other._module or (
            self._module == other._module and self._name >= other._name
        )

    def __hash__(self):
        return hash(self._module) ^ hash(self._name)

    def __str__(self):
        return f"{self._module}:{'.'.join(self._name)}"

    def __repr__(self):
        return f"{type(self).__name__}({str(self)!r})"


class TypeConName(_Name):
    """
    A reference to a type constructor.
    """


class TypeSynName(_Name):
    """
    A reference to a type synonym.
    """


class ValName(_Name):
    """
    A reference to a value.
    """


@dataclass(frozen=True)
class FieldWithType:
    field: str
    type: "Type"


@dataclass(frozen=True)
class VarWithType:
    var: str
    type: "Type"


@dataclass(frozen=True)
class TypeVarWithKind:
    var: str
    kind: "Kind"

    def __str__(self):
        return f"{self.var} : {self.kind}"

    def __repr__(self):
        return f"TypeVarWithKind({self})"


@dataclass(frozen=True)
class FieldWithExpr:
    field: str
    expr: "Expr"

    def __repr__(self):
        return f"FieldWithExpr({self.field}={self.expr})"


@dataclass(frozen=True)
class Binding:
    binder: "VarWithType"
    bound: "Expr"


class Kind:
    __slots__ = "_Sum_name", "_Sum_value"
    _Sum_name: str
    _Sum_value: Any

    class Arrow:
        params: "Sequence[Kind]"
        result: "Kind"

        def __init__(self, params: "Sequence[Kind]", result: "Kind"):
            self.params = params
            self.result = result

    def __init__(
        self,
        star: "Union[Unit, _Missing]" = MISSING,
        arrow: "Union[Arrow, _Missing]" = MISSING,
        nat: "Union[Unit, _Missing]" = MISSING,
    ):
        if star is not MISSING:
            object.__setattr__(self, "_Sum_name", "star")
            object.__setattr__(self, "_Sum_value", star)
        elif arrow is not MISSING:
            object.__setattr__(self, "_Sum_name", "arrow")
            object.__setattr__(self, "_Sum_value", arrow)
        elif nat is not MISSING:
            object.__setattr__(self, "_Sum_name", "nat")
            object.__setattr__(self, "_Sum_value", nat)
        else:
            raise ValueError("at least one must be specified")

    @property
    def star(self) -> "Optional[Unit]":
        return self._Sum_value if self._Sum_name == "star" else None

    @property
    def arrow(self) -> "Optional[Arrow]":
        return self._Sum_value if self._Sum_name == "arrow" else None

    @property
    def nat(self) -> "Optional[Unit]":
        return self._Sum_value if self._Sum_name == "nat" else None

    def __repr__(self):
        if self._Sum_name == "star":
            return "*"
        else:
            arrow = self.arrow
            params = [repr(i) for i in (*arrow.params, arrow.result)]
            return " -> ".join((f"({i})" if " " in i else i for i in params))


class PrimType(_IntEnum):
    UNIT = 0
    BOOL = 1
    INT64 = 2
    DECIMAL = 3
    CHAR = 4
    TEXT = 5
    TIMESTAMP = 6
    RELTIME = 7
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


# noinspection PyShadowingBuiltins
class Type:
    @dataclass(frozen=True)
    class Var:
        var: "str"
        args: "Sequence[Type]"

    class Con:
        tycon: "TypeConName"
        args: "Sequence[Type]"

        def __init__(self, tycon: "TypeConName", args: "Sequence[Type]"):
            self.tycon = tycon
            self.args = tuple(args)

        def __repr__(self):
            return f"Type.Con(tycon={self.tycon}, args={self.args})"

    @dataclass(frozen=True)
    class Syn:
        tysyn: "TypeSynName"
        args: "Sequence[Type]"

    class Prim:
        prim: "PrimType"
        args: "Sequence[Type]"

        def __init__(self, prim: "PrimType", args: "Sequence[Type]"):
            self.prim = prim
            self.args = tuple(args)

        def __repr__(self):
            return f"Type.Prim(prim={self.prim!r}, args={self.args!r})"

    class Fun:
        params: "Sequence[Type]"
        result: "Type"

        def __init__(self, params: "Sequence[Type]", result: "Type"):
            self.params = params
            self.result = result

    class Forall:
        vars: "Sequence[TypeVarWithKind]"
        body: "Type"

        # noinspection PyShadowingBuiltins
        def __init__(self, vars: "Sequence[TypeVarWithKind]", body: "Type"):
            self.vars = vars
            self.body = body

    class Struct:
        fields: "Sequence[FieldWithType]"

        def __init__(self, fields: "Sequence[FieldWithType]"):
            self.fields = tuple(fields)

    __slots__ = "_Sum_name", "_Sum_value"
    _Sum_name: str
    _Sum_value: Any

    def __init__(
        self,
        var: "Union[Type.Var, _Missing]" = MISSING,
        con: "Union[Type.Con, _Missing]" = MISSING,
        prim: "Union[Type.Prim, _Missing]" = MISSING,
        forall: "Union[Type.Forall, _Missing]" = MISSING,
        struct: "Union[Type.Struct, _Missing]" = MISSING,
        nat: "Union[int, _Missing]" = MISSING,
        syn: "Union[Type.Syn, _Missing]" = MISSING,
    ):
        if var is not MISSING:
            object.__setattr__(self, "_Sum_name", "var")
            object.__setattr__(self, "_Sum_value", var)
        elif con is not MISSING:
            object.__setattr__(self, "_Sum_name", "con")
            object.__setattr__(self, "_Sum_value", con)
        elif prim is not MISSING:
            object.__setattr__(self, "_Sum_name", "prim")
            object.__setattr__(self, "_Sum_value", prim)
        elif forall is not MISSING:
            object.__setattr__(self, "_Sum_name", "forall")
            object.__setattr__(self, "_Sum_value", forall)
        elif struct is not MISSING:
            object.__setattr__(self, "_Sum_name", "struct")
            object.__setattr__(self, "_Sum_value", struct)
        elif nat is not MISSING:
            object.__setattr__(self, "_Sum_name", "nat")
            object.__setattr__(self, "_Sum_value", nat)
        elif syn is not MISSING:
            object.__setattr__(self, "_Sum_name", "syn")
            object.__setattr__(self, "_Sum_value", syn)
        else:
            raise ValueError("unknown sum type")

    @property
    def var(self) -> "Type.Var":
        return self._Sum_value if self._Sum_name == "var" else None

    @property
    def con(self) -> "Type.Con":
        return self._Sum_value if self._Sum_name == "con" else None

    @property
    def prim(self) -> "Type.Prim":
        return self._Sum_value if self._Sum_name == "prim" else None

    @property
    def forall(self) -> "Type.Forall":
        return self._Sum_value if self._Sum_name == "forall" else None

    @property
    def struct(self) -> "Type.Struct":
        return self._Sum_value if self._Sum_name == "struct" else None

    @property
    def nat(self) -> int:
        return self._Sum_value if self._Sum_name == "nat" else None

    @property
    def syn(self) -> "Type.Syn":
        return self._Sum_value if self._Sum_name == "syn" else None

    # noinspection PyPep8Naming
    def Sum_match(
        self,
        var: "Callable[[Type.Var], T]",
        con: "Callable[[Type.Con], T]",
        prim: "Callable[[Type.Prim], T]",
        forall: "Callable[[Type.Forall], T]",
        struct: "Callable[[Type.Struct], T]",
        nat: "Callable[[int], T]",
        syn: "Callable[[Type.Syn], T]",
    ) -> "T":
        if self._Sum_name == "var":
            return var(self._Sum_value)
        elif self._Sum_name == "con":
            return con(self._Sum_value)
        elif self._Sum_name == "prim":
            return prim(self._Sum_value)
        elif self._Sum_name == "forall":
            return forall(self._Sum_value)
        elif self._Sum_name == "struct":
            return struct(self._Sum_value)
        elif self._Sum_name == "nat":
            return nat(self._Sum_value)
        elif self._Sum_name == "syn":
            return syn(self._Sum_value)
        else:
            raise Exception(f"invalid _Sum_name value: {self._Sum_name}")

    def __setattr__(self, key, value):
        raise Exception("Type is a read-only object")

    def __str__(self):
        """
        Return a str representation of this :class:`Type`. This is intentionally made to look more
        similar to DAML syntax.
        """
        # This import is done inside the function instead of outside to avoid circular references
        from ..pretty import DAML_PRETTY_PRINTER

        return DAML_PRETTY_PRINTER.visit_type(self)

    def __repr__(self):
        """
        Return a str representation of this :class:`Type`. This is intentionally made to look more
        similar to DAML syntax.
        """
        # This import is done inside the function instead of outside to avoid circular references
        from ..pretty import DAML_PRETTY_PRINTER

        # If rendering the type fails, print _something_; crashing in a repr(...) could be quite
        # obnoxious for users of this library
        # noinspection PyBroadException
        try:
            return f"Type({DAML_PRETTY_PRINTER.visit_type(self)})"
        except:  # noqa
            return "Type(...)"


class PrimLit:
    __slots__ = "_Sum_name", "_Sum_value"
    _Sum_name: str
    _Sum_value: Any

    class RoundingMode(_IntEnum):
        UP = 0
        DOWN = 1
        CEILING = 2
        FLOOR = 3
        HALF_UP = 4
        HALF_DOWN = 5
        HALF_EVEN = 6
        UNNECESSARY = 7

    def __init__(
        self,
        int64: "Union[int, _Missing]" = MISSING,
        decimal: "Union[str, _Missing]" = MISSING,
        text: "Union[str, _Missing]" = MISSING,
        timestamp: "Union[float, _Missing]" = MISSING,
        party: "Union[str, _Missing]" = MISSING,
        date: "Union[int, _Missing]" = MISSING,
        numeric: "Union[str, _Missing]" = MISSING,
        rounding_mode: "Union[RoundingMode, _Missing]" = MISSING,
    ):
        if int64 is not MISSING:
            object.__setattr__(self, "_Sum_name", "int64")
            object.__setattr__(self, "_Sum_value", int64)
        elif decimal is not MISSING:
            object.__setattr__(self, "_Sum_name", "decimal")
            object.__setattr__(self, "_Sum_value", decimal)
        elif text is not MISSING:
            object.__setattr__(self, "_Sum_name", "text")
            object.__setattr__(self, "_Sum_value", text)
        elif timestamp is not MISSING:
            object.__setattr__(self, "_Sum_name", "timestamp")
            object.__setattr__(self, "_Sum_value", timestamp)
        elif party is not MISSING:
            object.__setattr__(self, "_Sum_name", "party")
            object.__setattr__(self, "_Sum_value", party)
        elif date is not MISSING:
            object.__setattr__(self, "_Sum_name", "date")
            object.__setattr__(self, "_Sum_value", date)
        elif numeric is not MISSING:
            object.__setattr__(self, "_Sum_name", "numeric")
            object.__setattr__(self, "_Sum_value", numeric)
        elif numeric is not MISSING:
            object.__setattr__(self, "_Sum_name", "rounding_mode")
            object.__setattr__(self, "_Sum_value", rounding_mode)

    @property
    def int64(self) -> "Optional[int]":
        return self._Sum_value if self._Sum_name == "int64" else None

    @property
    def decimal(self) -> "Optional[str]":
        """
        our decimal type would fit in an int128, but sadly Protobuf does not
        have one. so, string it is. note that we can't store the whole and
        decimal part in two numbers either, because 10^28 > 2^63.
        """
        return self._Sum_value if self._Sum_name == "decimal" else None

    @property
    def text(self) -> "Optional[str]":
        return self._Sum_value if self._Sum_name == "text" else None

    @property
    def timestamp(self) -> "Optional[float]":
        """
        microseconds since the UNIX epoch. can go backwards. fixed
        since the vast majority of values will be greater than
        2^28, since currently the number of microseconds since the
        epoch is greater than that. Range: 0001-01-01T00:00:00Z to
        9999-12-31T23:59:59.999999Z, so that we can convert to/from
        https://www.ietf.org/rfc/rfc3339.txt
        """
        return self._Sum_value if self._Sum_name == "timestamp" else None

    @property
    def party(self) -> "Optional[str]":
        return self._Sum_value if self._Sum_name == "party" else None

    @property
    def date(self) -> "Optional[int]":
        """
        days since the unix epoch. can go backwards. limited from
        0001-01-01 to 9999-12-31, also to be compatible with
        https://www.ietf.org/rfc/rfc3339.txt
        """
        return self._Sum_value if self._Sum_name == "date" else None

    @property
    def numeric(self) -> "Optional[str]":
        """
        Serialization of number with precision 38 and scale between 0 and 37

        Must be a string that matched
            `-?([0-1]\\d*|0)\\.(\\d*)

        The number of decimal digits indicate the scale of the number.
        """
        return self._Sum_value if self._Sum_name == "numeric" else None

    @property
    def rounding_mode(self) -> "Optional[RoundingMode]":
        """
        Rounding mode for arithmetic operation

        Available in versions >= 1.13
        """
        return self._Sum_value if self._Sum_name == "rounding_mode" else None


# noinspection PyShadowingBuiltins
class Location:
    class Range:
        __slots__ = ("start_line", "start_col", "end_line", "end_col")

        def __init__(
            self, start_line: int = 0, start_col: int = 0, end_line: int = 0, end_col: int = 0
        ):
            object.__setattr__(self, "start_line", start_line)
            object.__setattr__(self, "start_col", start_col)
            object.__setattr__(self, "end_line", end_line)
            object.__setattr__(self, "end_col", end_col)

        start_line: int
        start_col: int
        end_line: int
        end_col: int

    module: "ModuleRef"
    range: "Range"

    def __init__(
        self,
        module: "Union[ModuleRef, _Missing]" = MISSING,
        range: "Union[Range, _Missing]" = MISSING,
    ):
        object.__setattr__(self, "module", module)
        object.__setattr__(self, "range", range)


# noinspection PyShadowingBuiltins
class Expr:
    class RecCon:
        tycon: "Type.Con"
        fields: "Sequence[FieldWithExpr]"

        def __init__(self, tycon: "Type.Con", fields: "Sequence[FieldWithExpr]"):
            self.tycon = tycon
            self.fields = tuple(fields)

        def __repr__(self):
            return f"Expr.RecCon(tycon={self.tycon}, fields={self.fields})"

    @dataclass(frozen=True)
    class RecProj:
        tycon: "Type.Con"  # Always fully applied string
        field: str
        record: "Expr"

        def __repr__(self):
            with StringIO() as buf:
                buf.write("Expr.RecProj(")
                if self.tycon is not None:
                    buf.write("tycon=")
                    buf.write(repr(self.tycon))
                    buf.write(", ")
                buf.write("record=")
                buf.write(repr(self.record))
                buf.write(", field=")
                buf.write(repr(self.field))
                buf.write(")")
                return buf.getvalue()

    # Set `field` in `record` to `update`.
    @dataclass(frozen=True)
    class RecUpd:
        tycon: "Type.Con"
        field: str
        record: "Expr"
        update: "Expr"

    class VariantCon:
        tycon: "Type.Con"  # Always fully applied
        variant_con: str
        variant_arg: "Expr"

        def __init__(self, tycon: "Type.Con", variant_con: str, variant_arg: "Expr"):
            self.tycon = tycon
            self.variant_con = variant_con
            self.variant_arg = variant_arg

    @dataclass(frozen=True)
    class EnumCon:
        tycon: "TypeConName"  # Always fully applied
        enum_con: str

    @dataclass(frozen=True)
    class StructCon:
        fields: "Sequence[FieldWithExpr]"  # length > 0

    @dataclass(frozen=True)
    class StructProj:
        field: str
        struct: "Expr"

    # Set `field` in `tuple` to `update`.
    @dataclass(frozen=True)
    class StructUpd:
        field: str
        struct: "Expr"
        update: "Expr"

    @dataclass(frozen=True)
    class App:
        fun: "Expr"
        args: "Sequence[Expr]"  # length > 0

    class TyApp:
        expr: "Expr"
        types: "Sequence[Type]"  # length > 0

        def __init__(self, expr: "Expr", types: "Sequence[Type]"):
            from ..util.typing import safe_cast

            object.__setattr__(self, "expr", safe_cast(Expr, expr))
            object.__setattr__(self, "types", tuple(types))

        def __repr__(self):
            return f"Expr.TyApp(types={self.types}, expr={self.expr})"

    class Abs:
        param: "Sequence[VarWithType]"  # length > 0
        body: "Expr"

        def __init__(self, param: "Sequence[VarWithType]", body: "Expr"):
            from ..util.typing import safe_cast

            object.__setattr__(self, "param", param)
            object.__setattr__(self, "body", safe_cast(Expr, body))

        def __repr__(self):
            with StringIO() as buf:
                buf.write("Expr.Abs(𝜆 ")
                buf.write(" ".join(vwt.var for vwt in self.param))
                buf.write(" . ")
                buf.write(repr(self.body))
                buf.write(")")
                return buf.getvalue()

    @dataclass(frozen=True)
    class TyAbs:
        param: "Sequence[TypeVarWithKind]"
        body: "Expr"

    @dataclass(frozen=True)
    class Nil:
        type: "Type"

        __slots__ = ("type",)

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type"):
            object.__setattr__(self, "type", type)

        def __repr__(self):
            return "Nil()"

    @dataclass(frozen=True)
    class Cons:
        type: "Type"
        front: "Sequence[Expr]"  # length > 0
        tail: "Expr"

        def __repr__(self):
            with StringIO() as buf:
                buf.write("Expr.Cons(front=")
                buf.write(repr(list(self.front)))
                buf.write(", tail=")
                buf.write(repr(self.tail))
                buf.write(")")
                return buf.getvalue()

    # noinspection PyPep8Naming
    class OptionalNone:
        type: "Type"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type"):
            self.type = type

        def __repr__(self):
            return f"Expr.None(: {self.type})"

    class OptionalSome:
        type: "Type"
        body: "Expr"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type", body: "Expr"):
            self.type = type
            self.body = body

        def __repr__(self):
            return f"Expr.Some({self.body!r} : {self.type})"

    class ToAny:
        type: "Type"
        expr: "Expr"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type", expr: "Expr"):
            self.type = type
            self.expr = expr

    class FromAny:
        type: "Type"
        expr: "Expr"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type", expr: "Expr"):
            self.type = type
            self.expr = expr

    class ToAnyException:
        type: "Type"
        expr: "Expr"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type", expr: "Expr"):
            self.type = type
            self.expr = expr

    class FromAnyException:
        type: "Type"
        expr: "Expr"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type", expr: "Expr"):
            self.type = type
            self.expr = expr

    class ToTextTemplateId:
        type: "Type"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type"):
            self.type = type

    class Throw:
        return_type: "Type"
        exception_type: "Type"
        exception_expr: "Expr"

        def __init__(self, return_type: "Type", exception_type: "Type", exception_expr: "Expr"):
            self.return_type = return_type
            self.exception_type = exception_type
            self.exception_expr = exception_expr

    class ToInterface:
        interface_type: "TypeConName"
        template_type: "TypeConName"
        template_expr: "Expr"

        def __init__(
            self, interface_type: "TypeConName", template_type: "TypeConName", template_expr: "Expr"
        ):
            self.interface_type = interface_type
            self.template_type = template_type
            self.template_expr = template_expr

    class FromInterface:
        interface_type: "TypeConName"
        template_type: "TypeConName"
        interface_expr: "Expr"

        def __init__(
            self,
            interface_type: "TypeConName",
            template_type: "TypeConName",
            interface_expr: "Expr",
        ):
            self.interface_type = interface_type
            self.template_type = template_type
            self.interface_expr = interface_expr

    class CallInterface:
        interface_type: "TypeConName"
        method_name: str
        interface_expr: "Expr"

        def __init__(self, interface_type: "TypeConName", method_name: str, interface_expr: "Expr"):
            self.interface_type = interface_type
            self.method_name = method_name
            self.interface_expr = interface_expr

    class ViewInterface:
        interface: "TypeConName"
        expr: "Expr"

        def __init__(self, interface: "TypeConName", expr: "Expr"):
            self.interface = interface
            self.expr = expr

    class SignatoryInterface:
        interface: "TypeConName"
        expr: "Expr"

        def __init__(self, interface: "TypeConName", expr: "Expr"):
            self.interface = interface
            self.expr = expr

    class ObserverInterface:
        interface: "TypeConName"
        expr: "Expr"

        def __init__(self, interface: "TypeConName", expr: "Expr"):
            self.interface = interface
            self.expr = expr

    class UnsafeFromInterface:
        interface_type: "TypeConName"
        template_type: "TypeConName"
        contract_id_expr: "Expr"
        interface_expr: "Expr"

        def __init__(
            self,
            interface_type: "TypeConName",
            template_type: "TypeConName",
            contract_id_expr: "Expr",
            interface_expr: "Expr",
        ):
            self.interface_type = interface_type
            self.template_type = template_type
            self.contract_id_expr = contract_id_expr
            self.interface_expr = interface_expr

    class InterfaceTemplateTypeRep:
        interface: "TypeConName"
        expr: "Expr"

        def __init__(self, interface: "TypeConName", expr: "Expr"):
            self.interface = interface
            self.expr = expr

    class ToRequiredInterface:
        required_interface: "TypeConName"
        requiring_interface: "TypeConName"
        expr: "Expr"

        def __init__(
            self,
            required_interface: "TypeConName",
            requiring_interface: "TypeConName",
            expr: "Expr",
        ):
            self.required_interface = required_interface
            self.requiring_interface = requiring_interface
            self.expr = expr

    class FromRequiredInterface:
        required_interface: "TypeConName"
        requiring_interface: "TypeConName"
        expr: "Expr"

        def __init__(
            self,
            required_interface: "TypeConName",
            requiring_interface: "TypeConName",
            expr: "Expr",
        ):
            self.required_interface = required_interface
            self.requiring_interface = requiring_interface
            self.expr = expr

    class UnsafeFromRequiredInterface:
        required_interface: "TypeConName"
        requiring_interface: "TypeConName"
        contract_id_expr: "Expr"
        interface_expr: "Expr"

        def __init__(
            self,
            required_interface: "TypeConName",
            requiring_interface: "TypeConName",
            contract_id_expr: "Expr",
            interface_expr: "Expr",
        ):
            self.required_interface = required_interface
            self.requiring_interface = requiring_interface
            self.contract_id_expr = contract_id_expr
            self.interface_expr = interface_expr

    class Experimental:
        name: str
        type: "Type"

        # noinspection PyShadowingBuiltins
        def __init__(self, name: str, type: "Type"):
            self.name = name
            self.type = type

    __slots__ = "location", "_Sum_name", "_Sum_value"
    location: Location
    _Sum_name: str
    _Sum_value: Any

    def __init__(
        self,
        *,
        var: "Union[str, _Missing]" = MISSING,
        val: "Union[ValName, _Missing]" = MISSING,
        builtin: "Union[BuiltinFunction, _Missing]" = MISSING,
        prim_con: "Union[PrimCon, _Missing]" = MISSING,
        prim_lit: "Union[PrimLit, _Missing]" = MISSING,
        rec_con: "Union[RecCon, _Missing]" = MISSING,
        rec_proj: "Union[RecProj, _Missing]" = MISSING,
        rec_upd: "Union[RecUpd, _Missing]" = MISSING,
        variant_con: "Union[VariantCon, _Missing]" = MISSING,
        enum_con: "Union[EnumCon, _Missing]" = MISSING,
        struct_con: "Union[StructCon, _Missing]" = MISSING,
        struct_proj: "Union[StructProj, _Missing]" = MISSING,
        struct_upd: "Union[StructUpd, _Missing]" = MISSING,
        app: "Union[App, _Missing]" = MISSING,
        ty_app: "Union[TyApp, _Missing]" = MISSING,
        abs: "Union[Abs, _Missing]" = MISSING,
        ty_abs: "Union[TyAbs, _Missing]" = MISSING,
        case: "Union[Case, _Missing]" = MISSING,
        let: "Union[Block, _Missing]" = MISSING,
        nil: "Union[Nil, _Missing]" = MISSING,
        cons: "Union[Cons, _Missing]" = MISSING,
        update: "Union[Update, _Missing]" = MISSING,
        scenario: "Union[Scenario, _Missing]" = MISSING,
        optional_none: "Union[OptionalNone, _Missing]" = MISSING,
        optional_some: "Union[OptionalSome, _Missing]" = MISSING,
        to_any: "Union[ToAny, _Missing]" = MISSING,
        from_any: "Union[FromAny, _Missing]" = MISSING,
        type_rep: "Union[Type, _Missing]" = MISSING,
        to_any_exception: "Union[Expr.ToAnyException, _Missing]" = MISSING,
        from_any_exception: "Union[Expr.FromAnyException, _Missing]" = MISSING,
        throw: "Union[Expr.Throw, _Missing]" = MISSING,
        to_interface: "Union[Expr.ToInterface, _Missing]" = MISSING,
        from_interface: "Union[Expr.FromInterface, _Missing]" = MISSING,
        call_interface: "Union[Expr.CallInterface, _Missing]" = MISSING,
        signatory_interface: "Union[Expr.SignatoryInterface, _Missing]" = MISSING,
        observer_interface: "Union[Expr.ObserverInterface, _Missing]" = MISSING,
        view_interface: "Union[Expr.ViewInterface, _Missing]" = MISSING,
        unsafe_from_interface: "Union[Expr.UnsafeFromInterface, _Missing]" = MISSING,
        interface_template_type_rep: "Union[Expr.InterfaceTemplateTypeRep, _Missing]" = MISSING,
        to_required_interface: "Union[Expr.ToRequiredInterface, _Missing]" = MISSING,
        from_required_interface: "Union[Expr.FromRequiredInterface, _Missing]" = MISSING,
        unsafe_from_required_interface: "Union[Expr.UnsafeFromRequiredInterface, _Missing]" = MISSING,
        experimental: "Union[Expr.Experimental, _Missing]" = MISSING,
        location: "Optional[Location]" = None,
    ):
        object.__setattr__(self, "location", location)
        if var is not MISSING:
            object.__setattr__(self, "_Sum_name", "var")
            object.__setattr__(self, "_Sum_value", var)
        elif val is not MISSING:
            object.__setattr__(self, "_Sum_name", "val")
            object.__setattr__(self, "_Sum_value", val)
        elif builtin is not MISSING:
            object.__setattr__(self, "_Sum_name", "builtin")
            object.__setattr__(self, "_Sum_value", builtin)
        elif prim_con is not MISSING:
            object.__setattr__(self, "_Sum_name", "prim_con")
            object.__setattr__(self, "_Sum_value", prim_con)
        elif prim_lit is not MISSING:
            object.__setattr__(self, "_Sum_name", "prim_lit")
            object.__setattr__(self, "_Sum_value", prim_lit)
        elif rec_con is not MISSING:
            object.__setattr__(self, "_Sum_name", "rec_con")
            object.__setattr__(self, "_Sum_value", rec_con)
        elif rec_proj is not MISSING:
            object.__setattr__(self, "_Sum_name", "rec_proj")
            object.__setattr__(self, "_Sum_value", rec_proj)
        elif variant_con is not MISSING:
            object.__setattr__(self, "_Sum_name", "variant_con")
            object.__setattr__(self, "_Sum_value", variant_con)
        elif enum_con is not MISSING:
            object.__setattr__(self, "_Sum_name", "enum_con")
            object.__setattr__(self, "_Sum_value", enum_con)
        elif struct_con is not MISSING:
            object.__setattr__(self, "_Sum_name", "struct_con")
            object.__setattr__(self, "_Sum_value", struct_con)
        elif struct_proj is not MISSING:
            object.__setattr__(self, "_Sum_name", "struct_proj")
            object.__setattr__(self, "_Sum_value", struct_proj)
        elif app is not MISSING:
            object.__setattr__(self, "_Sum_name", "app")
            object.__setattr__(self, "_Sum_value", app)
        elif ty_app is not MISSING:
            object.__setattr__(self, "_Sum_name", "ty_app")
            object.__setattr__(self, "_Sum_value", ty_app)
        elif abs is not MISSING:
            object.__setattr__(self, "_Sum_name", "abs")
            object.__setattr__(self, "_Sum_value", abs)
        elif ty_abs is not MISSING:
            object.__setattr__(self, "_Sum_name", "ty_abs")
            object.__setattr__(self, "_Sum_value", ty_abs)
        elif case is not MISSING:
            object.__setattr__(self, "_Sum_name", "case")
            object.__setattr__(self, "_Sum_value", case)
        elif let is not MISSING:
            object.__setattr__(self, "_Sum_name", "let")
            object.__setattr__(self, "_Sum_value", let)
        elif nil is not MISSING:
            object.__setattr__(self, "_Sum_name", "nil")
            object.__setattr__(self, "_Sum_value", nil)
        elif cons is not MISSING:
            object.__setattr__(self, "_Sum_name", "cons")
            object.__setattr__(self, "_Sum_value", cons)
        elif update is not MISSING:
            object.__setattr__(self, "_Sum_name", "update")
            object.__setattr__(self, "_Sum_value", update)
        elif scenario is not MISSING:
            object.__setattr__(self, "_Sum_name", "scenario")
            object.__setattr__(self, "_Sum_value", scenario)
        elif rec_upd is not MISSING:
            object.__setattr__(self, "_Sum_name", "rec_upd")
            object.__setattr__(self, "_Sum_value", rec_upd)
        elif struct_upd is not MISSING:
            object.__setattr__(self, "_Sum_name", "struct_upd")
            object.__setattr__(self, "_Sum_value", struct_upd)
        elif optional_none is not MISSING:
            object.__setattr__(self, "_Sum_name", "optional_none")
            object.__setattr__(self, "_Sum_value", optional_none)
        elif optional_some is not MISSING:
            object.__setattr__(self, "_Sum_name", "optional_some")
            object.__setattr__(self, "_Sum_value", optional_some)
        elif to_any is not MISSING:
            object.__setattr__(self, "_Sum_name", "to_any")
            object.__setattr__(self, "_Sum_value", to_any)
        elif from_any is not MISSING:
            object.__setattr__(self, "_Sum_name", "from_any")
            object.__setattr__(self, "_Sum_value", from_any)
        elif type_rep is not MISSING:
            object.__setattr__(self, "_Sum_name", "type_rep")
            object.__setattr__(self, "_Sum_value", type_rep)
        elif to_any_exception is not MISSING:
            object.__setattr__(self, "_Sum_name", "to_any_exception")
            object.__setattr__(self, "_Sum_value", to_any_exception)
        elif from_any_exception is not MISSING:
            object.__setattr__(self, "_Sum_name", "from_any_exception")
            object.__setattr__(self, "_Sum_value", from_any_exception)
        elif throw is not MISSING:
            object.__setattr__(self, "_Sum_name", "throw")
            object.__setattr__(self, "_Sum_value", throw)
        elif to_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "to_interface")
            object.__setattr__(self, "_Sum_value", to_interface)
        elif from_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "from_interface")
            object.__setattr__(self, "_Sum_value", from_interface)
        elif call_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "call_interface")
            object.__setattr__(self, "_Sum_value", call_interface)
        elif signatory_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "signatory_interface")
            object.__setattr__(self, "_Sum_value", signatory_interface)
        elif observer_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "observer_interface")
            object.__setattr__(self, "_Sum_value", observer_interface)
        elif view_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "view_interface")
            object.__setattr__(self, "_Sum_value", view_interface)
        elif unsafe_from_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "unsafe_from_interface")
            object.__setattr__(self, "_Sum_value", unsafe_from_interface)
        elif interface_template_type_rep is not MISSING:
            object.__setattr__(self, "_Sum_name", "interface_template_type_rep")
            object.__setattr__(self, "_Sum_value", interface_template_type_rep)
        elif to_required_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "to_required_interface")
            object.__setattr__(self, "_Sum_value", to_required_interface)
        elif from_required_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "from_required_interface")
            object.__setattr__(self, "_Sum_value", from_required_interface)
        elif unsafe_from_required_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "unsafe_from_required_interface")
            object.__setattr__(self, "_Sum_value", unsafe_from_required_interface)
        elif experimental is not MISSING:
            object.__setattr__(self, "_Sum_name", "experimental")
            object.__setattr__(self, "_Sum_value", experimental)
        else:
            raise ValueError(f"At least one valid Sum value must be supplied!")

    def __setattr__(self, key, value):
        raise Exception("Expr is read-only")

    @property
    def var(self) -> "Optional[str]":
        return self._Sum_value if self._Sum_name == "var" else None

    @property
    def val(self) -> "Optional[ValName]":
        return self._Sum_value if self._Sum_name == "val" else None

    @property
    def builtin(self) -> "Optional[BuiltinFunction]":
        return self._Sum_value if self._Sum_name == "builtin" else None

    @property
    def prim_con(self) -> "Optional[PrimCon]":
        return self._Sum_value if self._Sum_name == "prim_con" else None

    @property
    def prim_lit(self) -> "Optional[PrimLit]":
        return self._Sum_value if self._Sum_name == "prim_lit" else None

    @property
    def rec_con(self) -> "Optional[Expr.RecCon]":
        return self._Sum_value if self._Sum_name == "rec_con" else None

    @property
    def rec_proj(self) -> "Optional[RecProj]":
        return self._Sum_value if self._Sum_name == "rec_proj" else None

    @property
    def variant_con(self) -> "Optional[VariantCon]":
        return self._Sum_value if self._Sum_name == "variant_con" else None

    @property
    def enum_con(self) -> "Optional[EnumCon]":
        return self._Sum_value if self._Sum_name == "enum_con" else None

    @property
    def struct_con(self) -> "Optional[StructCon]":
        return self._Sum_value if self._Sum_name == "struct_con" else None

    @property
    def struct_proj(self) -> "Optional[StructProj]":
        return self._Sum_value if self._Sum_name == "struct_proj" else None

    @property
    def app(self) -> "Optional[App]":
        return self._Sum_value if self._Sum_name == "app" else None

    @property
    def ty_app(self) -> "Optional[Expr.TyApp]":
        return self._Sum_value if self._Sum_name == "ty_app" else None

    @property
    def abs(self) -> "Optional[Expr.Abs]":
        return self._Sum_value if self._Sum_name == "abs" else None

    @property
    def ty_abs(self) -> "Optional[Expr.TyAbs]":
        return self._Sum_value if self._Sum_name == "ty_abs" else None

    @property
    def case(self) -> "Optional[Case]":
        return self._Sum_value if self._Sum_name == "case" else None

    @property
    def let(self) -> "Optional[Block]":
        return self._Sum_value if self._Sum_name == "let" else None

    @property
    def nil(self) -> "Optional[Expr.Nil]":
        return self._Sum_value if self._Sum_name == "nil" else None

    @property
    def cons(self) -> "Optional[Expr.Cons]":
        return self._Sum_value if self._Sum_name == "cons" else None

    @property
    def update(self) -> "Optional[Update]":
        return self._Sum_value if self._Sum_name == "update" else None

    @property
    def scenario(self) -> "Optional[Scenario]":
        return self._Sum_value if self._Sum_name == "scenario" else None

    @property
    def rec_upd(self) -> "Optional[RecUpd]":
        return self._Sum_value if self._Sum_name == "rec_upd" else None

    @property
    def struct_upd(self) -> "Optional[StructUpd]":
        return self._Sum_value if self._Sum_name == "struct_upd" else None

    @property
    def optional_none(self) -> "Optional[OptionalNone]":
        return self._Sum_value if self._Sum_name == "optional_none" else None

    @property
    def optional_some(self) -> "Optional[OptionalSome]":
        return self._Sum_value if self._Sum_name == "optional_some" else None

    @property
    def to_any(self) -> "Optional[ToAny]":
        return self._Sum_value if self._Sum_name == "to_any" else None

    @property
    def from_any(self) -> "Optional[FromAny]":
        return self._Sum_value if self._Sum_name == "from_any" else None

    @property
    def to_text_template_id(self) -> "Optional[ToTextTemplateId]":
        return self._Sum_value if self._Sum_name == "to_text_template_id" else None

    @property
    def type_rep(self) -> "Optional[Type]":
        return self._Sum_value if self._Sum_name == "type_rep" else None

    @property
    def throw(self) -> "Optional[Throw]":
        return self._Sum_value if self._Sum_name == "throw" else None

    @property
    def to_interface(self) -> "Optional[ToInterface]":
        return self._Sum_value if self._Sum_name == "to_interface" else None

    @property
    def from_interface(self) -> "Optional[FromInterface]":
        return self._Sum_value if self._Sum_name == "from_interface" else None

    @property
    def call_interface(self) -> "Optional[CallInterface]":
        return self._Sum_value if self._Sum_name == "call_interface" else None

    @property
    def signatory_interface(self) -> "Optional[SignatoryInterface]":
        return self._Sum_value if self._Sum_name == "signatory_interface" else None

    @property
    def observer_interface(self) -> "Optional[ObserverInterface]":
        return self._Sum_value if self._Sum_name == "observer_interface" else None

    @property
    def view_interface(self) -> "Optional[ViewInterface]":
        return self._Sum_value if self._Sum_name == "view_interface" else None

    @property
    def unsafe_from_interface(self) -> "Optional[UnsafeFromInterface]":
        return self._Sum_value if self._Sum_name == "unsafe_from_interface" else None

    @property
    def interface_template_type_rep(self) -> "Optional[InterfaceTemplateTypeRep]":
        return self._Sum_value if self._Sum_name == "interface_template_type_rep" else None

    @property
    def to_required_interface(self) -> "Optional[ToRequiredInterface]":
        return self._Sum_value if self._Sum_name == "to_required_interface" else None

    @property
    def from_required_interface(self) -> "Optional[FromRequiredInterface]":
        return self._Sum_value if self._Sum_name == "from_required_interface" else None

    @property
    def unsafe_from_required_interface(self) -> "Optional[UnsafeFromRequiredInterface]":
        return self._Sum_value if self._Sum_name == "unsafe_from_required_interface" else None

    @property
    def experimental(self) -> "Optional[Experimental]":
        return self._Sum_value if self._Sum_name == "experimental" else None

    # noinspection PyPep8Naming
    def Sum_match(
        self,
        var: "_typing.Callable[[str], _T]",
        val: "_typing.Callable[[ValName], _T]",
        builtin: "_typing.Callable[[BuiltinFunction], _T]",
        prim_con: "_typing.Callable[[PrimCon], _T]",
        prim_lit: "_typing.Callable[[PrimLit], _T]",
        rec_con: "_typing.Callable[[Expr.RecCon], _T]",
        rec_proj: "_typing.Callable[[Expr.RecProj], _T]",
        rec_upd: "_typing.Callable[[Expr.RecUpd], _T]",
        variant_con: "_typing.Callable[[Expr.VariantCon], _T]",
        enum_con: "_typing.Callable[[Expr.EnumCon], _T]",
        struct_con: "_typing.Callable[[Expr.StructCon], _T]",
        struct_proj: "_typing.Callable[[Expr.StructProj], _T]",
        struct_upd: "_typing.Callable[[Expr.StructUpd], _T]",
        app: "_typing.Callable[[Expr.App], _T]",
        ty_app: "_typing.Callable[[Expr.TyApp], _T]",
        abs: "_typing.Callable[[Expr.Abs], _T]",
        ty_abs: "_typing.Callable[[Expr.TyAbs], _T]",
        case: "_typing.Callable[[Case], _T]",
        let: "_typing.Callable[[Block], _T]",
        nil: "_typing.Callable[[Expr.Nil], _T]",
        cons: "_typing.Callable[[Expr.Cons], _T]",
        update: "_typing.Callable[[Update], _T]",
        scenario: "_typing.Callable[[Scenario], _T]",
        optional_none: "_typing.Callable[[Expr.OptionalNone], _T]",
        optional_some: "_typing.Callable[[Expr.OptionalSome], _T]",
        to_any: "_typing.Callable[[Expr.ToAny], _T]",
        from_any: "_typing.Callable[[Expr.FromAny], _T]",
        type_rep: "_typing.Callable[[Type], _T]",
        to_any_exception: "_typing.Callable[[Expr.ToAnyException], _T]",
        from_any_exception: "_typing.Callable[[Expr.FromAnyException], _T]",
        throw: "_typing.Callable[[Expr.Throw], _T]",
        to_interface: "_typing.Callable[[ToInterface], _T]",
        from_interface: "_typing.Callable[[FromInterface], _T]",
        call_interface: "_typing.Callable[[CallInterface], _T]",
        signatory_interface: "_typing.Callable[[SignatoryInterface], _T]",
        observer_interface: "_typing.Callable[[ObserverInterface], _T]",
        view_interface: "_typing.Callable[[ViewInterface], _T]",
        unsafe_from_interface: "_typing.Callable[[UnsafeFromInterface], _T]",
        interface_template_type_rep: "_typing.Callable[[InterfaceTemplateTypeRep], _T]",
        to_required_interface: "_typing.Callable[[ToRequiredInterface], _T]",
        from_required_interface: "_typing.Callable[[FromRequiredInterface], _T]",
        unsafe_from_required_interface: "_typing.Callable[[UnsafeFromRequiredInterface], _T]",
        experimental: "_typing.Callable[[Expr.Experimental], _T]",
    ) -> "T":
        if self._Sum_name == "var":
            return var(self.var)  # type: ignore
        elif self._Sum_name == "val":
            return val(self.val)  # type: ignore
        elif self._Sum_name == "builtin":
            return builtin(self.builtin)  # type: ignore
        elif self._Sum_name == "prim_con":
            return prim_con(self.prim_con)  # type: ignore
        elif self._Sum_name == "prim_lit":
            return prim_lit(self.prim_lit)  # type: ignore
        elif self._Sum_name == "rec_con":
            return rec_con(self.rec_con)  # type: ignore
        elif self._Sum_name == "rec_proj":
            return rec_proj(self.rec_proj)  # type: ignore
        elif self._Sum_name == "variant_con":
            return variant_con(self.variant_con)  # type: ignore
        elif self._Sum_name == "enum_con":
            return enum_con(self.enum_con)  # type: ignore
        elif self._Sum_name == "struct_con":
            return struct_con(self.struct_con)  # type: ignore
        elif self._Sum_name == "struct_proj":
            return struct_proj(self.struct_proj)  # type: ignore
        elif self._Sum_name == "app":
            return app(self.app)  # type: ignore
        elif self._Sum_name == "ty_app":
            return ty_app(self.ty_app)  # type: ignore
        elif self._Sum_name == "abs":
            return abs(self.abs)  # type: ignore
        elif self._Sum_name == "ty_abs":
            return ty_abs(self.ty_abs)  # type: ignore
        elif self._Sum_name == "case":
            return case(self.case)  # type: ignore
        elif self._Sum_name == "let":
            return let(self.let)  # type: ignore
        elif self._Sum_name == "nil":
            return nil(self.nil)  # type: ignore
        elif self._Sum_name == "cons":
            return cons(self.cons)  # type: ignore
        elif self._Sum_name == "update":
            return update(self.update)  # type: ignore
        elif self._Sum_name == "scenario":
            return scenario(self.scenario)  # type: ignore
        elif self._Sum_name == "rec_upd":
            return rec_upd(self.rec_upd)  # type: ignore
        elif self._Sum_name == "struct_upd":
            return struct_upd(self.struct_upd)  # type: ignore
        elif self._Sum_name == "optional_none":
            return optional_none(self.optional_none)  # type: ignore
        elif self._Sum_name == "optional_some":
            return optional_some(self.optional_some)  # type: ignore
        elif self._Sum_name == "to_any":
            return to_any(self.to_any)  # type: ignore
        elif self._Sum_name == "from_any":
            return from_any(self.from_any)  # type: ignore
        elif self._Sum_name == "to_any_exception":
            return to_any_exception(self.to_any_exception)  # type: ignore
        elif self._Sum_name == "from_any_exception":
            return from_any_exception(self.from_any_exception)  # type: ignore
        elif self._Sum_name == "to_text_template_id":
            return to_text_template_id(self.to_text_template_id)  # type: ignore
        elif self._Sum_name == "type_rep":
            return type_rep(self.type_rep)  # type: ignore
        elif self._Sum_name == "throw":
            return throw(self.throw)  # type: ignore
        elif self._Sum_name == "to_interface":
            return to_interface(self.to_interface)  # type: ignore
        elif self._Sum_name == "from_interface":
            return from_interface(self.from_interface)  # type: ignore
        elif self._Sum_name == "call_interface":
            return call_interface(self.call_interface)  # type: ignore
        elif self._Sum_name == "signatory_interface":
            return signatory_interface(self.signatory_interface)  # type: ignore
        elif self._Sum_name == "observer_interface":
            return observer_interface(self.observer_interface)  # type: ignore
        elif self._Sum_name == "view_interface":
            return view_interface(self.view_interface)  # type: ignore
        elif self._Sum_name == "unsafe_from_interface":
            return unsafe_from_interface(self.unsafe_from_interface)  # type: ignore
        elif self._Sum_name == "interface_template_type_rep":
            return interface_template_type_rep(self.interface_template_type_rep)  # type: ignore
        elif self._Sum_name == "to_required_interface":
            return to_required_interface(self.to_required_interface)  # type: ignore
        elif self._Sum_name == "from_required_interface":
            return from_required_interface(self.from_required_interface)  # type: ignore
        elif self._Sum_name == "unsafe_from_required_interface":
            return unsafe_from_required_interface(self.unsafe_from_required_interface)  # type: ignore
        elif self._Sum_name == "experimental":
            return experimental(self.experimental)  # type: ignore
        else:
            raise Exception

    def __repr__(self):
        return f"Expr({self._Sum_name}={self._Sum_value!r})"


class CaseAlt:
    class Variant:
        con: "TypeConName"
        variant: str
        binder: str

        def __init__(self, con, variant, binder):
            self.con = con
            self.variant = variant
            self.binder = binder

    @dataclass(frozen=True)
    class Enum:
        con: TypeConName
        constructor: str

    @dataclass(frozen=True)
    class Cons:
        var_head: str
        var_tail: str

    @dataclass(frozen=True)
    class OptionalSome:
        var_body: str

    __slots__ = "body", "_Sum_name", "_Sum_value"
    body: "Expr"
    _Sum_name: str
    _Sum_value: Any

    def __init__(
        self,
        default: "Union[Unit, _Missing]" = MISSING,
        variant: "Union[Variant, _Missing]" = MISSING,
        prim_con: "Union[PrimCon, _Missing]" = MISSING,
        nil: "Union[Unit, _Missing]" = MISSING,
        cons: "Union[Cons, _Missing]" = MISSING,
        optional_none: "Union[Unit, _Missing]" = MISSING,
        optional_some: "Union[OptionalSome, _Missing]" = MISSING,
        body: "Union[Expr, _Missing]" = MISSING,
        enum: "Union[Enum, _Missing]" = MISSING,
    ):
        object.__setattr__(self, "body", body)
        if default is not MISSING:
            object.__setattr__(self, "_Sum_name", "default")
            object.__setattr__(self, "_Sum_value", default)
        elif variant is not MISSING:
            object.__setattr__(self, "_Sum_name", "variant")
            object.__setattr__(self, "_Sum_value", variant)
        elif prim_con is not MISSING:
            object.__setattr__(self, "_Sum_name", "prim_con")
            object.__setattr__(self, "_Sum_value", prim_con)
        elif nil is not MISSING:
            object.__setattr__(self, "_Sum_name", "nil")
            object.__setattr__(self, "_Sum_value", nil)
        elif cons is not MISSING:
            object.__setattr__(self, "_Sum_name", "cons")
            object.__setattr__(self, "_Sum_value", cons)
        elif optional_none is not MISSING:
            object.__setattr__(self, "_Sum_name", "optional_none")
            object.__setattr__(self, "_Sum_value", optional_none)
        elif optional_some is not MISSING:
            object.__setattr__(self, "_Sum_name", "optional_some")
            object.__setattr__(self, "_Sum_value", optional_some)
        elif enum is not MISSING:
            object.__setattr__(self, "_Sum_name", "enum")
            object.__setattr__(self, "_Sum_value", enum)

    @property
    def default(self) -> "Optional[Unit]":
        return self._Sum_value if self._Sum_name == "default" else None

    @property
    def variant(self) -> "Optional[Variant]":
        return self._Sum_value if self._Sum_name == "variant" else None

    @property
    def prim_con(self) -> "Optional[PrimCon]":
        return self._Sum_value if self._Sum_name == "prim_con" else None

    @property
    def nil(self) -> "Optional[Unit]":
        return self._Sum_value if self._Sum_name == "nil" else None

    @property
    def cons(self) -> "Optional[Cons]":
        return self._Sum_value if self._Sum_name == "cons" else None

    @property
    def optional_none(self) -> "Optional[Unit]":
        return self._Sum_value if self._Sum_name == "optional_none" else None

    @property
    def optional_some(self) -> "Optional[OptionalSome]":
        return self._Sum_value if self._Sum_name == "optional_some" else None

    @property
    def enum(self) -> "Optional[Enum]":
        return self._Sum_value if self._Sum_name == "enum" else None

    # noinspection PyPep8Naming
    def Sum_match(
        self,
        default: "Callable[[Unit], T]",
        variant: "Callable[[Variant], T]",
        prim_con: "Callable[[PrimCon], T]",
        nil: "Callable[[Unit], T]",
        cons: "Callable[[Cons], T]",
        optional_none: "Callable[[Unit], T]",
        optional_some: "Callable[[OptionalSome], T]",
        enum: "Callable[[Enum], T]",
    ):
        if self._Sum_name == "default":
            return default(self.default)  # type: ignore
        elif self._Sum_name == "variant":
            return variant(self.variant)  # type: ignore
        elif self._Sum_name == "prim_con":
            return prim_con(self.prim_con)  # type: ignore
        elif self._Sum_name == "nil":
            return nil(self.nil)  # type: ignore
        elif self._Sum_name == "cons":
            return cons(self.cons)  # type: ignore
        elif self._Sum_name == "optional_none":
            return optional_none(self.optional_none)  # type: ignore
        elif self._Sum_name == "optional_some":
            return optional_some(self.optional_some)  # type: ignore
        elif self._Sum_name == "enum":
            return enum(self.enum)  # type: ignore
        else:
            raise Exception


@dataclass(frozen=True)
class Case:
    # noinspection SpellCheckingInspection
    scrut: "Expr"
    alts: "Sequence[CaseAlt]"  # length > 0


@dataclass(frozen=True)
class Block:
    # A block of bindings and an expression.
    # Encodes a sequence of binds in e.g. a let or update block.
    bindings: "Sequence[Binding]"  # length > 0
    body: "Expr"


@dataclass(frozen=True)
class Pure:
    type: "Type"
    expr: "Expr"


class Update:
    class Create:
        template: "TypeConName"
        expr: "Expr"

        def __init__(self, template: "TypeConName", expr: "Expr"):
            self.template = template
            self.expr = expr

    class Exercise:
        template: "TypeConName"
        choice: str
        cid: "Expr"
        arg: "Expr"

        def __init__(self, template: "TypeConName", choice: str, cid: "Expr", arg: "Expr"):
            self.template = template
            self.choice = choice
            self.cid = cid
            self.arg = arg

    class ExerciseByKey:
        template: "TypeConName"
        choice: str
        key: "Expr"
        arg: "Expr"

        def __init__(self, template: "TypeConName", choice: str, key: "Expr", arg: "Expr"):
            self.template = template
            self.choice = choice
            self.key = key
            self.arg = arg

    class Fetch:
        template: "TypeConName"
        cid: "Expr"

        def __init__(self, template, cid):
            self.template = template
            self.cid = cid

    class EmbedExpr:
        type: "Type"  # the expression should be of type `Scenario type`
        body: "Expr"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type", body: "Expr"):
            self.type = type
            self.body = body

    class RetrieveByKey:
        template: "TypeConName"
        key: "Expr"

        def __init__(self, template: "TypeConName", key: "Expr"):
            self.template = template
            self.key = key

    class TryCatch:
        return_type: Type
        try_expr: Expr
        var: str
        catch_expr: Expr

        def __init__(self, return_type: Type, try_expr: Expr, var: str, catch_expr: Expr):
            self.return_type = return_type
            self.try_expr = try_expr
            self.var = var
            self.catch_expr = catch_expr

    class CreateInterface:
        interface: TypeConName
        expr: Expr

        def __init__(self, interface: TypeConName, expr: Expr):
            self.interface = interface
            self.expr = expr

    class ExerciseInterface:
        interface: TypeConName
        cid: Expr
        arg: Expr
        guard: Expr

        def __init__(self, interface: TypeConName, cid: Expr, arg: Expr, guard: Expr):
            self.interface = interface
            self.cid = cid
            self.arg = arg
            self.guard = guard

    class FetchInterface:
        interface: TypeConName
        cid: Expr

        def __init__(self, interface: TypeConName, cid: Expr):
            self.interface = interface
            self.cid = cid

    __slots__ = "_Sum_name", "_Sum_value"
    _Sum_name: str
    _Sum_value: Any

    def __init__(
        self,
        pure: "Union[Pure, _Missing]" = MISSING,
        block: "Union[Block, _Missing]" = MISSING,
        create: "Union[Update.Create, _Missing]" = MISSING,
        exercise: "Union[Update.Exercise, _Missing]" = MISSING,
        exercise_by_key: "Union[Update.ExerciseByKey, _Missing]" = MISSING,
        fetch: "Union[Update.Fetch, _Missing]" = MISSING,
        get_time: "Union[Unit, _Missing]" = MISSING,
        lookup_by_key: "Union[Update.RetrieveByKey, _Missing]" = MISSING,
        fetch_by_key: "Union[Update.RetrieveByKey, _Missing]" = MISSING,
        embed_expr: "Union[Update.EmbedExpr, _Missing]" = MISSING,
        try_catch: "Union[Update.TryCatch, _Missing]" = MISSING,
        create_interface: "Union[Update.CreateInterface, _Missing]" = MISSING,
        exercise_interface: "Union[Update.ExerciseInterface, _Missing]" = MISSING,
        fetch_interface: "Union[Update.FetchInterface, _Missing]" = MISSING,
    ):
        if pure is not MISSING:
            object.__setattr__(self, "_Sum_name", "pure")
            object.__setattr__(self, "_Sum_value", pure)
        elif block is not MISSING:
            object.__setattr__(self, "_Sum_name", "block")
            object.__setattr__(self, "_Sum_value", block)
        elif create is not MISSING:
            object.__setattr__(self, "_Sum_name", "create")
            object.__setattr__(self, "_Sum_value", create)
        elif exercise is not MISSING:
            object.__setattr__(self, "_Sum_name", "exercise")
            object.__setattr__(self, "_Sum_value", exercise)
        elif exercise_by_key is not MISSING:
            object.__setattr__(self, "_Sum_name", "exercise_by_key")
            object.__setattr__(self, "_Sum_value", exercise_by_key)
        elif fetch is not MISSING:
            object.__setattr__(self, "_Sum_name", "fetch")
            object.__setattr__(self, "_Sum_value", fetch)
        elif get_time is not MISSING:
            object.__setattr__(self, "_Sum_name", "get_time")
            object.__setattr__(self, "_Sum_value", get_time)
        elif lookup_by_key is not MISSING:
            object.__setattr__(self, "_Sum_name", "lookup_by_key")
            object.__setattr__(self, "_Sum_value", lookup_by_key)
        elif fetch_by_key is not MISSING:
            object.__setattr__(self, "_Sum_name", "fetch_by_key")
            object.__setattr__(self, "_Sum_value", fetch_by_key)
        elif embed_expr is not MISSING:
            object.__setattr__(self, "_Sum_name", "embed_expr")
            object.__setattr__(self, "_Sum_value", embed_expr)
        elif try_catch is not MISSING:
            object.__setattr__(self, "_Sum_name", "try_catch")
            object.__setattr__(self, "_Sum_value", try_catch)
        elif create_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "create_interface")
            object.__setattr__(self, "_Sum_value", create_interface)
        elif exercise_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "exercise_interface")
            object.__setattr__(self, "_Sum_value", exercise_interface)
        elif fetch_interface is not MISSING:
            object.__setattr__(self, "_Sum_name", "fetch_interface")
            object.__setattr__(self, "_Sum_value", fetch_interface)

    @property
    def pure(self) -> "Optional[Pure]":
        """this is purely for compact serialization -- specifically to
        reduce the AST depth. it adds no expressive power."""
        return self._Sum_value if self._Sum_name == "pure" else None  # type: ignore

    @property
    def block(self) -> "Optional[Block]":
        return self._Sum_value if self._Sum_name == "block" else None  # type: ignore

    @property
    def create(self) -> "Optional[Create]":
        return self._Sum_value if self._Sum_name == "create" else None  # type: ignore

    @property
    def exercise(self) -> "Optional[Exercise]":
        return self._Sum_value if self._Sum_name == "exercise" else None  # type: ignore

    @property
    def fetch(self) -> "Optional[Fetch]":
        return self._Sum_value if self._Sum_name == "fetch" else None  # type: ignore

    @property
    def get_time(self) -> "Optional[Unit]":
        return self._Sum_value if self._Sum_name == "get_time" else None  # type: ignore

    @property
    def lookup_by_key(self) -> "Optional[RetrieveByKey]":
        return self._Sum_value if self._Sum_name == "lookup_by_key" else None  # type: ignore

    @property
    def fetch_by_key(self) -> "Optional[RetrieveByKey]":
        return self._Sum_value if self._Sum_name == "fetch_by_key" else None  # type: ignore

    @property
    def embed_expr(self) -> "Optional[EmbedExpr]":
        """see similar constructor in `Scenario` on why this is useful."""
        return self._Sum_value if self._Sum_name == "embed_expr" else None  # type: ignore

    @property
    def create_interface(self) -> "Optional[CreateInterface]":
        return self._Sum_value if self._Sum_name == "create_interface" else None  # type: ignore

    @property
    def exercise_interface(self) -> "Optional[ExerciseInterface]":
        return self._Sum_value if self._Sum_name == "exercise_interface" else None  # type: ignore

    @property
    def fetch_interface(self) -> "Optional[FetchInterface]":
        return self._Sum_value if self._Sum_name == "fetch_interface" else None  # type: ignore

    def Sum_match(
        self,
        pure: "Callable[[Pure], T]",
        block: "Callable[[Block], T]",
        create: "Callable[[Create], T]",
        exercise: "Callable[[Exercise], T]",
        fetch: "Callable[[Fetch], T]",
        get_time: "Callable[[Unit], T]",
        lookup_by_key: "Callable[[RetrieveByKey], T]",
        fetch_by_key: "Callable[[RetrieveByKey], T]",
        embed_expr: "Callable[[EmbedExpr], T]",
        create_interface: "Callable[[CreateInterface], T]",
        exercise_interface: "Callable[[ExerciseInterface], T]",
        fetch_interface: "Callable[[FetchInterface], T]",
    ) -> T:
        if self._Sum_name == "pure":
            return pure(self._Sum_value)  # type: ignore
        elif self._Sum_name == "block":
            return block(self._Sum_value)  # type: ignore
        elif self._Sum_name == "create":
            return create(self._Sum_value)  # type: ignore
        elif self._Sum_name == "exercise":
            return exercise(self._Sum_value)  # type: ignore
        elif self._Sum_name == "fetch":
            return fetch(self._Sum_value)  # type: ignore
        elif self._Sum_name == "get_time":
            return get_time(self._Sum_value)  # type: ignore
        elif self._Sum_name == "lookup_by_key":
            return lookup_by_key(self._Sum_value)  # type: ignore
        elif self._Sum_name == "fetch_by_key":
            return fetch_by_key(self._Sum_value)  # type: ignore
        elif self._Sum_name == "embed_expr":
            return embed_expr(self._Sum_value)  # type: ignore
        elif self._Sum_name == "create_interface":
            return create_interface(self._Sum_value)  # type: ignore
        elif self._Sum_name == "exercise_interface":
            return exercise_interface(self._Sum_value)  # type: ignore
        elif self._Sum_name == "fetch_interface":
            return fetch_interface(self._Sum_value)  # type: ignore
        else:
            raise ValueError(f"Unknown Update.Sum case: {self._Sum_name}")


class Scenario:
    class Commit:
        party: "Expr"
        expr: "Expr"
        ret_type: "Type"

        def __init__(self, party: "Expr", expr: "Expr", ret_type: "Type"):
            self.party = party
            self.expr = expr
            self.ret_type = ret_type

    class EmbedExpr:
        type: "Type"  # the expression should be of type `Scenario type`
        body: "Expr"

        # noinspection PyShadowingBuiltins
        def __init__(self, type: "Type", body: "Expr"):
            self.type = type
            self.body = body

    __slots__ = "_Sum_name", "_Sum_value"
    _Sum_name: str
    _Sum_value: Any

    def __init__(
        self,
        pure: "Union[Pure, _Missing]" = MISSING,
        block: "Union[Block, _Missing]" = MISSING,
        commit: "Union[Commit, _Missing]" = MISSING,
        must_fail_at: "Union[Commit, _Missing]" = MISSING,
        pass_: "Union[Expr, _Missing]" = MISSING,
        get_time: "Union[Unit, _Missing]" = MISSING,
        get_party: "Union[Expr, _Missing]" = MISSING,
        embed_expr: "Union[EmbedExpr, _Missing]" = MISSING,
    ):
        if pure is not MISSING:
            object.__setattr__(self, "_Sum_name", "pure")
            object.__setattr__(self, "_Sum_value", pure)
        elif block is not MISSING:
            object.__setattr__(self, "_Sum_name", "block")
            object.__setattr__(self, "_Sum_value", block)
        elif commit is not MISSING:
            object.__setattr__(self, "_Sum_name", "commit")
            object.__setattr__(self, "_Sum_value", commit)
        elif must_fail_at is not MISSING:
            object.__setattr__(self, "_Sum_name", "mustFailAt")
            object.__setattr__(self, "_Sum_value", must_fail_at)
        elif pass_ is not MISSING:
            object.__setattr__(self, "_Sum_name", "pass")
            object.__setattr__(self, "_Sum_value", pass_)
        elif get_time is not MISSING:
            object.__setattr__(self, "_Sum_name", "get_time")
            object.__setattr__(self, "_Sum_value", get_time)
        elif get_party is not MISSING:
            object.__setattr__(self, "_Sum_name", "get_party")
            object.__setattr__(self, "_Sum_value", get_party)
        elif embed_expr is not MISSING:
            object.__setattr__(self, "_Sum_name", "embed_expr")
            object.__setattr__(self, "_Sum_value", embed_expr)

    @property
    def pure(self) -> "Optional[Pure]":
        """this is purely for compact serialization -- specifically to
        reduce the AST depth. it adds no expressive power."""
        return self._Sum_value if self._Sum_name == "pure" else None

    @property
    def block(self) -> "Optional[Block]":
        return self._Sum_value if self._Sum_name == "block" else None

    @property
    def commit(self) -> "Optional[Commit]":
        return self._Sum_value if self._Sum_name == "create" else None

    @property
    def must_fail_at(self) -> "Optional[Commit]":
        return self._Sum_value if self._Sum_name == "mustFailAt" else None

    @property
    def pass_(self) -> "Optional[Expr]":
        return self._Sum_value if self._Sum_name == "pass" else None

    @property
    def get_time(self) -> "Optional[Unit]":
        """The expression is of type `Text`."""
        return self._Sum_value if self._Sum_name == "get_time" else None

    @property
    def get_party(self) -> "Optional[Expr]":
        return self._Sum_value if self._Sum_name == "get_party" else None

    @property
    def embed_expr(self) -> "Optional[EmbedExpr]":
        """
        Embed an expression of type Scenario. note that this construct is useful
        to explicitly mark the start of scenario execution, which is useful in
        top level definitions. for example if we hav

        def test : Scenario Unit = if <blah> then <this> else <that>

        this is not a value, since it's headed with an `if`, but we can turn
        it into a value by wrapping the `if` with this constructor. in that
        case, the `if` will be executed every time the scenario runs --
        as expected.
        """
        return self._Sum_value if self._Sum_name == "embed_expr" else None

    def Sum_match(
        self,
        pure: "Callable[[Pure], T]",
        block: "Callable[[Block], T]",
        commit: "Callable[[Commit], T]",
        must_fail_at: "Callable[[Commit], T]",
        pass_: "Callable[[Expr], T]",
        get_time: "Callable[[Unit], T]",
        get_party: "Callable[[Expr], T]",
        embed_expr: "Callable[[EmbedExpr], T]",
    ) -> T:
        if self._Sum_name == "pure":
            return pure(self._Sum_value)
        if self._Sum_name == "block":
            return block(self._Sum_value)
        if self._Sum_name == "commit":
            return commit(self._Sum_value)
        if self._Sum_name == "mustFailAt":
            return must_fail_at(self._Sum_value)
        if self._Sum_name == "pass":
            return pass_(self._Sum_value)
        if self._Sum_name == "get_time":
            return get_time(self._Sum_value)
        if self._Sum_name == "get_party":
            return get_party(self._Sum_value)
        if self._Sum_name == "embed_expr":
            return embed_expr(self._Sum_value)
        else:
            raise ValueError(f"unknown Scenario.Sum case: {self._Sum_name!r}")


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


class PrimCon(_IntEnum):
    CON_UNIT = 0
    CON_FALSE = 1
    CON_TRUE = 2


@dataclass(frozen=True)
class TemplateChoice:
    """Template choice definition."""

    # Name of the choice.
    name: str

    # Indicator whether exercising the choice consumes the contract instance.
    consuming: bool

    # The controllers of the choice. They have type `List Party` and the
    # template parameter in scope, but not the choice parameter. All of these
    # controllers need to authorize the exercising of this choice (aka
    # conjunctive choice controllers).
    controllers: "Expr"

    observers: "Optional[Expr]"

    # Name to which the choice argument is bound and its type.
    arg_binder: "VarWithType"

    # Return type of the choice.
    ret_type: "Type"

    # Follow-up update of the choice. It has type `Update <ret_type>` and both
    # the template parameter and the choice parameter in scope.
    update: "Expr"

    # Name to bind the ContractId of the contract this choice is exercised on to.
    self_binder: str

    location: "Location"


@dataclass(init=False, frozen=True)
class KeyExpr:
    _Sum_name: str
    _Sum_value: "Union[KeyExpr.Projections, KeyExpr.Record]"

    @dataclass(init=False, frozen=True)
    class Projections:
        projections: "Sequence[KeyExpr.Projection]"

        def __init__(self, projections: "Sequence[KeyExpr.Projection]"):
            object.__setattr__(self, "projections", tuple(projections))

    @dataclass(init=False, frozen=True)
    class Projection:
        tycon: "Type.Con"
        field: str

        def __init__(self, tycon: "Type.Con", field: str):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "field", field)

    @dataclass(init=False, frozen=True)
    class Record:
        tycon: "Type.Con"
        fields: "Sequence[KeyExpr.RecordField]"

        def __init__(self, tycon: "Type.Con", fields: "Sequence[KeyExpr.RecordField]"):
            object.__setattr__(self, "tycon", tycon)
            object.__setattr__(self, "fields", tuple(fields))

    @dataclass(frozen=True)
    class RecordField:
        field: str
        expr: "KeyExpr"

    def __init__(self, projections=MISSING, record=MISSING):
        if projections is not MISSING:
            object.__setattr__(self, "_Sum_name", "projections")
            object.__setattr__(self, "_Sum_value", projections)
        elif record is not MISSING:
            object.__setattr__(self, "_Sum_name", "record")
            object.__setattr__(self, "_Sum_value", record)
        else:
            raise ValueError("one of projections or record must be set")

    @property
    def projections(self) -> "Optional[KeyExpr.Projections]":
        return self.projections if self._Sum_name == "projections" else None

    @property
    def record(self) -> "Optional[KeyExpr.Record]":
        return self.record if self._Sum_name == "record" else None


@dataclass(frozen=True)
class DefTemplate:
    """Contract template definition"""

    @dataclass(frozen=True)
    class DefKey:
        type: "Type"
        _key_expr_name: str
        _key_expr_value: Union[KeyExpr, Expr]
        maintainers: "Expr"

        def __init__(self, type=MISSING, key=MISSING, complex_key=MISSING, maintainers=MISSING):
            object.__setattr__(self, "type", type)
            if key is not MISSING:
                object.__setattr__(self, "_key_expr_name", "key")
                object.__setattr__(self, "_key_expr_value", key)
            elif complex_key is not MISSING:
                object.__setattr__(self, "_key_expr_name", "complex_key")
                object.__setattr__(self, "_key_expr_value", complex_key)
            else:
                raise ValueError("one of key/complex_key must be set")
            object.__setattr__(self, "maintainers", maintainers)

        @property
        def key(self) -> "Optional[KeyExpr]":
            if self._key_expr_name == "key":
                return self._key_expr_value  # type: ignore
            else:
                return None

        @property
        def complex_key(self) -> "Optional[Expr]":
            if self._key_expr_name == "complex_key":
                return self._key_expr_value  # type: ignore
            else:
                return None

    # The type constructor for the template, acting as both
    # the name of the template and the type of the template argument.
    tycon: "DottedName"

    # Name to which the template argument is bound.
    param: str

    # Optional pre-condition that the template argument must satisfy.
    # When present, it has type `Bool` and the template parameter in scope.
    precond: "Expr"

    # The signatories of the contract. They have type `List Party` and the
    # template parameter in scope.
    signatories: "Expr"

    # The agreement text associated with the contract. It has type `Text` and
    # the template parameter in scope.
    agreement: "Expr"

    # The choices available in the resulting contract.
    choices: "Sequence[TemplateChoice]"

    # The observers of the contract. They have type `List Party` and the
    # template parameter in scope.
    observers: "Expr"

    location: "Location"

    # The key definition for the template, if present
    key: "Optional[DefKey]"


class DefDataType:
    """
    A record, variant, or enum data type definition.
    """

    class Fields:
        fields: "Sequence[FieldWithType]"

        def __init__(self, fields: "Sequence[FieldWithType]"):
            self.fields = fields

    class EnumConstructors:
        constructors: "Sequence[str]"

        def __init__(self, constructors: "Sequence[str]"):
            self.constructors = constructors

    name: DottedName
    params: "Sequence[TypeVarWithKind]"
    _DataCons_name: str
    _DataCons_value: "Any"
    serializable: bool
    location: "Location"

    def __init__(
        self,
        name: "Union[DottedName, _Missing]" = MISSING,
        params: "Union[Sequence[TypeVarWithKind], _Missing]" = MISSING,
        record: "Union[DefDataType.Fields, _Missing]" = MISSING,
        variant: "Union[DefDataType.Fields, _Missing]" = MISSING,
        enum: "Union[DefDataType.EnumConstructors, _Missing]" = MISSING,
        interface: "Union[Unit, _Missing]" = MISSING,
        synonym: "Union[Type, _Missing]" = MISSING,
        serializable: "Union[bool, _Missing]" = MISSING,
        location: "Union[Location, _Missing]" = MISSING,
    ):
        self.name = name  # type: ignore
        self.params = params  # type: ignore
        if record is not MISSING:
            self._DataCons_name = "record"
            self._DataCons_value = record  # type: ignore
        elif variant is not MISSING:
            self._DataCons_name = "variant"
            self._DataCons_value = variant  # type: ignore
        elif enum is not MISSING:
            self._DataCons_name = "enum"
            self._DataCons_value = enum  # type: ignore
        elif interface is not MISSING:
            self._DataCons_name = "interface"
            self._DataCons_value = interface
        elif synonym is not MISSING:
            self._DataCons_name = "synonym"
            self._DataCons_value = synonym  # type: ignore
        self.serializable = serializable  # type: ignore
        self.location = location  # type: ignore

    @property
    def record(self) -> "Optional[DefDataType.Fields]":
        return self._DataCons_value if self._DataCons_name == "record" else None

    @property
    def variant(self) -> "Optional[DefDataType.Fields]":
        return self._DataCons_value if self._DataCons_name == "variant" else None

    @property
    def enum(self) -> "Optional[DefDataType.EnumConstructors]":
        if self._DataCons_name == "enum":
            return self._DataCons_value  # type: ignore
        else:
            return None

    @property
    def interface(self) -> "Optional[Unit]":
        if self._DataCons_name == "interface":
            return self._DataCons_value  # type: ignore
        else:
            return None

    @property
    def synonym(self) -> "Optional[Type]":
        if self._DataCons_name == "synonym":
            return self._DataCons_value  # type: ignore
        else:
            return None


@dataclass(frozen=True)
class DefTypeSyn:
    name: "DottedName"
    params: "Sequence[TypeVarWithKind]"
    type: "Type"
    location: "Optional[Location]"


class DefValue:
    """Value definition"""

    class NameWithType:
        """
        The reason why we have this type instead of just flattening name and type in
        DefValue is that it was VarWithType before, and we want to be binary-compatible
        with it.
        """

        name: "Sequence[str]"
        type: "Type"

        # noinspection PyShadowingBuiltins
        def __init__(self, name: "Sequence[str]", type: "Type"):
            self.name = tuple(name)
            self.type = type

    name_with_type: "DefValue.NameWithType"

    _lazy_lock: threading.RLock
    _expr: "Optional[Expr]"
    _expr_fn: "Callable[[], Expr]"

    # If true, the value must not contain any party literals and not reference
    # values which contain party literals.
    # This flag is used to simplify package validation by not requiring an
    # inference but only a check. Such a check must validate that this flag is
    # set correctly and that templates do not reference values which have this
    # flag set to false.
    no_party_literals: bool
    is_test: bool
    location: "Optional[Location]"

    __slots__ = (
        "name_with_type",
        "_lazy_lock",
        "_expr",
        "_expr_fn",
        "no_party_literals",
        "is_test",
        "location",
    )

    def __init__(
        self,
        name_with_type: "DefValue.NameWithType",
        expr: "Union[Expr, Callable[[], Expr]]",
        no_party_literals: bool,
        is_test: bool,
        location: "Optional[Location]" = None,
    ):
        object.__setattr__(self, "name_with_type", name_with_type)
        object.__setattr__(self, "_lazy_lock", threading.RLock())
        object.__setattr__(self, "_expr", None)
        object.__setattr__(self, "_expr_fn", (lambda: expr) if isinstance(expr, Expr) else expr)
        object.__setattr__(self, "no_party_literals", no_party_literals)
        object.__setattr__(self, "is_test", is_test)
        object.__setattr__(self, "location", location)

    @property
    def expr(self) -> "Expr":
        expr = self._expr
        if expr is not None:
            return expr

        with self._lazy_lock:
            expr = self._expr
            if expr is None:
                expr = self._expr_fn()  # type: ignore
                object.__setattr__(self, "_expr", expr)
            return expr

    def __setattr__(self, key, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (
                self.name_with_type,
                self.no_party_literals,
                self.is_test,
                self.location,
            )
        )

    def __repr__(self):
        return f"DefValue(name_with_type={self.name_with_type!r}, expr=..., no_party_literals={self.no_party_literals!r}, is_test={self.is_test!r}, location={self.location!r})"


@dataclass(frozen=True)
class FeatureFlags:
    forbid_party_literals: bool
    dont_divulge_contract_ids_in_create_arguments: bool
    dont_disclose_nonconsuming_choices_to_observers: bool


@dataclass(frozen=True)
class Module:
    name: "DottedName"
    flags: "FeatureFlags"
    synonyms: "Sequence[DefTypeSyn]"
    data_types: "Sequence[DefDataType]"
    values: "Sequence[DefValue]"
    templates: "Sequence[DefTemplate]"


@dataclass(frozen=True)
class Package:
    modules: "Sequence[Module]"
    metadata: "Optional[PackageMetadata]"


@dataclass(frozen=True)
class PackageMetadata:
    name: str
    version: str


@dataclass(frozen=True)
class Archive:
    hash: "PackageRef"
    package: "Package"
