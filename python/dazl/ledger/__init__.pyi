# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from logging import Logger
from os import PathLike
import sys
from typing import Callable, Collection, Optional, TypeVar, Union, overload

from . import aio, blocking
from ..damlast.lookup import SymbolLookup
from ..prim import Party, TimeDeltaLike
from .api_types import (
    ActAs,
    Admin,
    ArchiveEvent,
    Boundary,
    Command,
    CommandMeta,
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
from .config import Config

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol
else:
    from typing_extensions import Literal, Protocol

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
    lookup: Optional[SymbolLookup] = None,
) -> aio.Connection: ...

# noinspection PyShadowingNames
@overload
def connect(
    *,
    blocking: Literal[False],
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
    lookup: Optional[SymbolLookup] = None,
) -> aio.Connection: ...

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
    lookup: Optional[SymbolLookup] = None,
) -> blocking.Connection: ...

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
    lookup: Optional[SymbolLookup] = None,
) -> Connection: ...

PackageService = Union[aio.PackageService, blocking.PackageService]
Connection = Union[aio.Connection, blocking.Connection]
QueryStream = Union[aio.QueryStream, blocking.QueryStream]
