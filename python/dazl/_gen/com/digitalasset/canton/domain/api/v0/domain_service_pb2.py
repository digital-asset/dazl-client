# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/domain/api/v0/domain_service.proto
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
    'com/digitalasset/canton/domain/api/v0/domain_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import service_agreement_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:com/digitalasset/canton/domain/api/v0/domain_service.proto\x12%com.digitalasset.canton.domain.api.v0\x1a=com/digitalasset/canton/domain/api/v0/service_agreement.proto2\xb3\x01\n\rDomainService\x12\x9c\x01\n\x13GetServiceAgreement\x12\x41.com.digitalasset.canton.domain.api.v0.GetServiceAgreementRequest\x1a\x42.com.digitalasset.canton.domain.api.v0.GetServiceAgreementResponse\x1a\x03\x88\x02\x01\x42VZTgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/api/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.api.v0.domain_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZTgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/api/v0'
  _globals['_DOMAINSERVICE']._loaded_options = None
  _globals['_DOMAINSERVICE']._serialized_options = b'\210\002\001'
  _globals['_DOMAINSERVICE']._serialized_start=165
  _globals['_DOMAINSERVICE']._serialized_end=344
# @@protoc_insertion_point(module_scope)
