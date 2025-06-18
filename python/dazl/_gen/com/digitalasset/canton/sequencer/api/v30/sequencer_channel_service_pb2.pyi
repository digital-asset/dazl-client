# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v30 import crypto_pb2 as _crypto_pb2
from ....v30 import trace_context_pb2 as _trace_context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectToSequencerChannelRequest(_message.Message):
    __slots__ = ("metadata", "session_key", "session_key_acknowledgement", "payload", "trace_context")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    metadata: SequencerChannelMetadata
    session_key: SequencerChannelSessionKey
    session_key_acknowledgement: SequencerChannelSessionKeyAck
    payload: bytes
    trace_context: _trace_context_pb2.TraceContext
    def __init__(self, metadata: _Optional[_Union[SequencerChannelMetadata, _Mapping]] = ..., session_key: _Optional[_Union[SequencerChannelSessionKey, _Mapping]] = ..., session_key_acknowledgement: _Optional[_Union[SequencerChannelSessionKeyAck, _Mapping]] = ..., payload: _Optional[bytes] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ...) -> None: ...

class ConnectToSequencerChannelResponse(_message.Message):
    __slots__ = ("connected", "session_key", "session_key_acknowledgement", "payload", "trace_context")
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    connected: SequencerChannelConnectedToAllEndpoints
    session_key: SequencerChannelSessionKey
    session_key_acknowledgement: SequencerChannelSessionKeyAck
    payload: bytes
    trace_context: _trace_context_pb2.TraceContext
    def __init__(self, connected: _Optional[_Union[SequencerChannelConnectedToAllEndpoints, _Mapping]] = ..., session_key: _Optional[_Union[SequencerChannelSessionKey, _Mapping]] = ..., session_key_acknowledgement: _Optional[_Union[SequencerChannelSessionKeyAck, _Mapping]] = ..., payload: _Optional[bytes] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SequencerChannelMetadata(_message.Message):
    __slots__ = ("channel_id", "initiating_member", "receiving_member")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATING_MEMBER_FIELD_NUMBER: _ClassVar[int]
    RECEIVING_MEMBER_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    initiating_member: str
    receiving_member: str
    def __init__(self, channel_id: _Optional[str] = ..., initiating_member: _Optional[str] = ..., receiving_member: _Optional[str] = ...) -> None: ...

class SequencerChannelConnectedToAllEndpoints(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SequencerChannelSessionKey(_message.Message):
    __slots__ = ("encrypted_session_key",)
    ENCRYPTED_SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    encrypted_session_key: _crypto_pb2.AsymmetricEncrypted
    def __init__(self, encrypted_session_key: _Optional[_Union[_crypto_pb2.AsymmetricEncrypted, _Mapping]] = ...) -> None: ...

class SequencerChannelSessionKeyAck(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
