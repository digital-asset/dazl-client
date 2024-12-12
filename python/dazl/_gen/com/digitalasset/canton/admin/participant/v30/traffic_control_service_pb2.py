# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/admin/participant/v30/traffic_control_service.proto
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
    'com/digitalasset/canton/admin/participant/v30/traffic_control_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKcom/digitalasset/canton/admin/participant/v30/traffic_control_service.proto\x12-com.digitalasset.canton.admin.participant.v30\x1a\x1egoogle/protobuf/wrappers.proto\"9\n\x1aTrafficControlStateRequest\x12\x1b\n\tdomain_id\x18\x01 \x01(\tR\x08\x64omainId\"\x7f\n\x1bTrafficControlStateResponse\x12`\n\rtraffic_state\x18\x01 \x01(\x0b\x32;.com.digitalasset.canton.admin.participant.v30.TrafficStateR\x0ctrafficState\"\xb4\x02\n\x0cTrafficState\x12\x36\n\x17\x65xtra_traffic_purchased\x18\x01 \x01(\x03R\x15\x65xtraTrafficPurchased\x12\x34\n\x16\x65xtra_traffic_consumed\x18\x02 \x01(\x03R\x14\x65xtraTrafficConsumed\x12\x34\n\x16\x62\x61se_traffic_remainder\x18\x03 \x01(\x03R\x14\x62\x61seTrafficRemainder\x12,\n\x12last_consumed_cost\x18\x04 \x01(\x04R\x10lastConsumedCost\x12\x1c\n\ttimestamp\x18\x05 \x01(\x03R\ttimestamp\x12\x34\n\x06serial\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x06serial2\xc6\x01\n\x15TrafficControlService\x12\xac\x01\n\x13TrafficControlState\x12I.com.digitalasset.canton.admin.participant.v30.TrafficControlStateRequest\x1aJ.com.digitalasset.canton.admin.participant.v30.TrafficControlStateResponseB^Z\\github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/admin/participant/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.admin.participant.v30.traffic_control_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/admin/participant/v30'
  _globals['_TRAFFICCONTROLSTATEREQUEST']._serialized_start=158
  _globals['_TRAFFICCONTROLSTATEREQUEST']._serialized_end=215
  _globals['_TRAFFICCONTROLSTATERESPONSE']._serialized_start=217
  _globals['_TRAFFICCONTROLSTATERESPONSE']._serialized_end=344
  _globals['_TRAFFICSTATE']._serialized_start=347
  _globals['_TRAFFICSTATE']._serialized_end=655
  _globals['_TRAFFICCONTROLSERVICE']._serialized_start=658
  _globals['_TRAFFICCONTROLSERVICE']._serialized_end=856
# @@protoc_insertion_point(module_scope)