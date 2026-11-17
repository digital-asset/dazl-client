# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from ..v30 import common_pb2 as _common_pb2
from ..v30 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v31 import participant_transaction_pb2 as _participant_transaction_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalAuthorization(_message.Message):
    __slots__ = ("authentications", "hashing_scheme_version", "max_record_time")
    class HashingSchemeVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HASHING_SCHEME_VERSION_UNSPECIFIED: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
        HASHING_SCHEME_VERSION_V2: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
        HASHING_SCHEME_VERSION_V3: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
        HASHING_SCHEME_VERSION_V4: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
    HASHING_SCHEME_VERSION_UNSPECIFIED: ExternalAuthorization.HashingSchemeVersion
    HASHING_SCHEME_VERSION_V2: ExternalAuthorization.HashingSchemeVersion
    HASHING_SCHEME_VERSION_V3: ExternalAuthorization.HashingSchemeVersion
    HASHING_SCHEME_VERSION_V4: ExternalAuthorization.HashingSchemeVersion
    AUTHENTICATIONS_FIELD_NUMBER: _ClassVar[int]
    HASHING_SCHEME_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    authentications: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2.ExternalPartyAuthorization]
    hashing_scheme_version: ExternalAuthorization.HashingSchemeVersion
    max_record_time: int
    def __init__(self, authentications: _Optional[_Iterable[_Union[_participant_transaction_pb2.ExternalPartyAuthorization, _Mapping]]] = ..., hashing_scheme_version: _Optional[_Union[ExternalAuthorization.HashingSchemeVersion, str]] = ..., max_record_time: _Optional[int] = ...) -> None: ...

class SubmitterMetadata(_message.Message):
    __slots__ = ("salt", "act_as", "user_id", "command_id", "submitting_participant_uid", "submission_id", "dedup_period", "max_sequencing_time", "external_authorization")
    SALT_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUP_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    act_as: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    command_id: str
    submitting_participant_uid: str
    submission_id: str
    dedup_period: _participant_transaction_pb2.DeduplicationPeriod
    max_sequencing_time: int
    external_authorization: ExternalAuthorization
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ..., command_id: _Optional[str] = ..., submitting_participant_uid: _Optional[str] = ..., submission_id: _Optional[str] = ..., dedup_period: _Optional[_Union[_participant_transaction_pb2.DeduplicationPeriod, _Mapping]] = ..., max_sequencing_time: _Optional[int] = ..., external_authorization: _Optional[_Union[ExternalAuthorization, _Mapping]] = ...) -> None: ...

class ViewExternalCallResult(_message.Message):
    __slots__ = ("extension_id", "function_id", "config", "input", "output", "exercise_index", "call_index", "checking_parties")
    EXTENSION_ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_INDEX_FIELD_NUMBER: _ClassVar[int]
    CALL_INDEX_FIELD_NUMBER: _ClassVar[int]
    CHECKING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    extension_id: str
    function_id: str
    config: bytes
    input: bytes
    output: bytes
    exercise_index: int
    call_index: int
    checking_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, extension_id: _Optional[str] = ..., function_id: _Optional[str] = ..., config: _Optional[bytes] = ..., input: _Optional[bytes] = ..., output: _Optional[bytes] = ..., exercise_index: _Optional[int] = ..., call_index: _Optional[int] = ..., checking_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class ViewParticipantData(_message.Message):
    __slots__ = ("salt", "core_inputs", "created_core", "created_in_subview_archived_in_core", "resolved_keys", "action_description", "external_call_results", "rolled_back")
    SALT_FIELD_NUMBER: _ClassVar[int]
    CORE_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_CORE_FIELD_NUMBER: _ClassVar[int]
    CREATED_IN_SUBVIEW_ARCHIVED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ACTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CALL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ROLLED_BACK_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    core_inputs: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2.InputContract]
    created_core: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2_1.CreatedContract]
    created_in_subview_archived_in_core: _containers.RepeatedScalarFieldContainer[str]
    resolved_keys: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2_1.ViewParticipantData.KeyResolutionWithMaintainers]
    action_description: _participant_transaction_pb2_1.ActionDescription
    external_call_results: _containers.RepeatedCompositeFieldContainer[ViewExternalCallResult]
    rolled_back: bool
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., core_inputs: _Optional[_Iterable[_Union[_participant_transaction_pb2.InputContract, _Mapping]]] = ..., created_core: _Optional[_Iterable[_Union[_participant_transaction_pb2_1.CreatedContract, _Mapping]]] = ..., created_in_subview_archived_in_core: _Optional[_Iterable[str]] = ..., resolved_keys: _Optional[_Iterable[_Union[_participant_transaction_pb2_1.ViewParticipantData.KeyResolutionWithMaintainers, _Mapping]]] = ..., action_description: _Optional[_Union[_participant_transaction_pb2_1.ActionDescription, _Mapping]] = ..., external_call_results: _Optional[_Iterable[_Union[ViewExternalCallResult, _Mapping]]] = ..., rolled_back: _Optional[bool] = ...) -> None: ...

class EncryptedMultipleViewsMessage(_message.Message):
    __slots__ = ("compressed_view_trees", "view_hashes", "encryption_scheme", "submitting_participant_signature", "session_key_lookup", "physical_synchronizer_id", "view_type")
    class UncompressedViewTrees(_message.Message):
        __slots__ = ("view_trees",)
        VIEW_TREES_FIELD_NUMBER: _ClassVar[int]
        view_trees: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, view_trees: _Optional[_Iterable[bytes]] = ...) -> None: ...
    COMPRESSED_VIEW_TREES_FIELD_NUMBER: _ClassVar[int]
    VIEW_HASHES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SCHEME_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    compressed_view_trees: bytes
    view_hashes: _containers.RepeatedScalarFieldContainer[bytes]
    encryption_scheme: _crypto_pb2.SymmetricKeyScheme
    submitting_participant_signature: _crypto_pb2.Signature
    session_key_lookup: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.AsymmetricEncrypted]
    physical_synchronizer_id: str
    view_type: _common_pb2.ViewType
    def __init__(self, compressed_view_trees: _Optional[bytes] = ..., view_hashes: _Optional[_Iterable[bytes]] = ..., encryption_scheme: _Optional[_Union[_crypto_pb2.SymmetricKeyScheme, str]] = ..., submitting_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., session_key_lookup: _Optional[_Iterable[_Union[_crypto_pb2.AsymmetricEncrypted, _Mapping]]] = ..., physical_synchronizer_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ...) -> None: ...
