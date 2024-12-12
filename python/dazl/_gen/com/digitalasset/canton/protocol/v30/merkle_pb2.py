# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v30/merkle.proto
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
    'com/digitalasset/canton/protocol/v30/merkle.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1com/digitalasset/canton/protocol/v30/merkle.proto\x12$com.digitalasset.canton.protocol.v30\"\x8e\x03\n\x12GenTransactionTree\x12\x62\n\x12submitter_metadata\x18\x01 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x11submitterMetadata\x12\\\n\x0f\x63ommon_metadata\x18\x02 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x0e\x63ommonMetadata\x12\x66\n\x14participant_metadata\x18\x03 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x13participantMetadata\x12N\n\nroot_views\x18\x04 \x01(\x0b\x32/.com.digitalasset.canton.protocol.v30.MerkleSeqR\trootViews\"f\n\rBlindableNode\x12\x1e\n\tunblinded\x18\x01 \x01(\x0cH\x00R\tunblinded\x12#\n\x0c\x62linded_hash\x18\x02 \x01(\x0cH\x00R\x0b\x62lindedHashB\x10\n\x0e\x62linded_or_not\"d\n\tMerkleSeq\x12W\n\rroot_or_empty\x18\x01 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x0brootOrEmpty\"\xf3\x01\n\x10MerkleSeqElement\x12I\n\x05\x66irst\x18\x01 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x05\x66irst\x12K\n\x06second\x18\x02 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x06second\x12G\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v30.BlindableNodeR\x04\x64\x61taBUZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v30.merkle_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30'
  _globals['_GENTRANSACTIONTREE']._serialized_start=92
  _globals['_GENTRANSACTIONTREE']._serialized_end=490
  _globals['_BLINDABLENODE']._serialized_start=492
  _globals['_BLINDABLENODE']._serialized_end=594
  _globals['_MERKLESEQ']._serialized_start=596
  _globals['_MERKLESEQ']._serialized_end=696
  _globals['_MERKLESEQELEMENT']._serialized_start=699
  _globals['_MERKLESEQELEMENT']._serialized_end=942
# @@protoc_insertion_point(module_scope)