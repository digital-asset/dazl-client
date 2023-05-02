# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from datetime import datetime
import sys
from typing import (
    AbstractSet,
    Any,
    Collection,
    Iterator,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    Union,
    runtime_checkable,
)

from .. import (
    Connection as _Connection,
    PackageService as _PackageService,
    QueryStream as _QueryStream,
)
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...prim import ContractData, ContractId, Party, TimeDeltaLike
from ...query import Queries, Query
from ..api_types import (
    ArchiveEvent,
    Boundary,
    Command,
    CreateEvent,
    ExerciseResponse,
    MeteringReport,
    PartyInfo,
    Right,
    User,
    Version,
)
from .pkgloader import PackageLoader

__all__ = ["PackageService", "Connection", "QueryStream", "PackageLoader"]

Self = TypeVar("Self")

class PackageService(_PackageService, Protocol):
    def get_package(
        self, package_id: PackageRef, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> bytes: ...
    def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> AbstractSet[PackageRef]: ...

@runtime_checkable
class Connection(_Connection, PackageService, Protocol):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def submit(
        self,
        __commands: Union[Command, Sequence[Command]],
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> None: ...
    def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> CreateEvent: ...
    def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ExerciseResponse: ...
    def create_and_exercise(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ExerciseResponse: ...
    def exercise_by_key(
        self,
        __template_id: Union[str, TypeConName],
        __choice_name: str,
        __key: Any,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ExerciseResponse: ...
    def archive(
        self,
        __contract_id: ContractId,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ArchiveEvent: ...
    def archive_by_key(
        self,
        __template_id: str,
        __key: Any,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ArchiveEvent: ...
    def get_ledger_end(self, *, timeout: Optional[TimeDeltaLike] = ...) -> str: ...
    def query(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def query_many(
        self,
        *queries: Queries,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        *,
        offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream_many(
        self,
        *queries: Queries,
        offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def get_user(
        self, user_id: Optional[str] = None, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> User: ...
    def create_user(
        self,
        user: User,
        rights: Optional[Sequence[Right]] = ...,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> User: ...
    def list_users(self, *, timeout: Optional[TimeDeltaLike] = ...) -> Sequence[User]: ...
    def list_user_rights(
        self, user_id: Optional[str] = None, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Sequence[Right]: ...
    def allocate_party(
        self,
        *,
        identifier_hint: Optional[str] = None,
        display_name: Optional[str] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> PartyInfo: ...
    def list_known_parties(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Sequence[PartyInfo]: ...
    def get_version(self, *, timeout: Optional[TimeDeltaLike] = ...) -> Version: ...
    def upload_package(
        self, contents: bytes, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> None: ...
    def get_metering_report(
        self,
        from_: datetime,
        to: Optional[datetime] = None,
        application_id: Optional[str] = None,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> MeteringReport: ...

@runtime_checkable
class QueryStream(_QueryStream, Protocol):
    def creates(self) -> Iterator[CreateEvent]: ...
    def events(self) -> Iterator[Union[CreateEvent, ArchiveEvent]]: ...
    def items(self) -> Iterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    def __iter__(self) -> Iterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    def run(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
