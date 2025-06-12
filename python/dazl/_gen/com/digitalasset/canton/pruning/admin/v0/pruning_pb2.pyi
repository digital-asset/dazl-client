# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetSchedule(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("schedule",)
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        schedule: PruningSchedule
        def __init__(self, schedule: _Optional[_Union[PruningSchedule, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class GetSchedule(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ("schedule",)
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        schedule: PruningSchedule
        def __init__(self, schedule: _Optional[_Union[PruningSchedule, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class SetParticipantSchedule(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("schedule",)
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        schedule: ParticipantPruningSchedule
        def __init__(self, schedule: _Optional[_Union[ParticipantPruningSchedule, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class GetParticipantSchedule(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ("schedule",)
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        schedule: ParticipantPruningSchedule
        def __init__(self, schedule: _Optional[_Union[ParticipantPruningSchedule, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PruningSchedule(_message.Message):
    __slots__ = ("cron", "max_duration", "retention")
    CRON_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    cron: str
    max_duration: _duration_pb2.Duration
    retention: _duration_pb2.Duration
    def __init__(self, cron: _Optional[str] = ..., max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., retention: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ParticipantPruningSchedule(_message.Message):
    __slots__ = ("schedule", "prune_internally_only")
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    PRUNE_INTERNALLY_ONLY_FIELD_NUMBER: _ClassVar[int]
    schedule: PruningSchedule
    prune_internally_only: bool
    def __init__(self, schedule: _Optional[_Union[PruningSchedule, _Mapping]] = ..., prune_internally_only: bool = ...) -> None: ...

class ClearSchedule(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class SetCron(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("cron",)
        CRON_FIELD_NUMBER: _ClassVar[int]
        cron: str
        def __init__(self, cron: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class SetMaxDuration(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("max_duration",)
        MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
        max_duration: _duration_pb2.Duration
        def __init__(self, max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class SetRetention(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("retention",)
        RETENTION_FIELD_NUMBER: _ClassVar[int]
        retention: _duration_pb2.Duration
        def __init__(self, retention: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class LocatePruningTimestamp(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("index",)
        INDEX_FIELD_NUMBER: _ClassVar[int]
        index: int
        def __init__(self, index: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("timestamp",)
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
