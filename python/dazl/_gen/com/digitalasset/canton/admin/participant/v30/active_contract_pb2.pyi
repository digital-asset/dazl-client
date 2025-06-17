# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActiveContractOld(_message.Message):
    __slots__ = ("synchronizer_id", "contract", "reassignment_counter")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    contract: Contract
    reassignment_counter: int
    def __init__(self, synchronizer_id: _Optional[str] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., reassignment_counter: _Optional[int] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ("contract_id", "raw_contract_instance", "metadata", "ledger_create_time", "contract_salt")
    class Metadata(_message.Message):
        __slots__ = ("non_maintainer_signatories", "non_signatory_stakeholders", "key", "maintainers")
        NON_MAINTAINER_SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
        NON_SIGNATORY_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        non_maintainer_signatories: _containers.RepeatedScalarFieldContainer[str]
        non_signatory_stakeholders: _containers.RepeatedScalarFieldContainer[str]
        key: Contract.GlobalKey
        maintainers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, non_maintainer_signatories: _Optional[_Iterable[str]] = ..., non_signatory_stakeholders: _Optional[_Iterable[str]] = ..., key: _Optional[_Union[Contract.GlobalKey, _Mapping]] = ..., maintainers: _Optional[_Iterable[str]] = ...) -> None: ...
    class GlobalKey(_message.Message):
        __slots__ = ("template_id", "key", "package_name")
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        template_id: bytes
        key: bytes
        package_name: str
        def __init__(self, template_id: _Optional[bytes] = ..., key: _Optional[bytes] = ..., package_name: _Optional[str] = ...) -> None: ...
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_CONTRACT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LEDGER_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SALT_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    raw_contract_instance: bytes
    metadata: Contract.Metadata
    ledger_create_time: _timestamp_pb2.Timestamp
    contract_salt: _crypto_pb2.Salt
    def __init__(self, contract_id: _Optional[str] = ..., raw_contract_instance: _Optional[bytes] = ..., metadata: _Optional[_Union[Contract.Metadata, _Mapping]] = ..., ledger_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., contract_salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ...) -> None: ...

class ActiveContract(_message.Message):
    __slots__ = ("active_contract",)
    ACTIVE_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    active_contract: bytes
    def __init__(self, active_contract: _Optional[bytes] = ...) -> None: ...
