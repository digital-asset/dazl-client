# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/testing/time_service.proto
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
    'com/daml/ledger/api/v2/testing/time_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1com/daml/ledger/api/v2/testing/time_service.proto\x12\x1e\x63om.daml.ledger.api.v2.testing\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x10\n\x0eGetTimeRequest\"P\n\x0fGetTimeResponse\x12=\n\x0c\x63urrent_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63urrentTime\"\x86\x01\n\x0eSetTimeRequest\x12=\n\x0c\x63urrent_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63urrentTime\x12\x35\n\x08new_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07newTime2\xcc\x01\n\x0bTimeService\x12j\n\x07GetTime\x12..com.daml.ledger.api.v2.testing.GetTimeRequest\x1a/.com.daml.ledger.api.v2.testing.GetTimeResponse\x12Q\n\x07SetTime\x12..com.daml.ledger.api.v2.testing.SetTimeRequest\x1a\x16.google.protobuf.EmptyB\xa7\x01\n\x1e\x63om.daml.ledger.api.v2.testingB\x15TimeServiceOuterClassZMgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/testing\xaa\x02\x1e\x43om.Daml.Ledger.Api.V2.Testingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.testing.time_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.daml.ledger.api.v2.testingB\025TimeServiceOuterClassZMgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/testing\252\002\036Com.Daml.Ledger.Api.V2.Testing'
  _globals['_GETTIMEREQUEST']._serialized_start=147
  _globals['_GETTIMEREQUEST']._serialized_end=163
  _globals['_GETTIMERESPONSE']._serialized_start=165
  _globals['_GETTIMERESPONSE']._serialized_end=245
  _globals['_SETTIMEREQUEST']._serialized_start=248
  _globals['_SETTIMEREQUEST']._serialized_end=382
  _globals['_TIMESERVICE']._serialized_start=385
  _globals['_TIMESERVICE']._serialized_end=589
# @@protoc_insertion_point(module_scope)
