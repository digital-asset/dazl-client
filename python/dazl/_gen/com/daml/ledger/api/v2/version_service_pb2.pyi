# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import experimental_features_pb2 as _experimental_features_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLedgerApiVersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLedgerApiVersionResponse(_message.Message):
    __slots__ = ("version", "features")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    version: str
    features: FeaturesDescriptor
    def __init__(self, version: _Optional[str] = ..., features: _Optional[_Union[FeaturesDescriptor, _Mapping]] = ...) -> None: ...

class FeaturesDescriptor(_message.Message):
    __slots__ = ("experimental", "user_management", "party_management", "offset_checkpoint")
    EXPERIMENTAL_FIELD_NUMBER: _ClassVar[int]
    USER_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    PARTY_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    experimental: _experimental_features_pb2.ExperimentalFeatures
    user_management: UserManagementFeature
    party_management: PartyManagementFeature
    offset_checkpoint: OffsetCheckpointFeature
    def __init__(self, experimental: _Optional[_Union[_experimental_features_pb2.ExperimentalFeatures, _Mapping]] = ..., user_management: _Optional[_Union[UserManagementFeature, _Mapping]] = ..., party_management: _Optional[_Union[PartyManagementFeature, _Mapping]] = ..., offset_checkpoint: _Optional[_Union[OffsetCheckpointFeature, _Mapping]] = ...) -> None: ...

class UserManagementFeature(_message.Message):
    __slots__ = ("supported", "max_rights_per_user", "max_users_page_size")
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MAX_RIGHTS_PER_USER_FIELD_NUMBER: _ClassVar[int]
    MAX_USERS_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    max_rights_per_user: int
    max_users_page_size: int
    def __init__(self, supported: bool = ..., max_rights_per_user: _Optional[int] = ..., max_users_page_size: _Optional[int] = ...) -> None: ...

class PartyManagementFeature(_message.Message):
    __slots__ = ("max_parties_page_size",)
    MAX_PARTIES_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    max_parties_page_size: int
    def __init__(self, max_parties_page_size: _Optional[int] = ...) -> None: ...

class OffsetCheckpointFeature(_message.Message):
    __slots__ = ("max_offset_checkpoint_emission_delay",)
    MAX_OFFSET_CHECKPOINT_EMISSION_DELAY_FIELD_NUMBER: _ClassVar[int]
    max_offset_checkpoint_emission_delay: _duration_pb2.Duration
    def __init__(self, max_offset_checkpoint_emission_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
