# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from ..v30 import participant_transaction_pb2 as _participant_transaction_pb2
from . import common_stable_pb2 as _common_stable_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class ExternalAuthorization(_message.Message):
    __slots__ = ("authentications", "hashing_scheme_version", "max_record_time")
    class HashingSchemeVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HASHING_SCHEME_VERSION_UNSPECIFIED: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
        HASHING_SCHEME_VERSION_V2: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
        HASHING_SCHEME_VERSION_V3: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
    HASHING_SCHEME_VERSION_UNSPECIFIED: ExternalAuthorization.HashingSchemeVersion
    HASHING_SCHEME_VERSION_V2: ExternalAuthorization.HashingSchemeVersion
    HASHING_SCHEME_VERSION_V3: ExternalAuthorization.HashingSchemeVersion
    AUTHENTICATIONS_FIELD_NUMBER: _ClassVar[int]
    HASHING_SCHEME_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    authentications: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2.ExternalPartyAuthorization]
    hashing_scheme_version: ExternalAuthorization.HashingSchemeVersion
    max_record_time: int
    def __init__(self, authentications: _Optional[_Iterable[_Union[_participant_transaction_pb2.ExternalPartyAuthorization, _Mapping]]] = ..., hashing_scheme_version: _Optional[_Union[ExternalAuthorization.HashingSchemeVersion, str]] = ..., max_record_time: _Optional[int] = ...) -> None: ...

class ActionDescription(_message.Message):
    __slots__ = ("create", "exercise", "fetch")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    create: _participant_transaction_pb2.ActionDescription.CreateActionDescription
    exercise: _participant_transaction_pb2.ActionDescription.ExerciseActionDescription
    fetch: _participant_transaction_pb2.ActionDescription.FetchActionDescription
    def __init__(self, create: _Optional[_Union[_participant_transaction_pb2.ActionDescription.CreateActionDescription, _Mapping]] = ..., exercise: _Optional[_Union[_participant_transaction_pb2.ActionDescription.ExerciseActionDescription, _Mapping]] = ..., fetch: _Optional[_Union[_participant_transaction_pb2.ActionDescription.FetchActionDescription, _Mapping]] = ...) -> None: ...

class ViewParticipantData(_message.Message):
    __slots__ = ("salt", "core_inputs", "created_core", "created_in_subview_archived_in_core", "resolved_keys", "action_description", "rollback_context")
    class KeyResolutionWithMaintainers(_message.Message):
        __slots__ = ("key", "maintainers", "contract_ids")
        KEY_FIELD_NUMBER: _ClassVar[int]
        MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_IDS_FIELD_NUMBER: _ClassVar[int]
        key: _common_stable_pb2.GlobalKey
        maintainers: _containers.RepeatedScalarFieldContainer[str]
        contract_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[_Union[_common_stable_pb2.GlobalKey, _Mapping]] = ..., maintainers: _Optional[_Iterable[str]] = ..., contract_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    SALT_FIELD_NUMBER: _ClassVar[int]
    CORE_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_CORE_FIELD_NUMBER: _ClassVar[int]
    CREATED_IN_SUBVIEW_ARCHIVED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ACTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    core_inputs: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2.InputContract]
    created_core: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2.CreatedContract]
    created_in_subview_archived_in_core: _containers.RepeatedScalarFieldContainer[str]
    resolved_keys: _containers.RepeatedCompositeFieldContainer[ViewParticipantData.KeyResolutionWithMaintainers]
    action_description: ActionDescription
    rollback_context: _participant_transaction_pb2.ViewParticipantData.RollbackContext
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., core_inputs: _Optional[_Iterable[_Union[_participant_transaction_pb2.InputContract, _Mapping]]] = ..., created_core: _Optional[_Iterable[_Union[_participant_transaction_pb2.CreatedContract, _Mapping]]] = ..., created_in_subview_archived_in_core: _Optional[_Iterable[str]] = ..., resolved_keys: _Optional[_Iterable[_Union[ViewParticipantData.KeyResolutionWithMaintainers, _Mapping]]] = ..., action_description: _Optional[_Union[ActionDescription, _Mapping]] = ..., rollback_context: _Optional[_Union[_participant_transaction_pb2.ViewParticipantData.RollbackContext, _Mapping]] = ...) -> None: ...
