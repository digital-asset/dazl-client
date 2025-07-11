# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v0/participant_transfer.proto
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
    'com/digitalasset/canton/protocol/v0/participant_transfer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from . import common_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_common__pb2
from . import merkle_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_merkle__pb2
from . import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2
from ...time.v0 import time_proof_pb2 as com_dot_digitalasset_dot_canton_dot_time_dot_v0_dot_time__proof__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>com/digitalasset/canton/protocol/v0/participant_transfer.proto\x12#com.digitalasset.canton.protocol.v0\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x30\x63om/digitalasset/canton/protocol/v0/common.proto\x1a\x30\x63om/digitalasset/canton/protocol/v0/merkle.proto\x1a\x34\x63om/digitalasset/canton/protocol/v0/sequencing.proto\x1a\x30\x63om/digitalasset/canton/time/v0/time_proof.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"k\n\nTransferId\x12#\n\rorigin_domain\x18\x01 \x01(\tR\x0coriginDomain\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"g\n\x1aTransferOutMediatorMessage\x12I\n\x04tree\x18\x01 \x01(\x0b\x32\x35.com.digitalasset.canton.protocol.v0.TransferViewTreeR\x04tree\"f\n\x19TransferInMediatorMessage\x12I\n\x04tree\x18\x01 \x01(\x0b\x32\x35.com.digitalasset.canton.protocol.v0.TransferViewTreeR\x04tree\"\xc6\x01\n\x10TransferViewTree\x12S\n\x0b\x63ommon_data\x18\x01 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v0.BlindableNodeR\ncommonData\x12]\n\x10participant_data\x18\x02 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v0.BlindableNodeR\x0fparticipantData\"\xff\x01\n\x15TransferOutCommonData\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12#\n\rorigin_domain\x18\x02 \x01(\tR\x0coriginDomain\x12\"\n\x0cstakeholders\x18\x03 \x03(\tR\x0cstakeholders\x12#\n\radmin_parties\x18\x04 \x03(\tR\x0c\x61\x64minParties\x12\x12\n\x04uuid\x18\x05 \x01(\tR\x04uuid\x12\'\n\x0forigin_mediator\x18\x06 \x01(\tR\x0eoriginMediator\"\x8a\x02\n\x0fTransferOutView\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12\x1c\n\tsubmitter\x18\x02 \x01(\tR\tsubmitter\x12\x1f\n\x0b\x63ontract_id\x18\x03 \x01(\tR\ncontractId\x12#\n\rtarget_domain\x18\x04 \x01(\tR\x0ctargetDomain\x12V\n\x11target_time_proof\x18\x05 \x01(\x0b\x32*.com.digitalasset.canton.time.v0.TimeProofR\x0ftargetTimeProof\"\xd9\x01\n\x14TransferInCommonData\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12#\n\rtarget_domain\x18\x02 \x01(\tR\x0ctargetDomain\x12\"\n\x0cstakeholders\x18\x03 \x03(\tR\x0cstakeholders\x12\x12\n\x04uuid\x18\x04 \x01(\tR\x04uuid\x12\'\n\x0ftarget_mediator\x18\x06 \x01(\tR\x0etargetMediator\"\xe9\x02\n\x0eTransferInView\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12\x1c\n\tsubmitter\x18\x02 \x01(\tR\tsubmitter\x12U\n\x08\x63ontract\x18\x03 \x01(\x0b\x32\x39.com.digitalasset.canton.protocol.v0.SerializableContractR\x08\x63ontract\x12m\n\x19transfer_out_result_event\x18\x04 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v0.SignedContentR\x16transferOutResultEvent\x12\x36\n\x17\x63reating_transaction_id\x18\x05 \x01(\x0cR\x15\x63reatingTransactionIdBTZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v0.participant_transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/protocol/v0'
  _globals['_TRANSFERID']._serialized_start=388
  _globals['_TRANSFERID']._serialized_end=495
  _globals['_TRANSFEROUTMEDIATORMESSAGE']._serialized_start=497
  _globals['_TRANSFEROUTMEDIATORMESSAGE']._serialized_end=600
  _globals['_TRANSFERINMEDIATORMESSAGE']._serialized_start=602
  _globals['_TRANSFERINMEDIATORMESSAGE']._serialized_end=704
  _globals['_TRANSFERVIEWTREE']._serialized_start=707
  _globals['_TRANSFERVIEWTREE']._serialized_end=905
  _globals['_TRANSFEROUTCOMMONDATA']._serialized_start=908
  _globals['_TRANSFEROUTCOMMONDATA']._serialized_end=1163
  _globals['_TRANSFEROUTVIEW']._serialized_start=1166
  _globals['_TRANSFEROUTVIEW']._serialized_end=1432
  _globals['_TRANSFERINCOMMONDATA']._serialized_start=1435
  _globals['_TRANSFERINCOMMONDATA']._serialized_end=1652
  _globals['_TRANSFERINVIEW']._serialized_start=1655
  _globals['_TRANSFERINVIEW']._serialized_end=2016
# @@protoc_insertion_point(module_scope)
