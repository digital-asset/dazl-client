# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionShape(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_SHAPE_UNSPECIFIED: _ClassVar[TransactionShape]
    TRANSACTION_SHAPE_ACS_DELTA: _ClassVar[TransactionShape]
    TRANSACTION_SHAPE_LEDGER_EFFECTS: _ClassVar[TransactionShape]
TRANSACTION_SHAPE_UNSPECIFIED: TransactionShape
TRANSACTION_SHAPE_ACS_DELTA: TransactionShape
TRANSACTION_SHAPE_LEDGER_EFFECTS: TransactionShape

class Filters(_message.Message):
    __slots__ = ("cumulative",)
    CUMULATIVE_FIELD_NUMBER: _ClassVar[int]
    cumulative: _containers.RepeatedCompositeFieldContainer[CumulativeFilter]
    def __init__(self, cumulative: _Optional[_Iterable[_Union[CumulativeFilter, _Mapping]]] = ...) -> None: ...

class CumulativeFilter(_message.Message):
    __slots__ = ("wildcard_filter", "interface_filter", "template_filter")
    WILDCARD_FILTER_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FILTER_FIELD_NUMBER: _ClassVar[int]
    wildcard_filter: WildcardFilter
    interface_filter: InterfaceFilter
    template_filter: TemplateFilter
    def __init__(self, wildcard_filter: _Optional[_Union[WildcardFilter, _Mapping]] = ..., interface_filter: _Optional[_Union[InterfaceFilter, _Mapping]] = ..., template_filter: _Optional[_Union[TemplateFilter, _Mapping]] = ...) -> None: ...

class WildcardFilter(_message.Message):
    __slots__ = ("include_created_event_blob",)
    INCLUDE_CREATED_EVENT_BLOB_FIELD_NUMBER: _ClassVar[int]
    include_created_event_blob: bool
    def __init__(self, include_created_event_blob: bool = ...) -> None: ...

class InterfaceFilter(_message.Message):
    __slots__ = ("interface_id", "include_interface_view", "include_created_event_blob")
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERFACE_VIEW_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CREATED_EVENT_BLOB_FIELD_NUMBER: _ClassVar[int]
    interface_id: _value_pb2.Identifier
    include_interface_view: bool
    include_created_event_blob: bool
    def __init__(self, interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., include_interface_view: bool = ..., include_created_event_blob: bool = ...) -> None: ...

class TemplateFilter(_message.Message):
    __slots__ = ("template_id", "include_created_event_blob")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CREATED_EVENT_BLOB_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    include_created_event_blob: bool
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., include_created_event_blob: bool = ...) -> None: ...

class TransactionFilter(_message.Message):
    __slots__ = ("filters_by_party", "filters_for_any_party")
    class FiltersByPartyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Filters
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Filters, _Mapping]] = ...) -> None: ...
    FILTERS_BY_PARTY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FOR_ANY_PARTY_FIELD_NUMBER: _ClassVar[int]
    filters_by_party: _containers.MessageMap[str, Filters]
    filters_for_any_party: Filters
    def __init__(self, filters_by_party: _Optional[_Mapping[str, Filters]] = ..., filters_for_any_party: _Optional[_Union[Filters, _Mapping]] = ...) -> None: ...

class EventFormat(_message.Message):
    __slots__ = ("filters_by_party", "filters_for_any_party", "verbose")
    class FiltersByPartyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Filters
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Filters, _Mapping]] = ...) -> None: ...
    FILTERS_BY_PARTY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FOR_ANY_PARTY_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    filters_by_party: _containers.MessageMap[str, Filters]
    filters_for_any_party: Filters
    verbose: bool
    def __init__(self, filters_by_party: _Optional[_Mapping[str, Filters]] = ..., filters_for_any_party: _Optional[_Union[Filters, _Mapping]] = ..., verbose: bool = ...) -> None: ...

class TransactionFormat(_message.Message):
    __slots__ = ("event_format", "transaction_shape")
    EVENT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_SHAPE_FIELD_NUMBER: _ClassVar[int]
    event_format: EventFormat
    transaction_shape: TransactionShape
    def __init__(self, event_format: _Optional[_Union[EventFormat, _Mapping]] = ..., transaction_shape: _Optional[_Union[TransactionShape, str]] = ...) -> None: ...

class TopologyFormat(_message.Message):
    __slots__ = ("include_participant_authorization_events",)
    INCLUDE_PARTICIPANT_AUTHORIZATION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    include_participant_authorization_events: ParticipantAuthorizationTopologyFormat
    def __init__(self, include_participant_authorization_events: _Optional[_Union[ParticipantAuthorizationTopologyFormat, _Mapping]] = ...) -> None: ...

class ParticipantAuthorizationTopologyFormat(_message.Message):
    __slots__ = ("parties",)
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parties: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateFormat(_message.Message):
    __slots__ = ("include_transactions", "include_reassignments", "include_topology_events")
    INCLUDE_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TOPOLOGY_EVENTS_FIELD_NUMBER: _ClassVar[int]
    include_transactions: TransactionFormat
    include_reassignments: EventFormat
    include_topology_events: TopologyFormat
    def __init__(self, include_transactions: _Optional[_Union[TransactionFormat, _Mapping]] = ..., include_reassignments: _Optional[_Union[EventFormat, _Mapping]] = ..., include_topology_events: _Optional[_Union[TopologyFormat, _Mapping]] = ...) -> None: ...
