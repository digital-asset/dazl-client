# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/participant/admin/v0/transfer_service.proto
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
    'com/digitalasset/canton/participant/admin/v0/transfer_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....protocol.v0 import participant_transfer_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_participant__transfer__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCcom/digitalasset/canton/participant/admin/v0/transfer_service.proto\x12,com.digitalasset.canton.participant.admin.v0\x1a>com/digitalasset/canton/protocol/v0/participant_transfer.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbb\x02\n\x17\x41\x64minTransferOutRequest\x12)\n\x10submitting_party\x18\x01 \x01(\tR\x0fsubmittingParty\x12\x1f\n\x0b\x63ontract_id\x18\x02 \x01(\tR\ncontractId\x12#\n\rorigin_domain\x18\x03 \x01(\tR\x0coriginDomain\x12#\n\rtarget_domain\x18\x04 \x01(\tR\x0ctargetDomain\x12%\n\x0e\x61pplication_id\x18\x05 \x01(\tR\rapplicationId\x12#\n\rsubmission_id\x18\x06 \x01(\tR\x0csubmissionId\x12\x1f\n\x0bworkflow_id\x18\x07 \x01(\tR\nworkflowId\x12\x1d\n\ncommand_id\x18\x08 \x01(\tR\tcommandId\"l\n\x18\x41\x64minTransferOutResponse\x12P\n\x0btransfer_id\x18\x01 \x01(\x0b\x32/.com.digitalasset.canton.protocol.v0.TransferIdR\ntransferId\"\xcb\x02\n\x16\x41\x64minTransferInRequest\x12.\n\x13submitting_party_id\x18\x01 \x01(\tR\x11submittingPartyId\x12#\n\rtarget_domain\x18\x02 \x01(\tR\x0ctargetDomain\x12P\n\x0btransfer_id\x18\x03 \x01(\x0b\x32/.com.digitalasset.canton.protocol.v0.TransferIdR\ntransferId\x12%\n\x0e\x61pplication_id\x18\x04 \x01(\tR\rapplicationId\x12#\n\rsubmission_id\x18\x05 \x01(\tR\x0csubmissionId\x12\x1f\n\x0bworkflow_id\x18\x06 \x01(\tR\nworkflowId\x12\x1d\n\ncommand_id\x18\x07 \x01(\tR\tcommandId\"\x19\n\x17\x41\x64minTransferInResponse\"\x86\x02\n\x18\x41\x64minTransferSearchQuery\x12#\n\rsearch_domain\x18\x01 \x01(\tR\x0csearchDomain\x12\x30\n\x14\x66ilter_origin_domain\x18\x02 \x01(\tR\x12\x66ilterOriginDomain\x12\x45\n\x10\x66ilter_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x66ilterTimestamp\x12\x36\n\x17\x66ilter_submitting_party\x18\x04 \x01(\tR\x15\x66ilterSubmittingParty\x12\x14\n\x05limit\x18\x05 \x01(\x03R\x05limit\"\x93\x04\n\x1b\x41\x64minTransferSearchResponse\x12x\n\x07results\x18\x01 \x03(\x0b\x32^.com.digitalasset.canton.participant.admin.v0.AdminTransferSearchResponse.TransferSearchResultR\x07results\x1a\xf9\x02\n\x14TransferSearchResult\x12\x1f\n\x0b\x63ontract_id\x18\x01 \x01(\tR\ncontractId\x12P\n\x0btransfer_id\x18\x02 \x01(\x0b\x32/.com.digitalasset.canton.protocol.v0.TransferIdR\ntransferId\x12#\n\rorigin_domain\x18\x03 \x01(\tR\x0coriginDomain\x12#\n\rtarget_domain\x18\x04 \x01(\tR\x0ctargetDomain\x12)\n\x10submitting_party\x18\x05 \x01(\tR\x0fsubmittingParty\x12\x31\n\x15ready_for_transfer_in\x18\x06 \x01(\x08R\x12readyForTransferIn\x12\x46\n\x11target_time_proof\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0ftargetTimeProof2\xf2\x03\n\x0fTransferService\x12\x9c\x01\n\x0bTransferOut\x12\x45.com.digitalasset.canton.participant.admin.v0.AdminTransferOutRequest\x1a\x46.com.digitalasset.canton.participant.admin.v0.AdminTransferOutResponse\x12\x99\x01\n\nTransferIn\x12\x44.com.digitalasset.canton.participant.admin.v0.AdminTransferInRequest\x1a\x45.com.digitalasset.canton.participant.admin.v0.AdminTransferInResponse\x12\xa3\x01\n\x0eTransferSearch\x12\x46.com.digitalasset.canton.participant.admin.v0.AdminTransferSearchQuery\x1aI.com.digitalasset.canton.participant.admin.v0.AdminTransferSearchResponseB]Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.participant.admin.v0.transfer_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0'
  _globals['_ADMINTRANSFEROUTREQUEST']._serialized_start=215
  _globals['_ADMINTRANSFEROUTREQUEST']._serialized_end=530
  _globals['_ADMINTRANSFEROUTRESPONSE']._serialized_start=532
  _globals['_ADMINTRANSFEROUTRESPONSE']._serialized_end=640
  _globals['_ADMINTRANSFERINREQUEST']._serialized_start=643
  _globals['_ADMINTRANSFERINREQUEST']._serialized_end=974
  _globals['_ADMINTRANSFERINRESPONSE']._serialized_start=976
  _globals['_ADMINTRANSFERINRESPONSE']._serialized_end=1001
  _globals['_ADMINTRANSFERSEARCHQUERY']._serialized_start=1004
  _globals['_ADMINTRANSFERSEARCHQUERY']._serialized_end=1266
  _globals['_ADMINTRANSFERSEARCHRESPONSE']._serialized_start=1269
  _globals['_ADMINTRANSFERSEARCHRESPONSE']._serialized_end=1800
  _globals['_ADMINTRANSFERSEARCHRESPONSE_TRANSFERSEARCHRESULT']._serialized_start=1423
  _globals['_ADMINTRANSFERSEARCHRESPONSE_TRANSFERSEARCHRESULT']._serialized_end=1800
  _globals['_TRANSFERSERVICE']._serialized_start=1803
  _globals['_TRANSFERSERVICE']._serialized_end=2301
# @@protoc_insertion_point(module_scope)
