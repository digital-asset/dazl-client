# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/event_query_service.proto
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
    'com/daml/ledger/api/v2/event_query_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import event_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0com/daml/ledger/api/v2/event_query_service.proto\x12\x16\x63om.daml.ledger.api.v2\x1a\"com/daml/ledger/api/v2/event.proto\"n\n\x1cGetEventsByContractIdRequest\x12\x1f\n\x0b\x63ontract_id\x18\x01 \x01(\tR\ncontractId\x12-\n\x12requesting_parties\x18\x02 \x03(\tR\x11requestingParties\"\x98\x01\n\x1dGetEventsByContractIdResponse\x12\x39\n\x07\x63reated\x18\x01 \x01(\x0b\x32\x1f.com.daml.ledger.api.v2.CreatedR\x07\x63reated\x12<\n\x08\x61rchived\x18\x02 \x01(\x0b\x32 .com.daml.ledger.api.v2.ArchivedR\x08\x61rchived\"q\n\x07\x43reated\x12I\n\rcreated_event\x18\x01 \x01(\x0b\x32$.com.daml.ledger.api.v2.CreatedEventR\x0c\x63reatedEvent\x12\x1b\n\tdomain_id\x18\x02 \x01(\tR\x08\x64omainId\"u\n\x08\x41rchived\x12L\n\x0e\x61rchived_event\x18\x01 \x01(\x0b\x32%.com.daml.ledger.api.v2.ArchivedEventR\rarchivedEvent\x12\x1b\n\tdomain_id\x18\x02 \x01(\tR\x08\x64omainId2\x9a\x01\n\x11\x45ventQueryService\x12\x84\x01\n\x15GetEventsByContractId\x12\x34.com.daml.ledger.api.v2.GetEventsByContractIdRequest\x1a\x35.com.daml.ledger.api.v2.GetEventsByContractIdResponseB\x95\x01\n\x16\x63om.daml.ledger.api.v2B\x1b\x45ventQueryServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.event_query_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\033EventQueryServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_GETEVENTSBYCONTRACTIDREQUEST']._serialized_start=112
  _globals['_GETEVENTSBYCONTRACTIDREQUEST']._serialized_end=222
  _globals['_GETEVENTSBYCONTRACTIDRESPONSE']._serialized_start=225
  _globals['_GETEVENTSBYCONTRACTIDRESPONSE']._serialized_end=377
  _globals['_CREATED']._serialized_start=379
  _globals['_CREATED']._serialized_end=492
  _globals['_ARCHIVED']._serialized_start=494
  _globals['_ARCHIVED']._serialized_end=611
  _globals['_EVENTQUERYSERVICE']._serialized_start=614
  _globals['_EVENTQUERYSERVICE']._serialized_end=768
# @@protoc_insertion_point(module_scope)
