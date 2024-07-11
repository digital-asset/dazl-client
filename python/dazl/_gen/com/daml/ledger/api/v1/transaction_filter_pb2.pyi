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

class TransactionFilter(_message.Message):
    __slots__ = ["filters_by_party"]
    class FiltersByPartyEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Filters
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Filters, _Mapping]] = ...) -> None: ...
    FILTERS_BY_PARTY_FIELD_NUMBER: _ClassVar[int]
    filters_by_party: _containers.MessageMap[str, Filters]
    def __init__(self, filters_by_party: _Optional[_Mapping[str, Filters]] = ...) -> None: ...

class Filters(_message.Message):
    __slots__ = ["inclusive"]
    INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    inclusive: InclusiveFilters
    def __init__(self, inclusive: _Optional[_Union[InclusiveFilters, _Mapping]] = ...) -> None: ...

class InclusiveFilters(_message.Message):
    __slots__ = ["template_ids", "interface_filters"]
    TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    template_ids: _containers.RepeatedCompositeFieldContainer[_value_pb2.Identifier]
    interface_filters: _containers.RepeatedCompositeFieldContainer[InterfaceFilter]
    def __init__(self, template_ids: _Optional[_Iterable[_Union[_value_pb2.Identifier, _Mapping]]] = ..., interface_filters: _Optional[_Iterable[_Union[InterfaceFilter, _Mapping]]] = ...) -> None: ...

class InterfaceFilter(_message.Message):
    __slots__ = ["interface_id", "include_interface_view", "include_create_arguments_blob"]
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERFACE_VIEW_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CREATE_ARGUMENTS_BLOB_FIELD_NUMBER: _ClassVar[int]
    interface_id: _value_pb2.Identifier
    include_interface_view: bool
    include_create_arguments_blob: bool
    def __init__(self, interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., include_interface_view: bool = ..., include_create_arguments_blob: bool = ...) -> None: ...
