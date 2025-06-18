# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerdictResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERDICT_RESULT_UNSPECIFIED: _ClassVar[VerdictResult]
    VERDICT_RESULT_ACCEPTED: _ClassVar[VerdictResult]
    VERDICT_RESULT_REJECTED: _ClassVar[VerdictResult]
VERDICT_RESULT_UNSPECIFIED: VerdictResult
VERDICT_RESULT_ACCEPTED: VerdictResult
VERDICT_RESULT_REJECTED: VerdictResult

class VerdictsRequest(_message.Message):
    __slots__ = ("most_recently_received_record_time",)
    MOST_RECENTLY_RECEIVED_RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    most_recently_received_record_time: _timestamp_pb2.Timestamp
    def __init__(self, most_recently_received_record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class VerdictsResponse(_message.Message):
    __slots__ = ("verdict",)
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    verdict: Verdict
    def __init__(self, verdict: _Optional[_Union[Verdict, _Mapping]] = ...) -> None: ...

class Verdict(_message.Message):
    __slots__ = ("submitting_parties", "submitting_participant_uid", "verdict", "finalization_time", "record_time", "mediator_group", "transaction_views", "update_id")
    SUBMITTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    FINALIZATION_TIME_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_VIEWS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    submitting_parties: _containers.RepeatedScalarFieldContainer[str]
    submitting_participant_uid: str
    verdict: VerdictResult
    finalization_time: _timestamp_pb2.Timestamp
    record_time: _timestamp_pb2.Timestamp
    mediator_group: int
    transaction_views: TransactionViews
    update_id: str
    def __init__(self, submitting_parties: _Optional[_Iterable[str]] = ..., submitting_participant_uid: _Optional[str] = ..., verdict: _Optional[_Union[VerdictResult, str]] = ..., finalization_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., mediator_group: _Optional[int] = ..., transaction_views: _Optional[_Union[TransactionViews, _Mapping]] = ..., update_id: _Optional[str] = ...) -> None: ...

class TransactionViews(_message.Message):
    __slots__ = ("views", "root_views")
    class ViewsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TransactionView
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TransactionView, _Mapping]] = ...) -> None: ...
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    ROOT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    views: _containers.MessageMap[int, TransactionView]
    root_views: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, views: _Optional[_Mapping[int, TransactionView]] = ..., root_views: _Optional[_Iterable[int]] = ...) -> None: ...

class TransactionView(_message.Message):
    __slots__ = ("informees", "confirming_parties", "sub_views")
    INFORMEES_FIELD_NUMBER: _ClassVar[int]
    CONFIRMING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    SUB_VIEWS_FIELD_NUMBER: _ClassVar[int]
    informees: _containers.RepeatedScalarFieldContainer[str]
    confirming_parties: _containers.RepeatedCompositeFieldContainer[Quorum]
    sub_views: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, informees: _Optional[_Iterable[str]] = ..., confirming_parties: _Optional[_Iterable[_Union[Quorum, _Mapping]]] = ..., sub_views: _Optional[_Iterable[int]] = ...) -> None: ...

class Quorum(_message.Message):
    __slots__ = ("parties", "threshold")
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    threshold: int
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., threshold: _Optional[int] = ...) -> None: ...
