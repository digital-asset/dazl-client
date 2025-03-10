# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreparedTransaction(_message.Message):
    __slots__ = ("transaction", "metadata")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    transaction: DamlTransaction
    metadata: Metadata
    def __init__(self, transaction: _Optional[_Union[DamlTransaction, _Mapping]] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("submitter_info", "submission_seed", "submission_time", "used_packages", "node_seeds", "global_key_mapping", "disclosed_events", "ledger_effective_time", "workflow_id", "interpretation_time_nanos", "domain_id", "mediator_group", "transaction_id")
    class SubmitterInfo(_message.Message):
        __slots__ = ("act_as", "read_as", "command_id")
        ACT_AS_FIELD_NUMBER: _ClassVar[int]
        READ_AS_FIELD_NUMBER: _ClassVar[int]
        COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
        act_as: _containers.RepeatedScalarFieldContainer[str]
        read_as: _containers.RepeatedScalarFieldContainer[str]
        command_id: str
        def __init__(self, act_as: _Optional[_Iterable[str]] = ..., read_as: _Optional[_Iterable[str]] = ..., command_id: _Optional[str] = ...) -> None: ...
    class NodeSeed(_message.Message):
        __slots__ = ("node_id", "seed")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        SEED_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        seed: bytes
        def __init__(self, node_id: _Optional[int] = ..., seed: _Optional[bytes] = ...) -> None: ...
    class GlobalKeyMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: GlobalKey
        value: _value_pb2.Value
        def __init__(self, key: _Optional[_Union[GlobalKey, _Mapping]] = ..., value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...
    class ProcessedDisclosedContract(_message.Message):
        __slots__ = ("contract", "created_at", "driver_metadata")
        CONTRACT_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        DRIVER_METADATA_FIELD_NUMBER: _ClassVar[int]
        contract: Create
        created_at: int
        driver_metadata: bytes
        def __init__(self, contract: _Optional[_Union[Create, _Mapping]] = ..., created_at: _Optional[int] = ..., driver_metadata: _Optional[bytes] = ...) -> None: ...
    SUBMITTER_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_SEED_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_TIME_FIELD_NUMBER: _ClassVar[int]
    USED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NODE_SEEDS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    DISCLOSED_EVENTS_FIELD_NUMBER: _ClassVar[int]
    LEDGER_EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    INTERPRETATION_TIME_NANOS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    submitter_info: Metadata.SubmitterInfo
    submission_seed: bytes
    submission_time: int
    used_packages: _containers.RepeatedScalarFieldContainer[str]
    node_seeds: _containers.RepeatedCompositeFieldContainer[Metadata.NodeSeed]
    global_key_mapping: _containers.RepeatedCompositeFieldContainer[Metadata.GlobalKeyMappingEntry]
    disclosed_events: _containers.RepeatedCompositeFieldContainer[Metadata.ProcessedDisclosedContract]
    ledger_effective_time: int
    workflow_id: str
    interpretation_time_nanos: int
    domain_id: str
    mediator_group: int
    transaction_id: str
    def __init__(self, submitter_info: _Optional[_Union[Metadata.SubmitterInfo, _Mapping]] = ..., submission_seed: _Optional[bytes] = ..., submission_time: _Optional[int] = ..., used_packages: _Optional[_Iterable[str]] = ..., node_seeds: _Optional[_Iterable[_Union[Metadata.NodeSeed, _Mapping]]] = ..., global_key_mapping: _Optional[_Iterable[_Union[Metadata.GlobalKeyMappingEntry, _Mapping]]] = ..., disclosed_events: _Optional[_Iterable[_Union[Metadata.ProcessedDisclosedContract, _Mapping]]] = ..., ledger_effective_time: _Optional[int] = ..., workflow_id: _Optional[str] = ..., interpretation_time_nanos: _Optional[int] = ..., domain_id: _Optional[str] = ..., mediator_group: _Optional[int] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class DamlTransaction(_message.Message):
    __slots__ = ("version", "roots", "nodes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ROOTS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    version: str
    roots: _containers.RepeatedScalarFieldContainer[str]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, version: _Optional[str] = ..., roots: _Optional[_Iterable[str]] = ..., nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("version", "node_id", "create", "fetch", "exercise", "rollback", "lookup_by_key")
    class Fetch(_message.Message):
        __slots__ = ("contract_id", "package_name", "template_id", "signatories", "stakeholders", "acting_parties", "key_with_maintainers", "by_key")
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
        STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
        ACTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
        KEY_WITH_MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        contract_id: str
        package_name: str
        template_id: _value_pb2.Identifier
        signatories: _containers.RepeatedScalarFieldContainer[str]
        stakeholders: _containers.RepeatedScalarFieldContainer[str]
        acting_parties: _containers.RepeatedScalarFieldContainer[str]
        key_with_maintainers: GlobalKeyWithMaintainers
        by_key: bool
        def __init__(self, contract_id: _Optional[str] = ..., package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., signatories: _Optional[_Iterable[str]] = ..., stakeholders: _Optional[_Iterable[str]] = ..., acting_parties: _Optional[_Iterable[str]] = ..., key_with_maintainers: _Optional[_Union[GlobalKeyWithMaintainers, _Mapping]] = ..., by_key: bool = ...) -> None: ...
    class Exercise(_message.Message):
        __slots__ = ("fetch", "interface_id", "choice_id", "chosen_value", "consuming", "children", "exercise_result", "choice_observers", "choice_authorizers")
        FETCH_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        CHOICE_ID_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        CONSUMING_FIELD_NUMBER: _ClassVar[int]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        EXERCISE_RESULT_FIELD_NUMBER: _ClassVar[int]
        CHOICE_OBSERVERS_FIELD_NUMBER: _ClassVar[int]
        CHOICE_AUTHORIZERS_FIELD_NUMBER: _ClassVar[int]
        fetch: Node.Fetch
        interface_id: _value_pb2.Identifier
        choice_id: str
        chosen_value: _value_pb2.Value
        consuming: bool
        children: _containers.RepeatedScalarFieldContainer[str]
        exercise_result: _value_pb2.Value
        choice_observers: _containers.RepeatedScalarFieldContainer[str]
        choice_authorizers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, fetch: _Optional[_Union[Node.Fetch, _Mapping]] = ..., interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., choice_id: _Optional[str] = ..., chosen_value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., consuming: bool = ..., children: _Optional[_Iterable[str]] = ..., exercise_result: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., choice_observers: _Optional[_Iterable[str]] = ..., choice_authorizers: _Optional[_Iterable[str]] = ...) -> None: ...
    class Rollback(_message.Message):
        __slots__ = ("children",)
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        children: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, children: _Optional[_Iterable[str]] = ...) -> None: ...
    class LookupByKey(_message.Message):
        __slots__ = ("package_name", "template_id", "key", "contract_id")
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        package_name: str
        template_id: _value_pb2.Identifier
        key: GlobalKeyWithMaintainers
        contract_id: str
        def __init__(self, package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., key: _Optional[_Union[GlobalKeyWithMaintainers, _Mapping]] = ..., contract_id: _Optional[str] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    version: str
    node_id: str
    create: Create
    fetch: Node.Fetch
    exercise: Node.Exercise
    rollback: Node.Rollback
    lookup_by_key: Node.LookupByKey
    def __init__(self, version: _Optional[str] = ..., node_id: _Optional[str] = ..., create: _Optional[_Union[Create, _Mapping]] = ..., fetch: _Optional[_Union[Node.Fetch, _Mapping]] = ..., exercise: _Optional[_Union[Node.Exercise, _Mapping]] = ..., rollback: _Optional[_Union[Node.Rollback, _Mapping]] = ..., lookup_by_key: _Optional[_Union[Node.LookupByKey, _Mapping]] = ...) -> None: ...

class Create(_message.Message):
    __slots__ = ("contract_id", "package_name", "template_id", "argument", "signatories", "stakeholders", "package_version", "global_key_with_maintainers")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_KEY_WITH_MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    package_name: str
    template_id: _value_pb2.Identifier
    argument: _value_pb2.Value
    signatories: _containers.RepeatedScalarFieldContainer[str]
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    package_version: str
    global_key_with_maintainers: GlobalKeyWithMaintainers
    def __init__(self, contract_id: _Optional[str] = ..., package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., argument: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., signatories: _Optional[_Iterable[str]] = ..., stakeholders: _Optional[_Iterable[str]] = ..., package_version: _Optional[str] = ..., global_key_with_maintainers: _Optional[_Union[GlobalKeyWithMaintainers, _Mapping]] = ...) -> None: ...

class GlobalKey(_message.Message):
    __slots__ = ("template_id", "package_name", "key", "hash")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    package_name: str
    key: _value_pb2.Value
    hash: bytes
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., package_name: _Optional[str] = ..., key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., hash: _Optional[bytes] = ...) -> None: ...

class GlobalKeyWithMaintainers(_message.Message):
    __slots__ = ("key", "maintainers")
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
    key: GlobalKey
    maintainers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[_Union[GlobalKey, _Mapping]] = ..., maintainers: _Optional[_Iterable[str]] = ...) -> None: ...
