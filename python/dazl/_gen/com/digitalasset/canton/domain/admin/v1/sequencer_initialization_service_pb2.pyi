# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v0 import sequencer_initialization_snapshot_pb2 as _sequencer_initialization_snapshot_pb2
from ....protocol.v1 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v0 import topology_ext_pb2 as _topology_ext_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitRequest(_message.Message):
    __slots__ = ["domain_id", "topology_snapshot", "domain_parameters", "snapshot"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    topology_snapshot: _topology_ext_pb2.TopologyTransactions
    domain_parameters: _sequencing_pb2.StaticDomainParameters
    snapshot: _sequencer_initialization_snapshot_pb2.SequencerSnapshot
    def __init__(self, domain_id: _Optional[str] = ..., topology_snapshot: _Optional[_Union[_topology_ext_pb2.TopologyTransactions, _Mapping]] = ..., domain_parameters: _Optional[_Union[_sequencing_pb2.StaticDomainParameters, _Mapping]] = ..., snapshot: _Optional[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot, _Mapping]] = ...) -> None: ...
