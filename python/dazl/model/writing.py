# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Write-Side types
----------------

The :mod:`dazl.model.writing` module contains the Python classes used on the write-side of the
Ledger API.

.. autoclass:: Command
   :members:

.. autoclass:: CreateCommand
   :members:

.. autoclass:: ExerciseCommand
   :members:
"""
from dataclasses import dataclass, fields
from datetime import timedelta
from typing import TYPE_CHECKING, Any, Collection, List, Mapping, Optional, Sequence, Tuple, Union
import uuid
import warnings

from ..damlast.daml_lf_1 import Type, TypeConName
from ..damlast.daml_types import con
from ..damlast.lookup import find_choice
from ..damlast.protocols import SymbolLookup
from ..prim import ContractId, Party
from ..util.typing import safe_cast

if TYPE_CHECKING:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from .types import Type as DeprecatedType, TypeReference, UnresolvedTypeReference

    from ..values import Context, ValueMapper

CommandsOrCommandSequence = Union[None, "Command", Sequence[Optional["Command"]]]
EventHandlerResponse = Union[CommandsOrCommandSequence, "CommandBuilder", "CommandPayload"]


class Command:
    """
    Base class for write-side commands.
    """


@dataclass(init=False, frozen=True)
class CreateCommand(Command):
    """
    A command that creates a contract without any predecessors.

    .. attribute:: CreateCommand.template

        Refers to the type of a template. This can be passed in as a ``str`` to the constructor,
        where it assumed to represent the ID or name of a template.

    .. attribute:: CreateCommand.arguments

        The arguments to the create (as a ``dict``).
    """

    __slots__ = ("template_type", "arguments", "_template_type_deprecated")

    template_type: "TypeConName"
    arguments: "Mapping[str, Any]"
    _template_type_deprecated: "TypeReference"

    def __init__(self, template: "Union[str, TypeConName, DeprecatedType]", arguments=None):
        from ..damlast.compat import parse_template

        template_type, template_type_deprecated = parse_template(template)
        object.__setattr__(self, "template_type", template_type)
        object.__setattr__(self, "arguments", arguments or dict())
        object.__setattr__(self, "_template_type_deprecated", template_type_deprecated)

    @property
    def template(self) -> "TypeReference":
        warnings.warn(
            "CreateCommand.template is deprecated; use CreateCommand.template_type instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._template_type_deprecated

    def replace(self, template: "Union[None, str, DeprecatedType]" = None, arguments=None):
        """
        Create a new :class:`CreateCommand` with the same identifier as this command, but with new
        values for its parameters.

        :param template:
            The new value of the `template` field, or `None` to reuse the existing value.
        :param arguments:
            The new value of the `arguments` field, or `None` to reuse the existing value.
        """
        warnings.warn(
            "CreateCommand.replace is deprecated; simply construct a CreateCommand with the "
            "desired values instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if template is not None:
            template = (
                template
                if isinstance(template, DeprecatedType)
                else UnresolvedTypeReference(template)
            )
        return CreateCommand(
            template if template is not None else self.template_type,
            arguments if arguments is not None else self.arguments,
        )

    def __repr__(self):
        return f"<create {self.template_type} {self.arguments}>"


@dataclass(init=False, frozen=True)
class ExerciseCommand(Command):
    """
    A command that exercises a choice on a pre-existing contract.

    .. attribute:: ExerciseCommand.contract

        The :class:`ContractId` on which a choice is being exercised.

    .. attribute:: ExerciseCommand.choice

        Refers to a choice (either a :class:`ChoiceRef` or a :class:`ChoiceMetadata`).
        This can be passed in as a ``str`` to the constructor, where it assumed to represent the
        name of a choice.

    .. attribute:: ExerciseCommand.arguments

        The arguments to the exercise choice (as a ``dict``).

    Note that when an ``ExerciseCommand`` is created, an additional ``template_id`` parameter can
    be supplied to the constructor to aid in disambiguation of the specific choice being invoked.
    In some situations involving composite commands, a ``template_id`` must eventually be supplied
    before a choice can be exercised. If this ``template_id`` is specified, the ``contract`` and
    ``choice`` are both tagged with this ID.

    Instance methods:

    .. automethod:: replace
    """

    __slots__ = ("contract", "choice", "arguments")

    contract: "ContractId"
    choice: str
    arguments: "Optional[Any]"

    def __init__(self, contract: "ContractId", choice: str, arguments: "Optional[Any]" = None):
        object.__setattr__(self, "contract", safe_cast(ContractId, contract))
        object.__setattr__(self, "choice", safe_cast(str, choice))
        object.__setattr__(self, "arguments", dict(arguments) if arguments is not None else dict())

    def replace(self, contract=None, choice=None, arguments=None):
        """
        Create a new :class:`ExerciseCommand` with the same identifier as this command, but with new
        values for its parameters.

        :param contract:
            The new value of the `contract` field, or `None` to reuse the existing value.
            The same type coercion rules used in the constructor apply here.
        :param choice:
            The new value of the `choice` field, or `None` to reuse the existing value.
            The same type coercion rules used in the constructor apply here.
        :param arguments:
            The new value of the `choice` field, or `None` to reuse the existing value.
        """
        warnings.warn(
            "ExerciseCommand.replace is deprecated; simply construct a ExerciseCommand with the "
            "desired values instead.",
            DeprecationWarning,
        )
        return ExerciseCommand(
            contract if contract is not None else self.contract,
            choice if choice is not None else self.choice,
            arguments if arguments is not None else self.arguments,
        )

    def __repr__(self):
        return f"<exercise '{self.contract.value}' {self.choice} with {self.arguments}>"


@dataclass(init=False, frozen=True)
class ExerciseByKeyCommand(Command):
    template_type: "TypeConName"
    contract_key: "Any"
    choice: str
    choice_argument: "Any"
    _template_type_deprecated: "TypeReference"

    def __init__(
        self,
        template: "Union[str, TypeConName, TypeReference]",
        contract_key: "Any",
        choice: str,
        choice_argument: "Any",
    ):
        from ..damlast.compat import parse_template

        template_type, template_type_deprecated = parse_template(template)
        object.__setattr__(self, "template_type", template_type)
        object.__setattr__(self, "contract_key", contract_key)
        object.__setattr__(self, "choice", choice)
        object.__setattr__(self, "choice_argument", choice_argument)
        object.__setattr__(self, "_template_type_deprecated", template_type_deprecated)

    @property
    def template(self) -> "TypeReference":
        warnings.warn(
            "ExerciseByKeyCommand.template is deprecated; use ExerciseByKeyCommand.template_type "
            "instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._template_type_deprecated


@dataclass(init=False, frozen=True)
class CreateAndExerciseCommand(Command):
    template_type: "TypeConName"
    arguments: "Mapping[str, Any]"
    choice: str
    choice_argument: "Any"
    _template_type_deprecated: "TypeReference"

    def __init__(
        self,
        template: "Union[str, TypeConName, TypeReference]",
        arguments: "Mapping[str, Any]",
        choice: str,
        choice_argument: "Any",
    ):
        from ..damlast.compat import parse_template

        template_type, template_type_deprecated = parse_template(template)
        object.__setattr__(self, "template_type", template_type)
        object.__setattr__(self, "arguments", arguments)
        object.__setattr__(self, "choice", choice)
        object.__setattr__(self, "choice_argument", choice_argument)
        object.__setattr__(self, "_template_type_deprecated", template_type_deprecated)

    @property
    def template(self) -> "TypeReference":
        warnings.warn(
            "CreateAndExerciseCommand.template is deprecated; use "
            "CreateAndExerciseCommand.template_type instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._template_type_deprecated


class CommandBuilder:
    """
    Builder class for generating commands to be sent to the ledger.
    """

    @classmethod
    def coerce(cls, obj, atomic_default=False) -> "CommandBuilder":
        """
        Create a :class:`CommandBuilder` from the objects that an event handler is allowed to
        return.

        :param obj:
        :param atomic_default:
        :return:
        """
        if isinstance(obj, CommandBuilder):
            return obj

        builder = CommandBuilder(atomic_default=atomic_default)
        if obj is not None:
            builder.append(obj)
        return builder

    def __init__(self, atomic_default=False):
        self._atomic_default = atomic_default
        self._commands = [[]]  # type: List[List[Command]]
        self._defaults = CommandDefaults()

    def defaults(
        self,
        party: Optional[Party] = None,
        ledger_id: Optional[str] = None,
        workflow_id: Optional[str] = None,
        application_id: Optional[str] = None,
        command_id: Optional[str] = None,
        deduplication_time: Optional[timedelta] = None,
    ) -> None:
        if party is not None:
            self._defaults.default_party = party
        if ledger_id is not None:
            self._defaults.ledger_id = ledger_id
        if workflow_id is not None:
            self._defaults.default_workflow_id = workflow_id
        if application_id is not None:
            self._defaults.default_application_id = application_id
        if command_id is not None:
            self._defaults.default_command_id = command_id
        if deduplication_time is not None:
            self._defaults.default_deduplication_time = deduplication_time

    def create(self, template, arguments=None) -> "CommandBuilder":
        return self.append(create(template, arguments=arguments))

    def exercise(self, contract, choice, arguments=None) -> "CommandBuilder":
        return self.append(exercise(contract, choice, arguments=arguments))

    def create_and_exercise(
        self, template, create_arguments, choice_name, choice_arguments=None
    ) -> "CommandBuilder":
        return self.append(
            create_and_exercise(template, create_arguments, choice_name, choice_arguments)
        )

    def append(self, *commands: CommandsOrCommandSequence) -> "CommandBuilder":
        """
        Append one or more commands, or list of commands to the :class:`CommandBuilder` in flight.
        This method respects the value of ``atomic_default`` that this object was constructed with.
        In order to force commands to be submitted either atomically, use :meth:`append_atomically`.
        To allow these commands to be submitted in parallel use :meth:`append_nonatomically`.

        :param commands: One or more commands, or list of commands to be submitted to the ledger.
        :return: This object.
        """
        if self._atomic_default:
            # a command builder that defaults to being atomic will put all commands in a single
            # transaction; build on the very first transaction
            self._commands[0].extend(flatten_command_sequence(commands))
            return self
        else:
            return self.append_nonatomically(*commands)

    def append_atomically(self, *commands: CommandsOrCommandSequence) -> "CommandBuilder":
        self._commands.extend([flatten_command_sequence(commands)])
        return self

    def append_nonatomically(self, *commands: CommandsOrCommandSequence) -> "CommandBuilder":
        self._commands.extend([[cmd] for cmd in flatten_command_sequence(commands)])
        return self

    def build(self, defaults: "Optional[CommandDefaults]" = None) -> "Collection[CommandPayload]":
        """
        Return a collection of commands.
        """
        if defaults is None:
            raise ValueError("defaults must currently be specified")

        command_id = (
            defaults.default_command_id or self._defaults.default_command_id or uuid.uuid4().hex
        )

        return [
            CommandPayload(
                party=defaults.default_party or self._defaults.default_party,
                ledger_id=defaults.default_ledger_id or self._defaults.default_ledger_id,
                workflow_id=defaults.default_workflow_id or self._defaults.default_workflow_id,
                application_id=defaults.default_application_id
                or self._defaults.default_application_id,
                command_id=command_id,
                deduplication_time=defaults.default_deduplication_time
                or self._defaults.default_deduplication_time,
                commands=commands,
            )
            for i, commands in enumerate(self._commands)
            if commands
        ]

    def __format__(self, format_spec):
        if format_spec == "c":
            return str(self._commands)
        else:
            return repr(self)

    def __repr__(self):
        return f"CommandBuilder({self._commands})"


def flatten_command_sequence(commands: Sequence[CommandsOrCommandSequence]) -> List[Command]:
    """
    Convert a list of mixed commands, ``None``, and list of commands into an ordered sequence of
    non-``None`` commands.
    """
    ret = []  # type: List[Command]
    errors = []  # type: List[Tuple[Sequence[int], CommandsOrCommandSequence]]

    for i, obj in enumerate(commands):
        if obj is not None:
            if isinstance(obj, Command):
                ret.append(obj)
            else:
                try:
                    cmd_iter = iter(obj)
                except TypeError:
                    errors.append(((i,), obj))
                    continue
                for j, cmd in enumerate(cmd_iter):
                    if isinstance(cmd, Command):
                        ret.append(cmd)
                    else:
                        errors.append(((i, j), cmd))
    if errors:
        raise ValueError(
            f"Failed to interpret some elements as Commands in the list: " f"$[{index}] = {command}"
            for index, command in errors
        )
    return ret


@dataclass
class CommandDefaults:
    """
    Values to use for a :class:`Command` when no value is specified with the creation of the
    command.
    """

    default_party: Optional[Party] = None
    default_ledger_id: Optional[str] = None
    default_workflow_id: Optional[str] = None
    default_application_id: Optional[str] = None
    default_command_id: Optional[str] = None
    default_deduplication_time: Optional[timedelta] = None


@dataclass(frozen=True)
class CommandPayload:
    """
    A request to mutate active state of the ledger.

    .. attribute:: CommandPayload.party
        The party submitting the request.
    .. attribute:: CommandPayload.application_id:
        An optional application ID to accompany the request.
    .. attribute:: CommandPayload.command_id:
        A hash that represents the BIM commitment.
    .. attribute:: CommandPayload.deduplication_time:
        The maximum time interval before the client should consider this command expired.
    .. attribute:: CommandPayload.commands
        A sequence of commands to submit to the ledger. These commands are submitted atomically
        (in other words, they all succeed or they all fail).
    .. attribute:: CommandPayload.deduplication_time:
        The length of the time window during which all commands with the same party and command ID
        will be deduplicated. Duplicate commands submitted before the end of this window return an
        ``ALREADY_EXISTS`` error.
    """

    party: Party
    ledger_id: str
    workflow_id: str
    application_id: str
    command_id: str
    commands: "Sequence[Command]"
    deduplication_time: "Optional[timedelta]" = None

    def __post_init__(self):
        missing_fields = [
            field.name
            for field in fields(self)
            if field.name != "deduplication_time" and getattr(self, field.name) is None
        ]
        if missing_fields:
            raise ValueError(
                f"Some fields are set to None when they are required: " f"{missing_fields}"
            )


def create(template, arguments=None):
    if not isinstance(template, (str, TypeConName)):
        raise ValueError(
            "template must be a string name, a template type, or an instantiated template"
        )

    return CreateCommand(template, arguments)


def exercise(contract, choice, arguments=None):
    if not isinstance(choice, str):
        raise ValueError(
            "choice must be a string name, a template type, " "or an instantiated template"
        )

    return ExerciseCommand(contract, choice, arguments)


def exercise_by_key(template, contract_key, choice_name, choice_argument):
    return ExerciseByKeyCommand(template, contract_key, choice_name, choice_argument)


def create_and_exercise(template, create_arguments, choice_name, choice_argument):
    return CreateAndExerciseCommand(template, create_arguments, choice_name, choice_argument)


class Serializer:
    """
    Serializer interface for objects on the write-side of the API.
    """

    def serialize_value(self, tt: "Type", obj: "Any") -> "Any":
        raise NotImplementedError("serialize_value requires an implementation")

    def serialize_command(self, command: "Any") -> "Any":
        raise NotImplementedError("serialize_command requires an implementation")

    def serialize_command_request(self, command: "CommandPayload") -> "Any":
        raise NotImplementedError("serialize_command_request requires an implementation")


class AbstractSerializer(Serializer):
    """
    Implementation of :class:`Serializer` that helps enforce that all possible cases of type
    serialization have been implemented.
    """

    def __init__(self, lookup: "SymbolLookup"):
        self.lookup = lookup

    @property
    def mapper(self) -> "ValueMapper":
        raise NotImplementedError(f"{type(self)}.mapper() must be defined")

    def serialize_value(self, tt: "Type", obj: Any) -> "Any":
        from ..values import Context

        return Context(self.mapper, self.lookup).convert(tt, obj)

    def serialize_commands(self, commands: "Sequence[Command]") -> "Sequence[Any]":
        return [self.serialize_command(cmd) for cmd in commands]

    def serialize_command(self, command: "Command") -> "Any":
        if isinstance(command, CreateCommand):
            name = self.lookup.template_name(command.template_type)
            value = self.serialize_value(con(name), command.arguments)
            return self.serialize_create_command(name, value)

        elif isinstance(command, ExerciseCommand):
            template = self.lookup.template(command.contract.value_type)
            choice = find_choice(template, command.choice)
            args = self.serialize_value(choice.arg_binder.type, command.arguments)
            return self.serialize_exercise_command(command.contract, choice.name, args)

        elif isinstance(command, CreateAndExerciseCommand):
            name = self.lookup.template_name(command.template_type)
            template = self.lookup.template(name)
            create_value = self.serialize_value(con(name), command.arguments)
            choice = find_choice(template, command.choice)
            choice_args = self.serialize_value(choice.arg_binder.type, command.choice_argument)
            return self.serialize_create_and_exercise_command(
                name, create_value, choice.name, choice_args
            )

        elif isinstance(command, ExerciseByKeyCommand):
            name = self.lookup.template_name(command.template_type)
            template = self.lookup.template(name)
            key_type = template.key
            if key_type is None:
                raise ValueError(f"template {template.tycon} does not have a key")
            key_value = self.serialize_value(key_type.type, command.contract_key)
            choice = find_choice(template, command.choice)
            choice_args = self.serialize_value(choice.arg_binder.type, command.choice_argument)
            return self.serialize_exercise_by_key_command(name, key_value, choice.name, choice_args)

        else:
            raise ValueError(f"unknown Command type: {command!r}")

    def serialize_create_command(self, name: "TypeConName", template_args: "Any") -> "Any":
        raise NotImplementedError("serialize_create_command requires an implementation")

    def serialize_exercise_command(
        self, contract_id: "ContractId", choice_name: str, choice_args: "Any"
    ) -> "Any":
        raise NotImplementedError("serialize_exercise_command requires an implementation")

    def serialize_exercise_by_key_command(
        self, name: "TypeConName", key_arguments: "Any", choice_name: str, choice_arguments: "Any"
    ) -> "Any":
        raise NotImplementedError("serialize_exercise_by_key_command requires an implementation")

    def serialize_create_and_exercise_command(
        self, name: "TypeConName", create_args: "Any", choice_name: str, choice_arguments: "Any"
    ) -> "Any":
        raise NotImplementedError(
            "serialize_create_and_exercise_command requires an implementation"
        )

    def serialize_command_request(self, command: "CommandPayload") -> "Any":
        raise RuntimeError("this serializer does not support serialize_command_request")
