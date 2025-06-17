# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIEW_TYPE_UNSPECIFIED: _ClassVar[ViewType]
    VIEW_TYPE_TRANSACTION: _ClassVar[ViewType]
    VIEW_TYPE_UNASSIGNMENT: _ClassVar[ViewType]
    VIEW_TYPE_ASSIGNMENT: _ClassVar[ViewType]
VIEW_TYPE_UNSPECIFIED: ViewType
VIEW_TYPE_TRANSACTION: ViewType
VIEW_TYPE_UNASSIGNMENT: ViewType
VIEW_TYPE_ASSIGNMENT: ViewType

class DriverContractMetadata(_message.Message):
    __slots__ = ("contract_salt",)
    CONTRACT_SALT_FIELD_NUMBER: _ClassVar[int]
    contract_salt: _crypto_pb2.Salt
    def __init__(self, contract_salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ...) -> None: ...
