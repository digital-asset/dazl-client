# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto
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
    'com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ledger_sync_event_pb2 as com_dot_digitalasset_dot_canton_dot_participant_dot_protocol_dot_v30_dot_ledger__sync__event__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJcom/digitalasset/canton/participant/protocol/v30/submission_tracking.proto\x12\x30\x63om.digitalasset.canton.participant.protocol.v30\x1aHcom/digitalasset/canton/participant/protocol/v30/ledger_sync_event.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x9d\x01\n\x16SubmissionTrackingData\x12w\n\x0btransaction\x18\x01 \x01(\x0b\x32S.com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingDataH\x00R\x0btransactionB\n\n\x08tracking\"\xa7\x04\n!TransactionSubmissionTrackingData\x12i\n\x0f\x63ompletion_info\x18\x01 \x01(\x0b\x32@.com.digitalasset.canton.participant.protocol.v30.CompletionInfoR\x0e\x63ompletionInfo\x12\x8b\x01\n\x0frejection_cause\x18\x02 \x01(\x0b\x32\x62.com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingData.RejectionCauseR\x0erejectionCause\x12\x1b\n\tdomain_id\x18\x03 \x01(\tR\x08\x64omainId\x1a\xeb\x01\n\x0eRejectionCause\x12\x32\n\x07timeout\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x07timeout\x12\x9b\x01\n\x19rejection_reason_template\x18\x02 \x01(\x0b\x32].com.digitalasset.canton.participant.protocol.v30.CommandRejected.GrpcRejectionReasonTemplateH\x00R\x17rejectionReasonTemplateB\x07\n\x05\x63\x61useBaZ_github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/protocol/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.participant.protocol.v30.submission_tracking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z_github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/protocol/v30'
  _globals['_SUBMISSIONTRACKINGDATA']._serialized_start=232
  _globals['_SUBMISSIONTRACKINGDATA']._serialized_end=389
  _globals['_TRANSACTIONSUBMISSIONTRACKINGDATA']._serialized_start=392
  _globals['_TRANSACTIONSUBMISSIONTRACKINGDATA']._serialized_end=943
  _globals['_TRANSACTIONSUBMISSIONTRACKINGDATA_REJECTIONCAUSE']._serialized_start=708
  _globals['_TRANSACTIONSUBMISSIONTRACKINGDATA_REJECTIONCAUSE']._serialized_end=943
# @@protoc_insertion_point(module_scope)
