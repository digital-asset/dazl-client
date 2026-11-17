# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcsDigestTrace(_message.Message):
    __slots__ = ("traces",)
    TRACES_FIELD_NUMBER: _ClassVar[int]
    traces: _containers.RepeatedCompositeFieldContainer[TraceElement]
    def __init__(self, traces: _Optional[_Iterable[_Union[TraceElement, _Mapping]]] = ...) -> None: ...

class TraceElement(_message.Message):
    __slots__ = ("group", "single")
    class TraceGroup(_message.Message):
        __slots__ = ("description", "traces", "added_to_hash")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TRACES_FIELD_NUMBER: _ClassVar[int]
        ADDED_TO_HASH_FIELD_NUMBER: _ClassVar[int]
        description: str
        traces: _containers.RepeatedCompositeFieldContainer[TraceElement.SingleTrace]
        added_to_hash: bool
        def __init__(self, description: _Optional[str] = ..., traces: _Optional[_Iterable[_Union[TraceElement.SingleTrace, _Mapping]]] = ..., added_to_hash: _Optional[bool] = ...) -> None: ...
    class SingleTrace(_message.Message):
        __slots__ = ("contract_id", "reassignment_counter", "party1", "party2", "is_activation")
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
        PARTY1_FIELD_NUMBER: _ClassVar[int]
        PARTY2_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
        contract_id: bytes
        reassignment_counter: int
        party1: str
        party2: str
        is_activation: bool
        def __init__(self, contract_id: _Optional[bytes] = ..., reassignment_counter: _Optional[int] = ..., party1: _Optional[str] = ..., party2: _Optional[str] = ..., is_activation: _Optional[bool] = ...) -> None: ...
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SINGLE_FIELD_NUMBER: _ClassVar[int]
    group: TraceElement.TraceGroup
    single: TraceElement.SingleTrace
    def __init__(self, group: _Optional[_Union[TraceElement.TraceGroup, _Mapping]] = ..., single: _Optional[_Union[TraceElement.SingleTrace, _Mapping]] = ...) -> None: ...

class ReceivedAcsCommitments(_message.Message):
    __slots__ = ("commitment",)
    COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    commitment: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, commitment: _Optional[_Iterable[bytes]] = ...) -> None: ...
