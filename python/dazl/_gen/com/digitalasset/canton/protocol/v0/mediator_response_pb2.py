# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/protocol/v0/mediator_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;com/digitalasset/canton/protocol/v0/mediator_response.proto\x12#com.digitalasset.canton.protocol.v0\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc3\x02\n\x10MediatorResponse\x12\x39\n\nrequest_id\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\trequestId\x12\x16\n\x06sender\x18\x02 \x01(\tR\x06sender\x12\x1b\n\tview_hash\x18\x03 \x01(\x0cR\x08viewHash\x12V\n\rlocal_verdict\x18\x04 \x01(\x0b\x32\x31.com.digitalasset.canton.protocol.v0.LocalVerdictR\x0clocalVerdict\x12\x1b\n\troot_hash\x18\x05 \x01(\x0cR\x08rootHash\x12-\n\x12\x63onfirming_parties\x18\x06 \x03(\tR\x11\x63onfirmingParties\x12\x1b\n\tdomain_id\x18\x07 \x01(\tR\x08\x64omainId\"\xba\x01\n\x0cLocalVerdict\x12=\n\rlocal_approve\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x0clocalApprove\x12U\n\x0clocal_reject\x18\x02 \x01(\x0b\x32\x30.com.digitalasset.canton.protocol.v0.LocalRejectH\x00R\x0blocalRejectB\x14\n\x12some_local_verdict\"\xd2\x04\n\x0bLocalReject\x12I\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x35.com.digitalasset.canton.protocol.v0.LocalReject.CodeR\x04\x63ode\x12\x16\n\x06reason\x18\x02 \x01(\tR\x06reason\x12\x1a\n\x08resource\x18\x03 \x03(\tR\x08resource\"\xc3\x03\n\x04\x43ode\x12\x0f\n\x0bMissingCode\x10\x00\x12\x13\n\x0fLockedContracts\x10\x01\x12\x0e\n\nLockedKeys\x10\x02\x12\x15\n\x11InactiveContracts\x10\x03\x12\x10\n\x0c\x44uplicateKey\x10\x04\x12\x1b\n\x17\x43reatesExistingContract\x10\x05\x12\x0e\n\nLedgerTime\x10\x06\x12\x12\n\x0eSubmissionTime\x10\x07\x12\x10\n\x0cLocalTimeout\x10\x08\x12\x15\n\x11MalformedPayloads\x10\t\x12\x12\n\x0eMalformedModel\x10\n\x12\x1f\n\x1bMalformedConfirmationPolicy\x10\x0b\x12\x16\n\x12\x42\x61\x64RootHashMessage\x10\x0c\x12\x1e\n\x1aTransferOutActivenessCheck\x10\r\x12\x1e\n\x1aTransferInAlreadyCompleted\x10\x0e\x12\x1b\n\x17TransferInAlreadyActive\x10\x0f\x12\x1d\n\x19TransferInAlreadyArchived\x10\x10\x12\x14\n\x10TransferInLocked\x10\x11\x12\x13\n\x0fInconsistentKey\x10\x12\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v0.mediator_response_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MEDIATORRESPONSE']._serialized_start=163
  _globals['_MEDIATORRESPONSE']._serialized_end=486
  _globals['_LOCALVERDICT']._serialized_start=489
  _globals['_LOCALVERDICT']._serialized_end=675
  _globals['_LOCALREJECT']._serialized_start=678
  _globals['_LOCALREJECT']._serialized_end=1272
  _globals['_LOCALREJECT_CODE']._serialized_start=821
  _globals['_LOCALREJECT_CODE']._serialized_end=1272
# @@protoc_insertion_point(module_scope)
