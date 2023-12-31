# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import causality_pb2 as _causality_pb2
from ..v0 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v0 import sequencing_pb2 as _sequencing_pb2
from ..v0 import synchronization_pb2 as _synchronization_pb2
from ..v0 import topology_pb2 as _topology_pb2
from . import participant_transaction_pb2 as _participant_transaction_pb2_1
from . import participant_transfer_pb2 as _participant_transfer_pb2
from . import topology_pb2 as _topology_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvelopeContent(_message.Message):
    __slots__ = ["informee_message", "signed_message", "encrypted_view_message", "domain_topology_transaction_message", "transfer_out_mediator_message", "transfer_in_mediator_message", "root_hash_message", "register_topology_transaction_request", "register_topology_transaction_response", "causality_message"]
    INFORMEE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VIEW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_TOPOLOGY_TRANSACTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_IN_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TOPOLOGY_TRANSACTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TOPOLOGY_TRANSACTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CAUSALITY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    informee_message: _participant_transaction_pb2_1.InformeeMessage
    signed_message: _synchronization_pb2.SignedProtocolMessage
    encrypted_view_message: _participant_transaction_pb2_1.EncryptedViewMessage
    domain_topology_transaction_message: _topology_pb2.DomainTopologyTransactionMessage
    transfer_out_mediator_message: _participant_transfer_pb2.TransferOutMediatorMessage
    transfer_in_mediator_message: _participant_transfer_pb2.TransferInMediatorMessage
    root_hash_message: _participant_transaction_pb2.RootHashMessage
    register_topology_transaction_request: _topology_pb2.RegisterTopologyTransactionRequest
    register_topology_transaction_response: _topology_pb2_1.RegisterTopologyTransactionResponse
    causality_message: _causality_pb2.CausalityMessage
    def __init__(self, informee_message: _Optional[_Union[_participant_transaction_pb2_1.InformeeMessage, _Mapping]] = ..., signed_message: _Optional[_Union[_synchronization_pb2.SignedProtocolMessage, _Mapping]] = ..., encrypted_view_message: _Optional[_Union[_participant_transaction_pb2_1.EncryptedViewMessage, _Mapping]] = ..., domain_topology_transaction_message: _Optional[_Union[_topology_pb2.DomainTopologyTransactionMessage, _Mapping]] = ..., transfer_out_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferOutMediatorMessage, _Mapping]] = ..., transfer_in_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferInMediatorMessage, _Mapping]] = ..., root_hash_message: _Optional[_Union[_participant_transaction_pb2.RootHashMessage, _Mapping]] = ..., register_topology_transaction_request: _Optional[_Union[_topology_pb2.RegisterTopologyTransactionRequest, _Mapping]] = ..., register_topology_transaction_response: _Optional[_Union[_topology_pb2_1.RegisterTopologyTransactionResponse, _Mapping]] = ..., causality_message: _Optional[_Union[_causality_pb2.CausalityMessage, _Mapping]] = ...) -> None: ...

class SignedProtocolMessage(_message.Message):
    __slots__ = ["signature", "typed_signed_protocol_message_content"]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TYPED_SIGNED_PROTOCOL_MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    signature: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    typed_signed_protocol_message_content: bytes
    def __init__(self, signature: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., typed_signed_protocol_message_content: _Optional[bytes] = ...) -> None: ...
