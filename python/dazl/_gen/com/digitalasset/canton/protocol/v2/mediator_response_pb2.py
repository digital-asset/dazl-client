# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v2/mediator_response.proto
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
    'com/digitalasset/canton/protocol/v2/mediator_response.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..v1 import mediator_response_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_mediator__response__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;com/digitalasset/canton/protocol/v2/mediator_response.proto\x12#com.digitalasset.canton.protocol.v2\x1a;com/digitalasset/canton/protocol/v1/mediator_response.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x84\x03\n\x10MediatorResponse\x12\x39\n\nrequest_id\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\trequestId\x12\x16\n\x06sender\x18\x02 \x01(\tR\x06sender\x12V\n\rlocal_verdict\x18\x04 \x01(\x0b\x32\x31.com.digitalasset.canton.protocol.v1.LocalVerdictR\x0clocalVerdict\x12\x1b\n\troot_hash\x18\x05 \x01(\x0cR\x08rootHash\x12-\n\x12\x63onfirming_parties\x18\x06 \x03(\tR\x11\x63onfirmingParties\x12\x1b\n\tdomain_id\x18\x07 \x01(\tR\x08\x64omainId\x12V\n\rview_position\x18\x08 \x01(\x0b\x32\x31.com.digitalasset.canton.protocol.v2.ViewPositionR\x0cviewPositionJ\x04\x08\x03\x10\x04\"_\n\x0cViewPosition\x12O\n\x08position\x18\x01 \x03(\x0b\x32\x33.com.digitalasset.canton.protocol.v2.MerkleSeqIndexR\x08position\"+\n\x0eMerkleSeqIndex\x12\x19\n\x08is_right\x18\x01 \x03(\x08R\x07isRightBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v2.mediator_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2'
  _globals['_MEDIATORRESPONSE']._serialized_start=195
  _globals['_MEDIATORRESPONSE']._serialized_end=583
  _globals['_VIEWPOSITION']._serialized_start=585
  _globals['_VIEWPOSITION']._serialized_end=680
  _globals['_MERKLESEQINDEX']._serialized_start=682
  _globals['_MERKLESEQINDEX']._serialized_end=725
# @@protoc_insertion_point(module_scope)
