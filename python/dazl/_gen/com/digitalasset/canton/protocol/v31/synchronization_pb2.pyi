# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v30 import acs_commitments_pb2 as _acs_commitments_pb2
from ..v30 import participant_reassignment_pb2 as _participant_reassignment_pb2
from ..v30 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v30 import synchronization_pb2 as _synchronization_pb2
from ..v30 import topology_pb2 as _topology_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvelopeContent(_message.Message):
    __slots__ = ("informee_message", "encrypted_view_message", "unassignment_mediator_message", "assignment_mediator_message", "root_hash_message", "topology_transactions_broadcast", "acs_commitment_protocol_message", "lsu_sequencing_test_message")
    INFORMEE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VIEW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNMENT_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TRANSACTIONS_BROADCAST_FIELD_NUMBER: _ClassVar[int]
    ACS_COMMITMENT_PROTOCOL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LSU_SEQUENCING_TEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    informee_message: _participant_transaction_pb2.InformeeMessage
    encrypted_view_message: _participant_transaction_pb2.EncryptedViewMessage
    unassignment_mediator_message: _participant_reassignment_pb2.UnassignmentMediatorMessage
    assignment_mediator_message: _participant_reassignment_pb2.AssignmentMediatorMessage
    root_hash_message: _participant_transaction_pb2.RootHashMessage
    topology_transactions_broadcast: _topology_pb2.TopologyTransactionsBroadcast
    acs_commitment_protocol_message: _acs_commitments_pb2.AcsCommitmentProtocolMessage
    lsu_sequencing_test_message: _synchronization_pb2.LsuSequencingTestMessage
    def __init__(self, informee_message: _Optional[_Union[_participant_transaction_pb2.InformeeMessage, _Mapping]] = ..., encrypted_view_message: _Optional[_Union[_participant_transaction_pb2.EncryptedViewMessage, _Mapping]] = ..., unassignment_mediator_message: _Optional[_Union[_participant_reassignment_pb2.UnassignmentMediatorMessage, _Mapping]] = ..., assignment_mediator_message: _Optional[_Union[_participant_reassignment_pb2.AssignmentMediatorMessage, _Mapping]] = ..., root_hash_message: _Optional[_Union[_participant_transaction_pb2.RootHashMessage, _Mapping]] = ..., topology_transactions_broadcast: _Optional[_Union[_topology_pb2.TopologyTransactionsBroadcast, _Mapping]] = ..., acs_commitment_protocol_message: _Optional[_Union[_acs_commitments_pb2.AcsCommitmentProtocolMessage, _Mapping]] = ..., lsu_sequencing_test_message: _Optional[_Union[_synchronization_pb2.LsuSequencingTestMessage, _Mapping]] = ...) -> None: ...
