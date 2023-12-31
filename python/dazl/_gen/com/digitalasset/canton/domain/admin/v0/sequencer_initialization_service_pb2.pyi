# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v0 import crypto_pb2 as _crypto_pb2
from . import sequencer_initialization_snapshot_pb2 as _sequencer_initialization_snapshot_pb2
from ..v1 import sequencer_initialization_service_pb2 as _sequencer_initialization_service_pb2
from ..v2 import sequencer_initialization_service_pb2 as _sequencer_initialization_service_pb2_1
from ....protocol.v0 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v0 import topology_ext_pb2 as _topology_ext_pb2
from google.protobuf import empty_pb2 as _empty_pb2
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

class InitResponse(_message.Message):
    __slots__ = ["key_id", "public_key", "replicated"]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    public_key: _crypto_pb2.SigningPublicKey
    replicated: bool
    def __init__(self, key_id: _Optional[str] = ..., public_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ..., replicated: bool = ...) -> None: ...

class TopologyBootstrapRequest(_message.Message):
    __slots__ = ["initial_topology_snapshot"]
    INITIAL_TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    initial_topology_snapshot: _topology_ext_pb2.TopologyTransactions
    def __init__(self, initial_topology_snapshot: _Optional[_Union[_topology_ext_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...
