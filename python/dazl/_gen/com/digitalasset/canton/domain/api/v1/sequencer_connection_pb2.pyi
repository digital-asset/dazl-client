# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v0 import sequencer_connection_pb2 as _sequencer_connection_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerConnections(_message.Message):
    __slots__ = ["sequencer_connections", "sequencerTrustThreshold"]
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCERTRUSTTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    sequencer_connections: _containers.RepeatedCompositeFieldContainer[_sequencer_connection_pb2.SequencerConnection]
    sequencerTrustThreshold: int
    def __init__(self, sequencer_connections: _Optional[_Iterable[_Union[_sequencer_connection_pb2.SequencerConnection, _Mapping]]] = ..., sequencerTrustThreshold: _Optional[int] = ...) -> None: ...
