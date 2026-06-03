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
    __slots__ = ("pbft_view_change_timeout", "segment_length", "blacklist_leader_selection_policy")
    PBFT_VIEW_CHANGE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    BLACKLIST_LEADER_SELECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    pbft_view_change_timeout: _duration_pb2.Duration
    segment_length: int
    blacklist_leader_selection_policy: BlacklistLeaderSelectionPolicy
    def __init__(self, pbft_view_change_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., segment_length: _Optional[int] = ..., blacklist_leader_selection_policy: _Optional[_Union[BlacklistLeaderSelectionPolicy, _Mapping]] = ...) -> None: ...

class BlacklistLeaderSelectionPolicy(_message.Message):
    __slots__ = ("how_long_linear", "how_long_no_blacklisting", "how_many_num_faults_tolerated", "how_many_no_blacklisting")
    HOW_LONG_LINEAR_FIELD_NUMBER: _ClassVar[int]
    HOW_LONG_NO_BLACKLISTING_FIELD_NUMBER: _ClassVar[int]
    HOW_MANY_NUM_FAULTS_TOLERATED_FIELD_NUMBER: _ClassVar[int]
    HOW_MANY_NO_BLACKLISTING_FIELD_NUMBER: _ClassVar[int]
    how_long_linear: HowLongLinear
    how_long_no_blacklisting: HowLongNoBlacklisting
    how_many_num_faults_tolerated: HowManyNumFaultsTolerated
    how_many_no_blacklisting: HowManyNoBlacklisting
    def __init__(self, how_long_linear: _Optional[_Union[HowLongLinear, _Mapping]] = ..., how_long_no_blacklisting: _Optional[_Union[HowLongNoBlacklisting, _Mapping]] = ..., how_many_num_faults_tolerated: _Optional[_Union[HowManyNumFaultsTolerated, _Mapping]] = ..., how_many_no_blacklisting: _Optional[_Union[HowManyNoBlacklisting, _Mapping]] = ...) -> None: ...

class HowLongLinear(_message.Message):
    __slots__ = ("maximum_epoch_length_blacklisted",)
    MAXIMUM_EPOCH_LENGTH_BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    maximum_epoch_length_blacklisted: int
    def __init__(self, maximum_epoch_length_blacklisted: _Optional[int] = ...) -> None: ...

class HowLongNoBlacklisting(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HowManyNumFaultsTolerated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HowManyNoBlacklisting(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
