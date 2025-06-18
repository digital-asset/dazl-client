# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....admin.sequencer.v30 import sequencer_connection_pb2 as _sequencer_connection_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConnectionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConnectionResponse(_message.Message):
    __slots__ = ("sequencer_connections",)
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    sequencer_connections: _sequencer_connection_pb2.SequencerConnections
    def __init__(self, sequencer_connections: _Optional[_Union[_sequencer_connection_pb2.SequencerConnections, _Mapping]] = ...) -> None: ...

class SetConnectionRequest(_message.Message):
    __slots__ = ("sequencer_connections", "sequencer_connection_validation")
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    sequencer_connections: _sequencer_connection_pb2.SequencerConnections
    sequencer_connection_validation: _sequencer_connection_pb2.SequencerConnectionValidation
    def __init__(self, sequencer_connections: _Optional[_Union[_sequencer_connection_pb2.SequencerConnections, _Mapping]] = ..., sequencer_connection_validation: _Optional[_Union[_sequencer_connection_pb2.SequencerConnectionValidation, str]] = ...) -> None: ...

class SetConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
