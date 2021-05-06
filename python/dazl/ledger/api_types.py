# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import (
    TYPE_CHECKING,
    AbstractSet,
    Any,
    Collection,
    Mapping,
    NoReturn,
    Optional,
    Sequence,
    Union,
)

from ..damlast.daml_lf_1 import TypeConName
from ..damlast.lookup import parse_type_con_name
from ..prim import ContractData, ContractId, Party
from ..util.typing import safe_cast

__all__ = [
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "Event",
    "EventOrBoundary",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "PartyInfo",
    "SubmitResponse",
]


class Command:
    """
    Base class for write-side commands.

    This class provides no functionality on its own.
    """

    def __setattr__(self, key, value) -> NoReturn:
        """
        Raise :class:`AttributeError`; instances of this class are immutable.
        """
        raise AttributeError("Command instances are read-only")


class CreateCommand(Command):
    """
    A command that creates a contract without any predecessors.
    """

    __slots__ = ("_template_id", "_payload")
    if TYPE_CHECKING:
        _template_id: TypeConName
        _payload: ContractData

    def __init__(self, template_id: Union[str, TypeConName], payload: ContractData):
        """
        Initialize a :class:`CreateCommand`.

        :param template_id:
            The template of the contract to be created.
        :param payload:
            The template arguments for the contract to be created.
        """
        object.__setattr__(self, "_template_id", validate_template_id(template_id))
        object.__setattr__(self, "_payload", payload)

    @property
    def template_id(self) -> TypeConName:
        """
        Return the template of the contract to be created.
        """
        return self._template_id

    @property
    def payload(self) -> Mapping[str, Any]:
        """
        Return the template arguments for the contract to be created.
        """
        return self._payload

    def __eq__(self, other: "Any") -> bool:
        return (
            isinstance(other, CreateCommand)
            and self.template_id == other.template_id
            and self.payload == other.payload
        )

    def __repr__(self) -> str:
        return f"CreateCommand({self.template_id}, {self.payload})"


class CreateAndExerciseCommand(Command):
    """
    A command that exercises a choice on a newly-created contract in a single transaction.

    Instead of creating an instance of this command and submitting it with :meth:`Connection.submit`,
    consider using :meth:`Connection.create_and_exercise` instead, which also gives you access to
    the result of exercising the choice.
    """

    __slots__ = ("_template_id", "_payload", "_choice", "_argument")
    if TYPE_CHECKING:
        _template_id: TypeConName
        _payload: ContractData
        _choice: str
        _argument: Any

    def __init__(
        self,
        template_id: Union[str, TypeConName],
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
        object.__setattr__(self, "_template_id", validate_template_id(template_id))
        object.__setattr__(self, "_payload", payload)
        object.__setattr__(self, "_choice", choice)
        object.__setattr__(self, "_argument", dict(argument) if argument is not None else dict())

    @property
    def template_id(self) -> TypeConName:
        """
        The template of the contract to be created.
        """
        return self._template_id

    @property
    def payload(self) -> ContractData:
        """
        The template arguments for the contract to be created.
        """
        return self._payload

    @property
    def choice(self) -> str:
        """
        The choice to exercise.
        """
        return self._choice

    @property
    def argument(self) -> Any:
        """
        The choice arguments.
        """
        return self._argument

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


class ExerciseCommand(Command):
    """
    A command that exercises a choice on a contract identified by its contract ID.

    Instead of creating an instance of this command and submitting it with :meth:`Connection.submit`,
    consider using :meth:`Connection.exercise` instead, which also gives you access to the result of
    exercising the choice.
    """

    __slots__ = ("_choice", "_contract_id", "_argument")
    if TYPE_CHECKING:
        _choice: str
        _contract_id: ContractId
        _argument: Optional[Any]

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
        object.__setattr__(self, "_choice", safe_cast(str, choice))
        object.__setattr__(self, "_contract_id", safe_cast(ContractId, contract_id))
        object.__setattr__(self, "_argument", dict(argument) if argument is not None else dict())

    @property
    def contract_id(self) -> ContractId:
        """
        The contract ID of the contract to exercise.
        """
        return self._contract_id

    @property
    def choice(self) -> str:
        """
        The choice to exercise.
        """
        return self._choice

    @property
    def argument(self) -> Any:
        """
        The choice arguments.
        """
        return self._argument

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, ExerciseCommand)
            and self.choice == other.choice
            and self.contract_id == other.contract_id
            and self.argument == other.argument
        )

    def __repr__(self):
        return f"ExerciseCommand({self.choice!r}, {self.contract_id}, {self.argument})"


class ExerciseByKeyCommand(Command):
    """
    A command that exercises a choice on a contract identified by its contract key.

    Instead of creating an instance of this command and submitting it with :meth:`Connection.submit`,
    consider using :meth:`Connection.exercise_by_key` instead, which also gives you access to the
    result of exercising the choice.
    """

    __slots__ = ("_template_id", "_key", "_choice", "_argument")
    if TYPE_CHECKING:
        _template_id: TypeConName
        _key: Any
        _choice: str
        _argument: Optional[Any]

    def __init__(
        self,
        template_id: Union[str, TypeConName],
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
        object.__setattr__(self, "_template_id", validate_template_id(template_id))
        object.__setattr__(self, "_key", key)
        object.__setattr__(self, "_choice", choice)
        object.__setattr__(self, "_argument", dict(argument) if argument is not None else dict())

    @property
    def template_id(self) -> TypeConName:
        """
        The contract template type.
        """
        return self._template_id

    @property
    def key(self) -> Any:
        """
        The contract key of the contract to exercise.
        """
        return self._key

    @property
    def choice(self) -> str:
        """
        The choice to exercise.
        """
        return self._choice

    @property
    def argument(self) -> Any:
        """
        The choice arguments.
        """
        return self._argument

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


class CreateEvent:
    """
    An event that indicates a newly-created contract.
    """

    __slots__ = (
        "_contract_id",
        "_payload",
        "_signatories",
        "_observers",
        "_agreement_text",
        "_key",
    )
    if TYPE_CHECKING:
        _contract_id: ContractId
        _payload: ContractData
        _signatories: AbstractSet[Party]
        _observers: AbstractSet[Party]
        _agreement_text: Optional[str]
        _key: Optional[Any]

    def __init__(
        self,
        contract_id: ContractId,
        payload: ContractData,
        signatories: Collection[Party],
        observers: Collection[Party],
        agreement_text: Optional[str],
        key: Optional[Any],
    ):
        object.__setattr__(self, "_contract_id", contract_id)
        object.__setattr__(self, "_payload", payload)
        object.__setattr__(self, "_signatories", frozenset(signatories))
        object.__setattr__(self, "_observers", frozenset(observers))
        object.__setattr__(self, "_agreement_text", agreement_text)
        object.__setattr__(self, "_key", key)

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

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, CreateEvent)
            and self.contract_id == other.contract_id
            and self.payload == other.payload
            and self.signatories == other.signatories
            and self.observers == other.observers
            and self.agreement_text == other.agreement_text
            and self.key == other.key
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


Event = Union[CreateEvent, ArchiveEvent]


class Boundary:
    """
    An event that indicates a boundary in a query stream where events can be resumed.
    """

    __slots__ = ("_offset",)
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


EventOrBoundary = Union[Event, Boundary]


class ExerciseResponse:
    """
    Returned when directly exercising a choice using :meth:`Connection.create_and_exercise`,
    :meth:`Connection.exercise`, or :meth:`Connection.exercise_by_key`.
    """

    __slots__ = ("_result", "_events")
    if TYPE_CHECKING:
        _result: Optional[Any]
        _events: Sequence[Union[CreateEvent, ArchiveEvent]]

    def __init__(self, result: Optional[Any], events: Sequence[Union[CreateEvent, ArchiveEvent]]):
        object.__setattr__(self, "_result", result)
        object.__setattr__(self, "_events", tuple(events))

    @property
    def result(self) -> Optional[Any]:
        """
        The return value of the choice.
        """
        return self._result

    @property
    def events(self) -> Sequence[Union[CreateEvent, ArchiveEvent]]:
        """
        All of the events that occurred as a result of exercising the choice, including the archive
        event for the contract if the choice is consuming (or otherwise archives it as part of its
        execution).
        """
        return self._events

    def __repr__(self):
        return f"ExerciseResponse(result={self.result}, events={self.events})"


SubmitResponse = Union[None, CreateEvent, ExerciseResponse]


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
    def party(self) -> "Party":
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


def validate_template_id(value: Union[str, TypeConName]) -> TypeConName:
    if isinstance(value, TypeConName):
        return value
    else:
        return parse_type_con_name(value)
