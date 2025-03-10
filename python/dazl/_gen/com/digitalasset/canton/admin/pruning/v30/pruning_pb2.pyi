# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SharedContractsState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[SharedContractsState]
    SHARED_CONTRACTS: _ClassVar[SharedContractsState]
    NO_SHARED_CONTRACTS: _ClassVar[SharedContractsState]
STATE_UNSPECIFIED: SharedContractsState
SHARED_CONTRACTS: SharedContractsState
NO_SHARED_CONTRACTS: SharedContractsState

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

class SetNoWaitCommitmentsFrom(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("counter_participant_uids", "sequencing_timestamp", "pruning_offset", "domain_ids")
        COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
        SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        PRUNING_OFFSET_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
        counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
        sequencing_timestamp: _timestamp_pb2.Timestamp
        pruning_offset: str
        domain_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, counter_participant_uids: _Optional[_Iterable[str]] = ..., sequencing_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pruning_offset: _Optional[str] = ..., domain_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("participant_domains_mapping",)
        class ParticipantDomainsMappingEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Domains
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Domains, _Mapping]] = ...) -> None: ...
        PARTICIPANT_DOMAINS_MAPPING_FIELD_NUMBER: _ClassVar[int]
        participant_domains_mapping: _containers.MessageMap[str, Domains]
        def __init__(self, participant_domains_mapping: _Optional[_Mapping[str, Domains]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ResetNoWaitCommitmentsFrom(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("counter_participant_uids", "domain_ids")
        COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
        counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
        domain_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, counter_participant_uids: _Optional[_Iterable[str]] = ..., domain_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("participant_domains_mapping",)
        class ParticipantDomainsMappingEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Domains
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Domains, _Mapping]] = ...) -> None: ...
        PARTICIPANT_DOMAINS_MAPPING_FIELD_NUMBER: _ClassVar[int]
        participant_domains_mapping: _containers.MessageMap[str, Domains]
        def __init__(self, participant_domains_mapping: _Optional[_Mapping[str, Domains]] = ...) -> None: ...
    def __init__(self) -> None: ...

class Domains(_message.Message):
    __slots__ = ("domain_ids",)
    DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
    domain_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNoWaitCommitmentsFrom(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("domain_ids", "participant_uids")
        DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
        domain_ids: _containers.RepeatedScalarFieldContainer[str]
        participant_uids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, domain_ids: _Optional[_Iterable[str]] = ..., participant_uids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("ignored_participants", "not_ignored_participants")
        IGNORED_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
        NOT_IGNORED_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
        ignored_participants: _containers.RepeatedCompositeFieldContainer[NoWaitCommitmentsSetup]
        not_ignored_participants: _containers.RepeatedCompositeFieldContainer[WaitCommitmentsSetup]
        def __init__(self, ignored_participants: _Optional[_Iterable[_Union[NoWaitCommitmentsSetup, _Mapping]]] = ..., not_ignored_participants: _Optional[_Iterable[_Union[WaitCommitmentsSetup, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class NoWaitCommitmentsSetup(_message.Message):
    __slots__ = ("counter_participant_uid", "sequencing_timestamp", "pruning_offset", "domain_ids", "counter_participant_state")
    COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PRUNING_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
    COUNTER_PARTICIPANT_STATE_FIELD_NUMBER: _ClassVar[int]
    counter_participant_uid: str
    sequencing_timestamp: _timestamp_pb2.Timestamp
    pruning_offset: str
    domain_ids: Domains
    counter_participant_state: SharedContractsState
    def __init__(self, counter_participant_uid: _Optional[str] = ..., sequencing_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pruning_offset: _Optional[str] = ..., domain_ids: _Optional[_Union[Domains, _Mapping]] = ..., counter_participant_state: _Optional[_Union[SharedContractsState, str]] = ...) -> None: ...

class WaitCommitmentsSetup(_message.Message):
    __slots__ = ("counter_participant_uid", "domain_ids", "counter_participant_state")
    COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
    COUNTER_PARTICIPANT_STATE_FIELD_NUMBER: _ClassVar[int]
    counter_participant_uid: str
    domain_ids: Domains
    counter_participant_state: SharedContractsState
    def __init__(self, counter_participant_uid: _Optional[str] = ..., domain_ids: _Optional[_Union[Domains, _Mapping]] = ..., counter_participant_state: _Optional[_Union[SharedContractsState, str]] = ...) -> None: ...
