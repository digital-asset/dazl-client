# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/transaction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import event_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_event__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(com/daml/ledger/api/v1/transaction.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/event.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb8\x03\n\x0fTransactionTree\x12%\n\x0etransaction_id\x18\x01 \x01(\tR\rtransactionId\x12\x1d\n\ncommand_id\x18\x02 \x01(\tR\tcommandId\x12\x1f\n\x0bworkflow_id\x18\x03 \x01(\tR\nworkflowId\x12=\n\x0c\x65\x66\x66\x65\x63tive_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x65\x66\x66\x65\x63tiveAt\x12\x16\n\x06offset\x18\x06 \x01(\tR\x06offset\x12Y\n\x0c\x65vents_by_id\x18\x07 \x03(\x0b\x32\x37.com.daml.ledger.api.v1.TransactionTree.EventsByIdEntryR\neventsById\x12$\n\x0eroot_event_ids\x18\x08 \x03(\tR\x0crootEventIds\x1a`\n\x0f\x45ventsByIdEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.com.daml.ledger.api.v1.TreeEventR\x05value:\x02\x38\x01J\x04\x08\x05\x10\x06\"\x9d\x01\n\tTreeEvent\x12@\n\x07\x63reated\x18\x01 \x01(\x0b\x32$.com.daml.ledger.api.v1.CreatedEventH\x00R\x07\x63reated\x12\x46\n\texercised\x18\x02 \x01(\x0b\x32&.com.daml.ledger.api.v1.ExercisedEventH\x00R\texercisedB\x06\n\x04kind\"\x82\x02\n\x0bTransaction\x12%\n\x0etransaction_id\x18\x01 \x01(\tR\rtransactionId\x12\x1d\n\ncommand_id\x18\x02 \x01(\tR\tcommandId\x12\x1f\n\x0bworkflow_id\x18\x03 \x01(\tR\nworkflowId\x12=\n\x0c\x65\x66\x66\x65\x63tive_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x65\x66\x66\x65\x63tiveAt\x12\x35\n\x06\x65vents\x18\x05 \x03(\x0b\x32\x1d.com.daml.ledger.api.v1.EventR\x06\x65vents\x12\x16\n\x06offset\x18\x06 \x01(\tR\x06offsetB\x8f\x01\n\x16\x63om.daml.ledger.api.v1B\x15TransactionOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.transaction_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.daml.ledger.api.v1B\025TransactionOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _TRANSACTIONTREE_EVENTSBYIDENTRY._options = None
  _TRANSACTIONTREE_EVENTSBYIDENTRY._serialized_options = b'8\001'
  _globals['_TRANSACTIONTREE']._serialized_start=138
  _globals['_TRANSACTIONTREE']._serialized_end=578
  _globals['_TRANSACTIONTREE_EVENTSBYIDENTRY']._serialized_start=476
  _globals['_TRANSACTIONTREE_EVENTSBYIDENTRY']._serialized_end=572
  _globals['_TREEEVENT']._serialized_start=581
  _globals['_TREEEVENT']._serialized_end=738
  _globals['_TRANSACTION']._serialized_start=741
  _globals['_TRANSACTION']._serialized_end=999
# @@protoc_insertion_point(module_scope)
