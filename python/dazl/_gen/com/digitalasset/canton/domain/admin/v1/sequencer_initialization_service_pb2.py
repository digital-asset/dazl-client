# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/domain/admin/v1/sequencer_initialization_service.proto
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
    'com/digitalasset/canton/domain/admin/v1/sequencer_initialization_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..v0 import sequencer_initialization_snapshot_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__snapshot__pb2
from ....protocol.v1 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_sequencing__pb2
from ....protocol.v0 import topology_ext_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_topology__ext__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNcom/digitalasset/canton/domain/admin/v1/sequencer_initialization_service.proto\x12\'com.digitalasset.canton.domain.admin.v1\x1aOcom/digitalasset/canton/domain/admin/v0/sequencer_initialization_snapshot.proto\x1a\x34\x63om/digitalasset/canton/protocol/v1/sequencing.proto\x1a\x36\x63om/digitalasset/canton/protocol/v0/topology_ext.proto\"\xd4\x02\n\x0bInitRequest\x12\x1b\n\tdomain_id\x18\x01 \x01(\tR\x08\x64omainId\x12\x66\n\x11topology_snapshot\x18\x02 \x01(\x0b\x32\x39.com.digitalasset.canton.protocol.v0.TopologyTransactionsR\x10topologySnapshot\x12h\n\x11\x64omain_parameters\x18\x04 \x01(\x0b\x32;.com.digitalasset.canton.protocol.v1.StaticDomainParametersR\x10\x64omainParameters\x12V\n\x08snapshot\x18\x03 \x01(\x0b\x32:.com.digitalasset.canton.domain.admin.v0.SequencerSnapshotR\x08snapshotBXZVgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/domain/admin/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.admin.v1.sequencer_initialization_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZVgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/domain/admin/v1'
  _globals['_INITREQUEST']._serialized_start=315
  _globals['_INITREQUEST']._serialized_end=655
# @@protoc_insertion_point(module_scope)
