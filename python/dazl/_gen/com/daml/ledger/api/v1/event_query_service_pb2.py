# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/event_query_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import event_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__pb2
from . import value_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0com/daml/ledger/api/v1/event_query_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/event.proto\x1a\"com/daml/ledger/api/v1/value.proto\"n\n\x1cGetEventsByContractIdRequest\x12\x1f\n\x0b\x63ontract_id\x18\x01 \x01(\tR\ncontractId\x12-\n\x12requesting_parties\x18\x02 \x03(\tR\x11requestingParties\"\xb4\x01\n\x1dGetEventsByContractIdResponse\x12G\n\x0c\x63reate_event\x18\x01 \x01(\x0b\x32$.com.daml.ledger.api.v1.CreatedEventR\x0b\x63reateEvent\x12J\n\rarchive_event\x18\x02 \x01(\x0b\x32%.com.daml.ledger.api.v1.ArchivedEventR\x0c\x61rchiveEvent\"\x84\x02\n\x1dGetEventsByContractKeyRequest\x12@\n\x0c\x63ontract_key\x18\x01 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0b\x63ontractKey\x12\x43\n\x0btemplate_id\x18\x02 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12-\n\x12requesting_parties\x18\x03 \x03(\tR\x11requestingParties\x12-\n\x12\x63ontinuation_token\x18\x04 \x01(\tR\x11\x63ontinuationToken\"\xe4\x01\n\x1eGetEventsByContractKeyResponse\x12G\n\x0c\x63reate_event\x18\x01 \x01(\x0b\x32$.com.daml.ledger.api.v1.CreatedEventR\x0b\x63reateEvent\x12J\n\rarchive_event\x18\x02 \x01(\x0b\x32%.com.daml.ledger.api.v1.ArchivedEventR\x0c\x61rchiveEvent\x12-\n\x12\x63ontinuation_token\x18\x04 \x01(\tR\x11\x63ontinuationToken2\xa4\x02\n\x11\x45ventQueryService\x12\x84\x01\n\x15GetEventsByContractId\x12\x34.com.daml.ledger.api.v1.GetEventsByContractIdRequest\x1a\x35.com.daml.ledger.api.v1.GetEventsByContractIdResponse\x12\x87\x01\n\x16GetEventsByContractKey\x12\x35.com.daml.ledger.api.v1.GetEventsByContractKeyRequest\x1a\x36.com.daml.ledger.api.v1.GetEventsByContractKeyResponseB\x95\x01\n\x16\x63om.daml.ledger.api.v1B\x1b\x45ventQueryServiceOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.event_query_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.daml.ledger.api.v1B\033EventQueryServiceOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _globals['_GETEVENTSBYCONTRACTIDREQUEST']._serialized_start=148
  _globals['_GETEVENTSBYCONTRACTIDREQUEST']._serialized_end=258
  _globals['_GETEVENTSBYCONTRACTIDRESPONSE']._serialized_start=261
  _globals['_GETEVENTSBYCONTRACTIDRESPONSE']._serialized_end=441
  _globals['_GETEVENTSBYCONTRACTKEYREQUEST']._serialized_start=444
  _globals['_GETEVENTSBYCONTRACTKEYREQUEST']._serialized_end=704
  _globals['_GETEVENTSBYCONTRACTKEYRESPONSE']._serialized_start=707
  _globals['_GETEVENTSBYCONTRACTKEYRESPONSE']._serialized_end=935
  _globals['_EVENTQUERYSERVICE']._serialized_start=938
  _globals['_EVENTQUERYSERVICE']._serialized_end=1230
# @@protoc_insertion_point(module_scope)
