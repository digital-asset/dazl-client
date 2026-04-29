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

class AcsCommitment(_message.Message):
    __slots__ = ("physical_synchronizer_id", "sending_participant_uid", "counter_participant_uid", "from_exclusive", "to_inclusive", "commitment")
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    FROM_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    physical_synchronizer_id: str
    sending_participant_uid: str
    counter_participant_uid: str
    from_exclusive: int
    to_inclusive: int
    commitment: bytes
    def __init__(self, physical_synchronizer_id: _Optional[str] = ..., sending_participant_uid: _Optional[str] = ..., counter_participant_uid: _Optional[str] = ..., from_exclusive: _Optional[int] = ..., to_inclusive: _Optional[int] = ..., commitment: _Optional[bytes] = ...) -> None: ...

class AcsCommitmentProtocolMessage(_message.Message):
    __slots__ = ("acs_commitment", "signatures")
    ACS_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    acs_commitment: bytes
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    def __init__(self, acs_commitment: _Optional[bytes] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...
