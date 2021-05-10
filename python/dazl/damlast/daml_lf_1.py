from enum import IntEnum as _IntEnum
import builtins as _builtins
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


<<<<<<< HEAD
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
    ) -> "_T":
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
        guard: Optional[Expr]

        def __init__(self, interface: TypeConName, cid: Expr, arg: Expr, guard: Optional[Expr]):
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
=======
class PrimCon(_IntEnum):
    CON_UNIT = 0
    CON_FALSE = 1
    CON_TRUE = 2
>>>>>>> 7a94d0a (python: Generate daml_lf_1.py and daml_lf_1.pyi.)


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
        return (
            self.package_ref == __other.package_ref
            and self.module_name == __other.module_name
        )

    def __ne__(self, __other):
        return (
            self.package_ref != __other.package_ref
            or self.module_name != __other.module_name
        )

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
<<<<<<< HEAD
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
=======
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
>>>>>>> 7a94d0a (python: Generate daml_lf_1.py and daml_lf_1.pyi.)

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

<<<<<<< HEAD
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
=======
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

    def Sum_match(
        self, int64, decimal, numeric, text, timestamp, party, date, rounding_mode
    ):
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
>>>>>>> 7a94d0a (python: Generate daml_lf_1.py and daml_lf_1.pyi.)
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
    class ToInterface:
        __match_args__ = ("interface_type", "template_type", "template_expr")

        __slots__ = ("interface_type", "template_type", "template_expr")

        def __init__(self, interface_type, template_type, template_expr):
            object.__setattr__(self, "interface_type", interface_type)
            object.__setattr__(self, "template_type", template_type)
            object.__setattr__(self, "template_expr", template_expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface_type, self.template_type, self.template_expr))

        def __eq__(self, __other):
            return (
                self.interface_type == __other.interface_type
                and self.template_type == __other.template_type
                and self.template_expr == __other.template_expr
            )

        def __ne__(self, __other):
            return (
                self.interface_type != __other.interface_type
                or self.template_type != __other.template_type
                or self.template_expr != __other.template_expr
            )

        def __lt__(self, __other):
            return (self.interface_type, self.template_type, self.template_expr) < (
                __other.interface_type,
                __other.template_type,
                __other.template_expr,
            )

        def __le__(self, __other):
            return (self.interface_type, self.template_type, self.template_expr) <= (
                __other.interface_type,
                __other.template_type,
                __other.template_expr,
            )

        def __gt__(self, __other):
            return (self.interface_type, self.template_type, self.template_expr) > (
                __other.interface_type,
                __other.template_type,
                __other.template_expr,
            )

        def __ge__(self, __other):
            return (self.interface_type, self.template_type, self.template_expr) >= (
                __other.interface_type,
                __other.template_type,
                __other.template_expr,
            )

        def __repr__(self):
            return f"Expr.ToInterface(interface_type={self.interface_type!r}, template_type={self.template_type!r}, template_expr={self.template_expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromInterface:
        __match_args__ = ("interface_type", "template_type", "interface_expr")

        __slots__ = ("interface_type", "template_type", "interface_expr")

        def __init__(self, interface_type, template_type, interface_expr):
            object.__setattr__(self, "interface_type", interface_type)
            object.__setattr__(self, "template_type", template_type)
            object.__setattr__(self, "interface_expr", interface_expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface_type, self.template_type, self.interface_expr))

        def __eq__(self, __other):
            return (
                self.interface_type == __other.interface_type
                and self.template_type == __other.template_type
                and self.interface_expr == __other.interface_expr
            )

        def __ne__(self, __other):
            return (
                self.interface_type != __other.interface_type
                or self.template_type != __other.template_type
                or self.interface_expr != __other.interface_expr
            )

        def __lt__(self, __other):
            return (self.interface_type, self.template_type, self.interface_expr) < (
                __other.interface_type,
                __other.template_type,
                __other.interface_expr,
            )

        def __le__(self, __other):
            return (self.interface_type, self.template_type, self.interface_expr) <= (
                __other.interface_type,
                __other.template_type,
                __other.interface_expr,
            )

        def __gt__(self, __other):
            return (self.interface_type, self.template_type, self.interface_expr) > (
                __other.interface_type,
                __other.template_type,
                __other.interface_expr,
            )

        def __ge__(self, __other):
            return (self.interface_type, self.template_type, self.interface_expr) >= (
                __other.interface_type,
                __other.template_type,
                __other.interface_expr,
            )

        def __repr__(self):
            return f"Expr.FromInterface(interface_type={self.interface_type!r}, template_type={self.template_type!r}, interface_expr={self.interface_expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class CallInterface:
        __match_args__ = ("interface_type", "method_interned_name", "interface_expr")

        __slots__ = ("interface_type", "method_interned_name", "interface_expr")

        def __init__(self, interface_type, method_interned_name, interface_expr):
            object.__setattr__(self, "interface_type", interface_type)
            object.__setattr__(self, "method_interned_name", method_interned_name)
            object.__setattr__(self, "interface_expr", interface_expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash(
                (self.interface_type, self.method_interned_name, self.interface_expr)
            )

        def __eq__(self, __other):
            return (
                self.interface_type == __other.interface_type
                and self.method_interned_name == __other.method_interned_name
                and self.interface_expr == __other.interface_expr
            )

        def __ne__(self, __other):
            return (
                self.interface_type != __other.interface_type
                or self.method_interned_name != __other.method_interned_name
                or self.interface_expr != __other.interface_expr
            )

        def __lt__(self, __other):
            return (
                self.interface_type,
                self.method_interned_name,
                self.interface_expr,
            ) < (
                __other.interface_type,
                __other.method_interned_name,
                __other.interface_expr,
            )

        def __le__(self, __other):
            return (
                self.interface_type,
                self.method_interned_name,
                self.interface_expr,
            ) <= (
                __other.interface_type,
                __other.method_interned_name,
                __other.interface_expr,
            )

        def __gt__(self, __other):
            return (
                self.interface_type,
                self.method_interned_name,
                self.interface_expr,
            ) > (
                __other.interface_type,
                __other.method_interned_name,
                __other.interface_expr,
            )

        def __ge__(self, __other):
            return (
                self.interface_type,
                self.method_interned_name,
                self.interface_expr,
            ) >= (
                __other.interface_type,
                __other.method_interned_name,
                __other.interface_expr,
            )

        def __repr__(self):
            return f"Expr.CallInterface(interface_type={self.interface_type!r}, method_interned_name={self.method_interned_name!r}, interface_expr={self.interface_expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ViewInterface:
        __match_args__ = ("interface", "expr")

        __slots__ = ("interface", "expr")

        def __init__(self, interface, expr):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.expr))

        def __eq__(self, __other):
            return self.interface == __other.interface and self.expr == __other.expr

        def __ne__(self, __other):
            return self.interface != __other.interface or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.interface, self.expr) < (__other.interface, __other.expr)

        def __le__(self, __other):
            return (self.interface, self.expr) <= (__other.interface, __other.expr)

        def __gt__(self, __other):
            return (self.interface, self.expr) > (__other.interface, __other.expr)

        def __ge__(self, __other):
            return (self.interface, self.expr) >= (__other.interface, __other.expr)

        def __repr__(self):
            return f"Expr.ViewInterface(interface={self.interface!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class SignatoryInterface:
        __match_args__ = ("interface", "expr")

        __slots__ = ("interface", "expr")

        def __init__(self, interface, expr):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.expr))

        def __eq__(self, __other):
            return self.interface == __other.interface and self.expr == __other.expr

        def __ne__(self, __other):
            return self.interface != __other.interface or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.interface, self.expr) < (__other.interface, __other.expr)

        def __le__(self, __other):
            return (self.interface, self.expr) <= (__other.interface, __other.expr)

        def __gt__(self, __other):
            return (self.interface, self.expr) > (__other.interface, __other.expr)

        def __ge__(self, __other):
            return (self.interface, self.expr) >= (__other.interface, __other.expr)

        def __repr__(self):
            return f"Expr.SignatoryInterface(interface={self.interface!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ObserverInterface:
        __match_args__ = ("interface", "expr")

        __slots__ = ("interface", "expr")

        def __init__(self, interface, expr):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.expr))

        def __eq__(self, __other):
            return self.interface == __other.interface and self.expr == __other.expr

        def __ne__(self, __other):
            return self.interface != __other.interface or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.interface, self.expr) < (__other.interface, __other.expr)

        def __le__(self, __other):
            return (self.interface, self.expr) <= (__other.interface, __other.expr)

        def __gt__(self, __other):
            return (self.interface, self.expr) > (__other.interface, __other.expr)

        def __ge__(self, __other):
            return (self.interface, self.expr) >= (__other.interface, __other.expr)

        def __repr__(self):
            return f"Expr.ObserverInterface(interface={self.interface!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class UnsafeFromInterface:
        __match_args__ = (
            "interface_type",
            "template_type",
            "contract_id_expr",
            "interface_expr",
        )

        __slots__ = (
            "interface_type",
            "template_type",
            "contract_id_expr",
            "interface_expr",
        )

        def __init__(
            self, interface_type, template_type, contract_id_expr, interface_expr
        ):
            object.__setattr__(self, "interface_type", interface_type)
            object.__setattr__(self, "template_type", template_type)
            object.__setattr__(self, "contract_id_expr", contract_id_expr)
            object.__setattr__(self, "interface_expr", interface_expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash(
                (
                    self.interface_type,
                    self.template_type,
                    self.contract_id_expr,
                    self.interface_expr,
                )
            )

        def __eq__(self, __other):
            return (
                self.interface_type == __other.interface_type
                and self.template_type == __other.template_type
                and self.contract_id_expr == __other.contract_id_expr
                and self.interface_expr == __other.interface_expr
            )

        def __ne__(self, __other):
            return (
                self.interface_type != __other.interface_type
                or self.template_type != __other.template_type
                or self.contract_id_expr != __other.contract_id_expr
                or self.interface_expr != __other.interface_expr
            )

        def __lt__(self, __other):
            return (
                self.interface_type,
                self.template_type,
                self.contract_id_expr,
                self.interface_expr,
            ) < (
                __other.interface_type,
                __other.template_type,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __le__(self, __other):
            return (
                self.interface_type,
                self.template_type,
                self.contract_id_expr,
                self.interface_expr,
            ) <= (
                __other.interface_type,
                __other.template_type,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __gt__(self, __other):
            return (
                self.interface_type,
                self.template_type,
                self.contract_id_expr,
                self.interface_expr,
            ) > (
                __other.interface_type,
                __other.template_type,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __ge__(self, __other):
            return (
                self.interface_type,
                self.template_type,
                self.contract_id_expr,
                self.interface_expr,
            ) >= (
                __other.interface_type,
                __other.template_type,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __repr__(self):
            return f"Expr.UnsafeFromInterface(interface_type={self.interface_type!r}, template_type={self.template_type!r}, contract_id_expr={self.contract_id_expr!r}, interface_expr={self.interface_expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class ToRequiredInterface:
        __match_args__ = ("required_interface", "requiring_interface", "expr")

        __slots__ = ("required_interface", "requiring_interface", "expr")

        def __init__(self, required_interface, requiring_interface, expr):
            object.__setattr__(self, "required_interface", required_interface)
            object.__setattr__(self, "requiring_interface", requiring_interface)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.required_interface, self.requiring_interface, self.expr))

        def __eq__(self, __other):
            return (
                self.required_interface == __other.required_interface
                and self.requiring_interface == __other.requiring_interface
                and self.expr == __other.expr
            )

        def __ne__(self, __other):
            return (
                self.required_interface != __other.required_interface
                or self.requiring_interface != __other.requiring_interface
                or self.expr != __other.expr
            )

        def __lt__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) < (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __le__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) <= (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __gt__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) > (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __ge__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) >= (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __repr__(self):
            return f"Expr.ToRequiredInterface(required_interface={self.required_interface!r}, requiring_interface={self.requiring_interface!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class FromRequiredInterface:
        __match_args__ = ("required_interface", "requiring_interface", "expr")

        __slots__ = ("required_interface", "requiring_interface", "expr")

        def __init__(self, required_interface, requiring_interface, expr):
            object.__setattr__(self, "required_interface", required_interface)
            object.__setattr__(self, "requiring_interface", requiring_interface)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.required_interface, self.requiring_interface, self.expr))

        def __eq__(self, __other):
            return (
                self.required_interface == __other.required_interface
                and self.requiring_interface == __other.requiring_interface
                and self.expr == __other.expr
            )

        def __ne__(self, __other):
            return (
                self.required_interface != __other.required_interface
                or self.requiring_interface != __other.requiring_interface
                or self.expr != __other.expr
            )

        def __lt__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) < (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __le__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) <= (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __gt__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) > (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __ge__(self, __other):
            return (self.required_interface, self.requiring_interface, self.expr) >= (
                __other.required_interface,
                __other.requiring_interface,
                __other.expr,
            )

        def __repr__(self):
            return f"Expr.FromRequiredInterface(required_interface={self.required_interface!r}, requiring_interface={self.requiring_interface!r}, expr={self.expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class UnsafeFromRequiredInterface:
        __match_args__ = (
            "required_interface",
            "requiring_interface",
            "contract_id_expr",
            "interface_expr",
        )

        __slots__ = (
            "required_interface",
            "requiring_interface",
            "contract_id_expr",
            "interface_expr",
        )

        def __init__(
            self,
            required_interface,
            requiring_interface,
            contract_id_expr,
            interface_expr,
        ):
            object.__setattr__(self, "required_interface", required_interface)
            object.__setattr__(self, "requiring_interface", requiring_interface)
            object.__setattr__(self, "contract_id_expr", contract_id_expr)
            object.__setattr__(self, "interface_expr", interface_expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash(
                (
                    self.required_interface,
                    self.requiring_interface,
                    self.contract_id_expr,
                    self.interface_expr,
                )
            )

        def __eq__(self, __other):
            return (
                self.required_interface == __other.required_interface
                and self.requiring_interface == __other.requiring_interface
                and self.contract_id_expr == __other.contract_id_expr
                and self.interface_expr == __other.interface_expr
            )

        def __ne__(self, __other):
            return (
                self.required_interface != __other.required_interface
                or self.requiring_interface != __other.requiring_interface
                or self.contract_id_expr != __other.contract_id_expr
                or self.interface_expr != __other.interface_expr
            )

        def __lt__(self, __other):
            return (
                self.required_interface,
                self.requiring_interface,
                self.contract_id_expr,
                self.interface_expr,
            ) < (
                __other.required_interface,
                __other.requiring_interface,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __le__(self, __other):
            return (
                self.required_interface,
                self.requiring_interface,
                self.contract_id_expr,
                self.interface_expr,
            ) <= (
                __other.required_interface,
                __other.requiring_interface,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __gt__(self, __other):
            return (
                self.required_interface,
                self.requiring_interface,
                self.contract_id_expr,
                self.interface_expr,
            ) > (
                __other.required_interface,
                __other.requiring_interface,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __ge__(self, __other):
            return (
                self.required_interface,
                self.requiring_interface,
                self.contract_id_expr,
                self.interface_expr,
            ) >= (
                __other.required_interface,
                __other.requiring_interface,
                __other.contract_id_expr,
                __other.interface_expr,
            )

        def __repr__(self):
            return f"Expr.UnsafeFromRequiredInterface(required_interface={self.required_interface!r}, requiring_interface={self.requiring_interface!r}, contract_id_expr={self.contract_id_expr!r}, interface_expr={self.interface_expr!r}, )"

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class InterfaceTemplateTypeRep:
        __match_args__ = ("interface", "expr")

        __slots__ = ("interface", "expr")

        def __init__(self, interface, expr):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.expr))

        def __eq__(self, __other):
            return self.interface == __other.interface and self.expr == __other.expr

        def __ne__(self, __other):
            return self.interface != __other.interface or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.interface, self.expr) < (__other.interface, __other.expr)

        def __le__(self, __other):
            return (self.interface, self.expr) <= (__other.interface, __other.expr)

        def __gt__(self, __other):
            return (self.interface, self.expr) > (__other.interface, __other.expr)

        def __ge__(self, __other):
            return (self.interface, self.expr) >= (__other.interface, __other.expr)

        def __repr__(self):
            return f"Expr.InterfaceTemplateTypeRep(interface={self.interface!r}, expr={self.expr!r}, )"

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
        to_interface=None,
        from_interface=None,
        call_interface=None,
        signatory_interface=None,
        observer_interface=None,
        view_interface=None,
        unsafe_from_interface=None,
        interface_template_type_rep=None,
        to_required_interface=None,
        from_required_interface=None,
        unsafe_from_required_interface=None,
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
        if to_interface is not None:
            object.__setattr__(self, "Sum", ("to_interface", to_interface))
            Sum.append("to_interface")
        if from_interface is not None:
            object.__setattr__(self, "Sum", ("from_interface", from_interface))
            Sum.append("from_interface")
        if call_interface is not None:
            object.__setattr__(self, "Sum", ("call_interface", call_interface))
            Sum.append("call_interface")
        if signatory_interface is not None:
            object.__setattr__(
                self, "Sum", ("signatory_interface", signatory_interface)
            )
            Sum.append("signatory_interface")
        if observer_interface is not None:
            object.__setattr__(self, "Sum", ("observer_interface", observer_interface))
            Sum.append("observer_interface")
        if view_interface is not None:
            object.__setattr__(self, "Sum", ("view_interface", view_interface))
            Sum.append("view_interface")
        if unsafe_from_interface is not None:
            object.__setattr__(
                self, "Sum", ("unsafe_from_interface", unsafe_from_interface)
            )
            Sum.append("unsafe_from_interface")
        if interface_template_type_rep is not None:
            object.__setattr__(
                self,
                "Sum",
                ("interface_template_type_rep", interface_template_type_rep),
            )
            Sum.append("interface_template_type_rep")
        if to_required_interface is not None:
            object.__setattr__(
                self, "Sum", ("to_required_interface", to_required_interface)
            )
            Sum.append("to_required_interface")
        if from_required_interface is not None:
            object.__setattr__(
                self, "Sum", ("from_required_interface", from_required_interface)
            )
            Sum.append("from_required_interface")
        if unsafe_from_required_interface is not None:
            object.__setattr__(
                self,
                "Sum",
                ("unsafe_from_required_interface", unsafe_from_required_interface),
            )
            Sum.append("unsafe_from_required_interface")
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
        to_interface,
        from_interface,
        call_interface,
        signatory_interface,
        observer_interface,
        view_interface,
        unsafe_from_interface,
        interface_template_type_rep,
        to_required_interface,
        from_required_interface,
        unsafe_from_required_interface,
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
        elif self.Sum[0] == "to_interface":
            return to_interface(self.Sum[1])
        elif self.Sum[0] == "from_interface":
            return from_interface(self.Sum[1])
        elif self.Sum[0] == "call_interface":
            return call_interface(self.Sum[1])
        elif self.Sum[0] == "signatory_interface":
            return signatory_interface(self.Sum[1])
        elif self.Sum[0] == "observer_interface":
            return observer_interface(self.Sum[1])
        elif self.Sum[0] == "view_interface":
            return view_interface(self.Sum[1])
        elif self.Sum[0] == "unsafe_from_interface":
            return unsafe_from_interface(self.Sum[1])
        elif self.Sum[0] == "interface_template_type_rep":
            return interface_template_type_rep(self.Sum[1])
        elif self.Sum[0] == "to_required_interface":
            return to_required_interface(self.Sum[1])
        elif self.Sum[0] == "from_required_interface":
            return from_required_interface(self.Sum[1])
        elif self.Sum[0] == "unsafe_from_required_interface":
            return unsafe_from_required_interface(self.Sum[1])
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
            return (
                self.var_head == __other.var_head and self.var_tail == __other.var_tail
            )

        def __ne__(self, __other):
            return (
                self.var_head != __other.var_head or self.var_tail != __other.var_tail
            )

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

    def Sum_match(
        self, default, variant, prim_con, nil, cons, optional_none, optional_some, enum
    ):
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
    class CreateInterface:
        __match_args__ = ("interface", "expr")

        __slots__ = ("interface", "expr")

        def __init__(self, interface, expr):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "expr", expr)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.expr))

        def __eq__(self, __other):
            return self.interface == __other.interface and self.expr == __other.expr

        def __ne__(self, __other):
            return self.interface != __other.interface or self.expr != __other.expr

        def __lt__(self, __other):
            return (self.interface, self.expr) < (__other.interface, __other.expr)

        def __le__(self, __other):
            return (self.interface, self.expr) <= (__other.interface, __other.expr)

        def __gt__(self, __other):
            return (self.interface, self.expr) > (__other.interface, __other.expr)

        def __ge__(self, __other):
            return (self.interface, self.expr) >= (__other.interface, __other.expr)

        def __repr__(self):
            return f"Update.CreateInterface(interface={self.interface!r}, expr={self.expr!r}, )"

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
    class ExerciseInterface:
        __match_args__ = ("interface", "choice", "cid", "arg", "guard")

        __slots__ = ("interface", "choice", "cid", "arg", "guard")

        def __init__(self, interface, choice, cid, arg, guard):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "choice", choice)
            object.__setattr__(self, "cid", cid)
            object.__setattr__(self, "arg", arg)
            object.__setattr__(self, "guard", guard)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.choice, self.cid, self.arg, self.guard))

        def __eq__(self, __other):
            return (
                self.interface == __other.interface
                and self.choice == __other.choice
                and self.cid == __other.cid
                and self.arg == __other.arg
                and self.guard == __other.guard
            )

        def __ne__(self, __other):
            return (
                self.interface != __other.interface
                or self.choice != __other.choice
                or self.cid != __other.cid
                or self.arg != __other.arg
                or self.guard != __other.guard
            )

        def __lt__(self, __other):
            return (self.interface, self.choice, self.cid, self.arg, self.guard) < (
                __other.interface,
                __other.choice,
                __other.cid,
                __other.arg,
                __other.guard,
            )

        def __le__(self, __other):
            return (self.interface, self.choice, self.cid, self.arg, self.guard) <= (
                __other.interface,
                __other.choice,
                __other.cid,
                __other.arg,
                __other.guard,
            )

        def __gt__(self, __other):
            return (self.interface, self.choice, self.cid, self.arg, self.guard) > (
                __other.interface,
                __other.choice,
                __other.cid,
                __other.arg,
                __other.guard,
            )

        def __ge__(self, __other):
            return (self.interface, self.choice, self.cid, self.arg, self.guard) >= (
                __other.interface,
                __other.choice,
                __other.cid,
                __other.arg,
                __other.guard,
            )

        def __repr__(self):
            return f"Update.ExerciseInterface(interface={self.interface!r}, choice={self.choice!r}, cid={self.cid!r}, arg={self.arg!r}, guard={self.guard!r}, )"

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
    class FetchInterface:
        __match_args__ = ("interface", "cid")

        __slots__ = ("interface", "cid")

        def __init__(self, interface, cid):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "cid", cid)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.cid))

        def __eq__(self, __other):
            return self.interface == __other.interface and self.cid == __other.cid

        def __ne__(self, __other):
            return self.interface != __other.interface or self.cid != __other.cid

        def __lt__(self, __other):
            return (self.interface, self.cid) < (__other.interface, __other.cid)

        def __le__(self, __other):
            return (self.interface, self.cid) <= (__other.interface, __other.cid)

        def __gt__(self, __other):
            return (self.interface, self.cid) > (__other.interface, __other.cid)

        def __ge__(self, __other):
            return (self.interface, self.cid) >= (__other.interface, __other.cid)

        def __repr__(self):
            return f"Update.FetchInterface(interface={self.interface!r}, cid={self.cid!r}, )"

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
            return (
                f"Update.RetrieveByKey(template={self.template!r}, key={self.key!r}, )"
            )

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
        create_interface=None,
        exercise_interface=None,
        fetch_interface=None,
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
        if create_interface is not None:
            object.__setattr__(self, "Sum", ("create_interface", create_interface))
            Sum.append("create_interface")
        if exercise_interface is not None:
            object.__setattr__(self, "Sum", ("exercise_interface", exercise_interface))
            Sum.append("exercise_interface")
        if fetch_interface is not None:
            object.__setattr__(self, "Sum", ("fetch_interface", fetch_interface))
            Sum.append("fetch_interface")
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
        create_interface,
        exercise_interface,
        fetch_interface,
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
        elif self.Sum[0] == "create_interface":
            return create_interface(self.Sum[1])
        elif self.Sum[0] == "exercise_interface":
            return exercise_interface(self.Sum[1])
        elif self.Sum[0] == "fetch_interface":
            return fetch_interface(self.Sum[1])
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

    def Sum_match(
        self, pure, block, commit, must_fail_at, pass_, get_time, get_party, embed_expr
    ):
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
class InterfaceInstanceBody:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class InterfaceInstanceMethod:
        __match_args__ = ("method_interned_name", "value")

        __slots__ = ("method_interned_name", "value")

        def __init__(self, method_interned_name, value):
            object.__setattr__(self, "method_interned_name", method_interned_name)
            object.__setattr__(self, "value", value)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.method_interned_name, self.value))

        def __eq__(self, __other):
            return (
                self.method_interned_name == __other.method_interned_name
                and self.value == __other.value
            )

        def __ne__(self, __other):
            return (
                self.method_interned_name != __other.method_interned_name
                or self.value != __other.value
            )

        def __lt__(self, __other):
            return (self.method_interned_name, self.value) < (
                __other.method_interned_name,
                __other.value,
            )

        def __le__(self, __other):
            return (self.method_interned_name, self.value) <= (
                __other.method_interned_name,
                __other.value,
            )

        def __gt__(self, __other):
            return (self.method_interned_name, self.value) > (
                __other.method_interned_name,
                __other.value,
            )

        def __ge__(self, __other):
            return (self.method_interned_name, self.value) >= (
                __other.method_interned_name,
                __other.value,
            )

        def __repr__(self):
            return f"InterfaceInstanceBody.InterfaceInstanceMethod(method_interned_name={self.method_interned_name!r}, value={self.value!r}, )"

    __match_args__ = ("methods", "view")

    __slots__ = ("methods", "view")

    def __init__(self, methods, view):
        object.__setattr__(self, "methods", _builtins.tuple(methods))
        object.__setattr__(self, "view", view)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.methods, self.view))

    def __eq__(self, __other):
        return self.methods == __other.methods and self.view == __other.view

    def __ne__(self, __other):
        return self.methods != __other.methods or self.view != __other.view

    def __lt__(self, __other):
        return (self.methods, self.view) < (__other.methods, __other.view)

    def __le__(self, __other):
        return (self.methods, self.view) <= (__other.methods, __other.view)

    def __gt__(self, __other):
        return (self.methods, self.view) > (__other.methods, __other.view)

    def __ge__(self, __other):
        return (self.methods, self.view) >= (__other.methods, __other.view)

    def __repr__(self):
        return f"InterfaceInstanceBody(methods={self.methods!r}, view={self.view!r}, )"


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

    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class Implements:
        __match_args__ = ("interface", "body")

        __slots__ = ("interface", "body")

        def __init__(self, interface, body):
            object.__setattr__(self, "interface", interface)
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.interface, self.body))

        def __eq__(self, __other):
            return self.interface == __other.interface and self.body == __other.body

        def __ne__(self, __other):
            return self.interface != __other.interface or self.body != __other.body

        def __lt__(self, __other):
            return (self.interface, self.body) < (__other.interface, __other.body)

        def __le__(self, __other):
            return (self.interface, self.body) <= (__other.interface, __other.body)

        def __gt__(self, __other):
            return (self.interface, self.body) > (__other.interface, __other.body)

        def __ge__(self, __other):
            return (self.interface, self.body) >= (__other.interface, __other.body)

        def __repr__(self):
            return f"DefTemplate.Implements(interface={self.interface!r}, body={self.body!r}, )"

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
        "implements",
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
        implements,
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
        object.__setattr__(self, "implements", _builtins.tuple(implements))
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
                self.implements,
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
            and self.implements == __other.implements
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
            or self.implements != __other.implements
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
            self.implements,
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
            __other.implements,
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
            self.implements,
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
            __other.implements,
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
            self.implements,
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
            __other.implements,
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
            self.implements,
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
            __other.implements,
        )

    def __repr__(self):
        return f"DefTemplate(tycon={self.tycon!r}, param={self.param!r}, precond={self.precond!r}, signatories={self.signatories!r}, agreement={self.agreement!r}, choices={self.choices!r}, observers={self.observers!r}, location={self.location!r}, key={self.key!r}, implements={self.implements!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class InterfaceMethod:
    __match_args__ = ("location", "method_interned_name", "type")

    __slots__ = ("location", "method_interned_name", "type")

    def __init__(self, location, method_interned_name, type):
        object.__setattr__(self, "location", location)
        object.__setattr__(self, "method_interned_name", method_interned_name)
        object.__setattr__(self, "type", type)

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash((self.location, self.method_interned_name, self.type))

    def __eq__(self, __other):
        return (
            self.location == __other.location
            and self.method_interned_name == __other.method_interned_name
            and self.type == __other.type
        )

    def __ne__(self, __other):
        return (
            self.location != __other.location
            or self.method_interned_name != __other.method_interned_name
            or self.type != __other.type
        )

    def __lt__(self, __other):
        return (self.location, self.method_interned_name, self.type) < (
            __other.location,
            __other.method_interned_name,
            __other.type,
        )

    def __le__(self, __other):
        return (self.location, self.method_interned_name, self.type) <= (
            __other.location,
            __other.method_interned_name,
            __other.type,
        )

    def __gt__(self, __other):
        return (self.location, self.method_interned_name, self.type) > (
            __other.location,
            __other.method_interned_name,
            __other.type,
        )

    def __ge__(self, __other):
        return (self.location, self.method_interned_name, self.type) >= (
            __other.location,
            __other.method_interned_name,
            __other.type,
        )

    def __repr__(self):
        return f"InterfaceMethod(location={self.location!r}, method_interned_name={self.method_interned_name!r}, type={self.type!r}, )"


# noinspection PyShadowingBuiltins,SpellCheckingInspection
class DefInterface:
    # noinspection PyShadowingBuiltins,SpellCheckingInspection
    class CoImplements:
        __match_args__ = ("template", "body")

        __slots__ = ("template", "body")

        def __init__(self, template, body):
            object.__setattr__(self, "template", template)
            object.__setattr__(self, "body", body)

        def __setattr__(self, name, value):
            raise AttributeError

        def __hash__(self):
            return hash((self.template, self.body))

        def __eq__(self, __other):
            return self.template == __other.template and self.body == __other.body

        def __ne__(self, __other):
            return self.template != __other.template or self.body != __other.body

        def __lt__(self, __other):
            return (self.template, self.body) < (__other.template, __other.body)

        def __le__(self, __other):
            return (self.template, self.body) <= (__other.template, __other.body)

        def __gt__(self, __other):
            return (self.template, self.body) > (__other.template, __other.body)

        def __ge__(self, __other):
            return (self.template, self.body) >= (__other.template, __other.body)

        def __repr__(self):
            return f"DefInterface.CoImplements(template={self.template!r}, body={self.body!r}, )"

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

    __slots__ = (
        "location",
        "tycon",
        "methods",
        "param",
        "choices",
        "co_implements",
        "view",
        "requires",
    )

    def __init__(
        self, location, tycon, methods, param, choices, co_implements, view, requires
    ):
        object.__setattr__(self, "location", location)
        object.__setattr__(self, "tycon", tycon)
        object.__setattr__(self, "methods", _builtins.tuple(methods))
        object.__setattr__(self, "param", param)
        object.__setattr__(self, "choices", _builtins.tuple(choices))
        object.__setattr__(self, "co_implements", _builtins.tuple(co_implements))
        object.__setattr__(self, "view", view)
        object.__setattr__(self, "requires", _builtins.tuple(requires))

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (
                self.location,
                self.tycon,
                self.methods,
                self.param,
                self.choices,
                self.co_implements,
                self.view,
                self.requires,
            )
        )

    def __eq__(self, __other):
        return (
            self.location == __other.location
            and self.tycon == __other.tycon
            and self.methods == __other.methods
            and self.param == __other.param
            and self.choices == __other.choices
            and self.co_implements == __other.co_implements
            and self.view == __other.view
            and self.requires == __other.requires
        )

    def __ne__(self, __other):
        return (
            self.location != __other.location
            or self.tycon != __other.tycon
            or self.methods != __other.methods
            or self.param != __other.param
            or self.choices != __other.choices
            or self.co_implements != __other.co_implements
            or self.view != __other.view
            or self.requires != __other.requires
        )

    def __lt__(self, __other):
        return (
            self.location,
            self.tycon,
            self.methods,
            self.param,
            self.choices,
            self.co_implements,
            self.view,
            self.requires,
        ) < (
            __other.location,
            __other.tycon,
            __other.methods,
            __other.param,
            __other.choices,
            __other.co_implements,
            __other.view,
            __other.requires,
        )

    def __le__(self, __other):
        return (
            self.location,
            self.tycon,
            self.methods,
            self.param,
            self.choices,
            self.co_implements,
            self.view,
            self.requires,
        ) <= (
            __other.location,
            __other.tycon,
            __other.methods,
            __other.param,
            __other.choices,
            __other.co_implements,
            __other.view,
            __other.requires,
        )

    def __gt__(self, __other):
        return (
            self.location,
            self.tycon,
            self.methods,
            self.param,
            self.choices,
            self.co_implements,
            self.view,
            self.requires,
        ) > (
            __other.location,
            __other.tycon,
            __other.methods,
            __other.param,
            __other.choices,
            __other.co_implements,
            __other.view,
            __other.requires,
        )

    def __ge__(self, __other):
        return (
            self.location,
            self.tycon,
            self.methods,
            self.param,
            self.choices,
            self.co_implements,
            self.view,
            self.requires,
        ) >= (
            __other.location,
            __other.tycon,
            __other.methods,
            __other.param,
            __other.choices,
            __other.co_implements,
            __other.view,
            __other.requires,
        )

    def __repr__(self):
        return f"DefInterface(location={self.location!r}, tycon={self.tycon!r}, methods={self.methods!r}, param={self.param!r}, choices={self.choices!r}, co_implements={self.co_implements!r}, view={self.view!r}, requires={self.requires!r}, )"


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
        interface=None,
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
        if interface is not None:
            object.__setattr__(self, "DataCons", ("interface", interface))
            data_cons.append("interface")
        if len(data_cons) == 0:
            raise ValueError("one of must be specified")
        elif len(data_cons) > 1:
            raise ValueError("cannot specify at the same time")

    def data_cons_match(self, record, variant, enum, interface):
        if self.data_cons[0] == "record":
            return record(self.data_cons[1])
        elif self.data_cons[0] == "variant":
            return variant(self.data_cons[1])
        elif self.data_cons[0] == "enum":
            return enum(self.data_cons[1])
        elif self.data_cons[0] == "interface":
            return interface(self.data_cons[1])
        else:
            raise Exception("invalid case")

    def __getattr__(self, name):
        if self.DataCons[0] == name:
            return self.DataCons[1]
        raise AttributeError

    def __setattr__(self, name, value):
        raise AttributeError

    def __hash__(self):
        return hash(
            (self.name, self.params, self.data_cons, self.serializable, self.location)
        )

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
        return (
            self.name,
            self.params,
            self.data_cons,
            self.serializable,
            self.location,
        ) < (
            __other.name,
            __other.params,
            __other.data_cons,
            __other.serializable,
            __other.location,
        )

    def __le__(self, __other):
        return (
            self.name,
            self.params,
            self.data_cons,
            self.serializable,
            self.location,
        ) <= (
            __other.name,
            __other.params,
            __other.data_cons,
            __other.serializable,
            __other.location,
        )

    def __gt__(self, __other):
        return (
            self.name,
            self.params,
            self.data_cons,
            self.serializable,
            self.location,
        ) > (
            __other.name,
            __other.params,
            __other.data_cons,
            __other.serializable,
            __other.location,
        )

    def __ge__(self, __other):
        return (
            self.name,
            self.params,
            self.data_cons,
            self.serializable,
            self.location,
        ) >= (
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
        "interfaces",
    )

    __slots__ = (
        "name",
        "flags",
        "synonyms",
        "data_types",
        "values",
        "templates",
        "exceptions",
        "interfaces",
    )

    def __init__(
        self,
        name,
        flags,
        synonyms,
        data_types,
        values,
        templates,
        exceptions,
        interfaces,
    ):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "flags", flags)
        object.__setattr__(self, "synonyms", _builtins.tuple(synonyms))
        object.__setattr__(self, "data_types", _builtins.tuple(data_types))
        object.__setattr__(self, "values", _builtins.tuple(values))
        object.__setattr__(self, "templates", _builtins.tuple(templates))
        object.__setattr__(self, "exceptions", _builtins.tuple(exceptions))
        object.__setattr__(self, "interfaces", _builtins.tuple(interfaces))

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
                self.interfaces,
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
            and self.interfaces == __other.interfaces
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
            or self.interfaces != __other.interfaces
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
            self.interfaces,
        ) < (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
            __other.interfaces,
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
            self.interfaces,
        ) <= (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
            __other.interfaces,
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
            self.interfaces,
        ) > (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
            __other.interfaces,
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
            self.interfaces,
        ) >= (
            __other.name,
            __other.flags,
            __other.synonyms,
            __other.data_types,
            __other.values,
            __other.templates,
            __other.exceptions,
            __other.interfaces,
        )

    def __repr__(self):
        return f"Module(name={self.name!r}, flags={self.flags!r}, synonyms={self.synonyms!r}, data_types={self.data_types!r}, values={self.values!r}, templates={self.templates!r}, exceptions={self.exceptions!r}, interfaces={self.interfaces!r}, )"


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
