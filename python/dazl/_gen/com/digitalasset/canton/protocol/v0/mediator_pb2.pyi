# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import common_pb2 as _common_pb2
from . import mediator_response_pb2 as _mediator_response_pb2
from . import merkle_pb2 as _merkle_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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
    __slots__ = ["approve", "validator_reject", "mediator_reject", "timeout"]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_REJECT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REJECT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    approve: _empty_pb2.Empty
    validator_reject: RejectionReasons
    mediator_reject: MediatorRejection
    timeout: _empty_pb2.Empty
    def __init__(self, approve: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., validator_reject: _Optional[_Union[RejectionReasons, _Mapping]] = ..., mediator_reject: _Optional[_Union[MediatorRejection, _Mapping]] = ..., timeout: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class RejectionReasons(_message.Message):
    __slots__ = ["reasons"]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    reasons: _containers.RepeatedCompositeFieldContainer[RejectionReason]
    def __init__(self, reasons: _Optional[_Iterable[_Union[RejectionReason, _Mapping]]] = ...) -> None: ...

class RejectionReason(_message.Message):
    __slots__ = ["parties", "reject"]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    REJECT_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    reject: _mediator_response_pb2.LocalReject
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., reject: _Optional[_Union[_mediator_response_pb2.LocalReject, _Mapping]] = ...) -> None: ...

class MediatorRejection(_message.Message):
    __slots__ = ["code", "reason"]
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        MissingCode: _ClassVar[MediatorRejection.Code]
        InformeesNotHostedOnActiveParticipant: _ClassVar[MediatorRejection.Code]
        NotEnoughConfirmingParties: _ClassVar[MediatorRejection.Code]
        ViewThresholdBelowMinimumThreshold: _ClassVar[MediatorRejection.Code]
        InvalidRootHashMessage: _ClassVar[MediatorRejection.Code]
        Timeout: _ClassVar[MediatorRejection.Code]
        WrongDeclaredMediator: _ClassVar[MediatorRejection.Code]
        NonUniqueRequestUuid: _ClassVar[MediatorRejection.Code]
    MissingCode: MediatorRejection.Code
    InformeesNotHostedOnActiveParticipant: MediatorRejection.Code
    NotEnoughConfirmingParties: MediatorRejection.Code
    ViewThresholdBelowMinimumThreshold: MediatorRejection.Code
    InvalidRootHashMessage: MediatorRejection.Code
    Timeout: MediatorRejection.Code
    WrongDeclaredMediator: MediatorRejection.Code
    NonUniqueRequestUuid: MediatorRejection.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    code: MediatorRejection.Code
    reason: str
    def __init__(self, code: _Optional[_Union[MediatorRejection.Code, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class InformeeTree(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ...) -> None: ...

class MalformedMediatorRequestResult(_message.Message):
    __slots__ = ["request_id", "domain_id", "view_type", "rejection"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    REJECTION_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    domain_id: str
    view_type: _common_pb2.ViewType
    rejection: MediatorRejection
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., domain_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ..., rejection: _Optional[_Union[MediatorRejection, _Mapping]] = ...) -> None: ...

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
