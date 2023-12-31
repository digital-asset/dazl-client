# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediatorResponse(_message.Message):
    __slots__ = ["request_id", "sender", "view_hash", "local_verdict", "root_hash", "confirming_parties", "domain_id"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    VIEW_HASH_FIELD_NUMBER: _ClassVar[int]
    LOCAL_VERDICT_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    CONFIRMING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    sender: str
    view_hash: bytes
    local_verdict: LocalVerdict
    root_hash: bytes
    confirming_parties: _containers.RepeatedScalarFieldContainer[str]
    domain_id: str
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sender: _Optional[str] = ..., view_hash: _Optional[bytes] = ..., local_verdict: _Optional[_Union[LocalVerdict, _Mapping]] = ..., root_hash: _Optional[bytes] = ..., confirming_parties: _Optional[_Iterable[str]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class LocalVerdict(_message.Message):
    __slots__ = ["local_approve", "local_reject"]
    LOCAL_APPROVE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_REJECT_FIELD_NUMBER: _ClassVar[int]
    local_approve: _empty_pb2.Empty
    local_reject: LocalReject
    def __init__(self, local_approve: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., local_reject: _Optional[_Union[LocalReject, _Mapping]] = ...) -> None: ...

class LocalReject(_message.Message):
    __slots__ = ["code", "reason", "resource"]
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        MissingCode: _ClassVar[LocalReject.Code]
        LockedContracts: _ClassVar[LocalReject.Code]
        LockedKeys: _ClassVar[LocalReject.Code]
        InactiveContracts: _ClassVar[LocalReject.Code]
        DuplicateKey: _ClassVar[LocalReject.Code]
        CreatesExistingContract: _ClassVar[LocalReject.Code]
        LedgerTime: _ClassVar[LocalReject.Code]
        SubmissionTime: _ClassVar[LocalReject.Code]
        LocalTimeout: _ClassVar[LocalReject.Code]
        MalformedPayloads: _ClassVar[LocalReject.Code]
        MalformedModel: _ClassVar[LocalReject.Code]
        MalformedConfirmationPolicy: _ClassVar[LocalReject.Code]
        BadRootHashMessage: _ClassVar[LocalReject.Code]
        TransferOutActivenessCheck: _ClassVar[LocalReject.Code]
        TransferInAlreadyCompleted: _ClassVar[LocalReject.Code]
        TransferInAlreadyActive: _ClassVar[LocalReject.Code]
        TransferInAlreadyArchived: _ClassVar[LocalReject.Code]
        TransferInLocked: _ClassVar[LocalReject.Code]
        InconsistentKey: _ClassVar[LocalReject.Code]
    MissingCode: LocalReject.Code
    LockedContracts: LocalReject.Code
    LockedKeys: LocalReject.Code
    InactiveContracts: LocalReject.Code
    DuplicateKey: LocalReject.Code
    CreatesExistingContract: LocalReject.Code
    LedgerTime: LocalReject.Code
    SubmissionTime: LocalReject.Code
    LocalTimeout: LocalReject.Code
    MalformedPayloads: LocalReject.Code
    MalformedModel: LocalReject.Code
    MalformedConfirmationPolicy: LocalReject.Code
    BadRootHashMessage: LocalReject.Code
    TransferOutActivenessCheck: LocalReject.Code
    TransferInAlreadyCompleted: LocalReject.Code
    TransferInAlreadyActive: LocalReject.Code
    TransferInAlreadyArchived: LocalReject.Code
    TransferInLocked: LocalReject.Code
    InconsistentKey: LocalReject.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    code: LocalReject.Code
    reason: str
    resource: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, code: _Optional[_Union[LocalReject.Code, str]] = ..., reason: _Optional[str] = ..., resource: _Optional[_Iterable[str]] = ...) -> None: ...
