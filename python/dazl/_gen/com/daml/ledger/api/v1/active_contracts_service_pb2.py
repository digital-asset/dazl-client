# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/active_contracts_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import event_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__pb2
from . import transaction_filter_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__filter__pb2
from . import trace_context_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/active_contracts_service.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B ActiveContractsServiceOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5com/daml/ledger/api/v1/active_contracts_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/event.proto\x1a/com/daml/ledger/api/v1/transaction_filter.proto\x1a*com/daml/ledger/api/v1/trace_context.proto\"\xe1\x01\n\x19GetActiveContractsRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\x12\x41\n\x06\x66ilter\x18\x02 \x01(\x0b\x32).com.daml.ledger.api.v1.TransactionFilterR\x06\x66ilter\x12\x18\n\x07verbose\x18\x03 \x01(\x08R\x07verbose\x12J\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContextR\x0ctraceContext\"\xf2\x01\n\x1aGetActiveContractsResponse\x12\x16\n\x06offset\x18\x01 \x01(\tR\x06offset\x12\x1f\n\x0bworkflow_id\x18\x02 \x01(\tR\nworkflowId\x12O\n\x10\x61\x63tive_contracts\x18\x03 \x03(\x0b\x32$.com.daml.ledger.api.v1.CreatedEventR\x0f\x61\x63tiveContracts\x12J\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContextR\x0ctraceContext2\x97\x01\n\x16\x41\x63tiveContractsService\x12}\n\x12GetActiveContracts\x12\x31.com.daml.ledger.api.v1.GetActiveContractsRequest\x1a\x32.com.daml.ledger.api.v1.GetActiveContractsResponse0\x01\x42\xa4\x01\n\x16\x63om.daml.ledger.api.v1B ActiveContractsServiceOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__filter__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,])




_GETACTIVECONTRACTSREQUEST = _descriptor.Descriptor(
  name='GetActiveContractsRequest',
  full_name='com.daml.ledger.api.v1.GetActiveContractsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.GetActiveContractsRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ledgerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='com.daml.ledger.api.v1.GetActiveContractsRequest.filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verbose', full_name='com.daml.ledger.api.v1.GetActiveContractsRequest.verbose', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='verbose', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.GetActiveContractsRequest.trace_context', index=3,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='traceContext', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=211,
  serialized_end=436,
)


_GETACTIVECONTRACTSRESPONSE = _descriptor.Descriptor(
  name='GetActiveContractsResponse',
  full_name='com.daml.ledger.api.v1.GetActiveContractsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='com.daml.ledger.api.v1.GetActiveContractsResponse.offset', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='offset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='com.daml.ledger.api.v1.GetActiveContractsResponse.workflow_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='workflowId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active_contracts', full_name='com.daml.ledger.api.v1.GetActiveContractsResponse.active_contracts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='activeContracts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.GetActiveContractsResponse.trace_context', index=3,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='traceContext', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=439,
  serialized_end=681,
)

_GETACTIVECONTRACTSREQUEST.fields_by_name['filter'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__filter__pb2._TRANSACTIONFILTER
_GETACTIVECONTRACTSREQUEST.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETACTIVECONTRACTSRESPONSE.fields_by_name['active_contracts'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__pb2._CREATEDEVENT
_GETACTIVECONTRACTSRESPONSE.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
DESCRIPTOR.message_types_by_name['GetActiveContractsRequest'] = _GETACTIVECONTRACTSREQUEST
DESCRIPTOR.message_types_by_name['GetActiveContractsResponse'] = _GETACTIVECONTRACTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetActiveContractsRequest = _reflection.GeneratedProtocolMessageType('GetActiveContractsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIVECONTRACTSREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.active_contracts_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetActiveContractsRequest)
  })
_sym_db.RegisterMessage(GetActiveContractsRequest)

GetActiveContractsResponse = _reflection.GeneratedProtocolMessageType('GetActiveContractsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIVECONTRACTSRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.active_contracts_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetActiveContractsResponse)
  })
_sym_db.RegisterMessage(GetActiveContractsResponse)


DESCRIPTOR._options = None

_ACTIVECONTRACTSSERVICE = _descriptor.ServiceDescriptor(
  name='ActiveContractsService',
  full_name='com.daml.ledger.api.v1.ActiveContractsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=684,
  serialized_end=835,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetActiveContracts',
    full_name='com.daml.ledger.api.v1.ActiveContractsService.GetActiveContracts',
    index=0,
    containing_service=None,
    input_type=_GETACTIVECONTRACTSREQUEST,
    output_type=_GETACTIVECONTRACTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACTIVECONTRACTSSERVICE)

DESCRIPTOR.services_by_name['ActiveContractsService'] = _ACTIVECONTRACTSSERVICE

# @@protoc_insertion_point(module_scope)
