# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....admin.participant.v30 import active_contract_pb2 as _active_contract_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartyReplicationTargetParticipantMessage(_message.Message):
    __slots__ = ("initialize", "send_acs_up_to")
    class Initialize(_message.Message):
        __slots__ = ("initial_contract_ordinal_inclusive",)
        INITIAL_CONTRACT_ORDINAL_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        initial_contract_ordinal_inclusive: int
        def __init__(self, initial_contract_ordinal_inclusive: _Optional[int] = ...) -> None: ...
    class SendAcsUpTo(_message.Message):
        __slots__ = ("max_contract_ordinal_inclusive",)
        MAX_CONTRACT_ORDINAL_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        max_contract_ordinal_inclusive: int
        def __init__(self, max_contract_ordinal_inclusive: _Optional[int] = ...) -> None: ...
    INITIALIZE_FIELD_NUMBER: _ClassVar[int]
    SEND_ACS_UP_TO_FIELD_NUMBER: _ClassVar[int]
    initialize: PartyReplicationTargetParticipantMessage.Initialize
    send_acs_up_to: PartyReplicationTargetParticipantMessage.SendAcsUpTo
    def __init__(self, initialize: _Optional[_Union[PartyReplicationTargetParticipantMessage.Initialize, _Mapping]] = ..., send_acs_up_to: _Optional[_Union[PartyReplicationTargetParticipantMessage.SendAcsUpTo, _Mapping]] = ...) -> None: ...

class PartyReplicationSourceParticipantMessage(_message.Message):
    __slots__ = ("acs_batch", "end_of_acs")
    class AcsBatch(_message.Message):
        __slots__ = ("contracts",)
        CONTRACTS_FIELD_NUMBER: _ClassVar[int]
        contracts: _containers.RepeatedCompositeFieldContainer[_active_contract_pb2.ActiveContractOld]
        def __init__(self, contracts: _Optional[_Iterable[_Union[_active_contract_pb2.ActiveContractOld, _Mapping]]] = ...) -> None: ...
    class EndOfACS(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ACS_BATCH_FIELD_NUMBER: _ClassVar[int]
    END_OF_ACS_FIELD_NUMBER: _ClassVar[int]
    acs_batch: PartyReplicationSourceParticipantMessage.AcsBatch
    end_of_acs: PartyReplicationSourceParticipantMessage.EndOfACS
    def __init__(self, acs_batch: _Optional[_Union[PartyReplicationSourceParticipantMessage.AcsBatch, _Mapping]] = ..., end_of_acs: _Optional[_Union[PartyReplicationSourceParticipantMessage.EndOfACS, _Mapping]] = ...) -> None: ...
