# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import participant_reassignment_pb2 as _participant_reassignment_pb2
from . import participant_transaction_pb2 as _participant_transaction_pb2
from . import topology_pb2 as _topology_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypedSignedProtocolMessageContent(_message.Message):
    __slots__ = ("confirmation_responses", "confirmation_result", "acs_commitment", "set_traffic_purchased")
    CONFIRMATION_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ACS_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    SET_TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    confirmation_responses: bytes
    confirmation_result: bytes
    acs_commitment: bytes
    set_traffic_purchased: bytes
    def __init__(self, confirmation_responses: _Optional[bytes] = ..., confirmation_result: _Optional[bytes] = ..., acs_commitment: _Optional[bytes] = ..., set_traffic_purchased: _Optional[bytes] = ...) -> None: ...

class SignedProtocolMessage(_message.Message):
    __slots__ = ("signature", "typed_signed_protocol_message_content")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TYPED_SIGNED_PROTOCOL_MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    signature: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    typed_signed_protocol_message_content: bytes
    def __init__(self, signature: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., typed_signed_protocol_message_content: _Optional[bytes] = ...) -> None: ...

class EnvelopeContent(_message.Message):
    __slots__ = ("informee_message", "encrypted_view_message", "unassignment_mediator_message", "assignment_mediator_message", "root_hash_message", "topology_transactions_broadcast")
    INFORMEE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VIEW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNMENT_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TRANSACTIONS_BROADCAST_FIELD_NUMBER: _ClassVar[int]
    informee_message: _participant_transaction_pb2.InformeeMessage
    encrypted_view_message: _participant_transaction_pb2.EncryptedViewMessage
    unassignment_mediator_message: _participant_reassignment_pb2.UnassignmentMediatorMessage
    assignment_mediator_message: _participant_reassignment_pb2.AssignmentMediatorMessage
    root_hash_message: _participant_transaction_pb2.RootHashMessage
    topology_transactions_broadcast: _topology_pb2.TopologyTransactionsBroadcast
    def __init__(self, informee_message: _Optional[_Union[_participant_transaction_pb2.InformeeMessage, _Mapping]] = ..., encrypted_view_message: _Optional[_Union[_participant_transaction_pb2.EncryptedViewMessage, _Mapping]] = ..., unassignment_mediator_message: _Optional[_Union[_participant_reassignment_pb2.UnassignmentMediatorMessage, _Mapping]] = ..., assignment_mediator_message: _Optional[_Union[_participant_reassignment_pb2.AssignmentMediatorMessage, _Mapping]] = ..., root_hash_message: _Optional[_Union[_participant_transaction_pb2.RootHashMessage, _Mapping]] = ..., topology_transactions_broadcast: _Optional[_Union[_topology_pb2.TopologyTransactionsBroadcast, _Mapping]] = ...) -> None: ...
