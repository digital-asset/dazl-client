# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AcsCommitment(_message.Message):
    __slots__ = ("synchronizer_id", "sending_participant_uid", "counter_participant_uid", "from_exclusive", "to_inclusive", "commitment")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    FROM_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    sending_participant_uid: str
    counter_participant_uid: str
    from_exclusive: int
    to_inclusive: int
    commitment: bytes
    def __init__(self, synchronizer_id: _Optional[str] = ..., sending_participant_uid: _Optional[str] = ..., counter_participant_uid: _Optional[str] = ..., from_exclusive: _Optional[int] = ..., to_inclusive: _Optional[int] = ..., commitment: _Optional[bytes] = ...) -> None: ...
