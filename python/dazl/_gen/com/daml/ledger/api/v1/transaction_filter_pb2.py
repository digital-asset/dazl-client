# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/transaction_filter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import value_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/transaction_filter.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\033TransactionFilterOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/com/daml/ledger/api/v1/transaction_filter.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/value.proto\"\xe0\x01\n\x11TransactionFilter\x12g\n\x10\x66ilters_by_party\x18\x01 \x03(\x0b\x32=.com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntryR\x0e\x66iltersByParty\x1a\x62\n\x13\x46iltersByPartyEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.com.daml.ledger.api.v1.FiltersR\x05value:\x02\x38\x01\"Q\n\x07\x46ilters\x12\x46\n\tinclusive\x18\x01 \x01(\x0b\x32(.com.daml.ledger.api.v1.InclusiveFiltersR\tinclusive\"Y\n\x10InclusiveFilters\x12\x45\n\x0ctemplate_ids\x18\x01 \x03(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\x0btemplateIdsB\x9f\x01\n\x16\x63om.daml.ledger.api.v1B\x1bTransactionFilterOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2.DESCRIPTOR,])




_TRANSACTIONFILTER_FILTERSBYPARTYENTRY = _descriptor.Descriptor(
  name='FiltersByPartyEntry',
  full_name='com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=336,
)

_TRANSACTIONFILTER = _descriptor.Descriptor(
  name='TransactionFilter',
  full_name='com.daml.ledger.api.v1.TransactionFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filters_by_party', full_name='com.daml.ledger.api.v1.TransactionFilter.filters_by_party', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filtersByParty', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTIONFILTER_FILTERSBYPARTYENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=336,
)


_FILTERS = _descriptor.Descriptor(
  name='Filters',
  full_name='com.daml.ledger.api.v1.Filters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inclusive', full_name='com.daml.ledger.api.v1.Filters.inclusive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='inclusive', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=419,
)


_INCLUSIVEFILTERS = _descriptor.Descriptor(
  name='InclusiveFilters',
  full_name='com.daml.ledger.api.v1.InclusiveFilters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_ids', full_name='com.daml.ledger.api.v1.InclusiveFilters.template_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='templateIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=510,
)

_TRANSACTIONFILTER_FILTERSBYPARTYENTRY.fields_by_name['value'].message_type = _FILTERS
_TRANSACTIONFILTER_FILTERSBYPARTYENTRY.containing_type = _TRANSACTIONFILTER
_TRANSACTIONFILTER.fields_by_name['filters_by_party'].message_type = _TRANSACTIONFILTER_FILTERSBYPARTYENTRY
_FILTERS.fields_by_name['inclusive'].message_type = _INCLUSIVEFILTERS
_INCLUSIVEFILTERS.fields_by_name['template_ids'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
DESCRIPTOR.message_types_by_name['TransactionFilter'] = _TRANSACTIONFILTER
DESCRIPTOR.message_types_by_name['Filters'] = _FILTERS
DESCRIPTOR.message_types_by_name['InclusiveFilters'] = _INCLUSIVEFILTERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionFilter = _reflection.GeneratedProtocolMessageType('TransactionFilter', (_message.Message,), {

  'FiltersByPartyEntry' : _reflection.GeneratedProtocolMessageType('FiltersByPartyEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTIONFILTER_FILTERSBYPARTYENTRY,
    '__module__' : 'com.daml.ledger.api.v1.transaction_filter_pb2'
    # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.TransactionFilter.FiltersByPartyEntry)
    })
  ,
  'DESCRIPTOR' : _TRANSACTIONFILTER,
  '__module__' : 'com.daml.ledger.api.v1.transaction_filter_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.TransactionFilter)
  })
_sym_db.RegisterMessage(TransactionFilter)
_sym_db.RegisterMessage(TransactionFilter.FiltersByPartyEntry)

Filters = _reflection.GeneratedProtocolMessageType('Filters', (_message.Message,), {
  'DESCRIPTOR' : _FILTERS,
  '__module__' : 'com.daml.ledger.api.v1.transaction_filter_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.Filters)
  })
_sym_db.RegisterMessage(Filters)

InclusiveFilters = _reflection.GeneratedProtocolMessageType('InclusiveFilters', (_message.Message,), {
  'DESCRIPTOR' : _INCLUSIVEFILTERS,
  '__module__' : 'com.daml.ledger.api.v1.transaction_filter_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.InclusiveFilters)
  })
_sym_db.RegisterMessage(InclusiveFilters)


DESCRIPTOR._options = None
_TRANSACTIONFILTER_FILTERSBYPARTYENTRY._options = None
# @@protoc_insertion_point(module_scope)
