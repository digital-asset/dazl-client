# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from .....admin.participant.v30 import active_contract_pb2 as _active_contract_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartyReplicationInstruction(_message.Message):
    __slots__ = ("max_counter",)
    MAX_COUNTER_FIELD_NUMBER: _ClassVar[int]
    max_counter: int
    def __init__(self, max_counter: _Optional[int] = ...) -> None: ...

class PartyReplicationSourceMessage(_message.Message):
    __slots__ = ("acs_chunk", "source_participant_is_ready", "end_of_acs")
    class AcsChunk(_message.Message):
        __slots__ = ("chunk_counter", "contracts")
        CHUNK_COUNTER_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_FIELD_NUMBER: _ClassVar[int]
        chunk_counter: int
        contracts: _containers.RepeatedCompositeFieldContainer[_active_contract_pb2.ActiveContractOld]
        def __init__(self, chunk_counter: _Optional[int] = ..., contracts: _Optional[_Iterable[_Union[_active_contract_pb2.ActiveContractOld, _Mapping]]] = ...) -> None: ...
    class SourceParticipantIsReady(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class EndOfACS(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ACS_CHUNK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARTICIPANT_IS_READY_FIELD_NUMBER: _ClassVar[int]
    END_OF_ACS_FIELD_NUMBER: _ClassVar[int]
    acs_chunk: PartyReplicationSourceMessage.AcsChunk
    source_participant_is_ready: PartyReplicationSourceMessage.SourceParticipantIsReady
    end_of_acs: PartyReplicationSourceMessage.EndOfACS
    def __init__(self, acs_chunk: _Optional[_Union[PartyReplicationSourceMessage.AcsChunk, _Mapping]] = ..., source_participant_is_ready: _Optional[_Union[PartyReplicationSourceMessage.SourceParticipantIsReady, _Mapping]] = ..., end_of_acs: _Optional[_Union[PartyReplicationSourceMessage.EndOfACS, _Mapping]] = ...) -> None: ...
