# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from .. import crypto_pb2 as _crypto_pb2
from .. import state_service_pb2 as _state_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratePartyTopologyUpdateRequest(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "target_participant_uid", "participant_permission")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    target_participant_uid: str
    participant_permission: _state_service_pb2.ParticipantPermission
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., target_participant_uid: _Optional[str] = ..., participant_permission: _Optional[_Union[_state_service_pb2.ParticipantPermission, str]] = ...) -> None: ...

class GeneratePartyTopologyUpdateResponse(_message.Message):
    __slots__ = ("transaction", "hash")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    transaction: bytes
    hash: bytes
    def __init__(self, transaction: _Optional[bytes] = ..., hash: _Optional[bytes] = ...) -> None: ...

class AuthorizePartyUpdateRequest(_message.Message):
    __slots__ = ("synchronizer_id", "transaction", "signatures", "user_id", "identity_provider_id")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    transaction: bytes
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    user_id: str
    identity_provider_id: str
    def __init__(self, synchronizer_id: _Optional[str] = ..., transaction: _Optional[bytes] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., user_id: _Optional[str] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class AuthorizePartyUpdateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAddPartyStatusRequest(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "target_participant_uid")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    target_participant_uid: str
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., target_participant_uid: _Optional[str] = ...) -> None: ...

class GetAddPartyStatusResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: PartyReplicationStatus
    def __init__(self, status: _Optional[_Union[PartyReplicationStatus, _Mapping]] = ...) -> None: ...

class PartyReplicationStatus(_message.Message):
    __slots__ = ("current", "error")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PartyReplicationStatus.State]
        STATE_IN_PROGRESS: _ClassVar[PartyReplicationStatus.State]
        STATE_COMPLETED: _ClassVar[PartyReplicationStatus.State]
        STATE_FAILED: _ClassVar[PartyReplicationStatus.State]
    STATE_UNSPECIFIED: PartyReplicationStatus.State
    STATE_IN_PROGRESS: PartyReplicationStatus.State
    STATE_COMPLETED: PartyReplicationStatus.State
    STATE_FAILED: PartyReplicationStatus.State
    class ErrorDetails(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    current: PartyReplicationStatus.State
    error: PartyReplicationStatus.ErrorDetails
    def __init__(self, current: _Optional[_Union[PartyReplicationStatus.State, str]] = ..., error: _Optional[_Union[PartyReplicationStatus.ErrorDetails, _Mapping]] = ...) -> None: ...
