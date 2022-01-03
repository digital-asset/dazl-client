# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Command types that are used in the dazl v5 API.

These symbols are primarily kept for backwards compatibility.
"""
from dataclasses import dataclass, fields
from datetime import timedelta
from typing import Any, Collection, List, Mapping, Optional, Sequence, Tuple, Union
import uuid
import warnings

from ..damlast.daml_lf_1 import TypeConName
from ..ledger import api_types
from ..prim import ContractData, ContractId, Party

__all__ = [
    "CommandBuilder",
    "CommandDefaults",
    "CommandPayload",
    "CommandsOrCommandSequence",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "EventHandlerResponse",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "create",
    "create_and_exercise",
    "exercise",
    "exercise_by_key",
    "flatten_command_sequence",
]


class CreateCommand(api_types.CreateCommand):
    """
    A command that creates a contract without any predecessors.
    """

    def __init__(
        self, template: "Union[str, TypeConName]", arguments: "Optional[ContractData]" = None
    ):
        warnings.warn(
            "dazl.client.commands.CreateCommand is deprecated; "
            "prefer calling dazl.ledger.Connection.create or "
            "dazl.client.PartyClient.submit_create, "
            "or use dazl.ledger.CreateCommand instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(template, arguments or {})

    @property
    def template_type(self) -> "TypeConName":
        """
        Use :meth:`template_id` instead.
        """
        warnings.warn(
            "CreateCommand.template_type is deprecated; use CreateCommand.template_id instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.template_id

    @property
    def arguments(self) -> "Mapping[str, Any]":
        """
        Use :meth:`payload` instead.
        """
        warnings.warn(
            "CreateCommand.arguments is deprecated; use CreateCommand.payload instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.payload


class CreateAndExerciseCommand(api_types.CreateAndExerciseCommand):
    """
    A command that exercises a choice on a newly-created contract, in a single transaction.
    """

    def __init__(
        self,
        template: "Union[str, TypeConName]",
        arguments: "Mapping[str, Any]",
        choice: str,
        choice_argument: "Optional[Any]" = None,
    ):
        warnings.warn(
            "dazl.client.commands.CreateAndExerciseCommand is deprecated; "
            "prefer calling dazl.ledger.Connection.create_and_exercise or "
            "dazl.client.PartyClient.submit_create_and_exercise, "
            "or use dazl.ledger.CreateAndExerciseCommand instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(template, arguments, choice, choice_argument)

    @property
    def template_type(self) -> "TypeConName":
        """
        Use :meth:`template_id` instead.
        """
        warnings.warn(
            "CreateAndExerciseCommand.template_type is deprecated; "
            "use CreateAndExerciseCommand.template_id instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.template_id

    @property
    def arguments(self) -> "Any":
        """
        Use :meth:`payload` instead.
        """
        warnings.warn(
            "CreateAndExerciseCommand.arguments is deprecated; "
            "use CreateAndExerciseCommand.payload instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.payload

    @property
    def choice_argument(self) -> "Any":
        """
        Use :meth:`argument` instead.
        """
        warnings.warn(
            "CreateAndExerciseCommand.choice_argument is deprecated; "
            "use CreateAndExerciseCommand.argument instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.argument


class ExerciseCommand(api_types.ExerciseCommand):
    """
    A command that exercises a choice on a contract identified by its contract ID.
    """

    def __init__(self, contract: "ContractId", choice: str, arguments: "Optional[Any]" = None):
        warnings.warn(
            "dazl.client.commands.ExerciseCommand is deprecated; "
            "prefer calling dazl.ledger.Connection.exercise or "
            "dazl.client.PartyClient.submit_exercise, "
            "or use dazl.ledger.ExerciseCommand instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(contract, choice, arguments)

    @property
    def contract(self) -> "ContractId":
        """
        Use :meth:`contract_id` instead.
        """
        warnings.warn(
            "ExerciseCommand.contract is deprecated; use ExerciseCommand.contract_id instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.contract_id

    @property
    def arguments(self) -> "Any":
        """
        Use :meth:`argument` instead.
        """
        warnings.warn(
            "ExerciseCommand.arguments is deprecated; use ExerciseCommand.argument instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.argument


class ExerciseByKeyCommand(api_types.ExerciseByKeyCommand):
    def __init__(
        self,
        template: "Union[str, TypeConName]",
        contract_key: "Any",
        choice: str,
        choice_argument: "Optional[Any]" = None,
    ):
        warnings.warn(
            "dazl.client.commands.ExerciseByKeyCommand is deprecated; "
            "prefer calling dazl.ledger.Connection.exercise_by_key or "
            "dazl.client.PartyClient.submit_exercise_by_key, "
            "or use dazl.ledger.ExerciseByKeyCommand instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(template, contract_key, choice, choice_argument)

    @property
    def template_type(self) -> "TypeConName":
        """
        Use :meth:`template_id` instead.
        """
        warnings.warn(
            "ExerciseByKeyCommand.template_type is deprecated; "
            "use ExerciseByKeyCommand.template_id instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.template_id

    @property
    def contract_key(self) -> "Any":
        """
        Use :meth:`argument` instead.
        """
        warnings.warn(
            "ExerciseByKeyCommand.contract_key is deprecated; "
            "use ExerciseByKeyCommand.key instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self.key

    @property
    def choice_argument(self) -> "Any":
        """
        Use :meth:`argument` instead.
        """
        warnings.warn(
            "ExerciseByKeyCommand.choice_argument is deprecated; "
            "use ExerciseByKeyCommand.argument instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.argument


CommandsOrCommandSequence = Union[None, api_types.Command, Sequence[Optional[api_types.Command]]]


# noinspection PyDeprecation
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
        warnings.warn(
            "CommandBuilder is deprecated; "
            "prefer calling dazl.ledger.Connection.commands, "
            "dazl.client.PartyClient.submit, or construct commands explicitly instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            if isinstance(obj, CommandBuilder):
                return obj

            builder = CommandBuilder(atomic_default=atomic_default)
            if obj is not None:
                builder.append(obj)
            return builder

    def __init__(self, atomic_default: bool = False):
        warnings.warn(
            "CommandBuilder is deprecated; "
            "prefer calling dazl.ledger.Connection.commands, "
            "dazl.client.PartyClient.submit, or construct commands explicitly instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self._atomic_default = atomic_default
        self._commands = [[]]  # type: List[List[api_types.Command]]
        self._defaults = CommandDefaults()

    def defaults(
        self,
        party: "Optional[Party]" = None,
        ledger_id: "Optional[str]" = None,
        workflow_id: "Optional[str]" = None,
        application_id: "Optional[str]" = None,
        command_id: "Optional[str]" = None,
        deduplication_time: "Optional[timedelta]" = None,
    ) -> None:
        if party is not None:
            self._defaults.default_party = party
        if ledger_id is not None:
            self._defaults.default_ledger_id = ledger_id
        if workflow_id is not None:
            self._defaults.default_workflow_id = workflow_id
        if application_id is not None:
            self._defaults.default_application_id = application_id
        if command_id is not None:
            self._defaults.default_command_id = command_id
        if deduplication_time is not None:
            self._defaults.default_deduplication_time = deduplication_time

    def create(self, template, arguments=None) -> "CommandBuilder":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return self.append(create(template, arguments=arguments))

    def exercise(self, contract, choice, arguments=None) -> "CommandBuilder":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return self.append(exercise(contract, choice, arguments=arguments))

    def create_and_exercise(
        self, template, create_arguments, choice_name, choice_arguments=None
    ) -> "CommandBuilder":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return self.append(
                create_and_exercise(template, create_arguments, choice_name, choice_arguments)
            )

    def append(self, *commands: "CommandsOrCommandSequence") -> "CommandBuilder":
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

    def append_atomically(self, *commands: "CommandsOrCommandSequence") -> "CommandBuilder":
        self._commands.extend([flatten_command_sequence(commands)])
        return self

    def append_nonatomically(self, *commands: "CommandsOrCommandSequence") -> "CommandBuilder":
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

        cmds = []  # type: List[CommandPayload]
        for i, commands in enumerate(self._commands):
            if commands:
                party = defaults.default_party or self._defaults.default_party
                ledger_id = defaults.default_ledger_id or self._defaults.default_ledger_id
                workflow_id = defaults.default_workflow_id or self._defaults.default_workflow_id
                application_id = (
                    defaults.default_application_id or self._defaults.default_application_id
                )
                deduplication_time = (
                    defaults.default_deduplication_time or self._defaults.default_deduplication_time
                )

                # hitting any of these checks would be quite unusual as this information is
                # validated and supplied in places higher up in the code; they're primarily here to
                # make sure this function typechecks
                if not party:
                    raise ValueError("party is missing on a Command")
                if not ledger_id:
                    raise ValueError("ledger_id is missing on a Command")
                if not workflow_id:
                    raise ValueError("workflow_id is missing on a Command")
                if not application_id:
                    raise ValueError("application_id is missing on a Command")

                cmds.append(
                    CommandPayload(
                        party=party,
                        ledger_id=ledger_id,
                        workflow_id=workflow_id,
                        application_id=application_id,
                        command_id=command_id,
                        deduplication_time=deduplication_time,
                        commands=commands,
                    )
                )

        return cmds

    def __format__(self, format_spec):
        if format_spec == "c":
            return str(self._commands)
        else:
            return repr(self)

    def __repr__(self):
        return f"CommandBuilder({self._commands})"


def flatten_command_sequence(
    commands: "Sequence[CommandsOrCommandSequence]",
) -> "List[api_types.Command]":
    """
    Convert a list of mixed commands, ``None``, and list of commands into an ordered sequence of
    non-``None`` commands.
    """
    ret = []  # type: List[api_types.Command]
    errors = []  # type: List[Tuple[Sequence[int], CommandsOrCommandSequence]]

    for i, obj in enumerate(commands):
        if obj is not None:
            if isinstance(obj, api_types.Command):
                ret.append(obj)
            else:
                try:
                    cmd_iter = iter(obj)
                except TypeError:
                    errors.append(((i,), obj))
                    continue
                for j, cmd in enumerate(cmd_iter):
                    if isinstance(cmd, api_types.Command):
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
    commands: "Sequence[api_types.Command]"
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


# noinspection PyDeprecation
def create(template, arguments=None):
    warnings.warn(
        "dazl.client.commands.create is deprecated; "
        "prefer calling dazl.ledger.Connection.create or "
        "dazl.client.PartyClient.submit_create, "
        "or use dazl.ledger.CreateCommand instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return CreateCommand(template, arguments)


# noinspection PyDeprecation
def create_and_exercise(template, create_arguments, choice_name, choice_argument):
    warnings.warn(
        "dazl.client.commands.CreateAndExerciseCommand is deprecated; "
        "prefer calling dazl.ledger.Connection.create_and_exercise or "
        "dazl.client.PartyClient.submit_create_and_exercise, "
        "or use dazl.ledger.CreateAndExerciseCommand instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return CreateAndExerciseCommand(template, create_arguments, choice_name, choice_argument)


# noinspection PyDeprecation
def exercise(contract, choice, arguments=None):
    warnings.warn(
        "dazl.client.commands.exercise is deprecated; "
        "prefer calling dazl.ledger.Connection.exercise or "
        "dazl.client.PartyClient.submit_exercise, "
        "or use dazl.ledger.ExerciseCommand instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    if not isinstance(choice, str):
        raise ValueError(
            "choice must be a string name, a template type, or an instantiated template"
        )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return ExerciseCommand(contract, choice, arguments)


# noinspection PyDeprecation
def exercise_by_key(template, contract_key, choice_name, choice_argument):
    warnings.warn(
        "dazl.client.commands.ExerciseByKeyCommand is deprecated; "
        "prefer calling dazl.ledger.Connection.exercise_by_key or "
        "dazl.client.PartyClient.submit_exercise_by_key, "
        "or use dazl.ledger.ExerciseByKeyCommand instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        return ExerciseByKeyCommand(template, contract_key, choice_name, choice_argument)


EventHandlerResponse = Union[CommandsOrCommandSequence, CommandBuilder, CommandPayload]
