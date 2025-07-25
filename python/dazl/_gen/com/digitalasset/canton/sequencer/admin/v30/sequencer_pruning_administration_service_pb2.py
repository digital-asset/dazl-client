# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/sequencer/admin/v30/sequencer_pruning_administration_service.proto
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
    'com/digitalasset/canton/sequencer/admin/v30/sequencer_pruning_administration_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....admin.pruning.v30 import pruning_pb2 as com_dot_digitalasset_dot_canton_dot_admin_dot_pruning_dot_v30_dot_pruning__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nZcom/digitalasset/canton/sequencer/admin/v30/sequencer_pruning_administration_service.proto\x12+com.digitalasset.canton.sequencer.admin.v30\x1a\x37\x63om/digitalasset/canton/admin/pruning/v30/pruning.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"H\n\x0cPruneRequest\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\")\n\rPruneResponse\x12\x18\n\x07\x64\x65tails\x18\x01 \x01(\tR\x07\x64\x65tails2\xb7\t\n%SequencerPruningAdministrationService\x12~\n\x05Prune\x12\x39.com.digitalasset.canton.sequencer.admin.v30.PruneRequest\x1a:.com.digitalasset.canton.sequencer.admin.v30.PruneResponse\x12\x8c\x01\n\x0bSetSchedule\x12=.com.digitalasset.canton.admin.pruning.v30.SetScheduleRequest\x1a>.com.digitalasset.canton.admin.pruning.v30.SetScheduleResponse\x12\x80\x01\n\x07SetCron\x12\x39.com.digitalasset.canton.admin.pruning.v30.SetCronRequest\x1a:.com.digitalasset.canton.admin.pruning.v30.SetCronResponse\x12\x95\x01\n\x0eSetMaxDuration\x12@.com.digitalasset.canton.admin.pruning.v30.SetMaxDurationRequest\x1a\x41.com.digitalasset.canton.admin.pruning.v30.SetMaxDurationResponse\x12\x8f\x01\n\x0cSetRetention\x12>.com.digitalasset.canton.admin.pruning.v30.SetRetentionRequest\x1a?.com.digitalasset.canton.admin.pruning.v30.SetRetentionResponse\x12\x92\x01\n\rClearSchedule\x12?.com.digitalasset.canton.admin.pruning.v30.ClearScheduleRequest\x1a@.com.digitalasset.canton.admin.pruning.v30.ClearScheduleResponse\x12\x8c\x01\n\x0bGetSchedule\x12=.com.digitalasset.canton.admin.pruning.v30.GetScheduleRequest\x1a>.com.digitalasset.canton.admin.pruning.v30.GetScheduleResponse\x12\xad\x01\n\x16LocatePruningTimestamp\x12H.com.digitalasset.canton.admin.pruning.v30.LocatePruningTimestampRequest\x1aI.com.digitalasset.canton.admin.pruning.v30.LocatePruningTimestampResponseB\\ZZgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/admin/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.sequencer.admin.v30.sequencer_pruning_administration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZZgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/admin/v30'
  _globals['_PRUNEREQUEST']._serialized_start=229
  _globals['_PRUNEREQUEST']._serialized_end=301
  _globals['_PRUNERESPONSE']._serialized_start=303
  _globals['_PRUNERESPONSE']._serialized_end=344
  _globals['_SEQUENCERPRUNINGADMINISTRATIONSERVICE']._serialized_start=347
  _globals['_SEQUENCERPRUNINGADMINISTRATIONSERVICE']._serialized_end=1554
# @@protoc_insertion_point(module_scope)
