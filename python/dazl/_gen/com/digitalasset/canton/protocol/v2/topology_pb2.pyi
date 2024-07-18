# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v1 import topology_pb2 as _topology_pb2
from . import domain_params_pb2 as _domain_params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainParametersChange(_message.Message):
    __slots__ = ("domain", "domain_parameters")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    domain_parameters: _domain_params_pb2.DynamicDomainParameters
    def __init__(self, domain: _Optional[str] = ..., domain_parameters: _Optional[_Union[_domain_params_pb2.DynamicDomainParameters, _Mapping]] = ...) -> None: ...

class DomainGovernanceTransaction(_message.Message):
    __slots__ = ("domain_parameters_change",)
    DOMAIN_PARAMETERS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    domain_parameters_change: DomainParametersChange
    def __init__(self, domain_parameters_change: _Optional[_Union[DomainParametersChange, _Mapping]] = ...) -> None: ...

class TopologyTransaction(_message.Message):
    __slots__ = ("state_update", "domain_governance")
    STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_GOVERNANCE_FIELD_NUMBER: _ClassVar[int]
    state_update: _topology_pb2.TopologyStateUpdate
    domain_governance: DomainGovernanceTransaction
    def __init__(self, state_update: _Optional[_Union[_topology_pb2.TopologyStateUpdate, _Mapping]] = ..., domain_governance: _Optional[_Union[DomainGovernanceTransaction, _Mapping]] = ...) -> None: ...
