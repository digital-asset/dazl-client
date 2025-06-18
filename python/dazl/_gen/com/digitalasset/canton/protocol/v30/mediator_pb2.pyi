# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import common_pb2 as _common_pb2
from . import confirmation_response_pb2 as _confirmation_response_pb2
from . import merkle_pb2 as _merkle_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InformeeTree(_message.Message):
    __slots__ = ("tree",)
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ...) -> None: ...

class ParticipantReject(_message.Message):
    __slots__ = ("reasons",)
    REASONS_FIELD_NUMBER: _ClassVar[int]
    reasons: _containers.RepeatedCompositeFieldContainer[RejectionReason]
    def __init__(self, reasons: _Optional[_Iterable[_Union[RejectionReason, _Mapping]]] = ...) -> None: ...

class RejectionReason(_message.Message):
    __slots__ = ("parties", "reject")
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    REJECT_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    reject: _confirmation_response_pb2.LocalVerdict
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., reject: _Optional[_Union[_confirmation_response_pb2.LocalVerdict, _Mapping]] = ...) -> None: ...

class MediatorReject(_message.Message):
    __slots__ = ("reason", "is_malformed")
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_MALFORMED_FIELD_NUMBER: _ClassVar[int]
    reason: _status_pb2.Status
    is_malformed: bool
    def __init__(self, reason: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., is_malformed: bool = ...) -> None: ...

class Verdict(_message.Message):
    __slots__ = ("approve", "participant_reject", "mediator_reject")
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_REJECT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REJECT_FIELD_NUMBER: _ClassVar[int]
    approve: _empty_pb2.Empty
    participant_reject: ParticipantReject
    mediator_reject: MediatorReject
    def __init__(self, approve: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., participant_reject: _Optional[_Union[ParticipantReject, _Mapping]] = ..., mediator_reject: _Optional[_Union[MediatorReject, _Mapping]] = ...) -> None: ...

class ConfirmationResultMessage(_message.Message):
    __slots__ = ("synchronizer_id", "view_type", "request_id", "root_hash", "verdict")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    view_type: _common_pb2.ViewType
    request_id: int
    root_hash: bytes
    verdict: Verdict
    def __init__(self, synchronizer_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ..., request_id: _Optional[int] = ..., root_hash: _Optional[bytes] = ..., verdict: _Optional[_Union[Verdict, _Mapping]] = ...) -> None: ...
