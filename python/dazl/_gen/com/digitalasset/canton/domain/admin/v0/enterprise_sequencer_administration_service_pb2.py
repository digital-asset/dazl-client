# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/canton/domain/admin/v0/enterprise_sequencer_administration_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import sequencer_initialization_snapshot_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__snapshot__pb2
from ....pruning.admin.v0 import pruning_pb2 as com_dot_digitalasset_dot_canton_dot_pruning_dot_admin_dot_v0_dot_pruning__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nYcom/digitalasset/canton/domain/admin/v0/enterprise_sequencer_administration_service.proto\x12\'com.digitalasset.canton.domain.admin.v0\x1aOcom/digitalasset/canton/domain/admin/v0/sequencer_initialization_snapshot.proto\x1a\x36\x63om/digitalasset/canton/pruning/admin/v0/pruning.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"+\n\x0f\x45thereumAccount\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\"\xf5\x03\n\x0eLedgerIdentity\x12\x65\n\x10\x65thereum_account\x18\x01 \x01(\x0b\x32\x38.com.digitalasset.canton.domain.admin.v0.EthereumAccountH\x00R\x0f\x65thereumAccount\x1ag\n\x10\x41uthorizeRequest\x12S\n\x08identify\x18\x01 \x01(\x0b\x32\x37.com.digitalasset.canton.domain.admin.v0.LedgerIdentityR\x08identify\x1a\xd6\x01\n\x11\x41uthorizeResponse\x12[\n\x07success\x18\x01 \x01(\x0b\x32?.com.digitalasset.canton.domain.admin.v0.LedgerIdentity.SuccessH\x00R\x07success\x12[\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32?.com.digitalasset.canton.domain.admin.v0.LedgerIdentity.FailureH\x00R\x07\x66\x61ilureB\x07\n\x05value\x1a\t\n\x07Success\x1a!\n\x07\x46\x61ilure\x12\x16\n\x06reason\x18\x01 \x01(\tR\x06reasonB\x0c\n\nidentifier\"t\n\x07Pruning\x1a\x43\n\x07Request\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x1a$\n\x08Response\x12\x18\n\x07\x64\x65tails\x18\x01 \x01(\tR\x07\x64\x65tails\"\xb5\x04\n\x08Snapshot\x1a\x43\n\x07Request\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x1a\xb3\x02\n\x08Response\x12U\n\x07success\x18\x01 \x01(\x0b\x32\x39.com.digitalasset.canton.domain.admin.v0.Snapshot.SuccessH\x00R\x07success\x12U\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x39.com.digitalasset.canton.domain.admin.v0.Snapshot.FailureH\x00R\x07\x66\x61ilure\x12p\n\x10versionedSuccess\x18\x03 \x01(\x0b\x32\x42.com.digitalasset.canton.domain.admin.v0.Snapshot.VersionedSuccessH\x00R\x10versionedSuccessB\x07\n\x05value\x1a[\n\x07Success\x12P\n\x05state\x18\x01 \x01(\x0b\x32:.com.digitalasset.canton.domain.admin.v0.SequencerSnapshotR\x05state\x1a!\n\x07\x46\x61ilure\x12\x16\n\x06reason\x18\x01 \x01(\tR\x06reason\x1a.\n\x10VersionedSuccess\x12\x1a\n\x08snapshot\x18\x01 \x01(\x0cR\x08snapshot\".\n\x14\x44isableMemberRequest\x12\x16\n\x06member\x18\x01 \x01(\tR\x06member2\xd5\x0c\n(EnterpriseSequencerAdministrationService\x12|\n\x05Prune\x12\x38.com.digitalasset.canton.domain.admin.v0.Pruning.Request\x1a\x39.com.digitalasset.canton.domain.admin.v0.Pruning.Response\x12\x81\x01\n\x08Snapshot\x12\x39.com.digitalasset.canton.domain.admin.v0.Snapshot.Request\x1a:.com.digitalasset.canton.domain.admin.v0.Snapshot.Response\x12\x66\n\rDisableMember\x12=.com.digitalasset.canton.domain.admin.v0.DisableMemberRequest\x1a\x16.google.protobuf.Empty\x12\xae\x01\n\x17\x41uthorizeLedgerIdentity\x12H.com.digitalasset.canton.domain.admin.v0.LedgerIdentity.AuthorizeRequest\x1aI.com.digitalasset.canton.domain.admin.v0.LedgerIdentity.AuthorizeResponse\x12\x8c\x01\n\x0bSetSchedule\x12=.com.digitalasset.canton.pruning.admin.v0.SetSchedule.Request\x1a>.com.digitalasset.canton.pruning.admin.v0.SetSchedule.Response\x12\x80\x01\n\x07SetCron\x12\x39.com.digitalasset.canton.pruning.admin.v0.SetCron.Request\x1a:.com.digitalasset.canton.pruning.admin.v0.SetCron.Response\x12\x95\x01\n\x0eSetMaxDuration\x12@.com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Request\x1a\x41.com.digitalasset.canton.pruning.admin.v0.SetMaxDuration.Response\x12\x8f\x01\n\x0cSetRetention\x12>.com.digitalasset.canton.pruning.admin.v0.SetRetention.Request\x1a?.com.digitalasset.canton.pruning.admin.v0.SetRetention.Response\x12\x92\x01\n\rClearSchedule\x12?.com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Request\x1a@.com.digitalasset.canton.pruning.admin.v0.ClearSchedule.Response\x12\x8c\x01\n\x0bGetSchedule\x12=.com.digitalasset.canton.pruning.admin.v0.GetSchedule.Request\x1a>.com.digitalasset.canton.pruning.admin.v0.GetSchedule.Response\x12\xad\x01\n\x16LocatePruningTimestamp\x12H.com.digitalasset.canton.pruning.admin.v0.LocatePruningTimestamp.Request\x1aI.com.digitalasset.canton.pruning.admin.v0.LocatePruningTimestamp.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.admin.v0.enterprise_sequencer_administration_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ETHEREUMACCOUNT']._serialized_start=333
  _globals['_ETHEREUMACCOUNT']._serialized_end=376
  _globals['_LEDGERIDENTITY']._serialized_start=379
  _globals['_LEDGERIDENTITY']._serialized_end=880
  _globals['_LEDGERIDENTITY_AUTHORIZEREQUEST']._serialized_start=500
  _globals['_LEDGERIDENTITY_AUTHORIZEREQUEST']._serialized_end=603
  _globals['_LEDGERIDENTITY_AUTHORIZERESPONSE']._serialized_start=606
  _globals['_LEDGERIDENTITY_AUTHORIZERESPONSE']._serialized_end=820
  _globals['_LEDGERIDENTITY_SUCCESS']._serialized_start=822
  _globals['_LEDGERIDENTITY_SUCCESS']._serialized_end=831
  _globals['_LEDGERIDENTITY_FAILURE']._serialized_start=833
  _globals['_LEDGERIDENTITY_FAILURE']._serialized_end=866
  _globals['_PRUNING']._serialized_start=882
  _globals['_PRUNING']._serialized_end=998
  _globals['_PRUNING_REQUEST']._serialized_start=893
  _globals['_PRUNING_REQUEST']._serialized_end=960
  _globals['_PRUNING_RESPONSE']._serialized_start=962
  _globals['_PRUNING_RESPONSE']._serialized_end=998
  _globals['_SNAPSHOT']._serialized_start=1001
  _globals['_SNAPSHOT']._serialized_end=1566
  _globals['_SNAPSHOT_REQUEST']._serialized_start=893
  _globals['_SNAPSHOT_REQUEST']._serialized_end=960
  _globals['_SNAPSHOT_RESPONSE']._serialized_start=1083
  _globals['_SNAPSHOT_RESPONSE']._serialized_end=1390
  _globals['_SNAPSHOT_SUCCESS']._serialized_start=1392
  _globals['_SNAPSHOT_SUCCESS']._serialized_end=1483
  _globals['_SNAPSHOT_FAILURE']._serialized_start=833
  _globals['_SNAPSHOT_FAILURE']._serialized_end=866
  _globals['_SNAPSHOT_VERSIONEDSUCCESS']._serialized_start=1520
  _globals['_SNAPSHOT_VERSIONEDSUCCESS']._serialized_end=1566
  _globals['_DISABLEMEMBERREQUEST']._serialized_start=1568
  _globals['_DISABLEMEMBERREQUEST']._serialized_end=1614
  _globals['_ENTERPRISESEQUENCERADMINISTRATIONSERVICE']._serialized_start=1617
  _globals['_ENTERPRISESEQUENCERADMINISTRATIONSERVICE']._serialized_end=3238
# @@protoc_insertion_point(module_scope)