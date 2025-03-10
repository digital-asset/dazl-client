# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/checkpoint.proto
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
    'com/daml/ledger/api/v2/checkpoint.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'com/daml/ledger/api/v2/checkpoint.proto\x12\x16\x63om.daml.ledger.api.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"a\n\nCheckpoint\x12;\n\x0brecord_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nrecordTime\x12\x16\n\x06offset\x18\x02 \x01(\tR\x06offsetB\x8e\x01\n\x16\x63om.daml.ledger.api.v2B\x14\x43heckpointOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.checkpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\024CheckpointOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_CHECKPOINT']._serialized_start=100
  _globals['_CHECKPOINT']._serialized_end=197
# @@protoc_insertion_point(module_scope)
