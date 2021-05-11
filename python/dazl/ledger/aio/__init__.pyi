# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import abc
import sys
from typing import (
    AbstractSet,
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    DefaultDict,
    List,
    Optional,
    Sequence,
    TypeVar,
    Union,
    overload,
)

from .. import (
    Connection as _Connection,
    PackageService as _PackageService,
    QueryStream as _QueryStream,
)
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...prim import ContractData, ContractId
from ...query import Queries, Query
from ..api_types import (
    ArchiveEvent,
    Boundary,
    Command,
    CreateEvent,
    ExerciseResponse,
    PartyInfo,
    SubmitResponse,
)
from .pkgloader import PackageLoader

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable

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
    def __call__(self, __fn: CreateFn) -> CreateFn: ...
    @overload
    def __call__(self, __fn: ACreateFn) -> ACreateFn: ...

class AArchiveDecorator(Protocol):
    @overload
    def __call__(self, __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def __call__(self, __fn: AArchiveFn) -> AArchiveFn: ...

class ABoundaryDecorator(Protocol):
    @overload
    def __call__(self, __fn: BoundaryFn) -> BoundaryFn: ...
    @overload
    def __call__(self, __fn: ABoundaryFn) -> ABoundaryFn: ...

class PackageService(_PackageService, Protocol):
    async def get_package(self, __package_id: PackageRef) -> bytes: ...
    async def list_package_ids(self) -> AbstractSet[PackageRef]: ...

@runtime_checkable
class Connection(_Connection, PackageService, Protocol):
    async def __aenter__(self: ConnSelf) -> ConnSelf: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    async def open(self) -> None: ...
    async def close(self) -> None: ...
    async def submit(
        self,
        __commands: Union[Command, Sequence[Command]],
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> None: ...
    async def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> CreateEvent: ...
    async def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse: ...
    async def create_and_exercise(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse: ...
    async def exercise_by_key(
        self,
        __template_id: Union[str, TypeConName],
        __choice_name: str,
        __key: Any,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse: ...
    async def archive(
        self,
        __contract_id: ContractId,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ArchiveEvent: ...
    async def archive_by_key(
        self,
        __template_id: str,
        __key: Any,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ArchiveEvent: ...
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
    async def allocate_party(
        self, *, identifier_hint: Optional[str] = None, display_name: Optional[str] = None
    ) -> PartyInfo: ...
    async def list_known_parties(self) -> Sequence[PartyInfo]: ...
    async def upload_package(self, contents: bytes) -> None: ...

# PyCharm doesn't know what to make of these overloads with respect to the parent protocol,
# but mypy understands that these type signatures do not conflict with the parent base class
# noinspection PyProtocol,PyMethodOverriding
@runtime_checkable
class QueryStream(_QueryStream, Protocol):
    @overload
    def on_create(self) -> ACreateDecorator: ...
    @overload
    def on_create(self, __fn: CreateFn) -> CreateFn: ...
    @overload
    def on_create(self, __fn: ACreateFn) -> ACreateFn: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName]) -> ACreateDecorator: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName], __fn: CreateFn) -> CreateFn: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName], __fn: ACreateFn) -> ACreateFn: ...
    @overload
    def on_archive(self) -> AArchiveDecorator: ...
    @overload
    def on_archive(self, __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def on_archive(self, __fn: AArchiveFn) -> AArchiveFn: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName]) -> AArchiveDecorator: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName], __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName], __fn: AArchiveFn) -> AArchiveFn: ...
    @overload
    def on_boundary(self) -> ABoundaryDecorator: ...
    @overload
    def on_boundary(self, __fn: BoundaryFn) -> BoundaryFn: ...
    @overload
    def on_boundary(self, __fn: ABoundaryFn) -> ABoundaryFn: ...
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
    async def _emit(self, name: str, obj: Any) -> None: ...
    async def _emit_create(self, event: CreateEvent) -> None: ...
    async def _emit_archive(self, event: ArchiveEvent) -> None: ...
    async def _emit_boundary(self, event: Boundary) -> None: ...
