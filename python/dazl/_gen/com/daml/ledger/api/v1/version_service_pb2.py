# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v1/version_service.proto
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
    'com/daml/ledger/api/v1/version_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import experimental_features_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_experimental__features__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,com/daml/ledger/api/v1/version_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\x32\x63om/daml/ledger/api/v1/experimental_features.proto\"9\n\x1aGetLedgerApiVersionRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\"\x7f\n\x1bGetLedgerApiVersionResponse\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12\x46\n\x08\x66\x65\x61tures\x18\x02 \x01(\x0b\x32*.com.daml.ledger.api.v1.FeaturesDescriptorR\x08\x66\x65\x61tures\"\x99\x02\n\x12\x46\x65\x61turesDescriptor\x12V\n\x0fuser_management\x18\x02 \x01(\x0b\x32-.com.daml.ledger.api.v1.UserManagementFeatureR\x0euserManagement\x12Y\n\x10party_management\x18\x03 \x01(\x0b\x32..com.daml.ledger.api.v1.PartyManagementFeatureR\x0fpartyManagement\x12P\n\x0c\x65xperimental\x18\x01 \x01(\x0b\x32,.com.daml.ledger.api.v1.ExperimentalFeaturesR\x0c\x65xperimental\"\x93\x01\n\x15UserManagementFeature\x12\x1c\n\tsupported\x18\x01 \x01(\x08R\tsupported\x12-\n\x13max_rights_per_user\x18\x02 \x01(\x05R\x10maxRightsPerUser\x12-\n\x13max_users_page_size\x18\x03 \x01(\x05R\x10maxUsersPageSize\"K\n\x16PartyManagementFeature\x12\x31\n\x15max_parties_page_size\x18\x01 \x01(\x05R\x12maxPartiesPageSize2\x90\x01\n\x0eVersionService\x12~\n\x13GetLedgerApiVersion\x12\x32.com.daml.ledger.api.v1.GetLedgerApiVersionRequest\x1a\x33.com.daml.ledger.api.v1.GetLedgerApiVersionResponseB\x92\x01\n\x16\x63om.daml.ledger.api.v1B\x18VersionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.version_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v1B\030VersionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _globals['_GETLEDGERAPIVERSIONREQUEST']._serialized_start=124
  _globals['_GETLEDGERAPIVERSIONREQUEST']._serialized_end=181
  _globals['_GETLEDGERAPIVERSIONRESPONSE']._serialized_start=183
  _globals['_GETLEDGERAPIVERSIONRESPONSE']._serialized_end=310
  _globals['_FEATURESDESCRIPTOR']._serialized_start=313
  _globals['_FEATURESDESCRIPTOR']._serialized_end=594
  _globals['_USERMANAGEMENTFEATURE']._serialized_start=597
  _globals['_USERMANAGEMENTFEATURE']._serialized_end=744
  _globals['_PARTYMANAGEMENTFEATURE']._serialized_start=746
  _globals['_PARTYMANAGEMENTFEATURE']._serialized_end=821
  _globals['_VERSIONSERVICE']._serialized_start=824
  _globals['_VERSIONSERVICE']._serialized_end=968
# @@protoc_insertion_point(module_scope)
