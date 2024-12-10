# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/reassignment_command.proto
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
    'com/daml/ledger/api/v2/reassignment_command.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1com/daml/ledger/api/v2/reassignment_command.proto\x12\x16\x63om.daml.ledger.api.v2\"\xf0\x02\n\x13ReassignmentCommand\x12\x1f\n\x0bworkflow_id\x18\x01 \x01(\tR\nworkflowId\x12%\n\x0e\x61pplication_id\x18\x02 \x01(\tR\rapplicationId\x12\x1d\n\ncommand_id\x18\x03 \x01(\tR\tcommandId\x12\x1c\n\tsubmitter\x18\x04 \x01(\tR\tsubmitter\x12T\n\x10unassign_command\x18\x05 \x01(\x0b\x32\'.com.daml.ledger.api.v2.UnassignCommandH\x00R\x0funassignCommand\x12N\n\x0e\x61ssign_command\x18\x06 \x01(\x0b\x32%.com.daml.ledger.api.v2.AssignCommandH\x00R\rassignCommand\x12#\n\rsubmission_id\x18\x07 \x01(\tR\x0csubmissionIdB\t\n\x07\x63ommand\"b\n\x0fUnassignCommand\x12\x1f\n\x0b\x63ontract_id\x18\x01 \x01(\tR\ncontractId\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\x12\x16\n\x06target\x18\x03 \x01(\tR\x06target\"`\n\rAssignCommand\x12\x1f\n\x0bunassign_id\x18\x01 \x01(\tR\nunassignId\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\x12\x16\n\x06target\x18\x03 \x01(\tR\x06targetB\x97\x01\n\x16\x63om.daml.ledger.api.v2B\x1dReassignmentCommandOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.reassignment_command_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\035ReassignmentCommandOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_REASSIGNMENTCOMMAND']._serialized_start=78
  _globals['_REASSIGNMENTCOMMAND']._serialized_end=446
  _globals['_UNASSIGNCOMMAND']._serialized_start=448
  _globals['_UNASSIGNCOMMAND']._serialized_end=546
  _globals['_ASSIGNCOMMAND']._serialized_start=548
  _globals['_ASSIGNCOMMAND']._serialized_end=644
# @@protoc_insertion_point(module_scope)