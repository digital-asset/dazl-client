# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/daml_lf_2_1/daml_lf.proto
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
    'com/daml/daml_lf_2_1/daml_lf.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import daml_lf2_pb2 as com_dot_daml_dot_daml__lf__2__1_dot_daml__lf2__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"com/daml/daml_lf_2_1/daml_lf.proto\x12\x0b\x64\x61ml_lf_2_1\x1a#com/daml/daml_lf_2_1/daml_lf2.proto\"o\n\x0e\x41rchivePayload\x12\x14\n\x05minor\x18\x03 \x01(\tR\x05minor\x12\x32\n\tdaml_lf_2\x18\x04 \x01(\x0b\x32\x14.daml_lf_2_1.PackageH\x00R\x07\x64\x61mlLf2B\x05\n\x03SumJ\x06\x08\x8fN\x10\x90NJ\x04\x08\x01\x10\x02\"w\n\x07\x41rchive\x12>\n\rhash_function\x18\x01 \x01(\x0e\x32\x19.daml_lf_2_1.HashFunctionR\x0chashFunction\x12\x18\n\x07payload\x18\x03 \x01(\x0cR\x07payload\x12\x12\n\x04hash\x18\x04 \x01(\tR\x04hash*\x1a\n\x0cHashFunction\x12\n\n\x06SHA256\x10\x00\x42y\n\x14\x63om.daml.daml_lf_2_1ZCgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_2_1\xaa\x02\x1b\x43om.Daml.Daml_Lf_2_1.DamlLfb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.daml_lf_2_1.daml_lf_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.daml.daml_lf_2_1ZCgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/daml_lf_2_1\252\002\033Com.Daml.Daml_Lf_2_1.DamlLf'
  _globals['_HASHFUNCTION']._serialized_start=322
  _globals['_HASHFUNCTION']._serialized_end=348
  _globals['_ARCHIVEPAYLOAD']._serialized_start=88
  _globals['_ARCHIVEPAYLOAD']._serialized_end=199
  _globals['_ARCHIVE']._serialized_start=201
  _globals['_ARCHIVE']._serialized_end=320
# @@protoc_insertion_point(module_scope)
