# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
