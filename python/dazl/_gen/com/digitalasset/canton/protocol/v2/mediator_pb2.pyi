# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v1 import mediator_pb2 as _mediator_pb2
from ..v1 import mediator_response_pb2 as _mediator_response_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionResultMessage(_message.Message):
    __slots__ = ["request_id", "verdict", "root_hash", "domain_id"]
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
    __slots__ = ["approve", "participant_reject", "mediator_reject"]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_REJECT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REJECT_FIELD_NUMBER: _ClassVar[int]
    approve: _empty_pb2.Empty
    participant_reject: ParticipantReject
    mediator_reject: _mediator_pb2.MediatorReject
    def __init__(self, approve: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., participant_reject: _Optional[_Union[ParticipantReject, _Mapping]] = ..., mediator_reject: _Optional[_Union[_mediator_pb2.MediatorReject, _Mapping]] = ...) -> None: ...

class ParticipantReject(_message.Message):
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
