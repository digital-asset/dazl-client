# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SerializableContract(_message.Message):
    __slots__ = ("contract_id", "raw_contract_instance", "metadata", "ledger_create_time", "authentication_data")
    class Metadata(_message.Message):
        __slots__ = ("non_maintainer_signatories", "non_signatory_stakeholders", "key", "maintainers")
        NON_MAINTAINER_SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
        NON_SIGNATORY_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        non_maintainer_signatories: _containers.RepeatedScalarFieldContainer[str]
        non_signatory_stakeholders: _containers.RepeatedScalarFieldContainer[str]
        key: GlobalKey
        maintainers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, non_maintainer_signatories: _Optional[_Iterable[str]] = ..., non_signatory_stakeholders: _Optional[_Iterable[str]] = ..., key: _Optional[_Union[GlobalKey, _Mapping]] = ..., maintainers: _Optional[_Iterable[str]] = ...) -> None: ...
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_CONTRACT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LEDGER_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_DATA_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    raw_contract_instance: bytes
    metadata: SerializableContract.Metadata
    ledger_create_time: int
    authentication_data: bytes
    def __init__(self, contract_id: _Optional[str] = ..., raw_contract_instance: _Optional[bytes] = ..., metadata: _Optional[_Union[SerializableContract.Metadata, _Mapping]] = ..., ledger_create_time: _Optional[int] = ..., authentication_data: _Optional[bytes] = ...) -> None: ...

class GlobalKey(_message.Message):
    __slots__ = ("template_id", "key", "package_name", "hash")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    template_id: bytes
    key: bytes
    package_name: str
    hash: bytes
    def __init__(self, template_id: _Optional[bytes] = ..., key: _Optional[bytes] = ..., package_name: _Optional[str] = ..., hash: _Optional[bytes] = ...) -> None: ...
