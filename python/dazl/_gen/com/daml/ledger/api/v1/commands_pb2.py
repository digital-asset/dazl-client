# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v1/commands.proto
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
    'com/daml/ledger/api/v1/commands.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import value_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%com/daml/ledger/api/v1/commands.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/value.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xeb\x06\n\x08\x43ommands\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\x12\x1f\n\x0bworkflow_id\x18\x02 \x01(\tR\nworkflowId\x12%\n\x0e\x61pplication_id\x18\x03 \x01(\tR\rapplicationId\x12\x1d\n\ncommand_id\x18\x04 \x01(\tR\tcommandId\x12\x14\n\x05party\x18\x05 \x01(\tR\x05party\x12;\n\x08\x63ommands\x18\x08 \x03(\x0b\x32\x1f.com.daml.ledger.api.v1.CommandR\x08\x63ommands\x12N\n\x12\x64\x65\x64uplication_time\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationB\x02\x18\x01H\x00R\x11\x64\x65\x64uplicationTime\x12R\n\x16\x64\x65\x64uplication_duration\x18\x0f \x01(\x0b\x32\x19.google.protobuf.DurationH\x00R\x15\x64\x65\x64uplicationDuration\x12\x33\n\x14\x64\x65\x64uplication_offset\x18\x10 \x01(\tH\x00R\x13\x64\x65\x64uplicationOffset\x12I\n\x13min_ledger_time_abs\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10minLedgerTimeAbs\x12H\n\x13min_ledger_time_rel\x18\x0b \x01(\x0b\x32\x19.google.protobuf.DurationR\x10minLedgerTimeRel\x12\x15\n\x06\x61\x63t_as\x18\x0c \x03(\tR\x05\x61\x63tAs\x12\x17\n\x07read_as\x18\r \x03(\tR\x06readAs\x12#\n\rsubmission_id\x18\x0e \x01(\tR\x0csubmissionId\x12Z\n\x13\x64isclosed_contracts\x18\x11 \x03(\x0b\x32).com.daml.ledger.api.v1.DisclosedContractR\x12\x64isclosedContracts\x12\x45\n\x1fpackage_id_selection_preference\x18\x12 \x03(\tR\x1cpackageIdSelectionPreferenceB\x16\n\x14\x64\x65\x64uplication_periodJ\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08\"\xd4\x02\n\x07\x43ommand\x12?\n\x06\x63reate\x18\x01 \x01(\x0b\x32%.com.daml.ledger.api.v1.CreateCommandH\x00R\x06\x63reate\x12\x45\n\x08\x65xercise\x18\x02 \x01(\x0b\x32\'.com.daml.ledger.api.v1.ExerciseCommandH\x00R\x08\x65xercise\x12T\n\rexerciseByKey\x18\x04 \x01(\x0b\x32,.com.daml.ledger.api.v1.ExerciseByKeyCommandH\x00R\rexerciseByKey\x12`\n\x11\x63reateAndExercise\x18\x03 \x01(\x0b\x32\x30.com.daml.ledger.api.v1.CreateAndExerciseCommandH\x00R\x11\x63reateAndExerciseB\t\n\x07\x63ommand\"\x9f\x01\n\rCreateCommand\x12\x43\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12I\n\x10\x63reate_arguments\x18\x02 \x01(\x0b\x32\x1e.com.daml.ledger.api.v1.RecordR\x0f\x63reateArguments\"\xd7\x01\n\x0f\x45xerciseCommand\x12\x43\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12\x1f\n\x0b\x63ontract_id\x18\x02 \x01(\tR\ncontractId\x12\x16\n\x06\x63hoice\x18\x03 \x01(\tR\x06\x63hoice\x12\x46\n\x0f\x63hoice_argument\x18\x04 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0e\x63hoiceArgument\"\xfd\x01\n\x14\x45xerciseByKeyCommand\x12\x43\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12@\n\x0c\x63ontract_key\x18\x02 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0b\x63ontractKey\x12\x16\n\x06\x63hoice\x18\x03 \x01(\tR\x06\x63hoice\x12\x46\n\x0f\x63hoice_argument\x18\x04 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0e\x63hoiceArgument\"\x8a\x02\n\x18\x43reateAndExerciseCommand\x12\x43\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12I\n\x10\x63reate_arguments\x18\x02 \x01(\x0b\x32\x1e.com.daml.ledger.api.v1.RecordR\x0f\x63reateArguments\x12\x16\n\x06\x63hoice\x18\x03 \x01(\tR\x06\x63hoice\x12\x46\n\x0f\x63hoice_argument\x18\x04 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0e\x63hoiceArgument\"\xb9\x01\n\x11\x44isclosedContract\x12\x43\n\x0btemplate_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12\x1f\n\x0b\x63ontract_id\x18\x02 \x01(\tR\ncontractId\x12,\n\x12\x63reated_event_blob\x18\x06 \x01(\x0cR\x10\x63reatedEventBlobJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\x42\x8c\x01\n\x16\x63om.daml.ledger.api.v1B\x12\x43ommandsOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.commands_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v1B\022CommandsOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _globals['_COMMANDS'].fields_by_name['deduplication_time']._loaded_options = None
  _globals['_COMMANDS'].fields_by_name['deduplication_time']._serialized_options = b'\030\001'
  _globals['_COMMANDS']._serialized_start=167
  _globals['_COMMANDS']._serialized_end=1042
  _globals['_COMMAND']._serialized_start=1045
  _globals['_COMMAND']._serialized_end=1385
  _globals['_CREATECOMMAND']._serialized_start=1388
  _globals['_CREATECOMMAND']._serialized_end=1547
  _globals['_EXERCISECOMMAND']._serialized_start=1550
  _globals['_EXERCISECOMMAND']._serialized_end=1765
  _globals['_EXERCISEBYKEYCOMMAND']._serialized_start=1768
  _globals['_EXERCISEBYKEYCOMMAND']._serialized_end=2021
  _globals['_CREATEANDEXERCISECOMMAND']._serialized_start=2024
  _globals['_CREATEANDEXERCISECOMMAND']._serialized_end=2290
  _globals['_DISCLOSEDCONTRACT']._serialized_start=2293
  _globals['_DISCLOSEDCONTRACT']._serialized_end=2478
# @@protoc_insertion_point(module_scope)
