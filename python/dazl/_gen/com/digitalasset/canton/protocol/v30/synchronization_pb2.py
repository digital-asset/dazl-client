# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v30/synchronization.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'com/digitalasset/canton/protocol/v30/synchronization.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v30 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v30_dot_crypto__pb2
from . import participant_transaction_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_participant__transaction__pb2
from . import participant_transfer_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_participant__transfer__pb2
from . import topology_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_topology__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:com/digitalasset/canton/protocol/v30/synchronization.proto\x12$com.digitalasset.canton.protocol.v30\x1a/com/digitalasset/canton/crypto/v30/crypto.proto\x1a\x42\x63om/digitalasset/canton/protocol/v30/participant_transaction.proto\x1a?com/digitalasset/canton/protocol/v30/participant_transfer.proto\x1a\x33\x63om/digitalasset/canton/protocol/v30/topology.proto\"\x8c\x02\n!TypedSignedProtocolMessageContent\x12\x35\n\x15\x63onfirmation_response\x18\x02 \x01(\x0cH\x00R\x14\x63onfirmationResponse\x12\x31\n\x13\x63onfirmation_result\x18\x03 \x01(\x0cH\x00R\x12\x63onfirmationResult\x12\'\n\x0e\x61\x63s_commitment\x18\x04 \x01(\x0cH\x00R\racsCommitment\x12\x34\n\x15set_traffic_purchased\x18\x05 \x01(\x0cH\x00R\x13setTrafficPurchasedB\x1e\n\x1csome_signed_protocol_message\"\xb6\x01\n\x15SignedProtocolMessage\x12K\n\tsignature\x18\x01 \x03(\x0b\x32-.com.digitalasset.canton.crypto.v30.SignatureR\tsignature\x12P\n%typed_signed_protocol_message_content\x18\x02 \x01(\x0cR!typedSignedProtocolMessageContent\"\x84\x06\n\x0f\x45nvelopeContent\x12\x62\n\x10informee_message\x18\x01 \x01(\x0b\x32\x35.com.digitalasset.canton.protocol.v30.InformeeMessageH\x00R\x0finformeeMessage\x12r\n\x16\x65ncrypted_view_message\x18\x02 \x01(\x0b\x32:.com.digitalasset.canton.protocol.v30.EncryptedViewMessageH\x00R\x14\x65ncryptedViewMessage\x12\x85\x01\n\x1dtransfer_out_mediator_message\x18\x03 \x01(\x0b\x32@.com.digitalasset.canton.protocol.v30.TransferOutMediatorMessageH\x00R\x1atransferOutMediatorMessage\x12\x82\x01\n\x1ctransfer_in_mediator_message\x18\x04 \x01(\x0b\x32?.com.digitalasset.canton.protocol.v30.TransferInMediatorMessageH\x00R\x19transferInMediatorMessage\x12\x63\n\x11root_hash_message\x18\x05 \x01(\x0b\x32\x35.com.digitalasset.canton.protocol.v30.RootHashMessageH\x00R\x0frootHashMessage\x12\x8d\x01\n\x1ftopology_transactions_broadcast\x18\x06 \x01(\x0b\x32\x43.com.digitalasset.canton.protocol.v30.TopologyTransactionsBroadcastH\x00R\x1dtopologyTransactionsBroadcastB\x17\n\x15some_envelope_contentBUZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v30.synchronization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30'
  _globals['_TYPEDSIGNEDPROTOCOLMESSAGECONTENT']._serialized_start=336
  _globals['_TYPEDSIGNEDPROTOCOLMESSAGECONTENT']._serialized_end=604
  _globals['_SIGNEDPROTOCOLMESSAGE']._serialized_start=607
  _globals['_SIGNEDPROTOCOLMESSAGE']._serialized_end=789
  _globals['_ENVELOPECONTENT']._serialized_start=792
  _globals['_ENVELOPECONTENT']._serialized_end=1564
# @@protoc_insertion_point(module_scope)
