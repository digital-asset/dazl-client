# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# NOTE TO IMPLEMENTORS: A future version of this file is intended to be code-generated instead of
# manually maintained. The makeup of this file is intentionally highly formulaic in order to
# facilitate a smooth transition to automatically-generated data structures.

from dataclasses import dataclass
from enum import Enum
from io import StringIO
from typing import Callable, Optional, Sequence, Union

from ._base import MISSING, T
from ..model.types import ModuleRef, ValueReference, TypeReference as TypeConName, TypeReference
from ..util.typing import safe_cast


class Unit:
    __slots__ = ()


UNIT = Unit()


# PackageRef


class DottedName:
    __slots__ = 'segments',

    segments: Sequence[str]

    def __init__(self, segments: Sequence[str] = ()):
        object.__setattr__(self, 'segments', tuple(segments))


# ModuleRef
# TypeConName


ValName = ValueReference


@dataclass(frozen=True)
class FieldWithType:
    field: str
    type: 'Type'


@dataclass(frozen=True)
class VarWithType:
    var: str
    type: 'Type'


@dataclass(frozen=True)
class TypeVarWithKind:
    var: str
    kind: 'Kind'

    def __str__(self):
        return f'{self.var} : {self.kind}'

    def __repr__(self):
        return f'TypeVarWithKind({self})'


@dataclass(frozen=True)
class FieldWithExpr:
    field: str
    expr: 'Expr'

    def __repr__(self):
        return f'FieldWithExpr({self.field}={self.expr})'


@dataclass(frozen=True)
class Binding:
    binder: 'VarWithType'
    bound: 'Expr'


class Kind:
    __slots__ = ('_Sum_name', '_Sum_value')

    class Arrow:
        params: 'Sequence[Kind]'
        result: 'Kind'

        def __init__(self, params: 'Sequence[Kind]', result: 'Kind'):
            self.params = params
            self.result = result

    def __init__(
            self,
            star: 'Unit' = MISSING,
            arrow: 'Arrow' = MISSING,
            nat: 'Unit' = MISSING):
        if star is not MISSING:
            object.__setattr__(self, '_Sum_name', 'star')
            object.__setattr__(self, '_Sum_value', star)
        elif arrow is not MISSING:
            object.__setattr__(self, '_Sum_name', 'arrow')
            object.__setattr__(self, '_Sum_value', arrow)
        elif nat is not MISSING:
            object.__setattr__(self, '_Sum_name', 'nat')
            object.__setattr__(self, '_Sum_value', nat)
        else:
            raise ValueError('at least one must be specified')

    @property
    def star(self) -> 'Optional[Unit]':
        return self._Sum_value if self._Sum_name == 'star' else None

    @property
    def arrow(self) -> 'Optional[Arrow]':
        return self._Sum_value if self._Sum_name == 'arrow' else None

    @property
    def nat(self) -> 'Optional[Unit]':
        return self._Sum_value if self._Sum_name == 'nat' else None

    def __repr__(self):
        if self._Sum_name == 'star':
            return '*'
        else:
            arrow = self.arrow
            params = [repr(i) for i in (*arrow.params, arrow.result)]
            return ' -> '.join((f'({i})' if ' ' in i else i for i in params))


class PrimType(Enum):
    UNIT = 0          # arity = 0
    BOOL = 1          # arity = 0
    INT64 = 2         # arity = 0
    DECIMAL = 3       # arity = 0
    CHAR = 4          # arity = 0, we have removed this in favor of TEXT for everything text related
    TEXT = 5          # arity = 0
    TIMESTAMP = 6     # arity = 0
    RELTIME = 7       # we removed this in favor of INT64.
    PARTY = 8         # arity = 0
    LIST = 9          # arity = 1
    UPDATE = 10       # arity = 1
    SCENARIO = 11     # arity = 1
    DATE = 12         # arity = 0, days since the unix epoch
    CONTRACT_ID = 13  # arity = 1
    OPTIONAL = 14     # arity = 1
    ARROW = 15        # arity = 2
    TEXTMAP = 16      # arity = 1
    NUMERIC = 17
    ANY = 18
    TYPE_REP = 19
    GENMAP = 20


# noinspection PyShadowingBuiltins
class Type:

    @dataclass(frozen=True)
    class Var:
        var: 'str'
        args: 'Sequence[Type]'

    class Con:
        tycon: 'TypeReference'
        args: 'Sequence[Type]'

        def __init__(self, tycon: 'TypeReference', args: 'Sequence[Type]'):
            self.tycon = tycon
            self.args = tuple(args)

        def __repr__(self):
            return f'Type.Con(tycon={self.tycon}, args={self.args})'

    class Prim:
        prim: 'PrimType'
        args: 'Sequence[Type]'

        def __init__(
                self,
                prim: 'PrimType',
                args: 'Sequence[Type]'):
            self.prim = prim
            self.args = tuple(args)

        def __repr__(self):
            return f'Type.Prim(prim={self.prim!r}, args={self.args!r})'

    class Forall:
        vars: 'Sequence[TypeVarWithKind]'
        body: 'Type'

        # noinspection PyShadowingBuiltins
        def __init__(self, vars: 'Sequence[TypeVarWithKind]', body: 'Type'):
            self.vars = vars
            self.body = body

    class Tuple:
        fields: 'Sequence[FieldWithType]'

        def __init__(self, fields: 'Sequence[FieldWithType]'):
            self.fields = tuple(fields)

    @dataclass(frozen=True)
    class App:
        tyfun: 'Type'
        args: 'Sequence[Type]'

    __slots__ = '_Sum_name', '_Sum_value'

    def __init__(
            self,
            var: 'Type.Var' = MISSING,
            con: 'Type.Con' = MISSING,
            prim: 'Type.Prim' = MISSING,
            forall: 'Type.Forall' = MISSING,
            tuple: 'Type.Tuple' = MISSING,
            nat: int = MISSING):
        if var is not MISSING:
            object.__setattr__(self, '_Sum_name', 'var')
            object.__setattr__(self, '_Sum_value', var)
        elif con is not MISSING:
            object.__setattr__(self, '_Sum_name', 'con')
            object.__setattr__(self, '_Sum_value', con)
        elif prim is not MISSING:
            object.__setattr__(self, '_Sum_name', 'prim')
            object.__setattr__(self, '_Sum_value', prim)
        elif forall is not MISSING:
            object.__setattr__(self, '_Sum_name', 'forall')
            object.__setattr__(self, '_Sum_value', forall)
        elif tuple is not MISSING:
            object.__setattr__(self, '_Sum_name', 'tuple')
            object.__setattr__(self, '_Sum_value', tuple)
        elif nat is not MISSING:
            object.__setattr__(self, '_Sum_name', 'nat')
            object.__setattr__(self, '_Sum_value', nat)
        else:
            raise ValueError('unknown sum type')

    @property
    def var(self) -> 'Type.Var':
        return self._Sum_value if self._Sum_name == 'var' else None

    @property
    def con(self) -> 'Type.Con':
        return self._Sum_value if self._Sum_name == 'con' else None

    @property
    def prim(self) -> 'Type.Prim':
        return self._Sum_value if self._Sum_name == 'prim' else None

    @property
    def forall(self) -> 'Type.Forall':
        return self._Sum_value if self._Sum_name == 'forall' else None

    @property
    def tuple(self) -> 'Type.Tuple':
        return self._Sum_value if self._Sum_name == 'tuple' else None

    @property
    def nat(self) -> int:
        return self._Sum_value if self._Sum_name == 'nat' else None

    # noinspection PyPep8Naming
    def Sum_match(
            self,
            var: 'Callable[[Type.Var], T]',
            con: 'Callable[[Type.Con], T]',
            prim: 'Callable[[Type.Prim], T]',
            forall: 'Callable[[Type.Forall], T]',
            tuple: 'Callable[[Type.Tuple], T]',
            nat: 'Callable[[int], T]') -> 'T':
        if self._Sum_name == 'var':
            return var(self._Sum_value)
        elif self._Sum_name == 'con':
            return con(self._Sum_value)
        elif self._Sum_name == 'prim':
            return prim(self._Sum_value)
        elif self._Sum_name == 'forall':
            return forall(self._Sum_value)
        elif self._Sum_name == 'tuple':
            return tuple(self._Sum_value)
        elif self._Sum_name == 'nat':
            return nat(self._Sum_value)
        else:
            raise Exception('invalid _Sum_name value')

    def __setattr__(self, key, value):
        raise Exception('Type is a read-only object')

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
            return f'Type({DAML_PRETTY_PRINTER.visit_type(self)})'
        except:  # noqa
            return 'Type(...)'


class PrimLit:

    __slots__ = ('_Sum_name', '_Sum_value')

    def __init__(
            self,
            int64: int = MISSING,
            decimal: str = MISSING,
            text: str = MISSING,
            timestamp: float = MISSING,
            party: str = MISSING,
            date: int = MISSING,
            numeric: str = MISSING):
        if int64 is not MISSING:
            object.__setattr__(self, '_Sum_name', 'int64')
            object.__setattr__(self, '_Sum_value', int64)
        elif decimal is not MISSING:
            object.__setattr__(self, '_Sum_name', 'decimal')
            object.__setattr__(self, '_Sum_value', decimal)
        elif text is not MISSING:
            object.__setattr__(self, '_Sum_name', 'text')
            object.__setattr__(self, '_Sum_value', text)
        elif timestamp is not MISSING:
            object.__setattr__(self, '_Sum_name', 'timestamp')
            object.__setattr__(self, '_Sum_value', timestamp)
        elif party is not MISSING:
            object.__setattr__(self, '_Sum_name', 'party')
            object.__setattr__(self, '_Sum_value', party)
        elif date is not MISSING:
            object.__setattr__(self, '_Sum_name', 'date')
            object.__setattr__(self, '_Sum_value', date)
        elif numeric is not MISSING:
            object.__setattr__(self, '_Sum_name', 'numeric')
            object.__setattr__(self, '_Sum_value', numeric)

    @property
    def int64(self) -> 'Optional[int]':
        return self._Sum_value if self._Sum_name == 'int64' else None

    @property
    def decimal(self) -> 'Optional[str]':
        """
        our decimal type would fit in an int128, but sadly Protobuf does not
        have one. so, string it is. note that we can't store the whole and
        decimal part in two numbers either, because 10^28 > 2^63.
        """
        return self._Sum_value if self._Sum_name == 'decimal' else None

    @property
    def text(self) -> 'Optional[str]':
        return self._Sum_value if self._Sum_name == 'text' else None

    @property
    def timestamp(self) -> 'Optional[float]':
        """
        microseconds since the UNIX epoch. can go backwards. fixed
        since the vast majority of values will be greater than
        2^28, since currently the number of microseconds since the
        epoch is greater than that. Range: 0001-01-01T00:00:00Z to
        9999-12-31T23:59:59.999999Z, so that we can convert to/from
        https://www.ietf.org/rfc/rfc3339.txt
        """
        return self._Sum_value if self._Sum_name == 'timestamp' else None

    @property
    def party(self) -> 'Optional[str]':
        return self._Sum_value if self._Sum_name == 'party' else None

    @property
    def date(self) -> 'Optional[int]':
        """
        days since the unix epoch. can go backwards. limited from
        0001-01-01 to 9999-12-31, also to be compatible with
        https://www.ietf.org/rfc/rfc3339.txt
        """
        return self._Sum_value if self._Sum_name == 'date' else None

    @property
    def numeric(self) -> 'Optional[str]':
        """
        Serialization of number with precision 38 and scale between 0 and 37

        Must be a string that matched
            `-?([0-1]\d*|0)\.(\d*)

        The number of decimal digits indicate the scale of the number.
        """
        return self._Sum_value if self._Sum_name == 'date' else None


# noinspection PyShadowingBuiltins
class Location:

    class Range:
        __slots__ = ('start_line', 'start_col', 'end_line', 'end_col')

        def __init__(
                self,
                start_line: int = 0,
                start_col: int = 0,
                end_line: int = 0,
                end_col: int = 0):
            object.__setattr__(self, 'start_line', start_line)
            object.__setattr__(self, 'start_col', start_col)
            object.__setattr__(self, 'end_line', end_line)
            object.__setattr__(self, 'end_col', end_col)

        start_line: int
        start_col: int
        end_line: int
        end_col: int

    module: 'ModuleRef'
    range: 'Range'

    def __init__(self, module: 'ModuleRef' = MISSING, range: 'Range' = MISSING):
        object.__setattr__(self, 'module', module)
        object.__setattr__(self, 'range', range)


# noinspection PyShadowingBuiltins
class Expr:

    class RecCon:
        tycon: 'Type.Con'
        fields: 'Sequence[FieldWithExpr]'

        def __init__(self, tycon: 'Type.Con', fields: 'Sequence[FieldWithExpr]'):
            self.tycon = tycon
            self.fields = tuple(fields)

        def __repr__(self):
            return f'Expr.RecCon(tycon={self.tycon}, fields={self.fields})'

    @dataclass(frozen=True)
    class RecProj:
        tycon: 'Type.Con'  # Always fully applied string
        field: str
        record: 'Expr'

        def __repr__(self):
            with StringIO() as buf:
                buf.write('Expr.RecProj(')
                if self.tycon is not None:
                    buf.write('tycon=')
                    buf.write(repr(self.tycon))
                    buf.write(', ')
                buf.write('record=')
                buf.write(repr(self.record))
                buf.write(', field=')
                buf.write(repr(self.field))
                buf.write(')')
                return buf.getvalue()

    # Set `field` in `record` to `update`.
    @dataclass(frozen=True)
    class RecUpd:
        tycon: 'Type.Con'
        field: str
        record: 'Expr'
        update: 'Expr'

    class VariantCon:
        tycon: 'Type.Con'  # Always fully applied
        variant_con: str
        variant_arg: 'Expr'

        def __init__(self, tycon: 'Type.Con', variant_con: str, variant_arg: 'Expr'):
            self.tycon = tycon
            self.variant_con = variant_con
            self.variant_arg = variant_arg

    @dataclass(frozen=True)
    class EnumCon:
        tycon: 'TypeReference'  # Always fully applied
        enum_con: str

    @dataclass(frozen=True)
    class StructCon:
        fields: 'Sequence[FieldWithExpr]'  # length > 0

    @dataclass(frozen=True)
    class StructProj:
        field: str
        tuple: 'Expr'

    # Set `field` in `tuple` to `update`.
    @dataclass(frozen=True)
    class StructUpd:
        field: str
        tuple: 'Expr'
        update: 'Expr'

    @dataclass(frozen=True)
    class App:
        fun: 'Expr'
        args: 'Sequence[Expr]'  # length > 0

    class TyApp:
        expr: 'Expr'
        types: 'Sequence[Type]'  # length > 0

        def __init__(self, expr: 'Expr', types: 'Sequence[Type]'):
            object.__setattr__(self, 'expr', safe_cast(Expr, expr))
            object.__setattr__(self, 'types', tuple(types))

        def __repr__(self):
            return f'Expr.TyApp(types={self.types}, expr={self.expr})'

    class Abs:
        param: 'Sequence[VarWithType]'  # length > 0
        body: 'Expr'

        def __init__(self, param: 'Sequence[VarWithType]', body: 'Expr'):
            object.__setattr__(self, 'param', param)
            object.__setattr__(self, 'body', safe_cast(Expr, body))

        def __repr__(self):
            with StringIO() as buf:
                buf.write('Expr.Abs(𝜆 ')
                buf.write(' '.join(vwt.var for vwt in self.param))
                buf.write(' . ')
                buf.write(repr(self.body))
                buf.write(')')
                return buf.getvalue()

    @dataclass(frozen=True)
    class TyAbs:
        param: 'Sequence[TypeVarWithKind]'
        body: 'Expr'

    @dataclass(frozen=True)
    class Nil:
        type: 'Type'

        __slots__ = 'type',

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type'):
            object.__setattr__(self, 'type', type)

        def __repr__(self):
            return 'Nil()'

    @dataclass(frozen=True)
    class Cons:
        type: 'Type'
        front: 'Sequence[Expr]'  # length > 0
        tail: 'Expr'

        def __repr__(self):
            with StringIO() as buf:
                buf.write('Expr.Cons(front=')
                buf.write(repr(list(self.front)))
                buf.write(', tail=')
                buf.write(repr(self.tail))
                buf.write(')')
                return buf.getvalue()

    # noinspection PyPep8Naming
    class OptionalNone:
        type: 'Type'

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type'):
            self.type = type

        def __repr__(self):
            return f'Expr.None(: {self.type})'

    class OptionalSome:
        type: 'Type'
        body: 'Expr'

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type', body: 'Expr'):
            self.type = type
            self.body = body

        def __repr__(self):
            return f'Expr.Some({self.body!r} : {self.type})'

    class ToAny:
        type: 'Type'
        expr: 'Expr'

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type', expr: 'Expr'):
            self.type = type
            self.expr = expr

    class FromAny:
        type: 'Type'
        expr: 'Expr'

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type', expr: 'Expr'):
            self.type = type
            self.expr = expr

    class ToTextTemplateId:
        type: 'Type'

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type'):
            self.type = type

    __slots__ = 'location', '_Sum_name', '_Sum_value'

    def __init__(
            self,
            var: 'str' = MISSING,
            val: 'ValName' = MISSING,
            builtin: 'BuiltinFunction' = MISSING,
            prim_con: 'PrimCon' = MISSING,
            prim_lit: 'PrimLit' = MISSING,
            rec_con: 'RecCon' = MISSING,
            rec_proj: 'RecProj' = MISSING,
            variant_con: 'VariantCon' = MISSING,
            enum_con: 'EnumCon' = MISSING,
            struct_con: 'StructCon' = MISSING,
            struct_proj: 'StructProj' = MISSING,
            app: 'App' = MISSING,
            ty_app: 'TyApp' = MISSING,
            abs: 'Abs' = MISSING,
            ty_abs: 'TyAbs' = MISSING,
            case: 'Case' = MISSING,
            let: 'Block' = MISSING,
            nil: 'Nil' = MISSING,
            cons: 'Cons' = MISSING,
            update: 'Update' = MISSING,
            scenario: 'Scenario' = MISSING,
            rec_upd: 'RecUpd' = MISSING,
            struct_upd: 'StructUpd' = MISSING,
            optional_none: 'OptionalNone' = MISSING,
            optional_some: 'OptionalSome' = MISSING,
            location: 'Location' = MISSING,
            to_any: 'ToAny' = MISSING,
            from_any: 'FromAny' = MISSING,
            to_text_template_id: 'ToTextTemplateId' = MISSING,
            type_rep: 'Type' = MISSING):
        object.__setattr__(self, 'location', location)
        if var is not MISSING:
            object.__setattr__(self, '_Sum_name', 'var')
            object.__setattr__(self, '_Sum_value', var)
        elif val is not MISSING:
            object.__setattr__(self, '_Sum_name', 'val')
            object.__setattr__(self, '_Sum_value', val)
        elif builtin is not MISSING:
            object.__setattr__(self, '_Sum_name', 'builtin')
            object.__setattr__(self, '_Sum_value', builtin)
        elif prim_con is not MISSING:
            object.__setattr__(self, '_Sum_name', 'prim_con')
            object.__setattr__(self, '_Sum_value', prim_con)
        elif prim_lit is not MISSING:
            object.__setattr__(self, '_Sum_name', 'prim_lit')
            object.__setattr__(self, '_Sum_value', prim_lit)
        elif rec_con is not MISSING:
            object.__setattr__(self, '_Sum_name', 'rec_con')
            object.__setattr__(self, '_Sum_value', rec_con)
        elif rec_proj is not MISSING:
            object.__setattr__(self, '_Sum_name', 'rec_proj')
            object.__setattr__(self, '_Sum_value', rec_proj)
        elif variant_con is not MISSING:
            object.__setattr__(self, '_Sum_name', 'variant_con')
            object.__setattr__(self, '_Sum_value', variant_con)
        elif enum_con is not MISSING:
            object.__setattr__(self, '_Sum_name', 'enum_con')
            object.__setattr__(self, '_Sum_value', enum_con)
        elif struct_con is not MISSING:
            object.__setattr__(self, '_Sum_name', 'struct_con')
            object.__setattr__(self, '_Sum_value', struct_con)
        elif struct_proj is not MISSING:
            object.__setattr__(self, '_Sum_name', 'struct_proj')
            object.__setattr__(self, '_Sum_value', struct_proj)
        elif app is not MISSING:
            object.__setattr__(self, '_Sum_name', 'app')
            object.__setattr__(self, '_Sum_value', app)
        elif ty_app is not MISSING:
            object.__setattr__(self, '_Sum_name', 'ty_app')
            object.__setattr__(self, '_Sum_value', ty_app)
        elif abs is not MISSING:
            object.__setattr__(self, '_Sum_name', 'abs')
            object.__setattr__(self, '_Sum_value', abs)
        elif ty_abs is not MISSING:
            object.__setattr__(self, '_Sum_name', 'ty_abs')
            object.__setattr__(self, '_Sum_value', ty_abs)
        elif case is not MISSING:
            object.__setattr__(self, '_Sum_name', 'case')
            object.__setattr__(self, '_Sum_value', case)
        elif let is not MISSING:
            object.__setattr__(self, '_Sum_name', 'let')
            object.__setattr__(self, '_Sum_value', let)
        elif nil is not MISSING:
            object.__setattr__(self, '_Sum_name', 'nil')
            object.__setattr__(self, '_Sum_value', nil)
        elif cons is not MISSING:
            object.__setattr__(self, '_Sum_name', 'cons')
            object.__setattr__(self, '_Sum_value', cons)
        elif update is not MISSING:
            object.__setattr__(self, '_Sum_name', 'update')
            object.__setattr__(self, '_Sum_value', update)
        elif scenario is not MISSING:
            object.__setattr__(self, '_Sum_name', 'scenario')
            object.__setattr__(self, '_Sum_value', scenario)
        elif rec_upd is not MISSING:
            object.__setattr__(self, '_Sum_name', 'rec_upd')
            object.__setattr__(self, '_Sum_value', rec_upd)
        elif struct_upd is not MISSING:
            object.__setattr__(self, '_Sum_name', 'struct_upd')
            object.__setattr__(self, '_Sum_value', struct_upd)
        elif optional_none is not MISSING:
            object.__setattr__(self, '_Sum_name', 'optional_none')
            object.__setattr__(self, '_Sum_value', optional_none)
        elif optional_some is not MISSING:
            object.__setattr__(self, '_Sum_name', 'optional_some')
            object.__setattr__(self, '_Sum_value', optional_some)
        elif to_any is not MISSING:
            object.__setattr__(self, '_Sum_name', 'to_any')
            object.__setattr__(self, '_Sum_value', to_any)
        elif from_any is not MISSING:
            object.__setattr__(self, '_Sum_name', 'from_any')
            object.__setattr__(self, '_Sum_value', from_any)
        elif to_text_template_id is not MISSING:
            object.__setattr__(self, '_Sum_name', 'to_text_template_id')
            object.__setattr__(self, '_Sum_value', to_text_template_id)
        elif type_rep is not MISSING:
            object.__setattr__(self, '_Sum_name', 'type_rep')
            object.__setattr__(self, '_Sum_value', type_rep)
        else:
            raise ValueError(f'At least one valid Sum value must be supplied!')

    def __setattr__(self, key, value):
        raise Exception('Expr is read-only')

    @property
    def var(self) -> 'Optional[str]':
        return self._Sum_value if self._Sum_name == 'var' else None

    @property
    def val(self) -> 'Optional[ValName]':
        return self._Sum_value if self._Sum_name == 'val' else None

    @property
    def builtin(self) -> 'Optional[BuiltinFunction]':
        return self._Sum_value if self._Sum_name == 'builtin' else None

    @property
    def prim_con(self) -> 'Optional[PrimCon]':
        return self._Sum_value if self._Sum_name == 'prim_con' else None

    @property
    def prim_lit(self) -> 'Optional[PrimLit]':
        return self._Sum_value if self._Sum_name == 'prim_lit' else None

    @property
    def rec_con(self) -> 'Optional[Expr.RecCon]':
        return self._Sum_value if self._Sum_name == 'rec_con' else None

    @property
    def rec_proj(self) -> 'Optional[RecProj]':
        return self._Sum_value if self._Sum_name == 'rec_proj' else None

    @property
    def variant_con(self) -> 'Optional[VariantCon]':
        return self._Sum_value if self._Sum_name == 'variant_con' else None

    @property
    def enum_con(self) -> 'Optional[EnumCon]':
        return self._Sum_value if self._Sum_name == 'enum_con' else None

    @property
    def struct_con(self) -> 'Optional[StructCon]':
        return self._Sum_value if self._Sum_name == 'struct_con' else None

    @property
    def struct_proj(self) -> 'Optional[StructProj]':
        return self._Sum_value if self._Sum_name == 'struct_proj' else None

    @property
    def app(self) -> 'Optional[App]':
        return self._Sum_value if self._Sum_name == 'app' else None

    @property
    def ty_app(self) -> 'Optional[Expr.TyApp]':
        return self._Sum_value if self._Sum_name == 'ty_app' else None

    @property
    def abs(self) -> 'Optional[Expr.Abs]':
        return self._Sum_value if self._Sum_name == 'abs' else None

    @property
    def ty_abs(self) -> 'Optional[Expr.TyAbs]':
        return self._Sum_value if self._Sum_name == 'ty_abs' else None

    @property
    def case(self) -> 'Optional[Case]':
        return self._Sum_value if self._Sum_name == 'case' else None

    @property
    def let(self) -> 'Optional[Block]':
        return self._Sum_value if self._Sum_name == 'let' else None

    @property
    def nil(self) -> 'Optional[Expr.Nil]':
        return self._Sum_value if self._Sum_name == 'nil' else None

    @property
    def cons(self) -> 'Optional[Expr.Cons]':
        return self._Sum_value if self._Sum_name == 'cons' else None

    @property
    def update(self) -> 'Optional[Update]':
        return self._Sum_value if self._Sum_name == 'update' else None

    @property
    def scenario(self) -> 'Optional[Scenario]':
        return self._Sum_value if self._Sum_name == 'scenario' else None

    @property
    def rec_upd(self) -> 'Optional[RecUpd]':
        return self._Sum_value if self._Sum_name == 'rec_upd' else None

    @property
    def struct_upd(self) -> 'Optional[StructUpd]':
        return self._Sum_value if self._Sum_name == 'struct_upd' else None

    @property
    def optional_none(self) -> 'Optional[OptionalNone]':
        return self._Sum_value if self._Sum_name == 'optional_none' else None

    @property
    def optional_some(self) -> 'Optional[OptionalSome]':
        return self._Sum_value if self._Sum_name == 'optional_some' else None

    @property
    def to_any(self) -> 'Optional[ToAny]':
        return self._Sum_value if self._Sum_name == 'to_any' else None

    @property
    def from_any(self) -> 'Optional[FromAny]':
        return self._Sum_value if self._Sum_name == 'from_any' else None

    @property
    def to_text_template_id(self) -> 'Optional[ToTextTemplateId]':
        return self._Sum_value if self._Sum_name == 'to_text_template_id' else None

    @property
    def type_rep(self) -> 'Optional[Type]':
        return self._Sum_value if self._Sum_name == 'type_rep' else None

    # noinspection PyPep8Naming
    def Sum_match(
            self,
            var: 'Callable[[str], T]',
            val: 'Callable[[ValName], T]',
            builtin: 'Callable[[BuiltinFunction], T]',
            prim_con: 'Callable[[PrimCon], T]',
            prim_lit: 'Callable[[PrimLit], T]',
            rec_con: 'Callable[[RecCon], T]',
            rec_proj: 'Callable[[RecProj], T]',
            variant_con: 'Callable[[VariantCon], T]',
            enum_con: 'Callable[[EnumCon], T]',
            struct_con: 'Callable[[StructCon], T]',
            struct_proj: 'Callable[[StructProj], T]',
            app: 'Callable[[App], T]',
            ty_app: 'Callable[[TyApp], T]',
            abs: 'Callable[[Abs], T]',
            ty_abs: 'Callable[[TyAbs], T]',
            case: 'Callable[[Case], T]',
            let: 'Callable[[Block], T]',
            nil: 'Callable[[Nil], T]',
            cons: 'Callable[[Cons], T]',
            update: 'Callable[[Update], T]',
            scenario: 'Callable[[Scenario], T]',
            rec_upd: 'Callable[[RecUpd], T]',
            struct_upd: 'Callable[[StructUpd], T]',
            optional_none: 'Callable[[OptionalNone], T]',
            optional_some: 'Callable[[OptionalSome], T]',
            to_any: 'Callable[[ToAny], T]',
            from_any: 'Callable[[ToAny], T]',
            to_text_template_id: 'Callable[[ToTextTemplateId], T]',
            type_rep: 'Callable[[Type], T') -> 'T':
        if self._Sum_name == 'var':
            return var(self.var)
        elif self._Sum_name == 'val':
            return val(self.val)
        elif self._Sum_name == 'builtin':
            return builtin(self.builtin)
        elif self._Sum_name == 'prim_con':
            return prim_con(self.prim_con)
        elif self._Sum_name == 'prim_lit':
            return prim_lit(self.prim_lit)
        elif self._Sum_name == 'rec_con':
            return rec_con(self.rec_con)
        elif self._Sum_name == 'rec_proj':
            return rec_proj(self.rec_proj)
        elif self._Sum_name == 'variant_con':
            return variant_con(self.variant_con)
        elif self._Sum_name == 'enum_con':
            return enum_con(self.enum_con)
        elif self._Sum_name == 'struct_con':
            return struct_con(self.struct_con)
        elif self._Sum_name == 'struct_proj':
            return struct_proj(self.struct_proj)
        elif self._Sum_name == 'app':
            return app(self.app)
        elif self._Sum_name == 'ty_app':
            return ty_app(self.ty_app)
        elif self._Sum_name == 'abs':
            return abs(self.abs)
        elif self._Sum_name == 'ty_abs':
            return ty_abs(self.ty_abs)
        elif self._Sum_name == 'case':
            return case(self.case)
        elif self._Sum_name == 'let':
            return let(self.let)
        elif self._Sum_name == 'nil':
            return nil(self.nil)
        elif self._Sum_name == 'cons':
            return cons(self.cons)
        elif self._Sum_name == 'update':
            return update(self.update)
        elif self._Sum_name == 'scenario':
            return scenario(self.scenario)
        elif self._Sum_name == 'rec_upd':
            return rec_upd(self.rec_upd)
        elif self._Sum_name == 'struct_upd':
            return struct_upd(self.struct_upd)
        elif self._Sum_name == 'optional_none':
            return optional_none(self.optional_none)
        elif self._Sum_name == 'optional_some':
            return optional_some(self.optional_some)
        elif self._Sum_name == 'to_any':
            return to_any(self.to_any)
        elif self._Sum_name == 'from_any':
            return from_any(self.from_any)
        elif self._Sum_name == 'to_text_template_id':
            return to_text_template_id(self.to_text_template_id)
        elif self._Sum_name == 'type_rep':
            return type_rep(self.type_rep)
        else:
            raise Exception

    def __repr__(self):
        return f'Expr({self._Sum_name}={self._Sum_value!r})'


class CaseAlt:
    class Variant:
        con: 'TypeConName'
        variant: str
        binder: str

        def __init__(self, con, variant, binder):
            self.con = con
            self.variant = variant
            self.binder = binder

    @dataclass(frozen=True)
    class Enum:
        con: TypeReference
        constructor: str

    @dataclass(frozen=True)
    class Cons:
        var_head: str
        var_tail: str

    @dataclass(frozen=True)
    class OptionalSome:
        var_body: str

    __slots__ = 'body', '_Sum_name', '_Sum_value'
    body: 'Expr'

    def __init__(
            self,
            default: 'Unit' = MISSING,
            variant: 'Variant' = MISSING,
            prim_con: 'PrimCon' = MISSING,
            nil: 'Unit' = MISSING,
            cons: 'Cons' = MISSING,
            optional_none: 'Unit' = MISSING,
            optional_some: 'OptionalSome' = MISSING,
            body: 'Expr' = MISSING,
            enum: 'Enum' = MISSING):
        object.__setattr__(self, 'body', body)
        if default is not MISSING:
            object.__setattr__(self, '_Sum_name', 'default')
            object.__setattr__(self, '_Sum_value', default)
        elif variant is not MISSING:
            object.__setattr__(self, '_Sum_name', 'variant')
            object.__setattr__(self, '_Sum_value', variant)
        elif prim_con is not MISSING:
            object.__setattr__(self, '_Sum_name', 'prim_con')
            object.__setattr__(self, '_Sum_value', prim_con)
        elif nil is not MISSING:
            object.__setattr__(self, '_Sum_name', 'nil')
            object.__setattr__(self, '_Sum_value', nil)
        elif cons is not MISSING:
            object.__setattr__(self, '_Sum_name', 'cons')
            object.__setattr__(self, '_Sum_value', cons)
        elif optional_none is not MISSING:
            object.__setattr__(self, '_Sum_name', 'optional_none')
            object.__setattr__(self, '_Sum_value', optional_none)
        elif optional_some is not MISSING:
            object.__setattr__(self, '_Sum_name', 'optional_some')
            object.__setattr__(self, '_Sum_value', optional_some)
        elif enum is not MISSING:
            object.__setattr__(self, '_Sum_name', 'enum')
            object.__setattr__(self, '_Sum_value', enum)

    @property
    def default(self) -> 'Optional[Unit]':
        return self._Sum_value if self._Sum_name == 'default' else None

    @property
    def variant(self) -> 'Optional[Variant]':
        return self._Sum_value if self._Sum_name == 'variant' else None

    @property
    def prim_con(self) -> 'Optional[PrimCon]':
        return self._Sum_value if self._Sum_name == 'prim_con' else None

    @property
    def nil(self) -> 'Optional[Unit]':
        return self._Sum_value if self._Sum_name == 'nil' else None

    @property
    def cons(self) -> 'Optional[Cons]':
        return self._Sum_value if self._Sum_name == 'cons' else None

    @property
    def optional_none(self) -> 'Optional[Unit]':
        return self._Sum_value if self._Sum_name == 'optional_none' else None

    @property
    def optional_some(self) -> 'Optional[OptionalSome]':
        return self._Sum_value if self._Sum_name == 'optional_some' else None

    @property
    def enum(self) -> 'Optional[Enum]':
        return self._Sum_value if self._Sum_name == 'enum' else None

    # noinspection PyPep8Naming
    def Sum_match(
            self,
            default: 'Callable[[Unit], T]',
            variant: 'Callable[[Variant], T]',
            prim_con: 'Callable[[PrimCon], T]',
            nil: 'Callable[[Unit], T]',
            cons: 'Callable[[Cons], T]',
            optional_none: 'Callable[[Unit], T]',
            optional_some: 'Callable[[OptionalSome], T]',
            enum: 'Callable[[Enum], T]'):
        if self._Sum_name == 'default':
            return default(self.default)
        elif self._Sum_name == 'variant':
            return variant(self.variant)
        elif self._Sum_name == 'prim_con':
            return prim_con(self.prim_con)
        elif self._Sum_name == 'nil':
            return nil(self.nil)
        elif self._Sum_name == 'cons':
            return cons(self.cons)
        elif self._Sum_name == 'optional_none':
            return optional_none(self.optional_none)
        elif self._Sum_name == 'optional_some':
            return optional_some(self.optional_some)
        elif self._Sum_name == 'enum':
            return enum(self.enum)
        else:
            raise Exception


@dataclass(frozen=True)
class Case:
    # noinspection SpellCheckingInspection
    scrut: 'Expr'
    alts: 'Sequence[CaseAlt]'  # length > 0


@dataclass(frozen=True)
class Block:
    # A block of bindings and an expression.
    # Encodes a sequence of binds in e.g. a let or update block.
    bindings: 'Sequence[Binding]'  # length > 0
    body: 'Expr'


@dataclass(frozen=True)
class Pure:
    type: 'Type'
    expr: 'Expr'


class Update:

    class Create:
        template: 'TypeConName'
        expr: 'Expr'

        def __init__(self, template: 'TypeConName', expr: 'Expr'):
            self.template = template
            self.expr = expr

    class Exercise:
        template: 'TypeConName'
        choice: str
        cid: 'Expr'
        actor: 'Optional[Expr]'
        arg: 'Expr'

        def __init__(
                self, template: 'TypeConName', choice: str, cid: 'Expr', actor: 'Optional[Expr]',
                arg: 'Expr'):
            self.template = template
            self.choice = choice
            self.cid = cid
            self.actor = actor
            self.arg = arg

    class Fetch:
        template: 'TypeConName'
        cid: 'Expr'

        def __init__(self, template, cid):
            self.template = template
            self.cid = cid

    class EmbedExpr:
        type: 'Type'  # the expression should be of type `Scenario type`
        body: 'Expr'

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type', body: 'Expr'):
            self.type = type
            self.body = body

    class RetrieveByKey:
        template: 'TypeConName'
        key: 'Expr'

        def __init__(self, template: 'TypeConName', key: 'Expr'):
            self.template = template
            self.key = key

    __slots__ = '_Sum_name', '_Sum_value'

    def __init__(
            self,
            pure: 'Pure' = MISSING,
            block: 'Block' = MISSING,
            create: 'Create' = MISSING,
            exercise: 'Exercise' = MISSING,
            fetch: 'Fetch' = MISSING,
            get_time: 'Unit' = MISSING,
            lookup_by_key: 'RetrieveByKey' = MISSING,
            fetch_by_key: 'RetrieveByKey' = MISSING,
            embed_expr: 'EmbedExpr' = MISSING):
        if pure is not MISSING:
            object.__setattr__(self, '_Sum_name', 'pure')
            object.__setattr__(self, '_Sum_value', pure)
        elif block is not MISSING:
            object.__setattr__(self, '_Sum_name', 'block')
            object.__setattr__(self, '_Sum_value', block)
        elif create is not MISSING:
            object.__setattr__(self, '_Sum_name', 'create')
            object.__setattr__(self, '_Sum_value', create)
        elif exercise is not MISSING:
            object.__setattr__(self, '_Sum_name', 'exercise')
            object.__setattr__(self, '_Sum_value', exercise)
        elif fetch is not MISSING:
            object.__setattr__(self, '_Sum_name', 'fetch')
            object.__setattr__(self, '_Sum_value', fetch)
        elif get_time is not MISSING:
            object.__setattr__(self, '_Sum_name', 'get_time')
            object.__setattr__(self, '_Sum_value', get_time)
        elif embed_expr is not MISSING:
            object.__setattr__(self, '_Sum_name', 'embed_expr')
            object.__setattr__(self, '_Sum_value', embed_expr)
        elif lookup_by_key is not MISSING:
            object.__setattr__(self, '_Sum_name', 'lookup_by_key')
            object.__setattr__(self, '_Sum_value', lookup_by_key)
        elif fetch_by_key is not MISSING:
            object.__setattr__(self, '_Sum_name', 'fetch_by_key')
            object.__setattr__(self, '_Sum_value', fetch_by_key)

    @property
    def pure(self) -> 'Optional[Pure]':
        """this is purely for compact serialization -- specifically to
        reduce the AST depth. it adds no expressive power."""
        return self._Sum_value if self._Sum_name == 'pure' else None

    @property
    def block(self) -> 'Optional[Block]':
        return self._Sum_value if self._Sum_name == 'block' else None

    @property
    def create(self) -> 'Optional[Create]':
        return self._Sum_value if self._Sum_name == 'create' else None

    @property
    def exercise(self) -> 'Optional[Exercise]':
        return self._Sum_value if self._Sum_name == 'exercise' else None

    @property
    def fetch(self) -> 'Optional[Fetch]':
        return self._Sum_value if self._Sum_name == 'fetch' else None

    @property
    def get_time(self) -> 'Optional[Unit]':
        return self._Sum_value if self._Sum_name == 'get_time' else None

    @property
    def lookup_by_key(self) -> 'Optional[RetrieveByKey]':
        return self._Sum_value if self._Sum_name == 'lookup_by_key' else None

    @property
    def fetch_by_key(self) -> 'Optional[RetrieveByKey]':
        return self._Sum_value if self._Sum_name == 'fetch_by_key' else None

    @property
    def embed_expr(self) -> 'Optional[EmbedExpr]':
        """see similar constructor in `Scenario` on why this is useful."""
        return self._Sum_value if self._Sum_name == 'embed_expr' else None

    def Sum_match(
            self,
            pure: 'Callable[[Pure], T]',
            block: 'Callable[[Block], T]',
            create: 'Callable[[Create], T]',
            exercise: 'Callable[[Exercise], T]',
            fetch: 'Callable[[Fetch], T]',
            get_time: 'Callable[[Unit], T]',
            lookup_by_key: 'Callable[[RetrieveByKey], T]',
            fetch_by_key: 'Callable[[RetrieveByKey], T]',
            embed_expr: 'Callable[[EmbedExpr], T]') -> T:
        if self._Sum_name == 'pure':
            return pure(self._Sum_value)
        if self._Sum_name == 'block':
            return block(self._Sum_value)
        if self._Sum_name == 'create':
            return create(self._Sum_value)
        if self._Sum_name == 'exercise':
            return exercise(self._Sum_value)
        if self._Sum_name == 'fetch':
            return fetch(self._Sum_value)
        if self._Sum_name == 'get_time':
            return get_time(self._Sum_value)
        if self._Sum_name == 'lookup_by_key':
            return lookup_by_key(self._Sum_value)
        if self._Sum_name == 'fetch_by_key':
            return fetch_by_key(self._Sum_value)
        if self._Sum_name == 'embed_expr':
            return embed_expr(self._Sum_value)
        else:
            raise ValueError(f'Unknown Update.Sum case: {self._Sum_name}')


class Scenario:
    class Commit:
        party: 'Expr'
        expr: 'Expr'
        ret_type: 'Type'

        def __init__(self, party: 'Expr', expr: 'Expr', ret_type: 'Type'):
            self.party = party
            self.expr = expr
            self.ret_type = ret_type

    class EmbedExpr:
        type: 'Type'  # the expression should be of type `Scenario type`
        body: 'Expr'

        # noinspection PyShadowingBuiltins
        def __init__(self, type: 'Type', body: 'Expr'):
            self.type = type
            self.body = body

    __slots__ = '_Sum_name', '_Sum_value'

    def __init__(
            self,
            pure: 'Pure' = MISSING,
            block: 'Block' = MISSING,
            commit: 'Commit' = MISSING,
            must_fail_at: 'Commit' = MISSING,
            pass_: 'Expr' = MISSING,
            get_time: 'Unit' = MISSING,
            get_party: 'Expr' = MISSING,
            embed_expr: 'EmbedExpr' = MISSING):
        if pure is not MISSING:
            object.__setattr__(self, '_Sum_name', 'pure')
            object.__setattr__(self, '_Sum_value', pure)
        elif block is not MISSING:
            object.__setattr__(self, '_Sum_name', 'block')
            object.__setattr__(self, '_Sum_value', block)
        elif commit is not MISSING:
            object.__setattr__(self, '_Sum_name', 'commit')
            object.__setattr__(self, '_Sum_value', commit)
        elif must_fail_at is not MISSING:
            object.__setattr__(self, '_Sum_name', 'mustFailAt')
            object.__setattr__(self, '_Sum_value', must_fail_at)
        elif pass_ is not MISSING:
            object.__setattr__(self, '_Sum_name', 'pass')
            object.__setattr__(self, '_Sum_value', pass_)
        elif get_time is not MISSING:
            object.__setattr__(self, '_Sum_name', 'get_time')
            object.__setattr__(self, '_Sum_value', get_time)
        elif get_party is not MISSING:
            object.__setattr__(self, '_Sum_name', 'get_party')
            object.__setattr__(self, '_Sum_value', get_party)
        elif embed_expr is not MISSING:
            object.__setattr__(self, '_Sum_name', 'embed_expr')
            object.__setattr__(self, '_Sum_value', embed_expr)

    @property
    def pure(self) -> 'Optional[Pure]':
        """this is purely for compact serialization -- specifically to
        reduce the AST depth. it adds no expressive power."""
        return self._Sum_value if self._Sum_name == 'pure' else None

    @property
    def block(self) -> 'Optional[Block]':
        return self._Sum_value if self._Sum_name == 'block' else None

    @property
    def commit(self) -> 'Optional[Commit]':
        return self._Sum_value if self._Sum_name == 'create' else None

    @property
    def must_fail_at(self) -> 'Optional[Commit]':
        return self._Sum_value if self._Sum_name == 'mustFailAt' else None

    @property
    def pass_(self) -> 'Optional[Expr]':
        return self._Sum_value if self._Sum_name == 'pass' else None

    @property
    def get_time(self) -> 'Optional[Unit]':
        """The expression is of type `Text`."""
        return self._Sum_value if self._Sum_name == 'get_time' else None

    @property
    def get_party(self) -> 'Optional[Expr]':
        return self._Sum_value if self._Sum_name == 'get_party' else None

    @property
    def embed_expr(self) -> 'Optional[EmbedExpr]':
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
        return self._Sum_value if self._Sum_name == 'embed_expr' else None

    def Sum_match(
            self,
            pure: 'Callable[[Pure], T]',
            block: 'Callable[[Block], T]',
            commit: 'Callable[[Commit], T]',
            must_fail_at: 'Callable[[Commit], T]',
            pass_: 'Callable[[Expr], T]',
            get_time: 'Callable[[Unit], T]',
            get_party: 'Callable[[Expr], T]',
            embed_expr: 'Callable[[EmbedExpr], T]') -> T:
        if self._Sum_name == 'pure':
            return pure(self._Sum_value)
        if self._Sum_name == 'block':
            return block(self._Sum_value)
        if self._Sum_name == 'commit':
            return commit(self._Sum_value)
        if self._Sum_name == 'mustFailAt':
            return must_fail_at(self._Sum_value)
        if self._Sum_name == 'pass':
            return pass_(self._Sum_value)
        if self._Sum_name == 'get_time':
            return get_time(self._Sum_value)
        if self._Sum_name == 'get_party':
            return get_party(self._Sum_value)
        if self._Sum_name == 'embed_expr':
            return embed_expr(self._Sum_value)
        else:
            raise ValueError(f'unknown Scenario.Sum case: {self._Sum_name!r}')


class BuiltinFunction(Enum):
    CONCAT_LIST = -1000

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

    GENMAP_EMPTY = 124
    GENMAP_INSERT = 125
    GENMAP_LOOKUP = 126
    GENMAP_DELETE = 127
    GENMAP_KEYS = 128
    GENMAP_VALUES = 129
    GENMAP_SIZE = 130

    ADD_INT64 = 7
    SUB_INT64 = 8
    MUL_INT64 = 9
    DIV_INT64 = 10
    MOD_INT64 = 11
    EXP_INT64 = 12

    FOLDL = 20
    FOLDR = 21

    MAP_EMPTY = 96
    MAP_INSERT = 97
    MAP_LOOKUP = 98
    MAP_DELETE = 99
    MAP_TO_LIST = 100
    MAP_SIZE = 101

    EXPLODE_TEXT = 23
    APPEND_TEXT = 24

    ERROR = 25

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

    TO_TEXT_INT64 = 57
    TO_TEXT_DECIMAL = 58
    TO_TEXT_NUMERIC = 116
    TO_TEXT_TEXT = 60
    TO_TEXT_TIMESTAMP = 61
    TO_TEXT_DATE = 71
    TO_QUOTED_TEXT_PARTY = 63  # legacy, remove in next major version
    TO_TEXT_PARTY = 94  # Available Since version 1.2
    FROM_TEXT_PARTY = 95  # Available Since version 1.2
    FROM_TEXT_INT64 = 103  # Available Since version 1.5
    FROM_TEXT_DECIMAL = 104  # Available Since version 1.5
    FROM_TEXT_NUMERIC = 117
    SHA256_TEXT = 93  # Available Since version 1.2

    DATE_TO_UNIX_DAYS = 72  # Date -> Int64
    UNIX_DAYS_TO_DATE = 73  # Int64 -> Date

    TIMESTAMP_TO_UNIX_MICROSECONDS = 74  # Timestamp -> Int64
    UNIX_MICROSECONDS_TO_TIMESTAMP = 75  # Int64 -> Timestamp

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

    TRACE = 88

    COERCE_CONTRACT_ID = 102

    TO_TEXT_CODE_POINTS = 105
    FROM_TEXT_CODE_POINTS = 106

    TEXT_TO_UPPER = 9901
    TEXT_TO_LOWER = 9902
    TEXT_SLICE = 9903
    TEXT_SLICE_INDEX = 9904
    TEXT_CONTAINS_ONLY = 9905
    TEXT_REPLICATE = 9906
    TEXT_SPLIT_ON = 9907
    TEXT_INTERCALATE = 9908


class PrimCon(Enum):
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
    controllers: 'Expr'

    # Name to which the choice argument is bound and its type.
    arg_binder: 'VarWithType'

    # Return type of the choice.
    ret_type: 'Type'

    # Follow-up update of the choice. It has type `Update <ret_type>` and both
    # the template parameter and the choice parameter in scope.
    update: 'Expr'

    # Name to bind the ContractId of the contract this choice is exercised on to.
    self_binder: str

    location: 'Location'


@dataclass(init=False, frozen=True)
class KeyExpr:
    _Sum_name: str
    _Sum_value: 'Union[KeyExpr.Projections, KeyExpr.Record]'

    @dataclass(init=False, frozen=True)
    class Projections:
        projections: 'Sequence[KeyExpr.Projection]'

        def __init__(self, projections: 'Sequence[KeyExpr.Projection]'):
            object.__setattr__(self, 'projections', tuple(projections))

    @dataclass(init=False, frozen=True)
    class Projection:
        tycon: 'Type.Con'
        field: str

        def __init__(self, tycon: 'Type.Con', field: str):
            object.__setattr__(self, 'tycon', tycon)
            object.__setattr__(self, 'field', field)

    @dataclass(init=False, frozen=True)
    class Record:
        tycon: 'Type.Con'
        fields: 'Sequence[KeyExpr.RecordField]'

        def __init__(self, tycon: 'Type.Con', fields: 'Sequence[KeyExpr.RecordField]'):
            object.__setattr__(self, 'tycon', tycon)
            object.__setattr__(self, 'fields', tuple(fields))

    @dataclass(frozen=True)
    class RecordField:
        field: str
        expr: 'KeyExpr'

    def __init__(self, projections=MISSING, record=MISSING):
        if projections is not MISSING:
            object.__setattr__(self, '_Sum_name', 'projections')
            object.__setattr__(self, '_Sum_value', projections)
        elif record is not MISSING:
            object.__setattr__(self, '_Sum_name', 'record')
            object.__setattr__(self, '_Sum_value', record)
        else:
            raise ValueError('one of projections or record must be set')

    @property
    def projections(self) -> 'Optional[KeyExpr.Projections]':
        return self.projections if self._Sum_name == 'projections' else None

    @property
    def record(self) -> 'Optional[KeyExpr.Record]':
        return self.record if self._Sum_name == 'record' else None


@dataclass(frozen=True)
class DefTemplate:
    """Contract template definition"""

    @dataclass(frozen=True)
    class DefKey:
        type: 'Type'
        _key_expr_name: str
        _key_expr_value: Union[KeyExpr, Expr]
        maintainers: 'Expr'

        def __init__(
                self,
                type=MISSING,
                key=MISSING,
                complex_key=MISSING,
                maintainers=MISSING):
            object.__setattr__(self, 'type', type)
            if key is not MISSING:
                object.__setattr__(self, '_key_expr_name', 'key')
                object.__setattr__(self, '_key_expr_value', key)
            elif complex_key is not MISSING:
                object.__setattr__(self, '_key_expr_name', 'complex_key')
                object.__setattr__(self, '_key_expr_value', complex_key)
            else:
                raise ValueError('one of key/complex_key must be set')
            object.__setattr__(self, 'maintainers', maintainers)

        @property
        def key(self) -> 'Optional[KeyExpr]':
            return self._key_expr_value if self._key_expr_name == 'key' else None

        @property
        def complex_key(self) -> 'Optional[Expr]':
            return self._key_expr_value if self._key_expr_name == 'complex_key' else None

    # The type constructor for the template, acting as both
    # the name of the template and the type of the template argument.
    tycon: 'DottedName'

    # Name to which the template argument is bound.
    param: str

    # Optional pre-condition that the template argument must satisfy.
    # When present, it has type `Bool` and the template parameter in scope.
    precond: 'Expr'

    # The signatories of the contract. They have type `List Party` and the
    # template parameter in scope.
    signatories: 'Expr'

    # The agreement text associated with the contract. It has type `Text` and
    # the template parameter in scope.
    agreement: 'Expr'

    # The choices available in the resulting contract.
    choices: 'Sequence[TemplateChoice]'

    # The observers of the contract. They have type `List Party` and the
    # template parameter in scope.
    observers: 'Expr'

    location: 'Location'

    # The key definition for the template, if present
    key: 'Optional[DefKey]'


class DefDataType:

    class Fields:
        fields: 'Sequence[FieldWithType]'

        def __init__(self, fields: 'Sequence[FieldWithType]'):
            self.fields = fields

    class EnumConstructors:
        constructors: 'Sequence[str]'

        def __init__(self, constructors: 'Sequence[str]'):
            self.constructors = constructors

    name: DottedName
    params: 'Sequence[TypeVarWithKind]'
    _DataCons_name: str
    _DataCons_value: 'Fields'
    serializable: bool
    location: 'Location'

    def __init__(
            self,
            name: DottedName = MISSING,
            params: 'Sequence[TypeVarWithKind]' = MISSING,
            record: 'DefDataType.Fields' = MISSING,
            variant: 'DefDataType.Fields' = MISSING,
            enum: 'DefDataType.EnumConstructors' = MISSING,
            synonym: 'Type' = MISSING,
            serializable: bool = MISSING,
            location: 'Location' = MISSING):
        self.name = name
        self.params = params
        if record is not MISSING:
            self._DataCons_name = 'record'
            self._DataCons_value = record
        elif variant is not MISSING:
            self._DataCons_name = 'variant'
            self._DataCons_value = variant
        elif enum is not MISSING:
            self._DataCons_name = 'enum'
            self._DataCons_value = enum
        elif synonym is not MISSING:
            self._DataCons_name = 'synonym'
            self._DataCons_value = synonym
        self.serializable = serializable
        self.location = location

    @property
    def record(self) -> 'Optional[DefDataType.Fields]':
        return self._DataCons_value if self._DataCons_name == 'record' else None

    @property
    def variant(self) -> 'Optional[DefDataType.Fields]':
        return self._DataCons_value if self._DataCons_name == 'variant' else None

    @property
    def enum(self) -> 'Optional[DefDataType.EnumConstructors]':
        return self._DataCons_value if self._DataCons_name == 'enum' else None

    @property
    def synonym(self) -> 'Optional[Type]':
        return self._DataCons_value if self._DataCons_name == 'synonym' else None


@dataclass(frozen=True)
class DefValue:
    """Value definition"""

    class NameWithType:
        """
        The reason why we have this type instead of just flattening name and type in
        DefValue is that it was VarWithType before, and we want to be binary-compatible
        with it.
        """
        name: 'Sequence[str]'
        type: 'Type'

        # noinspection PyShadowingBuiltins
        def __init__(self, name: 'Sequence[str]', type: 'Type'):
            self.name = tuple(name)
            self.type = type

    name_with_type: 'DefValue.NameWithType'
    expr: 'Expr'

    # If true, the value must not contain any party literals and not reference
    # values which contain party literals.
    # This flag is used to simplify package validation by not requiring an
    # inference but only a check. Such a check must validate that this flag is
    # set correctly and that templates do not reference values which have this
    # flag set to false.
    no_party_literals: bool
    is_test: bool
    location: 'Optional[Location]'


@dataclass(frozen=True)
class FeatureFlags:
    forbidPartyLiterals: bool
    dontDivulgeContractIdsInCreateArguments: bool
    dontDiscloseNonConsumingChoicesToObservers: bool


@dataclass(frozen=True)
class Module:
    name: 'DottedName'
    flags: 'FeatureFlags'
    data_types: 'Sequence[DefDataType]'
    values: 'Sequence[DefValue]'
    templates: 'Sequence[DefTemplate]'


@dataclass(frozen=True)
class Package:
    modules: 'Sequence[Module]'


@dataclass(frozen=True)
class Archive:
    hash: str
    package: 'Package'
