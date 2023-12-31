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

class GetParticipantIdRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetParticipantIdResponse(_message.Message):
    __slots__ = ["participant_id"]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    def __init__(self, participant_id: _Optional[str] = ...) -> None: ...

class GetPartiesRequest(_message.Message):
    __slots__ = ["parties", "identity_provider_id"]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    identity_provider_id: str
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class GetPartiesResponse(_message.Message):
    __slots__ = ["party_details"]
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    party_details: _containers.RepeatedCompositeFieldContainer[PartyDetails]
    def __init__(self, party_details: _Optional[_Iterable[_Union[PartyDetails, _Mapping]]] = ...) -> None: ...

class ListKnownPartiesRequest(_message.Message):
    __slots__ = ["identity_provider_id"]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    identity_provider_id: str
    def __init__(self, identity_provider_id: _Optional[str] = ...) -> None: ...

class ListKnownPartiesResponse(_message.Message):
    __slots__ = ["party_details"]
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    party_details: _containers.RepeatedCompositeFieldContainer[PartyDetails]
    def __init__(self, party_details: _Optional[_Iterable[_Union[PartyDetails, _Mapping]]] = ...) -> None: ...

class AllocatePartyRequest(_message.Message):
    __slots__ = ["party_id_hint", "display_name", "local_metadata", "identity_provider_id"]
    PARTY_ID_HINT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    party_id_hint: str
    display_name: str
    local_metadata: _object_meta_pb2.ObjectMeta
    identity_provider_id: str
    def __init__(self, party_id_hint: _Optional[str] = ..., display_name: _Optional[str] = ..., local_metadata: _Optional[_Union[_object_meta_pb2.ObjectMeta, _Mapping]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class AllocatePartyResponse(_message.Message):
    __slots__ = ["party_details"]
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    party_details: PartyDetails
    def __init__(self, party_details: _Optional[_Union[PartyDetails, _Mapping]] = ...) -> None: ...

class UpdatePartyDetailsRequest(_message.Message):
    __slots__ = ["party_details", "update_mask"]
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    party_details: PartyDetails
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, party_details: _Optional[_Union[PartyDetails, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePartyDetailsResponse(_message.Message):
    __slots__ = ["party_details"]
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    party_details: PartyDetails
    def __init__(self, party_details: _Optional[_Union[PartyDetails, _Mapping]] = ...) -> None: ...

class PartyDetails(_message.Message):
    __slots__ = ["party", "display_name", "is_local", "local_metadata", "identity_provider_id"]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    display_name: str
    is_local: bool
    local_metadata: _object_meta_pb2.ObjectMeta
    identity_provider_id: str
    def __init__(self, party: _Optional[str] = ..., display_name: _Optional[str] = ..., is_local: bool = ..., local_metadata: _Optional[_Union[_object_meta_pb2.ObjectMeta, _Mapping]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class UpdatePartyIdentityProviderRequest(_message.Message):
    __slots__ = ["party", "source_identity_provider_id", "target_identity_provider_id"]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    source_identity_provider_id: str
    target_identity_provider_id: str
    def __init__(self, party: _Optional[str] = ..., source_identity_provider_id: _Optional[str] = ..., target_identity_provider_id: _Optional[str] = ...) -> None: ...

class UpdatePartyIdentityProviderResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
