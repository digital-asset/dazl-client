# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ....admin.pruning.v30 import pruning_pb2 as _pruning_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BftPruneRequest(_message.Message):
    __slots__ = ("retention", "min_blocks_to_keep")
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    MIN_BLOCKS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    retention: _duration_pb2.Duration
    min_blocks_to_keep: int
    def __init__(self, retention: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., min_blocks_to_keep: _Optional[int] = ...) -> None: ...

class BftPruneResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class BftPruningStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BftPruningStatusResponse(_message.Message):
    __slots__ = ("latest_block_epoch", "latest_block", "latest_block_timestamp", "lower_bound_epoch", "lower_bound_block")
    LATEST_BLOCK_EPOCH_FIELD_NUMBER: _ClassVar[int]
    LATEST_BLOCK_FIELD_NUMBER: _ClassVar[int]
    LATEST_BLOCK_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_EPOCH_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_BLOCK_FIELD_NUMBER: _ClassVar[int]
    latest_block_epoch: int
    latest_block: int
    latest_block_timestamp: _timestamp_pb2.Timestamp
    lower_bound_epoch: int
    lower_bound_block: int
    def __init__(self, latest_block_epoch: _Optional[int] = ..., latest_block: _Optional[int] = ..., latest_block_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., lower_bound_epoch: _Optional[int] = ..., lower_bound_block: _Optional[int] = ...) -> None: ...

class SetBftScheduleRequest(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: BftOrdererPruningSchedule
    def __init__(self, schedule: _Optional[_Union[BftOrdererPruningSchedule, _Mapping]] = ...) -> None: ...

class BftOrdererPruningSchedule(_message.Message):
    __slots__ = ("schedule", "min_blocks_to_keep")
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MIN_BLOCKS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    schedule: _pruning_pb2.PruningSchedule
    min_blocks_to_keep: int
    def __init__(self, schedule: _Optional[_Union[_pruning_pb2.PruningSchedule, _Mapping]] = ..., min_blocks_to_keep: _Optional[int] = ...) -> None: ...

class SetBftScheduleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBftScheduleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBftScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: BftOrdererPruningSchedule
    def __init__(self, schedule: _Optional[_Union[BftOrdererPruningSchedule, _Mapping]] = ...) -> None: ...

class SetMinBlocksToKeepRequest(_message.Message):
    __slots__ = ("min_blocks_to_keep",)
    MIN_BLOCKS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    min_blocks_to_keep: int
    def __init__(self, min_blocks_to_keep: _Optional[int] = ...) -> None: ...

class SetMinBlocksToKeepResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
