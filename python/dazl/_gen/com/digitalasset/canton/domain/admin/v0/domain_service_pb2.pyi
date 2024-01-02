# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v0 import crypto_pb2 as _crypto_pb2
from ....protocol.v0 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v1 import sequencing_pb2 as _sequencing_pb2_1
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDomainParameters(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = []  # type: ignore
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ["parameters_v0", "parameters_v1"]
        PARAMETERS_V0_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_V1_FIELD_NUMBER: _ClassVar[int]
        parameters_v0: _sequencing_pb2.StaticDomainParameters
        parameters_v1: _sequencing_pb2_1.StaticDomainParameters
        def __init__(self, parameters_v0: _Optional[_Union[_sequencing_pb2.StaticDomainParameters, _Mapping]] = ..., parameters_v1: _Optional[_Union[_sequencing_pb2_1.StaticDomainParameters, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ServiceAgreementAcceptances(_message.Message):
    __slots__ = ["acceptances"]
    ACCEPTANCES_FIELD_NUMBER: _ClassVar[int]
    acceptances: _containers.RepeatedCompositeFieldContainer[ServiceAgreementAcceptance]
    def __init__(self, acceptances: _Optional[_Iterable[_Union[ServiceAgreementAcceptance, _Mapping]]] = ...) -> None: ...

class ServiceAgreementAcceptance(_message.Message):
    __slots__ = ["agreement_id", "participant_id", "signature", "timestamp"]
    AGREEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    agreement_id: str
    participant_id: str
    signature: _crypto_pb2.Signature
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, agreement_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
