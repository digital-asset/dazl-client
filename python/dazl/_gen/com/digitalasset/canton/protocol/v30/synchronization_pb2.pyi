# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import participant_transaction_pb2 as _participant_transaction_pb2
from . import participant_transfer_pb2 as _participant_transfer_pb2
from . import topology_pb2 as _topology_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypedSignedProtocolMessageContent(_message.Message):
    __slots__ = ("confirmation_response", "confirmation_result", "acs_commitment", "set_traffic_purchased")
    CONFIRMATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ACS_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    SET_TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    confirmation_response: bytes
    confirmation_result: bytes
    acs_commitment: bytes
    set_traffic_purchased: bytes
    def __init__(self, confirmation_response: _Optional[bytes] = ..., confirmation_result: _Optional[bytes] = ..., acs_commitment: _Optional[bytes] = ..., set_traffic_purchased: _Optional[bytes] = ...) -> None: ...

class SignedProtocolMessage(_message.Message):
    __slots__ = ("signature", "typed_signed_protocol_message_content")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TYPED_SIGNED_PROTOCOL_MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    signature: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    typed_signed_protocol_message_content: bytes
    def __init__(self, signature: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., typed_signed_protocol_message_content: _Optional[bytes] = ...) -> None: ...

class EnvelopeContent(_message.Message):
    __slots__ = ("informee_message", "encrypted_view_message", "transfer_out_mediator_message", "transfer_in_mediator_message", "root_hash_message", "topology_transactions_broadcast")
    INFORMEE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VIEW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_IN_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TRANSACTIONS_BROADCAST_FIELD_NUMBER: _ClassVar[int]
    informee_message: _participant_transaction_pb2.InformeeMessage
    encrypted_view_message: _participant_transaction_pb2.EncryptedViewMessage
    transfer_out_mediator_message: _participant_transfer_pb2.TransferOutMediatorMessage
    transfer_in_mediator_message: _participant_transfer_pb2.TransferInMediatorMessage
    root_hash_message: _participant_transaction_pb2.RootHashMessage
    topology_transactions_broadcast: _topology_pb2.TopologyTransactionsBroadcast
    def __init__(self, informee_message: _Optional[_Union[_participant_transaction_pb2.InformeeMessage, _Mapping]] = ..., encrypted_view_message: _Optional[_Union[_participant_transaction_pb2.EncryptedViewMessage, _Mapping]] = ..., transfer_out_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferOutMediatorMessage, _Mapping]] = ..., transfer_in_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferInMediatorMessage, _Mapping]] = ..., root_hash_message: _Optional[_Union[_participant_transaction_pb2.RootHashMessage, _Mapping]] = ..., topology_transactions_broadcast: _Optional[_Union[_topology_pb2.TopologyTransactionsBroadcast, _Mapping]] = ...) -> None: ...
