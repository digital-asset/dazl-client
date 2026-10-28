# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import sequencer_initialization_snapshot_pb2 as _sequencer_initialization_snapshot_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnboardingStateForSequencerV2(_message.Message):
    __slots__ = ("topology_transaction", "static_synchronizer_parameters", "sequencer_snapshot")
    TOPOLOGY_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    STATIC_SYNCHRONIZER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    topology_transaction: bytes
    static_synchronizer_parameters: bytes
    sequencer_snapshot: _sequencer_initialization_snapshot_pb2.SequencerSnapshot
    def __init__(self, topology_transaction: _Optional[bytes] = ..., static_synchronizer_parameters: _Optional[bytes] = ..., sequencer_snapshot: _Optional[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot, _Mapping]] = ...) -> None: ...
