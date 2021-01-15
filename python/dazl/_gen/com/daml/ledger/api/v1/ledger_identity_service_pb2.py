# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/ledger_identity_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import trace_context_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/ledger_identity_service.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\037LedgerIdentityServiceOuterClass\252\002\026Com.Daml.Ledger.Api.V1',
  serialized_pb=b'\n4com/daml/ledger/api/v1/ledger_identity_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a*com/daml/ledger/api/v1/trace_context.proto\"X\n\x18GetLedgerIdentityRequest\x12<\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContext\".\n\x19GetLedgerIdentityResponse\x12\x11\n\tledger_id\x18\x01 \x01(\t2\x91\x01\n\x15LedgerIdentityService\x12x\n\x11GetLedgerIdentity\x12\x30.com.daml.ledger.api.v1.GetLedgerIdentityRequest\x1a\x31.com.daml.ledger.api.v1.GetLedgerIdentityResponseBR\n\x16\x63om.daml.ledger.api.v1B\x1fLedgerIdentityServiceOuterClass\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,])




_GETLEDGERIDENTITYREQUEST = _descriptor.Descriptor(
  name='GetLedgerIdentityRequest',
  full_name='com.daml.ledger.api.v1.GetLedgerIdentityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.GetLedgerIdentityRequest.trace_context', index=0,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=124,
  serialized_end=212,
)


_GETLEDGERIDENTITYRESPONSE = _descriptor.Descriptor(
  name='GetLedgerIdentityResponse',
  full_name='com.daml.ledger.api.v1.GetLedgerIdentityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.GetLedgerIdentityResponse.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=214,
  serialized_end=260,
)

_GETLEDGERIDENTITYREQUEST.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
DESCRIPTOR.message_types_by_name['GetLedgerIdentityRequest'] = _GETLEDGERIDENTITYREQUEST
DESCRIPTOR.message_types_by_name['GetLedgerIdentityResponse'] = _GETLEDGERIDENTITYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetLedgerIdentityRequest = _reflection.GeneratedProtocolMessageType('GetLedgerIdentityRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLEDGERIDENTITYREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.ledger_identity_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetLedgerIdentityRequest)
  })
_sym_db.RegisterMessage(GetLedgerIdentityRequest)

GetLedgerIdentityResponse = _reflection.GeneratedProtocolMessageType('GetLedgerIdentityResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLEDGERIDENTITYRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.ledger_identity_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetLedgerIdentityResponse)
  })
_sym_db.RegisterMessage(GetLedgerIdentityResponse)


DESCRIPTOR._options = None

_LEDGERIDENTITYSERVICE = _descriptor.ServiceDescriptor(
  name='LedgerIdentityService',
  full_name='com.daml.ledger.api.v1.LedgerIdentityService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=263,
  serialized_end=408,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLedgerIdentity',
    full_name='com.daml.ledger.api.v1.LedgerIdentityService.GetLedgerIdentity',
    index=0,
    containing_service=None,
    input_type=_GETLEDGERIDENTITYREQUEST,
    output_type=_GETLEDGERIDENTITYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEDGERIDENTITYSERVICE)

DESCRIPTOR.services_by_name['LedgerIdentityService'] = _LEDGERIDENTITYSERVICE

# @@protoc_insertion_point(module_scope)
