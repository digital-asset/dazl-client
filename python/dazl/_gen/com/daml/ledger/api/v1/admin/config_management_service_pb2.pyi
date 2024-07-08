# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTimeModelRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetTimeModelResponse(_message.Message):
    __slots__ = ["configuration_generation", "time_model"]
    CONFIGURATION_GENERATION_FIELD_NUMBER: _ClassVar[int]
    TIME_MODEL_FIELD_NUMBER: _ClassVar[int]
    configuration_generation: int
    time_model: TimeModel
    def __init__(self, configuration_generation: _Optional[int] = ..., time_model: _Optional[_Union[TimeModel, _Mapping]] = ...) -> None: ...

class SetTimeModelRequest(_message.Message):
    __slots__ = ["submission_id", "maximum_record_time", "configuration_generation", "new_time_model"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_GENERATION_FIELD_NUMBER: _ClassVar[int]
    NEW_TIME_MODEL_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    maximum_record_time: _timestamp_pb2.Timestamp
    configuration_generation: int
    new_time_model: TimeModel
    def __init__(self, submission_id: _Optional[str] = ..., maximum_record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., configuration_generation: _Optional[int] = ..., new_time_model: _Optional[_Union[TimeModel, _Mapping]] = ...) -> None: ...

class SetTimeModelResponse(_message.Message):
    __slots__ = ["configuration_generation"]
    CONFIGURATION_GENERATION_FIELD_NUMBER: _ClassVar[int]
    configuration_generation: int
    def __init__(self, configuration_generation: _Optional[int] = ...) -> None: ...

class TimeModel(_message.Message):
    __slots__ = ["avg_transaction_latency", "min_skew", "max_skew"]
    AVG_TRANSACTION_LATENCY_FIELD_NUMBER: _ClassVar[int]
    MIN_SKEW_FIELD_NUMBER: _ClassVar[int]
    MAX_SKEW_FIELD_NUMBER: _ClassVar[int]
    avg_transaction_latency: _duration_pb2.Duration
    min_skew: _duration_pb2.Duration
    max_skew: _duration_pb2.Duration
    def __init__(self, avg_transaction_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., min_skew: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_skew: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
