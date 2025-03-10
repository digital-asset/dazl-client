# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v2/admin/party_management_service.proto
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
    'com/daml/ledger/api/v2/admin/party_management_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import object_meta_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_object__meta__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;com/daml/ledger/api/v2/admin/party_management_service.proto\x12\x1c\x63om.daml.ledger.api.v2.admin\x1a.com/daml/ledger/api/v2/admin/object_meta.proto\x1a google/protobuf/field_mask.proto\"\x19\n\x17GetParticipantIdRequest\"A\n\x18GetParticipantIdResponse\x12%\n\x0eparticipant_id\x18\x01 \x01(\tR\rparticipantId\"_\n\x11GetPartiesRequest\x12\x18\n\x07parties\x18\x01 \x03(\tR\x07parties\x12\x30\n\x14identity_provider_id\x18\x02 \x01(\tR\x12identityProviderId\"e\n\x12GetPartiesResponse\x12O\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v2.admin.PartyDetailsR\x0cpartyDetails\"\x87\x01\n\x17ListKnownPartiesRequest\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x30\n\x14identity_provider_id\x18\x01 \x01(\tR\x12identityProviderId\"\x93\x01\n\x18ListKnownPartiesResponse\x12O\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v2.admin.PartyDetailsR\x0cpartyDetails\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xe0\x01\n\x14\x41llocatePartyRequest\x12\"\n\rparty_id_hint\x18\x01 \x01(\tR\x0bpartyIdHint\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12O\n\x0elocal_metadata\x18\x03 \x01(\x0b\x32(.com.daml.ledger.api.v2.admin.ObjectMetaR\rlocalMetadata\x12\x30\n\x14identity_provider_id\x18\x04 \x01(\tR\x12identityProviderId\"h\n\x15\x41llocatePartyResponse\x12O\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v2.admin.PartyDetailsR\x0cpartyDetails\"\xa9\x01\n\x19UpdatePartyDetailsRequest\x12O\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v2.admin.PartyDetailsR\x0cpartyDetails\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"m\n\x1aUpdatePartyDetailsResponse\x12O\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v2.admin.PartyDetailsR\x0cpartyDetails\"\xe5\x01\n\x0cPartyDetails\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x19\n\x08is_local\x18\x03 \x01(\x08R\x07isLocal\x12O\n\x0elocal_metadata\x18\x04 \x01(\x0b\x32(.com.daml.ledger.api.v2.admin.ObjectMetaR\rlocalMetadata\x12\x30\n\x14identity_provider_id\x18\x05 \x01(\tR\x12identityProviderId\"\xba\x01\n$UpdatePartyIdentityProviderIdRequest\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12=\n\x1bsource_identity_provider_id\x18\x02 \x01(\tR\x18sourceIdentityProviderId\x12=\n\x1btarget_identity_provider_id\x18\x03 \x01(\tR\x18targetIdentityProviderId\"\'\n%UpdatePartyIdentityProviderIdResponse2\xc0\x06\n\x16PartyManagementService\x12\x81\x01\n\x10GetParticipantId\x12\x35.com.daml.ledger.api.v2.admin.GetParticipantIdRequest\x1a\x36.com.daml.ledger.api.v2.admin.GetParticipantIdResponse\x12o\n\nGetParties\x12/.com.daml.ledger.api.v2.admin.GetPartiesRequest\x1a\x30.com.daml.ledger.api.v2.admin.GetPartiesResponse\x12\x81\x01\n\x10ListKnownParties\x12\x35.com.daml.ledger.api.v2.admin.ListKnownPartiesRequest\x1a\x36.com.daml.ledger.api.v2.admin.ListKnownPartiesResponse\x12x\n\rAllocateParty\x12\x32.com.daml.ledger.api.v2.admin.AllocatePartyRequest\x1a\x33.com.daml.ledger.api.v2.admin.AllocatePartyResponse\x12\x87\x01\n\x12UpdatePartyDetails\x12\x37.com.daml.ledger.api.v2.admin.UpdatePartyDetailsRequest\x1a\x38.com.daml.ledger.api.v2.admin.UpdatePartyDetailsResponse\x12\xa8\x01\n\x1dUpdatePartyIdentityProviderId\x12\x42.com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdRequest\x1a\x43.com.daml.ledger.api.v2.admin.UpdatePartyIdentityProviderIdResponseB\xac\x01\n\x1c\x63om.daml.ledger.api.v2.adminB PartyManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/admin\xaa\x02\x1c\x43om.Daml.Ledger.Api.V2.Adminb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v2.admin.party_management_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.daml.ledger.api.v2.adminB PartyManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v2/admin\252\002\034Com.Daml.Ledger.Api.V2.Admin'
  _globals['_GETPARTICIPANTIDREQUEST']._serialized_start=175
  _globals['_GETPARTICIPANTIDREQUEST']._serialized_end=200
  _globals['_GETPARTICIPANTIDRESPONSE']._serialized_start=202
  _globals['_GETPARTICIPANTIDRESPONSE']._serialized_end=267
  _globals['_GETPARTIESREQUEST']._serialized_start=269
  _globals['_GETPARTIESREQUEST']._serialized_end=364
  _globals['_GETPARTIESRESPONSE']._serialized_start=366
  _globals['_GETPARTIESRESPONSE']._serialized_end=467
  _globals['_LISTKNOWNPARTIESREQUEST']._serialized_start=470
  _globals['_LISTKNOWNPARTIESREQUEST']._serialized_end=605
  _globals['_LISTKNOWNPARTIESRESPONSE']._serialized_start=608
  _globals['_LISTKNOWNPARTIESRESPONSE']._serialized_end=755
  _globals['_ALLOCATEPARTYREQUEST']._serialized_start=758
  _globals['_ALLOCATEPARTYREQUEST']._serialized_end=982
  _globals['_ALLOCATEPARTYRESPONSE']._serialized_start=984
  _globals['_ALLOCATEPARTYRESPONSE']._serialized_end=1088
  _globals['_UPDATEPARTYDETAILSREQUEST']._serialized_start=1091
  _globals['_UPDATEPARTYDETAILSREQUEST']._serialized_end=1260
  _globals['_UPDATEPARTYDETAILSRESPONSE']._serialized_start=1262
  _globals['_UPDATEPARTYDETAILSRESPONSE']._serialized_end=1371
  _globals['_PARTYDETAILS']._serialized_start=1374
  _globals['_PARTYDETAILS']._serialized_end=1603
  _globals['_UPDATEPARTYIDENTITYPROVIDERIDREQUEST']._serialized_start=1606
  _globals['_UPDATEPARTYIDENTITYPROVIDERIDREQUEST']._serialized_end=1792
  _globals['_UPDATEPARTYIDENTITYPROVIDERIDRESPONSE']._serialized_start=1794
  _globals['_UPDATEPARTYIDENTITYPROVIDERIDRESPONSE']._serialized_end=1833
  _globals['_PARTYMANAGEMENTSERVICE']._serialized_start=1836
  _globals['_PARTYMANAGEMENTSERVICE']._serialized_end=2668
# @@protoc_insertion_point(module_scope)
