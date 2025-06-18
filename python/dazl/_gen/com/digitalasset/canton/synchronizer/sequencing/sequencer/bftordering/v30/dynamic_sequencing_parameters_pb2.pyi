# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DynamicSequencingParametersPayload(_message.Message):
    __slots__ = ("pbft_view_change_timeout",)
    PBFT_VIEW_CHANGE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    pbft_view_change_timeout: _duration_pb2.Duration
    def __init__(self, pbft_view_change_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
