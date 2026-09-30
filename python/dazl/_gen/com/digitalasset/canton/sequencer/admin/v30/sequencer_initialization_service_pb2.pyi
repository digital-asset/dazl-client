# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v31 import sequencing_pb2 as _sequencing_pb2_1
from ....protocol.v32 import sequencing_pb2 as _sequencing_pb2_1_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitializeSequencerFromGenesisStateRequest(_message.Message):
    __slots__ = ("topology_snapshot", "v30", "v31", "v32")
    TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    V30_FIELD_NUMBER: _ClassVar[int]
    V31_FIELD_NUMBER: _ClassVar[int]
    V32_FIELD_NUMBER: _ClassVar[int]
    topology_snapshot: bytes
    v30: _sequencing_pb2.StaticSynchronizerParameters
    v31: _sequencing_pb2_1.StaticSynchronizerParameters
    v32: _sequencing_pb2_1_1.StaticSynchronizerParameters
    def __init__(self, topology_snapshot: _Optional[bytes] = ..., v30: _Optional[_Union[_sequencing_pb2.StaticSynchronizerParameters, _Mapping]] = ..., v31: _Optional[_Union[_sequencing_pb2_1.StaticSynchronizerParameters, _Mapping]] = ..., v32: _Optional[_Union[_sequencing_pb2_1_1.StaticSynchronizerParameters, _Mapping]] = ...) -> None: ...

class InitializeSequencerFromGenesisStateResponse(_message.Message):
    __slots__ = ("replicated",)
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    replicated: bool
    def __init__(self, replicated: _Optional[bool] = ...) -> None: ...

class InitializeSequencerFromLsuPredecessorRequest(_message.Message):
    __slots__ = ("topology_snapshot", "v30", "v31", "v32", "ignore_psid_check", "synchronizer_id")
    TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    V30_FIELD_NUMBER: _ClassVar[int]
    V31_FIELD_NUMBER: _ClassVar[int]
    V32_FIELD_NUMBER: _ClassVar[int]
    IGNORE_PSID_CHECK_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    topology_snapshot: bytes
    v30: _sequencing_pb2.StaticSynchronizerParameters
    v31: _sequencing_pb2_1.StaticSynchronizerParameters
    v32: _sequencing_pb2_1_1.StaticSynchronizerParameters
    ignore_psid_check: bool
    synchronizer_id: str
    def __init__(self, topology_snapshot: _Optional[bytes] = ..., v30: _Optional[_Union[_sequencing_pb2.StaticSynchronizerParameters, _Mapping]] = ..., v31: _Optional[_Union[_sequencing_pb2_1.StaticSynchronizerParameters, _Mapping]] = ..., v32: _Optional[_Union[_sequencing_pb2_1_1.StaticSynchronizerParameters, _Mapping]] = ..., ignore_psid_check: _Optional[bool] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...

class InitializeSequencerFromLsuPredecessorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeSequencerFromOnboardingStateRequest(_message.Message):
    __slots__ = ("onboarding_state",)
    ONBOARDING_STATE_FIELD_NUMBER: _ClassVar[int]
    onboarding_state: bytes
    def __init__(self, onboarding_state: _Optional[bytes] = ...) -> None: ...

class InitializeSequencerFromOnboardingStateResponse(_message.Message):
    __slots__ = ("replicated",)
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    replicated: bool
    def __init__(self, replicated: _Optional[bool] = ...) -> None: ...

class InitializeSequencerFromGenesisStateV2Request(_message.Message):
    __slots__ = ("topology_snapshot", "synchronizer_parameters_v30", "synchronizer_parameters_v31", "synchronizer_parameters_v32")
    TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_PARAMETERS_V30_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_PARAMETERS_V31_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_PARAMETERS_V32_FIELD_NUMBER: _ClassVar[int]
    topology_snapshot: bytes
    synchronizer_parameters_v30: _sequencing_pb2.StaticSynchronizerParameters
    synchronizer_parameters_v31: _sequencing_pb2_1.StaticSynchronizerParameters
    synchronizer_parameters_v32: _sequencing_pb2_1_1.StaticSynchronizerParameters
    def __init__(self, topology_snapshot: _Optional[bytes] = ..., synchronizer_parameters_v30: _Optional[_Union[_sequencing_pb2.StaticSynchronizerParameters, _Mapping]] = ..., synchronizer_parameters_v31: _Optional[_Union[_sequencing_pb2_1.StaticSynchronizerParameters, _Mapping]] = ..., synchronizer_parameters_v32: _Optional[_Union[_sequencing_pb2_1_1.StaticSynchronizerParameters, _Mapping]] = ...) -> None: ...

class InitializeSequencerFromGenesisStateV2Response(_message.Message):
    __slots__ = ("replicated",)
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    replicated: bool
    def __init__(self, replicated: _Optional[bool] = ...) -> None: ...

class InitializeSequencerFromOnboardingStateV2Request(_message.Message):
    __slots__ = ("onboarding_state",)
    ONBOARDING_STATE_FIELD_NUMBER: _ClassVar[int]
    onboarding_state: bytes
    def __init__(self, onboarding_state: _Optional[bytes] = ...) -> None: ...

class InitializeSequencerFromOnboardingStateV2Response(_message.Message):
    __slots__ = ("replicated",)
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    replicated: bool
    def __init__(self, replicated: _Optional[bool] = ...) -> None: ...
