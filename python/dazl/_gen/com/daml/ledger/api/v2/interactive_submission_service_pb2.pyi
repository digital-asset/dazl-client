# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import commands_pb2 as _commands_pb2
from . import interactive_submission_data_pb2 as _interactive_submission_data_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignatureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_FORMAT_UNSPECIFIED: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_RAW: _ClassVar[SignatureFormat]
SIGNATURE_FORMAT_UNSPECIFIED: SignatureFormat
SIGNATURE_FORMAT_RAW: SignatureFormat

class PrepareSubmissionRequest(_message.Message):
    __slots__ = ("application_id", "command_id", "commands", "min_ledger_time_abs", "min_ledger_time_rel", "act_as", "read_as", "disclosed_contracts", "domain_id", "package_id_selection_preference")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_ABS_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_REL_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    READ_AS_FIELD_NUMBER: _ClassVar[int]
    DISCLOSED_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_SELECTION_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    command_id: str
    commands: _containers.RepeatedCompositeFieldContainer[_commands_pb2.Command]
    min_ledger_time_abs: _timestamp_pb2.Timestamp
    min_ledger_time_rel: _duration_pb2.Duration
    act_as: _containers.RepeatedScalarFieldContainer[str]
    read_as: _containers.RepeatedScalarFieldContainer[str]
    disclosed_contracts: _containers.RepeatedCompositeFieldContainer[_commands_pb2.DisclosedContract]
    domain_id: str
    package_id_selection_preference: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, application_id: _Optional[str] = ..., command_id: _Optional[str] = ..., commands: _Optional[_Iterable[_Union[_commands_pb2.Command, _Mapping]]] = ..., min_ledger_time_abs: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_ledger_time_rel: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., read_as: _Optional[_Iterable[str]] = ..., disclosed_contracts: _Optional[_Iterable[_Union[_commands_pb2.DisclosedContract, _Mapping]]] = ..., domain_id: _Optional[str] = ..., package_id_selection_preference: _Optional[_Iterable[str]] = ...) -> None: ...

class PrepareSubmissionResponse(_message.Message):
    __slots__ = ("prepared_transaction", "prepared_transaction_hash")
    PREPARED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    PREPARED_TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    prepared_transaction: _interactive_submission_data_pb2.PreparedTransaction
    prepared_transaction_hash: bytes
    def __init__(self, prepared_transaction: _Optional[_Union[_interactive_submission_data_pb2.PreparedTransaction, _Mapping]] = ..., prepared_transaction_hash: _Optional[bytes] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ("format", "signature", "signed_by")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    format: SignatureFormat
    signature: bytes
    signed_by: str
    def __init__(self, format: _Optional[_Union[SignatureFormat, str]] = ..., signature: _Optional[bytes] = ..., signed_by: _Optional[str] = ...) -> None: ...

class SinglePartySignatures(_message.Message):
    __slots__ = ("party", "signatures")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    party: str
    signatures: _containers.RepeatedCompositeFieldContainer[Signature]
    def __init__(self, party: _Optional[str] = ..., signatures: _Optional[_Iterable[_Union[Signature, _Mapping]]] = ...) -> None: ...

class PartySignatures(_message.Message):
    __slots__ = ("signatures",)
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    signatures: _containers.RepeatedCompositeFieldContainer[SinglePartySignatures]
    def __init__(self, signatures: _Optional[_Iterable[_Union[SinglePartySignatures, _Mapping]]] = ...) -> None: ...

class ExecuteSubmissionRequest(_message.Message):
    __slots__ = ("prepared_transaction", "parties_signatures", "workflow_id", "deduplication_duration", "deduplication_offset", "submission_id", "application_id")
    PREPARED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    PARTIES_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    prepared_transaction: _interactive_submission_data_pb2.PreparedTransaction
    parties_signatures: PartySignatures
    workflow_id: str
    deduplication_duration: _duration_pb2.Duration
    deduplication_offset: int
    submission_id: str
    application_id: str
    def __init__(self, prepared_transaction: _Optional[_Union[_interactive_submission_data_pb2.PreparedTransaction, _Mapping]] = ..., parties_signatures: _Optional[_Union[PartySignatures, _Mapping]] = ..., workflow_id: _Optional[str] = ..., deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., deduplication_offset: _Optional[int] = ..., submission_id: _Optional[str] = ..., application_id: _Optional[str] = ...) -> None: ...

class ExecuteSubmissionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
