# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/sequencer/admin/v30/sequencer_version_service.proto
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
    'com/digitalasset/canton/sequencer/admin/v30/sequencer_version_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....protocol.v30 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_sequencing__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKcom/digitalasset/canton/sequencer/admin/v30/sequencer_version_service.proto\x12+com.digitalasset.canton.sequencer.admin.v30\x1a\x35\x63om/digitalasset/canton/protocol/v30/sequencing.proto\"\x8a\x02\n\x10SequencerVersion\x1ax\n\x10HandshakeRequest\x12\x64\n\x11handshake_request\x18\x01 \x01(\x0b\x32\x37.com.digitalasset.canton.protocol.v30.Handshake.RequestR\x10handshakeRequest\x1a|\n\x11HandshakeResponse\x12g\n\x12handshake_response\x18\x01 \x01(\x0b\x32\x38.com.digitalasset.canton.protocol.v30.Handshake.ResponseR\x11handshakeResponse2\xc8\x01\n\x17SequencerVersionService\x12\xac\x01\n\tHandshake\x12N.com.digitalasset.canton.sequencer.admin.v30.SequencerVersion.HandshakeRequest\x1aO.com.digitalasset.canton.sequencer.admin.v30.SequencerVersion.HandshakeResponseB\\ZZgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/admin/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.sequencer.admin.v30.sequencer_version_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZZgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/admin/v30'
  _globals['_SEQUENCERVERSION']._serialized_start=180
  _globals['_SEQUENCERVERSION']._serialized_end=446
  _globals['_SEQUENCERVERSION_HANDSHAKEREQUEST']._serialized_start=200
  _globals['_SEQUENCERVERSION_HANDSHAKEREQUEST']._serialized_end=320
  _globals['_SEQUENCERVERSION_HANDSHAKERESPONSE']._serialized_start=322
  _globals['_SEQUENCERVERSION_HANDSHAKERESPONSE']._serialized_end=446
  _globals['_SEQUENCERVERSIONSERVICE']._serialized_start=449
  _globals['_SEQUENCERVERSIONSERVICE']._serialized_end=649
# @@protoc_insertion_point(module_scope)
