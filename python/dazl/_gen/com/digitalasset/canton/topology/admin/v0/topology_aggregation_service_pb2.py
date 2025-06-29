# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/topology/admin/v0/topology_aggregation_service.proto
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
    'com/digitalasset/canton/topology/admin/v0/topology_aggregation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from ....protocol.v0 import topology_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_topology__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLcom/digitalasset/canton/topology/admin/v0/topology_aggregation_service.proto\x12)com.digitalasset.canton.topology.admin.v0\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x32\x63om/digitalasset/canton/protocol/v0/topology.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd2\x01\n\x12ListPartiesRequest\x12/\n\x05\x61s_of\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04\x61sOf\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12#\n\rfilter_domain\x18\x03 \x01(\tR\x0c\x66ilterDomain\x12!\n\x0c\x66ilter_party\x18\x04 \x01(\tR\x0b\x66ilterParty\x12-\n\x12\x66ilter_participant\x18\x05 \x01(\tR\x11\x66ilterParticipant\"\xdf\x04\n\x13ListPartiesResponse\x12_\n\x07results\x18\x02 \x03(\x0b\x32\x45.com.digitalasset.canton.topology.admin.v0.ListPartiesResponse.ResultR\x07results\x1a\xe6\x03\n\x06Result\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12|\n\x0cparticipants\x18\x02 \x03(\x0b\x32X.com.digitalasset.canton.topology.admin.v0.ListPartiesResponse.Result.ParticipantDomainsR\x0cparticipants\x1a\xc7\x02\n\x12ParticipantDomains\x12 \n\x0bparticipant\x18\x01 \x01(\tR\x0bparticipant\x12\x84\x01\n\x07\x64omains\x18\x02 \x03(\x0b\x32j.com.digitalasset.canton.topology.admin.v0.ListPartiesResponse.Result.ParticipantDomains.DomainPermissionsR\x07\x64omains\x1a\x87\x01\n\x11\x44omainPermissions\x12\x16\n\x06\x64omain\x18\x01 \x01(\tR\x06\x64omain\x12Z\n\npermission\x18\x02 \x01(\x0e\x32:.com.digitalasset.canton.protocol.v0.ParticipantPermissionR\npermission\"\xe6\x01\n\x14ListKeyOwnersRequest\x12/\n\x05\x61s_of\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04\x61sOf\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12#\n\rfilter_domain\x18\x03 \x01(\tR\x0c\x66ilterDomain\x12\x31\n\x15\x66ilter_key_owner_type\x18\x04 \x01(\tR\x12\x66ilterKeyOwnerType\x12/\n\x14\x66ilter_key_owner_uid\x18\x05 \x01(\tR\x11\x66ilterKeyOwnerUid\"\xf3\x02\n\x15ListKeyOwnersResponse\x12\x61\n\x07results\x18\x01 \x03(\x0b\x32G.com.digitalasset.canton.topology.admin.v0.ListKeyOwnersResponse.ResultR\x07results\x1a\xf6\x01\n\x06Result\x12\x16\n\x06\x64omain\x18\x01 \x01(\tR\x06\x64omain\x12\x1b\n\tkey_owner\x18\x02 \x01(\tR\x08keyOwner\x12V\n\x0csigning_keys\x18\x03 \x03(\x0b\x32\x33.com.digitalasset.canton.crypto.v0.SigningPublicKeyR\x0bsigningKeys\x12_\n\x0f\x65ncryption_keys\x18\x04 \x03(\x0b\x32\x36.com.digitalasset.canton.crypto.v0.EncryptionPublicKeyR\x0e\x65ncryptionKeys2\xc0\x02\n\x1aTopologyAggregationService\x12\x8c\x01\n\x0bListParties\x12=.com.digitalasset.canton.topology.admin.v0.ListPartiesRequest\x1a>.com.digitalasset.canton.topology.admin.v0.ListPartiesResponse\x12\x92\x01\n\rListKeyOwners\x12?.com.digitalasset.canton.topology.admin.v0.ListKeyOwnersRequest\x1a@.com.digitalasset.canton.topology.admin.v0.ListKeyOwnersResponseBZZXgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/topology/admin/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.topology.admin.v0.topology_aggregation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZXgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/topology/admin/v0'
  _globals['_LISTPARTIESREQUEST']._serialized_start=257
  _globals['_LISTPARTIESREQUEST']._serialized_end=467
  _globals['_LISTPARTIESRESPONSE']._serialized_start=470
  _globals['_LISTPARTIESRESPONSE']._serialized_end=1077
  _globals['_LISTPARTIESRESPONSE_RESULT']._serialized_start=591
  _globals['_LISTPARTIESRESPONSE_RESULT']._serialized_end=1077
  _globals['_LISTPARTIESRESPONSE_RESULT_PARTICIPANTDOMAINS']._serialized_start=750
  _globals['_LISTPARTIESRESPONSE_RESULT_PARTICIPANTDOMAINS']._serialized_end=1077
  _globals['_LISTPARTIESRESPONSE_RESULT_PARTICIPANTDOMAINS_DOMAINPERMISSIONS']._serialized_start=942
  _globals['_LISTPARTIESRESPONSE_RESULT_PARTICIPANTDOMAINS_DOMAINPERMISSIONS']._serialized_end=1077
  _globals['_LISTKEYOWNERSREQUEST']._serialized_start=1080
  _globals['_LISTKEYOWNERSREQUEST']._serialized_end=1310
  _globals['_LISTKEYOWNERSRESPONSE']._serialized_start=1313
  _globals['_LISTKEYOWNERSRESPONSE']._serialized_end=1684
  _globals['_LISTKEYOWNERSRESPONSE_RESULT']._serialized_start=1438
  _globals['_LISTKEYOWNERSRESPONSE_RESULT']._serialized_end=1684
  _globals['_TOPOLOGYAGGREGATIONSERVICE']._serialized_start=1687
  _globals['_TOPOLOGYAGGREGATIONSERVICE']._serialized_end=2007
# @@protoc_insertion_point(module_scope)
