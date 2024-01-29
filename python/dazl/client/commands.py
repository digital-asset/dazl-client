# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Command types that are used in the dazl v5 API.

These symbols are primarily kept for backwards compatibility.
"""
from __future__ import annotations

from dataclasses import dataclass, fields
from datetime import timedelta
from typing import Any, Collection, List, Mapping, Optional, Sequence, Tuple, Union
import uuid
import warnings

from ..damlast import TypeConName
from ..ledger import Command, CreateAndExerciseCommand, CreateCommand, ExerciseCommand
from ..ledger.api_types import Commands, is_command
from ..prim import ContractData, ContractId, Party

__all__ = [
    "CommandBuilder",
    "CommandDefaults",
    "CommandPayload",
    "EventHandlerResponse",
    "flatten_command_sequence",
]


# noinspection PyDeprecation
class CommandBuilder:
    """
    Builder class for generating commands to be sent to the ledger.
    """

    @classmethod
    def coerce(cls, obj: EventHandlerResponse, atomic_default: bool = False) -> CommandBuilder:
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
            self._defaults.default_ledger_id = ledger_id
        if workflow_id is not None:
            self._defaults.default_workflow_id = workflow_id
        if application_id is not None:
            self._defaults.default_application_id = application_id
        if command_id is not None:
            self._defaults.default_command_id = command_id
        if deduplication_time is not None:
            self._defaults.default_deduplication_time = deduplication_time

    def create(self, template: Union[str, TypeConName], arguments: ContractData) -> CommandBuilder:
        return self.append(CreateCommand(template_id=template, payload=arguments))

    def exercise(
        self, contract: ContractId, choice: str, arguments: Optional[Mapping[str, Any]] = None
    ) -> CommandBuilder:
        return self.append(ExerciseCommand(contract_id=contract, choice=choice, argument=arguments))

    def create_and_exercise(
        self,
        template: Union[str, TypeConName],
        create_arguments: ContractData,
        choice_name: str,
        choice_arguments: Optional[Mapping[str, Any]] = None,
    ) -> CommandBuilder:
        return self.append(
            CreateAndExerciseCommand(
                template_id=template,
                payload=create_arguments,
                choice=choice_name,
                argument=choice_arguments,
            )
        )

    def append(self, *commands: Commands) -> CommandBuilder:
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

    def append_atomically(self, *commands: Commands) -> CommandBuilder:
        self._commands.extend([flatten_command_sequence(commands)])
        return self

    def append_nonatomically(self, *commands: Commands) -> CommandBuilder:
        self._commands.extend([[cmd] for cmd in flatten_command_sequence(commands)])
        return self

    def build(self, defaults: Optional[CommandDefaults] = None) -> Collection[CommandPayload]:
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


def flatten_command_sequence(commands: Sequence[Commands]) -> List[Command]:
    """
    Convert a list of mixed commands, ``None``, and list of commands into an ordered sequence of
    non-``None`` commands.
    """
    ret = []  # type: List[Command]
    errors = []  # type: List[Tuple[Sequence[int], Commands]]

    for i, obj in enumerate(commands):
        if obj is not None:
            if is_command(obj):
                ret.append(obj)
            else:
                try:
                    cmd_iter = iter(obj)  # type: ignore
                except TypeError:
                    errors.append(((i,), obj))
                    continue
                for j, cmd in enumerate(cmd_iter):
                    if is_command(cmd):
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
    commands: Sequence[Command]
    deduplication_time: Optional[timedelta] = None

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


EventHandlerResponse = Union[None, Commands, CommandBuilder]
