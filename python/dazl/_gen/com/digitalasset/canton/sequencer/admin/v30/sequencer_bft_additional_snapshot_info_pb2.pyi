# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BftSequencerSnapshotAdditionalInfo(_message.Message):
    __slots__ = ("sequencers_active_at",)
    class SequencersActiveAtEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BftSequencerSnapshotAdditionalInfo.SequencerActiveAt
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BftSequencerSnapshotAdditionalInfo.SequencerActiveAt, _Mapping]] = ...) -> None: ...
    class SequencerActiveAt(_message.Message):
        __slots__ = ("timestamp", "start_epoch_number", "first_block_number_in_start_epoch", "start_epoch_topology_query_timestamp", "start_epoch_could_alter_ordering_topology", "previous_bft_time", "previous_epoch_topology_query_timestamp", "leader_selection_policy_state")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        START_EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
        FIRST_BLOCK_NUMBER_IN_START_EPOCH_FIELD_NUMBER: _ClassVar[int]
        START_EPOCH_TOPOLOGY_QUERY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        START_EPOCH_COULD_ALTER_ORDERING_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_BFT_TIME_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_EPOCH_TOPOLOGY_QUERY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        LEADER_SELECTION_POLICY_STATE_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        start_epoch_number: int
        first_block_number_in_start_epoch: int
        start_epoch_topology_query_timestamp: int
        start_epoch_could_alter_ordering_topology: bool
        previous_bft_time: int
        previous_epoch_topology_query_timestamp: int
        leader_selection_policy_state: bytes
        def __init__(self, timestamp: _Optional[int] = ..., start_epoch_number: _Optional[int] = ..., first_block_number_in_start_epoch: _Optional[int] = ..., start_epoch_topology_query_timestamp: _Optional[int] = ..., start_epoch_could_alter_ordering_topology: bool = ..., previous_bft_time: _Optional[int] = ..., previous_epoch_topology_query_timestamp: _Optional[int] = ..., leader_selection_policy_state: _Optional[bytes] = ...) -> None: ...
    SEQUENCERS_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    sequencers_active_at: _containers.MessageMap[str, BftSequencerSnapshotAdditionalInfo.SequencerActiveAt]
    def __init__(self, sequencers_active_at: _Optional[_Mapping[str, BftSequencerSnapshotAdditionalInfo.SequencerActiveAt]] = ...) -> None: ...

class BlacklistLeaderSelectionPolicyState(_message.Message):
    __slots__ = ("epoch_number", "start_block_number", "blacklist")
    class BlacklistEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BlacklistLeaderSelectionPolicyState.BlacklistStatus
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BlacklistLeaderSelectionPolicyState.BlacklistStatus, _Mapping]] = ...) -> None: ...
    class BlacklistStatus(_message.Message):
        __slots__ = ("on_trial", "blacklisted")
        class OnTrial(_message.Message):
            __slots__ = ("failed_attempts_before_trial",)
            FAILED_ATTEMPTS_BEFORE_TRIAL_FIELD_NUMBER: _ClassVar[int]
            failed_attempts_before_trial: int
            def __init__(self, failed_attempts_before_trial: _Optional[int] = ...) -> None: ...
        class Blacklisted(_message.Message):
            __slots__ = ("failed_attempts_before", "epochs_left_until_new_trial")
            FAILED_ATTEMPTS_BEFORE_FIELD_NUMBER: _ClassVar[int]
            EPOCHS_LEFT_UNTIL_NEW_TRIAL_FIELD_NUMBER: _ClassVar[int]
            failed_attempts_before: int
            epochs_left_until_new_trial: int
            def __init__(self, failed_attempts_before: _Optional[int] = ..., epochs_left_until_new_trial: _Optional[int] = ...) -> None: ...
        ON_TRIAL_FIELD_NUMBER: _ClassVar[int]
        BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
        on_trial: BlacklistLeaderSelectionPolicyState.BlacklistStatus.OnTrial
        blacklisted: BlacklistLeaderSelectionPolicyState.BlacklistStatus.Blacklisted
        def __init__(self, on_trial: _Optional[_Union[BlacklistLeaderSelectionPolicyState.BlacklistStatus.OnTrial, _Mapping]] = ..., blacklisted: _Optional[_Union[BlacklistLeaderSelectionPolicyState.BlacklistStatus.Blacklisted, _Mapping]] = ...) -> None: ...
    EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    START_BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BLACKLIST_FIELD_NUMBER: _ClassVar[int]
    epoch_number: int
    start_block_number: int
    blacklist: _containers.MessageMap[str, BlacklistLeaderSelectionPolicyState.BlacklistStatus]
    def __init__(self, epoch_number: _Optional[int] = ..., start_block_number: _Optional[int] = ..., blacklist: _Optional[_Mapping[str, BlacklistLeaderSelectionPolicyState.BlacklistStatus]] = ...) -> None: ...
