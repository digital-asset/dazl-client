# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/command_completion_service.proto
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
    'com/daml/ledger/api/v2/command_completion_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import completion_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_completion__pb2
from . import offset_checkpoint_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_offset__checkpoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7com/daml/ledger/api/v2/command_completion_service.proto\x12\x16\x63om.daml.ledger.api.v2\x1a\'com/daml/ledger/api/v2/completion.proto\x1a.com/daml/ledger/api/v2/offset_checkpoint.proto\"u\n\x17\x43ompletionStreamRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x18\n\x07parties\x18\x02 \x03(\tR\x07parties\x12\'\n\x0f\x62\x65gin_exclusive\x18\x03 \x01(\x03R\x0e\x62\x65ginExclusive\"\xd0\x01\n\x18\x43ompletionStreamResponse\x12\x44\n\ncompletion\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v2.CompletionH\x00R\ncompletion\x12W\n\x11offset_checkpoint\x18\x02 \x01(\x0b\x32(.com.daml.ledger.api.v2.OffsetCheckpointH\x00R\x10offsetCheckpointB\x15\n\x13\x63ompletion_response2\x93\x01\n\x18\x43ommandCompletionService\x12w\n\x10\x43ompletionStream\x12/.com.daml.ledger.api.v2.CompletionStreamRequest\x1a\x30.com.daml.ledger.api.v2.CompletionStreamResponse0\x01\x42\x9c\x01\n\x16\x63om.daml.ledger.api.v2B\"CommandCompletionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.command_completion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\"CommandCompletionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_COMPLETIONSTREAMREQUEST']._serialized_start=172
  _globals['_COMPLETIONSTREAMREQUEST']._serialized_end=289
  _globals['_COMPLETIONSTREAMRESPONSE']._serialized_start=292
  _globals['_COMPLETIONSTREAMRESPONSE']._serialized_end=500
  _globals['_COMMANDCOMPLETIONSERVICE']._serialized_start=503
  _globals['_COMMANDCOMPLETIONSERVICE']._serialized_end=650
# @@protoc_insertion_point(module_scope)
