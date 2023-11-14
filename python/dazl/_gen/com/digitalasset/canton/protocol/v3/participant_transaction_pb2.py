# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/protocol/v3/participant_transaction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from ..v0 import participant_transaction_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_participant__transaction__pb2
from ..v1 import participant_transaction_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_participant__transaction__pb2
from ..v2 import participant_transaction_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v2_dot_participant__transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAcom/digitalasset/canton/protocol/v3/participant_transaction.proto\x12#com.digitalasset.canton.protocol.v3\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x41\x63om/digitalasset/canton/protocol/v0/participant_transaction.proto\x1a\x41\x63om/digitalasset/canton/protocol/v1/participant_transaction.proto\x1a\x41\x63om/digitalasset/canton/protocol/v2/participant_transaction.proto\"\x94\x05\n\x13ViewParticipantData\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12S\n\x0b\x63ore_inputs\x18\x02 \x03(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.InputContractR\ncoreInputs\x12W\n\x0c\x63reated_core\x18\x03 \x03(\x0b\x32\x34.com.digitalasset.canton.protocol.v1.CreatedContractR\x0b\x63reatedCore\x12K\n#created_in_subview_archived_in_core\x18\x04 \x03(\tR\x1e\x63reatedInSubviewArchivedInCore\x12i\n\rresolved_keys\x18\x05 \x03(\x0b\x32\x44.com.digitalasset.canton.protocol.v0.ViewParticipantData.ResolvedKeyR\x0cresolvedKeys\x12\x65\n\x12\x61\x63tion_description\x18\x06 \x01(\x0b\x32\x36.com.digitalasset.canton.protocol.v2.ActionDescriptionR\x11\x61\x63tionDescription\x12s\n\x10rollback_context\x18\x07 \x01(\x0b\x32H.com.digitalasset.canton.protocol.v0.ViewParticipantData.RollbackContextR\x0frollbackContextb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v3.participant_transaction_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VIEWPARTICIPANTDATA']._serialized_start=356
  _globals['_VIEWPARTICIPANTDATA']._serialized_end=1016
# @@protoc_insertion_point(module_scope)
