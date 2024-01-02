# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....pruning.admin.v0 import pruning_pb2 as _pruning_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PruneRequest(_message.Message):
    __slots__ = ["prune_up_to"]
    PRUNE_UP_TO_FIELD_NUMBER: _ClassVar[int]
    prune_up_to: str
    def __init__(self, prune_up_to: _Optional[str] = ...) -> None: ...

class PruneResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetSafePruningOffsetRequest(_message.Message):
    __slots__ = ["before_or_at", "ledger_end"]
    BEFORE_OR_AT_FIELD_NUMBER: _ClassVar[int]
    LEDGER_END_FIELD_NUMBER: _ClassVar[int]
    before_or_at: _timestamp_pb2.Timestamp
    ledger_end: str
    def __init__(self, before_or_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ledger_end: _Optional[str] = ...) -> None: ...

class GetSafePruningOffsetResponse(_message.Message):
    __slots__ = ["safe_pruning_offset", "no_safe_pruning_offset"]
    class NoSafePruningOffset(_message.Message):
        __slots__ = []  # type: ignore
        def __init__(self) -> None: ...
    SAFE_PRUNING_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NO_SAFE_PRUNING_OFFSET_FIELD_NUMBER: _ClassVar[int]
    safe_pruning_offset: str
    no_safe_pruning_offset: GetSafePruningOffsetResponse.NoSafePruningOffset
    def __init__(self, safe_pruning_offset: _Optional[str] = ..., no_safe_pruning_offset: _Optional[_Union[GetSafePruningOffsetResponse.NoSafePruningOffset, _Mapping]] = ...) -> None: ...
