# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from logging import Logger
from os import PathLike
from typing import Collection, Optional, Union

from ..prim import Party, TimeDeltaLike
from .api_types import (
    ArchiveEvent,
    Boundary,
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    PartyInfo,
)

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
]

# TODO: Look into ways of generating this signature from Config.create
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
): ...
