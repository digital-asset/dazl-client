# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto
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
    'com/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNcom/digitalasset/canton/domain/admin/v0/sequencer_administration_service.proto\x12\'com.digitalasset.canton.domain.admin.v0\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd3\x01\n\x15SequencerMemberStatus\x12\x16\n\x06member\x18\x01 \x01(\tR\x06member\x12?\n\rregistered_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cregisteredAt\x12G\n\x11last_acknowledged\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10lastAcknowledged\x12\x18\n\x07\x65nabled\x18\x04 \x01(\x08R\x07\x65nabled\"\xf6\x01\n\x16SequencerPruningStatus\x12,\n\x03now\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03now\x12T\n\x18\x65\x61rliest_event_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x16\x65\x61rliestEventTimestamp\x12X\n\x07members\x18\x03 \x03(\x0b\x32>.com.digitalasset.canton.domain.admin.v0.SequencerMemberStatusR\x07members2\x8a\x01\n\x1eSequencerAdministrationService\x12h\n\rPruningStatus\x12\x16.google.protobuf.Empty\x1a?.com.digitalasset.canton.domain.admin.v0.SequencerPruningStatusBXZVgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/domain/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.admin.v0.sequencer_administration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZVgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/domain/admin/v0'
  _globals['_SEQUENCERMEMBERSTATUS']._serialized_start=186
  _globals['_SEQUENCERMEMBERSTATUS']._serialized_end=397
  _globals['_SEQUENCERPRUNINGSTATUS']._serialized_start=400
  _globals['_SEQUENCERPRUNINGSTATUS']._serialized_end=646
  _globals['_SEQUENCERADMINISTRATIONSERVICE']._serialized_start=649
  _globals['_SEQUENCERADMINISTRATIONSERVICE']._serialized_end=787
# @@protoc_insertion_point(module_scope)
