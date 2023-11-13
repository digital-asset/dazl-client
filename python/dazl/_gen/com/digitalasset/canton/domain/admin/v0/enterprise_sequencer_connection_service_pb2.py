# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_connection_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...api.v0 import sequencer_connection_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connection__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nUcom/digitalasset/canton/domain/admin/v0/enterprise_sequencer_connection_service.proto\x12\'com.digitalasset.canton.domain.admin.v0\x1a@com/digitalasset/canton/domain/api/v0/sequencer_connection.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x16\n\x14GetConnectionRequest\"\xc2\x01\n\x15GetConnectionResponse\x12o\n\x15sequencer_connections\x18\x01 \x03(\x0b\x32:.com.digitalasset.canton.domain.api.v0.SequencerConnectionR\x14sequencerConnections\x12\x38\n\x17sequencerTrustThreshold\x18\x02 \x01(\rR\x17sequencerTrustThreshold\"\xc1\x01\n\x14SetConnectionRequest\x12o\n\x15sequencer_connections\x18\x01 \x03(\x0b\x32:.com.digitalasset.canton.domain.api.v0.SequencerConnectionR\x14sequencerConnections\x12\x38\n\x17sequencerTrustThreshold\x18\x02 \x01(\rR\x17sequencerTrustThreshold2\x9f\x02\n$EnterpriseSequencerConnectionService\x12\x8e\x01\n\rGetConnection\x12=.com.digitalasset.canton.domain.admin.v0.GetConnectionRequest\x1a>.com.digitalasset.canton.domain.admin.v0.GetConnectionResponse\x12\x66\n\rSetConnection\x12=.com.digitalasset.canton.domain.admin.v0.SetConnectionRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.admin.v0.enterprise_sequencer_connection_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETCONNECTIONREQUEST']._serialized_start=225
  _globals['_GETCONNECTIONREQUEST']._serialized_end=247
  _globals['_GETCONNECTIONRESPONSE']._serialized_start=250
  _globals['_GETCONNECTIONRESPONSE']._serialized_end=444
  _globals['_SETCONNECTIONREQUEST']._serialized_start=447
  _globals['_SETCONNECTIONREQUEST']._serialized_end=640
  _globals['_ENTERPRISESEQUENCERCONNECTIONSERVICE']._serialized_start=643
  _globals['_ENTERPRISESEQUENCERCONNECTIONSERVICE']._serialized_end=930
# @@protoc_insertion_point(module_scope)