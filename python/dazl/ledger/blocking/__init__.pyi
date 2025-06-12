# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime
from typing import (
    AbstractSet,
    Any,
    Iterator,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    runtime_checkable,
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
    User,
    Version,
)
from ..auth import TokenOrTokenProvider

__all__ = ["PackageService", "Connection", "QueryStream"]

Self = TypeVar("Self")

class PackageService(Protocol):
    def get_package(
        self,
        package_id: PackageRef,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> bytes: ...
    def list_package_ids(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> AbstractSet[PackageRef]: ...

@runtime_checkable
class Connection(PackageService, Protocol):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def submit(
        self,
        commands: Commands,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> None: ...
    def create(
        self,
        template_id: str | TypeConName,
        payload: ContractData,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> CreateEvent: ...
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
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ExerciseResponse: ...
    def create_and_exercise(
        self,
        template_id: str | TypeConName,
        payload: ContractData,
        choice_name: str,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ExerciseResponse: ...
    def exercise_by_key(
        self,
        template_id: str | TypeConName,
        choice_name: str,
        key: Any,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ExerciseResponse: ...
    def archive(
        self,
        contract_id: ContractId,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ArchiveEvent: ...
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
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> ArchiveEvent: ...
    def get_ledger_end(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> str: ...
    def query(
        self,
        template_id: str | TypeConName = "*",
        query: Query = None,
        /,
        *,
        read_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def query_many(
        self,
        *queries: Queries,
        read_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream(
        self,
        template_id: str | TypeConName = "*",
        query: Query = None,
        /,
        *,
        offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream_many(
        self,
        *queries: Queries,
        offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def get_user(
        self,
        user_id: Optional[str] = None,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> User: ...
    def create_user(
        self,
        user: User,
        rights: Optional[Sequence[Right]] = ...,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> User: ...
    def list_users(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Sequence[User]: ...
    def list_user_rights(
        self,
        user_id: Optional[str] = None,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Sequence[Right]: ...
    def allocate_party(
        self,
        *,
        identifier_hint: Optional[str] = None,
        display_name: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> PartyInfo: ...
    def list_known_parties(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Sequence[PartyInfo]: ...
    def get_version(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> Version: ...
    def upload_package(
        self,
        contents: bytes,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> None: ...
    def get_metering_report(
        self,
        from_: datetime,
        to: Optional[datetime] = None,
        application_id: Optional[str] = None,
        *,
        token: Optional[TokenOrTokenProvider] = ...,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> MeteringReport: ...

@runtime_checkable
class QueryStream(Protocol):
    def creates(self) -> Iterator[CreateEvent]: ...
    def events(self) -> Iterator[CreateEvent | ArchiveEvent]: ...
    def items(self) -> Iterator[CreateEvent | ArchiveEvent | Boundary]: ...
    def __iter__(self) -> Iterator[CreateEvent | ArchiveEvent | Boundary]: ...
    def run(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
