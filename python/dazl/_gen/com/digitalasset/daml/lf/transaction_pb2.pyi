# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Transaction(_message.Message):
    __slots__ = ("version", "roots", "nodes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ROOTS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    version: str
    roots: _containers.RepeatedScalarFieldContainer[str]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, version: _Optional[str] = ..., roots: _Optional[_Iterable[str]] = ..., nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class ThinContractInstance(_message.Message):
    __slots__ = ("package_name", "template_id", "arg_versioned", "agreement")
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ARG_VERSIONED_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    package_name: str
    template_id: _value_pb2.Identifier
    arg_versioned: _value_pb2.VersionedValue
    agreement: str
    def __init__(self, package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., arg_versioned: _Optional[_Union[_value_pb2.VersionedValue, _Mapping]] = ..., agreement: _Optional[str] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("version", "node_id", "create", "fetch", "exercise", "rollback", "query_by_key")
    class Fetch(_message.Message):
        __slots__ = ("contract_id", "package_name", "template_id", "interface_id", "non_maintainer_signatories", "non_signatory_stakeholders", "actors", "key_with_maintainers", "by_key")
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        NON_MAINTAINER_SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
        NON_SIGNATORY_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        KEY_WITH_MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        contract_id: bytes
        package_name: str
        template_id: _value_pb2.Identifier
        interface_id: _value_pb2.Identifier
        non_maintainer_signatories: _containers.RepeatedScalarFieldContainer[str]
        non_signatory_stakeholders: _containers.RepeatedScalarFieldContainer[str]
        actors: _containers.RepeatedScalarFieldContainer[str]
        key_with_maintainers: KeyWithMaintainers
        by_key: bool
        def __init__(self, contract_id: _Optional[bytes] = ..., package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., non_maintainer_signatories: _Optional[_Iterable[str]] = ..., non_signatory_stakeholders: _Optional[_Iterable[str]] = ..., actors: _Optional[_Iterable[str]] = ..., key_with_maintainers: _Optional[_Union[KeyWithMaintainers, _Mapping]] = ..., by_key: bool = ...) -> None: ...
    class Exercise(_message.Message):
        __slots__ = ("fetch", "interface_id", "choice", "arg", "consuming", "children", "result", "observers", "authorizers")
        FETCH_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        CHOICE_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        CONSUMING_FIELD_NUMBER: _ClassVar[int]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        OBSERVERS_FIELD_NUMBER: _ClassVar[int]
        AUTHORIZERS_FIELD_NUMBER: _ClassVar[int]
        fetch: Node.Fetch
        interface_id: _value_pb2.Identifier
        choice: str
        arg: bytes
        consuming: bool
        children: _containers.RepeatedScalarFieldContainer[str]
        result: bytes
        observers: _containers.RepeatedScalarFieldContainer[str]
        authorizers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, fetch: _Optional[_Union[Node.Fetch, _Mapping]] = ..., interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., choice: _Optional[str] = ..., arg: _Optional[bytes] = ..., consuming: bool = ..., children: _Optional[_Iterable[str]] = ..., result: _Optional[bytes] = ..., observers: _Optional[_Iterable[str]] = ..., authorizers: _Optional[_Iterable[str]] = ...) -> None: ...
    class Rollback(_message.Message):
        __slots__ = ("children",)
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        children: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, children: _Optional[_Iterable[str]] = ...) -> None: ...
    class QueryByKey(_message.Message):
        __slots__ = ("package_name", "template_id", "key_with_maintainers", "contract_id", "exaustive")
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_WITH_MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        EXAUSTIVE_FIELD_NUMBER: _ClassVar[int]
        package_name: str
        template_id: _value_pb2.Identifier
        key_with_maintainers: KeyWithMaintainers
        contract_id: _containers.RepeatedScalarFieldContainer[bytes]
        exaustive: bool
        def __init__(self, package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., key_with_maintainers: _Optional[_Union[KeyWithMaintainers, _Mapping]] = ..., contract_id: _Optional[_Iterable[bytes]] = ..., exaustive: bool = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_FIELD_NUMBER: _ClassVar[int]
    QUERY_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    version: str
    node_id: str
    create: FatContractInstance
    fetch: Node.Fetch
    exercise: Node.Exercise
    rollback: Node.Rollback
    query_by_key: Node.QueryByKey
    def __init__(self, version: _Optional[str] = ..., node_id: _Optional[str] = ..., create: _Optional[_Union[FatContractInstance, _Mapping]] = ..., fetch: _Optional[_Union[Node.Fetch, _Mapping]] = ..., exercise: _Optional[_Union[Node.Exercise, _Mapping]] = ..., rollback: _Optional[_Union[Node.Rollback, _Mapping]] = ..., query_by_key: _Optional[_Union[Node.QueryByKey, _Mapping]] = ...) -> None: ...

class Versioned(_message.Message):
    __slots__ = ("version", "payload")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    version: str
    payload: bytes
    def __init__(self, version: _Optional[str] = ..., payload: _Optional[bytes] = ...) -> None: ...

class FatContractInstance(_message.Message):
    __slots__ = ("contract_id", "package_name", "package_version", "template_id", "create_arg", "non_maintainer_signatories", "non_signatory_stakeholders", "created_at", "authentication_data", "contract_key_with_maintainers")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARG_FIELD_NUMBER: _ClassVar[int]
    NON_MAINTAINER_SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    NON_SIGNATORY_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_DATA_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_KEY_WITH_MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
    contract_id: bytes
    package_name: str
    package_version: _containers.RepeatedScalarFieldContainer[int]
    template_id: _value_pb2.Identifier
    create_arg: bytes
    non_maintainer_signatories: _containers.RepeatedScalarFieldContainer[str]
    non_signatory_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    created_at: int
    authentication_data: bytes
    contract_key_with_maintainers: KeyWithMaintainers
    def __init__(self, contract_id: _Optional[bytes] = ..., package_name: _Optional[str] = ..., package_version: _Optional[_Iterable[int]] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., create_arg: _Optional[bytes] = ..., non_maintainer_signatories: _Optional[_Iterable[str]] = ..., non_signatory_stakeholders: _Optional[_Iterable[str]] = ..., created_at: _Optional[int] = ..., authentication_data: _Optional[bytes] = ..., contract_key_with_maintainers: _Optional[_Union[KeyWithMaintainers, _Mapping]] = ...) -> None: ...

class KeyWithMaintainers(_message.Message):
    __slots__ = ("key", "maintainers", "hash")
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    maintainers: _containers.RepeatedScalarFieldContainer[str]
    hash: bytes
    def __init__(self, key: _Optional[bytes] = ..., maintainers: _Optional[_Iterable[str]] = ..., hash: _Optional[bytes] = ...) -> None: ...
