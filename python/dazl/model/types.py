# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Type system types
------------------

The :mod:`dazl.model.types` module contains the Python classes used to represent the DAML type
system.

+----------------------+---------------------------+
| DAML type            | Python type               |
+======================+===========================+
| ``Bool``             | ``bool``                  |
+----------------------+---------------------------+
| ``Int``              | ``int``                   |
+----------------------+---------------------------+
| ``Decimal``          | ``decimal.Decimal``       |
+----------------------+---------------------------+
| ``[a]``              | ``list``                  |
+----------------------+---------------------------+

.. autoclass:: Type
.. autoclass:: ScalarType
.. autoclass:: ListType
.. autoclass:: RecordType
.. autoclass:: VariantType
.. autoclass:: UnsupportedType
"""

from enum import Flag
from typing import Any, Callable, Collection, Dict, Optional, Sequence, Tuple, TypeVar, Union, \
    TYPE_CHECKING

from .. import LOG
from ..model.core import ContractData, Party
from ..util.typing import safe_cast, safe_dict_cast, safe_optional_cast

DottedNameish = Union[str, Sequence[str]]

if TYPE_CHECKING:
    from .types_store import PackageStore
    from ..damlast.daml_lf_1 import Expr


def dotted_name(obj: DottedNameish) -> Sequence[str]:
    """
    Sanitize a string or a tuple of strings to a dotted name.

    :param obj: A string or tuple of strings.
    :return: A tuple of strings.
    """
    if obj is None:
        raise ValueError('DottedName must be a non-None value')
    if isinstance(obj, str):
        return tuple(obj.split('.'))
    if isinstance(obj, Collection):
        for item in obj:
            if not isinstance(item, str):
                raise ValueError("DottedName's components must all be strings")
        return tuple(obj)
    else:
        raise ValueError('could not convert to a sequence of str: {obj!r}')


class NamedArgumentList(tuple):
    """
    A simple tuple to storing (name, value) pairs.
    """

    @property
    def names(self):
        return set(name for name, _ in self)


T = TypeVar('T')


def type_dispatch_table(
        on_type_ref: Callable[['TypeReference'], T],
        on_type_var: Callable[['TypeVariable'], T],
        on_type_app: Callable[['TypeApp'], T],
        on_scalar: Callable[['ScalarType'], T],
        on_contract_id: Callable[['ContractIdType'], T],
        on_optional: Callable[['OptionalType'], T],
        on_list: Callable[['ListType'], T],
        on_map: 'Callable[[MapType], T]',
        on_record: Callable[['RecordType'], T],
        on_variant: Callable[['VariantType'], T],
        on_enum: 'Callable[[EnumType], T]',
        on_unsupported: Callable[['UnsupportedType'], T]) -> Callable[['Type'], T]:
    def _impl(tt: Type):
        if isinstance(tt, TypeReference):
            return on_type_ref(tt)
        elif isinstance(tt, TypeVariable):
            return on_type_var(tt)
        elif isinstance(tt, TypeApp):
            return on_type_app(tt)
        elif isinstance(tt, ScalarType):
            return on_scalar(tt)
        elif isinstance(tt, ContractIdType):
            return on_contract_id(tt)
        elif isinstance(tt, OptionalType):
            return on_optional(tt)
        elif isinstance(tt, ListType):
            return on_list(tt)
        elif isinstance(tt, MapType):
            return on_map(tt)
        elif isinstance(tt, RecordType):
            return on_record(tt)
        elif isinstance(tt, VariantType):
            return on_variant(tt)
        elif isinstance(tt, EnumType):
            return on_enum(tt)
        elif isinstance(tt, UnsupportedType):
            return on_unsupported(tt)
        else:
            # note to maintainers: if you modify the Type hierarchy, you must also maintain this
            # poor man's pattern match over the hierarchy
            LOG.error('Incomplete implementation of type_match! (when handling %r)', tt)
            raise Exception(f'unknown Type subclass: {tt!r}')
    return _impl


def scalar_type_dispatch_table(
        on_unit: Callable[[], T],
        on_bool: Callable[[], T],
        on_text: Callable[[], T],
        on_int: Callable[[], T],
        on_decimal: Callable[[], T],
        on_party: Callable[[], T],
        on_date: Callable[[], T],
        on_datetime: Callable[[], T],
        on_timedelta: Callable[[], T]) -> Callable[['ScalarType'], T]:
    def _impl(tt: ScalarType):
        st = safe_cast(ScalarType, tt)
        if st == SCALAR_TYPE_UNIT:
            return on_unit()
        elif tt == SCALAR_TYPE_BOOL:
            return on_bool()
        elif tt == SCALAR_TYPE_TEXT or tt == SCALAR_TYPE_CHAR:
            return on_text()
        elif tt == SCALAR_TYPE_INTEGER:
            return on_int()
        elif tt == SCALAR_TYPE_DECIMAL:
            return on_decimal()
        elif tt == SCALAR_TYPE_PARTY:
            return on_party()
        elif tt == SCALAR_TYPE_DATE:
            return on_date()
        elif tt == SCALAR_TYPE_DATETIME:
            return on_datetime()
        elif tt == SCALAR_TYPE_RELTIME:
            return on_timedelta()
        else:
            # note to maintainers: if you modify the set of ScalarType instances, you must also
            # maintain this poor man's pattern match over the hierarchy
            LOG.error('Incomplete implementation of scalar_type_dispatch_table! (when handling %r)',
                      tt)
            raise Exception(f'unknown ScalarType: {tt!r}')
    return _impl


class Type:
    """
    A DAML-defined type.
    """

    def __str__(self):
        from ..pretty import DAML_PRETTY_PRINTER
        return DAML_PRETTY_PRINTER.visit_type(self)


class TypeApp(Type):
    """
    An application of one or more types to an open type.

    This is basically Type.Con in the Protobuf declaration.
    """

    def __init__(self, body: Type, arguments: Sequence[Type]):
        if not isinstance(body, Type):
            raise ValueError(f'a Type is required here (got {body} instead)')
        if not arguments:
            raise ValueError('at least one type argument is required in a TypeApp')
        self.body = body
        self.arguments = tuple(arguments)

    def __repr__(self):
        return f"<TypeApp(body={self.body}, arguments={self.arguments}>"


class _Reference:
    """
    A reference to another type.

    This is basically TypeConName in the Protobuf declaration.
    """
    __slots__ = ('module', 'name')

    module: 'ModuleRef'
    name: 'Sequence[str]'

    def __init__(self, module: 'ModuleRef', name: 'Sequence[str]'):
        from collections import Collection
        if not isinstance(name, Collection):
            raise TypeError(f'Tuple of strings required here (got {name!r} instead)')

        self.module = safe_cast(ModuleRef, module)
        self.name = tuple(name)  # type: Tuple[str, ...]

    @property
    def full_name(self):
        return '.'.join((*self.module.module_name, *self.name))

    @property
    def full_name_unambiguous(self):
        return '.'.join(self.module.module_name) + ':' + '.'.join(self.name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and \
               self.module == other.module and self.name == other.name

    def __ne__(self, other):
        return not isinstance(other, type(self)) or \
               self.module != other.module or self.name != other.name

    def __lt__(self, other):
        return self.module < other.module or \
               (self.module == other.module and self.name < other.name)

    def __le__(self, other):
        return self.module <= other.module or \
               (self.module == other.module and self.name <= other.name)

    def __gt__(self, other):
        return self.module > other.module or \
               (self.module == other.module and self.name > other.name)

    def __ge__(self, other):
        return self.module >= other.module or \
               (self.module == other.module and self.name >= other.name)

    def __hash__(self):
        return hash(self.module) ^ hash(self.name)

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return f"{self.full_name}@{self.module.package_id}"


class TypeReference(Type, _Reference):
    pass


class ValueReference(_Reference):
    pass


class TypeVariable(Type):
    """
    An unbound type in a Type expression.
    """
    __slots__ = 'name',

    def __init__(self, name: str):
        self.name = safe_cast(str, name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"TypeVariable({self.name})"

    def __eq__(self, other):
        return isinstance(other, TypeVariable) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class UnresolvedTypeReference(Type):
    """
    A reference that may or may not ultimately resolve to a type.
    """

    def __init__(self, name: str):
        self.name = safe_cast(str, name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<UnresolvedTypeReference({self.name!r})>'

    def __eq__(self, other):
        return isinstance(other, UnresolvedTypeReference) and self.name == other.name

    def __hash__(self):
        return hash((UnresolvedTypeReference, self.name))


class ConcreteType(Type):
    @property
    def adjective(self) -> 'TypeAdjective':
        raise NotImplementedError


class ScalarType(ConcreteType):
    """
    A DAML-defined type that represents a simple scalar value. You should not need to ever
    construct instances of this directly; all scalar types are builtins.
    """

    __slots__ = 'name',

    def __init__(self, name: str):
        """
        Construct an object that references a scalar DAML type.

        :param name: The name of this type as it is known in DAML.
        """
        self.name = safe_cast(str, name)

    @property
    def adjective(self):
        return TypeAdjective.DAML_BUILTIN

    def __repr__(self):
        """
        Return the DAML name of this type.
        """
        return self.name

    def __hash__(self):
        return hash((ScalarType, self.name))

    def __eq__(self, other):
        return isinstance(other, ScalarType) and self.name == other.name


class _BuiltInParameterizedType(ConcreteType):
    """
    Convenience class that encapsulates commonalities for the built-in types that have one type
    parameter.
    """
    __slots__ = ('type_parameter',)

    def __init__(self, type_parameter: Type):
        self.type_parameter = safe_cast(Type, type_parameter)

    @property
    def adjective(self):
        return TypeAdjective.DAML_BUILTIN

    def __repr__(self):
        py_type = type(self).__name__
        return f'<{py_type}({self.type_parameter!r})>'


class ContractIdType(_BuiltInParameterizedType):
    pass


class ListType(_BuiltInParameterizedType):
    pass


class MapType(ConcreteType):
    """
    A DAML-defined Map.

    Instance attributes:

    .. attribute: MapType.key_type

        The type of keys in this map.

    .. attribute: MapType.value_type

        The type of values in this map.

    .. attribute: MapType.internal_type

        The behind-the-scenes type that this :class:`MapType` is supposed to stand in as in context.
        This field should only be used by wire serializers and never be used for processing
        user-facing data.
    """
    __slots__ = ('key_type', 'value_type', 'internal_type')

    def __init__(self, key_type: Type, value_type: Type, internal_type: 'Optional[Type]' = None):
        self.key_type = safe_cast(Type, key_type)
        self.value_type = safe_cast(Type, value_type)
        self.internal_type = safe_optional_cast(Type, internal_type)

    @property
    def adjective(self):
        return TypeAdjective.DAML_BUILTIN

    def __repr__(self):
        py_type = type(self).__name__
        return f'<{py_type}({self.key_type!r}, {self.value_type!r})>'


class OptionalType(_BuiltInParameterizedType):
    """
    A DAML-defined Optional.

    Instance attributes:

    .. attribute: OptionalType.type_parameter

        The type of value in the Optional.

    .. attribute: OptionalType.internal_type

        The behind-the-scenes type that this :class:`MapType` is supposed to stand in as in context.
        This field should only be used by wire serializers and never be used for processing
        user-facing data.
    """
    __slots__ = 'internal_type',

    def __init__(self, type_parameter: Type, internal_type: 'Optional[Type]' = None):
        super().__init__(type_parameter)
        self.internal_type = safe_optional_cast(Type, internal_type)


class UpdateType(_BuiltInParameterizedType):
    pass


class ForAllType(Type):
    def __init__(self, type_vars, body_type):
        self.type_vars = type_vars
        self.body_type = body_type

    def __repr__(self):
        return f'<ForAllType({self.type_vars}, {self.body_type})>'


class _CompositeDataType(ConcreteType):
    """
    Either a :class:`RecordType` (product type) or a :class:`VariantType` (sum type).
    """

    def __init__(self,
                 named_args: 'NamedArgumentList',
                 name: 'Optional[TypeReference]',
                 type_args: 'Sequence[TypeVariable]',
                 adjective: 'TypeAdjective'):
        if type(self) == _CompositeDataType:
            raise Exception('_CompositeDataType cannot be constructed')
        if not isinstance(named_args, NamedArgumentList):
            raise TypeError('NamedArgumentList required here')
        if name is not None and not isinstance(name, TypeReference):
            raise TypeError('name must be a TypeReference or None')

        self.named_args = named_args
        self.name = name
        self.type_args = tuple(type_args)
        self._adjective = adjective

    @property
    def adjective(self):
        return self._adjective

    def field_type(self, name: str) -> Type:
        for key, value_type in self.named_args:
            if key == name:
                return value_type

        raise ValueError(f'field or constructor {name!r} not found in {self}')

    def __repr__(self):
        py_type = type(self).__name__

        name = '(anonymous)' if self.name is None else self.name
        full_name = ''.join(f' {v}' for v in ((name,) + self.type_args))

        return f'<{py_type}:{full_name} {self.named_args}>'


class FunctionType(Type):
    """
    Representation of a DAML function signature.

    Instances of this type aren't practically usable from this library. They are merely recorded in
    order to faithfully pretty-print metadata.
    """
    def __init__(self, parameters: Sequence[Type], result: Type):
        self.parameters = tuple(parameters)
        self.result = safe_cast(Type, result)

    def __str__(self):
        from io import StringIO
        with StringIO() as buf:
            for param in self.parameters:
                buf.write(str(param))
                buf.write(' -> ')
            buf.write(str(self.result))
            return buf.getvalue()

    def __repr__(self):
        return f'<FunctionType({self})>'


class RecordType(_CompositeDataType):

    def as_args_list(self):
        return self.named_args


class VariantType(_CompositeDataType):

    def as_args_list(self):
        return self.named_args

    def _find_ctor(self, constructor_name: str) -> Type:
        return self.field_type(constructor_name)


class EnumType(ConcreteType):

    __slots__ = 'constructors',

    def __init__(self, name: 'Optional[TypeReference]', constructors: 'Collection[str]'):
        self.name = name
        self.constructors = constructors

    @property
    def adjective(self) -> 'TypeAdjective':
        return TypeAdjective.USER_DEFINED


class UnsupportedType(Type):
    """
    A DAML type that is currently unparseable by the Python client library.
    """
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = safe_cast(str, name)

    def __repr__(self):
        return f'<UnsupportedType({self.name})>'


class ModuleRef:
    """
    A reference to a module.
    """
    __slots__ = ('package_id', 'module_name')

    def __init__(self, package_id: str, module_name: DottedNameish):
        self.package_id = safe_cast(str, package_id)
        self.module_name = dotted_name(module_name)

    def __eq__(self, other):
        return isinstance(other, ModuleRef) and \
               self.package_id == other.package_id and \
               self.module_name == other.module_name

    def __lt__(self, other):
        return self.package_id < other.package_id or \
               (self.package_id == other.package_id and self.module_name < other.module_name)

    def __le__(self, other):
        return self.package_id < other.package_id or \
               (self.package_id == other.package_id and self.module_name <= other.module_name)

    def __gt__(self, other):
        return self.package_id > other.package_id or \
               (self.package_id == other.package_id and self.module_name > other.module_name)

    def __ge__(self, other):
        return self.package_id > other.package_id or \
               (self.package_id == other.package_id and self.module_name >= other.module_name)

    def __hash__(self):
        return hash(self.package_id) ^ hash(self.module_name)

    def __repr__(self):
        return f'ModuleRef(package_id={self.package_id!r}, ' \
            f'module_name={".".join(self.module_name)!r})'


class Template:
    """
    Definition of a contract template.
    """

    def __init__(
            self,
            data_type: 'RecordType',
            key_type: 'Optional[Type]',
            choices: 'Collection[TemplateChoice]',
            observers: 'Expr',
            signatories: 'Expr',
            agreement: 'Expr',
            ensure: 'Expr'):
        if not isinstance(data_type, RecordType) or data_type.name is None:
            raise ValueError(f'data_type is required and must be a named record type '
                             f'(got {data_type})')
        self.data_type = safe_cast(RecordType, data_type)
        self.key_type = safe_optional_cast(Type, key_type)
        self.choices = choices
        self._observers = observers
        self._signatories = signatories
        self._agreement = agreement
        self._ensure = ensure

    def signatories(self, store: 'PackageStore', cdata: ContractData) -> Collection[Party]:
        from ..damlast.eval_scope import EvaluationScope
        from ..damlast.eval2 import Evaluator
        from ..damlast.pretty_print import pretty_print

        scope = EvaluationScope(store, {}) #{'this': cdata})
        print('Trying to evaluate:')
        print(pretty_print(scope, self._signatories))
        print('-')
        print(repr(self._signatories))
        print('-')
        print('')
        print('now here we go')
        return Evaluator(store, {'this': Evaluator.Constant(cdata)}, {}).eval_Expr(self._signatories)

    def observers(self, store: 'PackageStore', cdata: ContractData) -> Collection[Party]:
        from ..damlast import DamlPrettyPrintVisitor, CSharpPrettyPrintVisitor
        from ..damlast.expand import ExpandVisitor, SimplifyVisitor
        pp = CSharpPrettyPrintVisitor(store)
        ex = ExpandVisitor(store, always_expand=False)
        sp = SimplifyVisitor(store)

        expr = sp.visit_expr(ex.visit_expr(self._observers))
        print(pp.visit_expr(expr))


        return Evaluator(store, {'this': Evaluator.Constant(cdata)}, {}).eval_Expr(self._observers)

    def agreement(self, store: 'PackageStore', cdata: ContractData) -> str:
        """
        Return ths text of the agreement of this :class:`Template` from a contract data.

        :param cdata:
            An object that represents the record that describe the fields of this template.
        :return:
            The agreement string.
        """
        from ..damlast.eval_scope import EvaluationScope
        from ..damlast.eval2 import Evaluator
        from ..damlast.pretty_print import pretty_print

        scope = EvaluationScope(store, {}) #{'this': cdata})
        print('Trying to evaluate:')
        print(pretty_print(scope, self._signatories))
        print('-')
        print(repr(self._signatories))
        print('-')
        print('')
        print('now here we go')
        #fn = Evaluator(store, {}, {}).eval_Expr(self._agreement)
        #return fn(Evaluator.Constant(cdata))
        expr = Evaluator(store, {'this': Evaluator.Constant(cdata)}, {}).eval_Expr(self._agreement)
        return expr

    def ensure(self, store: 'PackageStore', cdata: 'ContractData') -> bool:
        from ..damlast import DamlPrettyPrintVisitor
        from ..damlast.expand import ExpandVisitor, SimplifyVisitor
        pp = DamlPrettyPrintVisitor()
        ex = ExpandVisitor(
            store,
            always_expand=True,
            val_blacklist=[ValueReference(
                module=ModuleRef('993b6de82f6297d2a618f0ac17e6c3c4173baf04f1903481f236dd8bf4c64554',
                                 module_name=('DA', 'Internal', 'Prelude')),
                name=('concat',))])
        sp = SimplifyVisitor(store)

        expr = sp.visit_expr(ex.visit_expr(self._ensure))
        print(pp.visit_expr(expr))


class TemplateChoice:
    __slots__ = ('name', 'consuming', 'data_type', '_controllers')

    def __init__(self, name: str, consuming: bool, data_type: Type, controllers: 'Expr'):
        self.name = name
        self.consuming = consuming
        self.data_type = data_type
        self._controllers = controllers

    @property
    def type(self):
        return self.data_type

    def controllers(self, cdata: ContractData) -> Collection[Party]:
        """
        Return every :class:`Party` that can exercise this choice given the specified contract data.
        """

C = TypeVar('C', RecordType, VariantType)


def as_commands(commands_ish, allow_callables=False):
    """
    Converts something that is either ``None``, a single :class:`Command`, or an iterable over
    :class:`Command` objects to a ``list`` of :class:`Command`.

    :param commands_ish:
        Something that might be construed as either a :class:`Command` or an iterable over
        :class:`Command`.
    :param allow_callables:
        If callables are encountered, invoke them and expect them to return something that can be
        easily serialized to a :class:`Command`.
    """
    from .writing import Command

    if commands_ish is None:
        return ()
    elif isinstance(commands_ish, Command):
        return (commands_ish,)
    elif allow_callables and callable(commands_ish):
        return as_commands(commands_ish(), allow_callables=False)

    # assume this is some kind of iterable structure, where everything needs to be a Command
    cmds = []
    for command in commands_ish:
        if allow_callables and callable(command):
            cmds.extend(as_commands(command(), allow_callables=False))
        elif isinstance(command, Command):
            cmds.append(command)
        else:
            raise TypeError(f'{command!r} is not a Command')
    return tuple(cmds)


def as_contract_id(cid, template_id=None):
    """
    Convert something that resembles a contract ID to a :class:`ContractId` or
    :class:`RelativeContractRef`.
    """
    from .core import ContractId

    if cid is None:
        raise ValueError('cid is required')
    elif isinstance(cid, str):
        return ContractId(cid, template_id)
    elif isinstance(cid, ContractId):
        return cid

    raise TypeError('Could not serialize an object to a contract ID: {!r}'.format(cid))


SCALAR_TYPE_UNIT = ScalarType('Unit')
SCALAR_TYPE_BOOL = ScalarType('Bool')
SCALAR_TYPE_CHAR = ScalarType('Char')
SCALAR_TYPE_INTEGER = ScalarType('Integer')
SCALAR_TYPE_DECIMAL = ScalarType('Decimal')
SCALAR_TYPE_TEXT = ScalarType('Text')
SCALAR_TYPE_PARTY = ScalarType('Party')
SCALAR_TYPE_RELTIME = ScalarType('RelTime')
SCALAR_TYPE_DATE = ScalarType('Date')
SCALAR_TYPE_TIME = ScalarType('Time')
SCALAR_TYPE_DATETIME = SCALAR_TYPE_TIME

ScalarType.BUILTINS = [
    SCALAR_TYPE_BOOL,
    SCALAR_TYPE_CHAR,
    SCALAR_TYPE_INTEGER,
    SCALAR_TYPE_DECIMAL,
    SCALAR_TYPE_TEXT,
    SCALAR_TYPE_PARTY,
    SCALAR_TYPE_RELTIME,
    SCALAR_TYPE_DATE,
    SCALAR_TYPE_TIME,
]


class TypeEvaluationContext:
    references: Dict[TypeReference, Type]
    variables: Dict[TypeVariable, Type]
    path: Sequence[Union[TypeReference, str]]

    __slots__ = ('references', 'variables', 'path')

    @classmethod
    def from_store(cls, store: 'PackageStore') -> 'TypeEvaluationContext':
        return cls(store.find_types(), {}, ())

    def __init__(self, references, variables, path):
        self.references = safe_dict_cast(TypeReference, Type, references)
        self.variables = safe_dict_cast(TypeVariable, Type, variables)
        self.path = path

    def append_path(self, component: Union[TypeReference, str]) -> 'TypeEvaluationContext':
        return TypeEvaluationContext(
            references=self.references,
            variables=self.variables,
            path=tuple((*self.path, component)))

    def resolve_var(self, var: TypeVariable) -> Type:
        return self.variables[var]

    def with_vars(self, new_vars: Dict[TypeVariable, Type]) -> 'TypeEvaluationContext':
        confirmed_new_vars = {}
        for new_var, new_var_value in new_vars.items():
            if new_var == new_var_value:
                # TODO: Why do these cases happen?
                continue
            confirmed_new_vars[new_var] = new_var_value

        return TypeEvaluationContext(
            references=self.references,
            variables={**self.variables, **confirmed_new_vars},
            path=self.path)


def type_evaluate_dispatch(
        on_scalar: 'Callable[[TypeEvaluationContext, ScalarType], T]',
        on_contract_id: 'Callable[[TypeEvaluationContext,  ContractIdType], T]',
        on_optional: 'Callable[[TypeEvaluationContext, OptionalType], T]',
        on_list: 'Callable[[TypeEvaluationContext, ListType], T]',
        on_map: 'Callable[[TypeEvaluationContext, MapType], T]',
        on_record: 'Callable[[TypeEvaluationContext, RecordType], T]',
        on_variant: 'Callable[[TypeEvaluationContext, VariantType], T]',
        on_enum: 'Callable[[TypeEvaluationContext, EnumType], T]',
        on_unsupported: 'Callable[[TypeEvaluationContext, UnsupportedType], T]') \
            -> 'Callable[[TypeEvaluationContext, Type], T]':
    """
    Produce a function that defers handling of core types to the passed in functions.

    The cases of :class:`TypeReference, :class:`TypeApp`, and :class:`TypeVariable` are handled
    automatically. Note, though that ultimately type evaluation is only performed at one level
    deep, and the produced function may need to be called multiple types at multiple depths of an
    object or type hierarchy.
    """
    def _impl(context, tt):
        resolve_depth = 0
        while isinstance(tt, (TypeReference, TypeVariable, TypeApp)):
            context, tt = single_reduce(context, tt)
            resolve_depth += 1
            if resolve_depth > 10:
                raise Exception('hit our max resolve depth, which is probably not so great')

        def error(_: Any) -> T: raise Exception()

        context, tt = annotate_context(context, tt)

        return type_dispatch_table(
            error, error, error,
            lambda st: on_scalar(context, st),
            lambda ct: on_contract_id(context, ct),
            lambda ot: on_optional(context, ot),
            lambda lt: on_list(context, lt),
            lambda mt: on_map(context, mt),
            lambda rt: on_record(context, rt),
            lambda vt: on_variant(context, vt),
            lambda et: on_enum(context, et),
            lambda ut: on_unsupported(context, tt))(tt)
    return _impl


def _type_evaluate_dispatch_error(_, __):
    raise Exception()


def type_evaluate_dispatch_default_error(
        on_scalar: Callable[['TypeEvaluationContext', 'ScalarType'], T] = _type_evaluate_dispatch_error,
        on_contract_id: Callable[['TypeEvaluationContext',  'ContractIdType'], T] = _type_evaluate_dispatch_error,
        on_optional: Callable[['TypeEvaluationContext',  'OptionalType'], T] = _type_evaluate_dispatch_error,
        on_list: Callable[['TypeEvaluationContext', 'ListType'], T] = _type_evaluate_dispatch_error,
        on_map: Callable[['TypeEvaluationContext', 'MapType'], T] = _type_evaluate_dispatch_error,
        on_record: Callable[['TypeEvaluationContext', 'RecordType'], T] = _type_evaluate_dispatch_error,
        on_variant: Callable[['TypeEvaluationContext', 'VariantType'], T] = _type_evaluate_dispatch_error,
        on_enum: 'Callable[[TypeEvaluationContext, EnumType], T]' = _type_evaluate_dispatch_error,
        on_unsupported: 'Callable[[TypeEvaluationContext, UnsupportedType], T]' = _type_evaluate_dispatch_error):
    return type_evaluate_dispatch(
        on_scalar, on_contract_id, on_optional, on_list, on_map, on_record, on_variant, on_enum,
        on_unsupported)


def single_reduce(context: TypeEvaluationContext, tt: Type) -> 'Tuple[TypeEvaluationContext, Type]':
    """
    Apply a single substitution/reduction/unwrapping. The context may be augmented with additional
    variables if a TypeApp is encountered.
    """
    def identity(t): return context, t

    def reduce_app(ta: TypeApp) -> 'Tuple[TypeEvaluationContext, Type]':
        body = context.references[ta.body] if isinstance(ta.body, TypeReference) else ta.body
        if not isinstance(body, (RecordType, VariantType)):
            raise Exception("Can't apply types to non-generic data structures")

        return context.with_vars(dict(zip(body.type_args, ta.arguments))), ta.body

    return type_dispatch_table(
        lambda tr: (context, context.references[tr]),
        lambda tv: (context, context.resolve_var(tv)),
        reduce_app,
        identity,
        identity,
        identity,
        identity,
        identity,
        identity,
        identity,
        identity,
        identity)(tt)


def annotate_context(context: TypeEvaluationContext, tt: Type) -> Tuple[TypeEvaluationContext, Type]:
    def identity(t): return context, t

    def error(_: Any) -> Any: raise Exception()

    def annotate_path(t: Union[RecordType, VariantType]) -> Tuple[TypeEvaluationContext, Type]:
        return context.append_path(t.name), t

    return type_dispatch_table(
        error, error, error, identity, identity, identity, identity, identity,
        annotate_path, annotate_path, identity, identity)(tt)


class TemplateMeta(type):
    """
    Metaclass for generated template types.
    """
    def __new__(mcs, name, bases, namespace, template_name: str):
        result = type.__new__(mcs, name, bases, dict(namespace))
        result._template_name = template_name
        return result

    def __str__(self):
        return self._template_name

    def __repr__(self):
        return self._template_name


class ChoiceMeta(type):
    """
    Metaclass for generated template choice types.
    """
    def __new__(mcs, name, bases, namespace, template_name: str, choice_name: str):
        result = type.__new__(mcs, name, bases, dict(namespace))
        result._template_name = template_name
        result._choice_name = choice_name
        return result

    def __str__(self):
        return self._choice_name

    def __repr__(self):
        return self._choice_name


class TypeAdjective(Flag):
    """
    Different descriptions for how and why a type comes to be.

    Instance attributes:

    .. attribute: TypeAdjective.DAML_BUILTIN:

        A native type to DAML, such as ``Integer``, ``Text``, or ``ContractId``

    .. attribute: TypeAdjective.DAML_INTERNAL:

        Types that are used internally to DAML and generally not exposed to users.

    .. attribute: TypeAdjective.USER_TEMPLATE_AUTOGENERATED:

        Types that were created because of a DAML ``template`` declaration.

    .. attribute: TypeAdjective.USER_CHOICE_AUTOGENERATED:

        Types that were created because of a DAML choice declaration.

    .. attribute: TypeAdjective.USER_DEFINED:

        Types that were explicitly created because of a user declaration.
    """
    NONE = 0
    DAML_BUILTIN = 1
    DAML_INTERNAL = 2
    USER_TEMPLATE_AUTOGENERATED = 4
    USER_CHOICE_AUTOGENERATED = 8
    USER_DEFINED = 16
    ANY = 0xFFFFFFFF


def module(obj):
    """
    Marker decorator that denotes a class as a module.
    """
    return obj


# types that can be used to refer to templates
TemplateNameLike = Union[str, TypeReference, UnresolvedTypeReference, Template]
