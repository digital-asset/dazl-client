# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....admin.domain.v30 import sequencer_connection_pb2 as _sequencer_connection_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitializeMediatorRequest(_message.Message):
    __slots__ = ("domain_id", "sequencer_connections", "sequencer_connection_validation")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    sequencer_connections: _sequencer_connection_pb2.SequencerConnections
    sequencer_connection_validation: _sequencer_connection_pb2.SequencerConnectionValidation
    def __init__(self, domain_id: _Optional[str] = ..., sequencer_connections: _Optional[_Union[_sequencer_connection_pb2.SequencerConnections, _Mapping]] = ..., sequencer_connection_validation: _Optional[_Union[_sequencer_connection_pb2.SequencerConnectionValidation, str]] = ...) -> None: ...

class InitializeMediatorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
