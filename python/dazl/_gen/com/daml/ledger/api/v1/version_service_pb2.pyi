# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import experimental_features_pb2 as _experimental_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLedgerApiVersionRequest(_message.Message):
    __slots__ = ["ledger_id"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    def __init__(self, ledger_id: _Optional[str] = ...) -> None: ...

class GetLedgerApiVersionResponse(_message.Message):
    __slots__ = ["version", "features"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    version: str
    features: FeaturesDescriptor
    def __init__(self, version: _Optional[str] = ..., features: _Optional[_Union[FeaturesDescriptor, _Mapping]] = ...) -> None: ...

class FeaturesDescriptor(_message.Message):
    __slots__ = ["user_management", "experimental"]
    USER_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_FIELD_NUMBER: _ClassVar[int]
    user_management: UserManagementFeature
    experimental: _experimental_features_pb2.ExperimentalFeatures
    def __init__(self, user_management: _Optional[_Union[UserManagementFeature, _Mapping]] = ..., experimental: _Optional[_Union[_experimental_features_pb2.ExperimentalFeatures, _Mapping]] = ...) -> None: ...

class UserManagementFeature(_message.Message):
    __slots__ = ["supported", "max_rights_per_user", "max_users_page_size"]
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MAX_RIGHTS_PER_USER_FIELD_NUMBER: _ClassVar[int]
    MAX_USERS_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    max_rights_per_user: int
    max_users_page_size: int
    def __init__(self, supported: bool = ..., max_rights_per_user: _Optional[int] = ..., max_users_page_size: _Optional[int] = ...) -> None: ...
