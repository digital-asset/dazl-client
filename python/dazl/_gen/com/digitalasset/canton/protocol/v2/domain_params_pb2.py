# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/protocol/v2/domain_params.proto
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
    'com/digitalasset/canton/protocol/v2/domain_params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7com/digitalasset/canton/protocol/v2/domain_params.proto\x12#com.digitalasset.canton.protocol.v2\x1a\x1egoogle/protobuf/duration.proto\"\x89\x01\n\rCatchUpConfig\x12\x32\n\x15\x63\x61tchup_interval_skip\x18\x01 \x01(\rR\x13\x63\x61tchupIntervalSkip\x12\x44\n\x1fnr_intervals_to_trigger_catchup\x18\x02 \x01(\rR\x1bnrIntervalsToTriggerCatchup\"\xda\x06\n\x17\x44ynamicDomainParameters\x12[\n\x1cparticipant_response_timeout\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1aparticipantResponseTimeout\x12U\n\x19mediator_reaction_timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x17mediatorReactionTimeout\x12[\n\x1ctransfer_exclusivity_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1atransferExclusivityTimeout\x12M\n\x15topology_change_delay\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x13topologyChangeDelay\x12\x63\n!ledger_time_record_time_tolerance\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1dledgerTimeRecordTimeTolerance\x12R\n\x17reconciliation_interval\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationR\x16reconciliationInterval\x12_\n\x1emediator_deduplication_timeout\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1cmediatorDeduplicationTimeout\x12\x37\n\x18max_rate_per_participant\x18\x08 \x01(\rR\x15maxRatePerParticipant\x12(\n\x10max_request_size\x18\t \x01(\rR\x0emaxRequestSize\x12\x62\n\x13\x63\x61tch_up_parameters\x18\n \x01(\x0b\x32\x32.com.digitalasset.canton.protocol.v2.CatchUpConfigR\x11\x63\x61tchUpParametersBTZRgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.protocol.v2.domain_params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/protocol/v2'
  _globals['_CATCHUPCONFIG']._serialized_start=129
  _globals['_CATCHUPCONFIG']._serialized_end=266
  _globals['_DYNAMICDOMAINPARAMETERS']._serialized_start=269
  _globals['_DYNAMICDOMAINPARAMETERS']._serialized_end=1127
# @@protoc_insertion_point(module_scope)
