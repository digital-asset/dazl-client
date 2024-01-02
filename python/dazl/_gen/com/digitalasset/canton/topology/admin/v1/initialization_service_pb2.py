# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/topology/admin/v1/initialization_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....protocol.v0 import topology_ext_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_topology__ext__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFcom/digitalasset/canton/topology/admin/v1/initialization_service.proto\x12)com.digitalasset.canton.topology.admin.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x36\x63om/digitalasset/canton/protocol/v0/topology_ext.proto\"<\n\rInitIdRequest\x12+\n\x11unique_identifier\x18\x01 \x01(\tR\x10uniqueIdentifier\"\x10\n\x0eInitIdResponse\"^\n\rGetIdResponse\x12 \n\x0binitialized\x18\x01 \x01(\x08R\x0binitialized\x12+\n\x11unique_identifier\x18\x02 \x01(\tR\x10uniqueIdentifier\"\"\n GetOnboardingTransactionsRequest\"\x82\x01\n!GetOnboardingTransactionsResponse\x12]\n\x0ctransactions\x18\x01 \x01(\x0b\x32\x39.com.digitalasset.canton.protocol.v0.TopologyTransactionsR\x0ctransactions2\xf6\x03\n\x1eIdentityInitializationServiceX\x12}\n\x06InitId\x12\x38.com.digitalasset.canton.topology.admin.v1.InitIdRequest\x1a\x39.com.digitalasset.canton.topology.admin.v1.InitIdResponse\x12\xb6\x01\n\x19GetOnboardingTransactions\x12K.com.digitalasset.canton.topology.admin.v1.GetOnboardingTransactionsRequest\x1aL.com.digitalasset.canton.topology.admin.v1.GetOnboardingTransactionsResponse\x12Y\n\x05GetId\x12\x16.google.protobuf.Empty\x1a\x38.com.digitalasset.canton.topology.admin.v1.GetIdResponse\x12\x41\n\x0b\x43urrentTime\x12\x16.google.protobuf.Empty\x1a\x1a.google.protobuf.Timestampb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.topology.admin.v1.initialization_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INITIDREQUEST']._serialized_start=235
  _globals['_INITIDREQUEST']._serialized_end=295
  _globals['_INITIDRESPONSE']._serialized_start=297
  _globals['_INITIDRESPONSE']._serialized_end=313
  _globals['_GETIDRESPONSE']._serialized_start=315
  _globals['_GETIDRESPONSE']._serialized_end=409
  _globals['_GETONBOARDINGTRANSACTIONSREQUEST']._serialized_start=411
  _globals['_GETONBOARDINGTRANSACTIONSREQUEST']._serialized_end=445
  _globals['_GETONBOARDINGTRANSACTIONSRESPONSE']._serialized_start=448
  _globals['_GETONBOARDINGTRANSACTIONSRESPONSE']._serialized_end=578
  _globals['_IDENTITYINITIALIZATIONSERVICEX']._serialized_start=581
  _globals['_IDENTITYINITIALIZATIONSERVICEX']._serialized_end=1083
# @@protoc_insertion_point(module_scope)
