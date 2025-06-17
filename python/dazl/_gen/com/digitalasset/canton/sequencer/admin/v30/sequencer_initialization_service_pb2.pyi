# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import sequencing_pb2 as _sequencing_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitializeSequencerFromGenesisStateRequest(_message.Message):
    __slots__ = ("topology_snapshot", "synchronizer_parameters")
    TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    topology_snapshot: bytes
    synchronizer_parameters: _sequencing_pb2.StaticSynchronizerParameters
    def __init__(self, topology_snapshot: _Optional[bytes] = ..., synchronizer_parameters: _Optional[_Union[_sequencing_pb2.StaticSynchronizerParameters, _Mapping]] = ...) -> None: ...

class InitializeSequencerFromGenesisStateResponse(_message.Message):
    __slots__ = ("replicated",)
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    replicated: bool
    def __init__(self, replicated: bool = ...) -> None: ...

class InitializeSequencerFromOnboardingStateRequest(_message.Message):
    __slots__ = ("onboarding_state",)
    ONBOARDING_STATE_FIELD_NUMBER: _ClassVar[int]
    onboarding_state: bytes
    def __init__(self, onboarding_state: _Optional[bytes] = ...) -> None: ...

class InitializeSequencerFromOnboardingStateResponse(_message.Message):
    __slots__ = ("replicated",)
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    replicated: bool
    def __init__(self, replicated: bool = ...) -> None: ...
