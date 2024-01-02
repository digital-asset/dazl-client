# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....traffic.v0 import member_traffic_status_pb2 as _member_traffic_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrafficControlStateRequest(_message.Message):
    __slots__ = ["domain_id"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    def __init__(self, domain_id: _Optional[str] = ...) -> None: ...

class TrafficControlStateResponse(_message.Message):
    __slots__ = ["traffic_state"]
    TRAFFIC_STATE_FIELD_NUMBER: _ClassVar[int]
    traffic_state: _member_traffic_status_pb2.MemberTrafficStatus
    def __init__(self, traffic_state: _Optional[_Union[_member_traffic_status_pb2.MemberTrafficStatus, _Mapping]] = ...) -> None: ...
