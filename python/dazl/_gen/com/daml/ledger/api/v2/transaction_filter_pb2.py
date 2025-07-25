# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/transaction_filter.proto
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
    'com/daml/ledger/api/v2/transaction_filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import value_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/com/daml/ledger/api/v2/transaction_filter.proto\x12\x16\x63om.daml.ledger.api.v2\x1a\"com/daml/ledger/api/v2/value.proto\"S\n\x07\x46ilters\x12H\n\ncumulative\x18\x01 \x03(\x0b\x32(.com.daml.ledger.api.v2.CumulativeFilterR\ncumulative\"\xa3\x02\n\x10\x43umulativeFilter\x12Q\n\x0fwildcard_filter\x18\x01 \x01(\x0b\x32&.com.daml.ledger.api.v2.WildcardFilterH\x00R\x0ewildcardFilter\x12T\n\x10interface_filter\x18\x02 \x01(\x0b\x32\'.com.daml.ledger.api.v2.InterfaceFilterH\x00R\x0finterfaceFilter\x12Q\n\x0ftemplate_filter\x18\x03 \x01(\x0b\x32&.com.daml.ledger.api.v2.TemplateFilterH\x00R\x0etemplateFilterB\x13\n\x11identifier_filter\"M\n\x0eWildcardFilter\x12;\n\x1ainclude_created_event_blob\x18\x01 \x01(\x08R\x17includeCreatedEventBlob\"\xcb\x01\n\x0fInterfaceFilter\x12\x45\n\x0cinterface_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v2.IdentifierR\x0binterfaceId\x12\x34\n\x16include_interface_view\x18\x02 \x01(\x08R\x14includeInterfaceView\x12;\n\x1ainclude_created_event_blob\x18\x03 \x01(\x08R\x17includeCreatedEventBlob\"\x92\x01\n\x0eTemplateFilter\x12\x43\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v2.IdentifierR\ntemplateId\x12;\n\x1ainclude_created_event_blob\x18\x02 \x01(\x08R\x17includeCreatedEventBlob\"\xb4\x02\n\x11TransactionFilter\x12g\n\x10\x66ilters_by_party\x18\x01 \x03(\x0b\x32=.com.daml.ledger.api.v2.TransactionFilter.FiltersByPartyEntryR\x0e\x66iltersByParty\x12R\n\x15\x66ilters_for_any_party\x18\x02 \x01(\x0b\x32\x1f.com.daml.ledger.api.v2.FiltersR\x12\x66iltersForAnyParty\x1a\x62\n\x13\x46iltersByPartyEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.com.daml.ledger.api.v2.FiltersR\x05value:\x02\x38\x01\"\xc2\x02\n\x0b\x45ventFormat\x12\x61\n\x10\x66ilters_by_party\x18\x01 \x03(\x0b\x32\x37.com.daml.ledger.api.v2.EventFormat.FiltersByPartyEntryR\x0e\x66iltersByParty\x12R\n\x15\x66ilters_for_any_party\x18\x02 \x01(\x0b\x32\x1f.com.daml.ledger.api.v2.FiltersR\x12\x66iltersForAnyParty\x12\x18\n\x07verbose\x18\x03 \x01(\x08R\x07verbose\x1a\x62\n\x13\x46iltersByPartyEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.com.daml.ledger.api.v2.FiltersR\x05value:\x02\x38\x01\"\xb2\x01\n\x11TransactionFormat\x12\x46\n\x0c\x65vent_format\x18\x01 \x01(\x0b\x32#.com.daml.ledger.api.v2.EventFormatR\x0b\x65ventFormat\x12U\n\x11transaction_shape\x18\x02 \x01(\x0e\x32(.com.daml.ledger.api.v2.TransactionShapeR\x10transactionShape\"\xaa\x01\n\x0eTopologyFormat\x12\x97\x01\n(include_participant_authorization_events\x18\x01 \x01(\x0b\x32>.com.daml.ledger.api.v2.ParticipantAuthorizationTopologyFormatR%includeParticipantAuthorizationEvents\"B\n&ParticipantAuthorizationTopologyFormat\x12\x18\n\x07parties\x18\x01 \x03(\tR\x07parties\"\xa6\x02\n\x0cUpdateFormat\x12\\\n\x14include_transactions\x18\x01 \x01(\x0b\x32).com.daml.ledger.api.v2.TransactionFormatR\x13includeTransactions\x12X\n\x15include_reassignments\x18\x02 \x01(\x0b\x32#.com.daml.ledger.api.v2.EventFormatR\x14includeReassignments\x12^\n\x17include_topology_events\x18\x03 \x01(\x0b\x32&.com.daml.ledger.api.v2.TopologyFormatR\x15includeTopologyEvents*|\n\x10TransactionShape\x12!\n\x1dTRANSACTION_SHAPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTRANSACTION_SHAPE_ACS_DELTA\x10\x01\x12$\n TRANSACTION_SHAPE_LEDGER_EFFECTS\x10\x02\x42\x95\x01\n\x16\x63om.daml.ledger.api.v2B\x1bTransactionFilterOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.transaction_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\033TransactionFilterOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_TRANSACTIONFILTER_FILTERSBYPARTYENTRY']._loaded_options = None
  _globals['_TRANSACTIONFILTER_FILTERSBYPARTYENTRY']._serialized_options = b'8\001'
  _globals['_EVENTFORMAT_FILTERSBYPARTYENTRY']._loaded_options = None
  _globals['_EVENTFORMAT_FILTERSBYPARTYENTRY']._serialized_options = b'8\001'
  _globals['_TRANSACTIONSHAPE']._serialized_start=2279
  _globals['_TRANSACTIONSHAPE']._serialized_end=2403
  _globals['_FILTERS']._serialized_start=111
  _globals['_FILTERS']._serialized_end=194
  _globals['_CUMULATIVEFILTER']._serialized_start=197
  _globals['_CUMULATIVEFILTER']._serialized_end=488
  _globals['_WILDCARDFILTER']._serialized_start=490
  _globals['_WILDCARDFILTER']._serialized_end=567
  _globals['_INTERFACEFILTER']._serialized_start=570
  _globals['_INTERFACEFILTER']._serialized_end=773
  _globals['_TEMPLATEFILTER']._serialized_start=776
  _globals['_TEMPLATEFILTER']._serialized_end=922
  _globals['_TRANSACTIONFILTER']._serialized_start=925
  _globals['_TRANSACTIONFILTER']._serialized_end=1233
  _globals['_TRANSACTIONFILTER_FILTERSBYPARTYENTRY']._serialized_start=1135
  _globals['_TRANSACTIONFILTER_FILTERSBYPARTYENTRY']._serialized_end=1233
  _globals['_EVENTFORMAT']._serialized_start=1236
  _globals['_EVENTFORMAT']._serialized_end=1558
  _globals['_EVENTFORMAT_FILTERSBYPARTYENTRY']._serialized_start=1135
  _globals['_EVENTFORMAT_FILTERSBYPARTYENTRY']._serialized_end=1233
  _globals['_TRANSACTIONFORMAT']._serialized_start=1561
  _globals['_TRANSACTIONFORMAT']._serialized_end=1739
  _globals['_TOPOLOGYFORMAT']._serialized_start=1742
  _globals['_TOPOLOGYFORMAT']._serialized_end=1912
  _globals['_PARTICIPANTAUTHORIZATIONTOPOLOGYFORMAT']._serialized_start=1914
  _globals['_PARTICIPANTAUTHORIZATIONTOPOLOGYFORMAT']._serialized_end=1980
  _globals['_UPDATEFORMAT']._serialized_start=1983
  _globals['_UPDATEFORMAT']._serialized_end=2277
# @@protoc_insertion_point(module_scope)
