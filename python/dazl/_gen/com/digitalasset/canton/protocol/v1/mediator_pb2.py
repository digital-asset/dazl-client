# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/protocol/v1/mediator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..v0 import common_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_common__pb2
from ..v0 import mediator_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_mediator__pb2
from . import merkle_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_merkle__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2com/digitalasset/canton/protocol/v1/mediator.proto\x12#com.digitalasset.canton.protocol.v1\x1a\x30\x63om/digitalasset/canton/protocol/v0/common.proto\x1a\x32\x63om/digitalasset/canton/protocol/v0/mediator.proto\x1a\x30\x63om/digitalasset/canton/protocol/v1/merkle.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfd\x01\n\x18TransactionResultMessage\x12\x39\n\nrequest_id\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\trequestId\x12\x46\n\x07verdict\x18\x02 \x01(\x0b\x32,.com.digitalasset.canton.protocol.v1.VerdictR\x07verdict\x12^\n\x11notification_tree\x18\x05 \x01(\x0b\x32\x31.com.digitalasset.canton.protocol.v1.InformeeTreeR\x10notificationTree\"\x9c\x02\n\x07Verdict\x12\x32\n\x07\x61pprove\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x07\x61pprove\x12g\n\x12participant_reject\x18\x02 \x01(\x0b\x32\x36.com.digitalasset.canton.protocol.v1.ParticipantRejectH\x00R\x11participantReject\x12^\n\x0fmediator_reject\x18\x03 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v1.MediatorRejectH\x00R\x0emediatorRejectB\x0e\n\x0csome_verdictJ\x04\x08\x04\x10\x05\"[\n\x0cInformeeTree\x12K\n\x04tree\x18\x01 \x01(\x0b\x32\x37.com.digitalasset.canton.protocol.v1.GenTransactionTreeR\x04tree\"c\n\x11ParticipantReject\x12N\n\x07reasons\x18\x01 \x03(\x0b\x32\x34.com.digitalasset.canton.protocol.v0.RejectionReasonR\x07reasons\"r\n\x0eMediatorReject\x12\x14\n\x05\x63\x61use\x18\x02 \x01(\tR\x05\x63\x61use\x12\x1d\n\nerror_code\x18\x03 \x01(\tR\terrorCode\x12%\n\x0e\x65rror_category\x18\x04 \x01(\rR\rerrorCategoryJ\x04\x08\x01\x10\x02\"\x97\x02\n\x1eMalformedMediatorRequestResult\x12\x39\n\nrequest_id\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\trequestId\x12\x1b\n\tdomain_id\x18\x02 \x01(\tR\x08\x64omainId\x12J\n\tview_type\x18\x03 \x01(\x0e\x32-.com.digitalasset.canton.protocol.v0.ViewTypeR\x08viewType\x12Q\n\trejection\x18\x04 \x01(\x0b\x32\x33.com.digitalasset.canton.protocol.v1.MediatorRejectR\trejection\"\x89\x02\n\x0eTransferResult\x12\x39\n\nrequest_id\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\trequestId\x12%\n\rorigin_domain\x18\x02 \x01(\tH\x00R\x0coriginDomain\x12%\n\rtarget_domain\x18\x03 \x01(\tH\x00R\x0ctargetDomain\x12\x1c\n\tinformees\x18\x04 \x03(\tR\tinformees\x12\x46\n\x07verdict\x18\x05 \x01(\x0b\x32,.com.digitalasset.canton.protocol.v1.VerdictR\x07verdictB\x08\n\x06\x64omainb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v1.mediator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRANSACTIONRESULTMESSAGE']._serialized_start=306
  _globals['_TRANSACTIONRESULTMESSAGE']._serialized_end=559
  _globals['_VERDICT']._serialized_start=562
  _globals['_VERDICT']._serialized_end=846
  _globals['_INFORMEETREE']._serialized_start=848
  _globals['_INFORMEETREE']._serialized_end=939
  _globals['_PARTICIPANTREJECT']._serialized_start=941
  _globals['_PARTICIPANTREJECT']._serialized_end=1040
  _globals['_MEDIATORREJECT']._serialized_start=1042
  _globals['_MEDIATORREJECT']._serialized_end=1156
  _globals['_MALFORMEDMEDIATORREQUESTRESULT']._serialized_start=1159
  _globals['_MALFORMEDMEDIATORREQUESTRESULT']._serialized_end=1438
  _globals['_TRANSFERRESULT']._serialized_start=1441
  _globals['_TRANSFERRESULT']._serialized_end=1706
# @@protoc_insertion_point(module_scope)
