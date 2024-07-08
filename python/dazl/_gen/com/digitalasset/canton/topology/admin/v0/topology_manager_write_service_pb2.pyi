# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v0 import crypto_pb2 as _crypto_pb2
from ....protocol.v0 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v0 import topology_pb2 as _topology_pb2
from ....protocol.v1 import sequencing_pb2 as _sequencing_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationSuccess(_message.Message):
    __slots__ = ["serialized"]
    SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    serialized: bytes
    def __init__(self, serialized: _Optional[bytes] = ...) -> None: ...

class AdditionSuccess(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class SignedTopologyTransactionAddition(_message.Message):
    __slots__ = ["serialized"]
    SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    serialized: bytes
    def __init__(self, serialized: _Optional[bytes] = ...) -> None: ...

class AuthorizationData(_message.Message):
    __slots__ = ["change", "signed_by", "replace_existing", "force_change"]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    FORCE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    change: _topology_pb2.TopologyChangeOp
    signed_by: str
    replace_existing: bool
    force_change: bool
    def __init__(self, change: _Optional[_Union[_topology_pb2.TopologyChangeOp, str]] = ..., signed_by: _Optional[str] = ..., replace_existing: bool = ..., force_change: bool = ...) -> None: ...

class NamespaceDelegationAuthorization(_message.Message):
    __slots__ = ["authorization", "namespace", "fingerprint_of_authorized_key", "is_root_delegation"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_OF_AUTHORIZED_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    namespace: str
    fingerprint_of_authorized_key: str
    is_root_delegation: bool
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., namespace: _Optional[str] = ..., fingerprint_of_authorized_key: _Optional[str] = ..., is_root_delegation: bool = ...) -> None: ...

class IdentifierDelegationAuthorization(_message.Message):
    __slots__ = ["authorization", "identifier", "fingerprint_of_authorized_key"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_OF_AUTHORIZED_KEY_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    identifier: str
    fingerprint_of_authorized_key: str
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., identifier: _Optional[str] = ..., fingerprint_of_authorized_key: _Optional[str] = ...) -> None: ...

class PartyToParticipantAuthorization(_message.Message):
    __slots__ = ["authorization", "side", "party", "participant", "permission"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    side: _topology_pb2.RequestSide
    party: str
    participant: str
    permission: _topology_pb2.ParticipantPermission
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., side: _Optional[_Union[_topology_pb2.RequestSide, str]] = ..., party: _Optional[str] = ..., participant: _Optional[str] = ..., permission: _Optional[_Union[_topology_pb2.ParticipantPermission, str]] = ...) -> None: ...

class OwnerToKeyMappingAuthorization(_message.Message):
    __slots__ = ["authorization", "key_owner", "fingerprint_of_key", "key_purpose"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    KEY_OWNER_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_OF_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    key_owner: str
    fingerprint_of_key: str
    key_purpose: _crypto_pb2.KeyPurpose
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., key_owner: _Optional[str] = ..., fingerprint_of_key: _Optional[str] = ..., key_purpose: _Optional[_Union[_crypto_pb2.KeyPurpose, str]] = ...) -> None: ...

class ParticipantDomainStateAuthorization(_message.Message):
    __slots__ = ["authorization", "side", "domain", "participant", "permission", "trust_level"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    TRUST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    side: _topology_pb2.RequestSide
    domain: str
    participant: str
    permission: _topology_pb2.ParticipantPermission
    trust_level: _topology_pb2.TrustLevel
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., side: _Optional[_Union[_topology_pb2.RequestSide, str]] = ..., domain: _Optional[str] = ..., participant: _Optional[str] = ..., permission: _Optional[_Union[_topology_pb2.ParticipantPermission, str]] = ..., trust_level: _Optional[_Union[_topology_pb2.TrustLevel, str]] = ...) -> None: ...

class MediatorDomainStateAuthorization(_message.Message):
    __slots__ = ["authorization", "side", "domain", "mediator"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    side: _topology_pb2.RequestSide
    domain: str
    mediator: str
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., side: _Optional[_Union[_topology_pb2.RequestSide, str]] = ..., domain: _Optional[str] = ..., mediator: _Optional[str] = ...) -> None: ...

class VettedPackagesAuthorization(_message.Message):
    __slots__ = ["authorization", "participant", "package_ids"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    participant: str
    package_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., participant: _Optional[str] = ..., package_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DomainParametersChangeAuthorization(_message.Message):
    __slots__ = ["authorization", "domain", "parameters_v0", "parameters_v1"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_V0_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_V1_FIELD_NUMBER: _ClassVar[int]
    authorization: AuthorizationData
    domain: str
    parameters_v0: _sequencing_pb2.DynamicDomainParameters
    parameters_v1: _sequencing_pb2_1.DynamicDomainParameters
    def __init__(self, authorization: _Optional[_Union[AuthorizationData, _Mapping]] = ..., domain: _Optional[str] = ..., parameters_v0: _Optional[_Union[_sequencing_pb2.DynamicDomainParameters, _Mapping]] = ..., parameters_v1: _Optional[_Union[_sequencing_pb2_1.DynamicDomainParameters, _Mapping]] = ...) -> None: ...
