# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import completion_pb2 as _completion_pb2
from . import offset_checkpoint_pb2 as _offset_checkpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompletionStreamRequest(_message.Message):
    __slots__ = ("user_id", "parties", "begin_exclusive")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    BEGIN_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    parties: _containers.RepeatedScalarFieldContainer[str]
    begin_exclusive: int
    def __init__(self, user_id: _Optional[str] = ..., parties: _Optional[_Iterable[str]] = ..., begin_exclusive: _Optional[int] = ...) -> None: ...

class GetCompletionsRequest(_message.Message):
    __slots__ = ("parties", "begin_exclusive")
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    BEGIN_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    begin_exclusive: int
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., begin_exclusive: _Optional[int] = ...) -> None: ...

class CompletionStreamResponse(_message.Message):
    __slots__ = ("completion", "offset_checkpoint")
    COMPLETION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    completion: _completion_pb2.Completion
    offset_checkpoint: _offset_checkpoint_pb2.OffsetCheckpoint
    def __init__(self, completion: _Optional[_Union[_completion_pb2.Completion, _Mapping]] = ..., offset_checkpoint: _Optional[_Union[_offset_checkpoint_pb2.OffsetCheckpoint, _Mapping]] = ...) -> None: ...

class GetCompletionByHashRequest(_message.Message):
    __slots__ = ("transaction_hash",)
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    transaction_hash: bytes
    def __init__(self, transaction_hash: _Optional[bytes] = ...) -> None: ...

class GetCompletionByHashResponse(_message.Message):
    __slots__ = ("accepted_completion", "last_rejected_completions")
    ACCEPTED_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    LAST_REJECTED_COMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    accepted_completion: _completion_pb2.Completion
    last_rejected_completions: _containers.RepeatedCompositeFieldContainer[_completion_pb2.Completion]
    def __init__(self, accepted_completion: _Optional[_Union[_completion_pb2.Completion, _Mapping]] = ..., last_rejected_completions: _Optional[_Iterable[_Union[_completion_pb2.Completion, _Mapping]]] = ...) -> None: ...
