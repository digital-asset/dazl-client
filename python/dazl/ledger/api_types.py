# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import abc
from datetime import datetime
import sys
from typing import (
    TYPE_CHECKING,
    AbstractSet,
    Any,
    Collection,
    Final,
    Mapping,
    NoReturn,
    Optional,
    Sequence,
    TypeGuard,
    final,
)
import uuid
import warnings

from .. import _repr
from ..damlast.daml_lf_1 import TypeConName
from ..damlast.lookup import parse_type_con_name
from ..prim import LEDGER_STRING_REGEX, ContractData, ContractId, Parties, Party, to_parties
from ..util.typing import safe_cast

if sys.version_info >= (3, 12):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


__all__ = [
    "is_command",
    "to_commands",
    "ActAs",
    "Admin",
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CommandMeta",
    "Commands",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "Event",
    "EventOrBoundary",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "IdentityProviderAdmin",
    "InterfaceView",
    "MeteringReport",
    "MeteringReportApplication",
    "MeteringReportRequest",
    "PartyInfo",
    "ReadAs",
    "Right",
    "SubmitResponse",
    "User",
    "Version",
    "VersionFeatures",
    "VersionUserManagementFeature",
]


def is_command(obj: Any, /) -> TypeGuard[Command]:
    """
    Determine whether an object is a :class:`Command`.

    This function is equivalent to calling ``isinstance(obj, Command)``, and only existed
    to support Python 3.8 and Python 3.9-based code.
    """
    warnings.warn(
        "is_command is deprecated; use isinstance(obj, Command) instead.", DeprecationWarning
    )
    return isinstance(obj, _Command)


def to_commands(*commands: Optional[Commands]) -> Sequence[Command]:
    cmds = list[Command]()
    if commands is not None:
        for c in commands:
            if c is not None:
                if is_command(c):
                    cmds.append(c)
                else:
                    cmds.extend(to_commands(*c))  # type: ignore
    return cmds


class _Command:
    """
    Base class for write-side commands.

    This class provides no functionality on its own.
    """

    def __setattr__(self, key, value) -> NoReturn:
        """
        Raise :class:`AttributeError`; instances of this class are immutable.
        """
        raise AttributeError("Command instances are read-only")


@final
class CreateCommand(_Command):
    """
    A command that creates a contract without any predecessors.

    Attributes:
    - template_id: The template of the contract to be created.
    - payload: The template arguments for the contract to be created.
    """

    __slots__ = ("template_id", "payload")
    __match_args__ = ("template_id", "payload")
    template_id: Final[TypeConName]  # type: ignore
    payload: Final[ContractData]  # type: ignore

    def __init__(self, template_id: str | TypeConName, payload: ContractData):
        """
        Initialize a :class:`CreateCommand`.

        :param template_id:
            The template of the contract to be created.
        :param payload:
            The template arguments for the contract to be created.
        """
        object.__setattr__(self, "template_id", validate_template_id(template_id))
        object.__setattr__(self, "payload", payload)

    def __eq__(self, other: Any, /) -> bool:
        return (
            isinstance(other, CreateCommand)
            and self.template_id == other.template_id
            and self.payload == other.payload
        )

    def __repr__(self) -> str:
        return f"CreateCommand({self.template_id}, {self.payload})"


@final
class CreateAndExerciseCommand(_Command):
    """
    A command that exercises a choice on a newly-created contract in a single transaction.

    Instead of creating an instance of this command and submitting it with :meth:`Connection.submit`,
    consider using :meth:`Connection.create_and_exercise` instead, which also gives you access to
    the result of exercising the choice.

    Attributes:
    - template_id: The template of the contract to be created.
    - payload: The template arguments for the contract to be created.
    - choice: The choice to exercise.
    - argument: The choice arguments. Can be omitted for choices that take no arguments.
    """

    __slots__ = ("template_id", "payload", "choice", "argument")
    __match_args__ = ("template_id", "payload", "choice", "argument")
    template_id: Final[TypeConName]  # type: ignore
    payload: Final[ContractData]  # type: ignore
    choice: Final[str]  # type: ignore
    argument: Final[Any]  # type: ignore

    def __init__(
        self,
        template_id: str | TypeConName,
        payload: ContractData,
        choice: str,
        argument: Optional[Any] = None,
    ):
        """
        Initialize a :class:`CreateAndExerciseCommand`.

        :param template_id:
            The template of the contract to be created.
        :param payload:
            The template arguments for the contract to be created.
        :param choice:
            The choice to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no arguments.
        """
        object.__setattr__(self, "template_id", validate_template_id(template_id))
        object.__setattr__(self, "payload", payload)
        object.__setattr__(self, "choice", choice)
        object.__setattr__(self, "argument", dict(argument) if argument is not None else dict())

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, CreateAndExerciseCommand)
            and self.template_id == other.template_id
            and self.payload == other.payload
            and self.choice == other.choice
            and self.argument == other.argument
        )

    def __repr__(self) -> str:
        return f"CreateAndExerciseCommand({self.template_id}, {self.payload}, {self.choice!r}, {self.argument})"


@final
class ExerciseCommand(_Command):
    """
    A command that exercises a choice on a contract identified by its contract ID.

    Instead of creating an instance of this command and submitting it with :meth:`Connection.submit`,
    consider using :meth:`Connection.exercise` instead, which also gives you access to the result of
    exercising the choice.
    """

    __slots__ = ("contract_id", "choice", "argument")
    __match_args__ = ("contract_id", "choice", "argument")
    contract_id: Final[ContractId]  # type: ignore
    choice: Final[str]  # type: ignore
    argument: Final[Any]  # type: ignore

    def __init__(self, contract_id: ContractId, choice: str, argument: Optional[Any] = None):
        """
        Initialize an :class:`ExerciseCommand`.

        :param contract_id:
            The contract ID of the contract to exercise.
        :param choice:
            The choice to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no arguments.
        """
        object.__setattr__(self, "contract_id", safe_cast(ContractId, contract_id))
        object.__setattr__(self, "choice", safe_cast(str, choice))
        object.__setattr__(self, "argument", dict(argument) if argument is not None else dict())

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, ExerciseCommand)
            and self.contract_id == other.contract_id
            and self.choice == other.choice
            and self.argument == other.argument
        )

    def __repr__(self):
        return f"ExerciseCommand({self.contract_id}, {self.choice!r}, {self.argument})"


@final
class ExerciseByKeyCommand(_Command):
    """
    A command that exercises a choice on a contract identified by its contract key.

    Instead of creating an instance of this command and submitting it with :meth:`Connection.submit`,
    consider using :meth:`Connection.exercise_by_key` instead, which also gives you access to the
    result of exercising the choice.
    """

    __slots__ = ("template_id", "key", "choice", "argument")
    __match_args__ = ("template_id", "key", "choice", "argument")
    template_id: TypeConName
    key: Any
    choice: str
    argument: Optional[Any]

    def __init__(
        self,
        template_id: str | TypeConName,
        key: Any,
        choice: str,
        argument: Optional[Any] = None,
    ):
        """
        Initialize an :class:`ExerciseByKeyCommand`.

        :param template_id:
            The contract template type.
        :param key:
            The contract key of the contract to exercise.
        :param choice:
            The choice to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no arguments.
        """
        object.__setattr__(self, "template_id", validate_template_id(template_id))
        object.__setattr__(self, "key", key)
        object.__setattr__(self, "choice", choice)
        object.__setattr__(self, "argument", dict(argument) if argument is not None else dict())

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, ExerciseByKeyCommand)
            and self.template_id == other.template_id
            and self.key == other.key
            and self.choice == other.choice
            and self.argument == other.argument
        )

    def __repr__(self):
        return f"ExerciseByKeyCommand({self.template_id}, {self.key}, {self.choice!r}, {self.argument})"


Command: TypeAlias = (
    CreateCommand | ExerciseCommand | CreateAndExerciseCommand | ExerciseByKeyCommand
)


Commands: TypeAlias = Command | Sequence[Command]


class CommandMeta:
    """
    Additional fields that accompany a command submission.

    .. py:attribute:: workflow_id
        :type: str | None

        An optional workflow ID.

    .. py:attribute:: command_id
        :type: str | None

        An optional command ID. If unspecified, a random one will be created.

    .. py:attribute:: read_as
        :type: Collection[Party] | None

        An optional set of read-as parties to use to submit this command. Note that for a
        ledger with authorization, these parties must be a subset of the parties in the token.

    .. py:attribute:: act_as
        :type: Collection[Party] | None

        An optional set of act-as parties to use to submit this command. Note that for a
        ledger with authorization, these parties must be a subset of the parties in the token.
    """

    __slots__ = "workflow_id", "command_id", "read_as", "act_as", "user_id"

    workflow_id: Optional[str]
    command_id: Optional[str]
    read_as: Optional[Sequence[Party]]
    act_as: Optional[Sequence[Party]]
    user_id: str

    def __init__(
        self,
        workflow_id: Optional[str],
        command_id: Optional[str],
        read_as: Optional[Parties],
        act_as: Optional[Parties],
        user_id: str,
    ):
        if workflow_id:
            if not LEDGER_STRING_REGEX.match(workflow_id):
                raise ValueError("workflow_id must be a valid ledger string")
        else:
            workflow_id = None

        if command_id:
            if not LEDGER_STRING_REGEX.match(command_id):
                raise ValueError("command_id must be a valid ledger string")
        else:
            command_id = uuid.uuid4().hex

        object.__setattr__(self, "workflow_id", workflow_id)
        object.__setattr__(self, "command_id", command_id)
        object.__setattr__(self, "read_as", to_parties(read_as))
        object.__setattr__(self, "act_as", to_parties(act_as))
        object.__setattr__(self, "user_id", user_id)

    @property
    def application_name(self) -> str:
        return self.user_id

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, CommandMeta)
            and self.workflow_id == other.workflow_id
            and self.command_id == other.command_id
            and self.read_as == other.read_as
            and self.act_as == other.act_as
        )

    def __repr__(self) -> str:
        s = []
        if self.workflow_id is not None:
            s.append(f"workflow_id={_repr.str(self.workflow_id)}")
        if self.command_id is not None:
            s.append(f"command_id={_repr.str(self.command_id )}")
        if self.read_as is not None:
            s.append(f"read_as={_repr.list(self.read_as)}")
        if self.act_as is not None:
            s.append(f"act_as={_repr.list(self.act_as)}")
        return f"{self.__class__.__name__}({', '.join(s)})"


class CreateEvent:
    """
    An event that indicates a newly-created contract.
    """

    __match_args__ = (
        "contract_id",
        "payload",
        "signatories",
        "observers",
        "agreement_text",
        "key",
        "created_event_blob",
        "interface_views",
    )
    __slots__ = (
        "_contract_id",
        "_payload",
        "_signatories",
        "_observers",
        "_agreement_text",
        "_key",
        "_created_event_blob",
        "_interface_views",
    )
    if TYPE_CHECKING:
        _contract_id: ContractId
        _payload: ContractData
        _signatories: AbstractSet[Party]
        _observers: AbstractSet[Party]
        _agreement_text: Optional[str]
        _key: Optional[Any]
        _created_event_blob: Optional[bytes]
        _interface_views: Sequence[InterfaceView]

    def __init__(
        self,
        contract_id: ContractId,
        payload: ContractData,
        signatories: Collection[Party],
        observers: Collection[Party],
        agreement_text: Optional[str],
        key: Optional[Any],
        created_event_blob: Optional[bytes] = None,
        interface_views: Sequence[InterfaceView] = (),
    ):
        object.__setattr__(self, "_contract_id", contract_id)
        object.__setattr__(self, "_payload", payload)
        object.__setattr__(self, "_signatories", frozenset(signatories))
        object.__setattr__(self, "_observers", frozenset(observers))
        object.__setattr__(self, "_agreement_text", agreement_text)
        object.__setattr__(self, "_key", key)
        object.__setattr__(self, "_created_event_blob", created_event_blob)
        object.__setattr__(self, "_interface_views", tuple(interface_views))

    @property
    def contract_id(self) -> ContractId:
        """
        The ID of the created contract.
        """
        return self._contract_id

    @property
    def payload(self) -> ContractData:
        """
        The `parameters <https://docs.daml.com/daml/reference/templates.html#template-parameters>`_
        that were used to create the contract.
        """
        return self._payload

    @property
    def signatories(self) -> AbstractSet[Party]:
        """
        The `signatories <https://docs.daml.com/daml/reference/templates.html#signatory-parties>`_
        for this contract as specified by the template.
        """
        return self._signatories

    @property
    def observers(self) -> AbstractSet[Party]:
        """
        The `observers <https://docs.daml.com/daml/reference/templates.html#observers>`_ for this
        contract as specified explicitly by the template or implicitly as choice controllers.
        """
        return self._observers

    @property
    def agreement_text(self) -> Optional[str]:
        """
        The `agreement text <https://docs.daml.com/daml/reference/templates.html#agreements>`_ of
        the contract.
        """
        return self._agreement_text

    @property
    def key(self) -> Optional[Any]:
        """
        The `key <https://docs.daml.com/daml/reference/templates.html#contract-keys-and-maintainers>`_
        of the contract, if defined.
        """
        return self._key

    @property
    def created_event_blob(self) -> Optional[bytes]:
        """
        Opaque representation of contract create event payload intended for
        forwarding to an API server as a contract disclosed as part of a
        command submission.
        """
        return self._created_event_blob

    @property
    def interface_views(self) -> Sequence[InterfaceView]:
        """
        Interface views specified in the transaction filter.
        Includes an :class:`InterfaceView` for each interface for which there
        is an interface filter.
        """
        return self._interface_views

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, CreateEvent)
            and self.contract_id == other.contract_id
            and self.payload == other.payload
            and self.signatories == other.signatories
            and self.observers == other.observers
            and self.agreement_text == other.agreement_text
            and self.key == other.key
            and self.created_event_blob == other.created_event_blob
            and self.interface_views == other.interface_views
        )


class ArchiveEvent:
    """
    An event that indicates a contract was archived.
    """

    __slots__ = ("_contract_id",)
    if TYPE_CHECKING:
        _contract_id: ContractId

    def __init__(self, contract_id: ContractId):
        object.__setattr__(self, "_contract_id", contract_id)

    @property
    def contract_id(self) -> ContractId:
        """
        The contract ID of the archived contract.
        """
        return self._contract_id


Event = CreateEvent | ArchiveEvent


class Boundary:
    """
    An event that indicates a boundary in a query stream where events can be resumed.
    """

    __slots__ = ("_offset",)
    __match_args__ = ("offset",)
    if TYPE_CHECKING:
        _offset: Optional[str]

    def __init__(self, offset: Optional[str]):
        object.__setattr__(self, "_offset", offset)

    @property
    def offset(self) -> Optional[str]:
        """
        The offset at which this boundary occurred.

        If this is ``None``, that indicates that an active contract set was requested, but the
        ledger is completely empty.
        """
        return self._offset

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Boundary) and self.offset == other.offset

    def __hash__(self):
        return hash(self._offset)

    def __repr__(self):
        return f"Boundary({self._offset!r})"


EventOrBoundary = Event | Boundary


class ExerciseResponse:
    """
    Returned when directly exercising a choice using :meth:`Connection.create_and_exercise`,
    :meth:`Connection.exercise`, or :meth:`Connection.exercise_by_key`.
    """

    __slots__ = ("_result", "_events")
    __match_args__ = ("result", "events")
    if TYPE_CHECKING:
        _result: Optional[Any]
        _events: Sequence[CreateEvent | ArchiveEvent]

    def __init__(self, result: Optional[Any], events: Sequence[CreateEvent | ArchiveEvent]):
        object.__setattr__(self, "_result", result)
        object.__setattr__(self, "_events", tuple(events))

    @property
    def result(self) -> Optional[Any]:
        """
        The return value of the choice.
        """
        return self._result

    @property
    def events(self) -> Sequence[CreateEvent | ArchiveEvent]:
        """
        All of the events that occurred as a result of exercising the choice, including the archive
        event for the contract if the choice is consuming (or otherwise archives it as part of its
        execution).
        """
        return self._events

    def __repr__(self):
        return f"ExerciseResponse(result={self.result}, events={self.events})"


class InterfaceView:
    __slots__ = ("_interface_id", "_view_value")
    __match_args__ = ("interface_id", "view_value")
    if TYPE_CHECKING:
        _interface_id: TypeConName
        _view_value: Any

    def __init__(self, interface_id: TypeConName, view_value: Any):
        object.__setattr__(self, "_interface_id", interface_id)
        object.__setattr__(self, "_view_value", view_value)

    @property
    def interface_id(self) -> TypeConName:
        """
        The interface implemented by the matched event.
        """
        return self._interface_id

    @property
    def view_value(self) -> Any:
        """
        The value of the interface's view method on this event. Set if it was requested in the
        ``InterfaceFilter`` and it could be successfully computed.
        """
        return self._view_value

    def __eq__(self, other: object, /) -> bool:
        return (
            isinstance(other, InterfaceView)
            and self.interface_id == other.interface_id
            and self.view_value == other.view_value
        )


SubmitResponse: TypeAlias = Optional[CreateEvent | ExerciseResponse]


class User:
    """
    Full information about a ``User``.
    """

    __slots__ = ("id", "primary_party", "resource_version", "annotations")
    __match_args__ = ("id", "primary_party", "resource_version", "annotations")

    id: str
    primary_party: Party
    resource_version: Optional[str]
    annotations: Optional[Mapping[str, str]]

    def __init__(
        self,
        id: str,
        primary_party: Party,
        resource_version: Optional[str] = None,
        annotations: Optional[Mapping[str, str]] = None,
    ):
        self.id = id
        self.primary_party = primary_party
        self.resource_version = resource_version
        self.annotations = annotations


class _Right(abc.ABC):
    """
    Information about an individual right for a :class:`User`.
    """

    def __setattr__(self, key, value):
        """
        Overridden to make Right objects read-only.
        """
        raise AttributeError


@final
class ReadAs(_Right):
    __slots__: Final = ("party",)
    __match_args__: Final = ("party",)

    party: Party

    def __init__(self, party: Party, /):
        object.__setattr__(self, "party", party)

    def __repr__(self) -> str:
        return f"ReadAs({self.party!r})"


@final
class ActAs(_Right):
    __slots__: Final = ("party",)
    __match_args__: Final = ("party",)

    party: Party

    def __init__(self, party: Party, /):
        object.__setattr__(self, "party", party)

    def __repr__(self) -> str:
        return f"ActAs({self.party!r})"


@final
class _Admin(_Right):
    __slots__: Final = ()
    __match_args__: Final = ()

    def __repr__(self) -> str:
        return "Admin"


Admin = _Admin()


@final
class _IdentityProviderAdmin(_Right):
    __slots__: Final = ()
    __match_args__: Final = ()

    def __repr__(self) -> str:
        return "IdentityProviderAdmin"


IdentityProviderAdmin = _IdentityProviderAdmin()


Right: TypeAlias = _Admin | _IdentityProviderAdmin | ReadAs | ActAs


class PartyInfo:
    """
    Full information about a ``Party``.
    """

    __slots__ = ("_party", "_display_name", "_is_local")
    if TYPE_CHECKING:
        _party: Party
        _display_name: str
        _is_local: bool

    def __init__(self, party: Party, display_name: str, is_local: bool):
        object.__setattr__(self, "_party", party)
        object.__setattr__(self, "_display_name", display_name)
        object.__setattr__(self, "_is_local", is_local)

    @property
    def party(self) -> Party:
        """
        The stable unique identifier of a Daml ``Party``.
        """
        return self._party

    @property
    def display_name(self) -> str:
        """
        The human-readable name associated with the ``Party``.
        """
        return self._display_name

    @property
    def is_local(self) -> bool:
        """
        Indicates if the ``Party`` is hosted by the backing participant.
        """
        return self._is_local


class Version:
    __slots__ = ("version", "features")

    version: Final[str]  # type: ignore
    features: Final[VersionFeatures]  # type: ignore

    def __init__(self, version: str, features: VersionFeatures):
        object.__setattr__(self, "version", version)
        object.__setattr__(self, "features", features)


class VersionFeatures:
    __slots__ = ("user_management",)

    user_management: Final[VersionUserManagementFeature]  # type: ignore

    def __init__(self, user_management: VersionUserManagementFeature):
        object.__setattr__(self, "user_management", user_management)


class VersionUserManagementFeature:
    __slots__ = ("supported", "max_rights_per_user", "max_users_page_size")

    supported: Final[bool]  # type: ignore
    max_rights_per_user: Final[int]  # type: ignore
    max_users_page_size: Final[int]  # type: ignore

    def __init__(self, supported: bool, max_rights_per_user: int, max_users_page_size: int):
        object.__setattr__(self, "supported", supported)
        object.__setattr__(self, "max_rights_per_user", max_rights_per_user)
        object.__setattr__(self, "max_users_page_size", max_users_page_size)


class MeteringReport:
    __slots__ = ("participant", "request", "final", "applications")

    participant: str
    request: MeteringReportRequest
    final: bool
    applications: Sequence[MeteringReportApplication]

    def __init__(
        self,
        participant: str,
        request: MeteringReportRequest,
        final: bool,
        applications: Sequence[MeteringReportApplication],
    ):
        object.__setattr__(self, "participant", participant)
        object.__setattr__(self, "request", request)
        object.__setattr__(self, "final", final)
        object.__setattr__(self, "applications", applications)


class MeteringReportRequest:
    __slots__ = ("application", "from_", "to")
    application: str
    from_: datetime
    to: datetime

    def __init__(self, application: str, from_: datetime, to: datetime):
        object.__setattr__(self, "application", application)
        object.__setattr__(self, "from_", from_)
        object.__setattr__(self, "to", to)


class MeteringReportApplication:
    __slots__ = ("application", "events")

    application: str
    events: int

    def __init__(self, application: str, events: int):
        object.__setattr__(self, "application", application)
        object.__setattr__(self, "events", events)


def validate_template_id(value: str | TypeConName) -> TypeConName:
    if isinstance(value, TypeConName):
        return value
    else:
        return parse_type_con_name(value)
