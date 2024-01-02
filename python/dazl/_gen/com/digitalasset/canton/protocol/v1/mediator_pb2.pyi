# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v0 import common_pb2 as _common_pb2
from ..v0 import mediator_pb2 as _mediator_pb2
from . import merkle_pb2 as _merkle_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionResultMessage(_message.Message):
    __slots__ = ["request_id", "verdict", "notification_tree"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TREE_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    verdict: Verdict
    notification_tree: InformeeTree
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., verdict: _Optional[_Union[Verdict, _Mapping]] = ..., notification_tree: _Optional[_Union[InformeeTree, _Mapping]] = ...) -> None: ...

class Verdict(_message.Message):
    __slots__ = ["approve", "participant_reject", "mediator_reject"]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_REJECT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REJECT_FIELD_NUMBER: _ClassVar[int]
    approve: _empty_pb2.Empty
    participant_reject: ParticipantReject
    mediator_reject: MediatorReject
    def __init__(self, approve: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., participant_reject: _Optional[_Union[ParticipantReject, _Mapping]] = ..., mediator_reject: _Optional[_Union[MediatorReject, _Mapping]] = ...) -> None: ...

class InformeeTree(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ...) -> None: ...

class ParticipantReject(_message.Message):
    __slots__ = ["reasons"]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    reasons: _containers.RepeatedCompositeFieldContainer[_mediator_pb2.RejectionReason]
    def __init__(self, reasons: _Optional[_Iterable[_Union[_mediator_pb2.RejectionReason, _Mapping]]] = ...) -> None: ...

class MediatorReject(_message.Message):
    __slots__ = ["cause", "error_code", "error_category"]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    cause: str
    error_code: str
    error_category: int
    def __init__(self, cause: _Optional[str] = ..., error_code: _Optional[str] = ..., error_category: _Optional[int] = ...) -> None: ...

class MalformedMediatorRequestResult(_message.Message):
    __slots__ = ["request_id", "domain_id", "view_type", "rejection"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    REJECTION_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    domain_id: str
    view_type: _common_pb2.ViewType
    rejection: MediatorReject
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., domain_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ..., rejection: _Optional[_Union[MediatorReject, _Mapping]] = ...) -> None: ...

class TransferResult(_message.Message):
    __slots__ = ["request_id", "origin_domain", "target_domain", "informees", "verdict"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    INFORMEES_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    origin_domain: str
    target_domain: str
    informees: _containers.RepeatedScalarFieldContainer[str]
    verdict: Verdict
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., origin_domain: _Optional[str] = ..., target_domain: _Optional[str] = ..., informees: _Optional[_Iterable[str]] = ..., verdict: _Optional[_Union[Verdict, _Mapping]] = ...) -> None: ...
