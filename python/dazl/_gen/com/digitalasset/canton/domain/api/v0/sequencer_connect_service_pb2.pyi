# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import service_agreement_pb2 as _service_agreement_pb2
from ....protocol.v0 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v1 import sequencing_pb2 as _sequencing_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerConnect(_message.Message):
    __slots__ = []  # type: ignore
    class GetDomainId(_message.Message):
        __slots__ = []  # type: ignore
        class Request(_message.Message):
            __slots__ = []  # type: ignore
            def __init__(self) -> None: ...
        class Response(_message.Message):
            __slots__ = ["domain_id", "sequencer_id"]
            DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
            SEQUENCER_ID_FIELD_NUMBER: _ClassVar[int]
            domain_id: str
            sequencer_id: str
            def __init__(self, domain_id: _Optional[str] = ..., sequencer_id: _Optional[str] = ...) -> None: ...
        def __init__(self) -> None: ...
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
    class VerifyActive(_message.Message):
        __slots__ = []  # type: ignore
        class Request(_message.Message):
            __slots__ = []  # type: ignore
            def __init__(self) -> None: ...
        class Response(_message.Message):
            __slots__ = ["success", "failure"]
            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            FAILURE_FIELD_NUMBER: _ClassVar[int]
            success: SequencerConnect.VerifyActive.Success
            failure: SequencerConnect.VerifyActive.Failure
            def __init__(self, success: _Optional[_Union[SequencerConnect.VerifyActive.Success, _Mapping]] = ..., failure: _Optional[_Union[SequencerConnect.VerifyActive.Failure, _Mapping]] = ...) -> None: ...
        class Success(_message.Message):
            __slots__ = ["is_active"]
            IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
            is_active: bool
            def __init__(self, is_active: bool = ...) -> None: ...
        class Failure(_message.Message):
            __slots__ = ["reason"]
            REASON_FIELD_NUMBER: _ClassVar[int]
            reason: str
            def __init__(self, reason: _Optional[str] = ...) -> None: ...
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...
