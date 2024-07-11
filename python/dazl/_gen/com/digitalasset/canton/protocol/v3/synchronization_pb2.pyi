# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v0 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v0 import sequencing_pb2 as _sequencing_pb2
from ..v0 import topology_pb2 as _topology_pb2
from ..v1 import participant_transaction_pb2 as _participant_transaction_pb2_1
from ..v1 import participant_transfer_pb2 as _participant_transfer_pb2
from ..v1 import sequencing_pb2 as _sequencing_pb2_1
from ..v1 import topology_pb2 as _topology_pb2_1
from ..v2 import topology_pb2 as _topology_pb2_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvelopeContent(_message.Message):
    __slots__ = ["informee_message", "encrypted_view_message", "domain_topology_transaction_message", "transfer_out_mediator_message", "transfer_in_mediator_message", "root_hash_message", "register_topology_transaction_request", "register_topology_transaction_response", "register_topology_transaction_request_x", "register_topology_transaction_response_x", "accepted_topology_transactions"]
    INFORMEE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VIEW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_TOPOLOGY_TRANSACTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_IN_MEDIATOR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TOPOLOGY_TRANSACTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TOPOLOGY_TRANSACTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TOPOLOGY_TRANSACTION_REQUEST_X_FIELD_NUMBER: _ClassVar[int]
    REGISTER_TOPOLOGY_TRANSACTION_RESPONSE_X_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_TOPOLOGY_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    informee_message: _participant_transaction_pb2_1.InformeeMessage
    encrypted_view_message: _participant_transaction_pb2_1.EncryptedViewMessage
    domain_topology_transaction_message: _topology_pb2_1.DomainTopologyTransactionMessage
    transfer_out_mediator_message: _participant_transfer_pb2.TransferOutMediatorMessage
    transfer_in_mediator_message: _participant_transfer_pb2.TransferInMediatorMessage
    root_hash_message: _participant_transaction_pb2.RootHashMessage
    register_topology_transaction_request: _topology_pb2.RegisterTopologyTransactionRequest
    register_topology_transaction_response: _topology_pb2_1.RegisterTopologyTransactionResponse
    register_topology_transaction_request_x: _topology_pb2_1_1.RegisterTopologyTransactionRequestX
    register_topology_transaction_response_x: _topology_pb2_1_1.RegisterTopologyTransactionResponseX
    accepted_topology_transactions: _topology_pb2_1_1.AcceptedTopologyTransactionsX
    def __init__(self, informee_message: _Optional[_Union[_participant_transaction_pb2_1.InformeeMessage, _Mapping]] = ..., encrypted_view_message: _Optional[_Union[_participant_transaction_pb2_1.EncryptedViewMessage, _Mapping]] = ..., domain_topology_transaction_message: _Optional[_Union[_topology_pb2_1.DomainTopologyTransactionMessage, _Mapping]] = ..., transfer_out_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferOutMediatorMessage, _Mapping]] = ..., transfer_in_mediator_message: _Optional[_Union[_participant_transfer_pb2.TransferInMediatorMessage, _Mapping]] = ..., root_hash_message: _Optional[_Union[_participant_transaction_pb2.RootHashMessage, _Mapping]] = ..., register_topology_transaction_request: _Optional[_Union[_topology_pb2.RegisterTopologyTransactionRequest, _Mapping]] = ..., register_topology_transaction_response: _Optional[_Union[_topology_pb2_1.RegisterTopologyTransactionResponse, _Mapping]] = ..., register_topology_transaction_request_x: _Optional[_Union[_topology_pb2_1_1.RegisterTopologyTransactionRequestX, _Mapping]] = ..., register_topology_transaction_response_x: _Optional[_Union[_topology_pb2_1_1.RegisterTopologyTransactionResponseX, _Mapping]] = ..., accepted_topology_transactions: _Optional[_Union[_topology_pb2_1_1.AcceptedTopologyTransactionsX, _Mapping]] = ...) -> None: ...
