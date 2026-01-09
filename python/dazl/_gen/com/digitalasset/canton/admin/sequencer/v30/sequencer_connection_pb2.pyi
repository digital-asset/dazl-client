# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerConnectionValidation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEQUENCER_CONNECTION_VALIDATION_UNSPECIFIED: _ClassVar[SequencerConnectionValidation]
    SEQUENCER_CONNECTION_VALIDATION_DISABLED: _ClassVar[SequencerConnectionValidation]
    SEQUENCER_CONNECTION_VALIDATION_ACTIVE: _ClassVar[SequencerConnectionValidation]
    SEQUENCER_CONNECTION_VALIDATION_ALL: _ClassVar[SequencerConnectionValidation]
    SEQUENCER_CONNECTION_VALIDATION_THRESHOLD_ACTIVE: _ClassVar[SequencerConnectionValidation]
SEQUENCER_CONNECTION_VALIDATION_UNSPECIFIED: SequencerConnectionValidation
SEQUENCER_CONNECTION_VALIDATION_DISABLED: SequencerConnectionValidation
SEQUENCER_CONNECTION_VALIDATION_ACTIVE: SequencerConnectionValidation
SEQUENCER_CONNECTION_VALIDATION_ALL: SequencerConnectionValidation
SEQUENCER_CONNECTION_VALIDATION_THRESHOLD_ACTIVE: SequencerConnectionValidation

class SequencerConnection(_message.Message):
    __slots__ = ("grpc", "alias", "sequencer_id")
    class Grpc(_message.Message):
        __slots__ = ("connections", "transport_security", "custom_trust_certificates")
        CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_SECURITY_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_TRUST_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        connections: _containers.RepeatedScalarFieldContainer[str]
        transport_security: bool
        custom_trust_certificates: bytes
        def __init__(self, connections: _Optional[_Iterable[str]] = ..., transport_security: bool = ..., custom_trust_certificates: _Optional[bytes] = ...) -> None: ...
    GRPC_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_ID_FIELD_NUMBER: _ClassVar[int]
    grpc: SequencerConnection.Grpc
    alias: str
    sequencer_id: str
    def __init__(self, grpc: _Optional[_Union[SequencerConnection.Grpc, _Mapping]] = ..., alias: _Optional[str] = ..., sequencer_id: _Optional[str] = ...) -> None: ...

class SequencerConnections(_message.Message):
    __slots__ = ("sequencer_connections", "sequencer_trust_threshold", "submission_request_amplification", "sequencer_liveness_margin", "sequencer_connection_pool_delays")
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_TRUST_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_REQUEST_AMPLIFICATION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_LIVENESS_MARGIN_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_POOL_DELAYS_FIELD_NUMBER: _ClassVar[int]
    sequencer_connections: _containers.RepeatedCompositeFieldContainer[SequencerConnection]
    sequencer_trust_threshold: int
    submission_request_amplification: SubmissionRequestAmplification
    sequencer_liveness_margin: int
    sequencer_connection_pool_delays: SequencerConnectionPoolDelays
    def __init__(self, sequencer_connections: _Optional[_Iterable[_Union[SequencerConnection, _Mapping]]] = ..., sequencer_trust_threshold: _Optional[int] = ..., submission_request_amplification: _Optional[_Union[SubmissionRequestAmplification, _Mapping]] = ..., sequencer_liveness_margin: _Optional[int] = ..., sequencer_connection_pool_delays: _Optional[_Union[SequencerConnectionPoolDelays, _Mapping]] = ...) -> None: ...

class SubmissionRequestAmplification(_message.Message):
    __slots__ = ("factor", "patience")
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    PATIENCE_FIELD_NUMBER: _ClassVar[int]
    factor: int
    patience: _duration_pb2.Duration
    def __init__(self, factor: _Optional[int] = ..., patience: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SequencerConnectionPoolDelays(_message.Message):
    __slots__ = ("min_restart_delay", "max_restart_delay", "subscription_request_delay", "warn_validation_delay")
    MIN_RESTART_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_RESTART_DELAY_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_REQUEST_DELAY_FIELD_NUMBER: _ClassVar[int]
    WARN_VALIDATION_DELAY_FIELD_NUMBER: _ClassVar[int]
    min_restart_delay: _duration_pb2.Duration
    max_restart_delay: _duration_pb2.Duration
    subscription_request_delay: _duration_pb2.Duration
    warn_validation_delay: _duration_pb2.Duration
    def __init__(self, min_restart_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_restart_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., subscription_request_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., warn_validation_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
