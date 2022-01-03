# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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
from typing import (
    TYPE_CHECKING,
    AbstractSet,
    Any,
    Callable,
    ClassVar,
    Collection,
    Dict,
    Mapping,
    NewType,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)
import warnings

from .. import LOG
from ..damlast.daml_lf_1 import DottedName, Expr, ModuleRef, PackageRef, TypeConName
from ..prim import ContractData, Party
from ..util.typing import safe_cast, safe_dict_cast, safe_optional_cast

warnings.warn("The symbols in dazl.model.types are deprecated", DeprecationWarning, stacklevel=2)

DottedNameish = Union[str, Sequence[str]]

T_co = TypeVar("T_co", covariant=True)

if TYPE_CHECKING:
    from .types_store import PackageStore


# Reference to a ledger ID.
LedgerId = NewType("LedgerId", str)

# Reference to a package via a package identifier. The identifier is the ascii7
# lowercase hex-encoded hash of the package contents found in the DAML LF Archive.
#
# This is re-exported from the daml_lf_1 as PackageId for backwards compatibility, and will
# be removed in dazl v8.
PackageId = PackageRef

# A set of PackageId.
PackageIdSet = AbstractSet[PackageId]


def type_ref(s: str) -> "TypeReference":
    """
    Convenience method for creating a fully-qualified :class:`TypeReference`. A few formats are
    supported:

    "packageId:module:entity"
    "module:entity@pkgid"
    "module.entity@pkgid"
    """
    warnings.warn(
        "type_ref is deprecated; there is no replacement", DeprecationWarning, stacklevel=2
    )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        # Attempt to parse in an older format still used by Navigator for display purposes.
        me, is_at, pkgid = s.partition("@")
        if is_at:
            # encourage people to use the new format
            m, has_colon, e = me.partition(":")
            if not has_colon:
                m, _, e = me.rpartition(".")

            pkg_ref = PackageRef(pkgid)
            module_name = DottedName(m.split("."))
            entity_name = e.split(".")
        else:
            components = s.split(":")
            if len(components) != 3:
                raise ValueError(f"could not parse as a template reference: {s!r}")

            pkg_ref = PackageRef(components[0])
            module_name = DottedName(components[1].split("."))
            entity_name = components[2].split(".")

        return TypeReference(
            con=TypeConName(module=ModuleRef(pkg_ref, module_name), name=entity_name)
        )


def dotted_name(obj: DottedNameish) -> "Sequence[str]":
    """
    Sanitize a string or a tuple of strings to a dotted name.

    :param obj: A string or tuple of strings.
    :return: A tuple of strings.
    """
    if obj is None:
        raise ValueError("DottedName must be a non-None value")
    if isinstance(obj, str):
        return tuple(obj.split("."))
    if isinstance(obj, Collection):
        for item in obj:
            if not isinstance(item, str):
                raise ValueError("DottedName's components must all be strings")
        return tuple(obj)
    else:
        raise ValueError("could not convert to a sequence of str: {obj!r}")


class NamedArgumentList(tuple):
    """
    A simple tuple to storing (name, value) pairs.
    """

    @property
    def names(self):
        return set(name for name, _ in self)


def type_dispatch_table(
    on_type_ref: Callable[["TypeReference"], T_co],
    on_type_var: Callable[["TypeVariable"], T_co],
    on_type_app: Callable[["TypeApp"], T_co],
    on_scalar: Callable[["ScalarType"], T_co],
    on_contract_id: Callable[["ContractIdType"], T_co],
    on_optional: Callable[["OptionalType"], T_co],
    on_list: Callable[["ListType"], T_co],
    on_text_map: "Callable[[TextMapType], T_co]",
    on_record: Callable[["RecordType"], T_co],
    on_variant: Callable[["VariantType"], T_co],
    on_enum: "Callable[[EnumType], T_co]",
    on_unsupported: Callable[["UnsupportedType"], T_co],
) -> Callable[["Type"], T_co]:
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
        elif isinstance(tt, TextMapType):
            return on_text_map(tt)
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
            LOG.error("Incomplete implementation of type_match! (when handling %r)", tt)
            raise Exception(f"unknown Type subclass: {tt!r}")

    return _impl


def scalar_type_dispatch_table(
    on_unit: "Callable[[], T_co]",
    on_bool: "Callable[[], T_co]",
    on_text: "Callable[[], T_co]",
    on_int: "Callable[[], T_co]",
    on_decimal: "Callable[[], T_co]",
    on_party: "Callable[[], T_co]",
    on_date: "Callable[[], T_co]",
    on_datetime: "Callable[[], T_co]",
    on_timedelta: "Callable[[], T_co]",
) -> "Callable[[ScalarType], T_co]":
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
        elif tt == SCALAR_TYPE_DECIMAL or tt == SCALAR_TYPE_NUMERIC:
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
            LOG.error(
                "Incomplete implementation of scalar_type_dispatch_table! (when handling %r)", tt
            )
            raise Exception(f"unknown ScalarType: {tt!r}")

    return _impl


class Type:
    """
    A DAML-defined type.
    """

    def __init__(self):
        warnings.warn(
            "dazl.model.types.Type and its subclasses are deprecated. "
            "Use dazl.damlast.daml_lf_1.Type instead.",
            DeprecationWarning,
            stacklevel=2,
        )

    def __str__(self):
        from ..pretty import DAML_PRETTY_PRINTER

        return DAML_PRETTY_PRINTER.visit_type(self)


class TypeApp(Type):
    """
    An application of one or more types to an open type.

    This is basically Type.Con in the Protobuf declaration.
    """

    def __init__(self, body: Type, arguments: Sequence[Type]):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()

        warnings.warn(
            "dazl.model.types.TypeApp and its subclasses are deprecated. "
            "Use dazl.damlast.daml_lf_1.Type instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if not isinstance(body, Type):
            raise ValueError(f"a Type is required here (got {body} instead)")
        if not arguments:
            raise ValueError("at least one type argument is required in a TypeApp")
        self.body = body
        self.arguments = tuple(arguments)

    def __repr__(self):
        return f"<TypeApp(body={self.body}, arguments={self.arguments}>"


class TypeVariable(Type):
    """
    An unbound type in a Type expression.
    """

    __slots__ = ("name",)

    def __init__(self, name: str):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()

        warnings.warn(
            "dazl.model.types.TypeVar is deprecated. " "Use dazl.damlast.daml_lf_1.Type instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.name = safe_cast(str, name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"TypeVariable({self.name})"

    def __eq__(self, other):
        return isinstance(other, TypeVariable) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class TypeReference(Type):
    def __init__(self, con: "TypeConName"):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "TypeReference is deprecated; in most cases, use TypeConName instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self.con = con

    def __str__(self):
        return str(self.con)

    def __eq__(self, other):
        return isinstance(other, TypeReference) and self.con == other.con

    def __hash__(self):
        return hash(self.con)


class UnresolvedTypeReference(Type):
    """
    A reference that may or may not ultimately resolve to a type.
    """

    def __init__(self, name: str):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "UnresolvedTypeReference is deprecated; in most cases, use TypeConName instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self.name = safe_cast(str, name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<UnresolvedTypeReference({self.name!r})>"

    def __eq__(self, other):
        return isinstance(other, UnresolvedTypeReference) and self.name == other.name

    def __hash__(self):
        return hash((UnresolvedTypeReference, self.name))


class ConcreteType(Type):
    pass


class ScalarType(ConcreteType):
    """
    A DAML-defined type that represents a simple scalar value. You should not need to ever
    construct instances of this directly; all scalar types are builtins.
    """

    __slots__ = ("name",)
    name: str
    BUILTINS: "ClassVar[Sequence[ScalarType]]"

    def __init__(self, name: str):
        """
        Construct an object that references a scalar DAML type.

        :param name: The name of this type as it is known in DAML.
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "ScalarType is deprecated; in most cases, use dazl.damlast.daml_lf_1 types instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self.name = safe_cast(str, name)

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

    __slots__ = ("type_parameter",)

    def __init__(self, type_parameter: Type):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()

        warnings.warn(
            "ContractIdType, and ListType, TypeRefType are deprecated; use dazl.damlast.daml_lf_1 types instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self.type_parameter = safe_cast(Type, type_parameter)

    def __repr__(self):
        py_type = type(self).__name__
        return f"<{py_type}({self.type_parameter!r})>"


class ContractIdType(_BuiltInParameterizedType):
    pass


class ListType(_BuiltInParameterizedType):
    pass


class TypeRefType(_BuiltInParameterizedType):
    pass


class TextMapType(ConcreteType):
    """
    A DAML-defined TextMap.

    Instance attributes:

    .. attribute: TextMapType.value_type

        The type of values in this map.
    """

    __slots__ = ("value_type",)

    def __init__(self, value_type: Type):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "TextMapType is deprecated; use dazl.damlast.daml_lf_1 types instead",
            DeprecationWarning,
            stacklevel=2,
        )

        self.value_type = safe_cast(Type, value_type)

    def __repr__(self):
        py_type = type(self).__name__
        return f"<{py_type}({self.value_type!r})>"


class GenMapType(ConcreteType):
    """
    A DAML-defined GenMap.

    Instance attributes:

    .. attribute: TextMapType.key_type

        The type of keys in this map.

    .. attribute: TextMapType.value_type

        The type of values in this map.
    """

    __slots__ = "key_type", "value_type"

    def __init__(self, key_type: Type, value_type: Type):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "GenMapType is deprecated; use dazl.damlast.daml_lf_1 types instead",
            DeprecationWarning,
            stacklevel=2,
        )

        self.key_type = safe_cast(Type, key_type)
        self.value_type = safe_cast(Type, value_type)

    def __repr__(self):
        py_type = type(self).__name__
        return f"<{py_type}({self.key_type!r}, {self.value_type!r})>"


class OptionalType(_BuiltInParameterizedType):
    """
    A DAML-defined Optional.

    Instance attributes:

    .. attribute: OptionalType.type_parameter

        The type of value in the Optional.
    """


class UpdateType(_BuiltInParameterizedType):
    pass


class ForAllType(Type):
    def __init__(self, type_vars, body_type):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "ForAllType is deprecated; there is no replacement", DeprecationWarning, stacklevel=2
        )

        self.type_vars = type_vars
        self.body_type = body_type

    def __repr__(self):
        return f"<ForAllType({self.type_vars}, {self.body_type})>"


class _CompositeDataType(ConcreteType):
    """
    Either a :class:`RecordType` (product type) or a :class:`VariantType` (sum type).
    """

    def __init__(
        self,
        named_args: "NamedArgumentList",
        name: "Optional[TypeReference]",
        type_args: "Sequence[TypeVariable]",
    ):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "RecordType and VariantType are deprecated; use dazl.damlast.daml_lf_1 types instead",
            DeprecationWarning,
            stacklevel=2,
        )

        if type(self) == _CompositeDataType:
            raise Exception("_CompositeDataType cannot be constructed")
        if not isinstance(named_args, NamedArgumentList):
            raise TypeError("NamedArgumentList required here")
        if name is not None and not isinstance(name, TypeReference):
            raise TypeError("name must be a TypeReference or None")

        self.named_args = named_args
        self.name = name
        self.type_args = tuple(type_args)

    def field_type(self, name: str) -> Type:
        for key, value_type in self.named_args:
            if key == name:
                return value_type

        raise ValueError(f"field or constructor {name!r} not found in {self}")

    def __repr__(self):
        py_type = type(self).__name__

        name = "(anonymous)" if self.name is None else self.name
        full_name = "".join(f" {v}" for v in ((name,) + self.type_args))

        return f"<{py_type}:{full_name} {self.named_args}>"


class FunctionType(Type):
    """
    Representation of a DAML function signature.

    Instances of this type aren't practically usable from this library. They are merely recorded in
    order to faithfully pretty-print metadata.
    """

    def __init__(self, parameters: Sequence[Type], result: Type):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()
        warnings.warn(
            "FunctionType is deprecated; there is no replacement", DeprecationWarning, stacklevel=2
        )

        self.parameters = tuple(parameters)
        self.result = safe_cast(Type, result)

    def __str__(self):
        from io import StringIO

        with StringIO() as buf:
            for param in self.parameters:
                buf.write(str(param))
                buf.write(" -> ")
            buf.write(str(self.result))
            return buf.getvalue()

    def __repr__(self):
        return f"<FunctionType({self})>"


class RecordType(_CompositeDataType):
    def as_args_list(self):
        return self.named_args


class VariantType(_CompositeDataType):
    def as_args_list(self):
        return self.named_args

    def _find_ctor(self, constructor_name: str) -> Type:
        return self.field_type(constructor_name)


class EnumType(ConcreteType):

    __slots__ = ("constructors",)

    def __init__(self, name: "Optional[TypeReference]", constructors: "Collection[str]"):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            super().__init__()

        warnings.warn(
            "EnumType is deprecated; use dazl.damlast.daml_lf_1 types instead",
            DeprecationWarning,
            stacklevel=2,
        )

        self.name = name
        self.constructors = constructors


class UnsupportedType(Type):
    """
    A DAML type that is currently unparseable by the Python client library.
    """

    __slots__ = ("name",)

    def __init__(self, name):
        self.name = safe_cast(str, name)

    def __repr__(self):
        return f"<UnsupportedType({self.name})>"


class Template:
    """
    Definition of a contract template.
    """

    def __init__(
        self,
        data_type: "RecordType",
        key_type: "Optional[Type]",
        choices: "Collection[TemplateChoice]",
        observers: "Expr",
        signatories: "Expr",
        agreement: "Expr",
        ensure: "Expr",
    ):
        if not isinstance(data_type, RecordType) or data_type.name is None:
            raise ValueError(
                f"data_type is required and must be a named record type " f"(got {data_type})"
            )
        self.data_type = safe_cast(RecordType, data_type)
        self.key_type = safe_optional_cast(Type, key_type)
        self.choices = choices
        self._observers = observers
        self._signatories = signatories
        self._agreement = agreement
        self._ensure = ensure


class TemplateChoice:
    __slots__ = ("name", "consuming", "data_type", "return_type", "_controllers")

    def __init__(
        self, name: str, consuming: bool, data_type: Type, return_type: Type, controllers: "Expr"
    ):
        self.name = name
        self.consuming = consuming
        self.data_type = data_type
        self.return_type = return_type
        self._controllers = controllers

    @property
    def type(self):
        return self.data_type

    def controllers(self, cdata: ContractData) -> Collection[Party]:
        """
        Return every :class:`Party` that can exercise this choice given the specified contract data.
        """


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
            raise TypeError(f"{command!r} is not a Command")
    return tuple(cmds)


def as_contract_id(cid, template_id=None):
    """
    Convert something that resembles a contract ID to a :class:`ContractId` or
    :class:`RelativeContractRef`.
    """
    warnings.warn(
        "as_contract_id is deprecated; there is no replacement", DeprecationWarning, stacklevel=2
    )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from .core import ContractId

        if cid is None:
            raise ValueError("cid is required")
        elif isinstance(cid, str):
            return ContractId(cid, template_id)
        elif isinstance(cid, ContractId):
            return cid

        raise TypeError("Could not serialize an object to a contract ID: {!r}".format(cid))


with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    SCALAR_TYPE_UNIT = ScalarType("Unit")
    SCALAR_TYPE_BOOL = ScalarType("Bool")
    SCALAR_TYPE_CHAR = ScalarType("Char")
    SCALAR_TYPE_INTEGER = ScalarType("Integer")
    SCALAR_TYPE_DECIMAL = ScalarType("Decimal")
    SCALAR_TYPE_NUMERIC = ScalarType("Numeric")
    SCALAR_TYPE_TEXT = ScalarType("Text")
    SCALAR_TYPE_PARTY = ScalarType("Party")
    SCALAR_TYPE_RELTIME = ScalarType("RelTime")
    SCALAR_TYPE_DATE = ScalarType("Date")
    SCALAR_TYPE_TIME = ScalarType("Time")
    SCALAR_TYPE_ANY = ScalarType("Any")
    SCALAR_TYPE_DATETIME = SCALAR_TYPE_TIME

ScalarType.BUILTINS = [
    SCALAR_TYPE_BOOL,
    SCALAR_TYPE_CHAR,
    SCALAR_TYPE_INTEGER,
    SCALAR_TYPE_DECIMAL,
    SCALAR_TYPE_NUMERIC,
    SCALAR_TYPE_TEXT,
    SCALAR_TYPE_PARTY,
    SCALAR_TYPE_RELTIME,
    SCALAR_TYPE_DATE,
    SCALAR_TYPE_TIME,
    SCALAR_TYPE_ANY,
]


class TypeEvaluationContext:
    references: Dict[TypeConName, ConcreteType]
    variables: Dict[TypeVariable, Type]
    path: Sequence[Union[TypeReference, str]]

    __slots__ = ("references", "variables", "path")

    @classmethod
    def from_store(cls, store: "PackageStore") -> "TypeEvaluationContext":
        return cls(store.types(), {}, ())

    def __init__(self, references: "Mapping[TypeConName, ConcreteType]", variables, path):
        self.references = safe_dict_cast(TypeConName, ConcreteType, references)
        self.variables = safe_dict_cast(TypeVariable, Type, variables)
        self.path = path

    def append_path(self, component: Union[TypeReference, str]) -> "TypeEvaluationContext":
        return TypeEvaluationContext(
            references=self.references,
            variables=self.variables,
            path=tuple((*self.path, component)),
        )

    def resolve_var(self, var: TypeVariable) -> Type:
        return self.variables[var]

    def with_vars(self, new_vars: "Dict[TypeVariable, Type]") -> "TypeEvaluationContext":
        confirmed_new_vars = {}
        for new_var, new_var_value in new_vars.items():
            if new_var == new_var_value:
                # TODO: Why do these cases happen?
                continue
            confirmed_new_vars[new_var] = new_var_value

        return TypeEvaluationContext(
            references=self.references,
            variables={**self.variables, **confirmed_new_vars},
            path=self.path,
        )


def type_evaluate_dispatch(
    on_scalar: "Callable[[TypeEvaluationContext, ScalarType], T_co]",
    on_contract_id: "Callable[[TypeEvaluationContext,  ContractIdType], T_co]",
    on_optional: "Callable[[TypeEvaluationContext, OptionalType], T_co]",
    on_list: "Callable[[TypeEvaluationContext, ListType], T_co]",
    on_text_map: "Callable[[TypeEvaluationContext, TextMapType], T_co]",
    on_record: "Callable[[TypeEvaluationContext, RecordType], T_co]",
    on_variant: "Callable[[TypeEvaluationContext, VariantType], T_co]",
    on_enum: "Callable[[TypeEvaluationContext, EnumType], T_co]",
    on_unsupported: "Callable[[TypeEvaluationContext, UnsupportedType], T_co]",
) -> "Callable[[TypeEvaluationContext, Type], T_co]":
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
                raise Exception("hit our max resolve depth, which is probably not so great")

        def error(_: Any) -> "T_co":
            raise Exception()

        context, tt = annotate_context(context, tt)

        return type_dispatch_table(
            error,
            error,
            error,
            lambda st: on_scalar(context, st),
            lambda ct: on_contract_id(context, ct),
            lambda ot: on_optional(context, ot),
            lambda lt: on_list(context, lt),
            lambda mt: on_text_map(context, mt),
            lambda rt: on_record(context, rt),
            lambda vt: on_variant(context, vt),
            lambda et: on_enum(context, et),
            lambda ut: on_unsupported(context, tt),
        )(tt)

    return _impl


def _type_evaluate_dispatch_error(_, __):
    raise Exception()


def type_evaluate_dispatch_default_error(
    on_scalar: "Callable[[TypeEvaluationContext, ScalarType], T_co]" = _type_evaluate_dispatch_error,
    on_contract_id: "Callable[[TypeEvaluationContext,  ContractIdType], T_co]" = _type_evaluate_dispatch_error,
    on_optional: "Callable[[TypeEvaluationContext,  OptionalType], T_co]" = _type_evaluate_dispatch_error,
    on_list: "Callable[[TypeEvaluationContext, ListType], T_co]" = _type_evaluate_dispatch_error,
    on_text_map: "Callable[[TypeEvaluationContext, TextMapType], T_co]" = _type_evaluate_dispatch_error,
    on_record: "Callable[[TypeEvaluationContext, RecordType], T_co]" = _type_evaluate_dispatch_error,
    on_variant: "Callable[[TypeEvaluationContext, VariantType], T_co]" = _type_evaluate_dispatch_error,
    on_enum: "Callable[[TypeEvaluationContext, EnumType], T_co]" = _type_evaluate_dispatch_error,
    on_unsupported: "Callable[[TypeEvaluationContext, UnsupportedType], T_co]" = _type_evaluate_dispatch_error,
):
    return type_evaluate_dispatch(
        on_scalar,
        on_contract_id,
        on_optional,
        on_list,
        on_text_map,
        on_record,
        on_variant,
        on_enum,
        on_unsupported,
    )


def single_reduce(context: TypeEvaluationContext, tt: Type) -> "Tuple[TypeEvaluationContext, Type]":
    """
    Apply a single substitution/reduction/unwrapping. The context may be augmented with additional
    variables if a TypeApp is encountered.
    """

    def identity(t):
        return context, t

    def reduce_app(ta: TypeApp) -> "Tuple[TypeEvaluationContext, Type]":
        body = context.references[ta.body.con] if isinstance(ta.body, TypeReference) else ta.body
        if not isinstance(body, (RecordType, VariantType)):
            raise Exception("Can't apply types to non-generic data structures")

        return context.with_vars(dict(zip(body.type_args, ta.arguments))), ta.body

    return type_dispatch_table(
        lambda tr: (context, context.references[tr.con]),
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
        identity,
    )(tt)


def annotate_context(
    context: TypeEvaluationContext, tt: Type
) -> Tuple[TypeEvaluationContext, Type]:
    def identity(t):
        return context, t

    def error(_: Any) -> Any:
        raise Exception()

    def annotate_path(t: Union[RecordType, VariantType]) -> Tuple[TypeEvaluationContext, Type]:
        if t.name is None:
            raise ValueError("cannot annotate a path with an anonymous type")

        return context.append_path(t.name), t

    return type_dispatch_table(
        error,
        error,
        error,
        identity,
        identity,
        identity,
        identity,
        identity,
        annotate_path,
        annotate_path,
        identity,
        identity,
    )(tt)


# types that can be used to refer to templates
TemplateNameLike = Union[str, TypeConName, TypeReference, UnresolvedTypeReference, Template]
