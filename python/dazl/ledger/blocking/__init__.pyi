# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import sys
from typing import Any, Iterator, Optional, Sequence, TypeVar, Union

from .. import Connection as _Connection, QueryStream as _QueryStream
from ...damlast.daml_lf_1 import TypeConName
from ...prim import ContractData, ContractId
from ...query import Queries, Query
from ..api_types import ArchiveEvent, Boundary, Command, CreateEvent, ExerciseResponse

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable

__all__ = ["Connection", "QueryStream"]

Self = TypeVar("Self")
@runtime_checkable
class Connection(_Connection, Protocol):
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
    def query(self, __template_id: str = "*", __query: Query = None) -> QueryStream: ...
    def query_many(self, *q: Queries) -> QueryStream: ...
    def stream(
        self, __template_id: str = "*", __query: Query = None, *, offset: Optional[str] = None
    ) -> QueryStream: ...
    def stream_many(self, *q: Queries, offset: Optional[str] = None) -> QueryStream: ...

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
