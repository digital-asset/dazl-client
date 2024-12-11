# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/command_service.proto
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
    'com/daml/ledger/api/v2/command_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import commands_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_commands__pb2
from . import transaction_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,com/daml/ledger/api/v2/command_service.proto\x12\x16\x63om.daml.ledger.api.v2\x1a%com/daml/ledger/api/v2/commands.proto\x1a(com/daml/ledger/api/v2/transaction.proto\"T\n\x14SubmitAndWaitRequest\x12<\n\x08\x63ommands\x18\x01 \x01(\x0b\x32 .com.daml.ledger.api.v2.CommandsR\x08\x63ommands\"a\n\x15SubmitAndWaitResponse\x12\x1b\n\tupdate_id\x18\x01 \x01(\tR\x08updateId\x12+\n\x11\x63ompletion_offset\x18\x02 \x01(\x03R\x10\x63ompletionOffset\"l\n#SubmitAndWaitForTransactionResponse\x12\x45\n\x0btransaction\x18\x01 \x01(\x0b\x32#.com.daml.ledger.api.v2.TransactionR\x0btransaction\"t\n\'SubmitAndWaitForTransactionTreeResponse\x12I\n\x0btransaction\x18\x01 \x01(\x0b\x32\'.com.daml.ledger.api.v2.TransactionTreeR\x0btransaction2\x9c\x03\n\x0e\x43ommandService\x12l\n\rSubmitAndWait\x12,.com.daml.ledger.api.v2.SubmitAndWaitRequest\x1a-.com.daml.ledger.api.v2.SubmitAndWaitResponse\x12\x88\x01\n\x1bSubmitAndWaitForTransaction\x12,.com.daml.ledger.api.v2.SubmitAndWaitRequest\x1a;.com.daml.ledger.api.v2.SubmitAndWaitForTransactionResponse\x12\x90\x01\n\x1fSubmitAndWaitForTransactionTree\x12,.com.daml.ledger.api.v2.SubmitAndWaitRequest\x1a?.com.daml.ledger.api.v2.SubmitAndWaitForTransactionTreeResponseB\x92\x01\n\x16\x63om.daml.ledger.api.v2B\x18\x43ommandServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.command_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\030CommandServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_SUBMITANDWAITREQUEST']._serialized_start=153
  _globals['_SUBMITANDWAITREQUEST']._serialized_end=237
  _globals['_SUBMITANDWAITRESPONSE']._serialized_start=239
  _globals['_SUBMITANDWAITRESPONSE']._serialized_end=336
  _globals['_SUBMITANDWAITFORTRANSACTIONRESPONSE']._serialized_start=338
  _globals['_SUBMITANDWAITFORTRANSACTIONRESPONSE']._serialized_end=446
  _globals['_SUBMITANDWAITFORTRANSACTIONTREERESPONSE']._serialized_start=448
  _globals['_SUBMITANDWAITFORTRANSACTIONTREERESPONSE']._serialized_end=564
  _globals['_COMMANDSERVICE']._serialized_start=567
  _globals['_COMMANDSERVICE']._serialized_end=979
# @@protoc_insertion_point(module_scope)
