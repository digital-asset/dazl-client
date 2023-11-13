# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/domain/api/v0/domain_time_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?com/digitalasset/canton/domain/api/v0/domain_time_service.proto\x12%com.digitalasset.canton.domain.api.v0\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x91\x01\n\x10\x46\x65tchTimeRequest\x12\x39\n\tdomain_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08\x64omainId\x12\x42\n\x0f\x66reshness_bound\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0e\x66reshnessBound\"M\n\x11\x46\x65tchTimeResponse\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\x87\x01\n\x10\x41waitTimeRequest\x12\x39\n\tdomain_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08\x64omainId\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp2\xf1\x01\n\x11\x44omainTimeService\x12~\n\tFetchTime\x12\x37.com.digitalasset.canton.domain.api.v0.FetchTimeRequest\x1a\x38.com.digitalasset.canton.domain.api.v0.FetchTimeResponse\x12\\\n\tAwaitTime\x12\x37.com.digitalasset.canton.domain.api.v0.AwaitTimeRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.api.v0.domain_time_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FETCHTIMEREQUEST']._serialized_start=233
  _globals['_FETCHTIMEREQUEST']._serialized_end=378
  _globals['_FETCHTIMERESPONSE']._serialized_start=380
  _globals['_FETCHTIMERESPONSE']._serialized_end=457
  _globals['_AWAITTIMEREQUEST']._serialized_start=460
  _globals['_AWAITTIMEREQUEST']._serialized_end=595
  _globals['_DOMAINTIMESERVICE']._serialized_start=598
  _globals['_DOMAINTIMESERVICE']._serialized_end=839
# @@protoc_insertion_point(module_scope)