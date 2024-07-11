# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import sequencer_administration_service_pb2 as _sequencer_administration_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerSnapshot(_message.Message):
    __slots__ = ["latest_timestamp", "head_member_counters", "status", "additional"]
    class HeadMemberCountersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    LATEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HEAD_MEMBER_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    latest_timestamp: _timestamp_pb2.Timestamp
    head_member_counters: _containers.ScalarMap[str, int]
    status: _sequencer_administration_service_pb2.SequencerPruningStatus
    additional: ImplementationSpecificInfo
    def __init__(self, latest_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., head_member_counters: _Optional[_Mapping[str, int]] = ..., status: _Optional[_Union[_sequencer_administration_service_pb2.SequencerPruningStatus, _Mapping]] = ..., additional: _Optional[_Union[ImplementationSpecificInfo, _Mapping]] = ...) -> None: ...

class ImplementationSpecificInfo(_message.Message):
    __slots__ = ["implementation_name", "info"]
    IMPLEMENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    implementation_name: str
    info: bytes
    def __init__(self, implementation_name: _Optional[str] = ..., info: _Optional[bytes] = ...) -> None: ...
