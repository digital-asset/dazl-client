# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/participant/admin/v0/ping_pong_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDcom/digitalasset/canton/participant/admin/v0/ping_pong_service.proto\x12,com.digitalasset.canton.participant.admin.v0\"\x8c\x02\n\x0bPingRequest\x12%\n\x0etarget_parties\x18\x01 \x03(\tR\rtargetParties\x12\x1e\n\nvalidators\x18\x02 \x03(\tR\nvalidators\x12\x31\n\x14timeout_milliseconds\x18\x03 \x01(\x04R\x13timeoutMilliseconds\x12\x16\n\x06levels\x18\x04 \x01(\x04R\x06levels\x12:\n\x19grace_period_milliseconds\x18\x05 \x01(\x04R\x17gracePeriodMilliseconds\x12\x1f\n\x0bworkflow_id\x18\x06 \x01(\tR\nworkflowId\x12\x0e\n\x02id\x18\x07 \x01(\tR\x02id\"H\n\x0bPingSuccess\x12\x1b\n\tping_time\x18\x01 \x01(\x04R\x08pingTime\x12\x1c\n\tresponder\x18\x02 \x01(\tR\tresponder\"\r\n\x0bPingFailure\"\xc8\x01\n\x0cPingResponse\x12U\n\x07success\x18\x01 \x01(\x0b\x32\x39.com.digitalasset.canton.participant.admin.v0.PingSuccessH\x00R\x07success\x12U\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x39.com.digitalasset.canton.participant.admin.v0.PingFailureH\x00R\x07\x66\x61ilureB\n\n\x08response2\x8c\x01\n\x0bPingService\x12}\n\x04ping\x12\x39.com.digitalasset.canton.participant.admin.v0.PingRequest\x1a:.com.digitalasset.canton.participant.admin.v0.PingResponseB]Z[github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/participant/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.participant.admin.v0.ping_pong_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z[github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/participant/admin/v0'
  _globals['_PINGREQUEST']._serialized_start=119
  _globals['_PINGREQUEST']._serialized_end=387
  _globals['_PINGSUCCESS']._serialized_start=389
  _globals['_PINGSUCCESS']._serialized_end=461
  _globals['_PINGFAILURE']._serialized_start=463
  _globals['_PINGFAILURE']._serialized_end=476
  _globals['_PINGRESPONSE']._serialized_start=479
  _globals['_PINGRESPONSE']._serialized_end=679
  _globals['_PINGSERVICE']._serialized_start=682
  _globals['_PINGSERVICE']._serialized_end=822
# @@protoc_insertion_point(module_scope)
