# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v1/package_service.proto
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
    'com/daml/ledger/api/v1/package_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,com/daml/ledger/api/v1/package_service.proto\x12\x16\x63om.daml.ledger.api.v1\"2\n\x13ListPackagesRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\"7\n\x14ListPackagesResponse\x12\x1f\n\x0bpackage_ids\x18\x01 \x03(\tR\npackageIds\"O\n\x11GetPackageRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\x12\x1d\n\npackage_id\x18\x02 \x01(\tR\tpackageId\"\x9c\x01\n\x12GetPackageResponse\x12I\n\rhash_function\x18\x01 \x01(\x0e\x32$.com.daml.ledger.api.v1.HashFunctionR\x0chashFunction\x12\'\n\x0f\x61rchive_payload\x18\x02 \x01(\x0cR\x0e\x61rchivePayload\x12\x12\n\x04hash\x18\x03 \x01(\tR\x04hash\"U\n\x17GetPackageStatusRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\x12\x1d\n\npackage_id\x18\x02 \x01(\tR\tpackageId\"h\n\x18GetPackageStatusResponse\x12L\n\x0epackage_status\x18\x01 \x01(\x0e\x32%.com.daml.ledger.api.v1.PackageStatusR\rpackageStatus*,\n\rPackageStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nREGISTERED\x10\x01*\x1a\n\x0cHashFunction\x12\n\n\x06SHA256\x10\x00\x32\xd7\x02\n\x0ePackageService\x12i\n\x0cListPackages\x12+.com.daml.ledger.api.v1.ListPackagesRequest\x1a,.com.daml.ledger.api.v1.ListPackagesResponse\x12\x63\n\nGetPackage\x12).com.daml.ledger.api.v1.GetPackageRequest\x1a*.com.daml.ledger.api.v1.GetPackageResponse\x12u\n\x10GetPackageStatus\x12/.com.daml.ledger.api.v1.GetPackageStatusRequest\x1a\x30.com.daml.ledger.api.v1.GetPackageStatusResponseB\x92\x01\n\x16\x63om.daml.ledger.api.v1B\x18PackageServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.package_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v1B\030PackageServiceOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _globals['_PACKAGESTATUS']._serialized_start=614
  _globals['_PACKAGESTATUS']._serialized_end=658
  _globals['_HASHFUNCTION']._serialized_start=660
  _globals['_HASHFUNCTION']._serialized_end=686
  _globals['_LISTPACKAGESREQUEST']._serialized_start=72
  _globals['_LISTPACKAGESREQUEST']._serialized_end=122
  _globals['_LISTPACKAGESRESPONSE']._serialized_start=124
  _globals['_LISTPACKAGESRESPONSE']._serialized_end=179
  _globals['_GETPACKAGEREQUEST']._serialized_start=181
  _globals['_GETPACKAGEREQUEST']._serialized_end=260
  _globals['_GETPACKAGERESPONSE']._serialized_start=263
  _globals['_GETPACKAGERESPONSE']._serialized_end=419
  _globals['_GETPACKAGESTATUSREQUEST']._serialized_start=421
  _globals['_GETPACKAGESTATUSREQUEST']._serialized_end=506
  _globals['_GETPACKAGESTATUSRESPONSE']._serialized_start=508
  _globals['_GETPACKAGESTATUSRESPONSE']._serialized_end=612
  _globals['_PACKAGESERVICE']._serialized_start=689
  _globals['_PACKAGESERVICE']._serialized_end=1032
# @@protoc_insertion_point(module_scope)
