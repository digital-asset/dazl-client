# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains definitions for built-in DAML functions.
"""

import operator

from datetime import timedelta
from decimal import Decimal, ROUND_HALF_EVEN
from functools import reduce
from typing import Any, Callable, Optional, Union


_ONE = Decimal('1')
_ONE_THOUSAND = Decimal('1000')
_BUILTINS = dict()


class FunctionMetadata:
    name: str
    impl: Callable[..., Any]
    infix: bool

    def __init__(self, name, impl, infix):
        self.name = name
        self.impl = impl
        self.infix = infix


def define_builtin(symbol: str, fn: Callable[..., Any], infix: bool=False):
    func_metadata = FunctionMetadata(symbol, fn, infix)
    _BUILTINS[symbol] = func_metadata
    return func_metadata


def lookup_builtin(symbol: str) -> Optional['FunctionMetadata']:
    return _BUILTINS.get(symbol)


def foldl(func, acc, xs):
    return reduce(func, xs, acc)


def foldr(func, acc, xs):
    return reduce(lambda x, y: func(y, x), xs[::-1], acc)


def lookup(label, record):
    return record[label]


def extend(label: str, value: Any, record: dict) -> dict:
    new_record = dict(record)
    new_record[label] = value
    return new_record


def tag(label: str, value: Any) -> dict:
    return {label: value}


def round_(value):
    return Decimal(value).quantize(_ONE, ROUND_HALF_EVEN)


def exercises(parameter_count: int, choice_name: str, party: str, contract_id: 'ContractId', *arguments) -> 'Update':
    pass


def commit(party: str, update: 'Update') -> 'Scenario':
    pass


def n_arity(fn):
    return lambda *xs: reduce(fn, xs)


def from_relative_time(value: timedelta) -> Decimal:
    return Decimal(value._to_microseconds()) * _ONE_THOUSAND


def to_relative_time(value: Union[int, float]) -> timedelta:
    # TODO: This is a very lossy conversion; not clear what the best way to handle this is absent
    # a subclassing of ``timedelta``
    return timedelta(microseconds=float(Decimal(value) / _ONE_THOUSAND))


BUILTIN_ADD = define_builtin('+', n_arity(operator.add), infix=True)
BUILTIN_SUB = define_builtin('-', operator.sub, infix=True)
BUILTIN_MUL = define_builtin('*', n_arity(operator.mul), infix=True)
BUILTIN_DIV = define_builtin('/', operator.truediv, infix=True)
BUILTIN_POW = define_builtin('^', pow, infix=True)
BUILTIN_LT = define_builtin('<', operator.lt, infix=True)
BUILTIN_LE = define_builtin('<=', operator.le, infix=True)
BUILTIN_GT = define_builtin('>', operator.gt, infix=True)
BUILTIN_GE = define_builtin('>=', operator.ge, infix=True)
BUILTIN_EQ = define_builtin('==', operator.eq, infix=True)
BUILTIN_NE = define_builtin('/=', operator.ne, infix=True)
BUILTIN_AND = define_builtin('&&', n_arity(operator.and_), infix=True)
BUILTIN_OR = define_builtin('||', n_arity(operator.or_), infix=True)
BUILTIN_CONCAT = define_builtin('<>', n_arity(operator.add), infix=True)
# overlay

define_builtin('toText', str)
define_builtin('singleton', str)
define_builtin('unpack', list)
define_builtin('fromRelTime', from_relative_time)
define_builtin('toRelTime', to_relative_time)
define_builtin('fromInteger', Decimal)
define_builtin('toInteger', int)

define_builtin('round', round_)
define_builtin('divD', operator.truediv)
define_builtin('remD', operator.mod)

BUILTIN_NOT = define_builtin('not', operator.not_)
define_builtin('or', operator.or_)
define_builtin('and', operator.and_)

define_builtin('nil', lambda: [])
define_builtin('cons', lambda x, xs: xs + [x])
define_builtin('foldl', foldl)
define_builtin('foldr', foldr)

define_builtin('lookup', lookup)
define_builtin('extend', extend)
define_builtin('tag', tag)
define_builtin('exercises', exercises)
define_builtin('commit', commit)

define_builtin('create', lambda *args, **kwargs: None)
define_builtin('delete', lambda *args, **kwargs: None)
define_builtin('pure', lambda *args, **kwargs: None)
define_builtin('assert', lambda *args, **kwargs: None)
