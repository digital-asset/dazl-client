# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from typing import Any, Awaitable, Callable, Collection, Mapping, Optional, Sequence, TypeVar, Union

from ..prim import ContractData, ContractId, Party

__all__ = [
    "Event",
    "InitEvent",
    "ReadyEvent",
    "CreateEvent",
    "ArchiveEvent",
    "ExerciseResponse",
    "PartyInfo",
    "Query",
    "EventHandler",
    "AEventHandler",
]

Query = Union[None, Mapping[str, Any], Collection[Mapping[str, Any]]]


class Event:
    """
    Superclass of all dazl events.
    """

    __slots__ = ()

    def __setattr__(self, key, value):
        raise AttributeError("Event instances are read-only")


E = TypeVar("E", bound=Event)

EventHandler = Callable[[E], None]
AEventHandler = Union[Callable[[E], None], Callable[[E], Awaitable[None]]]


class InitEvent(Event):
    pass


class ReadyEvent(Event):
    pass


class CreateEvent(Event):
    __slots__ = ("_cid", "_cdata")

    _cid: "ContractId"
    _cdata: "ContractData"

    def __init__(self, cid: "ContractId", cdata: "ContractData"):
        object.__setattr__(self, "_cid", cid)
        object.__setattr__(self, "_cdata", cdata)

    @property
    def cid(self) -> "ContractId":
        return self._cid

    @property
    def cdata(self) -> "ContractData":
        return self._cdata


class ArchiveEvent(Event):
    __slots__ = ("_cid",)

    _cid: "ContractId"

    def __init__(self, cid: "ContractId"):
        object.__setattr__(self, "_cid", cid)

    @property
    def cid(self) -> "ContractId":
        return self._cid


class ExerciseResponse:
    __slots__ = "_result", "_events"

    _result: "Optional[Any]"
    _events: "Sequence[Union[CreateEvent, ArchiveEvent]]"

    def __init__(
        self, result: "Optional[Any]", events: "Sequence[Union[CreateEvent, ArchiveEvent]]"
    ):
        object.__setattr__(self, "_result", result)
        object.__setattr__(self, "_events", tuple(events))

    @property
    def result(self) -> "Optional[Any]":
        return self._result

    @property
    def events(self) -> "Sequence[Union[CreateEvent, ArchiveEvent]]":
        return self._events

    def __repr__(self):
        return f"ExerciseResponse(result={self.result}, events={self.events})"


class PartyInfo:
    __slots__ = "_party", "_display_name", "_is_local"

    _party: "Party"
    _display_name: str
    _is_local: bool

    def __init__(self, party: "Party", display_name: str, is_local: bool):
        object.__setattr__(self, "_party", party)
        object.__setattr__(self, "_display_name", display_name)
        object.__setattr__(self, "_is_local", is_local)

    @property
    def party(self) -> "Party":
        return self._party

    @property
    def display_name(self) -> str:
        return self._display_name

    @property
    def is_local(self) -> bool:
        return self._is_local
