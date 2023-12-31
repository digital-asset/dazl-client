# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v0 import crypto_pb2 as _crypto_pb2
from ....protocol.v0 import topology_pb2 as _topology_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPartiesRequest(_message.Message):
    __slots__ = ["as_of", "limit", "filter_domain", "filter_party", "filter_participant"]
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    as_of: _timestamp_pb2.Timestamp
    limit: int
    filter_domain: str
    filter_party: str
    filter_participant: str
    def __init__(self, as_of: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ..., filter_domain: _Optional[str] = ..., filter_party: _Optional[str] = ..., filter_participant: _Optional[str] = ...) -> None: ...

class ListPartiesResponse(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["party", "participants"]
        class ParticipantDomains(_message.Message):
            __slots__ = ["participant", "domains"]
            class DomainPermissions(_message.Message):
                __slots__ = ["domain", "permission"]
                DOMAIN_FIELD_NUMBER: _ClassVar[int]
                PERMISSION_FIELD_NUMBER: _ClassVar[int]
                domain: str
                permission: _topology_pb2.ParticipantPermission
                def __init__(self, domain: _Optional[str] = ..., permission: _Optional[_Union[_topology_pb2.ParticipantPermission, str]] = ...) -> None: ...
            PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
            DOMAINS_FIELD_NUMBER: _ClassVar[int]
            participant: str
            domains: _containers.RepeatedCompositeFieldContainer[ListPartiesResponse.Result.ParticipantDomains.DomainPermissions]
            def __init__(self, participant: _Optional[str] = ..., domains: _Optional[_Iterable[_Union[ListPartiesResponse.Result.ParticipantDomains.DomainPermissions, _Mapping]]] = ...) -> None: ...
        PARTY_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
        party: str
        participants: _containers.RepeatedCompositeFieldContainer[ListPartiesResponse.Result.ParticipantDomains]
        def __init__(self, party: _Optional[str] = ..., participants: _Optional[_Iterable[_Union[ListPartiesResponse.Result.ParticipantDomains, _Mapping]]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPartiesResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPartiesResponse.Result, _Mapping]]] = ...) -> None: ...

class ListKeyOwnersRequest(_message.Message):
    __slots__ = ["as_of", "limit", "filter_domain", "filter_key_owner_type", "filter_key_owner_uid"]
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    as_of: _timestamp_pb2.Timestamp
    limit: int
    filter_domain: str
    filter_key_owner_type: str
    filter_key_owner_uid: str
    def __init__(self, as_of: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ..., filter_domain: _Optional[str] = ..., filter_key_owner_type: _Optional[str] = ..., filter_key_owner_uid: _Optional[str] = ...) -> None: ...

class ListKeyOwnersResponse(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["domain", "key_owner", "signing_keys", "encryption_keys"]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        KEY_OWNER_FIELD_NUMBER: _ClassVar[int]
        SIGNING_KEYS_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_KEYS_FIELD_NUMBER: _ClassVar[int]
        domain: str
        key_owner: str
        signing_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.SigningPublicKey]
        encryption_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.EncryptionPublicKey]
        def __init__(self, domain: _Optional[str] = ..., key_owner: _Optional[str] = ..., signing_keys: _Optional[_Iterable[_Union[_crypto_pb2.SigningPublicKey, _Mapping]]] = ..., encryption_keys: _Optional[_Iterable[_Union[_crypto_pb2.EncryptionPublicKey, _Mapping]]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListKeyOwnersResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListKeyOwnersResponse.Result, _Mapping]]] = ...) -> None: ...
