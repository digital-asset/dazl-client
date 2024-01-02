# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...protocol.v0 import sequencing_pb2 as _sequencing_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeProof(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _sequencing_pb2.PossiblyIgnoredSequencedEvent
    def __init__(self, event: _Optional[_Union[_sequencing_pb2.PossiblyIgnoredSequencedEvent, _Mapping]] = ...) -> None: ...
