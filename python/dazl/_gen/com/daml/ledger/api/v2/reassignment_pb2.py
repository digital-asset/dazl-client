# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/reassignment.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'com/daml/ledger/api/v2/reassignment.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import event_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_event__pb2
from . import trace_context_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_trace__context__pb2
from . import value_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_value__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)com/daml/ledger/api/v2/reassignment.proto\x12\x16\x63om.daml.ledger.api.v2\x1a\"com/daml/ledger/api/v2/event.proto\x1a*com/daml/ledger/api/v2/trace_context.proto\x1a\"com/daml/ledger/api/v2/value.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xba\x03\n\x0cReassignment\x12\x1b\n\tupdate_id\x18\x01 \x01(\tR\x08updateId\x12\x1d\n\ncommand_id\x18\x02 \x01(\tR\tcommandId\x12\x1f\n\x0bworkflow_id\x18\x03 \x01(\tR\nworkflowId\x12\x16\n\x06offset\x18\x04 \x01(\x03R\x06offset\x12T\n\x10unassigned_event\x18\x05 \x01(\x0b\x32\'.com.daml.ledger.api.v2.UnassignedEventH\x00R\x0funassignedEvent\x12N\n\x0e\x61ssigned_event\x18\x06 \x01(\x0b\x32%.com.daml.ledger.api.v2.AssignedEventH\x00R\rassignedEvent\x12I\n\rtrace_context\x18\x07 \x01(\x0b\x32$.com.daml.ledger.api.v2.TraceContextR\x0ctraceContext\x12;\n\x0brecord_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nrecordTimeB\x07\n\x05\x65vent\"\xb8\x03\n\x0fUnassignedEvent\x12\x1f\n\x0bunassign_id\x18\x01 \x01(\tR\nunassignId\x12\x1f\n\x0b\x63ontract_id\x18\x02 \x01(\tR\ncontractId\x12\x43\n\x0btemplate_id\x18\x03 \x01(\x0b\x32\".com.daml.ledger.api.v2.IdentifierR\ntemplateId\x12\x16\n\x06source\x18\x04 \x01(\tR\x06source\x12\x16\n\x06target\x18\x05 \x01(\tR\x06target\x12\x1c\n\tsubmitter\x18\x06 \x01(\tR\tsubmitter\x12\x31\n\x14reassignment_counter\x18\x07 \x01(\x04R\x13reassignmentCounter\x12Q\n\x16\x61ssignment_exclusivity\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x15\x61ssignmentExclusivity\x12\'\n\x0fwitness_parties\x18\t \x03(\tR\x0ewitnessParties\x12!\n\x0cpackage_name\x18\n \x01(\tR\x0bpackageName\"\xfc\x01\n\rAssignedEvent\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12\x16\n\x06target\x18\x02 \x01(\tR\x06target\x12\x1f\n\x0bunassign_id\x18\x03 \x01(\tR\nunassignId\x12\x1c\n\tsubmitter\x18\x04 \x01(\tR\tsubmitter\x12\x31\n\x14reassignment_counter\x18\x05 \x01(\x04R\x13reassignmentCounter\x12I\n\rcreated_event\x18\x06 \x01(\x0b\x32$.com.daml.ledger.api.v2.CreatedEventR\x0c\x63reatedEventB\x90\x01\n\x16\x63om.daml.ledger.api.v2B\x16ReassignmentOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\xaa\x02\x16\x43om.Daml.Ledger.Api.V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.reassignment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v2B\026ReassignmentOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2\252\002\026Com.Daml.Ledger.Api.V2'
  _globals['_REASSIGNMENT']._serialized_start=219
  _globals['_REASSIGNMENT']._serialized_end=661
  _globals['_UNASSIGNEDEVENT']._serialized_start=664
  _globals['_UNASSIGNEDEVENT']._serialized_end=1104
  _globals['_ASSIGNEDEVENT']._serialized_start=1107
  _globals['_ASSIGNEDEVENT']._serialized_end=1359
# @@protoc_insertion_point(module_scope)
