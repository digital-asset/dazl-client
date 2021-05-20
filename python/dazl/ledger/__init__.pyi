# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from logging import Logger
from os import PathLike
import sys
from typing import (
    AbstractSet,
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Collection,
    Iterator,
    Optional,
    Sequence,
    TypeVar,
    Union,
    overload,
)

from ..damlast import TypeConName
from ..damlast.daml_lf_1 import PackageRef
from ..prim import ContractData, ContractId, Party, TimeDeltaLike
from ..query import Queries, Query
from .aio import Connection as AioConnection, QueryStream as AioQueryStream
from .api_types import (
    ArchiveEvent,
    Boundary,
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    Event,
    EventOrBoundary,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    PartyInfo,
    SubmitResponse,
)
from .blocking import Connection as BlockingConnection, QueryStream as BlockingQueryStream
from .config import Config

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol, runtime_checkable
else:
    from typing_extensions import Literal, Protocol, runtime_checkable

__all__ = [
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "PartyInfo",
    "PackageService",
    "Connection",
    "QueryStream",
]

CreateFn = TypeVar("CreateFn", bound=Callable[[CreateEvent], SubmitResponse])
ArchiveFn = TypeVar("ArchiveFn", bound=Callable[[ArchiveEvent], SubmitResponse])
BoundaryFn = TypeVar("BoundaryFn", bound=Callable[[Boundary], SubmitResponse])

# These are written as Protocols with __call__ instead of a Callable so that they can be safely
# overloaded for the asynchronous variants. See dazl.ledger.aio's typing file.

class OnCreateDecorator(Protocol):
    def __call__(self, __fn: CreateFn) -> CreateFn: ...

class OnArchiveDecorator(Protocol):
    def __call__(self, __fn: ArchiveFn) -> ArchiveFn: ...

class OnBoundaryDecorator(Protocol):
    def __call__(self, __fn: BoundaryFn) -> BoundaryFn: ...

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
# TODO: Look into ways of generating this signatures from Config.create
#
# noinspection PyShadowingNames
@overload
def connect(
    *,
    blocking: Literal[False] = False,
    url: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    scheme: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    application_name: Optional[str] = None,
    oauth_token: Optional[str] = None,
    oauth_token_file: Optional[str] = None,
    ca: Optional[bytes] = None,
    ca_file: Optional[PathLike] = None,
    cert: Optional[bytes] = None,
    cert_file: Optional[PathLike] = None,
    cert_key: Optional[bytes] = None,
    cert_key_file: Optional[PathLike] = None,
    connect_timeout: Optional[TimeDeltaLike] = None,
    use_http_proxy: bool = True,
    logger: Optional[Logger] = None,
    logger_name: Optional[str] = None,
    log_level: Optional[str] = None,
) -> AioConnection: ...

# noinspection PyShadowingNames
@overload
def connect(
    *,
    blocking: Literal[True],
    url: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    scheme: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    application_name: Optional[str] = None,
    oauth_token: Optional[str] = None,
    oauth_token_file: Optional[str] = None,
    ca: Optional[bytes] = None,
    ca_file: Optional[PathLike] = None,
    cert: Optional[bytes] = None,
    cert_file: Optional[PathLike] = None,
    cert_key: Optional[bytes] = None,
    cert_key_file: Optional[PathLike] = None,
    connect_timeout: Optional[TimeDeltaLike] = None,
    use_http_proxy: bool = True,
    logger: Optional[Logger] = None,
    logger_name: Optional[str] = None,
    log_level: Optional[str] = None,
) -> BlockingConnection: ...

# noinspection PyShadowingNames
@overload
def connect(
    *,
    blocking: bool,
    url: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    scheme: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    application_name: Optional[str] = None,
    oauth_token: Optional[str] = None,
    oauth_token_file: Optional[str] = None,
    ca: Optional[bytes] = None,
    ca_file: Optional[PathLike] = None,
    cert: Optional[bytes] = None,
    cert_file: Optional[PathLike] = None,
    cert_key: Optional[bytes] = None,
    cert_key_file: Optional[PathLike] = None,
    connect_timeout: Optional[TimeDeltaLike] = None,
    use_http_proxy: bool = True,
    logger: Optional[Logger] = None,
    logger_name: Optional[str] = None,
    log_level: Optional[str] = None,
) -> Connection: ...

class PackageService(Protocol):
    def get_package(self, package_id: PackageRef) -> Union[bytes, Awaitable[bytes]]: ...
    def list_package_ids(
        self,
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
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> Union[CreateEvent, Awaitable[CreateEvent]]: ...
    def create_and_exercise(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> Union[ExerciseResponse, Awaitable[ExerciseResponse]]: ...
    def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> Union[ExerciseResponse, Awaitable[ExerciseResponse]]: ...
    def exercise_by_key(
        self,
        __template_id: Union[str, TypeConName],
        __choice_name: str,
        __key: Any,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> Union[ExerciseResponse, Awaitable[ExerciseResponse]]: ...
    def submit(
        self,
        __commands: Union[Command, Sequence[Command]],
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> Union[None, Awaitable[None]]: ...
    def archive(
        self,
        __contract_id: ContractId,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> Union[ArchiveEvent, Awaitable[ArchiveEvent]]: ...
    def archive_by_key(
        self,
        __template_id: str,
        __key: Any,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> Union[ArchiveEvent, Awaitable[ArchiveEvent]]: ...
    def query(
        self, __template_id: Union[str, TypeConName] = "*", __query: Query = None
    ) -> QueryStream: ...
    def query_many(self, *queries: Queries) -> QueryStream: ...
    def stream(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        *,
        offset: Optional[str] = None,
    ) -> QueryStream: ...
    def stream_many(self, *queries: Queries, offset: Optional[str] = None) -> QueryStream: ...
    def allocate_party(
        self, *, identifier_hint: str = None, display_name: str = None
    ) -> Union[PartyInfo, Awaitable[PartyInfo]]: ...
    def list_known_parties(self) -> Union[Sequence[PartyInfo], Awaitable[Sequence[PartyInfo]]]: ...
    def upload_package(self, __contents: bytes) -> Union[None, Awaitable[None]]: ...

@runtime_checkable
class QueryStream(Protocol):
    @overload
    def on_create(self) -> OnCreateDecorator: ...
    @overload
    def on_create(self, __fn: CreateFn) -> CreateFn: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName]) -> OnCreateDecorator: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName], __fn: CreateFn) -> CreateFn: ...
    @overload
    def on_archive(self) -> OnArchiveDecorator: ...
    @overload
    def on_archive(self, __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName]) -> OnArchiveDecorator: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName], __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def on_boundary(self) -> OnBoundaryDecorator: ...
    @overload
    def on_boundary(self, __fn: BoundaryFn) -> BoundaryFn: ...
    def close(self) -> Union[None, Awaitable[None]]: ...
    def run(self) -> Union[None, Awaitable[None]]: ...
    def creates(self) -> Union[Iterator[CreateEvent], AsyncIterator[CreateEvent]]: ...
    def events(self) -> Union[Iterator[Event], AsyncIterator[Event]]: ...
    def items(self) -> Union[Iterator[EventOrBoundary], AsyncIterator[EventOrBoundary]]: ...
