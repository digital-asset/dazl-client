class Unit:  # Product
    """
    Canonical encoding in one-ofs for cases that carry no meaningful
     values.
    """
    __slots__ = ()

    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

# Package reference
PackageRef = NewType("PackageRef", str)

# A `name`, e.g. Util.Either.isLeft
#  *Available in version < 1.7*
DottedName = NewType("DottedName", str)

# A fully qualified module reference
ModuleRef = NewType("ModuleRef", str)

class TypeConName:  # Product
    """
    A fully qualified reference to a type constructor name.
    """
    __slots__ = "_module", "_name"
    @property
    def module(self) -> "ModuleRef":
        return self._module

    @property
    def name(self) -> "DottedName":
        return self._name


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class TypeSynName:  # Product
    """
    A fully qualified reference to a type synonym name.
     *Available in versions >= 1.8*
    """
    __slots__ = "_module", "_name"
    @property
    def module(self) -> "ModuleRef":
        return self._module

    @property
    def name(self) -> "DottedName":
        return self._name


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class ValName:  # Product
    """
    A fully qualified reference to a value definition.
    """
    __slots__ = "_module", "_name"
    @property
    def module(self) -> "ModuleRef":
        return self._module

    @property
    def name(self) -> "DottedName":
        return self._name


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class FieldWithType:  # Product
    """
    A field name definition in a record or a variant associated with a type.
    """
    __slots__ = "_field", "_type"
    @property
    def field(self) -> str:
        return self._field

    @property
    def type(self) -> "Type":
        return self._type


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class VarWithType:  # Product
    """
    Binder associated with a type.
    """
    __slots__ = "_var", "_type"
    @property
    def var(self) -> str:
        return self._var

    @property
    def type(self) -> "Type":
        return self._type


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class TypeVarWithKind:  # Product
    """
    Type binder associated with a kind.
    """
    __slots__ = "_var", "_kind"
    @property
    def var(self) -> str:
        return self._var

    @property
    def kind(self) -> "Kind":
        return self._kind


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class FieldWithExpr:  # Product
    """
    A field in a record with its value.
    """
    __slots__ = "_field", "_expr"
    @property
    def field(self) -> str:
        return self._field

    @property
    def expr(self) -> "Expr":
        return self._expr


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Binding:  # Product
    """
    A binding of a typed binder to an expression
    """
    __slots__ = "_binder", "_bound"
    @property
    def binder(self) -> "VarWithType":
        return self._binder

    @property
    def bound(self) -> "Expr":
        return self._bound


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Kind:  # Sum
    """
    Kinds
    """
    __slots__ = "__ctor", "__value"
    def __init__(self, star = MISSING, arrow = MISSING, nat = MISSING):
        if star is not MISSING:
            object.__setattr__(self, "__ctor", "star")
            object.__setattr__(self, "__value", star)
        if arrow is not MISSING:
            object.__setattr__(self, "__ctor", "arrow")
            object.__setattr__(self, "__value", arrow)
        if nat is not MISSING:
            object.__setattr__(self, "__ctor", "nat")
            object.__setattr__(self, "__value", nat)
    @property
    def star(self) -> "Optional[Unit]":
        return self.__value if self.__ctor == "star" else None

    @property
    def arrow(self) -> "Optional[Kind.Arrow]":
        return self.__value if self.__ctor == "arrow" else None

    @property
    def nat(self) -> "Optional[Unit]":
        return self.__value if self.__ctor == "nat" else None

    def match(self,
            star: "Callable[[Unit], T]",
            arrow: "Callable[[Unit], T]",
            nat: "Callable[[Unit], T]",
            ) -> 'T':
        if self.__ctor == "star":
            return star(self.__value)
        elif self.__ctor == "arrow":
            return arrow(self.__value)
        elif self.__ctor == "nat":
            return nat(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Arrow:  # Product
        __slots__ = "_params", "_result"
        @property
        def params(self) -> "Sequence[Kind]":
            return self._params

        @property
        def result(self) -> "Kind":
            return self._result


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class Type:  # Sum
    """
    Types
    """
    __slots__ = "__ctor", "__value"
    def __init__(self, var = MISSING, con = MISSING, prim = MISSING, fun = MISSING, forall = MISSING, struct = MISSING, nat = MISSING, syn = MISSING):
        if var is not MISSING:
            object.__setattr__(self, "__ctor", "var")
            object.__setattr__(self, "__value", var)
        if con is not MISSING:
            object.__setattr__(self, "__ctor", "con")
            object.__setattr__(self, "__value", con)
        if prim is not MISSING:
            object.__setattr__(self, "__ctor", "prim")
            object.__setattr__(self, "__value", prim)
        if fun is not MISSING:
            object.__setattr__(self, "__ctor", "fun")
            object.__setattr__(self, "__value", fun)
        if forall is not MISSING:
            object.__setattr__(self, "__ctor", "forall")
            object.__setattr__(self, "__value", forall)
        if struct is not MISSING:
            object.__setattr__(self, "__ctor", "struct")
            object.__setattr__(self, "__value", struct)
        if nat is not MISSING:
            object.__setattr__(self, "__ctor", "nat")
            object.__setattr__(self, "__value", nat)
        if syn is not MISSING:
            object.__setattr__(self, "__ctor", "syn")
            object.__setattr__(self, "__value", syn)
    @property
    def var(self) -> "Optional[Type.Var]":
        return self.__value if self.__ctor == "var" else None

    @property
    def con(self) -> "Optional[Type.Con]":
        return self.__value if self.__ctor == "con" else None

    @property
    def prim(self) -> "Optional[Type.Prim]":
        return self.__value if self.__ctor == "prim" else None

    @property
    def fun(self) -> "Optional[Type.Fun]":
        return self.__value if self.__ctor == "fun" else None

    @property
    def forall(self) -> "Optional[Type.Forall]":
        return self.__value if self.__ctor == "forall" else None

    @property
    def struct(self) -> "Optional[Type.Struct]":
        return self.__value if self.__ctor == "struct" else None

    @property
    def nat(self) -> "Optional[int64]":
        return self.__value if self.__ctor == "nat" else None

    @property
    def syn(self) -> "Optional[Type.Syn]":
        return self.__value if self.__ctor == "syn" else None

    def match(self,
            var: "Callable[[Type.Syn], T]",
            con: "Callable[[Type.Syn], T]",
            prim: "Callable[[Type.Syn], T]",
            fun: "Callable[[Type.Syn], T]",
            forall: "Callable[[Type.Syn], T]",
            struct: "Callable[[Type.Syn], T]",
            nat: "Callable[[Type.Syn], T]",
            syn: "Callable[[Type.Syn], T]",
            ) -> 'T':
        if self.__ctor == "var":
            return var(self.__value)
        elif self.__ctor == "con":
            return con(self.__value)
        elif self.__ctor == "prim":
            return prim(self.__value)
        elif self.__ctor == "fun":
            return fun(self.__value)
        elif self.__ctor == "forall":
            return forall(self.__value)
        elif self.__ctor == "struct":
            return struct(self.__value)
        elif self.__ctor == "nat":
            return nat(self.__value)
        elif self.__ctor == "syn":
            return syn(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Var:  # Product
        __slots__ = "_var", "_args"
        @property
        def var(self) -> str:
            return self._var

        @property
        def args(self) -> "Sequence[Type]":
            return self._args


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Con:  # Product
        __slots__ = "_tycon", "_args"
        @property
        def tycon(self) -> "TypeConName":
            return self._tycon

        @property
        def args(self) -> "Sequence[Type]":
            return self._args


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Syn:  # Product
        __slots__ = "_tysyn", "_args"
        @property
        def tysyn(self) -> "TypeSynName":
            return self._tysyn

        @property
        def args(self) -> "Sequence[Type]":
            return self._args


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Prim:  # Product
        __slots__ = "_prim", "_args"
        @property
        def prim(self) -> "PrimType":
            return self._prim

        @property
        def args(self) -> "Sequence[Type]":
            return self._args


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Fun:  # Product
        __slots__ = "_params", "_result"
        @property
        def params(self) -> "Sequence[Type]":
            return self._params

        @property
        def result(self) -> "Type":
            return self._result


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Forall:  # Product
        __slots__ = "_vars", "_body"
        @property
        def vars(self) -> "Sequence[TypeVarWithKind]":
            return self._vars

        @property
        def body(self) -> "Type":
            return self._body


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Struct:  # Product
        __slots__ = "_fields",
        @property
        def fields(self) -> "Sequence[FieldWithType]":
            return self._fields


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class PrimLit:  # Sum
    """
    Builtin literals
     FixMe: Renamed
    """
    __slots__ = "__ctor", "__value"
    def __init__(self, int64 = MISSING, decimal = MISSING, numeric = MISSING, text = MISSING, timestamp = MISSING, party = MISSING, date = MISSING):
        if int64 is not MISSING:
            object.__setattr__(self, "__ctor", "int64")
            object.__setattr__(self, "__value", int64)
        if decimal is not MISSING:
            object.__setattr__(self, "__ctor", "decimal")
            object.__setattr__(self, "__value", decimal)
        if numeric is not MISSING:
            object.__setattr__(self, "__ctor", "numeric")
            object.__setattr__(self, "__value", numeric)
        if text is not MISSING:
            object.__setattr__(self, "__ctor", "text")
            object.__setattr__(self, "__value", text)
        if timestamp is not MISSING:
            object.__setattr__(self, "__ctor", "timestamp")
            object.__setattr__(self, "__value", timestamp)
        if party is not MISSING:
            object.__setattr__(self, "__ctor", "party")
            object.__setattr__(self, "__value", party)
        if date is not MISSING:
            object.__setattr__(self, "__ctor", "date")
            object.__setattr__(self, "__value", date)
    @property
    def int64(self) -> "Optional[int64]":
        return self.__value if self.__ctor == "int64" else None

    @property
    def decimal(self) -> "Optional[str]":
        return self.__value if self.__ctor == "decimal" else None

    @property
    def numeric(self) -> "Optional[str]":
        return self.__value if self.__ctor == "numeric" else None

    @property
    def text(self) -> "Optional[str]":
        return self.__value if self.__ctor == "text" else None

    @property
    def timestamp(self) -> "Optional[fixed64]":
        return self.__value if self.__ctor == "timestamp" else None

    @property
    def party(self) -> "Optional[str]":
        return self.__value if self.__ctor == "party" else None

    @property
    def date(self) -> "Optional[int32]":
        return self.__value if self.__ctor == "date" else None

    def match(self,
            int64: "Callable[[int32], T]",
            decimal: "Callable[[int32], T]",
            numeric: "Callable[[int32], T]",
            text: "Callable[[int32], T]",
            timestamp: "Callable[[int32], T]",
            party: "Callable[[int32], T]",
            date: "Callable[[int32], T]",
            ) -> 'T':
        if self.__ctor == "int64":
            return int64(self.__value)
        elif self.__ctor == "decimal":
            return decimal(self.__value)
        elif self.__ctor == "numeric":
            return numeric(self.__value)
        elif self.__ctor == "text":
            return text(self.__value)
        elif self.__ctor == "timestamp":
            return timestamp(self.__value)
        elif self.__ctor == "party":
            return party(self.__value)
        elif self.__ctor == "date":
            return date(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Location:  # Product
    """
    Source code locations
    """
    __slots__ = "_module", "_range"
    @property
    def module(self) -> "ModuleRef":
        return self._module

    @property
    def range(self) -> "Location.Range":
        return self._range


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Range:  # Product
        __slots__ = "_start_line", "_start_col", "_end_line", "_end_col"
        @property
        def start_line(self) -> "int32":
            return self._start_line

        @property
        def start_col(self) -> "int32":
            return self._start_col

        @property
        def end_line(self) -> "int32":
            return self._end_line

        @property
        def end_col(self) -> "int32":
            return self._end_col


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class Expr:  # Sum
    """
    Expressions
    """
    __slots__ = "__ctor", "__value", "_location"
    def __init__(self, location, var = MISSING, val = MISSING, builtin = MISSING, prim_con = MISSING, prim_lit = MISSING, rec_con = MISSING, rec_proj = MISSING, rec_upd = MISSING, variant_con = MISSING, enum_con = MISSING, struct_con = MISSING, struct_proj = MISSING, struct_upd = MISSING, app = MISSING, ty_app = MISSING, abs = MISSING, ty_abs = MISSING, case = MISSING, let = MISSING, nil = MISSING, cons = MISSING, update = MISSING, scenario = MISSING, optional_none = MISSING, optional_some = MISSING, to_any = MISSING, from_any = MISSING, type_rep = MISSING):
        object.__setattr__(self, "_location", location)
        if var is not MISSING:
            object.__setattr__(self, "__ctor", "var")
            object.__setattr__(self, "__value", var)
        if val is not MISSING:
            object.__setattr__(self, "__ctor", "val")
            object.__setattr__(self, "__value", val)
        if builtin is not MISSING:
            object.__setattr__(self, "__ctor", "builtin")
            object.__setattr__(self, "__value", builtin)
        if prim_con is not MISSING:
            object.__setattr__(self, "__ctor", "prim_con")
            object.__setattr__(self, "__value", prim_con)
        if prim_lit is not MISSING:
            object.__setattr__(self, "__ctor", "prim_lit")
            object.__setattr__(self, "__value", prim_lit)
        if rec_con is not MISSING:
            object.__setattr__(self, "__ctor", "rec_con")
            object.__setattr__(self, "__value", rec_con)
        if rec_proj is not MISSING:
            object.__setattr__(self, "__ctor", "rec_proj")
            object.__setattr__(self, "__value", rec_proj)
        if rec_upd is not MISSING:
            object.__setattr__(self, "__ctor", "rec_upd")
            object.__setattr__(self, "__value", rec_upd)
        if variant_con is not MISSING:
            object.__setattr__(self, "__ctor", "variant_con")
            object.__setattr__(self, "__value", variant_con)
        if enum_con is not MISSING:
            object.__setattr__(self, "__ctor", "enum_con")
            object.__setattr__(self, "__value", enum_con)
        if struct_con is not MISSING:
            object.__setattr__(self, "__ctor", "struct_con")
            object.__setattr__(self, "__value", struct_con)
        if struct_proj is not MISSING:
            object.__setattr__(self, "__ctor", "struct_proj")
            object.__setattr__(self, "__value", struct_proj)
        if struct_upd is not MISSING:
            object.__setattr__(self, "__ctor", "struct_upd")
            object.__setattr__(self, "__value", struct_upd)
        if app is not MISSING:
            object.__setattr__(self, "__ctor", "app")
            object.__setattr__(self, "__value", app)
        if ty_app is not MISSING:
            object.__setattr__(self, "__ctor", "ty_app")
            object.__setattr__(self, "__value", ty_app)
        if abs is not MISSING:
            object.__setattr__(self, "__ctor", "abs")
            object.__setattr__(self, "__value", abs)
        if ty_abs is not MISSING:
            object.__setattr__(self, "__ctor", "ty_abs")
            object.__setattr__(self, "__value", ty_abs)
        if case is not MISSING:
            object.__setattr__(self, "__ctor", "case")
            object.__setattr__(self, "__value", case)
        if let is not MISSING:
            object.__setattr__(self, "__ctor", "let")
            object.__setattr__(self, "__value", let)
        if nil is not MISSING:
            object.__setattr__(self, "__ctor", "nil")
            object.__setattr__(self, "__value", nil)
        if cons is not MISSING:
            object.__setattr__(self, "__ctor", "cons")
            object.__setattr__(self, "__value", cons)
        if update is not MISSING:
            object.__setattr__(self, "__ctor", "update")
            object.__setattr__(self, "__value", update)
        if scenario is not MISSING:
            object.__setattr__(self, "__ctor", "scenario")
            object.__setattr__(self, "__value", scenario)
        if optional_none is not MISSING:
            object.__setattr__(self, "__ctor", "optional_none")
            object.__setattr__(self, "__value", optional_none)
        if optional_some is not MISSING:
            object.__setattr__(self, "__ctor", "optional_some")
            object.__setattr__(self, "__value", optional_some)
        if to_any is not MISSING:
            object.__setattr__(self, "__ctor", "to_any")
            object.__setattr__(self, "__value", to_any)
        if from_any is not MISSING:
            object.__setattr__(self, "__ctor", "from_any")
            object.__setattr__(self, "__value", from_any)
        if type_rep is not MISSING:
            object.__setattr__(self, "__ctor", "type_rep")
            object.__setattr__(self, "__value", type_rep)
    @property
    def location(self) -> "Location":
        return self._location

    @property
    def var(self) -> "Optional[str]":
        return self.__value if self.__ctor == "var" else None

    @property
    def val(self) -> "Optional[ValName]":
        return self.__value if self.__ctor == "val" else None

    @property
    def builtin(self) -> "Optional[BuiltinFunction]":
        return self.__value if self.__ctor == "builtin" else None

    @property
    def prim_con(self) -> "Optional[PrimCon]":
        return self.__value if self.__ctor == "prim_con" else None

    @property
    def prim_lit(self) -> "Optional[PrimLit]":
        return self.__value if self.__ctor == "prim_lit" else None

    @property
    def rec_con(self) -> "Optional[Expr.RecCon]":
        return self.__value if self.__ctor == "rec_con" else None

    @property
    def rec_proj(self) -> "Optional[Expr.RecProj]":
        return self.__value if self.__ctor == "rec_proj" else None

    @property
    def rec_upd(self) -> "Optional[Expr.RecUpd]":
        return self.__value if self.__ctor == "rec_upd" else None

    @property
    def variant_con(self) -> "Optional[Expr.VariantCon]":
        return self.__value if self.__ctor == "variant_con" else None

    @property
    def enum_con(self) -> "Optional[Expr.EnumCon]":
        return self.__value if self.__ctor == "enum_con" else None

    @property
    def struct_con(self) -> "Optional[Expr.StructCon]":
        return self.__value if self.__ctor == "struct_con" else None

    @property
    def struct_proj(self) -> "Optional[Expr.StructProj]":
        return self.__value if self.__ctor == "struct_proj" else None

    @property
    def struct_upd(self) -> "Optional[Expr.StructUpd]":
        return self.__value if self.__ctor == "struct_upd" else None

    @property
    def app(self) -> "Optional[Expr.App]":
        return self.__value if self.__ctor == "app" else None

    @property
    def ty_app(self) -> "Optional[Expr.TyApp]":
        return self.__value if self.__ctor == "ty_app" else None

    @property
    def abs(self) -> "Optional[Expr.Abs]":
        return self.__value if self.__ctor == "abs" else None

    @property
    def ty_abs(self) -> "Optional[Expr.TyAbs]":
        return self.__value if self.__ctor == "ty_abs" else None

    @property
    def case(self) -> "Optional[Case]":
        return self.__value if self.__ctor == "case" else None

    @property
    def let(self) -> "Optional[Block]":
        return self.__value if self.__ctor == "let" else None

    @property
    def nil(self) -> "Optional[Expr.Nil]":
        return self.__value if self.__ctor == "nil" else None

    @property
    def cons(self) -> "Optional[Expr.Cons]":
        return self.__value if self.__ctor == "cons" else None

    @property
    def update(self) -> "Optional[Update]":
        return self.__value if self.__ctor == "update" else None

    @property
    def scenario(self) -> "Optional[Scenario]":
        return self.__value if self.__ctor == "scenario" else None

    @property
    def optional_none(self) -> "Optional[Expr.OptionalNone]":
        return self.__value if self.__ctor == "optional_none" else None

    @property
    def optional_some(self) -> "Optional[Expr.OptionalSome]":
        return self.__value if self.__ctor == "optional_some" else None

    @property
    def to_any(self) -> "Optional[Expr.ToAny]":
        return self.__value if self.__ctor == "to_any" else None

    @property
    def from_any(self) -> "Optional[Expr.FromAny]":
        return self.__value if self.__ctor == "from_any" else None

    @property
    def type_rep(self) -> "Optional[Type]":
        return self.__value if self.__ctor == "type_rep" else None

    def match(self,
            var: "Callable[[Type], T]",
            val: "Callable[[Type], T]",
            builtin: "Callable[[Type], T]",
            prim_con: "Callable[[Type], T]",
            prim_lit: "Callable[[Type], T]",
            rec_con: "Callable[[Type], T]",
            rec_proj: "Callable[[Type], T]",
            rec_upd: "Callable[[Type], T]",
            variant_con: "Callable[[Type], T]",
            enum_con: "Callable[[Type], T]",
            struct_con: "Callable[[Type], T]",
            struct_proj: "Callable[[Type], T]",
            struct_upd: "Callable[[Type], T]",
            app: "Callable[[Type], T]",
            ty_app: "Callable[[Type], T]",
            abs: "Callable[[Type], T]",
            ty_abs: "Callable[[Type], T]",
            case: "Callable[[Type], T]",
            let: "Callable[[Type], T]",
            nil: "Callable[[Type], T]",
            cons: "Callable[[Type], T]",
            update: "Callable[[Type], T]",
            scenario: "Callable[[Type], T]",
            optional_none: "Callable[[Type], T]",
            optional_some: "Callable[[Type], T]",
            to_any: "Callable[[Type], T]",
            from_any: "Callable[[Type], T]",
            type_rep: "Callable[[Type], T]",
            ) -> 'T':
        if self.__ctor == "var":
            return var(self.__value)
        elif self.__ctor == "val":
            return val(self.__value)
        elif self.__ctor == "builtin":
            return builtin(self.__value)
        elif self.__ctor == "prim_con":
            return prim_con(self.__value)
        elif self.__ctor == "prim_lit":
            return prim_lit(self.__value)
        elif self.__ctor == "rec_con":
            return rec_con(self.__value)
        elif self.__ctor == "rec_proj":
            return rec_proj(self.__value)
        elif self.__ctor == "rec_upd":
            return rec_upd(self.__value)
        elif self.__ctor == "variant_con":
            return variant_con(self.__value)
        elif self.__ctor == "enum_con":
            return enum_con(self.__value)
        elif self.__ctor == "struct_con":
            return struct_con(self.__value)
        elif self.__ctor == "struct_proj":
            return struct_proj(self.__value)
        elif self.__ctor == "struct_upd":
            return struct_upd(self.__value)
        elif self.__ctor == "app":
            return app(self.__value)
        elif self.__ctor == "ty_app":
            return ty_app(self.__value)
        elif self.__ctor == "abs":
            return abs(self.__value)
        elif self.__ctor == "ty_abs":
            return ty_abs(self.__value)
        elif self.__ctor == "case":
            return case(self.__value)
        elif self.__ctor == "let":
            return let(self.__value)
        elif self.__ctor == "nil":
            return nil(self.__value)
        elif self.__ctor == "cons":
            return cons(self.__value)
        elif self.__ctor == "update":
            return update(self.__value)
        elif self.__ctor == "scenario":
            return scenario(self.__value)
        elif self.__ctor == "optional_none":
            return optional_none(self.__value)
        elif self.__ctor == "optional_some":
            return optional_some(self.__value)
        elif self.__ctor == "to_any":
            return to_any(self.__value)
        elif self.__ctor == "from_any":
            return from_any(self.__value)
        elif self.__ctor == "type_rep":
            return type_rep(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class RecCon:  # Product
        __slots__ = "_tycon", "_fields"
        @property
        def tycon(self) -> "Type.Con":
            return self._tycon

        @property
        def fields(self) -> "Sequence[FieldWithExpr]":
            return self._fields


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class RecProj:  # Product
        __slots__ = "_tycon", "_field", "_record"
        @property
        def tycon(self) -> "Type.Con":
            return self._tycon

        @property
        def field(self) -> str:
            return self._field

        @property
        def record(self) -> "Expr":
            return self._record


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class RecUpd:  # Product
        __slots__ = "_tycon", "_field", "_record", "_update"
        @property
        def tycon(self) -> "Type.Con":
            return self._tycon

        @property
        def field(self) -> str:
            return self._field

        @property
        def record(self) -> "Expr":
            return self._record

        @property
        def update(self) -> "Expr":
            return self._update


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class VariantCon:  # Product
        __slots__ = "_tycon", "_variant_con", "_variant_arg"
        @property
        def tycon(self) -> "Type.Con":
            return self._tycon

        @property
        def variant_con(self) -> str:
            return self._variant_con

        @property
        def variant_arg(self) -> "Expr":
            return self._variant_arg


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class EnumCon:  # Product
        __slots__ = "_tycon", "_enum_con"
        @property
        def tycon(self) -> "TypeConName":
            return self._tycon

        @property
        def enum_con(self) -> str:
            return self._enum_con


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class StructCon:  # Product
        __slots__ = "_fields",
        @property
        def fields(self) -> "Sequence[FieldWithExpr]":
            return self._fields


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class StructProj:  # Product
        __slots__ = "_field", "_struct"
        @property
        def field(self) -> str:
            return self._field

        @property
        def struct(self) -> "Expr":
            return self._struct


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class StructUpd:  # Product
        __slots__ = "_field", "_struct", "_update"
        @property
        def field(self) -> str:
            return self._field

        @property
        def struct(self) -> "Expr":
            return self._struct

        @property
        def update(self) -> "Expr":
            return self._update


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class App:  # Product
        __slots__ = "_fun", "_args"
        @property
        def fun(self) -> "Expr":
            return self._fun

        @property
        def args(self) -> "Sequence[Expr]":
            return self._args


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class TyApp:  # Product
        __slots__ = "_expr", "_types"
        @property
        def expr(self) -> "Expr":
            return self._expr

        @property
        def types(self) -> "Sequence[Type]":
            return self._types


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Abs:  # Product
        __slots__ = "_param", "_body"
        @property
        def param(self) -> "Sequence[VarWithType]":
            return self._param

        @property
        def body(self) -> "Expr":
            return self._body


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class TyAbs:  # Product
        __slots__ = "_param", "_body"
        @property
        def param(self) -> "Sequence[TypeVarWithKind]":
            return self._param

        @property
        def body(self) -> "Expr":
            return self._body


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Nil:  # Product
        __slots__ = "_type",
        @property
        def type(self) -> "Type":
            return self._type


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Cons:  # Product
        __slots__ = "_type", "_front", "_tail"
        @property
        def type(self) -> "Type":
            return self._type

        @property
        def front(self) -> "Sequence[Expr]":
            return self._front

        @property
        def tail(self) -> "Expr":
            return self._tail


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class OptionalNone:  # Product
        __slots__ = "_type",
        @property
        def type(self) -> "Type":
            return self._type


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class OptionalSome:  # Product
        __slots__ = "_type", "_body"
        @property
        def type(self) -> "Type":
            return self._type

        @property
        def body(self) -> "Expr":
            return self._body


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class ToAny:  # Product
        __slots__ = "_type", "_expr"
        @property
        def type(self) -> "Type":
            return self._type

        @property
        def expr(self) -> "Expr":
            return self._expr


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class FromAny:  # Product
        __slots__ = "_type", "_expr"
        @property
        def type(self) -> "Type":
            return self._type

        @property
        def expr(self) -> "Expr":
            return self._expr


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class CaseAlt:  # Sum
    """
    Case alternative
    """
    __slots__ = "__ctor", "__value", "_body"
    def __init__(self, body, default = MISSING, variant = MISSING, prim_con = MISSING, nil = MISSING, cons = MISSING, optional_none = MISSING, optional_some = MISSING, enum = MISSING):
        if default is not MISSING:
            object.__setattr__(self, "__ctor", "default")
            object.__setattr__(self, "__value", default)
        if variant is not MISSING:
            object.__setattr__(self, "__ctor", "variant")
            object.__setattr__(self, "__value", variant)
        if prim_con is not MISSING:
            object.__setattr__(self, "__ctor", "prim_con")
            object.__setattr__(self, "__value", prim_con)
        if nil is not MISSING:
            object.__setattr__(self, "__ctor", "nil")
            object.__setattr__(self, "__value", nil)
        if cons is not MISSING:
            object.__setattr__(self, "__ctor", "cons")
            object.__setattr__(self, "__value", cons)
        if optional_none is not MISSING:
            object.__setattr__(self, "__ctor", "optional_none")
            object.__setattr__(self, "__value", optional_none)
        if optional_some is not MISSING:
            object.__setattr__(self, "__ctor", "optional_some")
            object.__setattr__(self, "__value", optional_some)
        if enum is not MISSING:
            object.__setattr__(self, "__ctor", "enum")
            object.__setattr__(self, "__value", enum)
        object.__setattr__(self, "_body", body)
    @property
    def default(self) -> "Optional[Unit]":
        return self.__value if self.__ctor == "default" else None

    @property
    def variant(self) -> "Optional[CaseAlt.Variant]":
        return self.__value if self.__ctor == "variant" else None

    @property
    def prim_con(self) -> "Optional[PrimCon]":
        return self.__value if self.__ctor == "prim_con" else None

    @property
    def nil(self) -> "Optional[Unit]":
        return self.__value if self.__ctor == "nil" else None

    @property
    def cons(self) -> "Optional[CaseAlt.Cons]":
        return self.__value if self.__ctor == "cons" else None

    @property
    def optional_none(self) -> "Optional[Unit]":
        return self.__value if self.__ctor == "optional_none" else None

    @property
    def optional_some(self) -> "Optional[CaseAlt.OptionalSome]":
        return self.__value if self.__ctor == "optional_some" else None

    @property
    def enum(self) -> "Optional[CaseAlt.Enum]":
        return self.__value if self.__ctor == "enum" else None

    @property
    def body(self) -> "Expr":
        return self._body

    def match(self,
            default: "Callable[[Expr], T]",
            variant: "Callable[[Expr], T]",
            prim_con: "Callable[[Expr], T]",
            nil: "Callable[[Expr], T]",
            cons: "Callable[[Expr], T]",
            optional_none: "Callable[[Expr], T]",
            optional_some: "Callable[[Expr], T]",
            enum: "Callable[[Expr], T]",
            ) -> 'T':
        if self.__ctor == "default":
            return default(self.__value)
        elif self.__ctor == "variant":
            return variant(self.__value)
        elif self.__ctor == "prim_con":
            return prim_con(self.__value)
        elif self.__ctor == "nil":
            return nil(self.__value)
        elif self.__ctor == "cons":
            return cons(self.__value)
        elif self.__ctor == "optional_none":
            return optional_none(self.__value)
        elif self.__ctor == "optional_some":
            return optional_some(self.__value)
        elif self.__ctor == "enum":
            return enum(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Variant:  # Product
        __slots__ = "_con", "_variant", "_binder"
        @property
        def con(self) -> "TypeConName":
            return self._con

        @property
        def variant(self) -> str:
            return self._variant

        @property
        def binder(self) -> str:
            return self._binder


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Enum:  # Product
        __slots__ = "_con", "_constructor"
        @property
        def con(self) -> "TypeConName":
            return self._con

        @property
        def constructor(self) -> str:
            return self._constructor


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Cons:  # Product
        __slots__ = "_var_head", "_var_tail"
        @property
        def var_head(self) -> str:
            return self._var_head

        @property
        def var_tail(self) -> str:
            return self._var_tail


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class OptionalSome:  # Product
        __slots__ = "_var_body",
        @property
        def var_body(self) -> str:
            return self._var_body


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class Case:  # Product
    __slots__ = "_scrut", "_alts"
    @property
    def scrut(self) -> "Expr":
        return self._scrut

    @property
    def alts(self) -> "Sequence[CaseAlt]":
        return self._alts


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Block:  # Product
    """
    A block of bindings and an expression.
     Encodes a sequence of binds in e.g. a let or update block.
    """
    __slots__ = "_bindings", "_body"
    @property
    def bindings(self) -> "Sequence[Binding]":
        return self._bindings

    @property
    def body(self) -> "Expr":
        return self._body


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Pure:  # Product
    """
    A Pure statement either scenario or update
    """
    __slots__ = "_type", "_expr"
    @property
    def type(self) -> "Type":
        return self._type

    @property
    def expr(self) -> "Expr":
        return self._expr


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Update:  # Sum
    __slots__ = "__ctor", "__value"
    def __init__(self, pure = MISSING, block = MISSING, create = MISSING, exercise = MISSING, fetch = MISSING, get_time = MISSING, lookup_by_key = MISSING, fetch_by_key = MISSING, embed_expr = MISSING):
        if pure is not MISSING:
            object.__setattr__(self, "__ctor", "pure")
            object.__setattr__(self, "__value", pure)
        if block is not MISSING:
            object.__setattr__(self, "__ctor", "block")
            object.__setattr__(self, "__value", block)
        if create is not MISSING:
            object.__setattr__(self, "__ctor", "create")
            object.__setattr__(self, "__value", create)
        if exercise is not MISSING:
            object.__setattr__(self, "__ctor", "exercise")
            object.__setattr__(self, "__value", exercise)
        if fetch is not MISSING:
            object.__setattr__(self, "__ctor", "fetch")
            object.__setattr__(self, "__value", fetch)
        if get_time is not MISSING:
            object.__setattr__(self, "__ctor", "get_time")
            object.__setattr__(self, "__value", get_time)
        if lookup_by_key is not MISSING:
            object.__setattr__(self, "__ctor", "lookup_by_key")
            object.__setattr__(self, "__value", lookup_by_key)
        if fetch_by_key is not MISSING:
            object.__setattr__(self, "__ctor", "fetch_by_key")
            object.__setattr__(self, "__value", fetch_by_key)
        if embed_expr is not MISSING:
            object.__setattr__(self, "__ctor", "embed_expr")
            object.__setattr__(self, "__value", embed_expr)
    @property
    def pure(self) -> "Optional[Pure]":
        return self.__value if self.__ctor == "pure" else None

    @property
    def block(self) -> "Optional[Block]":
        return self.__value if self.__ctor == "block" else None

    @property
    def create(self) -> "Optional[Update.Create]":
        return self.__value if self.__ctor == "create" else None

    @property
    def exercise(self) -> "Optional[Update.Exercise]":
        return self.__value if self.__ctor == "exercise" else None

    @property
    def fetch(self) -> "Optional[Update.Fetch]":
        return self.__value if self.__ctor == "fetch" else None

    @property
    def get_time(self) -> "Optional[Unit]":
        return self.__value if self.__ctor == "get_time" else None

    @property
    def lookup_by_key(self) -> "Optional[Update.RetrieveByKey]":
        return self.__value if self.__ctor == "lookup_by_key" else None

    @property
    def fetch_by_key(self) -> "Optional[Update.RetrieveByKey]":
        return self.__value if self.__ctor == "fetch_by_key" else None

    @property
    def embed_expr(self) -> "Optional[Update.EmbedExpr]":
        return self.__value if self.__ctor == "embed_expr" else None

    def match(self,
            pure: "Callable[[Update.EmbedExpr], T]",
            block: "Callable[[Update.EmbedExpr], T]",
            create: "Callable[[Update.EmbedExpr], T]",
            exercise: "Callable[[Update.EmbedExpr], T]",
            fetch: "Callable[[Update.EmbedExpr], T]",
            get_time: "Callable[[Update.EmbedExpr], T]",
            lookup_by_key: "Callable[[Update.EmbedExpr], T]",
            fetch_by_key: "Callable[[Update.EmbedExpr], T]",
            embed_expr: "Callable[[Update.EmbedExpr], T]",
            ) -> 'T':
        if self.__ctor == "pure":
            return pure(self.__value)
        elif self.__ctor == "block":
            return block(self.__value)
        elif self.__ctor == "create":
            return create(self.__value)
        elif self.__ctor == "exercise":
            return exercise(self.__value)
        elif self.__ctor == "fetch":
            return fetch(self.__value)
        elif self.__ctor == "get_time":
            return get_time(self.__value)
        elif self.__ctor == "lookup_by_key":
            return lookup_by_key(self.__value)
        elif self.__ctor == "fetch_by_key":
            return fetch_by_key(self.__value)
        elif self.__ctor == "embed_expr":
            return embed_expr(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Create:  # Product
        __slots__ = "_template", "_expr"
        @property
        def template(self) -> "TypeConName":
            return self._template

        @property
        def expr(self) -> "Expr":
            return self._expr


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Exercise:  # Product
        __slots__ = "_template", "_choice", "_cid", "_actor", "_arg"
        @property
        def template(self) -> "TypeConName":
            return self._template

        @property
        def choice(self) -> str:
            return self._choice

        @property
        def cid(self) -> "Expr":
            return self._cid

        @property
        def actor(self) -> "Expr":
            return self._actor

        @property
        def arg(self) -> "Expr":
            return self._arg


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Fetch:  # Product
        __slots__ = "_template", "_cid"
        @property
        def template(self) -> "TypeConName":
            return self._template

        @property
        def cid(self) -> "Expr":
            return self._cid


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class EmbedExpr:  # Product
        __slots__ = "_type", "_body"
        @property
        def type(self) -> "Type":
            return self._type

        @property
        def body(self) -> "Expr":
            return self._body


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class RetrieveByKey:  # Product
        __slots__ = "_template", "_key"
        @property
        def template(self) -> "TypeConName":
            return self._template

        @property
        def key(self) -> "Expr":
            return self._key


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class Scenario:  # Sum
    """
    Scenario actions
    """
    __slots__ = "__ctor", "__value"
    def __init__(self, pure = MISSING, block = MISSING, commit = MISSING, mustFailAt = MISSING, pass_ = MISSING, get_time = MISSING, get_party = MISSING, embed_expr = MISSING):
        if pure is not MISSING:
            object.__setattr__(self, "__ctor", "pure")
            object.__setattr__(self, "__value", pure)
        if block is not MISSING:
            object.__setattr__(self, "__ctor", "block")
            object.__setattr__(self, "__value", block)
        if commit is not MISSING:
            object.__setattr__(self, "__ctor", "commit")
            object.__setattr__(self, "__value", commit)
        if mustFailAt is not MISSING:
            object.__setattr__(self, "__ctor", "mustFailAt")
            object.__setattr__(self, "__value", mustFailAt)
        if pass_ is not MISSING:
            object.__setattr__(self, "__ctor", "pass")
            object.__setattr__(self, "__value", pass_)
        if get_time is not MISSING:
            object.__setattr__(self, "__ctor", "get_time")
            object.__setattr__(self, "__value", get_time)
        if get_party is not MISSING:
            object.__setattr__(self, "__ctor", "get_party")
            object.__setattr__(self, "__value", get_party)
        if embed_expr is not MISSING:
            object.__setattr__(self, "__ctor", "embed_expr")
            object.__setattr__(self, "__value", embed_expr)
    @property
    def pure(self) -> "Optional[Pure]":
        return self.__value if self.__ctor == "pure" else None

    @property
    def block(self) -> "Optional[Block]":
        return self.__value if self.__ctor == "block" else None

    @property
    def commit(self) -> "Optional[Scenario.Commit]":
        return self.__value if self.__ctor == "commit" else None

    @property
    def mustFailAt(self) -> "Optional[Scenario.Commit]":
        return self.__value if self.__ctor == "mustFailAt" else None

    @property
    def pass_(self) -> "Optional[Expr]":
        return self.__value if self.__ctor == "pass" else None

    @property
    def get_time(self) -> "Optional[Unit]":
        return self.__value if self.__ctor == "get_time" else None

    @property
    def get_party(self) -> "Optional[Expr]":
        return self.__value if self.__ctor == "get_party" else None

    @property
    def embed_expr(self) -> "Optional[Scenario.EmbedExpr]":
        return self.__value if self.__ctor == "embed_expr" else None

    def match(self,
            pure: "Callable[[Scenario.EmbedExpr], T]",
            block: "Callable[[Scenario.EmbedExpr], T]",
            commit: "Callable[[Scenario.EmbedExpr], T]",
            mustFailAt: "Callable[[Scenario.EmbedExpr], T]",
            pass_: "Callable[[Scenario.EmbedExpr], T]",
            get_time: "Callable[[Scenario.EmbedExpr], T]",
            get_party: "Callable[[Scenario.EmbedExpr], T]",
            embed_expr: "Callable[[Scenario.EmbedExpr], T]",
            ) -> 'T':
        if self.__ctor == "pure":
            return pure(self.__value)
        elif self.__ctor == "block":
            return block(self.__value)
        elif self.__ctor == "commit":
            return commit(self.__value)
        elif self.__ctor == "mustFailAt":
            return mustFailAt(self.__value)
        elif self.__ctor == "pass":
            return pass_(self.__value)
        elif self.__ctor == "get_time":
            return get_time(self.__value)
        elif self.__ctor == "get_party":
            return get_party(self.__value)
        elif self.__ctor == "embed_expr":
            return embed_expr(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Commit:  # Product
        __slots__ = "_party", "_expr", "_ret_type"
        @property
        def party(self) -> "Expr":
            return self._party

        @property
        def expr(self) -> "Expr":
            return self._expr

        @property
        def ret_type(self) -> "Type":
            return self._ret_type


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class EmbedExpr:  # Product
        __slots__ = "_type", "_body"
        @property
        def type(self) -> "Type":
            return self._type

        @property
        def body(self) -> "Expr":
            return self._body


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class TemplateChoice:  # Product
    """
    Template choice definition.
    """
    __slots__ = "_name", "_consuming", "_controllers", "_arg_binder", "_ret_type", "_update", "_self_binder", "_location"
    @property
    def name(self) -> str:
        return self._name

    @property
    def consuming(self) -> "bool":
        return self._consuming

    @property
    def controllers(self) -> "Expr":
        return self._controllers

    @property
    def arg_binder(self) -> "VarWithType":
        return self._arg_binder

    @property
    def ret_type(self) -> "Type":
        return self._ret_type

    @property
    def update(self) -> "Expr":
        return self._update

    @property
    def self_binder(self) -> str:
        return self._self_binder

    @property
    def location(self) -> "Location":
        return self._location


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class KeyExpr:  # Sum
    """
    we restrict key expressions to records of projections, much like SQL
    """
    __slots__ = "__ctor", "__value"
    def __init__(self, projections = MISSING, record = MISSING):
        if projections is not MISSING:
            object.__setattr__(self, "__ctor", "projections")
            object.__setattr__(self, "__value", projections)
        if record is not MISSING:
            object.__setattr__(self, "__ctor", "record")
            object.__setattr__(self, "__value", record)
    @property
    def projections(self) -> "Optional[KeyExpr.Projections]":
        return self.__value if self.__ctor == "projections" else None

    @property
    def record(self) -> "Optional[KeyExpr.Record]":
        return self.__value if self.__ctor == "record" else None

    def match(self,
            projections: "Callable[[KeyExpr.Record], T]",
            record: "Callable[[KeyExpr.Record], T]",
            ) -> 'T':
        if self.__ctor == "projections":
            return projections(self.__value)
        elif self.__ctor == "record":
            return record(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Projection:  # Product
        __slots__ = "_tycon", "_field"
        @property
        def tycon(self) -> "Type.Con":
            return self._tycon

        @property
        def field(self) -> str:
            return self._field


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Projections:  # Product
        __slots__ = "_projections",
        @property
        def projections(self) -> "Sequence[KeyExpr.Projection]":
            return self._projections


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class RecordField:  # Product
        __slots__ = "_field", "_expr"
        @property
        def field(self) -> str:
            return self._field

        @property
        def expr(self) -> "KeyExpr":
            return self._expr


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class Record:  # Product
        __slots__ = "_tycon", "_fields"
        @property
        def tycon(self) -> "Type.Con":
            return self._tycon

        @property
        def fields(self) -> "Sequence[KeyExpr.RecordField]":
            return self._fields


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class DefTemplate:  # Product
    """
    Contract template definition
    """
    __slots__ = "_tycon", "_param", "_precond", "_signatories", "_agreement", "_choices", "_observers", "_location", "_key"
    @property
    def tycon(self) -> "DottedName":
        return self._tycon

    @property
    def param(self) -> str:
        return self._param

    @property
    def precond(self) -> "Expr":
        return self._precond

    @property
    def signatories(self) -> "Expr":
        return self._signatories

    @property
    def agreement(self) -> "Expr":
        return self._agreement

    @property
    def choices(self) -> "Sequence[TemplateChoice]":
        return self._choices

    @property
    def observers(self) -> "Expr":
        return self._observers

    @property
    def location(self) -> "Location":
        return self._location

    @property
    def key(self) -> "DefTemplate.DefKey":
        return self._key


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class DefKey:  # Sum
        __slots__ = "__ctor", "__value", "_type", "_maintainers"
        def __init__(self, type, maintainers, key = MISSING, complex_key = MISSING):
            object.__setattr__(self, "_type", type)
            if key is not MISSING:
                object.__setattr__(self, "__ctor", "key")
                object.__setattr__(self, "__value", key)
            if complex_key is not MISSING:
                object.__setattr__(self, "__ctor", "complex_key")
                object.__setattr__(self, "__value", complex_key)
            object.__setattr__(self, "_maintainers", maintainers)
        @property
        def type(self) -> "Type":
            return self._type

        @property
        def key(self) -> "Optional[KeyExpr]":
            return self.__value if self.__ctor == "key" else None

        @property
        def complex_key(self) -> "Optional[Expr]":
            return self.__value if self.__ctor == "complex_key" else None

        @property
        def maintainers(self) -> "Expr":
            return self._maintainers

        def match(self,
                key: "Callable[[Expr], T]",
                complex_key: "Callable[[Expr], T]",
                ) -> 'T':
            if self.__ctor == "key":
                return key(self.__value)
            elif self.__ctor == "complex_key":
                return complex_key(self.__value)
            else:
                raise ValueError(f"unknown case: {self.__ctor}")
        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class DefDataType:  # Sum
    """
    Data type definition
    """
    __slots__ = "__ctor", "__value", "_params", "_serializable", "_location"
    def __init__(self, params, serializable, location, name = MISSING, record = MISSING, variant = MISSING, enum = MISSING):
        if name is not MISSING:
            object.__setattr__(self, "__ctor", "name")
            object.__setattr__(self, "__value", name)
        object.__setattr__(self, "_params", params)
        if record is not MISSING:
            object.__setattr__(self, "__ctor", "record")
            object.__setattr__(self, "__value", record)
        if variant is not MISSING:
            object.__setattr__(self, "__ctor", "variant")
            object.__setattr__(self, "__value", variant)
        if enum is not MISSING:
            object.__setattr__(self, "__ctor", "enum")
            object.__setattr__(self, "__value", enum)
        object.__setattr__(self, "_serializable", serializable)
        object.__setattr__(self, "_location", location)
    @property
    def name(self) -> "Optional[DottedName]":
        return self.__value if self.__ctor == "name" else None

    @property
    def params(self) -> "Sequence[TypeVarWithKind]":
        return self._params

    @property
    def record(self) -> "Optional[DefDataType.Fields]":
        return self.__value if self.__ctor == "record" else None

    @property
    def variant(self) -> "Optional[DefDataType.Fields]":
        return self.__value if self.__ctor == "variant" else None

    @property
    def enum(self) -> "Optional[DefDataType.EnumConstructors]":
        return self.__value if self.__ctor == "enum" else None

    @property
    def serializable(self) -> "bool":
        return self._serializable

    @property
    def location(self) -> "Location":
        return self._location

    def match(self,
            name: "Callable[[Location], T]",
            record: "Callable[[Location], T]",
            variant: "Callable[[Location], T]",
            enum: "Callable[[Location], T]",
            ) -> 'T':
        if self.__ctor == "name":
            return name(self.__value)
        elif self.__ctor == "record":
            return record(self.__value)
        elif self.__ctor == "variant":
            return variant(self.__value)
        elif self.__ctor == "enum":
            return enum(self.__value)
        else:
            raise ValueError(f"unknown case: {self.__ctor}")
    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class Fields:  # Product
        __slots__ = "_fields",
        @property
        def fields(self) -> "Sequence[FieldWithType]":
            return self._fields


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

    class EnumConstructors:  # Product
        __slots__ = "_constructors",
        @property
        def constructors(self) -> "Sequence[str]":
            return self._constructors


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class DefTypeSyn:  # Product
    """
    Type synonym definition
     *Available in versions >= 1.8*
    """
    __slots__ = "_name", "_params", "_type", "_location"
    @property
    def name(self) -> "DottedName":
        return self._name

    @property
    def params(self) -> "Sequence[TypeVarWithKind]":
        return self._params

    @property
    def type(self) -> "Type":
        return self._type

    @property
    def location(self) -> "Location":
        return self._location


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class DefValue:  # Product
    """
    Value definition
    """
    __slots__ = "_name_with_type", "_expr", "_no_party_literals", "_is_test", "_location"
    @property
    def name_with_type(self) -> "DefValue.NameWithType":
        return self._name_with_type

    @property
    def expr(self) -> "Expr":
        return self._expr

    @property
    def no_party_literals(self) -> "bool":
        return self._no_party_literals

    @property
    def is_test(self) -> "bool":
        return self._is_test

    @property
    def location(self) -> "Location":
        return self._location


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

    class NameWithType:  # Product
        __slots__ = "_name", "_type"
        @property
        def name(self) -> "DottedName":
            return self._name

        @property
        def type(self) -> "Type":
            return self._type


        def __setattr__(self, key, value):
            """
            Overridden to prevent modifications; this is a read-only type.
            """
            raise Exception("this object is read-only")

class FeatureFlags:  # Product
    __slots__ = "_forbidPartyLiterals", "_dontDivulgeContractIdsInCreateArguments", "_dontDiscloseNonConsumingChoicesToObservers"
    @property
    def forbidPartyLiterals(self) -> "bool":
        return self._forbidPartyLiterals

    @property
    def dontDivulgeContractIdsInCreateArguments(self) -> "bool":
        return self._dontDivulgeContractIdsInCreateArguments

    @property
    def dontDiscloseNonConsumingChoicesToObservers(self) -> "bool":
        return self._dontDiscloseNonConsumingChoicesToObservers


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Module:  # Product
    __slots__ = "_name", "_flags", "_synonyms", "_data_types", "_values", "_templates"
    @property
    def name(self) -> "DottedName":
        return self._name

    @property
    def flags(self) -> "FeatureFlags":
        return self._flags

    @property
    def synonyms(self) -> "Sequence[DefTypeSyn]":
        return self._synonyms

    @property
    def data_types(self) -> "Sequence[DefDataType]":
        return self._data_types

    @property
    def values(self) -> "Sequence[DefValue]":
        return self._values

    @property
    def templates(self) -> "Sequence[DefTemplate]":
        return self._templates


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class InternedDottedName:  # Product
    __slots__ = "_segments",
    @property
    def segments(self) -> "Sequence[str]":
        return self._segments


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class PackageMetadata:  # Product
    __slots__ = "_name", "_version"
    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")

class Package:  # Product
    __slots__ = "_modules", "_interned_strings", "_interned_dotted_names", "_metadata"
    @property
    def modules(self) -> "Sequence[Module]":
        return self._modules

    @property
    def interned_strings(self) -> "Sequence[str]":
        return self._interned_strings

    @property
    def interned_dotted_names(self) -> "Sequence[InternedDottedName]":
        return self._interned_dotted_names

    @property
    def metadata(self) -> "PackageMetadata":
        return self._metadata


    def __setattr__(self, key, value):
        """
        Overridden to prevent modifications; this is a read-only type.
        """
        raise Exception("this object is read-only")


None
