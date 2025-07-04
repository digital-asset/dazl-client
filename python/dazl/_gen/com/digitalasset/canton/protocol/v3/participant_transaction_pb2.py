# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v3/participant_transaction.proto
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
    'com/digitalasset/canton/protocol/v3/participant_transaction.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from ..v0 import participant_transaction_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_participant__transaction__pb2
from ..v1 import participant_transaction_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_participant__transaction__pb2
from ..v2 import participant_transaction_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v2_dot_participant__transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAcom/digitalasset/canton/protocol/v3/participant_transaction.proto\x12#com.digitalasset.canton.protocol.v3\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x41\x63om/digitalasset/canton/protocol/v0/participant_transaction.proto\x1a\x41\x63om/digitalasset/canton/protocol/v1/participant_transaction.proto\x1a\x41\x63om/digitalasset/canton/protocol/v2/participant_transaction.proto\"\x94\x05\n\x13ViewParticipantData\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12S\n\x0b\x63ore_inputs\x18\x02 \x03(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.InputContractR\ncoreInputs\x12W\n\x0c\x63reated_core\x18\x03 \x03(\x0b\x32\x34.com.digitalasset.canton.protocol.v1.CreatedContractR\x0b\x63reatedCore\x12K\n#created_in_subview_archived_in_core\x18\x04 \x03(\tR\x1e\x63reatedInSubviewArchivedInCore\x12i\n\rresolved_keys\x18\x05 \x03(\x0b\x32\x44.com.digitalasset.canton.protocol.v0.ViewParticipantData.ResolvedKeyR\x0cresolvedKeys\x12\x65\n\x12\x61\x63tion_description\x18\x06 \x01(\x0b\x32\x36.com.digitalasset.canton.protocol.v2.ActionDescriptionR\x11\x61\x63tionDescription\x12s\n\x10rollback_context\x18\x07 \x01(\x0b\x32H.com.digitalasset.canton.protocol.v0.ViewParticipantData.RollbackContextR\x0frollbackContext\"\xff\x06\n\x11\x41\x63tionDescription\x12h\n\x06\x63reate\x18\x01 \x01(\x0b\x32N.com.digitalasset.canton.protocol.v0.ActionDescription.CreateActionDescriptionH\x00R\x06\x63reate\x12n\n\x08\x65xercise\x18\x02 \x01(\x0b\x32P.com.digitalasset.canton.protocol.v3.ActionDescription.ExerciseActionDescriptionH\x00R\x08\x65xercise\x12\x65\n\x05\x66\x65tch\x18\x03 \x01(\x0b\x32M.com.digitalasset.canton.protocol.v1.ActionDescription.FetchActionDescriptionH\x00R\x05\x66\x65tch\x12y\n\rlookup_by_key\x18\x04 \x01(\x0b\x32S.com.digitalasset.canton.protocol.v1.ActionDescription.LookupByKeyActionDescriptionH\x00R\x0blookupByKey\x1a\x9e\x03\n\x19\x45xerciseActionDescription\x12*\n\x11input_contract_id\x18\x01 \x01(\tR\x0finputContractId\x12\x16\n\x06\x63hoice\x18\x02 \x01(\tR\x06\x63hoice\x12!\n\x0c\x63hosen_value\x18\x03 \x01(\x0cR\x0b\x63hosenValue\x12\x16\n\x06\x61\x63tors\x18\x04 \x03(\tR\x06\x61\x63tors\x12\x15\n\x06\x62y_key\x18\x05 \x01(\x08R\x05\x62yKey\x12\x1b\n\tnode_seed\x18\x06 \x01(\x0cR\x08nodeSeed\x12\x18\n\x07version\x18\x07 \x01(\tR\x07version\x12\x16\n\x06\x66\x61iled\x18\x08 \x01(\x08R\x06\x66\x61iled\x12&\n\x0cinterface_id\x18\t \x01(\tH\x00R\x0binterfaceId\x88\x01\x01\x12$\n\x0btemplate_id\x18\n \x01(\tH\x01R\ntemplateId\x88\x01\x01\x12-\n\x12package_preference\x18\x0b \x03(\tR\x11packagePreferenceB\x0f\n\r_interface_idB\x0e\n\x0c_template_idB\r\n\x0b\x64\x65scriptionBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v3.participant_transaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v3'
  _globals['_VIEWPARTICIPANTDATA']._serialized_start=356
  _globals['_VIEWPARTICIPANTDATA']._serialized_end=1016
  _globals['_ACTIONDESCRIPTION']._serialized_start=1019
  _globals['_ACTIONDESCRIPTION']._serialized_end=1914
  _globals['_ACTIONDESCRIPTION_EXERCISEACTIONDESCRIPTION']._serialized_start=1485
  _globals['_ACTIONDESCRIPTION_EXERCISEACTIONDESCRIPTION']._serialized_end=1899
# @@protoc_insertion_point(module_scope)
