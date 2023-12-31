# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeProofRequestConfig(_message.Message):
    __slots__ = ["initialRetryDelay", "maxRetryDelay", "maxSequencingDelay"]
    INITIALRETRYDELAY_FIELD_NUMBER: _ClassVar[int]
    MAXRETRYDELAY_FIELD_NUMBER: _ClassVar[int]
    MAXSEQUENCINGDELAY_FIELD_NUMBER: _ClassVar[int]
    initialRetryDelay: _duration_pb2.Duration
    maxRetryDelay: _duration_pb2.Duration
    maxSequencingDelay: _duration_pb2.Duration
    def __init__(self, initialRetryDelay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., maxRetryDelay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., maxSequencingDelay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class DomainTimeTrackerConfig(_message.Message):
    __slots__ = ["observationLatency", "patienceDuration", "minObservationDuration", "timeProofRequest"]
    OBSERVATIONLATENCY_FIELD_NUMBER: _ClassVar[int]
    PATIENCEDURATION_FIELD_NUMBER: _ClassVar[int]
    MINOBSERVATIONDURATION_FIELD_NUMBER: _ClassVar[int]
    TIMEPROOFREQUEST_FIELD_NUMBER: _ClassVar[int]
    observationLatency: _duration_pb2.Duration
    patienceDuration: _duration_pb2.Duration
    minObservationDuration: _duration_pb2.Duration
    timeProofRequest: TimeProofRequestConfig
    def __init__(self, observationLatency: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., patienceDuration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., minObservationDuration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., timeProofRequest: _Optional[_Union[TimeProofRequestConfig, _Mapping]] = ...) -> None: ...
