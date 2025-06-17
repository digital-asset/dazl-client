# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v30 import topology_pb2 as _topology_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerConnect(_message.Message):
    __slots__ = ()
    class HandshakeRequest(_message.Message):
        __slots__ = ("client_protocol_versions", "minimum_protocol_version")
        CLIENT_PROTOCOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        client_protocol_versions: _containers.RepeatedScalarFieldContainer[int]
        minimum_protocol_version: int
        def __init__(self, client_protocol_versions: _Optional[_Iterable[int]] = ..., minimum_protocol_version: _Optional[int] = ...) -> None: ...
    class HandshakeResponse(_message.Message):
        __slots__ = ("server_protocol_version", "success", "failure")
        class Success(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Failure(_message.Message):
            __slots__ = ("reason",)
            REASON_FIELD_NUMBER: _ClassVar[int]
            reason: str
            def __init__(self, reason: _Optional[str] = ...) -> None: ...
        SERVER_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        server_protocol_version: int
        success: SequencerConnect.HandshakeResponse.Success
        failure: SequencerConnect.HandshakeResponse.Failure
        def __init__(self, server_protocol_version: _Optional[int] = ..., success: _Optional[_Union[SequencerConnect.HandshakeResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SequencerConnect.HandshakeResponse.Failure, _Mapping]] = ...) -> None: ...
    class GetSynchronizerIdRequest(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetSynchronizerIdResponse(_message.Message):
        __slots__ = ("synchronizer_id", "sequencer_uid")
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
        synchronizer_id: str
        sequencer_uid: str
        def __init__(self, synchronizer_id: _Optional[str] = ..., sequencer_uid: _Optional[str] = ...) -> None: ...
    class GetSynchronizerParametersRequest(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetSynchronizerParametersResponse(_message.Message):
        __slots__ = ("parameters_v1",)
        PARAMETERS_V1_FIELD_NUMBER: _ClassVar[int]
        parameters_v1: _sequencing_pb2.StaticSynchronizerParameters
        def __init__(self, parameters_v1: _Optional[_Union[_sequencing_pb2.StaticSynchronizerParameters, _Mapping]] = ...) -> None: ...
    class VerifyActiveRequest(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class VerifyActiveResponse(_message.Message):
        __slots__ = ("success", "failure")
        class Success(_message.Message):
            __slots__ = ("is_active",)
            IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
            is_active: bool
            def __init__(self, is_active: bool = ...) -> None: ...
        class Failure(_message.Message):
            __slots__ = ("reason",)
            REASON_FIELD_NUMBER: _ClassVar[int]
            reason: str
            def __init__(self, reason: _Optional[str] = ...) -> None: ...
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        success: SequencerConnect.VerifyActiveResponse.Success
        failure: SequencerConnect.VerifyActiveResponse.Failure
        def __init__(self, success: _Optional[_Union[SequencerConnect.VerifyActiveResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SequencerConnect.VerifyActiveResponse.Failure, _Mapping]] = ...) -> None: ...
    class RegisterOnboardingTopologyTransactionsRequest(_message.Message):
        __slots__ = ("topology_transactions",)
        TOPOLOGY_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
        topology_transactions: _containers.RepeatedCompositeFieldContainer[_topology_pb2.SignedTopologyTransaction]
        def __init__(self, topology_transactions: _Optional[_Iterable[_Union[_topology_pb2.SignedTopologyTransaction, _Mapping]]] = ...) -> None: ...
    class RegisterOnboardingTopologyTransactionsResponse(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
