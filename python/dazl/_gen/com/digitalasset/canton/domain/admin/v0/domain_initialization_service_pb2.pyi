# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...api.v0 import sequencer_connection_pb2 as _sequencer_connection_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainNodeSequencerConfig(_message.Message):
    __slots__ = ["sequencerConnection"]
    SEQUENCERCONNECTION_FIELD_NUMBER: _ClassVar[int]
    sequencerConnection: _sequencer_connection_pb2.SequencerConnection
    def __init__(self, sequencerConnection: _Optional[_Union[_sequencer_connection_pb2.SequencerConnection, _Mapping]] = ...) -> None: ...

class DomainInitRequest(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: DomainNodeSequencerConfig
    def __init__(self, config: _Optional[_Union[DomainNodeSequencerConfig, _Mapping]] = ...) -> None: ...
