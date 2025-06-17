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
        __slots__ = ("timestamp", "start_epoch_number", "first_block_number_in_start_epoch", "start_epoch_topology_query_timestamp", "start_epoch_could_alter_ordering_topology", "previous_bft_time", "previous_epoch_topology_query_timestamp")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        START_EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
        FIRST_BLOCK_NUMBER_IN_START_EPOCH_FIELD_NUMBER: _ClassVar[int]
        START_EPOCH_TOPOLOGY_QUERY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        START_EPOCH_COULD_ALTER_ORDERING_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_BFT_TIME_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_EPOCH_TOPOLOGY_QUERY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        start_epoch_number: int
        first_block_number_in_start_epoch: int
        start_epoch_topology_query_timestamp: int
        start_epoch_could_alter_ordering_topology: bool
        previous_bft_time: int
        previous_epoch_topology_query_timestamp: int
        def __init__(self, timestamp: _Optional[int] = ..., start_epoch_number: _Optional[int] = ..., first_block_number_in_start_epoch: _Optional[int] = ..., start_epoch_topology_query_timestamp: _Optional[int] = ..., start_epoch_could_alter_ordering_topology: bool = ..., previous_bft_time: _Optional[int] = ..., previous_epoch_topology_query_timestamp: _Optional[int] = ...) -> None: ...
    SEQUENCERS_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    sequencers_active_at: _containers.MessageMap[str, BftSequencerSnapshotAdditionalInfo.SequencerActiveAt]
    def __init__(self, sequencers_active_at: _Optional[_Mapping[str, BftSequencerSnapshotAdditionalInfo.SequencerActiveAt]] = ...) -> None: ...
