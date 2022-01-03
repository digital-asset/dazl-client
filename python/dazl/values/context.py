# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Mapping, NoReturn, Optional, Sequence
import warnings

from ..damlast import IdentityTypeVisitor
from ..damlast.daml_lf_1 import DefDataType, FieldWithType, PrimType, Type
from ..damlast.lookup import EmptyLookup
from ..damlast.protocols import SymbolLookup
from ..prim import ContractId, DazlError, to_str, to_variant
from .mapper import ValueMapper

if TYPE_CHECKING:
    from .mapper import ValueMapper


__all__ = ["Context", "UnboundVarError"]


# Context is designed to be subclassable, so avoid making methods that could be static, static.
# noinspection PyMethodMayBeStatic
class Context:
    """
    A context under which object translation can occur.

    Usage:

    > context = Context(mapper)
    > context.convert(obj_type, obj)
    """

    def __init__(
        self,
        mapper: "ValueMapper",
        lookup: "Optional[SymbolLookup]" = None,
        path: "Sequence[str]" = (),
    ):
        """
        Initialize a Context.

        Note that ``None`` as a :class:`SymbolLookup` means that mappers that use the created
         :class:`Context` can only understand and map primitive types; this may be suitable for
        some limited use cases, so it is allowed.

        :param lookup:
            :class:`SymbolLookup` implementation that can provide references to types and templates.
            If ``None``, mappers that use this context cannot resolve any complex types.
        """
        self.mapper = mapper
        self.lookup = lookup if lookup is not None else EmptyLookup()
        self.path = tuple(path)

    def convert(self, item_type: "Type", obj: "Any"):
        """
        Convert a value from one representation to another.

        :param item_type:
            The assumed DAML-LF :class:`Type` of ``obj``.
        :param obj:
            The object to convert.
        """
        try:
            if item_type.var is not None:
                # We support type variables, but only when they are bound; if we receive a type
                # variable here (outside of a Type.Con context where type arguments can be
                # immediately applied and substituted) we can't meaningfully process them.
                raise UnboundVarError(item_type.var.var)
            elif item_type.con is not None:
                dt = self.resolve_data_type(item_type.con)
                if dt.record is not None:
                    return self.mapper.data_record(self, dt, dt.record, obj)
                elif dt.variant is not None:
                    return self.mapper.data_variant(self, dt, dt.variant, obj)
                elif dt.enum is not None:
                    return self.mapper.data_enum(self, dt, dt.enum, obj)
            elif item_type.prim is not None:
                if item_type.prim.prim == PrimType.UNIT:
                    return self.mapper.prim_unit(self, obj)
                elif item_type.prim.prim == PrimType.BOOL:
                    return self.mapper.prim_bool(self, obj)
                elif item_type.prim.prim == PrimType.INT64:
                    return self.mapper.prim_int64(self, obj)
                elif item_type.prim.prim == PrimType.DECIMAL:
                    return self.mapper.prim_numeric(self, 10, obj)
                elif item_type.prim.prim == PrimType.TEXT or item_type.prim.prim == PrimType.CHAR:
                    return self.mapper.prim_text(self, obj)
                elif item_type.prim.prim == PrimType.TIMESTAMP:
                    return self.mapper.prim_timestamp(self, obj)
                elif item_type.prim.prim == PrimType.PARTY:
                    return self.mapper.prim_party(self, obj)
                elif item_type.prim.prim == PrimType.LIST:
                    return self.mapper.prim_list(self, item_type.prim.args[0], obj)
                elif item_type.prim.prim == PrimType.DATE:
                    return self.mapper.prim_date(self, obj)
                elif item_type.prim.prim == PrimType.CONTRACT_ID:
                    return self.mapper.prim_contract_id(self, item_type.prim.args[0], obj)
                elif item_type.prim.prim == PrimType.OPTIONAL:
                    return self.mapper.prim_optional(self, item_type.prim.args[0], obj)
                elif item_type.prim.prim == PrimType.TEXTMAP:
                    return self.mapper.prim_text_map(self, item_type.prim.args[0], obj)
                elif item_type.prim.prim == PrimType.NUMERIC:
                    return self.mapper.prim_numeric(self, item_type.prim.args[0].nat, obj)
                elif item_type.prim.prim == PrimType.GENMAP:
                    return self.mapper.prim_gen_map(
                        self, item_type.prim.args[0], item_type.prim.args[1], obj
                    )

            raise ValueError(f"could not process type: {item_type}")

        except ValueError as ex:
            # re-raise ValueErrors with a more descriptive string that includes the current context
            # path
            raise ValueError(f'value at {".".join(self.path)} has an invalid value: {obj}') from ex

    def convert_list(
        self,
        element_type: "Type",
        elements: "Sequence[Any]",
        mapper: "Optional[ValueMapper]" = None,
    ) -> "List[Any]":
        """
        Convert a _list_ of elements, each of an assumed type.

        This is a convenience method for :class:`ValueMapper` implementations where lists are
        implemented as Python lists. Note that a :class:`ValueMapper` may choose to implement list
        type conversion in a completely different way instead of calling this function, which may be
        necessary if a list of DAML-LF values is encoded in a way other than a Python list
        (i.e., Protobuf).

        :param element_type:
            The :class:`Type` of the element.
        :param elements:
            An iterable collection of objects to convert.
        :param mapper:
            If not ``None``, an alternate mapper to use when descending down the object.
        """
        return [
            self.append_path(f"[{i}", mapper=mapper).convert(element_type, elem)
            for i, elem in enumerate(elements)
        ]

    def convert_optional(
        self, element_type: "Type", element: "Optional[Any]", mapper: "Optional[ValueMapper]" = None
    ) -> "List[Any]":
        """
        Convert a _list_ of elements, each of an assumed type.

        This is a convenience method for :class:`ValueMapper` implementations where DAML-LF
        Optionals are implemented as normal Python values or ``None``. A :class:`ValueMapper` may
        choose to implement optional type conversion in a completely different way, which may be
        necessary if an Optional of a DAML-LF value is encoded in a way other than its natural
        representation or ``None`` (i.e., Protobuf).

        :param element_type:
            The :class:`Type` of the element.
        :param element:
            An object to convert.
        :param mapper:
            If not ``None``, an alternate mapper to use when descending down the object.
        :return:
            The converted object, or ``None`` if the value of the object is ``None``.
        """
        return (
            self.append_path("?", mapper=mapper).convert(element_type, element)
            if element is not None
            else None
        )

    def convert_text_map(
        self,
        element_type: "Type",
        elements: "Mapping[str, Any]",
        mapper: "Optional[ValueMapper]" = None,
    ) -> "Dict[str, Any]":
        """
        Convert a _map_ of elements, each of an assumed type.

        This is a convenience method for :class:`ValueMapper` implementations where DAML-LF TextMaps
        are represented as Python dictionaries. Note that a :class:`ValueMapper` may choose to
        implement TextMap type conversion in a completely different way instead of calling this
        function, which may be necessary if a TextMap of DAML-LF values is encoded in a way other
        than a Python dict (i.e., Protobuf).

        :param element_type:
            The :class:`Type` of the element.
        :param elements:
            A mapping of keys to values.
        :param mapper:
            If not ``None``, an alternate mapper to use when descending down the object.
        """
        return {
            key: self.append_path(key, mapper=mapper).convert(element_type, value)
            for key, value in elements.items()
        }

    def convert_gen_map(
        self,
        key_type: "Type",
        value_type: "Type",
        elements: "Mapping[Any, Any]",
        mapper: "Optional[ValueMapper]" = None,
    ) -> "Dict[str, Any]":
        """
        Convert a _map_ of elements, each of an assumed type.

        This is a convenience method for :class:`ValueMapper` implementations where DAML-LF TextMaps
        are represented as Python dictionaries. Note that a :class:`ValueMapper` may choose to
        implement TextMap type conversion in a completely different way instead of calling this
        function, which may be necessary if a TextMap of DAML-LF values is encoded in a way other
        than a Python dict (i.e., Protobuf).

        :param key_type:
            The :class:`Type` of the key.
        :param value_type:
            The :class:`Type` of the value.
        :param elements:
            A mapping of keys to values.
        :param mapper:
            If not ``None``, an alternate mapper to use when descending down the object.
        """
        return {
            self.append_path("[i]", mapper=mapper)
            .convert(key_type, key): self.append_path(key, mapper=mapper)
            .convert(value_type, value)
            for i, (key, value) in enumerate(elements.items())
        }

    def convert_contract_id(self, element_type: "Type", contract_id: "Any") -> "ContractId":
        """
        Convert a contract ID string to a :class:`ContractId`.
        """
        with warnings.catch_warnings():
            # TODO: Drop this and switch to new-style ContractIds
            warnings.simplefilter("ignore", DeprecationWarning)
            from ..model.core import ContractId as DeprecatedContractId

            if isinstance(contract_id, DeprecatedContractId):
                return contract_id
            elif isinstance(contract_id, ContractId):
                # convert new-style ContractId instances to deprecated subclasses; for now, this is
                # still the canonical form of a ContractId until the deprecated version is dropped
                return DeprecatedContractId(contract_id.value, element_type.con.tycon)
            else:
                return DeprecatedContractId(contract_id, element_type.con.tycon)

    def resolve_data_type(self, con: "Type.Con") -> "DefDataType":
        """
        Resolve a :class:`DefDataType`, including applying any type parameters.

        In order to support recursive types and type variables, only the variables that are fields
        of the resolved :class:`DefDataType` are replaced.
        """
        dt = self.lookup.data_type(con.tycon)
        if len(dt.params) != len(con.args):
            # every time we encounter DefDataType, we expect to be given its type arguments in the
            # same place; there are no other constructs in DAML-LF that express type application,
            # so failure to supply type arguments here is an error
            raise ValueError("partially-applied types are not allowed")

        # without type arguments, simply return the original DefDataType; it does not need to be
        # modified
        if not con.args:
            return dt

        # from this point on, we discard all type arguments and the original name of the DefDataType
        # since the fully-applied type is NOT the same type as the original, nor is it correct to
        # say it takes any type arguments

        type_vars = {tvwk.var: arg for (tvwk, arg) in zip(dt.params, con.args)}

        if dt.record is not None:
            return DefDataType(
                record=self._replace_all_type_vars(type_vars, dt.record),
                serializable=dt.serializable,
                location=dt.location,
            )

        elif dt.variant is not None:
            return DefDataType(
                variant=self._replace_all_type_vars(type_vars, dt.variant),
                serializable=dt.serializable,
                location=dt.location,
            )

        elif dt.enum is not None:
            return DefDataType(enum=dt.enum, serializable=dt.serializable, location=dt.location)

        elif dt.synonym is not None:
            return DefDataType(
                synonym=dt.synonym, serializable=dt.serializable, location=dt.location
            )

        else:
            raise ValueError("unknown DefDataType cannot have variables applied to them")

    def append_path(self, path: str, mapper: "Optional[ValueMapper]" = None) -> "Context":
        """
        Return a new :class:`Context` marked at a deeper path within an object hierarchy.

        :param path:
            The path to append to the current :class:`Context`'s path.
        :param mapper:
            If not ``None``, an alternate mapper to use when descending down the object.
        :return:
            A new :class:`Context` with a modified path and possibly a modified mapper.
        """
        return Context(
            mapper if mapper is not None else self.mapper, self.lookup, self.path + (path,)
        )

    def value_validate_enum(self, value: "Any", enum: "DefDataType.EnumConstructors") -> str:
        """
        Return either a confirmed valid value from the list of possible enums, or throw an error.

        :param value:
            The "natural" Python type for an enum (either a string or a variant object).
        :param enum:
            The enum constructors to validate against.
        :return:
            The string that is the valid constructor from the list of constructors to choose from.
        :raise ValueError:
            if the value could not be understood as one of the enum constructors.
        """
        from collections.abc import Mapping

        if isinstance(value, Mapping):
            ctor, _ = to_variant(value)
        else:
            ctor = to_str(value)

        if ctor in enum.constructors:
            return ctor

        self.value_error(value, f"expected one of {enum.constructors}")

    def value_warn(self, value: "Any", message: str) -> "None":
        """
        Raise a :class:`ValueWarning`, enriched with information in the current context.
        """
        warnings.warn(
            f'value at {".".join(self.path)} has a possibly invalid value: {value} ({message})',
            ValueWarning,
            stacklevel=2,
        )

    def value_error(self, value: "Any", message: str) -> "NoReturn":
        """
        Raise a :class:`ValueError`, enriched with information in the current context.
        """
        raise ValueError(
            f'value at {".".join(self.path)} has an invalid value: {value} ({message})'
        )

    @property
    def depth(self) -> int:
        """
        Return the number of components in the path of this context.
        """
        return len(self.path)

    def _replace_all_type_vars(
        self, type_vars: "Mapping[str, Type]", fields: "DefDataType.Fields"
    ) -> "DefDataType.Fields":
        """
        Substitute type variables from the given mapping into each of the provided fields.
        """
        tv = ReplacingTypeVisitor(type_vars)
        return DefDataType.Fields(
            [FieldWithType(f.field, tv.visit_type(f.type)) for f in fields.fields]
        )


class ReplacingTypeVisitor(IdentityTypeVisitor):
    def __init__(self, type_vars: "Mapping[str, Type]"):
        self.type_vars = type_vars

    def resolve_type(self, var: "str") -> "Optional[Type]":
        replacement = self.type_vars.get(var)
        if replacement is None:
            raise UnboundVarError(var)

        return replacement


class UnboundVarError(DazlError):
    def __init__(self, var):
        self.var = var


class ValueWarning(Warning):
    pass
