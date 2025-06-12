# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from . import reassignment_pb2 as _reassignment_pb2
from . import transaction_filter_pb2 as _transaction_filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTICIPANT_PERMISSION_UNSPECIFIED: _ClassVar[ParticipantPermission]
    PARTICIPANT_PERMISSION_SUBMISSION: _ClassVar[ParticipantPermission]
    PARTICIPANT_PERMISSION_CONFIRMATION: _ClassVar[ParticipantPermission]
    PARTICIPANT_PERMISSION_OBSERVATION: _ClassVar[ParticipantPermission]
PARTICIPANT_PERMISSION_UNSPECIFIED: ParticipantPermission
PARTICIPANT_PERMISSION_SUBMISSION: ParticipantPermission
PARTICIPANT_PERMISSION_CONFIRMATION: ParticipantPermission
PARTICIPANT_PERMISSION_OBSERVATION: ParticipantPermission

class GetActiveContractsRequest(_message.Message):
    __slots__ = ("filter", "verbose", "active_at_offset")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    filter: _transaction_filter_pb2.TransactionFilter
    verbose: bool
    active_at_offset: int
    def __init__(self, filter: _Optional[_Union[_transaction_filter_pb2.TransactionFilter, _Mapping]] = ..., verbose: bool = ..., active_at_offset: _Optional[int] = ...) -> None: ...

class GetActiveContractsResponse(_message.Message):
    __slots__ = ("workflow_id", "active_contract", "incomplete_unassigned", "incomplete_assigned")
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_UNASSIGNED_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    active_contract: ActiveContract
    incomplete_unassigned: IncompleteUnassigned
    incomplete_assigned: IncompleteAssigned
    def __init__(self, workflow_id: _Optional[str] = ..., active_contract: _Optional[_Union[ActiveContract, _Mapping]] = ..., incomplete_unassigned: _Optional[_Union[IncompleteUnassigned, _Mapping]] = ..., incomplete_assigned: _Optional[_Union[IncompleteAssigned, _Mapping]] = ...) -> None: ...

class ActiveContract(_message.Message):
    __slots__ = ("created_event", "domain_id", "reassignment_counter")
    CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    created_event: _event_pb2.CreatedEvent
    domain_id: str
    reassignment_counter: int
    def __init__(self, created_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., domain_id: _Optional[str] = ..., reassignment_counter: _Optional[int] = ...) -> None: ...

class IncompleteUnassigned(_message.Message):
    __slots__ = ("created_event", "unassigned_event")
    CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED_EVENT_FIELD_NUMBER: _ClassVar[int]
    created_event: _event_pb2.CreatedEvent
    unassigned_event: _reassignment_pb2.UnassignedEvent
    def __init__(self, created_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., unassigned_event: _Optional[_Union[_reassignment_pb2.UnassignedEvent, _Mapping]] = ...) -> None: ...

class IncompleteAssigned(_message.Message):
    __slots__ = ("assigned_event",)
    ASSIGNED_EVENT_FIELD_NUMBER: _ClassVar[int]
    assigned_event: _reassignment_pb2.AssignedEvent
    def __init__(self, assigned_event: _Optional[_Union[_reassignment_pb2.AssignedEvent, _Mapping]] = ...) -> None: ...

class GetConnectedDomainsRequest(_message.Message):
    __slots__ = ("party", "participant_id")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    participant_id: str
    def __init__(self, party: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class GetConnectedDomainsResponse(_message.Message):
    __slots__ = ("connected_domains",)
    class ConnectedDomain(_message.Message):
        __slots__ = ("domain_alias", "domain_id", "permission")
        DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        domain_alias: str
        domain_id: str
        permission: ParticipantPermission
        def __init__(self, domain_alias: _Optional[str] = ..., domain_id: _Optional[str] = ..., permission: _Optional[_Union[ParticipantPermission, str]] = ...) -> None: ...
    CONNECTED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    connected_domains: _containers.RepeatedCompositeFieldContainer[GetConnectedDomainsResponse.ConnectedDomain]
    def __init__(self, connected_domains: _Optional[_Iterable[_Union[GetConnectedDomainsResponse.ConnectedDomain, _Mapping]]] = ...) -> None: ...

class GetLedgerEndRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLedgerEndResponse(_message.Message):
    __slots__ = ("offset",)
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: int
    def __init__(self, offset: _Optional[int] = ...) -> None: ...

class GetLatestPrunedOffsetsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLatestPrunedOffsetsResponse(_message.Message):
    __slots__ = ("participant_pruned_up_to_inclusive", "all_divulged_contracts_pruned_up_to_inclusive")
    PARTICIPANT_PRUNED_UP_TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    ALL_DIVULGED_CONTRACTS_PRUNED_UP_TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    participant_pruned_up_to_inclusive: int
    all_divulged_contracts_pruned_up_to_inclusive: int
    def __init__(self, participant_pruned_up_to_inclusive: _Optional[int] = ..., all_divulged_contracts_pruned_up_to_inclusive: _Optional[int] = ...) -> None: ...
