# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import topology_pb2 as _topology_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Quorum(_message.Message):
    __slots__ = ("party_index_and_weight", "threshold")
    PARTY_INDEX_AND_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    party_index_and_weight: _containers.RepeatedCompositeFieldContainer[PartyIndexAndWeight]
    threshold: int
    def __init__(self, party_index_and_weight: _Optional[_Iterable[_Union[PartyIndexAndWeight, _Mapping]]] = ..., threshold: _Optional[int] = ...) -> None: ...

class PartyIndexAndWeight(_message.Message):
    __slots__ = ("index", "weight")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    index: int
    weight: int
    def __init__(self, index: _Optional[int] = ..., weight: _Optional[int] = ...) -> None: ...

class TrustParty(_message.Message):
    __slots__ = ("party", "required_trust_level")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_TRUST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    party: str
    required_trust_level: _topology_pb2.TrustLevel
    def __init__(self, party: _Optional[str] = ..., required_trust_level: _Optional[_Union[_topology_pb2.TrustLevel, str]] = ...) -> None: ...
