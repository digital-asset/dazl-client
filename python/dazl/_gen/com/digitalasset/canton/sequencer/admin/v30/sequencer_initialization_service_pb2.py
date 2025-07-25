# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/sequencer/admin/v30/sequencer_initialization_service.proto
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
    'com/digitalasset/canton/sequencer/admin/v30/sequencer_initialization_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....protocol.v30 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v30_dot_sequencing__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRcom/digitalasset/canton/sequencer/admin/v30/sequencer_initialization_service.proto\x12+com.digitalasset.canton.sequencer.admin.v30\x1a\x35\x63om/digitalasset/canton/protocol/v30/sequencing.proto\"\xd6\x01\n*InitializeSequencerFromGenesisStateRequest\x12+\n\x11topology_snapshot\x18\x01 \x01(\x0cR\x10topologySnapshot\x12{\n\x17synchronizer_parameters\x18\x02 \x01(\x0b\x32\x42.com.digitalasset.canton.protocol.v30.StaticSynchronizerParametersR\x16synchronizerParameters\"M\n+InitializeSequencerFromGenesisStateResponse\x12\x1e\n\nreplicated\x18\x01 \x01(\x08R\nreplicated\"Z\n-InitializeSequencerFromOnboardingStateRequest\x12)\n\x10onboarding_state\x18\x01 \x01(\x0cR\x0fonboardingState\"P\n.InitializeSequencerFromOnboardingStateResponse\x12\x1e\n\nreplicated\x18\x01 \x01(\x08R\nreplicated2\xe3\x03\n\x1eSequencerInitializationService\x12\xda\x01\n#InitializeSequencerFromGenesisState\x12W.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateRequest\x1aX.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromGenesisStateResponse(\x01\x12\xe3\x01\n&InitializeSequencerFromOnboardingState\x12Z.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateRequest\x1a[.com.digitalasset.canton.sequencer.admin.v30.InitializeSequencerFromOnboardingStateResponse(\x01\x42\\ZZgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/admin/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.sequencer.admin.v30.sequencer_initialization_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZZgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/sequencer/admin/v30'
  _globals['_INITIALIZESEQUENCERFROMGENESISSTATEREQUEST']._serialized_start=187
  _globals['_INITIALIZESEQUENCERFROMGENESISSTATEREQUEST']._serialized_end=401
  _globals['_INITIALIZESEQUENCERFROMGENESISSTATERESPONSE']._serialized_start=403
  _globals['_INITIALIZESEQUENCERFROMGENESISSTATERESPONSE']._serialized_end=480
  _globals['_INITIALIZESEQUENCERFROMONBOARDINGSTATEREQUEST']._serialized_start=482
  _globals['_INITIALIZESEQUENCERFROMONBOARDINGSTATEREQUEST']._serialized_end=572
  _globals['_INITIALIZESEQUENCERFROMONBOARDINGSTATERESPONSE']._serialized_start=574
  _globals['_INITIALIZESEQUENCERFROMONBOARDINGSTATERESPONSE']._serialized_end=654
  _globals['_SEQUENCERINITIALIZATIONSERVICE']._serialized_start=657
  _globals['_SEQUENCERINITIALIZATIONSERVICE']._serialized_end=1140
# @@protoc_insertion_point(module_scope)
