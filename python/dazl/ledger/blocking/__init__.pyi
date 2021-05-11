# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import sys
from typing import AbstractSet, Any, Iterator, Optional, Sequence, TypeVar, Union

from .. import (
    Connection as _Connection,
    PackageService as _PackageService,
    QueryStream as _QueryStream,
)
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...prim import ContractData, ContractId
from ...query import Queries, Query
from ..api_types import ArchiveEvent, Boundary, Command, CreateEvent, ExerciseResponse, PartyInfo

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable

__all__ = ["PackageService", "Connection", "QueryStream"]

Self = TypeVar("Self")

class PackageService(_PackageService, Protocol):
    def get_package(self, package_id: PackageRef) -> bytes: ...
    def list_package_ids(self) -> AbstractSet[PackageRef]: ...

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
    ) -> None: ...
    def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> CreateEvent: ...
    def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
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
    ) -> ExerciseResponse: ...
    def archive(
        self,
        __contract_id: ContractId,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ArchiveEvent: ...
    def archive_by_key(
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
    def allocate_party(
        self, *, identifier_hint: Optional[str] = None, display_name: Optional[str] = None
    ) -> PartyInfo: ...
    def list_known_parties(self) -> Sequence[PartyInfo]: ...
    def upload_package(self, contents: bytes) -> None: ...

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
