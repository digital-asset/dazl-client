# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DynamicSequencingParametersPayload(_message.Message):
    __slots__ = ("pbft_view_change_timeout", "segment_length", "blacklist_leader_selection_policy", "max_requests_in_batch", "max_batches_per_proposal", "pbft_view_change_timeout_step", "pbft_view_change_timeout_upper_bound", "stricter_detection_of_requests_potentially_changing_ordering_topology")
    PBFT_VIEW_CHANGE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    BLACKLIST_LEADER_SELECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUESTS_IN_BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCHES_PER_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    PBFT_VIEW_CHANGE_TIMEOUT_STEP_FIELD_NUMBER: _ClassVar[int]
    PBFT_VIEW_CHANGE_TIMEOUT_UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    STRICTER_DETECTION_OF_REQUESTS_POTENTIALLY_CHANGING_ORDERING_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    pbft_view_change_timeout: _duration_pb2.Duration
    segment_length: int
    blacklist_leader_selection_policy: BlacklistLeaderSelectionPolicy
    max_requests_in_batch: int
    max_batches_per_proposal: int
    pbft_view_change_timeout_step: _duration_pb2.Duration
    pbft_view_change_timeout_upper_bound: _duration_pb2.Duration
    stricter_detection_of_requests_potentially_changing_ordering_topology: bool
    def __init__(self, pbft_view_change_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., segment_length: _Optional[int] = ..., blacklist_leader_selection_policy: _Optional[_Union[BlacklistLeaderSelectionPolicy, _Mapping]] = ..., max_requests_in_batch: _Optional[int] = ..., max_batches_per_proposal: _Optional[int] = ..., pbft_view_change_timeout_step: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., pbft_view_change_timeout_upper_bound: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., stricter_detection_of_requests_potentially_changing_ordering_topology: _Optional[bool] = ...) -> None: ...

class BlacklistLeaderSelectionPolicy(_message.Message):
    __slots__ = ("how_long_linear", "how_long_no_blacklisting", "how_long_linear_with_parameters", "how_long_exponential", "how_many_num_faults_tolerated", "how_many_no_blacklisting")
    HOW_LONG_LINEAR_FIELD_NUMBER: _ClassVar[int]
    HOW_LONG_NO_BLACKLISTING_FIELD_NUMBER: _ClassVar[int]
    HOW_LONG_LINEAR_WITH_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    HOW_LONG_EXPONENTIAL_FIELD_NUMBER: _ClassVar[int]
    HOW_MANY_NUM_FAULTS_TOLERATED_FIELD_NUMBER: _ClassVar[int]
    HOW_MANY_NO_BLACKLISTING_FIELD_NUMBER: _ClassVar[int]
    how_long_linear: HowLongLinear
    how_long_no_blacklisting: HowLongNoBlacklisting
    how_long_linear_with_parameters: HowLongLinearWithParameters
    how_long_exponential: HowLongExponential
    how_many_num_faults_tolerated: HowManyNumFaultsTolerated
    how_many_no_blacklisting: HowManyNoBlacklisting
    def __init__(self, how_long_linear: _Optional[_Union[HowLongLinear, _Mapping]] = ..., how_long_no_blacklisting: _Optional[_Union[HowLongNoBlacklisting, _Mapping]] = ..., how_long_linear_with_parameters: _Optional[_Union[HowLongLinearWithParameters, _Mapping]] = ..., how_long_exponential: _Optional[_Union[HowLongExponential, _Mapping]] = ..., how_many_num_faults_tolerated: _Optional[_Union[HowManyNumFaultsTolerated, _Mapping]] = ..., how_many_no_blacklisting: _Optional[_Union[HowManyNoBlacklisting, _Mapping]] = ...) -> None: ...

class HowLongLinear(_message.Message):
    __slots__ = ("maximum_epoch_length_blacklisted",)
    MAXIMUM_EPOCH_LENGTH_BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    maximum_epoch_length_blacklisted: int
    def __init__(self, maximum_epoch_length_blacklisted: _Optional[int] = ...) -> None: ...

class HowLongNoBlacklisting(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HowLongLinearWithParameters(_message.Message):
    __slots__ = ("slope", "initial_value", "maximum_epoch_length_blacklisted")
    SLOPE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_EPOCH_LENGTH_BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    slope: int
    initial_value: int
    maximum_epoch_length_blacklisted: int
    def __init__(self, slope: _Optional[int] = ..., initial_value: _Optional[int] = ..., maximum_epoch_length_blacklisted: _Optional[int] = ...) -> None: ...

class HowLongExponential(_message.Message):
    __slots__ = ("initial_value", "maximum_epoch_length_blacklisted")
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_EPOCH_LENGTH_BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    initial_value: int
    maximum_epoch_length_blacklisted: int
    def __init__(self, initial_value: _Optional[int] = ..., maximum_epoch_length_blacklisted: _Optional[int] = ...) -> None: ...

class HowManyNumFaultsTolerated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HowManyNoBlacklisting(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
