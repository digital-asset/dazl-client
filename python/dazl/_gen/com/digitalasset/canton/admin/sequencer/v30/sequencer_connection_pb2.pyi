# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
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
    __slots__ = ("grpc", "alias")
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
    grpc: SequencerConnection.Grpc
    alias: str
    def __init__(self, grpc: _Optional[_Union[SequencerConnection.Grpc, _Mapping]] = ..., alias: _Optional[str] = ...) -> None: ...

class SequencerConnections(_message.Message):
    __slots__ = ("sequencer_connections", "sequencer_trust_threshold", "submission_request_amplification")
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_TRUST_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_REQUEST_AMPLIFICATION_FIELD_NUMBER: _ClassVar[int]
    sequencer_connections: _containers.RepeatedCompositeFieldContainer[SequencerConnection]
    sequencer_trust_threshold: int
    submission_request_amplification: SubmissionRequestAmplification
    def __init__(self, sequencer_connections: _Optional[_Iterable[_Union[SequencerConnection, _Mapping]]] = ..., sequencer_trust_threshold: _Optional[int] = ..., submission_request_amplification: _Optional[_Union[SubmissionRequestAmplification, _Mapping]] = ...) -> None: ...

class SubmissionRequestAmplification(_message.Message):
    __slots__ = ("factor", "patience")
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    PATIENCE_FIELD_NUMBER: _ClassVar[int]
    factor: int
    patience: _duration_pb2.Duration
    def __init__(self, factor: _Optional[int] = ..., patience: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
