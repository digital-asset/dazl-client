# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from ....topology.admin.v30 import common_pb2 as _common_pb2
from ....v30 import trace_context_pb2 as _trace_context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendAsyncRequest(_message.Message):
    __slots__ = ("signed_submission_request",)
    SIGNED_SUBMISSION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    signed_submission_request: bytes
    def __init__(self, signed_submission_request: _Optional[bytes] = ...) -> None: ...

class TrafficControlErrorReason(_message.Message):
    __slots__ = ("error",)
    class Error(_message.Message):
        __slots__ = ("insufficient_traffic", "outdated_traffic_cost")
        INSUFFICIENT_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
        OUTDATED_TRAFFIC_COST_FIELD_NUMBER: _ClassVar[int]
        insufficient_traffic: str
        outdated_traffic_cost: str
        def __init__(self, insufficient_traffic: _Optional[str] = ..., outdated_traffic_cost: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: TrafficControlErrorReason.Error
    def __init__(self, error: _Optional[_Union[TrafficControlErrorReason.Error, _Mapping]] = ...) -> None: ...

class SendAsyncResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscriptionRequestV2(_message.Message):
    __slots__ = ("member", "timestamp")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    member: str
    timestamp: int
    def __init__(self, member: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class SubscriptionResponse(_message.Message):
    __slots__ = ("signed_sequenced_event", "trace_context")
    SIGNED_SEQUENCED_EVENT_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    signed_sequenced_event: bytes
    trace_context: _trace_context_pb2.TraceContext
    def __init__(self, signed_sequenced_event: _Optional[bytes] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ...) -> None: ...

class AcknowledgeRequest(_message.Message):
    __slots__ = ("member", "timestamp")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    member: str
    timestamp: int
    def __init__(self, member: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class AcknowledgeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcknowledgeSignedRequest(_message.Message):
    __slots__ = ("signed_acknowledge_request",)
    SIGNED_ACKNOWLEDGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    signed_acknowledge_request: bytes
    def __init__(self, signed_acknowledge_request: _Optional[bytes] = ...) -> None: ...

class AcknowledgeSignedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DownloadTopologyStateForInitRequest(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: str
    def __init__(self, member: _Optional[str] = ...) -> None: ...

class DownloadTopologyStateForInitResponse(_message.Message):
    __slots__ = ("topology_transactions",)
    TOPOLOGY_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    topology_transactions: _common_pb2.TopologyTransactions
    def __init__(self, topology_transactions: _Optional[_Union[_common_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...

class GetTrafficStateForMemberRequest(_message.Message):
    __slots__ = ("member", "timestamp")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    member: str
    timestamp: int
    def __init__(self, member: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class GetTrafficStateForMemberResponse(_message.Message):
    __slots__ = ("traffic_state",)
    TRAFFIC_STATE_FIELD_NUMBER: _ClassVar[int]
    traffic_state: _traffic_control_parameters_pb2.TrafficState
    def __init__(self, traffic_state: _Optional[_Union[_traffic_control_parameters_pb2.TrafficState, _Mapping]] = ...) -> None: ...
