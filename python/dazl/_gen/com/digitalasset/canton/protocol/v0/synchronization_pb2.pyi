# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from . import causality_pb2 as _causality_pb2
from . import participant_transaction_pb2 as _participant_transaction_pb2
from . import participant_transfer_pb2 as _participant_transfer_pb2
from . import topology_pb2 as _topology_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignedProtocolMessage(_message.Message):
    __slots__ = ["signature", "mediator_response", "transaction_result", "malformed_mediator_request_result", "transfer_result", "acs_commitment"]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    MALFORMED_MEDIATOR_REQUEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_RESULT_FIELD_NUMBER: _ClassVar[int]
    ACS_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    signature: _crypto_pb2.Signature
    mediator_response: bytes
    transaction_result: bytes
    malformed_mediator_request_result: bytes
    transfer_result: bytes
    acs_commitment: bytes
    def __init__(self, signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., mediator_response: _Optional[bytes] = ..., transaction_result: _Optional[bytes] = ..., malformed_mediator_request_result: _Optional[bytes] = ..., transfer_result: _Optional[bytes] = ..., acs_commitment: _Optional[bytes] = ...) -> None: ...

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
    informee_message: _participant_transaction_pb2.InformeeMessage
    signed_message: SignedProtocolMessage
    encrypted_view_message: _participant_transaction_pb2.EncryptedViewMessage
    domain_topology_transaction_message: _topology_pb2.DomainTopologyTransactionMessage
    transfer_out_mediator_message: _participant_transfer_pb2.TransferOutMediatorMessage
    transfer_in_mediator_message: _participant_transfer_pb2.TransferInMediatorMessage
    root_hash_message: _participant_transaction_pb2.RootHashMessage
    register_topology_transaction_request: _topology_pb2.RegisterTopologyTransactionRequest
    register_topology_transaction_response: _topology_pb2.RegisterTopologyTransactionResponse
    causality_message: _causality_pb2.CausalityMessage
    def __init__(self, informee_message: _Optional[_Union[_participant_transaction_pb2.InformeeMessage, _Mapping]] = ..., signed_message: _Optional[_Union[SignedProtocolMessage, _Mapping]] = ..., encrypted_view_message: _Optional[_Union[_participant_transaction_pb2.EncryptedViewMessage, _Mapping]] = ..., domain_topology_transaction_message: _Optional[_Union[_topology_pb2.DomainTopologyTransactionMessage, _Mapping]] = ..., transfer_out_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferOutMediatorMessage, _Mapping]] = ..., transfer_in_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferInMediatorMessage, _Mapping]] = ..., root_hash_message: _Optional[_Union[_participant_transaction_pb2.RootHashMessage, _Mapping]] = ..., register_topology_transaction_request: _Optional[_Union[_topology_pb2.RegisterTopologyTransactionRequest, _Mapping]] = ..., register_topology_transaction_response: _Optional[_Union[_topology_pb2.RegisterTopologyTransactionResponse, _Mapping]] = ..., causality_message: _Optional[_Union[_causality_pb2.CausalityMessage, _Mapping]] = ...) -> None: ...

class TypedSignedProtocolMessageContent(_message.Message):
    __slots__ = ["mediator_response", "transaction_result", "malformed_mediator_request_result", "transfer_result", "acs_commitment"]
    MEDIATOR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    MALFORMED_MEDIATOR_REQUEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_RESULT_FIELD_NUMBER: _ClassVar[int]
    ACS_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    mediator_response: bytes
    transaction_result: bytes
    malformed_mediator_request_result: bytes
    transfer_result: bytes
    acs_commitment: bytes
    def __init__(self, mediator_response: _Optional[bytes] = ..., transaction_result: _Optional[bytes] = ..., malformed_mediator_request_result: _Optional[bytes] = ..., transfer_result: _Optional[bytes] = ..., acs_commitment: _Optional[bytes] = ...) -> None: ...
