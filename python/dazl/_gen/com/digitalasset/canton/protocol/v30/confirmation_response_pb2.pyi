# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalVerdict(_message.Message):
    __slots__ = ("code", "reason")
    class VerdictCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERDICT_CODE_UNSPECIFIED: _ClassVar[LocalVerdict.VerdictCode]
        VERDICT_CODE_LOCAL_APPROVE: _ClassVar[LocalVerdict.VerdictCode]
        VERDICT_CODE_LOCAL_REJECT: _ClassVar[LocalVerdict.VerdictCode]
        VERDICT_CODE_LOCAL_MALFORMED: _ClassVar[LocalVerdict.VerdictCode]
    VERDICT_CODE_UNSPECIFIED: LocalVerdict.VerdictCode
    VERDICT_CODE_LOCAL_APPROVE: LocalVerdict.VerdictCode
    VERDICT_CODE_LOCAL_REJECT: LocalVerdict.VerdictCode
    VERDICT_CODE_LOCAL_MALFORMED: LocalVerdict.VerdictCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    code: LocalVerdict.VerdictCode
    reason: _status_pb2.Status
    def __init__(self, code: _Optional[_Union[LocalVerdict.VerdictCode, str]] = ..., reason: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class ConfirmationResponse(_message.Message):
    __slots__ = ("request_id", "sender", "local_verdict", "root_hash", "confirming_parties", "domain_id", "view_position")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_VERDICT_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    CONFIRMING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_POSITION_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    sender: str
    local_verdict: LocalVerdict
    root_hash: bytes
    confirming_parties: _containers.RepeatedScalarFieldContainer[str]
    domain_id: str
    view_position: ViewPosition
    def __init__(self, request_id: _Optional[int] = ..., sender: _Optional[str] = ..., local_verdict: _Optional[_Union[LocalVerdict, _Mapping]] = ..., root_hash: _Optional[bytes] = ..., confirming_parties: _Optional[_Iterable[str]] = ..., domain_id: _Optional[str] = ..., view_position: _Optional[_Union[ViewPosition, _Mapping]] = ...) -> None: ...

class ViewPosition(_message.Message):
    __slots__ = ("position",)
    POSITION_FIELD_NUMBER: _ClassVar[int]
    position: _containers.RepeatedCompositeFieldContainer[MerkleSeqIndex]
    def __init__(self, position: _Optional[_Iterable[_Union[MerkleSeqIndex, _Mapping]]] = ...) -> None: ...

class MerkleSeqIndex(_message.Message):
    __slots__ = ("is_right",)
    IS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    is_right: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, is_right: _Optional[_Iterable[bool]] = ...) -> None: ...
