from typing import Any, TypeVar

from . import ledger_api_types as api
from ..model.writing import CreateCommand, CreateAndExerciseCommand, \
    ExerciseByKeyCommand, ExerciseCommand


Self = TypeVar('Self')
T = TypeVar('T')


class CommandSerializer:
    """
    Base class for a serializer for commands and values over the DAML Ledger API.
    """

    def write_command(self, command):
        if isinstance(command, CreateCommand):
            return self.write_create_command(command)
        elif isinstance(command, ExerciseCommand):
            return self.write_exercise_command(command)
        elif isinstance(command, CreateAndExerciseCommand):
            return self.write_create_and_exercise_command(command)
        elif isinstance(command, ExerciseByKeyCommand):
            return self.write_exercise_by_key_command(command)
        else:
            raise ValueError(f'unknown command type: {command!r}')

    def write_create_command(self, command):
        raise NotImplementedError('CommandSerializer.write_create_command not implemented')

    def write_exercise_command(self, command):
        raise NotImplementedError('CommandSerializer.write_exercise_command not implemented')

    def write_create_and_exercise_command(self, command):
        raise NotImplementedError(
            'CommandSerializer.write_create_and_exercise_command not implemented')

    def write_exercise_by_key_command(self, command):
        raise NotImplementedError('CommandSerializer.write_exercise_by_key_command not implemented')


class ValueSerializer:
    """
    Serialize a value.
    """

    def __init__(self, context: 'api.TypeContext', path: str, target: 'Any'):
        self.context = context
        self.path = path
        self.target = target

    def descend(self: 'Self', path: str, target: 'Any') -> 'Self':
        return type(self)(self.types, path, target)

    def write_value(self, api_type: 'api.Type', obj: 'Any') -> None:
        try:
            api_type.match(
                self.context,
                lambda var: self.context.resolve_var(var),
                lambda con: self.context.resolve_con(con),
                lambda data: data,
                lambda prim: prim,
                lambda syn: self.context.bind_vars(syn.args)
            )
            if isinstance(api_type, api.RecordType):
                self.write_record(api_type, obj)
            elif isinstance(api_type, api.VariantType):
                self.write_variant(api_type, obj)
            elif isinstance(api_type, api.ContractIdType):
                self.write_contract_id(api_type, obj)
            elif isinstance(api_type, api.ListType):
                self.write_list(api_type, obj)
            elif isinstance(api_type, api.IntType):
                self.write_int(api_type, obj)
            elif isinstance(api_type, api.NumericType):
                self.write_numeric(api_type, obj)
            elif isinstance(api_type, api.TextType):
                self.write_text(api_type, obj)
            elif isinstance(api_type, api.DatetimeType):
                self.write_datetime(api_type, obj)
            elif isinstance(api_type, api.PartyType):
                self.write_party(api_type, obj)
            elif isinstance(api_type, api.BoolType):
                self.write_bool(api_type, obj)
            elif isinstance(api_type, api.UnitType):
                self.write_unit(api_type, obj)
            elif isinstance(api_type, api.DateType):
                self.write_date(api_type, obj)
            elif isinstance(api_type, api.OptionalType):
                self.write_optional(api_type, obj)
            elif isinstance(api_type, api.TextMapType):
                self.write_textmap(api_type, obj)
            elif isinstance(api_type, api.EnumType):
                self.write_enum(api_type, obj)
            elif isinstance(api_type, api.GenMapType):
                self.write_genmap(api_type, obj)
            else:
                self.write_unknown(api_type, obj)
        except Exception:  # noqa
            raise

    def write_record(self, api_type: 'api.RecordType', obj: 'Any') -> None:
        """
        Write a record.

        :param api_type: The :class:`RecordType` that defines this type.
        :param obj: The object to convert to a record value.
        """
        raise NotImplementedError('Serializer.write_record not implemented')

    def write_variant(self, api_type: 'api.VariantType', obj: 'Any') -> None:
        """
        Write a variant.

        :param api_type: The :class:`VariantType` that defines this type.
        :param obj: The object to convert to a variant value.
        """
        raise NotImplementedError('Serializer.write_variant not implemented')

    def write_contract_id(self, api_type: 'api.ContractIdType', obj: 'Any') -> None:
        """
        Write a contract ID.

        :param api_type: The :class:`ContractIdType` that defines this type.
        :param obj: The object to convert to a contract ID value.
        """
        raise NotImplementedError('Serializer.write_contract_id not implemented')

    def write_list(self, api_type: 'api.ListType', obj: 'Any') -> None:
        """
        Write a list.

        :param api_type: The :class:`ListType` that defines this type.
        :param obj: The object to convert to a list value.
        """
        raise NotImplementedError('Serializer.write_list not implemented')

    def write_int(self, api_type: 'api.IntType', obj: 'Any') -> None:
        """
        Write an int value.

        :param api_type: The :class:`IntType` that defines this type.
        :param obj: The object to convert to an int value.
        """
        raise NotImplementedError('Serializer.write_int not implemented')

    def write_numeric(self, api_type: 'api.NumericType', obj: 'Any') -> None:
        """
        Write a numeric value.

        :param api_type: The :class:`NumericType` that defines this type.
        :param obj: The object to convert to an numeric value.
        """
        raise NotImplementedError('Serializer.write_int not implemented')

    def write_text(self, api_type: 'api.TextType', obj: 'Any') -> None:
        """
        Write a text value.

        :param api_type: The :class:`TextType` that defines this type.
        :param obj: The object to convert to a text value.
        """
        raise NotImplementedError('Serializer.write_text not implemented')

    def write_datetime(self, api_type: 'api.DatetimeType', obj: 'Any') -> None:
        """
        Write a datetime value.

        :param api_type: The :class:`DatetimeType` that defines this type.
        :param obj: The object to convert to a text value.
        """
        raise NotImplementedError('Serializer.write_datetime not implemented')

    def write_party(self, api_type: 'api.PartyType', obj: 'Any') -> None:
        """
        Write a party value.

        :param api_type: The :class:`PartyType` that defines this type.
        :param obj: The object to convert to a party value.
        """
        raise NotImplementedError('Serializer.write_party not implemented')

    def write_bool(self, api_type: 'api.BoolType', obj: 'Any') -> None:
        """
        Write a boolean value.

        :param api_type: The :class:`BoolType` that defines this type.
        :param obj: The object to convert to a boolean value.
        """
        raise NotImplementedError('Serializer.write_bool not implemented')

    def write_unit(self, api_type: 'api.UnitType', obj: 'Any') -> None:
        """
        Write ``Unit``.

        :param api_type: The :class:`UnitType` that defines this type.
        :param obj: The object to convert to a Unit value.
        """
        raise NotImplementedError('Serializer.write_unit not implemented')

    def write_date(self, api_type: 'api.DateType', obj: 'Any') -> None:
        """
        Write a date value.

        :param api_type: The :class:`DateType` that defines this type.
        :param obj: The object to convert to a text value.
        """
        raise NotImplementedError('Serializer.write_date not implemented')

    def write_optional(self, api_type: 'api.OptionalType', obj: 'Any') -> None:
        """
        Write an optional value.

        :param api_type: The :class:`OptionalType` that defines this type.
        :param obj: The object to convert to an optional value.
        """
        raise NotImplementedError('Serializer.write_optional not implemented')

    def write_textmap(self, api_type: 'api.TextMapType', obj: 'Any') -> None:
        """
        Write a TextMap value.

        :param api_type: The :class:`TextMapType` that defines this type.
        :param obj: The object to convert to a TextMap value.
        """
        raise NotImplementedError('Serializer.write_textmap not implemented')

    def write_enum(self, api_type: 'api.EnumType', obj: 'Any') -> None:
        """
        Write an enum value.

        :param api_type: The :class:`EnumType` that defines this type.
        :param obj: The object to convert to an enum value.
        """
        raise NotImplementedError('Serializer.write_enum not implemented')

    def write_genmap(self, api_type: 'api.GenMapType', obj: 'Any') -> None:
        """
        Write a genmap value.

        :param api_type: The :class:`GenMapType` that defines this type.
        :param obj: The object to convert to a genmap value.
        """
        raise NotImplementedError('Serializer.write_genmap not implemented')

    def write_unknown(self, api_type: 'api.Type', obj: 'Any') -> None:
        """
        Write a value that could not be mapped to a known type.

        :param api_type: The :class:`Type` that defines this type.
        :param obj: The object to convert to an optional value.
        """
        raise NotImplementedError('Serializer.write_unknown not implemented')

