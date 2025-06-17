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
    __slots__ = ("filter", "verbose", "active_at_offset", "event_format")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EVENT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    filter: _transaction_filter_pb2.TransactionFilter
    verbose: bool
    active_at_offset: int
    event_format: _transaction_filter_pb2.EventFormat
    def __init__(self, filter: _Optional[_Union[_transaction_filter_pb2.TransactionFilter, _Mapping]] = ..., verbose: bool = ..., active_at_offset: _Optional[int] = ..., event_format: _Optional[_Union[_transaction_filter_pb2.EventFormat, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("created_event", "synchronizer_id", "reassignment_counter")
    CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    created_event: _event_pb2.CreatedEvent
    synchronizer_id: str
    reassignment_counter: int
    def __init__(self, created_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., synchronizer_id: _Optional[str] = ..., reassignment_counter: _Optional[int] = ...) -> None: ...

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

class GetConnectedSynchronizersRequest(_message.Message):
    __slots__ = ("party", "participant_id")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    participant_id: str
    def __init__(self, party: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class GetConnectedSynchronizersResponse(_message.Message):
    __slots__ = ("connected_synchronizers",)
    class ConnectedSynchronizer(_message.Message):
        __slots__ = ("synchronizer_alias", "synchronizer_id", "permission")
        SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        synchronizer_alias: str
        synchronizer_id: str
        permission: ParticipantPermission
        def __init__(self, synchronizer_alias: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., permission: _Optional[_Union[ParticipantPermission, str]] = ...) -> None: ...
    CONNECTED_SYNCHRONIZERS_FIELD_NUMBER: _ClassVar[int]
    connected_synchronizers: _containers.RepeatedCompositeFieldContainer[GetConnectedSynchronizersResponse.ConnectedSynchronizer]
    def __init__(self, connected_synchronizers: _Optional[_Iterable[_Union[GetConnectedSynchronizersResponse.ConnectedSynchronizer, _Mapping]]] = ...) -> None: ...

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
