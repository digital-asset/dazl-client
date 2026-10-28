# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v30 import bft_ordering_service_pb2 as _bft_ordering_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StateTransferMessage(_message.Message):
    __slots__ = ("block_request", "block_response")
    BLOCK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BLOCK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    block_request: _bft_ordering_service_pb2.BlockTransferRequest
    block_response: _bft_ordering_service_pb2.RetransmissionResponse
    def __init__(self, block_request: _Optional[_Union[_bft_ordering_service_pb2.BlockTransferRequest, _Mapping]] = ..., block_response: _Optional[_Union[_bft_ordering_service_pb2.RetransmissionResponse, _Mapping]] = ...) -> None: ...
