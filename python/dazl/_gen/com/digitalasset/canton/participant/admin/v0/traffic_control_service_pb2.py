# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/participant/admin/v0/traffic_control_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....traffic.v0 import member_traffic_status_pb2 as com_dot_digitalasset_dot_canton_dot_traffic_dot_v0_dot_member__traffic__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJcom/digitalasset/canton/participant/admin/v0/traffic_control_service.proto\x12,com.digitalasset.canton.participant.admin.v0\x1a>com/digitalasset/canton/traffic/v0/member_traffic_status.proto\"9\n\x1aTrafficControlStateRequest\x12\x1b\n\tdomain_id\x18\x01 \x01(\tR\x08\x64omainId\"{\n\x1bTrafficControlStateResponse\x12\\\n\rtraffic_state\x18\x01 \x01(\x0b\x32\x37.com.digitalasset.canton.traffic.v0.MemberTrafficStatusR\x0ctrafficState2\xc4\x01\n\x15TrafficControlService\x12\xaa\x01\n\x13TrafficControlState\x12H.com.digitalasset.canton.participant.admin.v0.TrafficControlStateRequest\x1aI.com.digitalasset.canton.participant.admin.v0.TrafficControlStateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.participant.admin.v0.traffic_control_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRAFFICCONTROLSTATEREQUEST']._serialized_start=188
  _globals['_TRAFFICCONTROLSTATEREQUEST']._serialized_end=245
  _globals['_TRAFFICCONTROLSTATERESPONSE']._serialized_start=247
  _globals['_TRAFFICCONTROLSTATERESPONSE']._serialized_end=370
  _globals['_TRAFFICCONTROLSERVICE']._serialized_start=373
  _globals['_TRAFFICCONTROLSERVICE']._serialized_end=569
# @@protoc_insertion_point(module_scope)
