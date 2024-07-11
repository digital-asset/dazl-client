# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Value(_message.Message):
    __slots__ = ["record", "variant", "contract_id", "list", "int64", "numeric", "text", "timestamp", "party", "bool", "unit", "date", "optional", "map", "enum", "gen_map"]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    GEN_MAP_FIELD_NUMBER: _ClassVar[int]
    record: Record
    variant: Variant
    contract_id: str
    list: List
    int64: int
    numeric: str
    text: str
    timestamp: int
    party: str
    bool: bool  # type: ignore
    unit: _empty_pb2.Empty
    date: int
    optional: Optional
    map: Map
    enum: Enum
    gen_map: GenMap
    def __init__(self, record: _Optional[_Union[Record, _Mapping]] = ..., variant: _Optional[_Union[Variant, _Mapping]] = ..., contract_id: _Optional[str] = ..., list: _Optional[_Union[List, _Mapping]] = ..., int64: _Optional[int] = ..., numeric: _Optional[str] = ..., text: _Optional[str] = ..., timestamp: _Optional[int] = ..., party: _Optional[str] = ..., bool: bool = ..., unit: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., date: _Optional[int] = ..., optional: _Optional[_Union[Optional, _Mapping]] = ..., map: _Optional[_Union[Map, _Mapping]] = ..., enum: _Optional[_Union[Enum, _Mapping]] = ..., gen_map: _Optional[_Union[GenMap, _Mapping]] = ...) -> None: ...  # type: ignore

class Record(_message.Message):
    __slots__ = ["record_id", "fields"]
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    record_id: Identifier
    fields: _containers.RepeatedCompositeFieldContainer[RecordField]
    def __init__(self, record_id: _Optional[_Union[Identifier, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[RecordField, _Mapping]]] = ...) -> None: ...

class RecordField(_message.Message):
    __slots__ = ["label", "value"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: Value
    def __init__(self, label: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...

class Identifier(_message.Message):
    __slots__ = ["package_id", "module_name", "entity_name"]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    module_name: str
    entity_name: str
    def __init__(self, package_id: _Optional[str] = ..., module_name: _Optional[str] = ..., entity_name: _Optional[str] = ...) -> None: ...

class Variant(_message.Message):
    __slots__ = ["variant_id", "constructor", "value"]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    variant_id: Identifier
    constructor: str
    value: Value
    def __init__(self, variant_id: _Optional[_Union[Identifier, _Mapping]] = ..., constructor: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...

class Enum(_message.Message):
    __slots__ = ["enum_id", "constructor"]
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    enum_id: Identifier
    constructor: str
    def __init__(self, enum_id: _Optional[_Union[Identifier, _Mapping]] = ..., constructor: _Optional[str] = ...) -> None: ...

class List(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, elements: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class Optional(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: Value
    def __init__(self, value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...

class Map(_message.Message):
    __slots__ = ["entries"]
    class Entry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[Map.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[Map.Entry, _Mapping]]] = ...) -> None: ...

class GenMap(_message.Message):
    __slots__ = ["entries"]
    class Entry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: Value
        value: Value
        def __init__(self, key: _Optional[_Union[Value, _Mapping]] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[GenMap.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[GenMap.Entry, _Mapping]]] = ...) -> None: ...
