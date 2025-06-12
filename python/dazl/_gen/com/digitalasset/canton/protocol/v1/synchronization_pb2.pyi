# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v0 import causality_pb2 as _causality_pb2
from ..v0 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v0 import synchronization_pb2 as _synchronization_pb2
from ..v0 import topology_pb2 as _topology_pb2
from . import participant_transaction_pb2 as _participant_transaction_pb2_1
from . import participant_transfer_pb2 as _participant_transfer_pb2
from . import topology_pb2 as _topology_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvelopeContent(_message.Message):
    __slots__ = ("informee_message", "signed_message", "encrypted_view_message", "domain_topology_transaction_message", "transfer_out_mediator_message", "transfer_in_mediator_message", "root_hash_message", "register_topology_transaction_request", "register_topology_transaction_response", "causality_message")
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
