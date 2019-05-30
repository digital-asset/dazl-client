# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains all of the magic for defining Expr and its subclasses.
"""

from typing import Dict, Any, Optional, NamedTuple, Set

from ..util.typing import unpack_optional

TRIGGER_ANY_TIME = 'TRIGGER_ANY_TIME'
TRIGGER_ON_INIT = 'TRIGGER_ON_INIT'

EQUALS = '='


class _Unquoted:
    __slots__ = ('value',)

    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


def coerce_type(cls, obj):
    core_optional_type = unpack_optional(cls)
    if core_optional_type is not None:
        if obj is None:
            return None
        else:
            return coerce_type(core_optional_type, obj)

    if hasattr(cls, 'coerce'):
        return cls.coerce(obj)
    return obj


class FieldInfo(NamedTuple):
    name: str
    assignment: str
    type_annotation: Any
    type_imports: Set[Any]


def _field_assignment(field_name, type_annotation) -> FieldInfo:
    optional_type = unpack_optional(type_annotation)
    if optional_type is not None:
        assignment = f'self.{field_name} = coerce_type({optional_type.__name__}, {field_name}) ' \
                     f'if {field_name} is not None else None'
        return FieldInfo(
            name=field_name,
            assignment=assignment,
            type_annotation=type_annotation,
            type_imports={optional_type})
    elif hasattr(type_annotation, '__name__'):
        return FieldInfo(
            name=field_name,
            assignment=f'self.{field_name} = coerce_type({type_annotation.__name__}, {field_name})',
            type_annotation=type_annotation,
            type_imports={type_annotation})
    else:
        # TODO: Should this emit a warning?
        return FieldInfo(
            name=field_name,
            assignment=f'self.{field_name} = {field_name}',
            type_annotation=type_annotation,
            type_imports=set())


def _define_expr_data_class(name: str, annotated_fields: Dict[str, Any]) -> Optional[type]:
    """
    Create a simple type that defines some basic

    :return:
    """

    if not annotated_fields:
        return None

    field_infos = [_field_assignment(field_name, type_annotation)
                   for field_name, type_annotation in annotated_fields.items()]
    type_annotations = {im for fi in field_infos for im in fi.type_imports}

    data_class = f'_{name}Data'
    init_arg_list = ', '.join(annotated_fields.keys())

    init_assignments = '\n        '.join(fi.assignment for fi in field_infos)
    repr_fields = ', '.join(f'{field}={{self.{field}}}' for field in annotated_fields)
    newargs = repr(tuple(_Unquoted(f'self.{field}') for field in annotated_fields))

    ns = dict(coerce_type=coerce_type)
    ns.update({typ.__name__: typ for typ in type_annotations})
    exec_locals = {}

    class_def = f'''
class {data_class}:
    def __init__(self, {init_arg_list}):
        {init_assignments}

    def __repr__(self):
        return f'<{name}({repr_fields})>'

    def __getnewargs__(self):
        return {newargs}
'''
    try:
        exec(class_def, ns, exec_locals)
    except:
        print('Failed to construct an Expr representation from this string:')
        print(class_def)
        raise

    type_def = exec_locals[data_class]
    type_def.__annotations__ = annotated_fields
    return type_def


class _ExprMeta(type):
    """
    Metaclass for :class:`Expr` instances. Not meant to be used directly by outside callers.

    This expects a :class:`NamedTuple`-style syntax class definition, and does all the magic
    to actually turn it into an implementation. The generated class is compatible with rewriting.
    """
    def __new__(mcs, name, bases, dct):
        data_base_class = _define_expr_data_class(name, dct.get('__annotations__', {}))
        if data_base_class is not None:
            bases = (data_base_class,) + bases
        return super().__new__(mcs, name, bases, dct)


class Expr(metaclass=_ExprMeta):
    """
    An expression.
    """

    @classmethod
    def coerce(cls, obj):
        if isinstance(obj, cls):
            return obj
        else:
            raise TypeError(f"Couldn't convert to a {cls.__name__!r}: {obj!r}")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    ################################################################################################
    # COMPARISON FUNCTIONS

    def __lt__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of a less-than comparison of this expression with
        another expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_LT
        return AppExpr(BUILTIN_LT, (self, exprify_value(other)))

    def __le__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of a less-than-or-equal comparison of this
        expression with another expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_LE
        return AppExpr(BUILTIN_LE, (self, exprify_value(other)))

    def __eq__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of comparing this expression with another
        expression for equality.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_EQ
        return AppExpr(BUILTIN_EQ, (self, exprify_value(other)))

    def __ne__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of comparing this expression with another
        expression for inequality.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_NE
        return AppExpr(BUILTIN_NE, (self, exprify_value(other)))

    def __gt__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of a greater-than comparison of this expression with
        another expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_GT
        return AppExpr(BUILTIN_GT, (self, exprify_value(other)))

    def __ge__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of a greater-than-or-equal comparison of this
        expression with another expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_GE
        return AppExpr(BUILTIN_GE, (self, exprify_value(other)))

    ################################################################################################
    # MATHEMATICAL FUNCTIONS

    def __add__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of summing this expression with another expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_ADD
        return AppExpr(BUILTIN_ADD, (self, exprify_value(other)))

    def __sub__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of subtracting another expression from this
        expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_SUB
        return AppExpr(BUILTIN_SUB, (self, exprify_value(other)))

    def __mul__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of multiplying this expression by another
        expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_MUL
        return AppExpr(BUILTIN_MUL, (self, exprify_value(other)))

    def __truediv__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of dividing this expression by another
        expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_MUL
        return AppExpr(BUILTIN_MUL, (self, exprify_value(other)))

    def __concat__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of summing this expression with another expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_CONCAT
        return AppExpr(BUILTIN_CONCAT, (self, exprify_value(other)))

    def __pow__(self, other: 'Expr') -> 'Expr':
        """
        Return an expression that is the result of raising this expression by another expression.
        """
        from .expr_impl import AppExpr
        from .builtins import BUILTIN_POW
        return AppExpr(BUILTIN_POW, (self, exprify_value(other)))


def exprify_args(arguments):
    return {key: exprify_value(value) for key, value in arguments.items()}


def exprify_value(value):
    """
    Converts the specified unknown value to a subclass of `Expr` that is suitable to be used as an
    argument to a contract creation or choice exercising.
    """
    from .expr_impl import ConstantExpr, GetContractIdExpr, TemplateExpr, TemplateSelectExpr
    if isinstance(value, (TemplateExpr, TemplateSelectExpr)):
        # in an argument context, a bare template reference actually needs to resolve to the
        # contract ID of the default alias for a given template ID
        return GetContractIdExpr.coerce(value)

    elif isinstance(value, Expr):
        return value

    return ConstantExpr(value)
