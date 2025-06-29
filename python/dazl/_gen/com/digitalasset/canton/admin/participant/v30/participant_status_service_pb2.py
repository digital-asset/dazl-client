# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/admin/participant/v30/participant_status_service.proto
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
    'com/digitalasset/canton/admin/participant/v30/participant_status_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...health.v30 import status_service_pb2 as com_dot_digitalasset_dot_canton_dot_admin_dot_health_dot_v30_dot_status__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNcom/digitalasset/canton/admin/participant/v30/participant_status_service.proto\x12-com.digitalasset.canton.admin.participant.v30\x1a=com/digitalasset/canton/admin/health/v30/status_service.proto\"\x1a\n\x18ParticipantStatusRequest\"\xf1\x01\n\x15\x43onnectedSynchronizer\x12\'\n\x0fsynchronizer_id\x18\x01 \x01(\tR\x0esynchronizerId\x12\x63\n\x06health\x18\x02 \x01(\x0e\x32K.com.digitalasset.canton.admin.participant.v30.ConnectedSynchronizer.HealthR\x06health\"J\n\x06Health\x12\x16\n\x12HEALTH_UNSPECIFIED\x10\x00\x12\x12\n\x0eHEALTH_HEALTHY\x10\x01\x12\x14\n\x10HEALTH_UNHEALTHY\x10\x02\"\xdf\x04\n\x19ParticipantStatusResponse\x12\x82\x01\n\x06status\x18\x01 \x01(\x0b\x32h.com.digitalasset.canton.admin.participant.v30.ParticipantStatusResponse.ParticipantStatusResponseStatusH\x00R\x06status\x12\x63\n\x0fnot_initialized\x18\x02 \x01(\x0b\x32\x38.com.digitalasset.canton.admin.health.v30.NotInitializedH\x00R\x0enotInitialized\x1a\xcf\x02\n\x1fParticipantStatusResponseStatus\x12U\n\rcommon_status\x18\x01 \x01(\x0b\x32\x30.com.digitalasset.canton.admin.health.v30.StatusR\x0c\x63ommonStatus\x12}\n\x17\x63onnected_synchronizers\x18\x02 \x03(\x0b\x32\x44.com.digitalasset.canton.admin.participant.v30.ConnectedSynchronizerR\x16\x63onnectedSynchronizers\x12\x16\n\x06\x61\x63tive\x18\x03 \x01(\x08R\x06\x61\x63tive\x12>\n\x1bsupported_protocol_versions\x18\x04 \x03(\x05R\x19supportedProtocolVersionsB\x06\n\x04kind2\xc3\x01\n\x18ParticipantStatusService\x12\xa6\x01\n\x11ParticipantStatus\x12G.com.digitalasset.canton.admin.participant.v30.ParticipantStatusRequest\x1aH.com.digitalasset.canton.admin.participant.v30.ParticipantStatusResponseB^Z\\github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/admin/participant/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.admin.participant.v30.participant_status_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/admin/participant/v30'
  _globals['_PARTICIPANTSTATUSREQUEST']._serialized_start=192
  _globals['_PARTICIPANTSTATUSREQUEST']._serialized_end=218
  _globals['_CONNECTEDSYNCHRONIZER']._serialized_start=221
  _globals['_CONNECTEDSYNCHRONIZER']._serialized_end=462
  _globals['_CONNECTEDSYNCHRONIZER_HEALTH']._serialized_start=388
  _globals['_CONNECTEDSYNCHRONIZER_HEALTH']._serialized_end=462
  _globals['_PARTICIPANTSTATUSRESPONSE']._serialized_start=465
  _globals['_PARTICIPANTSTATUSRESPONSE']._serialized_end=1072
  _globals['_PARTICIPANTSTATUSRESPONSE_PARTICIPANTSTATUSRESPONSESTATUS']._serialized_start=729
  _globals['_PARTICIPANTSTATUSRESPONSE_PARTICIPANTSTATUSRESPONSESTATUS']._serialized_end=1064
  _globals['_PARTICIPANTSTATUSSERVICE']._serialized_start=1075
  _globals['_PARTICIPANTSTATUSSERVICE']._serialized_end=1270
# @@protoc_insertion_point(module_scope)
