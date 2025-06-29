# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v30/mediator.proto
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
    'com/digitalasset/canton/protocol/v30/mediator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_common__pb2
from . import confirmation_response_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_confirmation__response__pb2
from . import merkle_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_merkle__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3com/digitalasset/canton/protocol/v30/mediator.proto\x12$com.digitalasset.canton.protocol.v30\x1a\x31\x63om/digitalasset/canton/protocol/v30/common.proto\x1a@com/digitalasset/canton/protocol/v30/confirmation_response.proto\x1a\x31\x63om/digitalasset/canton/protocol/v30/merkle.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto\"\\\n\x0cInformeeTree\x12L\n\x04tree\x18\x01 \x01(\x0b\x32\x38.com.digitalasset.canton.protocol.v30.GenTransactionTreeR\x04tree\"d\n\x11ParticipantReject\x12O\n\x07reasons\x18\x01 \x03(\x0b\x32\x35.com.digitalasset.canton.protocol.v30.RejectionReasonR\x07reasons\"w\n\x0fRejectionReason\x12\x18\n\x07parties\x18\x01 \x03(\tR\x07parties\x12J\n\x06reject\x18\x02 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v30.LocalVerdictR\x06reject\"_\n\x0eMediatorReject\x12*\n\x06reason\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusR\x06reason\x12!\n\x0cis_malformed\x18\x02 \x01(\x08R\x0bisMalformed\"\x98\x02\n\x07Verdict\x12\x32\n\x07\x61pprove\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x07\x61pprove\x12h\n\x12participant_reject\x18\x02 \x01(\x0b\x32\x37.com.digitalasset.canton.protocol.v30.ParticipantRejectH\x00R\x11participantReject\x12_\n\x0fmediator_reject\x18\x03 \x01(\x0b\x32\x34.com.digitalasset.canton.protocol.v30.MediatorRejectH\x00R\x0emediatorRejectB\x0e\n\x0csome_verdict\"\x96\x02\n\x19\x43onfirmationResultMessage\x12\'\n\x0fsynchronizer_id\x18\x01 \x01(\tR\x0esynchronizerId\x12K\n\tview_type\x18\x02 \x01(\x0e\x32..com.digitalasset.canton.protocol.v30.ViewTypeR\x08viewType\x12\x1d\n\nrequest_id\x18\x03 \x01(\x03R\trequestId\x12\x1b\n\troot_hash\x18\x04 \x01(\x0cR\x08rootHash\x12G\n\x07verdict\x18\x05 \x01(\x0b\x32-.com.digitalasset.canton.protocol.v30.VerdictR\x07verdictBUZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v30.mediator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZSgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v30'
  _globals['_INFORMEETREE']._serialized_start=315
  _globals['_INFORMEETREE']._serialized_end=407
  _globals['_PARTICIPANTREJECT']._serialized_start=409
  _globals['_PARTICIPANTREJECT']._serialized_end=509
  _globals['_REJECTIONREASON']._serialized_start=511
  _globals['_REJECTIONREASON']._serialized_end=630
  _globals['_MEDIATORREJECT']._serialized_start=632
  _globals['_MEDIATORREJECT']._serialized_end=727
  _globals['_VERDICT']._serialized_start=730
  _globals['_VERDICT']._serialized_end=1010
  _globals['_CONFIRMATIONRESULTMESSAGE']._serialized_start=1013
  _globals['_CONFIRMATIONRESULTMESSAGE']._serialized_end=1291
# @@protoc_insertion_point(module_scope)
