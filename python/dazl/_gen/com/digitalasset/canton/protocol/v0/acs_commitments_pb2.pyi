# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcsCommitment(_message.Message):
    __slots__ = ["domain_id", "sending_participant", "counter_participant", "from_exclusive", "to_inclusive", "commitment"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SENDING_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    COUNTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    FROM_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    sending_participant: str
    counter_participant: str
    from_exclusive: _timestamp_pb2.Timestamp
    to_inclusive: _timestamp_pb2.Timestamp
    commitment: bytes
    def __init__(self, domain_id: _Optional[str] = ..., sending_participant: _Optional[str] = ..., counter_participant: _Optional[str] = ..., from_exclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., to_inclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., commitment: _Optional[bytes] = ...) -> None: ...
