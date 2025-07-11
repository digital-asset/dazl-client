# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v1/merkle.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'com/digitalasset/canton/protocol/v1/merkle.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0com/digitalasset/canton/protocol/v1/merkle.proto\x12#com.digitalasset.canton.protocol.v1\"\x8a\x03\n\x12GenTransactionTree\x12\x61\n\x12submitter_metadata\x18\x01 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x11submitterMetadata\x12[\n\x0f\x63ommon_metadata\x18\x02 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x0e\x63ommonMetadata\x12\x65\n\x14participant_metadata\x18\x03 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x13participantMetadata\x12M\n\nroot_views\x18\x04 \x01(\x0b\x32..com.digitalasset.canton.protocol.v1.MerkleSeqR\trootViews\"f\n\rBlindableNode\x12\x1e\n\tunblinded\x18\x01 \x01(\x0cH\x00R\tunblinded\x12#\n\x0c\x62linded_hash\x18\x02 \x01(\x0cH\x00R\x0b\x62lindedHashB\x10\n\x0e\x62linded_or_not\"c\n\tMerkleSeq\x12V\n\rroot_or_empty\x18\x01 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x0brootOrEmpty\"\xf0\x01\n\x10MerkleSeqElement\x12H\n\x05\x66irst\x18\x01 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x05\x66irst\x12J\n\x06second\x18\x02 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x06second\x12\x46\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x04\x64\x61taBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v1.merkle_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1'
  _globals['_GENTRANSACTIONTREE']._serialized_start=90
  _globals['_GENTRANSACTIONTREE']._serialized_end=484
  _globals['_BLINDABLENODE']._serialized_start=486
  _globals['_BLINDABLENODE']._serialized_end=588
  _globals['_MERKLESEQ']._serialized_start=590
  _globals['_MERKLESEQ']._serialized_end=689
  _globals['_MERKLESEQELEMENT']._serialized_start=692
  _globals['_MERKLESEQELEMENT']._serialized_end=932
# @@protoc_insertion_point(module_scope)
