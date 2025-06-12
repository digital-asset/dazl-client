# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v2 import topology_pb2 as _topology_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyTransaction(_message.Message):
    __slots__ = ("state_update", "domain_governance")
    STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_GOVERNANCE_FIELD_NUMBER: _ClassVar[int]
    state_update: _topology_pb2.TopologyStateUpdate
    domain_governance: _topology_pb2.DomainGovernanceTransaction
    def __init__(self, state_update: _Optional[_Union[_topology_pb2.TopologyStateUpdate, _Mapping]] = ..., domain_governance: _Optional[_Union[_topology_pb2.DomainGovernanceTransaction, _Mapping]] = ...) -> None: ...
