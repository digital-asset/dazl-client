# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime
import sys
from typing import (
    AbstractSet,
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Literal,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    Union,
    overload,
    runtime_checkable,
)

from ..damlast import TypeConName
from ..damlast.daml_lf_1 import PackageRef
from ..prim import ContractData, ContractId, Parties, TimeDeltaLike
from ..query import Queries, Query
from .aio import Connection as AioConnection, QueryStream as AioQueryStream
from .api_types import (
    ActAs,
    Admin,
    ArchiveEvent,
    Boundary,
    Command,
    CommandMeta,
    Commands,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    Event,
    EventOrBoundary,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    MeteringReport,
    PartyInfo,
    ReadAs,
    Right,
    SubmitResponse,
    User,
    Version,
)
from .blocking import Connection as BlockingConnection, QueryStream as BlockingQueryStream
from .config import Config, ConfigArgs

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = [
    "aio",
    "ActAs",
    "Admin",
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CommandMeta",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "Event",
    "EventOrBoundary",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "PartyInfo",
    "PackageService",
    "MeteringReport",
    "ReadAs",
    "Connection",
    "QueryStream",
    "User",
]

CreateFn = TypeVar("CreateFn", bound=Callable[[CreateEvent], SubmitResponse])
ArchiveFn = TypeVar("ArchiveFn", bound=Callable[[ArchiveEvent], SubmitResponse])
BoundaryFn = TypeVar("BoundaryFn", bound=Callable[[Boundary], SubmitResponse])

# These are written as Protocols with __call__ instead of a Callable so that they can be safely
# overloaded for the asynchronous variants. See dazl.ledger.aio's typing file.

class OnCreateDecorator(Protocol):
    def __call__(self, fn: CreateFn, /) -> CreateFn: ...

class OnArchiveDecorator(Protocol):
    def __call__(self, fn: ArchiveFn, /) -> ArchiveFn: ...

class OnBoundaryDecorator(Protocol):
    def __call__(self, fn: BoundaryFn, /) -> BoundaryFn: ...

# These overload declarations were painfully constructed in careful consultation with:
#     https://github.com/python/mypy/issues/6580
#
# * ``blocking: Literal[False] = False`` must appear as the very first argument to the first
#   overload; this reflects the _actual_ default value combined with a literal value marker.
#   Putting this parameter in any other position causes the mypy error "Overloaded function
#   signatures 1 and 2 overlap with incompatible return types".
# * All other subsequent overloads must define the ``blocking`` parameter as a _non-optional_
#   positional parameter. Specifying a default value in these cases confuses mypy and MUST be
#   avoided.
# * An explicit overload typed as a bool is also required.
#
# Separately PyCharm thinks the name of the parameter "blocking" conflicts with the import to
# dazl.ledger.blocking above, even though that's not actually the case. Either way we silence
# that warning too.
#
@overload
def connect(**kwargs: Unpack[ConfigArgs]) -> AioConnection: ...

# noinspection PyShadowingNames
@overload
def connect(*, blocking: Literal[False], **kwargs: Unpack[ConfigArgs]) -> AioConnection: ...

# noinspection PyShadowingNames
@overload
def connect(*, blocking: Literal[True], **kwargs: Unpack[ConfigArgs]) -> BlockingConnection: ...

# noinspection PyShadowingNames
@overload
def connect(*, blocking: bool, **kwargs: Unpack[ConfigArgs]) -> Connection: ...

class PackageService(Protocol):
    def get_package(
        self, package_id: PackageRef, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[bytes, Awaitable[bytes]]: ...
    def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[AbstractSet[PackageRef], Awaitable[AbstractSet[PackageRef]]]: ...

@runtime_checkable
class Connection(PackageService, Protocol):
    @property
    def config(self) -> Config: ...
    @property
    def codec(self) -> Any: ...
    @property
    def is_closed(self) -> bool: ...
    def open(self) -> Union[None, Awaitable[None]]: ...
    def close(self) -> Union[None, Awaitable[None]]: ...
    def create(
        self,
        template_id: Union[str, TypeConName],
        payload: ContractData,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[CreateEvent, Awaitable[CreateEvent]]: ...
    def create_and_exercise(
        self,
        template_id: Union[str, TypeConName],
        payload: ContractData,
        choice_name: str,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[ExerciseResponse, Awaitable[ExerciseResponse]]: ...
    def exercise(
        self,
        contract_id: ContractId,
        choice_name: str,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[ExerciseResponse, Awaitable[ExerciseResponse]]: ...
    def exercise_by_key(
        self,
        template_id: Union[str, TypeConName],
        choice_name: str,
        key: Any,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[ExerciseResponse, Awaitable[ExerciseResponse]]: ...
    def submit(
        self,
        commands: Commands,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[None, Awaitable[None]]: ...
    def get_ledger_end(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[str, Awaitable[str]]: ...
    def archive(
        self,
        contract_id: ContractId,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[ArchiveEvent, Awaitable[ArchiveEvent]]: ...
    def archive_by_key(
        self,
        template_id: str,
        key: Any,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[ArchiveEvent, Awaitable[ArchiveEvent]]: ...
    def query(
        self,
        template_id: Union[str, TypeConName] = "*",
        query: Query = None,
        /,
        *,
        read_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def query_many(
        self,
        *queries: Queries,
        read_as: Optional[Parties],
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream(
        self,
        template_id: Union[str, TypeConName] = "*",
        query: Query = None,
        /,
        *,
        offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream_many(
        self,
        *queries: Queries,
        offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def get_user(
        self, user_id: Optional[str] = None, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[User, Awaitable[User]]: ...
    def create_user(
        self,
        user: User,
        rights: Optional[Sequence[Right]] = ...,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[User, Awaitable[User]]: ...
    def list_users(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[Sequence[User], Awaitable[Sequence[User]]]: ...
    def list_user_rights(
        self, user_id: Optional[str] = None, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[Sequence[Right], Awaitable[Sequence[Right]]]: ...
    def allocate_party(
        self,
        *,
        identifier_hint: Optional[str] = None,
        display_name: Optional[str] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[PartyInfo, Awaitable[PartyInfo]]: ...
    def list_known_parties(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[Sequence[PartyInfo], Awaitable[Sequence[PartyInfo]]]: ...
    def upload_package(
        self, contents: bytes, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[None, Awaitable[None]]: ...
    def get_version(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Union[Version, Awaitable[Version]]: ...
    def get_metering_report(
        self,
        from_: datetime,
        to: Optional[datetime] = None,
        application_id: Optional[str] = None,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Union[MeteringReport, Awaitable[MeteringReport]]: ...

@runtime_checkable
class QueryStream(Protocol):
    @overload
    def on_create(self) -> OnCreateDecorator: ...
    @overload
    def on_create(self, fn: CreateFn, /) -> CreateFn: ...
    @overload
    def on_create(self, name: Union[str, TypeConName], /) -> OnCreateDecorator: ...
    @overload
    def on_create(self, name: Union[str, TypeConName], fn: CreateFn, /) -> CreateFn: ...
    @overload
    def on_archive(self) -> OnArchiveDecorator: ...
    @overload
    def on_archive(self, fn: ArchiveFn, /) -> ArchiveFn: ...
    @overload
    def on_archive(self, name: Union[str, TypeConName], /) -> OnArchiveDecorator: ...
    @overload
    def on_archive(self, name: Union[str, TypeConName], fn: ArchiveFn, /) -> ArchiveFn: ...
    @overload
    def on_boundary(self) -> OnBoundaryDecorator: ...
    @overload
    def on_boundary(self, fn: BoundaryFn, /) -> BoundaryFn: ...
    def close(self) -> Union[None, Awaitable[None]]: ...
    def run(self) -> Union[None, Awaitable[None]]: ...
    def creates(self) -> Union[Iterator[CreateEvent], AsyncIterator[CreateEvent]]: ...
    def events(self) -> Union[Iterator[Event], AsyncIterator[Event]]: ...
    def items(self) -> Union[Iterator[EventOrBoundary], AsyncIterator[EventOrBoundary]]: ...
