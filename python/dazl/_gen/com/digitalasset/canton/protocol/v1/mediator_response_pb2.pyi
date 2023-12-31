# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
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
    __slots__ = ["cause_prefix", "details", "resource", "error_code", "error_category"]
    CAUSE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    cause_prefix: str
    details: str
    resource: _containers.RepeatedScalarFieldContainer[str]
    error_code: str
    error_category: int
    def __init__(self, cause_prefix: _Optional[str] = ..., details: _Optional[str] = ..., resource: _Optional[_Iterable[str]] = ..., error_code: _Optional[str] = ..., error_category: _Optional[int] = ...) -> None: ...
