# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/update_service.proto
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
    'com/daml/ledger/api/v2/update_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import offset_checkpoint_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_offset__checkpoint__pb2
from . import reassignment_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_reassignment__pb2
from . import transaction_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_transaction__pb2
from . import transaction_filter_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_transaction__filter__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+com/daml/ledger/api/v2/update_service.proto\x12\x16\x63om.daml.ledger.api.v2\x1a.com/daml/ledger/api/v2/offset_checkpoint.proto\x1a)com/daml/ledger/api/v2/reassignment.proto\x1a(com/daml/ledger/api/v2/transaction.proto\x1a/com/daml/ledger/api/v2/transaction_filter.proto\"\xd5\x01\n\x11GetUpdatesRequest\x12\'\n\x0f\x62\x65gin_exclusive\x18\x01 \x01(\x03R\x0e\x62\x65ginExclusive\x12(\n\rend_inclusive\x18\x02 \x01(\x03H\x00R\x0c\x65ndInclusive\x88\x01\x01\x12\x41\n\x06\x66ilter\x18\x03 \x01(\x0b\x32).com.daml.ledger.api.v2.TransactionFilterR\x06\x66ilter\x12\x18\n\x07verbose\x18\x04 \x01(\x08R\x07verboseB\x10\n\x0e_end_inclusive\"\x8c\x02\n\x12GetUpdatesResponse\x12G\n\x0btransaction\x18\x01 \x01(\x0b\x32#.com.daml.ledger.api.v2.TransactionH\x00R\x0btransaction\x12J\n\x0creassignment\x18\x02 \x01(\x0b\x32$.com.daml.ledger.api.v2.ReassignmentH\x00R\x0creassignment\x12W\n\x11offset_checkpoint\x18\x03 \x01(\x0b\x32(.com.daml.ledger.api.v2.OffsetCheckpointH\x00R\x10offsetCheckpointB\x08\n\x06update\"\x9d\x02\n\x16GetUpdateTreesResponse\x12T\n\x10transaction_tree\x18\x01 \x01(\x0b\x32\'.com.daml.ledger.api.v2.TransactionTreeH\x00R\x0ftransactionTree\x12J\n\x0creassignment\x18\x02 \x01(\x0b\x32$.com.daml.ledger.api.v2.ReassignmentH\x00R\x0creassignment\x12W\n\x11offset_checkpoint\x18\x03 \x01(\x0b\x32(.com.daml.ledger.api.v2.OffsetCheckpointH\x00R\x10offsetCheckpointB\x08\n\x06update\"j\n\x1eGetTransactionByEventIdRequest\x12\x19\n\x08\x65vent_id\x18\x01 \x01(\tR\x07\x65ventId\x12-\n\x12requesting_parties\x18\x02 \x03(\tR\x11requestingParties\"g\n\x19GetTransactionByIdRequest\x12\x1b\n\tupdate_id\x18\x01 \x01(\tR\x08updateId\x12-\n\x12requesting_parties\x18\x02 \x03(\tR\x11requestingParties\"g\n\x1aGetTransactionTreeResponse\x12I\n\x0btransaction\x18\x01 \x01(\x0b\x32\'.com.daml.ledger.api.v2.TransactionTreeR\x0btransaction\"_\n\x16GetTransactionResponse\x12\x45\n\x0btransaction\x18\x01 \x01(\x0b\x32#.com.daml.ledger.api.v2.TransactionR\x0btransaction2\xef\x05\n\rUpdateService\x12\x65\n\nGetUpdates\x12).com.daml.ledger.api.v2.GetUpdatesRequest\x1a*.com.daml.ledger.api.v2.GetUpdatesResponse0\x01\x12m\n\x0eGetUpdateTrees\x12).com.daml.ledger.api.v2.GetUpdatesRequest\x1a..com.daml.ledger.api.v2.GetUpdateTreesResponse0\x01\x12\x89\x01\n\x1bGetTransactionTreeByEventId\x12\x36.com.daml.ledger.api.v2.GetTransactionByEventIdRequest\x1a\x32.com.daml.ledger.api.v2.GetTransactionTreeResponse\x12\x7f\n\x16GetTransactionTreeById\x12\x31.com.daml.ledger.api.v2.GetTransactionByIdRequest\x1a\x32.com.daml.ledger.api.v2.GetTransactionTreeResponse\x12\x81\x01\n\x17GetTransactionByEventId\x12\x36.com.daml.ledger.api.v2.GetTransactionByEventIdRequest\x1a..com.daml.ledger.api.v2.GetTransactionResponse\x12w\n\x12GetTransactionById\x12\x31.com.daml.ledger.api.v2.GetTransactionByIdRequest\x1a..com.daml.ledger.api.v2.GetTransactionResponseB\x91\x01\n\x16\x63om.daml.ledger.api.v2B\x17UpdateServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.update_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\027UpdateServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_GETUPDATESREQUEST']._serialized_start=254
  _globals['_GETUPDATESREQUEST']._serialized_end=467
  _globals['_GETUPDATESRESPONSE']._serialized_start=470
  _globals['_GETUPDATESRESPONSE']._serialized_end=738
  _globals['_GETUPDATETREESRESPONSE']._serialized_start=741
  _globals['_GETUPDATETREESRESPONSE']._serialized_end=1026
  _globals['_GETTRANSACTIONBYEVENTIDREQUEST']._serialized_start=1028
  _globals['_GETTRANSACTIONBYEVENTIDREQUEST']._serialized_end=1134
  _globals['_GETTRANSACTIONBYIDREQUEST']._serialized_start=1136
  _globals['_GETTRANSACTIONBYIDREQUEST']._serialized_end=1239
  _globals['_GETTRANSACTIONTREERESPONSE']._serialized_start=1241
  _globals['_GETTRANSACTIONTREERESPONSE']._serialized_end=1344
  _globals['_GETTRANSACTIONRESPONSE']._serialized_start=1346
  _globals['_GETTRANSACTIONRESPONSE']._serialized_end=1441
  _globals['_UPDATESERVICE']._serialized_start=1444
  _globals['_UPDATESERVICE']._serialized_end=2195
# @@protoc_insertion_point(module_scope)
