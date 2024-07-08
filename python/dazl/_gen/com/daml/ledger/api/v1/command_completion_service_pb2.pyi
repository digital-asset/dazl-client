# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import completion_pb2 as _completion_pb2
from . import ledger_offset_pb2 as _ledger_offset_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompletionStreamRequest(_message.Message):
    __slots__ = ["ledger_id", "application_id", "parties", "offset"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    application_id: str
    parties: _containers.RepeatedScalarFieldContainer[str]
    offset: _ledger_offset_pb2.LedgerOffset
    def __init__(self, ledger_id: _Optional[str] = ..., application_id: _Optional[str] = ..., parties: _Optional[_Iterable[str]] = ..., offset: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ...) -> None: ...

class CompletionStreamResponse(_message.Message):
    __slots__ = ["checkpoint", "completions"]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    COMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    checkpoint: Checkpoint
    completions: _containers.RepeatedCompositeFieldContainer[_completion_pb2.Completion]
    def __init__(self, checkpoint: _Optional[_Union[Checkpoint, _Mapping]] = ..., completions: _Optional[_Iterable[_Union[_completion_pb2.Completion, _Mapping]]] = ...) -> None: ...

class Checkpoint(_message.Message):
    __slots__ = ["record_time", "offset"]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    record_time: _timestamp_pb2.Timestamp
    offset: _ledger_offset_pb2.LedgerOffset
    def __init__(self, record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., offset: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ...) -> None: ...

class CompletionEndRequest(_message.Message):
    __slots__ = ["ledger_id"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    def __init__(self, ledger_id: _Optional[str] = ...) -> None: ...

class CompletionEndResponse(_message.Message):
    __slots__ = ["offset"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: _ledger_offset_pb2.LedgerOffset
    def __init__(self, offset: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ...) -> None: ...
