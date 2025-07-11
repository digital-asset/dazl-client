# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/domain/api/v0/sequencer_authentication_service.proto
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
    'com/digitalasset/canton/domain/api/v0/sequencer_authentication_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....crypto.v0 import crypto_pb2 as com_dot_digitalasset_dot_canton_dot_crypto_dot_v0_dot_crypto__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLcom/digitalasset/canton/domain/api/v0/sequencer_authentication_service.proto\x12%com.digitalasset.canton.domain.api.v0\x1a.com/digitalasset/canton/crypto/v0/crypto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcd\x03\n\tChallenge\x1a[\n\x07Request\x12\x16\n\x06member\x18\x01 \x01(\tR\x06member\x12\x38\n\x18member_protocol_versions\x18\x02 \x03(\tR\x16memberProtocolVersions\x1a\xbf\x01\n\x08Response\x12T\n\x07success\x18\x01 \x01(\x0b\x32\x38.com.digitalasset.canton.domain.api.v0.Challenge.SuccessH\x00R\x07success\x12T\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x38.com.digitalasset.canton.domain.api.v0.Challenge.FailureH\x00R\x07\x66\x61ilureB\x07\n\x05value\x1aj\n\x07Success\x12%\n\x0e\x64omain_version\x18\x01 \x01(\tR\rdomainVersion\x12\x14\n\x05nonce\x18\x02 \x01(\x0cR\x05nonce\x12\"\n\x0c\x66ingerprints\x18\x03 \x03(\tR\x0c\x66ingerprints\x1a\x35\n\x07\x46\x61ilure\x12\x12\n\x04\x63ode\x18\x01 \x01(\rR\x04\x63ode\x12\x16\n\x06reason\x18\x02 \x01(\tR\x06reason\"\xf5\x03\n\x0e\x41uthentication\x1a\x83\x01\n\x07Request\x12\x16\n\x06member\x18\x01 \x01(\tR\x06member\x12J\n\tsignature\x18\x02 \x01(\x0b\x32,.com.digitalasset.canton.crypto.v0.SignatureR\tsignature\x12\x14\n\x05nonce\x18\x03 \x01(\x0cR\x05nonce\x1a\xc9\x01\n\x08Response\x12Y\n\x07success\x18\x01 \x01(\x0b\x32=.com.digitalasset.canton.domain.api.v0.Authentication.SuccessH\x00R\x07success\x12Y\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32=.com.digitalasset.canton.domain.api.v0.Authentication.FailureH\x00R\x07\x66\x61ilureB\x07\n\x05value\x1aZ\n\x07Success\x12\x14\n\x05token\x18\x01 \x01(\x0cR\x05token\x12\x39\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\x1a\x35\n\x07\x46\x61ilure\x12\x12\n\x04\x63ode\x18\x01 \x01(\rR\x04\x63ode\x12\x16\n\x06reason\x18\x02 \x01(\tR\x06reason2\xb7\x02\n\x1eSequencerAuthenticationService\x12\x82\x01\n\tChallenge\x12\x38.com.digitalasset.canton.domain.api.v0.Challenge.Request\x1a\x39.com.digitalasset.canton.domain.api.v0.Challenge.Response\"\x00\x12\x8f\x01\n\x0c\x41uthenticate\x12=.com.digitalasset.canton.domain.api.v0.Authentication.Request\x1a>.com.digitalasset.canton.domain.api.v0.Authentication.Response\"\x00\x42VZTgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/api/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.domain.api.v0.sequencer_authentication_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZTgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/domain/api/v0'
  _globals['_CHALLENGE']._serialized_start=201
  _globals['_CHALLENGE']._serialized_end=662
  _globals['_CHALLENGE_REQUEST']._serialized_start=214
  _globals['_CHALLENGE_REQUEST']._serialized_end=305
  _globals['_CHALLENGE_RESPONSE']._serialized_start=308
  _globals['_CHALLENGE_RESPONSE']._serialized_end=499
  _globals['_CHALLENGE_SUCCESS']._serialized_start=501
  _globals['_CHALLENGE_SUCCESS']._serialized_end=607
  _globals['_CHALLENGE_FAILURE']._serialized_start=609
  _globals['_CHALLENGE_FAILURE']._serialized_end=662
  _globals['_AUTHENTICATION']._serialized_start=665
  _globals['_AUTHENTICATION']._serialized_end=1166
  _globals['_AUTHENTICATION_REQUEST']._serialized_start=684
  _globals['_AUTHENTICATION_REQUEST']._serialized_end=815
  _globals['_AUTHENTICATION_RESPONSE']._serialized_start=818
  _globals['_AUTHENTICATION_RESPONSE']._serialized_end=1019
  _globals['_AUTHENTICATION_SUCCESS']._serialized_start=1021
  _globals['_AUTHENTICATION_SUCCESS']._serialized_end=1111
  _globals['_AUTHENTICATION_FAILURE']._serialized_start=609
  _globals['_AUTHENTICATION_FAILURE']._serialized_end=662
  _globals['_SEQUENCERAUTHENTICATIONSERVICE']._serialized_start=1169
  _globals['_SEQUENCERAUTHENTICATIONSERVICE']._serialized_end=1480
# @@protoc_insertion_point(module_scope)
