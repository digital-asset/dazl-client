# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenTransactionTree(_message.Message):
    __slots__ = ["submitter_metadata", "common_metadata", "participant_metadata", "root_views"]
    SUBMITTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_METADATA_FIELD_NUMBER: _ClassVar[int]
    ROOT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    submitter_metadata: BlindableNode
    common_metadata: BlindableNode
    participant_metadata: BlindableNode
    root_views: MerkleSeq
    def __init__(self, submitter_metadata: _Optional[_Union[BlindableNode, _Mapping]] = ..., common_metadata: _Optional[_Union[BlindableNode, _Mapping]] = ..., participant_metadata: _Optional[_Union[BlindableNode, _Mapping]] = ..., root_views: _Optional[_Union[MerkleSeq, _Mapping]] = ...) -> None: ...

class BlindableNode(_message.Message):
    __slots__ = ["unblinded", "blinded_hash"]
    UNBLINDED_FIELD_NUMBER: _ClassVar[int]
    BLINDED_HASH_FIELD_NUMBER: _ClassVar[int]
    unblinded: bytes
    blinded_hash: bytes
    def __init__(self, unblinded: _Optional[bytes] = ..., blinded_hash: _Optional[bytes] = ...) -> None: ...

class MerkleSeq(_message.Message):
    __slots__ = ["root_or_empty"]
    ROOT_OR_EMPTY_FIELD_NUMBER: _ClassVar[int]
    root_or_empty: BlindableNode
    def __init__(self, root_or_empty: _Optional[_Union[BlindableNode, _Mapping]] = ...) -> None: ...

class MerkleSeqElement(_message.Message):
    __slots__ = ["first", "second", "data"]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    first: BlindableNode
    second: BlindableNode
    data: BlindableNode
    def __init__(self, first: _Optional[_Union[BlindableNode, _Mapping]] = ..., second: _Optional[_Union[BlindableNode, _Mapping]] = ..., data: _Optional[_Union[BlindableNode, _Mapping]] = ...) -> None: ...
