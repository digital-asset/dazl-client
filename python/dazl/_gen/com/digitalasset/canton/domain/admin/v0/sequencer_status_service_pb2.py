# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/domain/admin/v0/sequencer_status_service.proto
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
    'com/digitalasset/canton/domain/admin/v0/sequencer_status_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....health.admin.v0 import status_service_pb2 as com_dot_digitalasset_dot_canton_dot_health_dot_admin_dot_v0_dot_status__service__pb2
from ....health.admin.v1 import status_service_pb2 as com_dot_digitalasset_dot_canton_dot_health_dot_admin_dot_v1_dot_status__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFcom/digitalasset/canton/domain/admin/v0/sequencer_status_service.proto\x12\'com.digitalasset.canton.domain.admin.v0\x1a<com/digitalasset/canton/health/admin/v0/status_service.proto\x1a<com/digitalasset/canton/health/admin/v1/status_service.proto\"\x18\n\x16SequencerStatusRequest\"\xba\x06\n\x17SequencerStatusResponse\x12x\n\x06status\x18\x01 \x01(\x0b\x32^.com.digitalasset.canton.domain.admin.v0.SequencerStatusResponse.SequencerStatusResponseStatusH\x00R\x06status\x12\x66\n\x0bunavailable\x18\x02 \x01(\x0b\x32\x42.com.digitalasset.canton.health.admin.v0.NodeStatus.NotInitializedH\x00R\x0bunavailable\x12L\n\x07\x66\x61ilure\x18\x03 \x01(\x0b\x32\x30.com.digitalasset.canton.health.admin.v1.FailureH\x00R\x07\x66\x61ilure\x1a\xe6\x03\n\x1dSequencerStatusResponseStatus\x12T\n\rcommon_status\x18\x01 \x01(\x0b\x32/.com.digitalasset.canton.health.admin.v1.StatusR\x0c\x63ommonStatus\x12<\n\x1a\x63onnected_participants_uid\x18\x02 \x03(\tR\x18\x63onnectedParticipantsUid\x12\x36\n\x17\x63onnected_mediators_uid\x18\x07 \x03(\tR\x15\x63onnectedMediatorsUid\x12\\\n\tsequencer\x18\x03 \x01(\x0b\x32>.com.digitalasset.canton.health.admin.v0.SequencerHealthStatusR\tsequencer\x12\x1b\n\tdomain_id\x18\x04 \x01(\tR\x08\x64omainId\x12S\n\x05\x61\x64min\x18\x05 \x01(\x0b\x32=.com.digitalasset.canton.health.admin.v0.SequencerAdminStatusR\x05\x61\x64min\x12)\n\x10protocol_version\x18\x06 \x01(\x05R\x0fprotocolVersionB\x06\n\x04kind2\xaf\x01\n\x16SequencerStatusService\x12\x94\x01\n\x0fSequencerStatus\x12?.com.digitalasset.canton.domain.admin.v0.SequencerStatusRequest\x1a@.com.digitalasset.canton.domain.admin.v0.SequencerStatusResponseBXZVgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.admin.v0.sequencer_status_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZVgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/admin/v0'
  _globals['_SEQUENCERSTATUSREQUEST']._serialized_start=239
  _globals['_SEQUENCERSTATUSREQUEST']._serialized_end=263
  _globals['_SEQUENCERSTATUSRESPONSE']._serialized_start=266
  _globals['_SEQUENCERSTATUSRESPONSE']._serialized_end=1092
  _globals['_SEQUENCERSTATUSRESPONSE_SEQUENCERSTATUSRESPONSESTATUS']._serialized_start=598
  _globals['_SEQUENCERSTATUSRESPONSE_SEQUENCERSTATUSRESPONSESTATUS']._serialized_end=1084
  _globals['_SEQUENCERSTATUSSERVICE']._serialized_start=1095
  _globals['_SEQUENCERSTATUSSERVICE']._serialized_end=1270
# @@protoc_insertion_point(module_scope)
