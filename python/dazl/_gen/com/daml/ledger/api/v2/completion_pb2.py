# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/completion.proto
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
    'com/daml/ledger/api/v2/completion.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import offset_checkpoint_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_offset__checkpoint__pb2
from . import trace_context_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_trace__context__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'com/daml/ledger/api/v2/completion.proto\x12\x16\x63om.daml.ledger.api.v2\x1a.com/daml/ledger/api/v2/offset_checkpoint.proto\x1a*com/daml/ledger/api/v2/trace_context.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\"\xa0\x04\n\nCompletion\x12\x1d\n\ncommand_id\x18\x01 \x01(\tR\tcommandId\x12*\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\x12\x1b\n\tupdate_id\x18\x03 \x01(\tR\x08updateId\x12%\n\x0e\x61pplication_id\x18\x04 \x01(\tR\rapplicationId\x12\x15\n\x06\x61\x63t_as\x18\x05 \x03(\tR\x05\x61\x63tAs\x12#\n\rsubmission_id\x18\x06 \x01(\tR\x0csubmissionId\x12\x33\n\x14\x64\x65\x64uplication_offset\x18\x07 \x01(\x03H\x00R\x13\x64\x65\x64uplicationOffset\x12R\n\x16\x64\x65\x64uplication_duration\x18\x08 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00R\x15\x64\x65\x64uplicationDuration\x12I\n\rtrace_context\x18\t \x01(\x0b\x32$.com.daml.ledger.api.v2.TraceContextR\x0ctraceContext\x12\x16\n\x06offset\x18\n \x01(\x03R\x06offset\x12\x43\n\x0b\x64omain_time\x18\x0b \x01(\x0b\x32\".com.daml.ledger.api.v2.DomainTimeR\ndomainTimeB\x16\n\x14\x64\x65\x64uplication_periodB\x8e\x01\n\x16\x63om.daml.ledger.api.v2B\x14\x43ompletionOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.completion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\024CompletionOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_COMPLETION']._serialized_start=217
  _globals['_COMPLETION']._serialized_end=761
# @@protoc_insertion_point(module_scope)