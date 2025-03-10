# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerAuthentication(_message.Message):
    __slots__ = ()
    class ChallengeRequest(_message.Message):
        __slots__ = ("member", "member_protocol_versions")
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        MEMBER_PROTOCOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        member: str
        member_protocol_versions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, member: _Optional[str] = ..., member_protocol_versions: _Optional[_Iterable[str]] = ...) -> None: ...
    class ChallengeResponse(_message.Message):
        __slots__ = ("success", "failure")
        class Success(_message.Message):
            __slots__ = ("domain_version", "nonce", "fingerprints")
            DOMAIN_VERSION_FIELD_NUMBER: _ClassVar[int]
            NONCE_FIELD_NUMBER: _ClassVar[int]
            FINGERPRINTS_FIELD_NUMBER: _ClassVar[int]
            domain_version: str
            nonce: bytes
            fingerprints: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, domain_version: _Optional[str] = ..., nonce: _Optional[bytes] = ..., fingerprints: _Optional[_Iterable[str]] = ...) -> None: ...
        class Failure(_message.Message):
            __slots__ = ("code", "reason")
            CODE_FIELD_NUMBER: _ClassVar[int]
            REASON_FIELD_NUMBER: _ClassVar[int]
            code: int
            reason: str
            def __init__(self, code: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        success: SequencerAuthentication.ChallengeResponse.Success
        failure: SequencerAuthentication.ChallengeResponse.Failure
        def __init__(self, success: _Optional[_Union[SequencerAuthentication.ChallengeResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SequencerAuthentication.ChallengeResponse.Failure, _Mapping]] = ...) -> None: ...
    class AuthenticateRequest(_message.Message):
        __slots__ = ("member", "signature", "nonce")
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        NONCE_FIELD_NUMBER: _ClassVar[int]
        member: str
        signature: _crypto_pb2.Signature
        nonce: bytes
        def __init__(self, member: _Optional[str] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., nonce: _Optional[bytes] = ...) -> None: ...
    class AuthenticateResponse(_message.Message):
        __slots__ = ("success", "failure")
        class Success(_message.Message):
            __slots__ = ("token", "expires_at")
            TOKEN_FIELD_NUMBER: _ClassVar[int]
            EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
            token: bytes
            expires_at: _timestamp_pb2.Timestamp
            def __init__(self, token: _Optional[bytes] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class Failure(_message.Message):
            __slots__ = ("code", "reason")
            CODE_FIELD_NUMBER: _ClassVar[int]
            REASON_FIELD_NUMBER: _ClassVar[int]
            code: int
            reason: str
            def __init__(self, code: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        success: SequencerAuthentication.AuthenticateResponse.Success
        failure: SequencerAuthentication.AuthenticateResponse.Failure
        def __init__(self, success: _Optional[_Union[SequencerAuthentication.AuthenticateResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SequencerAuthentication.AuthenticateResponse.Failure, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
