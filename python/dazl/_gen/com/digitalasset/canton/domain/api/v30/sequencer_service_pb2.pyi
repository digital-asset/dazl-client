# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from ....topology.admin.v30 import topology_ext_pb2 as _topology_ext_pb2
from ....v30 import trace_context_pb2 as _trace_context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendAsyncVersionedRequest(_message.Message):
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

class SendAsyncVersionedResponse(_message.Message):
    __slots__ = ("error",)
    class Error(_message.Message):
        __slots__ = ("request_invalid", "request_refused", "overloaded", "sender_unknown", "shutting_down", "unavailable", "unknown_recipients", "internal", "generic", "traffic_control")
        REQUEST_INVALID_FIELD_NUMBER: _ClassVar[int]
        REQUEST_REFUSED_FIELD_NUMBER: _ClassVar[int]
        OVERLOADED_FIELD_NUMBER: _ClassVar[int]
        SENDER_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        SHUTTING_DOWN_FIELD_NUMBER: _ClassVar[int]
        UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_FIELD_NUMBER: _ClassVar[int]
        GENERIC_FIELD_NUMBER: _ClassVar[int]
        TRAFFIC_CONTROL_FIELD_NUMBER: _ClassVar[int]
        request_invalid: str
        request_refused: str
        overloaded: str
        sender_unknown: str
        shutting_down: str
        unavailable: str
        unknown_recipients: str
        internal: str
        generic: str
        traffic_control: TrafficControlErrorReason
        def __init__(self, request_invalid: _Optional[str] = ..., request_refused: _Optional[str] = ..., overloaded: _Optional[str] = ..., sender_unknown: _Optional[str] = ..., shutting_down: _Optional[str] = ..., unavailable: _Optional[str] = ..., unknown_recipients: _Optional[str] = ..., internal: _Optional[str] = ..., generic: _Optional[str] = ..., traffic_control: _Optional[_Union[TrafficControlErrorReason, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: SendAsyncVersionedResponse.Error
    def __init__(self, error: _Optional[_Union[SendAsyncVersionedResponse.Error, _Mapping]] = ...) -> None: ...

class SubscriptionRequest(_message.Message):
    __slots__ = ("member", "counter")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    member: str
    counter: int
    def __init__(self, member: _Optional[str] = ..., counter: _Optional[int] = ...) -> None: ...

class VersionedSubscriptionResponse(_message.Message):
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
    topology_transactions: _topology_ext_pb2.TopologyTransactions
    def __init__(self, topology_transactions: _Optional[_Union[_topology_ext_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...

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

class SequencedEventTrafficState(_message.Message):
    __slots__ = ("extra_traffic_remainder", "extra_traffic_consumed")
    EXTRA_TRAFFIC_REMAINDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_TRAFFIC_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    extra_traffic_remainder: int
    extra_traffic_consumed: int
    def __init__(self, extra_traffic_remainder: _Optional[int] = ..., extra_traffic_consumed: _Optional[int] = ...) -> None: ...
