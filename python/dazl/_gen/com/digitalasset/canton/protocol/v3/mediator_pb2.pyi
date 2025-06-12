# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v2 import mediator_pb2 as _mediator_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Verdict(_message.Message):
    __slots__ = ("approve", "participant_reject", "mediator_reject")
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_REJECT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REJECT_FIELD_NUMBER: _ClassVar[int]
    approve: _empty_pb2.Empty
    participant_reject: _mediator_pb2.ParticipantReject
    mediator_reject: _mediator_pb2.MediatorReject
    def __init__(self, approve: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., participant_reject: _Optional[_Union[_mediator_pb2.ParticipantReject, _Mapping]] = ..., mediator_reject: _Optional[_Union[_mediator_pb2.MediatorReject, _Mapping]] = ...) -> None: ...

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
