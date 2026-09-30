# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from . import acs_replication_pb2 as _acs_replication_pb2
from ....protocol.v30 import topology_pb2 as _topology_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartyReplicationStatus(_message.Message):
    __slots__ = ("parameters", "authorization", "replication", "indexing", "has_completed", "error_message", "acs_replication_status", "replication_mode")
    class ReplicationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPLICATION_MODE_UNSPECIFIED: _ClassVar[PartyReplicationStatus.ReplicationMode]
        REPLICATION_MODE_FILE: _ClassVar[PartyReplicationStatus.ReplicationMode]
        REPLICATION_MODE_SEQUENCER_CHANNEL: _ClassVar[PartyReplicationStatus.ReplicationMode]
    REPLICATION_MODE_UNSPECIFIED: PartyReplicationStatus.ReplicationMode
    REPLICATION_MODE_FILE: PartyReplicationStatus.ReplicationMode
    REPLICATION_MODE_SEQUENCER_CHANNEL: PartyReplicationStatus.ReplicationMode
    class ReplicationParameters(_message.Message):
        __slots__ = ("request_id", "party_id", "synchronizer_id", "source_participant_uid", "target_participant_uid", "topology_serial", "participant_permission")
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        PARTY_ID_FIELD_NUMBER: _ClassVar[int]
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
        request_id: str
        party_id: str
        synchronizer_id: str
        source_participant_uid: str
        target_participant_uid: str
        topology_serial: int
        participant_permission: _topology_pb2.Enums.ParticipantPermission
        def __init__(self, request_id: _Optional[str] = ..., party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., source_participant_uid: _Optional[str] = ..., target_participant_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., participant_permission: _Optional[_Union[_topology_pb2.Enums.ParticipantPermission, str]] = ...) -> None: ...
    class PartyReplicationAuthorization(_message.Message):
        __slots__ = ("onboarding_at", "is_onboarding_flag_cleared")
        ONBOARDING_AT_FIELD_NUMBER: _ClassVar[int]
        IS_ONBOARDING_FLAG_CLEARED_FIELD_NUMBER: _ClassVar[int]
        onboarding_at: _timestamp_pb2.Timestamp
        is_onboarding_flag_cleared: bool
        def __init__(self, onboarding_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_onboarding_flag_cleared: _Optional[bool] = ...) -> None: ...
    class AcsIndexingProgress(_message.Message):
        __slots__ = ("indexed_contract_activation_change_count", "next_indexing_counter", "indexing_almost_done_watermark")
        INDEXED_CONTRACT_ACTIVATION_CHANGE_COUNT_FIELD_NUMBER: _ClassVar[int]
        NEXT_INDEXING_COUNTER_FIELD_NUMBER: _ClassVar[int]
        INDEXING_ALMOST_DONE_WATERMARK_FIELD_NUMBER: _ClassVar[int]
        indexed_contract_activation_change_count: int
        next_indexing_counter: int
        indexing_almost_done_watermark: int
        def __init__(self, indexed_contract_activation_change_count: _Optional[int] = ..., next_indexing_counter: _Optional[int] = ..., indexing_almost_done_watermark: _Optional[int] = ...) -> None: ...
    class PartyReplicationError(_message.Message):
        __slots__ = ("error_type", "error_message")
        class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ERROR_TYPE_UNSPECIFIED: _ClassVar[PartyReplicationStatus.PartyReplicationError.ErrorType]
            ERROR_TYPE_FAILED: _ClassVar[PartyReplicationStatus.PartyReplicationError.ErrorType]
            ERROR_TYPE_DISCONNECTED: _ClassVar[PartyReplicationStatus.PartyReplicationError.ErrorType]
        ERROR_TYPE_UNSPECIFIED: PartyReplicationStatus.PartyReplicationError.ErrorType
        ERROR_TYPE_FAILED: PartyReplicationStatus.PartyReplicationError.ErrorType
        ERROR_TYPE_DISCONNECTED: PartyReplicationStatus.PartyReplicationError.ErrorType
        ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_type: PartyReplicationStatus.PartyReplicationError.ErrorType
        error_message: str
        def __init__(self, error_type: _Optional[_Union[PartyReplicationStatus.PartyReplicationError.ErrorType, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    INDEXING_FIELD_NUMBER: _ClassVar[int]
    HAS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACS_REPLICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    parameters: PartyReplicationStatus.ReplicationParameters
    authorization: PartyReplicationStatus.PartyReplicationAuthorization
    replication: _acs_replication_pb2.AcsReplicationStatus.AcsReplicationProgress
    indexing: PartyReplicationStatus.AcsIndexingProgress
    has_completed: bool
    error_message: PartyReplicationStatus.PartyReplicationError
    acs_replication_status: _acs_replication_pb2.AcsReplicationStatus
    replication_mode: PartyReplicationStatus.ReplicationMode
    def __init__(self, parameters: _Optional[_Union[PartyReplicationStatus.ReplicationParameters, _Mapping]] = ..., authorization: _Optional[_Union[PartyReplicationStatus.PartyReplicationAuthorization, _Mapping]] = ..., replication: _Optional[_Union[_acs_replication_pb2.AcsReplicationStatus.AcsReplicationProgress, _Mapping]] = ..., indexing: _Optional[_Union[PartyReplicationStatus.AcsIndexingProgress, _Mapping]] = ..., has_completed: _Optional[bool] = ..., error_message: _Optional[_Union[PartyReplicationStatus.PartyReplicationError, _Mapping]] = ..., acs_replication_status: _Optional[_Union[_acs_replication_pb2.AcsReplicationStatus, _Mapping]] = ..., replication_mode: _Optional[_Union[PartyReplicationStatus.ReplicationMode, str]] = ...) -> None: ...
