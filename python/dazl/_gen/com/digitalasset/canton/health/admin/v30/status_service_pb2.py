# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/health/admin/v30/status_service.proto
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
    'com/digitalasset/canton/health/admin/v30/status_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=com/digitalasset/canton/health/admin/v30/status_service.proto\x12(com.digitalasset.canton.health.admin.v30\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\"i\n\x13TopologyQueueStatus\x12\x18\n\x07manager\x18\x01 \x01(\rR\x07manager\x12\x1e\n\ndispatcher\x18\x02 \x01(\rR\ndispatcher\x12\x18\n\x07\x63lients\x18\x03 \x01(\rR\x07\x63lients\"\x0f\n\rStatusRequest\"\x9f\r\n\x0eStatusResponse\x12r\n\x0fnot_initialized\x18\x01 \x01(\x0b\x32G.com.digitalasset.canton.health.admin.v30.StatusResponse.NotInitializedH\x00R\x0enotInitialized\x12[\n\x07success\x18\x02 \x01(\x0b\x32?.com.digitalasset.canton.health.admin.v30.StatusResponse.StatusH\x00R\x07success\x1a\xe7\x03\n\x06Status\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x31\n\x06uptime\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06uptime\x12`\n\x05ports\x18\x03 \x03(\x0b\x32J.com.digitalasset.canton.health.admin.v30.StatusResponse.Status.PortsEntryR\x05ports\x12\x14\n\x05\x65xtra\x18\x04 \x01(\x0cR\x05\x65xtra\x12\x16\n\x06\x61\x63tive\x18\x05 \x01(\x08R\x06\x61\x63tive\x12\x66\n\x0ftopology_queues\x18\x06 \x01(\x0b\x32=.com.digitalasset.canton.health.admin.v30.TopologyQueueStatusR\x0etopologyQueues\x12h\n\ncomponents\x18\x07 \x03(\x0b\x32H.com.digitalasset.canton.health.admin.v30.StatusResponse.ComponentStatusR\ncomponents\x1a\x38\n\nPortsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\x1a\xb3\x04\n\x0f\x43omponentStatus\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x65\n\x02ok\x18\x02 \x01(\x0b\x32S.com.digitalasset.canton.health.admin.v30.StatusResponse.ComponentStatus.StatusDataH\x00R\x02ok\x12q\n\x08\x64\x65graded\x18\x03 \x01(\x0b\x32S.com.digitalasset.canton.health.admin.v30.StatusResponse.ComponentStatus.StatusDataH\x00R\x08\x64\x65graded\x12m\n\x06\x66\x61iled\x18\x04 \x01(\x0b\x32S.com.digitalasset.canton.health.admin.v30.StatusResponse.ComponentStatus.StatusDataH\x00R\x06\x66\x61iled\x12k\n\x05\x66\x61tal\x18\x05 \x01(\x0b\x32S.com.digitalasset.canton.health.admin.v30.StatusResponse.ComponentStatus.StatusDataH\x00R\x05\x66\x61tal\x1aL\n\nStatusData\x12>\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0b\x64\x65scriptionB\x08\n\x06status\x1a\x8f\x03\n\x0eNotInitialized\x12\x16\n\x06\x61\x63tive\x18\x01 \x01(\x08R\x06\x61\x63tive\x12\x9c\x01\n\x1awaiting_for_external_input\x18\x02 \x01(\x0e\x32_.com.digitalasset.canton.health.admin.v30.StatusResponse.NotInitialized.WaitingForExternalInputR\x17waitingForExternalInput\"\xc5\x01\n\x17WaitingForExternalInput\x12*\n&WAITING_FOR_EXTERNAL_INPUT_UNSPECIFIED\x10\x00\x12!\n\x1dWAITING_FOR_EXTERNAL_INPUT_ID\x10\x01\x12,\n(WAITING_FOR_EXTERNAL_INPUT_NODE_TOPOLOGY\x10\x02\x12-\n)WAITING_FOR_EXTERNAL_INPUT_INITIALIZATION\x10\x03\x42\n\n\x08response\"P\n\x11HealthDumpRequest\x12;\n\nchunk_size\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\tchunkSize\"*\n\x12HealthDumpResponse\x12\x14\n\x05\x63hunk\x18\x01 \x01(\x0cR\x05\x63hunk\"\xf2\x01\n\x15ParticipantStatusInfo\x12|\n\x11\x63onnected_domains\x18\x01 \x03(\x0b\x32O.com.digitalasset.canton.health.admin.v30.ParticipantStatusInfo.ConnectedDomainR\x10\x63onnectedDomains\x12\x16\n\x06\x61\x63tive\x18\x02 \x01(\x08R\x06\x61\x63tive\x1a\x43\n\x0f\x43onnectedDomain\x12\x16\n\x06\x64omain\x18\x01 \x01(\tR\x06\x64omain\x12\x18\n\x07healthy\x18\x02 \x01(\x08R\x07healthy\"\xa5\x02\n\x13SequencerNodeStatus\x12<\n\x1a\x63onnected_participant_uids\x18\x01 \x03(\tR\x18\x63onnectedParticipantUids\x12]\n\tsequencer\x18\x02 \x01(\x0b\x32?.com.digitalasset.canton.health.admin.v30.SequencerHealthStatusR\tsequencer\x12\x1b\n\tdomain_id\x18\x03 \x01(\tR\x08\x64omainId\x12T\n\x05\x61\x64min\x18\x04 \x01(\x0b\x32>.com.digitalasset.canton.health.admin.v30.SequencerAdminStatusR\x05\x61\x64min\"g\n\x15SequencerHealthStatus\x12\x16\n\x06\x61\x63tive\x18\x01 \x01(\x08R\x06\x61\x63tive\x12\x36\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x07\x64\x65tails\"J\n\x14SequencerAdminStatus\x12\x32\n\x15\x61\x63\x63\x65pts_admin_changes\x18\x01 \x01(\x08R\x13\x61\x63\x63\x65ptsAdminChanges\"1\n\x12MediatorNodeStatus\x12\x1b\n\tdomain_id\x18\x01 \x01(\tR\x08\x64omainId\"*\n\x12SetLogLevelRequest\x12\x14\n\x05level\x18\x01 \x01(\tR\x05level\"\x15\n\x13SetLogLevelResponse\"\x16\n\x14GetLastErrorsRequest\"\xb4\x01\n\x15GetLastErrorsResponse\x12]\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x45.com.digitalasset.canton.health.admin.v30.GetLastErrorsResponse.ErrorR\x06\x65rrors\x1a<\n\x05\x45rror\x12\x19\n\x08trace_id\x18\x01 \x01(\tR\x07traceId\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\"5\n\x18GetLastErrorTraceRequest\x12\x19\n\x08trace_id\x18\x01 \x01(\tR\x07traceId\"7\n\x19GetLastErrorTraceResponse\x12\x1a\n\x08messages\x18\x01 \x03(\tR\x08messages2\xd7\x05\n\rStatusService\x12{\n\x06Status\x12\x37.com.digitalasset.canton.health.admin.v30.StatusRequest\x1a\x38.com.digitalasset.canton.health.admin.v30.StatusResponse\x12\x89\x01\n\nHealthDump\x12;.com.digitalasset.canton.health.admin.v30.HealthDumpRequest\x1a<.com.digitalasset.canton.health.admin.v30.HealthDumpResponse0\x01\x12\x8a\x01\n\x0bSetLogLevel\x12<.com.digitalasset.canton.health.admin.v30.SetLogLevelRequest\x1a=.com.digitalasset.canton.health.admin.v30.SetLogLevelResponse\x12\x90\x01\n\rGetLastErrors\x12>.com.digitalasset.canton.health.admin.v30.GetLastErrorsRequest\x1a?.com.digitalasset.canton.health.admin.v30.GetLastErrorsResponse\x12\x9c\x01\n\x11GetLastErrorTrace\x12\x42.com.digitalasset.canton.health.admin.v30.GetLastErrorTraceRequest\x1a\x43.com.digitalasset.canton.health.admin.v30.GetLastErrorTraceResponseBYZWgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/health/admin/v30b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.health.admin.v30.status_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZWgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/health/admin/v30'
  _globals['_STATUSRESPONSE_STATUS_PORTSENTRY']._loaded_options = None
  _globals['_STATUSRESPONSE_STATUS_PORTSENTRY']._serialized_options = b'8\001'
  _globals['_TOPOLOGYQUEUESTATUS']._serialized_start=171
  _globals['_TOPOLOGYQUEUESTATUS']._serialized_end=276
  _globals['_STATUSREQUEST']._serialized_start=278
  _globals['_STATUSREQUEST']._serialized_end=293
  _globals['_STATUSRESPONSE']._serialized_start=296
  _globals['_STATUSRESPONSE']._serialized_end=1991
  _globals['_STATUSRESPONSE_STATUS']._serialized_start=524
  _globals['_STATUSRESPONSE_STATUS']._serialized_end=1011
  _globals['_STATUSRESPONSE_STATUS_PORTSENTRY']._serialized_start=955
  _globals['_STATUSRESPONSE_STATUS_PORTSENTRY']._serialized_end=1011
  _globals['_STATUSRESPONSE_COMPONENTSTATUS']._serialized_start=1014
  _globals['_STATUSRESPONSE_COMPONENTSTATUS']._serialized_end=1577
  _globals['_STATUSRESPONSE_COMPONENTSTATUS_STATUSDATA']._serialized_start=1491
  _globals['_STATUSRESPONSE_COMPONENTSTATUS_STATUSDATA']._serialized_end=1567
  _globals['_STATUSRESPONSE_NOTINITIALIZED']._serialized_start=1580
  _globals['_STATUSRESPONSE_NOTINITIALIZED']._serialized_end=1979
  _globals['_STATUSRESPONSE_NOTINITIALIZED_WAITINGFOREXTERNALINPUT']._serialized_start=1782
  _globals['_STATUSRESPONSE_NOTINITIALIZED_WAITINGFOREXTERNALINPUT']._serialized_end=1979
  _globals['_HEALTHDUMPREQUEST']._serialized_start=1993
  _globals['_HEALTHDUMPREQUEST']._serialized_end=2073
  _globals['_HEALTHDUMPRESPONSE']._serialized_start=2075
  _globals['_HEALTHDUMPRESPONSE']._serialized_end=2117
  _globals['_PARTICIPANTSTATUSINFO']._serialized_start=2120
  _globals['_PARTICIPANTSTATUSINFO']._serialized_end=2362
  _globals['_PARTICIPANTSTATUSINFO_CONNECTEDDOMAIN']._serialized_start=2295
  _globals['_PARTICIPANTSTATUSINFO_CONNECTEDDOMAIN']._serialized_end=2362
  _globals['_SEQUENCERNODESTATUS']._serialized_start=2365
  _globals['_SEQUENCERNODESTATUS']._serialized_end=2658
  _globals['_SEQUENCERHEALTHSTATUS']._serialized_start=2660
  _globals['_SEQUENCERHEALTHSTATUS']._serialized_end=2763
  _globals['_SEQUENCERADMINSTATUS']._serialized_start=2765
  _globals['_SEQUENCERADMINSTATUS']._serialized_end=2839
  _globals['_MEDIATORNODESTATUS']._serialized_start=2841
  _globals['_MEDIATORNODESTATUS']._serialized_end=2890
  _globals['_SETLOGLEVELREQUEST']._serialized_start=2892
  _globals['_SETLOGLEVELREQUEST']._serialized_end=2934
  _globals['_SETLOGLEVELRESPONSE']._serialized_start=2936
  _globals['_SETLOGLEVELRESPONSE']._serialized_end=2957
  _globals['_GETLASTERRORSREQUEST']._serialized_start=2959
  _globals['_GETLASTERRORSREQUEST']._serialized_end=2981
  _globals['_GETLASTERRORSRESPONSE']._serialized_start=2984
  _globals['_GETLASTERRORSRESPONSE']._serialized_end=3164
  _globals['_GETLASTERRORSRESPONSE_ERROR']._serialized_start=3104
  _globals['_GETLASTERRORSRESPONSE_ERROR']._serialized_end=3164
  _globals['_GETLASTERRORTRACEREQUEST']._serialized_start=3166
  _globals['_GETLASTERRORTRACEREQUEST']._serialized_end=3219
  _globals['_GETLASTERRORTRACERESPONSE']._serialized_start=3221
  _globals['_GETLASTERRORTRACERESPONSE']._serialized_end=3276
  _globals['_STATUSSERVICE']._serialized_start=3279
  _globals['_STATUSSERVICE']._serialized_end=4006
# @@protoc_insertion_point(module_scope)
