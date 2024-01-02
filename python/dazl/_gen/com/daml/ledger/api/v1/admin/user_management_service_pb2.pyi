# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import object_meta_pb2 as _object_meta_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["id", "primary_party", "is_deactivated", "metadata", "identity_provider_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PARTY_FIELD_NUMBER: _ClassVar[int]
    IS_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    primary_party: str
    is_deactivated: bool
    metadata: _object_meta_pb2.ObjectMeta
    identity_provider_id: str
    def __init__(self, id: _Optional[str] = ..., primary_party: _Optional[str] = ..., is_deactivated: bool = ..., metadata: _Optional[_Union[_object_meta_pb2.ObjectMeta, _Mapping]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class Right(_message.Message):
    __slots__ = ["participant_admin", "can_act_as", "can_read_as", "identity_provider_admin"]
    class ParticipantAdmin(_message.Message):
        __slots__ = []  # type: ignore
        def __init__(self) -> None: ...
    class CanActAs(_message.Message):
        __slots__ = ["party"]
        PARTY_FIELD_NUMBER: _ClassVar[int]
        party: str
        def __init__(self, party: _Optional[str] = ...) -> None: ...
    class CanReadAs(_message.Message):
        __slots__ = ["party"]
        PARTY_FIELD_NUMBER: _ClassVar[int]
        party: str
        def __init__(self, party: _Optional[str] = ...) -> None: ...
    class IdentityProviderAdmin(_message.Message):
        __slots__ = []  # type: ignore
        def __init__(self) -> None: ...
    PARTICIPANT_ADMIN_FIELD_NUMBER: _ClassVar[int]
    CAN_ACT_AS_FIELD_NUMBER: _ClassVar[int]
    CAN_READ_AS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ADMIN_FIELD_NUMBER: _ClassVar[int]
    participant_admin: Right.ParticipantAdmin
    can_act_as: Right.CanActAs
    can_read_as: Right.CanReadAs
    identity_provider_admin: Right.IdentityProviderAdmin
    def __init__(self, participant_admin: _Optional[_Union[Right.ParticipantAdmin, _Mapping]] = ..., can_act_as: _Optional[_Union[Right.CanActAs, _Mapping]] = ..., can_read_as: _Optional[_Union[Right.CanReadAs, _Mapping]] = ..., identity_provider_admin: _Optional[_Union[Right.IdentityProviderAdmin, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ["user", "rights"]
    USER_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    user: User
    rights: _containers.RepeatedCompositeFieldContainer[Right]
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., rights: _Optional[_Iterable[_Union[Right, _Mapping]]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ["user_id", "identity_provider_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    identity_provider_id: str
    def __init__(self, user_id: _Optional[str] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ["user", "update_mask"]
    USER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user: User
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ["user_id", "identity_provider_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    identity_provider_id: str
    def __init__(self, user_id: _Optional[str] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ["page_token", "page_size", "identity_provider_id"]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    page_token: str
    page_size: int
    identity_provider_id: str
    def __init__(self, page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ["users", "next_page_token"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    next_page_token: str
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GrantUserRightsRequest(_message.Message):
    __slots__ = ["user_id", "rights", "identity_provider_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    rights: _containers.RepeatedCompositeFieldContainer[Right]
    identity_provider_id: str
    def __init__(self, user_id: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[Right, _Mapping]]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class GrantUserRightsResponse(_message.Message):
    __slots__ = ["newly_granted_rights"]
    NEWLY_GRANTED_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    newly_granted_rights: _containers.RepeatedCompositeFieldContainer[Right]
    def __init__(self, newly_granted_rights: _Optional[_Iterable[_Union[Right, _Mapping]]] = ...) -> None: ...

class RevokeUserRightsRequest(_message.Message):
    __slots__ = ["user_id", "rights", "identity_provider_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    rights: _containers.RepeatedCompositeFieldContainer[Right]
    identity_provider_id: str
    def __init__(self, user_id: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[Right, _Mapping]]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class RevokeUserRightsResponse(_message.Message):
    __slots__ = ["newly_revoked_rights"]
    NEWLY_REVOKED_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    newly_revoked_rights: _containers.RepeatedCompositeFieldContainer[Right]
    def __init__(self, newly_revoked_rights: _Optional[_Iterable[_Union[Right, _Mapping]]] = ...) -> None: ...

class ListUserRightsRequest(_message.Message):
    __slots__ = ["user_id", "identity_provider_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    identity_provider_id: str
    def __init__(self, user_id: _Optional[str] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class ListUserRightsResponse(_message.Message):
    __slots__ = ["rights"]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    rights: _containers.RepeatedCompositeFieldContainer[Right]
    def __init__(self, rights: _Optional[_Iterable[_Union[Right, _Mapping]]] = ...) -> None: ...

class UpdateUserIdentityProviderRequest(_message.Message):
    __slots__ = ["user_id", "source_identity_provider_id", "target_identity_provider_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    source_identity_provider_id: str
    target_identity_provider_id: str
    def __init__(self, user_id: _Optional[str] = ..., source_identity_provider_id: _Optional[str] = ..., target_identity_provider_id: _Optional[str] = ...) -> None: ...

class UpdateUserIdentityProviderResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
