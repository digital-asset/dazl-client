# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerConnectionValidation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[SequencerConnectionValidation]
    DISABLED: _ClassVar[SequencerConnectionValidation]
    ACTIVE: _ClassVar[SequencerConnectionValidation]
    ALL: _ClassVar[SequencerConnectionValidation]
UNKNOWN: SequencerConnectionValidation
DISABLED: SequencerConnectionValidation
ACTIVE: SequencerConnectionValidation
ALL: SequencerConnectionValidation

class SequencerConnection(_message.Message):
    __slots__ = ("grpc", "alias")
    class Grpc(_message.Message):
        __slots__ = ("connections", "transportSecurity", "customTrustCertificates")
        CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        TRANSPORTSECURITY_FIELD_NUMBER: _ClassVar[int]
        CUSTOMTRUSTCERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        connections: _containers.RepeatedScalarFieldContainer[str]
        transportSecurity: bool
        customTrustCertificates: _wrappers_pb2.BytesValue
        def __init__(self, connections: _Optional[_Iterable[str]] = ..., transportSecurity: bool = ..., customTrustCertificates: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...
    GRPC_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    grpc: SequencerConnection.Grpc
    alias: str
    def __init__(self, grpc: _Optional[_Union[SequencerConnection.Grpc, _Mapping]] = ..., alias: _Optional[str] = ...) -> None: ...

class SequencerConnections(_message.Message):
    __slots__ = ("sequencer_connections", "sequencerTrustThreshold", "submission_request_amplification")
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCERTRUSTTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_REQUEST_AMPLIFICATION_FIELD_NUMBER: _ClassVar[int]
    sequencer_connections: _containers.RepeatedCompositeFieldContainer[SequencerConnection]
    sequencerTrustThreshold: int
    submission_request_amplification: SubmissionRequestAmplification
    def __init__(self, sequencer_connections: _Optional[_Iterable[_Union[SequencerConnection, _Mapping]]] = ..., sequencerTrustThreshold: _Optional[int] = ..., submission_request_amplification: _Optional[_Union[SubmissionRequestAmplification, _Mapping]] = ...) -> None: ...

class SubmissionRequestAmplification(_message.Message):
    __slots__ = ("factor", "patience")
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    PATIENCE_FIELD_NUMBER: _ClassVar[int]
    factor: int
    patience: _duration_pb2.Duration
    def __init__(self, factor: _Optional[int] = ..., patience: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
