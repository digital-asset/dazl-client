from abc import ABC
from types import MappingProxyType
from typing import Any, Callable, Collection, Mapping, Optional, Sequence, TypeVar


class Type:

    def match(
            self,
            context: 'TypeContext',
            var: 'Callable[[TypeContext, TypeVar], T]',
            con: 'Callable[[TypeContext, TypeCon], T]',
            data: 'Callable[[TypeContext, DataType], T]',
            prim: 'Callable[[TypeContext, PrimType], T]',
            syn: 'Callable[[TypeContext, TypeSyn], T]') -> T:
        """
        Match on a Type.

        :param context: A context that can be used to resolve types and type variables.
        :param var: Called for type variables.
        :param con: Called for type constructors.
        :param data: Called for ``DefDataType`` types (record, variants, enums).
        :param prim: Called for primitive types (including numerics).
        :param syn: Called for type synonyms.
        :return: The return value from the function that was called.
        """
        raise NotImplementedError


class DataType(Type, ABC):
    """
    Abstract superclass for API types that correspond to DAML-LF ``DefDataType`` instances.
    """

    def match(
            self,
            context: 'TypeContext',
            var: 'Callable[[TypeContext, TypeVar], T]',
            con: 'Callable[[TypeContext, TypeCon], T]',
            data: 'Callable[[TypeContext, DataType], T]',
            prim: 'Callable[[TypeContext, PrimType], T]',
            syn: 'Callable[[TypeContext, TypeSyn], T]') -> T:
        return data(context, self)

    def match_data(
            self,
            context: 'TypeContext',
            record: 'Callable[[TypeContext, RecordType], T]',
            variant: 'Callable[[TypeContext, VariantType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]') -> T:
        raise NotImplementedError


class _DataFieldsType(DataType, ABC):
    """
    Superclass of :class:`RecordType` and :class:`VariantType`.
    """

    __slots__ = '_fields', 'params'

    def __init__(self, fields: 'Mapping[str, Type]', params: 'Sequence[str]'):
        self._fields = fields
        self.params = params

    def field_names(self) -> 'Sequence[str]':
        return tuple(self._fields)

    def field_type(self, name: str) -> 'Type':
        return self._fields[name]


class RecordType(_DataFieldsType):

    def match_data(
            self,
            context: 'TypeContext',
            record: 'Callable[[TypeContext, RecordType], T]',
            variant: 'Callable[[TypeContext, VariantType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]') -> T:
        return record(context, self)


class VariantType(_DataFieldsType):

    def match_data(
            self,
            context: 'TypeContext',
            record: 'Callable[[TypeContext, RecordType], T]',
            variant: 'Callable[[TypeContext, VariantType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]') -> T:
        return variant(context, self)


class PrimType(Type, ABC):
    """
    Primitive type superclass.
    """

    def match(
            self,
            context: 'TypeContext',
            var: 'Callable[[TypeContext, TypeVar], T]',
            con: 'Callable[[TypeContext, TypeCon], T]',
            data: 'Callable[[TypeContext, DataType], T]',
            prim: 'Callable[[TypeContext, PrimType], T]',
            syn: 'Callable[[TypeContext, TypeSyn], T]') -> T:
        return prim(context, self)

    # noinspection PyShadowingBuiltins
    def match_prim(
            self,
            context: 'TypeContext',
            contract_id: 'Callable[[TypeContext, ContractIdType], T]',
            list: 'Callable[[TypeContext, ListType], T]',
            int: 'Callable[[TypeContext, IntType], T]',
            numeric: 'Callable[[TypeContext, NumericType], T]',
            text: 'Callable[[TypeContext, TextType], T]',
            datetime: 'Callable[[TypeContext, DatetimeType], T]',
            party: 'Callable[[TypeContext, PartyType], T]',
            bool: 'Callable[[TypeContext, BoolType], T]',
            unit: 'Callable[[TypeContext, UnitType], T]',
            date: 'Callable[[TypeContext, DateType], T]',
            optional: 'Callable[[TypeContext, OptionalType], T]',
            textmap: 'Callable[[TypeContext, TextMapType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]',
            genmap: 'Callable[[TypeContext, GenMapType], T]') -> T:
        raise NotImplementedError('PrimType.match_prim not implemented')


class _PrimArgType(PrimType, ABC):
    def __init__(self, arg_type: 'Type'):
        self.arg_type = arg_type


class ContractIdType(_PrimArgType):
    # noinspection PyShadowingBuiltins
    def match_prim(
            self,
            context: 'TypeContext',
            contract_id: 'Callable[[TypeContext, ContractIdType], T]',
            list: 'Callable[[TypeContext, ListType], T]',
            int: 'Callable[[TypeContext, IntType], T]',
            numeric: 'Callable[[TypeContext, NumericType], T]',
            text: 'Callable[[TypeContext, TextType], T]',
            datetime: 'Callable[[TypeContext, DatetimeType], T]',
            party: 'Callable[[TypeContext, PartyType], T]',
            bool: 'Callable[[TypeContext, BoolType], T]',
            unit: 'Callable[[TypeContext, UnitType], T]',
            date: 'Callable[[TypeContext, DateType], T]',
            optional: 'Callable[[TypeContext, OptionalType], T]',
            textmap: 'Callable[[TypeContext, TextMapType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]',
            genmap: 'Callable[[TypeContext, GenMapType], T]') -> T:
        return contract_id(context, self)


class ListType(_PrimArgType):
    # noinspection PyShadowingBuiltins
    def match_prim(
            self,
            context: 'TypeContext',
            contract_id: 'Callable[[TypeContext, ContractIdType], T]',
            list: 'Callable[[TypeContext, ListType], T]',
            int: 'Callable[[TypeContext, IntType], T]',
            numeric: 'Callable[[TypeContext, NumericType], T]',
            text: 'Callable[[TypeContext, TextType], T]',
            datetime: 'Callable[[TypeContext, DatetimeType], T]',
            party: 'Callable[[TypeContext, PartyType], T]',
            bool: 'Callable[[TypeContext, BoolType], T]',
            unit: 'Callable[[TypeContext, UnitType], T]',
            date: 'Callable[[TypeContext, DateType], T]',
            optional: 'Callable[[TypeContext, OptionalType], T]',
            textmap: 'Callable[[TypeContext, TextMapType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]',
            genmap: 'Callable[[TypeContext, GenMapType], T]') -> T:
        return list(context, self)


class IntType(PrimType):
    # noinspection PyShadowingBuiltins
    def match_prim(
            self,
            context: 'TypeContext',
            contract_id: 'Callable[[TypeContext, ContractIdType], T]',
            list: 'Callable[[TypeContext, ListType], T]',
            int: 'Callable[[TypeContext, IntType], T]',
            numeric: 'Callable[[TypeContext, NumericType], T]',
            text: 'Callable[[TypeContext, TextType], T]',
            datetime: 'Callable[[TypeContext, DatetimeType], T]',
            party: 'Callable[[TypeContext, PartyType], T]',
            bool: 'Callable[[TypeContext, BoolType], T]',
            unit: 'Callable[[TypeContext, UnitType], T]',
            date: 'Callable[[TypeContext, DateType], T]',
            optional: 'Callable[[TypeContext, OptionalType], T]',
            textmap: 'Callable[[TypeContext, TextMapType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]',
            genmap: 'Callable[[TypeContext, GenMapType], T]') -> T:
        return int(context, self)


class NumericType(PrimType):
    def __init__(self, nat: int):
        self.nat = nat

    # noinspection PyShadowingBuiltins
    def match_prim(
            self,
            context: 'TypeContext',
            contract_id: 'Callable[[TypeContext, ContractIdType], T]',
            list: 'Callable[[TypeContext, ListType], T]',
            int: 'Callable[[TypeContext, IntType], T]',
            numeric: 'Callable[[TypeContext, NumericType], T]',
            text: 'Callable[[TypeContext, TextType], T]',
            datetime: 'Callable[[TypeContext, DatetimeType], T]',
            party: 'Callable[[TypeContext, PartyType], T]',
            bool: 'Callable[[TypeContext, BoolType], T]',
            unit: 'Callable[[TypeContext, UnitType], T]',
            date: 'Callable[[TypeContext, DateType], T]',
            optional: 'Callable[[TypeContext, OptionalType], T]',
            textmap: 'Callable[[TypeContext, TextMapType], T]',
            enum: 'Callable[[TypeContext, EnumType], T]',
            genmap: 'Callable[[TypeContext, GenMapType], T]') -> T:
        return numeric(context, self)

    def __str__(self):
        return f'Numeric {self.nat}'

    def __eq__(self, other):
        return isinstance(other, NumericType) and self.nat == other.nat


class TextType(Type):
    pass


class DatetimeType(Type):
    pass


class PartyType(Type):
    pass


class BoolType(Type):
    pass


class UnitType(Type):
    pass


class DateType(Type):
    pass


class OptionalType(_PrimArgType):
    pass


class TextMapType(_PrimArgType):
    pass


class EnumType(Type):
    def __init__(self, values: 'Collection[str]'):
        self.values = values


class GenMapType(Type):

    def __init__(self, key_value: 'Type', value_type: 'Type'):
        self.key_type = key_value
        self.value_type = value_type


class TypeVar(Type):
    """
    A type variable.
    """

    def __init__(self, type_var: str):
        self.type_var = type_var


class TypeCon(Type):
    def __init__(self, con: 'TypeConName'):
        self.con = con


def TypeSyn(Type):
    pass


class TypeContext:

    def __init__(
            self,
            constructors: 'Mapping[TypeCon, Type]',
            variables: 'Mapping[TypeVar, Type]'):
        self.constructors = {}
        self.variables = variables

    def resolve_con(self, con: 'TypeCon') -> 'Optional[Type]':
        return self.constructors.get(con)

    def resolve_var(self, var: 'TypeVar') -> 'Optional[Type]':
        return self.variables.get(var)

    def bind_vars(self, bindings: 'Mapping[TypeVar, Type]') -> 'TypeContext':
        return TypeContext(
            self.constructors,
            MappingProxyType({**self.variables, **bindings}))

