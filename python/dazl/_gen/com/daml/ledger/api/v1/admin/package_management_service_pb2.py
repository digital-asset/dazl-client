# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/admin/package_management_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=com/daml/ledger/api/v1/admin/package_management_service.proto\x12\x1c\x63om.daml.ledger.api.v1.admin\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1a\n\x18ListKnownPackagesRequest\"r\n\x19ListKnownPackagesResponse\x12U\n\x0fpackage_details\x18\x01 \x03(\x0b\x32,.com.daml.ledger.api.v1.admin.PackageDetailsR\x0epackageDetails\"\xbe\x01\n\x0ePackageDetails\x12\x1d\n\npackage_id\x18\x01 \x01(\tR\tpackageId\x12!\n\x0cpackage_size\x18\x02 \x01(\x04R\x0bpackageSize\x12;\n\x0bknown_since\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nknownSince\x12-\n\x12source_description\x18\x04 \x01(\tR\x11sourceDescription\"V\n\x14UploadDarFileRequest\x12\x19\n\x08\x64\x61r_file\x18\x01 \x01(\x0cR\x07\x64\x61rFile\x12#\n\rsubmission_id\x18\x02 \x01(\tR\x0csubmissionId\"\x17\n\x15UploadDarFileResponse2\x9b\x02\n\x18PackageManagementService\x12\x84\x01\n\x11ListKnownPackages\x12\x36.com.daml.ledger.api.v1.admin.ListKnownPackagesRequest\x1a\x37.com.daml.ledger.api.v1.admin.ListKnownPackagesResponse\x12x\n\rUploadDarFile\x12\x32.com.daml.ledger.api.v1.admin.UploadDarFileRequest\x1a\x33.com.daml.ledger.api.v1.admin.UploadDarFileResponseB\xae\x01\n\x1c\x63om.daml.ledger.api.v1.adminB\"PackageManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\xaa\x02\x1c\x43om.Daml.Ledger.Api.V1.Adminb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.admin.package_management_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.daml.ledger.api.v1.adminB\"PackageManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\252\002\034Com.Daml.Ledger.Api.V1.Admin'
  _LISTKNOWNPACKAGESREQUEST._serialized_start=128
  _LISTKNOWNPACKAGESREQUEST._serialized_end=154
  _LISTKNOWNPACKAGESRESPONSE._serialized_start=156
  _LISTKNOWNPACKAGESRESPONSE._serialized_end=270
  _PACKAGEDETAILS._serialized_start=273
  _PACKAGEDETAILS._serialized_end=463
  _UPLOADDARFILEREQUEST._serialized_start=465
  _UPLOADDARFILEREQUEST._serialized_end=551
  _UPLOADDARFILERESPONSE._serialized_start=553
  _UPLOADDARFILERESPONSE._serialized_end=576
  _PACKAGEMANAGEMENTSERVICE._serialized_start=579
  _PACKAGEMANAGEMENTSERVICE._serialized_end=862
# @@protoc_insertion_point(module_scope)
