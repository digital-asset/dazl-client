# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/daml/ledger/api/v1/value.proto
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
    'com/daml/ledger/api/v1/value.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"com/daml/ledger/api/v1/value.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\x1bgoogle/protobuf/empty.proto\"\xa0\x05\n\x05Value\x12\x38\n\x06record\x18\x01 \x01(\x0b\x32\x1e.com.daml.ledger.api.v1.RecordH\x00R\x06record\x12;\n\x07variant\x18\x02 \x01(\x0b\x32\x1f.com.daml.ledger.api.v1.VariantH\x00R\x07variant\x12!\n\x0b\x63ontract_id\x18\x03 \x01(\tH\x00R\ncontractId\x12\x32\n\x04list\x18\x04 \x01(\x0b\x32\x1c.com.daml.ledger.api.v1.ListH\x00R\x04list\x12\x1a\n\x05int64\x18\x05 \x01(\x12\x42\x02\x30\x01H\x00R\x05int64\x12\x1a\n\x07numeric\x18\x06 \x01(\tH\x00R\x07numeric\x12\x14\n\x04text\x18\x08 \x01(\tH\x00R\x04text\x12\"\n\ttimestamp\x18\t \x01(\x10\x42\x02\x30\x01H\x00R\ttimestamp\x12\x16\n\x05party\x18\x0b \x01(\tH\x00R\x05party\x12\x14\n\x04\x62ool\x18\x0c \x01(\x08H\x00R\x04\x62ool\x12,\n\x04unit\x18\r \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x04unit\x12\x14\n\x04\x64\x61te\x18\x0e \x01(\x05H\x00R\x04\x64\x61te\x12>\n\x08optional\x18\x0f \x01(\x0b\x32 .com.daml.ledger.api.v1.OptionalH\x00R\x08optional\x12/\n\x03map\x18\x10 \x01(\x0b\x32\x1b.com.daml.ledger.api.v1.MapH\x00R\x03map\x12\x32\n\x04\x65num\x18\x11 \x01(\x0b\x32\x1c.com.daml.ledger.api.v1.EnumH\x00R\x04\x65num\x12\x39\n\x07gen_map\x18\x12 \x01(\x0b\x32\x1e.com.daml.ledger.api.v1.GenMapH\x00R\x06genMapB\x05\n\x03Sum\"\x86\x01\n\x06Record\x12?\n\trecord_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\x08recordId\x12;\n\x06\x66ields\x18\x02 \x03(\x0b\x32#.com.daml.ledger.api.v1.RecordFieldR\x06\x66ields\"X\n\x0bRecordField\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x05value\"s\n\nIdentifier\x12\x1d\n\npackage_id\x18\x01 \x01(\tR\tpackageId\x12\x1f\n\x0bmodule_name\x18\x03 \x01(\tR\nmoduleName\x12\x1f\n\x0b\x65ntity_name\x18\x04 \x01(\tR\nentityNameJ\x04\x08\x02\x10\x03\"\xa3\x01\n\x07Variant\x12\x41\n\nvariant_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\tvariantId\x12 \n\x0b\x63onstructor\x18\x02 \x01(\tR\x0b\x63onstructor\x12\x33\n\x05value\x18\x03 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x05value\"e\n\x04\x45num\x12;\n\x07\x65num_id\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\x06\x65numId\x12 \n\x0b\x63onstructor\x18\x02 \x01(\tR\x0b\x63onstructor\"A\n\x04List\x12\x39\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x08\x65lements\"?\n\x08Optional\x12\x33\n\x05value\x18\x01 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x05value\"\x92\x01\n\x03Map\x12;\n\x07\x65ntries\x18\x01 \x03(\x0b\x32!.com.daml.ledger.api.v1.Map.EntryR\x07\x65ntries\x1aN\n\x05\x45ntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x05value\"\xb7\x01\n\x06GenMap\x12>\n\x07\x65ntries\x18\x01 \x03(\x0b\x32$.com.daml.ledger.api.v1.GenMap.EntryR\x07\x65ntries\x1am\n\x05\x45ntry\x12/\n\x03key\x18\x01 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x05valueB\x89\x01\n\x16\x63om.daml.ledger.api.v1B\x0fValueOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.daml.ledger.api.v1.value_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.daml.ledger.api.v1B\017ValueOuterClassZEgithub.com/digital-asset/dazl-client/v8/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1'
  _globals['_VALUE'].fields_by_name['int64']._loaded_options = None
  _globals['_VALUE'].fields_by_name['int64']._serialized_options = b'0\001'
  _globals['_VALUE'].fields_by_name['timestamp']._loaded_options = None
  _globals['_VALUE'].fields_by_name['timestamp']._serialized_options = b'0\001'
  _globals['_VALUE']._serialized_start=92
  _globals['_VALUE']._serialized_end=764
  _globals['_RECORD']._serialized_start=767
  _globals['_RECORD']._serialized_end=901
  _globals['_RECORDFIELD']._serialized_start=903
  _globals['_RECORDFIELD']._serialized_end=991
  _globals['_IDENTIFIER']._serialized_start=993
  _globals['_IDENTIFIER']._serialized_end=1108
  _globals['_VARIANT']._serialized_start=1111
  _globals['_VARIANT']._serialized_end=1274
  _globals['_ENUM']._serialized_start=1276
  _globals['_ENUM']._serialized_end=1377
  _globals['_LIST']._serialized_start=1379
  _globals['_LIST']._serialized_end=1444
  _globals['_OPTIONAL']._serialized_start=1446
  _globals['_OPTIONAL']._serialized_end=1509
  _globals['_MAP']._serialized_start=1512
  _globals['_MAP']._serialized_end=1658
  _globals['_MAP_ENTRY']._serialized_start=1580
  _globals['_MAP_ENTRY']._serialized_end=1658
  _globals['_GENMAP']._serialized_start=1661
  _globals['_GENMAP']._serialized_end=1844
  _globals['_GENMAP_ENTRY']._serialized_start=1735
  _globals['_GENMAP_ENTRY']._serialized_end=1844
# @@protoc_insertion_point(module_scope)
