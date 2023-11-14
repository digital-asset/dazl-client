# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/protocol/v0/topology_ext.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6com/digitalasset/canton/protocol/v0/topology_ext.proto\x12#com.digitalasset.canton.protocol.v0\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc9\x02\n\x14TopologyTransactions\x12T\n\x05items\x18\x01 \x03(\x0b\x32>.com.digitalasset.canton.protocol.v0.TopologyTransactions.ItemR\x05items\x1a\xda\x01\n\x04Item\x12\x38\n\tsequenced\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tsequenced\x12\x39\n\nvalid_from\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tvalidFrom\x12;\n\x0bvalid_until\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nvalidUntil\x12 \n\x0btransaction\x18\x03 \x01(\x0cR\x0btransactionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v0.topology_ext_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TOPOLOGYTRANSACTIONS']._serialized_start=129
  _globals['_TOPOLOGYTRANSACTIONS']._serialized_end=458
  _globals['_TOPOLOGYTRANSACTIONS_ITEM']._serialized_start=240
  _globals['_TOPOLOGYTRANSACTIONS_ITEM']._serialized_end=458
# @@protoc_insertion_point(module_scope)
