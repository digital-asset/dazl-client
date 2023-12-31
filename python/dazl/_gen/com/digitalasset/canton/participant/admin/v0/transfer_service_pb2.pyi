# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v0 import participant_transfer_pb2 as _participant_transfer_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdminTransferOutRequest(_message.Message):
    __slots__ = ["submitting_party", "contract_id", "origin_domain", "target_domain", "application_id", "submission_id", "workflow_id", "command_id"]
    SUBMITTING_PARTY_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    submitting_party: str
    contract_id: str
    origin_domain: str
    target_domain: str
    application_id: str
    submission_id: str
    workflow_id: str
    command_id: str
    def __init__(self, submitting_party: _Optional[str] = ..., contract_id: _Optional[str] = ..., origin_domain: _Optional[str] = ..., target_domain: _Optional[str] = ..., application_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., command_id: _Optional[str] = ...) -> None: ...

class AdminTransferOutResponse(_message.Message):
    __slots__ = ["transfer_id"]
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: _participant_transfer_pb2.TransferId
    def __init__(self, transfer_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ...) -> None: ...

class AdminTransferInRequest(_message.Message):
    __slots__ = ["submitting_party_id", "target_domain", "transfer_id", "application_id", "submission_id", "workflow_id", "command_id"]
    SUBMITTING_PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    submitting_party_id: str
    target_domain: str
    transfer_id: _participant_transfer_pb2.TransferId
    application_id: str
    submission_id: str
    workflow_id: str
    command_id: str
    def __init__(self, submitting_party_id: _Optional[str] = ..., target_domain: _Optional[str] = ..., transfer_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ..., application_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., command_id: _Optional[str] = ...) -> None: ...

class AdminTransferInResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class AdminTransferSearchQuery(_message.Message):
    __slots__ = ["search_domain", "filter_origin_domain", "filter_timestamp", "filter_submitting_party", "limit"]
    SEARCH_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILTER_ORIGIN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILTER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FILTER_SUBMITTING_PARTY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    search_domain: str
    filter_origin_domain: str
    filter_timestamp: _timestamp_pb2.Timestamp
    filter_submitting_party: str
    limit: int
    def __init__(self, search_domain: _Optional[str] = ..., filter_origin_domain: _Optional[str] = ..., filter_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter_submitting_party: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class AdminTransferSearchResponse(_message.Message):
    __slots__ = ["results"]
    class TransferSearchResult(_message.Message):
        __slots__ = ["contract_id", "transfer_id", "origin_domain", "target_domain", "submitting_party", "ready_for_transfer_in", "target_time_proof"]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        SUBMITTING_PARTY_FIELD_NUMBER: _ClassVar[int]
        READY_FOR_TRANSFER_IN_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIME_PROOF_FIELD_NUMBER: _ClassVar[int]
        contract_id: str
        transfer_id: _participant_transfer_pb2.TransferId
        origin_domain: str
        target_domain: str
        submitting_party: str
        ready_for_transfer_in: bool
        target_time_proof: _timestamp_pb2.Timestamp
        def __init__(self, contract_id: _Optional[str] = ..., transfer_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ..., origin_domain: _Optional[str] = ..., target_domain: _Optional[str] = ..., submitting_party: _Optional[str] = ..., ready_for_transfer_in: bool = ..., target_time_proof: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[AdminTransferSearchResponse.TransferSearchResult]
    def __init__(self, results: _Optional[_Iterable[_Union[AdminTransferSearchResponse.TransferSearchResult, _Mapping]]] = ...) -> None: ...
