# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v1/trace_context.proto
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
    'com/daml/ledger/api/v1/trace_context.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*com/daml/ledger/api/v1/trace_context.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\x1egoogle/protobuf/wrappers.proto\"\x8c\x01\n\x0cTraceContext\x12>\n\x0btraceparent\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0btraceparent\x12<\n\ntracestate\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\ntracestateBGZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.trace_context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1'
  _globals['_TRACECONTEXT']._serialized_start=103
  _globals['_TRACECONTEXT']._serialized_end=243
# @@protoc_insertion_point(module_scope)
