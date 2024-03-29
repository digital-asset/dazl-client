# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/pruning/admin/v0/pruning.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6com/digitalasset/canton/pruning/admin/v0/pruning.proto\x12(com.digitalasset.canton.pruning.admin.v0\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"{\n\x0bSetSchedule\x1a`\n\x07Request\x12U\n\x08schedule\x18\x01 \x01(\x0b\x32\x39.com.digitalasset.canton.pruning.admin.v0.PruningScheduleR\x08schedule\x1a\n\n\x08Response\"{\n\x0bGetSchedule\x1a\t\n\x07Request\x1a\x61\n\x08Response\x12U\n\x08schedule\x18\x01 \x01(\x0b\x32\x39.com.digitalasset.canton.pruning.admin.v0.PruningScheduleR\x08schedule\"\x9c\x01\n\x0fPruningSchedule\x12\x12\n\x04\x63ron\x18\x01 \x01(\tR\x04\x63ron\x12<\n\x0cmax_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bmaxDuration\x12\x37\n\tretention\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\tretention\"&\n\rClearSchedule\x1a\t\n\x07Request\x1a\n\n\x08Response\"4\n\x07SetCron\x1a\x1d\n\x07Request\x12\x12\n\x04\x63ron\x18\x01 \x01(\tR\x04\x63ron\x1a\n\n\x08Response\"e\n\x0eSetMaxDuration\x1aG\n\x07Request\x12<\n\x0cmax_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bmaxDuration\x1a\n\n\x08Response\"^\n\x0cSetRetention\x1a\x42\n\x07Request\x12\x37\n\tretention\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\tretention\x1a\n\n\x08Response\"\x7f\n\x16LocatePruningTimestamp\x1a\x1f\n\x07Request\x12\x14\n\x05index\x18\x01 \x01(\x05R\x05index\x1a\x44\n\x08Response\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestampBYZWgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/pruning/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.pruning.admin.v0.pruning_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZWgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/pruning/admin/v0'
  _globals['_SETSCHEDULE']._serialized_start=165
  _globals['_SETSCHEDULE']._serialized_end=288
  _globals['_SETSCHEDULE_REQUEST']._serialized_start=180
  _globals['_SETSCHEDULE_REQUEST']._serialized_end=276
  _globals['_SETSCHEDULE_RESPONSE']._serialized_start=278
  _globals['_SETSCHEDULE_RESPONSE']._serialized_end=288
  _globals['_GETSCHEDULE']._serialized_start=290
  _globals['_GETSCHEDULE']._serialized_end=413
  _globals['_GETSCHEDULE_REQUEST']._serialized_start=180
  _globals['_GETSCHEDULE_REQUEST']._serialized_end=189
  _globals['_GETSCHEDULE_RESPONSE']._serialized_start=316
  _globals['_GETSCHEDULE_RESPONSE']._serialized_end=413
  _globals['_PRUNINGSCHEDULE']._serialized_start=416
  _globals['_PRUNINGSCHEDULE']._serialized_end=572
  _globals['_CLEARSCHEDULE']._serialized_start=574
  _globals['_CLEARSCHEDULE']._serialized_end=612
  _globals['_CLEARSCHEDULE_REQUEST']._serialized_start=180
  _globals['_CLEARSCHEDULE_REQUEST']._serialized_end=189
  _globals['_CLEARSCHEDULE_RESPONSE']._serialized_start=278
  _globals['_CLEARSCHEDULE_RESPONSE']._serialized_end=288
  _globals['_SETCRON']._serialized_start=614
  _globals['_SETCRON']._serialized_end=666
  _globals['_SETCRON_REQUEST']._serialized_start=625
  _globals['_SETCRON_REQUEST']._serialized_end=654
  _globals['_SETCRON_RESPONSE']._serialized_start=278
  _globals['_SETCRON_RESPONSE']._serialized_end=288
  _globals['_SETMAXDURATION']._serialized_start=668
  _globals['_SETMAXDURATION']._serialized_end=769
  _globals['_SETMAXDURATION_REQUEST']._serialized_start=686
  _globals['_SETMAXDURATION_REQUEST']._serialized_end=757
  _globals['_SETMAXDURATION_RESPONSE']._serialized_start=278
  _globals['_SETMAXDURATION_RESPONSE']._serialized_end=288
  _globals['_SETRETENTION']._serialized_start=771
  _globals['_SETRETENTION']._serialized_end=865
  _globals['_SETRETENTION_REQUEST']._serialized_start=787
  _globals['_SETRETENTION_REQUEST']._serialized_end=853
  _globals['_SETRETENTION_RESPONSE']._serialized_start=278
  _globals['_SETRETENTION_RESPONSE']._serialized_end=288
  _globals['_LOCATEPRUNINGTIMESTAMP']._serialized_start=867
  _globals['_LOCATEPRUNINGTIMESTAMP']._serialized_end=994
  _globals['_LOCATEPRUNINGTIMESTAMP_REQUEST']._serialized_start=893
  _globals['_LOCATEPRUNINGTIMESTAMP_REQUEST']._serialized_end=924
  _globals['_LOCATEPRUNINGTIMESTAMP_RESPONSE']._serialized_start=926
  _globals['_LOCATEPRUNINGTIMESTAMP_RESPONSE']._serialized_end=994
# @@protoc_insertion_point(module_scope)
