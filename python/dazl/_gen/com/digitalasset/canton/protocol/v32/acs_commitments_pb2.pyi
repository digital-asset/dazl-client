# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommitmentPeriod(_message.Message):
    __slots__ = ("from_exclusive", "to_inclusive")
    FROM_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    from_exclusive: int
    to_inclusive: int
    def __init__(self, from_exclusive: _Optional[int] = ..., to_inclusive: _Optional[int] = ...) -> None: ...

class AcsCommitment(_message.Message):
    __slots__ = ("physical_synchronizer_id", "sending_participant_uid", "counterparticipant_uid", "period", "digest")
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    physical_synchronizer_id: str
    sending_participant_uid: str
    counterparticipant_uid: str
    period: CommitmentPeriod
    digest: bytes
    def __init__(self, physical_synchronizer_id: _Optional[str] = ..., sending_participant_uid: _Optional[str] = ..., counterparticipant_uid: _Optional[str] = ..., period: _Optional[_Union[CommitmentPeriod, _Mapping]] = ..., digest: _Optional[bytes] = ...) -> None: ...

class AcsCommitmentProtocolMessage(_message.Message):
    __slots__ = ("acs_commitment", "signature")
    ACS_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    acs_commitment: bytes
    signature: _crypto_pb2.Signature
    def __init__(self, acs_commitment: _Optional[bytes] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class AcsCommitmentSummary(_message.Message):
    __slots__ = ("physical_synchronizer_id", "commitment_tick", "addressed_counterparticipants", "unsent_digests", "batch_index", "last_batch")
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_TICK_FIELD_NUMBER: _ClassVar[int]
    ADDRESSED_COUNTERPARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    UNSENT_DIGESTS_FIELD_NUMBER: _ClassVar[int]
    BATCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    LAST_BATCH_FIELD_NUMBER: _ClassVar[int]
    physical_synchronizer_id: str
    commitment_tick: int
    addressed_counterparticipants: _containers.RepeatedScalarFieldContainer[str]
    unsent_digests: _containers.RepeatedCompositeFieldContainer[DigestForCounterparticipant]
    batch_index: int
    last_batch: bool
    def __init__(self, physical_synchronizer_id: _Optional[str] = ..., commitment_tick: _Optional[int] = ..., addressed_counterparticipants: _Optional[_Iterable[str]] = ..., unsent_digests: _Optional[_Iterable[_Union[DigestForCounterparticipant, _Mapping]]] = ..., batch_index: _Optional[int] = ..., last_batch: _Optional[bool] = ...) -> None: ...

class DigestForCounterparticipant(_message.Message):
    __slots__ = ("digest", "counterparticipant")
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    digest: bytes
    counterparticipant: str
    def __init__(self, digest: _Optional[bytes] = ..., counterparticipant: _Optional[str] = ...) -> None: ...

class AcsCommitmentSummaryProtocolMessage(_message.Message):
    __slots__ = ("acs_commitment_summary", "signature")
    ACS_COMMITMENT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    acs_commitment_summary: bytes
    signature: _crypto_pb2.Signature
    def __init__(self, acs_commitment_summary: _Optional[bytes] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...
