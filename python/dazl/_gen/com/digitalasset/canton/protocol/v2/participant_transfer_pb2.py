# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/protocol/v2/participant_transfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from ..v0 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2
from ..v1 import common_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v1_dot_common__pb2
from ...time.v0 import time_proof_pb2 as com_dot_digitalasset_dot_canton_dot_time_dot_v0_dot_time__proof__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>com/digitalasset/canton/protocol/v2/participant_transfer.proto\x12#com.digitalasset.canton.protocol.v2\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x34\x63om/digitalasset/canton/protocol/v0/sequencing.proto\x1a\x30\x63om/digitalasset/canton/protocol/v1/common.proto\x1a\x30\x63om/digitalasset/canton/time/v0/time_proof.proto\"\xd1\x04\n\x0fTransferOutView\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12\x1c\n\tsubmitter\x18\x02 \x01(\tR\tsubmitter\x12\x1f\n\x0b\x63ontract_id\x18\x03 \x01(\tR\ncontractId\x12\x1f\n\x0btemplate_id\x18\x04 \x01(\tR\ntemplateId\x12#\n\rtarget_domain\x18\x05 \x01(\tR\x0ctargetDomain\x12V\n\x11target_time_proof\x18\x06 \x01(\x0b\x32*.com.digitalasset.canton.time.v0.TimeProofR\x0ftargetTimeProof\x12\x36\n\x17target_protocol_version\x18\x07 \x01(\x05R\x15targetProtocolVersion\x12\x35\n\x16submitting_participant\x18\x08 \x01(\tR\x15submittingParticipant\x12%\n\x0e\x61pplication_id\x18\t \x01(\tR\rapplicationId\x12#\n\rsubmission_id\x18\n \x01(\tR\x0csubmissionId\x12\x1f\n\x0bworkflow_id\x18\x0b \x01(\tR\nworkflowId\x12\x1d\n\ncommand_id\x18\x0c \x01(\tR\tcommandId\x12)\n\x10transfer_counter\x18\r \x01(\x03R\x0ftransferCounter\"\x8f\x05\n\x0eTransferInView\x12;\n\x04salt\x18\x01 \x01(\x0b\x32\'.com.digitalasset.canton.crypto.v0.SaltR\x04salt\x12\x1c\n\tsubmitter\x18\x02 \x01(\tR\tsubmitter\x12U\n\x08\x63ontract\x18\x03 \x01(\x0b\x32\x39.com.digitalasset.canton.protocol.v1.SerializableContractR\x08\x63ontract\x12m\n\x19transfer_out_result_event\x18\x04 \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v0.SignedContentR\x16transferOutResultEvent\x12\x36\n\x17\x63reating_transaction_id\x18\x05 \x01(\x0cR\x15\x63reatingTransactionId\x12\x36\n\x17source_protocol_version\x18\x06 \x01(\x05R\x15sourceProtocolVersion\x12\x35\n\x16submitting_participant\x18\x07 \x01(\tR\x15submittingParticipant\x12%\n\x0e\x61pplication_id\x18\x08 \x01(\tR\rapplicationId\x12#\n\rsubmission_id\x18\t \x01(\tR\x0csubmissionId\x12\x1f\n\x0bworkflow_id\x18\n \x01(\tR\nworkflowId\x12\x1d\n\ncommand_id\x18\x0b \x01(\tR\tcommandId\x12)\n\x10transfer_counter\x18\x0c \x01(\x03R\x0ftransferCounterBTZRgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v2.participant_transfer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v2'
  _globals['_TRANSFEROUTVIEW']._serialized_start=306
  _globals['_TRANSFEROUTVIEW']._serialized_end=899
  _globals['_TRANSFERINVIEW']._serialized_start=902
  _globals['_TRANSFERINVIEW']._serialized_end=1557
# @@protoc_insertion_point(module_scope)
