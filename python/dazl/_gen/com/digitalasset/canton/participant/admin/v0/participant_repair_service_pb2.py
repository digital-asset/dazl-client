# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/participant/admin/v0/participant_repair_service.proto
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
    'com/digitalasset/canton/participant/admin/v0/participant_repair_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import domain_connectivity_pb2 as com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMcom/digitalasset/canton/participant/admin/v0/participant_repair_service.proto\x12,com.digitalasset.canton.participant.admin.v0\x1a\x46\x63om/digitalasset/canton/participant/admin/v0/domain_connectivity.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa5\x04\n\x0f\x44ownloadRequest\x12\x18\n\x07parties\x18\x01 \x03(\tR\x07parties\x12(\n\x10\x66ilter_domain_id\x18\x02 \x01(\tR\x0e\x66ilterDomainId\x12\x38\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12)\n\x10protocol_version\x18\x04 \x01(\tR\x0fprotocolVersion\x12:\n\tchunkSize\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\tchunkSize\x12\x1f\n\x0bgzip_format\x18\x06 \x01(\x08R\ngzipFormat\x12\x90\x01\n\x17\x63ontract_domain_renames\x18\x07 \x03(\x0b\x32X.com.digitalasset.canton.participant.admin.v0.DownloadRequest.ContractDomainRenamesEntryR\x15\x63ontractDomainRenames\x12/\n\x13parties_offboarding\x18\x08 \x01(\x08R\x12partiesOffboarding\x1aH\n\x1a\x43ontractDomainRenamesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xb5\x01\n\x15PurgeContractsRequest\x12\x16\n\x06\x64omain\x18\x01 \x01(\tR\x06\x64omain\x12!\n\x0c\x63ontract_ids\x18\x02 \x03(\tR\x0b\x63ontractIds\x12\x32\n\x15ignore_already_purged\x18\x03 \x01(\x08R\x13ignoreAlreadyPurged\x12-\n\x12offboarded_parties\x18\x04 \x03(\tR\x11offboardedParties\"\x18\n\x16PurgeContractsResponse\"(\n\x10\x41\x63sSnapshotChunk\x12\x14\n\x05\x63hunk\x18\x01 \x01(\x0cR\x05\x63hunk\"S\n\rUploadRequest\x12!\n\x0c\x61\x63s_snapshot\x18\x01 \x01(\x0cR\x0b\x61\x63sSnapshot\x12\x1f\n\x0bgzip_format\x18\x02 \x01(\x08R\ngzipFormat\"\x10\n\x0eUploadResponse\"\xf9\x01\n\x14MigrateDomainRequest\x12!\n\x0csource_alias\x18\x01 \x01(\tR\x0bsourceAlias\x12\x8b\x01\n\x1ftarget_domain_connection_config\x18\x02 \x01(\x0b\x32\x44.com.digitalasset.canton.participant.admin.v0.DomainConnectionConfigR\x1ctargetDomainConnectionConfig\x12\x30\n\x05\x66orce\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x05\x66orce\"\x17\n\x15MigrateDomainResponse\"t\n\x0e\x41\x63tiveContract\x12)\n\x10protocol_version\x18\x01 \x01(\x05R\x0fprotocolVersion\x12\x1b\n\tdomain_id\x18\x02 \x01(\tR\x08\x64omainId\x12\x1a\n\x08\x63ontract\x18\x03 \x01(\x0cR\x08\x63ontract\"\xc5\x04\n\x10\x45xportAcsRequest\x12\x18\n\x07parties\x18\x01 \x03(\tR\x07parties\x12(\n\x10\x66ilter_domain_id\x18\x02 \x01(\tR\x0e\x66ilterDomainId\x12\x38\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12\x91\x01\n\x17\x63ontract_domain_renames\x18\x04 \x03(\x0b\x32Y.com.digitalasset.canton.participant.admin.v0.ExportAcsRequest.ContractDomainRenamesEntryR\x15\x63ontractDomainRenames\x12/\n\x13parties_offboarding\x18\x05 \x01(\x08R\x12partiesOffboarding\x1aV\n\x0cTargetDomain\x12\x1b\n\tdomain_id\x18\x01 \x01(\tR\x08\x64omainId\x12)\n\x10protocol_version\x18\x02 \x01(\x05R\x0fprotocolVersion\x1a\x95\x01\n\x1a\x43ontractDomainRenamesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x61\n\x05value\x18\x02 \x01(\x0b\x32K.com.digitalasset.canton.participant.admin.v0.ExportAcsRequest.TargetDomainR\x05value:\x02\x38\x01\")\n\x11\x45xportAcsResponse\x12\x14\n\x05\x63hunk\x18\x01 \x01(\x0cR\x05\x63hunk\"\x90\x01\n\x10ImportAcsRequest\x12!\n\x0c\x61\x63s_snapshot\x18\x01 \x01(\x0cR\x0b\x61\x63sSnapshot\x12,\n\x12workflow_id_prefix\x18\x02 \x01(\tR\x10workflowIdPrefix\x12+\n\x11onboarded_parties\x18\x03 \x03(\tR\x10onboardedParties\"\x13\n\x11ImportAcsResponse\"B\n\x1dPurgeDeactivatedDomainRequest\x12!\n\x0c\x64omain_alias\x18\x01 \x01(\tR\x0b\x64omainAlias\" \n\x1ePurgeDeactivatedDomainResponse\"\x92\x01\n\x13IgnoreEventsRequest\x12\x1b\n\tdomain_id\x18\x01 \x01(\tR\x08\x64omainId\x12%\n\x0e\x66rom_inclusive\x18\x02 \x01(\x03R\rfromInclusive\x12!\n\x0cto_inclusive\x18\x03 \x01(\x03R\x0btoInclusive\x12\x14\n\x05\x66orce\x18\x04 \x01(\x08R\x05\x66orce\"\x16\n\x14IgnoreEventsResponse\"\x94\x01\n\x15UnignoreEventsRequest\x12\x1b\n\tdomain_id\x18\x01 \x01(\tR\x08\x64omainId\x12%\n\x0e\x66rom_inclusive\x18\x02 \x01(\x03R\rfromInclusive\x12!\n\x0cto_inclusive\x18\x03 \x01(\x03R\x0btoInclusive\x12\x14\n\x05\x66orce\x18\x04 \x01(\x08R\x05\x66orce\"\x18\n\x16UnignoreEventsResponse2\xf7\n\n\x18ParticipantRepairService\x12\x8b\x01\n\x08\x44ownload\x12=.com.digitalasset.canton.participant.admin.v0.DownloadRequest\x1a>.com.digitalasset.canton.participant.admin.v0.AcsSnapshotChunk0\x01\x12\x8e\x01\n\tExportAcs\x12>.com.digitalasset.canton.participant.admin.v0.ExportAcsRequest\x1a?.com.digitalasset.canton.participant.admin.v0.ExportAcsResponse0\x01\x12\x85\x01\n\x06Upload\x12;.com.digitalasset.canton.participant.admin.v0.UploadRequest\x1a<.com.digitalasset.canton.participant.admin.v0.UploadResponse(\x01\x12\x8e\x01\n\tImportAcs\x12>.com.digitalasset.canton.participant.admin.v0.ImportAcsRequest\x1a?.com.digitalasset.canton.participant.admin.v0.ImportAcsResponse(\x01\x12\x9b\x01\n\x0ePurgeContracts\x12\x43.com.digitalasset.canton.participant.admin.v0.PurgeContractsRequest\x1a\x44.com.digitalasset.canton.participant.admin.v0.PurgeContractsResponse\x12\x98\x01\n\rMigrateDomain\x12\x42.com.digitalasset.canton.participant.admin.v0.MigrateDomainRequest\x1a\x43.com.digitalasset.canton.participant.admin.v0.MigrateDomainResponse\x12\xb3\x01\n\x16PurgeDeactivatedDomain\x12K.com.digitalasset.canton.participant.admin.v0.PurgeDeactivatedDomainRequest\x1aL.com.digitalasset.canton.participant.admin.v0.PurgeDeactivatedDomainResponse\x12\x95\x01\n\x0cIgnoreEvents\x12\x41.com.digitalasset.canton.participant.admin.v0.IgnoreEventsRequest\x1a\x42.com.digitalasset.canton.participant.admin.v0.IgnoreEventsResponse\x12\x9b\x01\n\x0eUnignoreEvents\x12\x43.com.digitalasset.canton.participant.admin.v0.UnignoreEventsRequest\x1a\x44.com.digitalasset.canton.participant.admin.v0.UnignoreEventsResponseB]Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.participant.admin.v0.participant_repair_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z[github.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/participant/admin/v0'
  _globals['_DOWNLOADREQUEST_CONTRACTDOMAINRENAMESENTRY']._loaded_options = None
  _globals['_DOWNLOADREQUEST_CONTRACTDOMAINRENAMESENTRY']._serialized_options = b'8\001'
  _globals['_EXPORTACSREQUEST_CONTRACTDOMAINRENAMESENTRY']._loaded_options = None
  _globals['_EXPORTACSREQUEST_CONTRACTDOMAINRENAMESENTRY']._serialized_options = b'8\001'
  _globals['_DOWNLOADREQUEST']._serialized_start=265
  _globals['_DOWNLOADREQUEST']._serialized_end=814
  _globals['_DOWNLOADREQUEST_CONTRACTDOMAINRENAMESENTRY']._serialized_start=742
  _globals['_DOWNLOADREQUEST_CONTRACTDOMAINRENAMESENTRY']._serialized_end=814
  _globals['_PURGECONTRACTSREQUEST']._serialized_start=817
  _globals['_PURGECONTRACTSREQUEST']._serialized_end=998
  _globals['_PURGECONTRACTSRESPONSE']._serialized_start=1000
  _globals['_PURGECONTRACTSRESPONSE']._serialized_end=1024
  _globals['_ACSSNAPSHOTCHUNK']._serialized_start=1026
  _globals['_ACSSNAPSHOTCHUNK']._serialized_end=1066
  _globals['_UPLOADREQUEST']._serialized_start=1068
  _globals['_UPLOADREQUEST']._serialized_end=1151
  _globals['_UPLOADRESPONSE']._serialized_start=1153
  _globals['_UPLOADRESPONSE']._serialized_end=1169
  _globals['_MIGRATEDOMAINREQUEST']._serialized_start=1172
  _globals['_MIGRATEDOMAINREQUEST']._serialized_end=1421
  _globals['_MIGRATEDOMAINRESPONSE']._serialized_start=1423
  _globals['_MIGRATEDOMAINRESPONSE']._serialized_end=1446
  _globals['_ACTIVECONTRACT']._serialized_start=1448
  _globals['_ACTIVECONTRACT']._serialized_end=1564
  _globals['_EXPORTACSREQUEST']._serialized_start=1567
  _globals['_EXPORTACSREQUEST']._serialized_end=2148
  _globals['_EXPORTACSREQUEST_TARGETDOMAIN']._serialized_start=1910
  _globals['_EXPORTACSREQUEST_TARGETDOMAIN']._serialized_end=1996
  _globals['_EXPORTACSREQUEST_CONTRACTDOMAINRENAMESENTRY']._serialized_start=1999
  _globals['_EXPORTACSREQUEST_CONTRACTDOMAINRENAMESENTRY']._serialized_end=2148
  _globals['_EXPORTACSRESPONSE']._serialized_start=2150
  _globals['_EXPORTACSRESPONSE']._serialized_end=2191
  _globals['_IMPORTACSREQUEST']._serialized_start=2194
  _globals['_IMPORTACSREQUEST']._serialized_end=2338
  _globals['_IMPORTACSRESPONSE']._serialized_start=2340
  _globals['_IMPORTACSRESPONSE']._serialized_end=2359
  _globals['_PURGEDEACTIVATEDDOMAINREQUEST']._serialized_start=2361
  _globals['_PURGEDEACTIVATEDDOMAINREQUEST']._serialized_end=2427
  _globals['_PURGEDEACTIVATEDDOMAINRESPONSE']._serialized_start=2429
  _globals['_PURGEDEACTIVATEDDOMAINRESPONSE']._serialized_end=2461
  _globals['_IGNOREEVENTSREQUEST']._serialized_start=2464
  _globals['_IGNOREEVENTSREQUEST']._serialized_end=2610
  _globals['_IGNOREEVENTSRESPONSE']._serialized_start=2612
  _globals['_IGNOREEVENTSRESPONSE']._serialized_end=2634
  _globals['_UNIGNOREEVENTSREQUEST']._serialized_start=2637
  _globals['_UNIGNOREEVENTSREQUEST']._serialized_end=2785
  _globals['_UNIGNOREEVENTSRESPONSE']._serialized_start=2787
  _globals['_UNIGNOREEVENTSRESPONSE']._serialized_end=2811
  _globals['_PARTICIPANTREPAIRSERVICE']._serialized_start=2814
  _globals['_PARTICIPANTREPAIRSERVICE']._serialized_end=4213
# @@protoc_insertion_point(module_scope)
