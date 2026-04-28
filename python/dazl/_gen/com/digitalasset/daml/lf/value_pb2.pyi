# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionedValue(_message.Message):
    __slots__ = ("version", "value")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    version: str
    value: bytes
    def __init__(self, version: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class Identifier(_message.Message):
    __slots__ = ("package_id", "module_name", "name")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    module_name: _containers.RepeatedScalarFieldContainer[str]
    name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, package_id: _Optional[str] = ..., module_name: _Optional[_Iterable[str]] = ..., name: _Optional[_Iterable[str]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ("unit", "bool", "int64", "date", "timestamp", "numeric", "party", "text", "contract_id", "optional", "list", "map", "text_map", "record", "variant", "enum")
    class Record(_message.Message):
        __slots__ = ("fields",)
        class Field(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: Value
            def __init__(self, value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedCompositeFieldContainer[Value.Record.Field]
        def __init__(self, fields: _Optional[_Iterable[_Union[Value.Record.Field, _Mapping]]] = ...) -> None: ...
    class Variant(_message.Message):
        __slots__ = ("constructor", "value")
        CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        constructor: str
        value: Value
        def __init__(self, constructor: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    class Enum(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class List(_message.Message):
        __slots__ = ("elements",)
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[Value]
        def __init__(self, elements: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...
    class Optional(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: Value
        def __init__(self, value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    class TextMap(_message.Message):
        __slots__ = ("entries",)
        class Entry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[Value.TextMap.Entry]
        def __init__(self, entries: _Optional[_Iterable[_Union[Value.TextMap.Entry, _Mapping]]] = ...) -> None: ...
    class Map(_message.Message):
        __slots__ = ("entries",)
        class Entry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: Value
            value: Value
            def __init__(self, key: _Optional[_Union[Value, _Mapping]] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[Value.Map.Entry]
        def __init__(self, entries: _Optional[_Iterable[_Union[Value.Map.Entry, _Mapping]]] = ...) -> None: ...
    UNIT_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    TEXT_MAP_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    unit: _empty_pb2.Empty
    bool: bool  # type: ignore
    int64: int
    date: int
    timestamp: int
    numeric: str
    party: str
    text: str
    contract_id: bytes
    optional: Value.Optional
    list: Value.List
    map: Value.Map
    text_map: Value.TextMap
    record: Value.Record
    variant: Value.Variant
    enum: Value.Enum
    def __init__(self, unit: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., bool: bool = ..., int64: _Optional[int] = ..., date: _Optional[int] = ..., timestamp: _Optional[int] = ..., numeric: _Optional[str] = ..., party: _Optional[str] = ..., text: _Optional[str] = ..., contract_id: _Optional[bytes] = ..., optional: _Optional[_Union[Value.Optional, _Mapping]] = ..., list: _Optional[_Union[Value.List, _Mapping]] = ..., map: _Optional[_Union[Value.Map, _Mapping]] = ..., text_map: _Optional[_Union[Value.TextMap, _Mapping]] = ..., record: _Optional[_Union[Value.Record, _Mapping]] = ..., variant: _Optional[_Union[Value.Variant, _Mapping]] = ..., enum: _Optional[_Union[Value.Enum, _Mapping]] = ...) -> None: ...  # type: ignore
