# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerAuthentication(_message.Message):
    __slots__ = ()
    class ChallengeRequest(_message.Message):
        __slots__ = ("member", "member_protocol_versions")
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        MEMBER_PROTOCOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        member: str
        member_protocol_versions: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, member: _Optional[str] = ..., member_protocol_versions: _Optional[_Iterable[int]] = ...) -> None: ...
    class ChallengeResponse(_message.Message):
        __slots__ = ("nonce", "fingerprints")
        NONCE_FIELD_NUMBER: _ClassVar[int]
        FINGERPRINTS_FIELD_NUMBER: _ClassVar[int]
        nonce: bytes
        fingerprints: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, nonce: _Optional[bytes] = ..., fingerprints: _Optional[_Iterable[str]] = ...) -> None: ...
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
        __slots__ = ("token", "expires_at")
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
        token: bytes
        expires_at: _timestamp_pb2.Timestamp
        def __init__(self, token: _Optional[bytes] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class LogoutRequest(_message.Message):
        __slots__ = ("token",)
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        token: bytes
        def __init__(self, token: _Optional[bytes] = ...) -> None: ...
    class LogoutResponse(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
