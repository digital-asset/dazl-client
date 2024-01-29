# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import abc
from datetime import datetime
from typing import (
    AbstractSet,
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    DefaultDict,
    List,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    Union,
    overload,
    runtime_checkable,
)

from .. import (
    Connection as _Connection,
    PackageService as _PackageService,
    QueryStream as _QueryStream,
)
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...prim import ContractData, ContractId, Parties, TimeDeltaLike
from ...query import Queries, Query
from ..api_types import (
    ArchiveEvent,
    Boundary,
    Commands,
    CreateEvent,
    ExerciseResponse,
    MeteringReport,
    PartyInfo,
    Right,
    SubmitResponse,
    User,
    Version,
)
from .pkgloader import PackageLoader

__all__ = ["PackageService", "Connection", "QueryStream", "QueryStreamBase", "PackageLoader"]

ConnSelf = TypeVar("ConnSelf", bound="Connection")
QSSelf = TypeVar("QSSelf", bound="QueryStream")
CreateFn = TypeVar("CreateFn", bound=Callable[[CreateEvent], SubmitResponse])
ACreateFn = TypeVar("ACreateFn", bound=Callable[[CreateEvent], Awaitable[SubmitResponse]])
ArchiveFn = TypeVar("ArchiveFn", bound=Callable[[ArchiveEvent], SubmitResponse])
AArchiveFn = TypeVar("AArchiveFn", bound=Callable[[ArchiveEvent], Awaitable[SubmitResponse]])
BoundaryFn = TypeVar("BoundaryFn", bound=Callable[[Boundary], SubmitResponse])
ABoundaryFn = TypeVar("ABoundaryFn", bound=Callable[[Boundary], Awaitable[SubmitResponse]])

# mypy treats Callables as _covariant_ in their arguments, and _contravariant_ in their return
# types. That means that A -> A and B -> B are incompatible types.
#
# However, we can define an object that has two overloaded __call__ signatures, which means that
# we have an *object* that can be used like a function, but supports adding additional "overloads",
# such that the base type supports being called with A, and returns A, and the subtype supports
# that, AS WELL AS being called with B and returning B.
#
# mypy completely understands what is going on here, and manages to validate correct usages of these
# decorators, *as well as* flagging incorrect usages!
class ACreateDecorator(Protocol):
    @overload
    def __call__(self, fn: CreateFn, /) -> CreateFn: ...
    @overload
    def __call__(self, fn: ACreateFn, /) -> ACreateFn: ...

class AArchiveDecorator(Protocol):
    @overload
    def __call__(self, fn: ArchiveFn, /) -> ArchiveFn: ...
    @overload
    def __call__(self, fn: AArchiveFn, /) -> AArchiveFn: ...

class ABoundaryDecorator(Protocol):
    @overload
    def __call__(self, fn: BoundaryFn, /) -> BoundaryFn: ...
    @overload
    def __call__(self, fn: ABoundaryFn, /) -> ABoundaryFn: ...

class PackageService(_PackageService, Protocol):
    async def get_package(
        self, package_id: PackageRef, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> bytes: ...
    async def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> AbstractSet[PackageRef]: ...

@runtime_checkable
class Connection(_Connection, PackageService, Protocol):
    async def __aenter__(self: ConnSelf) -> ConnSelf: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    async def open(self) -> None: ...
    async def close(self) -> None: ...
    async def submit(
        self,
        commands: Commands,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> None: ...
    async def create(
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
    ) -> CreateEvent: ...
    async def exercise(
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
    ) -> ExerciseResponse: ...
    async def create_and_exercise(
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
    ) -> ExerciseResponse: ...
    async def exercise_by_key(
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
    ) -> ExerciseResponse: ...
    async def archive(
        self,
        contract_id: ContractId,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ArchiveEvent: ...
    async def archive_by_key(
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
    ) -> ArchiveEvent: ...
    async def get_ledger_end(self, *, timeout: Optional[TimeDeltaLike] = ...) -> str: ...
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
        read_as: Optional[Parties] = None,
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
    async def get_user(
        self, user_id: Optional[str] = None, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> User: ...
    async def create_user(
        self,
        user: User,
        rights: Optional[Sequence[Right]] = ...,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> User: ...
    async def list_users(self, *, timeout: Optional[TimeDeltaLike] = ...) -> Sequence[User]: ...
    async def list_user_rights(
        self, user_id: Optional[str] = None, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Sequence[Right]: ...
    async def allocate_party(
        self,
        *,
        identifier_hint: Optional[str] = None,
        display_name: Optional[str] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> PartyInfo: ...
    async def list_known_parties(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Sequence[PartyInfo]: ...
    async def get_version(self, *, timeout: Optional[TimeDeltaLike] = ...) -> Version: ...
    async def upload_package(
        self, contents: bytes, /, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> None: ...
    async def get_metering_report(
        self,
        from_: datetime,
        to: Optional[datetime] = None,
        application_id: Optional[str] = None,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> MeteringReport: ...

# PyCharm doesn't know what to make of these overloads with respect to the parent protocol,
# but mypy understands that these type signatures do not conflict with the parent base class
# noinspection PyProtocol,PyMethodOverriding
@runtime_checkable
class QueryStream(_QueryStream, Protocol):
    @overload
    def on_create(self) -> ACreateDecorator: ...
    @overload
    def on_create(self, fn: CreateFn, /) -> CreateFn: ...
    @overload
    def on_create(self, fn: ACreateFn, /) -> ACreateFn: ...
    @overload
    def on_create(self, name: Union[str, TypeConName], /) -> ACreateDecorator: ...
    @overload
    def on_create(self, name: Union[str, TypeConName], fn: CreateFn, /) -> CreateFn: ...
    @overload
    def on_create(self, name: Union[str, TypeConName], fn: ACreateFn, /) -> ACreateFn: ...
    @overload
    def on_archive(self) -> AArchiveDecorator: ...
    @overload
    def on_archive(self, fn: ArchiveFn, /) -> ArchiveFn: ...
    @overload
    def on_archive(self, fn: AArchiveFn, /) -> AArchiveFn: ...
    @overload
    def on_archive(self, name: Union[str, TypeConName], /) -> AArchiveDecorator: ...
    @overload
    def on_archive(self, name: Union[str, TypeConName], fn: ArchiveFn, /) -> ArchiveFn: ...
    @overload
    def on_archive(self, name: Union[str, TypeConName], fn: AArchiveFn, /) -> AArchiveFn: ...
    @overload
    def on_boundary(self) -> ABoundaryDecorator: ...
    @overload
    def on_boundary(self, fn: BoundaryFn, /) -> BoundaryFn: ...
    @overload
    def on_boundary(self, fn: ABoundaryFn, /) -> ABoundaryFn: ...
    def creates(self) -> AsyncIterator[CreateEvent]: ...
    def events(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent]]: ...
    def items(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    def __aiter__(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    async def run(self) -> None: ...
    async def close(self) -> None: ...
    async def __aenter__(self: QSSelf) -> QSSelf: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...

class QueryStreamBase(QueryStream, abc.ABC):
    @property
    def _callbacks(self) -> DefaultDict[str, List[Callable]]: ...
    @abc.abstractmethod
    def items(self): ...
    async def _emit(self, name: str, obj: Any, /) -> None: ...
    async def _emit_create(self, event: CreateEvent, /) -> None: ...
    async def _emit_archive(self, event: ArchiveEvent, /) -> None: ...
    async def _emit_boundary(self, event: Boundary, /) -> None: ...
