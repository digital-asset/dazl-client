# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import sequencing_pb2 as _sequencing_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerVersion(_message.Message):
    __slots__ = ()
    class HandshakeRequest(_message.Message):
        __slots__ = ("handshake_request",)
        HANDSHAKE_REQUEST_FIELD_NUMBER: _ClassVar[int]
        handshake_request: _sequencing_pb2.Handshake.Request
        def __init__(self, handshake_request: _Optional[_Union[_sequencing_pb2.Handshake.Request, _Mapping]] = ...) -> None: ...
    class HandshakeResponse(_message.Message):
        __slots__ = ("handshake_response",)
        HANDSHAKE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        handshake_response: _sequencing_pb2.Handshake.Response
        def __init__(self, handshake_response: _Optional[_Union[_sequencing_pb2.Handshake.Response, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
