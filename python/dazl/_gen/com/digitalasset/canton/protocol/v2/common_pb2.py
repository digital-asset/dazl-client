# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v2/common.proto
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
    'com/digitalasset/canton/protocol/v2/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from ..v1 import common_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0com/digitalasset/canton/protocol/v2/common.proto\x12#com.digitalasset.canton.protocol.v2\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x30\x63om/digitalasset/canton/protocol/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xce\x02\n\x14SerializableContract\x12\x1f\n\x0b\x63ontract_id\x18\x01 \x01(\tR\ncontractId\x12\x32\n\x15raw_contract_instance\x18\x02 \x01(\x0cR\x13rawContractInstance\x12I\n\x08metadata\x18\x03 \x01(\x0b\x32-.com.digitalasset.canton.protocol.v1.MetadataR\x08metadata\x12H\n\x12ledger_create_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10ledgerCreateTime\x12L\n\rcontract_salt\x18\x05 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x0c\x63ontractSaltBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v2.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2'
  _globals['_SERIALIZABLECONTRACT']._serialized_start=221
  _globals['_SERIALIZABLECONTRACT']._serialized_end=555
# @@protoc_insertion_point(module_scope)
