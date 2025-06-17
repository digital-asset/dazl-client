# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetScheduleRequest(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: PruningSchedule
    def __init__(self, schedule: _Optional[_Union[PruningSchedule, _Mapping]] = ...) -> None: ...

class SetScheduleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetScheduleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: PruningSchedule
    def __init__(self, schedule: _Optional[_Union[PruningSchedule, _Mapping]] = ...) -> None: ...

class SetParticipantScheduleRequest(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: ParticipantPruningSchedule
    def __init__(self, schedule: _Optional[_Union[ParticipantPruningSchedule, _Mapping]] = ...) -> None: ...

class SetParticipantScheduleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetParticipantScheduleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetParticipantScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: ParticipantPruningSchedule
    def __init__(self, schedule: _Optional[_Union[ParticipantPruningSchedule, _Mapping]] = ...) -> None: ...

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

class ClearScheduleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearScheduleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetCronRequest(_message.Message):
    __slots__ = ("cron",)
    CRON_FIELD_NUMBER: _ClassVar[int]
    cron: str
    def __init__(self, cron: _Optional[str] = ...) -> None: ...

class SetCronResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetMaxDurationRequest(_message.Message):
    __slots__ = ("max_duration",)
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    max_duration: _duration_pb2.Duration
    def __init__(self, max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SetMaxDurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetRetentionRequest(_message.Message):
    __slots__ = ("retention",)
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    retention: _duration_pb2.Duration
    def __init__(self, retention: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SetRetentionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocatePruningTimestampRequest(_message.Message):
    __slots__ = ("index",)
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: int
    def __init__(self, index: _Optional[int] = ...) -> None: ...

class LocatePruningTimestampResponse(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SetNoWaitCommitmentsFromRequest(_message.Message):
    __slots__ = ("counter_participant_uids", "synchronizer_ids")
    COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, counter_participant_uids: _Optional[_Iterable[str]] = ..., synchronizer_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class SetNoWaitCommitmentsFromResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetNoWaitCommitmentsFromRequest(_message.Message):
    __slots__ = ("counter_participant_uids", "synchronizer_ids")
    COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, counter_participant_uids: _Optional[_Iterable[str]] = ..., synchronizer_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ResetNoWaitCommitmentsFromResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Synchronizers(_message.Message):
    __slots__ = ("synchronizer_ids",)
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, synchronizer_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNoWaitCommitmentsFromRequest(_message.Message):
    __slots__ = ("synchronizer_ids", "participant_uids")
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    participant_uids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, synchronizer_ids: _Optional[_Iterable[str]] = ..., participant_uids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNoWaitCommitmentsFromResponse(_message.Message):
    __slots__ = ("ignored_participants", "not_ignored_participants")
    IGNORED_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    NOT_IGNORED_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    ignored_participants: _containers.RepeatedCompositeFieldContainer[WaitCommitmentsSetup]
    not_ignored_participants: _containers.RepeatedCompositeFieldContainer[WaitCommitmentsSetup]
    def __init__(self, ignored_participants: _Optional[_Iterable[_Union[WaitCommitmentsSetup, _Mapping]]] = ..., not_ignored_participants: _Optional[_Iterable[_Union[WaitCommitmentsSetup, _Mapping]]] = ...) -> None: ...

class WaitCommitmentsSetup(_message.Message):
    __slots__ = ("counter_participant_uid", "synchronizers")
    COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZERS_FIELD_NUMBER: _ClassVar[int]
    counter_participant_uid: str
    synchronizers: Synchronizers
    def __init__(self, counter_participant_uid: _Optional[str] = ..., synchronizers: _Optional[_Union[Synchronizers, _Mapping]] = ...) -> None: ...
