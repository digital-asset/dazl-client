# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v1 import mediator_response_pb2 as _mediator_response_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediatorResponse(_message.Message):
    __slots__ = ["request_id", "sender", "local_verdict", "root_hash", "confirming_parties", "domain_id", "view_position"]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_VERDICT_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    CONFIRMING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_POSITION_FIELD_NUMBER: _ClassVar[int]
    request_id: _timestamp_pb2.Timestamp
    sender: str
    local_verdict: _mediator_response_pb2.LocalVerdict
    root_hash: bytes
    confirming_parties: _containers.RepeatedScalarFieldContainer[str]
    domain_id: str
    view_position: ViewPosition
    def __init__(self, request_id: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sender: _Optional[str] = ..., local_verdict: _Optional[_Union[_mediator_response_pb2.LocalVerdict, _Mapping]] = ..., root_hash: _Optional[bytes] = ..., confirming_parties: _Optional[_Iterable[str]] = ..., domain_id: _Optional[str] = ..., view_position: _Optional[_Union[ViewPosition, _Mapping]] = ...) -> None: ...

class ViewPosition(_message.Message):
    __slots__ = ["position"]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    position: _containers.RepeatedCompositeFieldContainer[MerkleSeqIndex]
    def __init__(self, position: _Optional[_Iterable[_Union[MerkleSeqIndex, _Mapping]]] = ...) -> None: ...

class MerkleSeqIndex(_message.Message):
    __slots__ = ["is_right"]
    IS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    is_right: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, is_right: _Optional[_Iterable[bool]] = ...) -> None: ...
