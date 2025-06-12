# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v0 import common_pb2 as _common_pb2
from ..v1 import mediator_pb2 as _mediator_pb2
from ..v1 import mediator_response_pb2 as _mediator_response_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionResultMessage(_message.Message):
    __slots__ = ("request_id", "verdict", "root_hash", "domain_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    verdict: Verdict
    root_hash: bytes
    domain_id: str
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., verdict: _Optional[_Union[Verdict, _Mapping]] = ..., root_hash: _Optional[bytes] = ..., domain_id: _Optional[str] = ...) -> None: ...

class Verdict(_message.Message):
    __slots__ = ("approve", "participant_reject", "mediator_reject")
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_REJECT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REJECT_FIELD_NUMBER: _ClassVar[int]
    approve: _empty_pb2.Empty
    participant_reject: ParticipantReject
    mediator_reject: _mediator_pb2.MediatorReject
    def __init__(self, approve: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., participant_reject: _Optional[_Union[ParticipantReject, _Mapping]] = ..., mediator_reject: _Optional[_Union[_mediator_pb2.MediatorReject, _Mapping]] = ...) -> None: ...

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
    reject: _mediator_response_pb2.LocalReject
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., reject: _Optional[_Union[_mediator_response_pb2.LocalReject, _Mapping]] = ...) -> None: ...

class TransferResult(_message.Message):
    __slots__ = ("request_id", "source_domain", "target_domain", "informees", "verdict")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    INFORMEES_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    source_domain: str
    target_domain: str
    informees: _containers.RepeatedScalarFieldContainer[str]
    verdict: Verdict
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_domain: _Optional[str] = ..., target_domain: _Optional[str] = ..., informees: _Optional[_Iterable[str]] = ..., verdict: _Optional[_Union[Verdict, _Mapping]] = ...) -> None: ...

class MediatorReject(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: _status_pb2.Status
    def __init__(self, reason: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class MalformedMediatorRequestResult(_message.Message):
    __slots__ = ("request_id", "domain_id", "view_type", "rejection")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    REJECTION_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    domain_id: str
    view_type: _common_pb2.ViewType
    rejection: MediatorReject
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., domain_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ..., rejection: _Optional[_Union[MediatorReject, _Mapping]] = ...) -> None: ...
