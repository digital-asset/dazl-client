# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/participant/admin/v0/pruning_service.proto
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
    'com/digitalasset/canton/participant/admin/v0/pruning_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....pruning.admin.v0 import pruning_pb2 as com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBcom/digitalasset/canton/participant/admin/v0/pruning_service.proto\x12,com.digitalasset.canton.participant.admin.v0\x1a\x36\x63om/digitalasset/canton/pruning/admin/v0/pruning.proto\x1a\x1fgoogle/protobuf/timestamp.proto\".\n\x0cPruneRequest\x12\x1e\n\x0bprune_up_to\x18\x01 \x01(\tR\tpruneUpTo\"\x0f\n\rPruneResponse\"z\n\x1bGetSafePruningOffsetRequest\x12<\n\x0c\x62\x65\x66ore_or_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nbeforeOrAt\x12\x1d\n\nledger_end\x18\x02 \x01(\tR\tledgerEnd\"\x8b\x02\n\x1cGetSafePruningOffsetResponse\x12\x30\n\x13safe_pruning_offset\x18\x01 \x01(\tH\x00R\x11safePruningOffset\x12\x95\x01\n\x16no_safe_pruning_offset\x18\x02 \x01(\x0b\x32^.com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetResponse.NoSafePruningOffsetH\x00R\x13noSafePruningOffset\x1a\x15\n\x13NoSafePruningOffsetB\n\n\x08response2\x83\x0c\n\x0ePruningService\x12\x80\x01\n\x05Prune\x12:.com.digitalasset.canton.participant.admin.v0.PruneRequest\x1a;.com.digitalasset.canton.participant.admin.v0.PruneResponse\x12\xad\x01\n\x14GetSafePruningOffset\x12I.com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetRequest\x1aJ.com.digitalasset.canton.participant.admin.v0.GetSafePruningOffsetResponse\x12\x8c\x01\n\x0bSetSchedule\x12=.com.digitalasset.canton.pruning.admin.v0.SetSchedule.Request\x1a>.com.digitalasset.canton.pruning.admin.v0.SetSchedule.Response\x12\xad\x01\n\x16SetParticipantSchedule\x12H.com.digitalasset.canton.pruning.admin.v0.SetParticipantSchedule.Request\x1aI.com.digitalasset.canton.pruning.admin.v0.SetParticipantSchedule.Response\x12\x80\x01\n\x07SetCron\x12\x39.com.digitalasset.canton.pruning.admin.v0.SetCron.Request\x1a:.com.digitalasset.canton.pruning.admin.v0.SetCron.Response\x12\x95\x01\n\x0eSetMaxDuration\x12@.com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Request\x1a\x41.com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Response\x12\x8f\x01\n\x0cSetRetention\x12>.com.digitalasset.canton.pruning.admin.v0.SetRetention.Request\x1a?.com.digitalasset.canton.pruning.admin.v0.SetRetention.Response\x12\x92\x01\n\rClearSchedule\x12?.com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Request\x1a@.com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Response\x12\x8c\x01\n\x0bGetSchedule\x12=.com.digitalasset.canton.pruning.admin.v0.GetSchedule.Request\x1a>.com.digitalasset.canton.pruning.admin.v0.GetSchedule.Response\x12\xad\x01\n\x16GetParticipantSchedule\x12H.com.digitalasset.canton.pruning.admin.v0.GetParticipantSchedule.Request\x1aI.com.digitalasset.canton.pruning.admin.v0.GetParticipantSchedule.ResponseB]Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.participant.admin.v0.pruning_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0'
  _globals['_PRUNEREQUEST']._serialized_start=205
  _globals['_PRUNEREQUEST']._serialized_end=251
  _globals['_PRUNERESPONSE']._serialized_start=253
  _globals['_PRUNERESPONSE']._serialized_end=268
  _globals['_GETSAFEPRUNINGOFFSETREQUEST']._serialized_start=270
  _globals['_GETSAFEPRUNINGOFFSETREQUEST']._serialized_end=392
  _globals['_GETSAFEPRUNINGOFFSETRESPONSE']._serialized_start=395
  _globals['_GETSAFEPRUNINGOFFSETRESPONSE']._serialized_end=662
  _globals['_GETSAFEPRUNINGOFFSETRESPONSE_NOSAFEPRUNINGOFFSET']._serialized_start=629
  _globals['_GETSAFEPRUNINGOFFSETRESPONSE_NOSAFEPRUNINGOFFSET']._serialized_end=650
  _globals['_PRUNINGSERVICE']._serialized_start=665
  _globals['_PRUNINGSERVICE']._serialized_end=2204
# @@protoc_insertion_point(module_scope)
