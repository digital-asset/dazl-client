# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeProofRequestConfig(_message.Message):
    __slots__ = ("initial_retry_delay", "max_retry_delay", "max_sequencing_delay")
    INITIAL_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQUENCING_DELAY_FIELD_NUMBER: _ClassVar[int]
    initial_retry_delay: _duration_pb2.Duration
    max_retry_delay: _duration_pb2.Duration
    max_sequencing_delay: _duration_pb2.Duration
    def __init__(self, initial_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_sequencing_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SynchronizerTimeTrackerConfig(_message.Message):
    __slots__ = ("observation_latency", "patience_duration", "min_observation_duration", "time_proof_request")
    OBSERVATION_LATENCY_FIELD_NUMBER: _ClassVar[int]
    PATIENCE_DURATION_FIELD_NUMBER: _ClassVar[int]
    MIN_OBSERVATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    TIME_PROOF_REQUEST_FIELD_NUMBER: _ClassVar[int]
    observation_latency: _duration_pb2.Duration
    patience_duration: _duration_pb2.Duration
    min_observation_duration: _duration_pb2.Duration
    time_proof_request: TimeProofRequestConfig
    def __init__(self, observation_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., patience_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., min_observation_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., time_proof_request: _Optional[_Union[TimeProofRequestConfig, _Mapping]] = ...) -> None: ...
