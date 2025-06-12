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

class CatchUpConfig(_message.Message):
    __slots__ = ("catchup_interval_skip", "nr_intervals_to_trigger_catchup")
    CATCHUP_INTERVAL_SKIP_FIELD_NUMBER: _ClassVar[int]
    NR_INTERVALS_TO_TRIGGER_CATCHUP_FIELD_NUMBER: _ClassVar[int]
    catchup_interval_skip: int
    nr_intervals_to_trigger_catchup: int
    def __init__(self, catchup_interval_skip: _Optional[int] = ..., nr_intervals_to_trigger_catchup: _Optional[int] = ...) -> None: ...

class DynamicDomainParameters(_message.Message):
    __slots__ = ("participant_response_timeout", "mediator_reaction_timeout", "transfer_exclusivity_timeout", "topology_change_delay", "ledger_time_record_time_tolerance", "reconciliation_interval", "mediator_deduplication_timeout", "max_rate_per_participant", "max_request_size", "catch_up_parameters")
    PARTICIPANT_RESPONSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REACTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_EXCLUSIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_CHANGE_DELAY_FIELD_NUMBER: _ClassVar[int]
    LEDGER_TIME_RECORD_TIME_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_DEDUPLICATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_RATE_PER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUEST_SIZE_FIELD_NUMBER: _ClassVar[int]
    CATCH_UP_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    participant_response_timeout: _duration_pb2.Duration
    mediator_reaction_timeout: _duration_pb2.Duration
    transfer_exclusivity_timeout: _duration_pb2.Duration
    topology_change_delay: _duration_pb2.Duration
    ledger_time_record_time_tolerance: _duration_pb2.Duration
    reconciliation_interval: _duration_pb2.Duration
    mediator_deduplication_timeout: _duration_pb2.Duration
    max_rate_per_participant: int
    max_request_size: int
    catch_up_parameters: CatchUpConfig
    def __init__(self, participant_response_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mediator_reaction_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., transfer_exclusivity_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., topology_change_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ledger_time_record_time_tolerance: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., reconciliation_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mediator_deduplication_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_rate_per_participant: _Optional[int] = ..., max_request_size: _Optional[int] = ..., catch_up_parameters: _Optional[_Union[CatchUpConfig, _Mapping]] = ...) -> None: ...
