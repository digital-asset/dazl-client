# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v2/topology.proto
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
    'com/digitalasset/canton/protocol/v2/topology.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..v1 import topology_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_topology__pb2
from . import domain_params_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v2_dot_domain__params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2com/digitalasset/canton/protocol/v2/topology.proto\x12#com.digitalasset.canton.protocol.v2\x1a\x32\x63om/digitalasset/canton/protocol/v1/topology.proto\x1a\x37\x63om/digitalasset/canton/protocol/v2/domain_params.proto\"\x9b\x01\n\x16\x44omainParametersChange\x12\x16\n\x06\x64omain\x18\x01 \x01(\tR\x06\x64omain\x12i\n\x11\x64omain_parameters\x18\x02 \x01(\x0b\x32<.com.digitalasset.canton.protocol.v2.DynamicDomainParametersR\x10\x64omainParameters\"\xa1\x01\n\x1b\x44omainGovernanceTransaction\x12w\n\x18\x64omain_parameters_change\x18\x01 \x01(\x0b\x32;.com.digitalasset.canton.protocol.v2.DomainParametersChangeH\x00R\x16\x64omainParametersChangeB\t\n\x07mapping\"\xf4\x01\n\x13TopologyTransaction\x12]\n\x0cstate_update\x18\x01 \x01(\x0b\x32\x38.com.digitalasset.canton.protocol.v1.TopologyStateUpdateH\x00R\x0bstateUpdate\x12o\n\x11\x64omain_governance\x18\x02 \x01(\x0b\x32@.com.digitalasset.canton.protocol.v2.DomainGovernanceTransactionH\x00R\x10\x64omainGovernanceB\r\n\x0btransactionBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v2.topology_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v2'
  _globals['_DOMAINPARAMETERSCHANGE']._serialized_start=201
  _globals['_DOMAINPARAMETERSCHANGE']._serialized_end=356
  _globals['_DOMAINGOVERNANCETRANSACTION']._serialized_start=359
  _globals['_DOMAINGOVERNANCETRANSACTION']._serialized_end=520
  _globals['_TOPOLOGYTRANSACTION']._serialized_start=523
  _globals['_TOPOLOGYTRANSACTION']._serialized_end=767
# @@protoc_insertion_point(module_scope)
