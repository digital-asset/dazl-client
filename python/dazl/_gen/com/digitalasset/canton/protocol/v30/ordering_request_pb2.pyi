# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderingRequest(_message.Message):
    __slots__ = ("sequencer_uid", "content")
    SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    sequencer_uid: str
    content: _wrappers_pb2.BytesValue
    def __init__(self, sequencer_uid: _Optional[str] = ..., content: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...
