# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v1/participant_transfer.proto
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
    'com/digitalasset/canton/protocol/v1/participant_transfer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from ..v0 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2
from . import common_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_common__pb2
from . import merkle_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_merkle__pb2
from ...time.v0 import time_proof_pb2 as com_dot_digitalasset_dot_canton_dot_time_dot_v0_dot_time__proof__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>com/digitalasset/canton/protocol/v1/participant_transfer.proto\x12#com.digitalasset.canton.protocol.v1\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x34\x63om/digitalasset/canton/protocol/v0/sequencing.proto\x1a\x30\x63om/digitalasset/canton/protocol/v1/common.proto\x1a\x30\x63om/digitalasset/canton/protocol/v1/merkle.proto\x1a\x30\x63om/digitalasset/canton/time/v0/time_proof.proto\"\xb7\x02\n\x15TransferOutCommonData\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12#\n\rsource_domain\x18\x02 \x01(\tR\x0csourceDomain\x12\"\n\x0cstakeholders\x18\x03 \x03(\tR\x0cstakeholders\x12#\n\radmin_parties\x18\x04 \x03(\tR\x0c\x61\x64minParties\x12\x12\n\x04uuid\x18\x05 \x01(\tR\x04uuid\x12\'\n\x0fsource_mediator\x18\x06 \x01(\tR\x0esourceMediator\x12\x36\n\x17source_protocol_version\x18\x07 \x01(\x05R\x15sourceProtocolVersion\"\xc6\x01\n\x10TransferViewTree\x12S\n\x0b\x63ommon_data\x18\x01 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\ncommonData\x12]\n\x10participant_data\x18\x02 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v1.BlindableNodeR\x0fparticipantData\"f\n\x19TransferInMediatorMessage\x12I\n\x04tree\x18\x01 \x01(\x0b\x32\x35.com.digitalasset.canton.protocol.v1.TransferViewTreeR\x04tree\"g\n\x1aTransferOutMediatorMessage\x12I\n\x04tree\x18\x01 \x01(\x0b\x32\x35.com.digitalasset.canton.protocol.v1.TransferViewTreeR\x04tree\"\xc2\x02\n\x0fTransferOutView\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12\x1c\n\tsubmitter\x18\x02 \x01(\tR\tsubmitter\x12\x1f\n\x0b\x63ontract_id\x18\x03 \x01(\tR\ncontractId\x12#\n\rtarget_domain\x18\x04 \x01(\tR\x0ctargetDomain\x12V\n\x11target_time_proof\x18\x05 \x01(\x0b\x32*.com.digitalasset.canton.time.v0.TimeProofR\x0ftargetTimeProof\x12\x36\n\x17target_protocol_version\x18\x06 \x01(\x05R\x15targetProtocolVersion\"\x91\x02\n\x14TransferInCommonData\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12#\n\rtarget_domain\x18\x02 \x01(\tR\x0ctargetDomain\x12\"\n\x0cstakeholders\x18\x03 \x03(\tR\x0cstakeholders\x12\x12\n\x04uuid\x18\x04 \x01(\tR\x04uuid\x12\'\n\x0ftarget_mediator\x18\x06 \x01(\tR\x0etargetMediator\x12\x36\n\x17target_protocol_version\x18\x07 \x01(\x05R\x15targetProtocolVersion\"\xa1\x03\n\x0eTransferInView\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12\x1c\n\tsubmitter\x18\x02 \x01(\tR\tsubmitter\x12U\n\x08\x63ontract\x18\x03 \x01(\x0b\x32\x39.com.digitalasset.canton.protocol.v1.SerializableContractR\x08\x63ontract\x12m\n\x19transfer_out_result_event\x18\x04 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v0.SignedContentR\x16transferOutResultEvent\x12\x36\n\x17\x63reating_transaction_id\x18\x05 \x01(\x0cR\x15\x63reatingTransactionId\x12\x36\n\x17source_protocol_version\x18\x06 \x01(\x05R\x15sourceProtocolVersionBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v1.participant_transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v1'
  _globals['_TRANSFEROUTCOMMONDATA']._serialized_start=356
  _globals['_TRANSFEROUTCOMMONDATA']._serialized_end=667
  _globals['_TRANSFERVIEWTREE']._serialized_start=670
  _globals['_TRANSFERVIEWTREE']._serialized_end=868
  _globals['_TRANSFERINMEDIATORMESSAGE']._serialized_start=870
  _globals['_TRANSFERINMEDIATORMESSAGE']._serialized_end=972
  _globals['_TRANSFEROUTMEDIATORMESSAGE']._serialized_start=974
  _globals['_TRANSFEROUTMEDIATORMESSAGE']._serialized_end=1077
  _globals['_TRANSFEROUTVIEW']._serialized_start=1080
  _globals['_TRANSFEROUTVIEW']._serialized_end=1402
  _globals['_TRANSFERINCOMMONDATA']._serialized_start=1405
  _globals['_TRANSFERINCOMMONDATA']._serialized_end=1678
  _globals['_TRANSFERINVIEW']._serialized_start=1681
  _globals['_TRANSFERINVIEW']._serialized_end=2098
# @@protoc_insertion_point(module_scope)
