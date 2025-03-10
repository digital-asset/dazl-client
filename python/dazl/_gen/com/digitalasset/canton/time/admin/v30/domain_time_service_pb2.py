# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/time/admin/v30/domain_time_service.proto
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
    'com/digitalasset/canton/time/admin/v30/domain_time_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@com/digitalasset/canton/time/admin/v30/domain_time_service.proto\x12&com.digitalasset.canton.time.admin.v30\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x91\x01\n\x10\x46\x65tchTimeRequest\x12\x39\n\tdomain_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08\x64omainId\x12\x42\n\x0f\x66reshness_bound\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0e\x66reshnessBound\"M\n\x11\x46\x65tchTimeResponse\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\x87\x01\n\x10\x41waitTimeRequest\x12\x39\n\tdomain_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08\x64omainId\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\x13\n\x11\x41waitTimeResponse2\x99\x02\n\x11\x44omainTimeService\x12\x80\x01\n\tFetchTime\x12\x38.com.digitalasset.canton.time.admin.v30.FetchTimeRequest\x1a\x39.com.digitalasset.canton.time.admin.v30.FetchTimeResponse\x12\x80\x01\n\tAwaitTime\x12\x38.com.digitalasset.canton.time.admin.v30.AwaitTimeRequest\x1a\x39.com.digitalasset.canton.time.admin.v30.AwaitTimeResponseBWZUgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/time/admin/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.time.admin.v30.domain_time_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZUgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/time/admin/v30'
  _globals['_FETCHTIMEREQUEST']._serialized_start=206
  _globals['_FETCHTIMEREQUEST']._serialized_end=351
  _globals['_FETCHTIMERESPONSE']._serialized_start=353
  _globals['_FETCHTIMERESPONSE']._serialized_end=430
  _globals['_AWAITTIMEREQUEST']._serialized_start=433
  _globals['_AWAITTIMEREQUEST']._serialized_end=568
  _globals['_AWAITTIMERESPONSE']._serialized_start=570
  _globals['_AWAITTIMERESPONSE']._serialized_end=589
  _globals['_DOMAINTIMESERVICE']._serialized_start=592
  _globals['_DOMAINTIMESERVICE']._serialized_end=873
# @@protoc_insertion_point(module_scope)
