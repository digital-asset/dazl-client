# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityProviderConfig(_message.Message):
    __slots__ = ["identity_provider_id", "is_deactivated", "issuer", "jwks_url", "audience"]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    JWKS_URL_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    identity_provider_id: str
    is_deactivated: bool
    issuer: str
    jwks_url: str
    audience: str
    def __init__(self, identity_provider_id: _Optional[str] = ..., is_deactivated: bool = ..., issuer: _Optional[str] = ..., jwks_url: _Optional[str] = ..., audience: _Optional[str] = ...) -> None: ...

class CreateIdentityProviderConfigRequest(_message.Message):
    __slots__ = ["identity_provider_config"]
    IDENTITY_PROVIDER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    identity_provider_config: IdentityProviderConfig
    def __init__(self, identity_provider_config: _Optional[_Union[IdentityProviderConfig, _Mapping]] = ...) -> None: ...

class CreateIdentityProviderConfigResponse(_message.Message):
    __slots__ = ["identity_provider_config"]
    IDENTITY_PROVIDER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    identity_provider_config: IdentityProviderConfig
    def __init__(self, identity_provider_config: _Optional[_Union[IdentityProviderConfig, _Mapping]] = ...) -> None: ...

class GetIdentityProviderConfigRequest(_message.Message):
    __slots__ = ["identity_provider_id"]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    identity_provider_id: str
    def __init__(self, identity_provider_id: _Optional[str] = ...) -> None: ...

class GetIdentityProviderConfigResponse(_message.Message):
    __slots__ = ["identity_provider_config"]
    IDENTITY_PROVIDER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    identity_provider_config: IdentityProviderConfig
    def __init__(self, identity_provider_config: _Optional[_Union[IdentityProviderConfig, _Mapping]] = ...) -> None: ...

class ListIdentityProviderConfigsRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListIdentityProviderConfigsResponse(_message.Message):
    __slots__ = ["identity_provider_configs"]
    IDENTITY_PROVIDER_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    identity_provider_configs: _containers.RepeatedCompositeFieldContainer[IdentityProviderConfig]
    def __init__(self, identity_provider_configs: _Optional[_Iterable[_Union[IdentityProviderConfig, _Mapping]]] = ...) -> None: ...

class UpdateIdentityProviderConfigRequest(_message.Message):
    __slots__ = ["identity_provider_config", "update_mask"]
    IDENTITY_PROVIDER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    identity_provider_config: IdentityProviderConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, identity_provider_config: _Optional[_Union[IdentityProviderConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateIdentityProviderConfigResponse(_message.Message):
    __slots__ = ["identity_provider_config"]
    IDENTITY_PROVIDER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    identity_provider_config: IdentityProviderConfig
    def __init__(self, identity_provider_config: _Optional[_Union[IdentityProviderConfig, _Mapping]] = ...) -> None: ...

class DeleteIdentityProviderConfigRequest(_message.Message):
    __slots__ = ["identity_provider_id"]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    identity_provider_id: str
    def __init__(self, identity_provider_id: _Optional[str] = ...) -> None: ...

class DeleteIdentityProviderConfigResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
