# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ......crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BftOrderingServiceReceiveRequest(_message.Message):
    __slots__ = ("trace_context", "body", "sent_by", "sent_at")
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    SENT_BY_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    trace_context: str
    body: BftOrderingMessageBody
    sent_by: str
    sent_at: _timestamp_pb2.Timestamp
    def __init__(self, trace_context: _Optional[str] = ..., body: _Optional[_Union[BftOrderingMessageBody, _Mapping]] = ..., sent_by: _Optional[str] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BftOrderingServiceReceiveResponse(_message.Message):
    __slots__ = ()
    FROM_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class BftOrderingMessageBody(_message.Message):
    __slots__ = ("availability_message", "consensus_message", "state_transfer_message", "retransmission_message")
    AVAILABILITY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_TRANSFER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRANSMISSION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    availability_message: SignedMessage
    consensus_message: SignedMessage
    state_transfer_message: SignedMessage
    retransmission_message: SignedMessage
    def __init__(self, availability_message: _Optional[_Union[SignedMessage, _Mapping]] = ..., consensus_message: _Optional[_Union[SignedMessage, _Mapping]] = ..., state_transfer_message: _Optional[_Union[SignedMessage, _Mapping]] = ..., retransmission_message: _Optional[_Union[SignedMessage, _Mapping]] = ...) -> None: ...

class SignedMessage(_message.Message):
    __slots__ = ("message", "signature")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    message: bytes
    signature: _crypto_pb2.Signature
    def __init__(self, message: _Optional[bytes] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., **kwargs) -> None: ...

class AvailabilityMessage(_message.Message):
    __slots__ = ("ping", "store_request", "store_response", "batch_request", "batch_response")
    PING_FIELD_NUMBER: _ClassVar[int]
    STORE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STORE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BATCH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BATCH_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ping: _empty_pb2.Empty
    store_request: StoreRequest
    store_response: StoreResponse
    batch_request: BatchRequest
    batch_response: BatchResponse
    def __init__(self, ping: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., store_request: _Optional[_Union[StoreRequest, _Mapping]] = ..., store_response: _Optional[_Union[StoreResponse, _Mapping]] = ..., batch_request: _Optional[_Union[BatchRequest, _Mapping]] = ..., batch_response: _Optional[_Union[BatchResponse, _Mapping]] = ...) -> None: ...

class StoreRequest(_message.Message):
    __slots__ = ("batch_id", "batch")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch_id: bytes
    batch: Batch
    def __init__(self, batch_id: _Optional[bytes] = ..., batch: _Optional[_Union[Batch, _Mapping]] = ...) -> None: ...

class Batch(_message.Message):
    __slots__ = ("ordering_requests", "epoch_number")
    ORDERING_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ordering_requests: _containers.RepeatedCompositeFieldContainer[OrderingRequest]
    epoch_number: int
    def __init__(self, ordering_requests: _Optional[_Iterable[_Union[OrderingRequest, _Mapping]]] = ..., epoch_number: _Optional[int] = ...) -> None: ...

class OrderingRequest(_message.Message):
    __slots__ = ("trace_context", "tag", "payload", "ordering_start_instant")
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ORDERING_START_INSTANT_FIELD_NUMBER: _ClassVar[int]
    trace_context: str
    tag: str
    payload: bytes
    ordering_start_instant: _timestamp_pb2.Timestamp
    def __init__(self, trace_context: _Optional[str] = ..., tag: _Optional[str] = ..., payload: _Optional[bytes] = ..., ordering_start_instant: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StoreResponse(_message.Message):
    __slots__ = ("batch_id", "signature")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    batch_id: bytes
    signature: _crypto_pb2.Signature
    def __init__(self, batch_id: _Optional[bytes] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class BatchRequest(_message.Message):
    __slots__ = ("batch_id",)
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    batch_id: bytes
    def __init__(self, batch_id: _Optional[bytes] = ...) -> None: ...

class BatchResponse(_message.Message):
    __slots__ = ("batch_id", "batch")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch_id: bytes
    batch: Batch
    def __init__(self, batch_id: _Optional[bytes] = ..., batch: _Optional[_Union[Batch, _Mapping]] = ...) -> None: ...

class OrderingBlock(_message.Message):
    __slots__ = ("proofs",)
    PROOFS_FIELD_NUMBER: _ClassVar[int]
    proofs: _containers.RepeatedCompositeFieldContainer[ProofOfAvailability]
    def __init__(self, proofs: _Optional[_Iterable[_Union[ProofOfAvailability, _Mapping]]] = ...) -> None: ...

class ProofOfAvailability(_message.Message):
    __slots__ = ("batch_id", "acks", "epoch_number")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    ACKS_FIELD_NUMBER: _ClassVar[int]
    EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    batch_id: bytes
    acks: _containers.RepeatedCompositeFieldContainer[AvailabilityAck]
    epoch_number: int
    def __init__(self, batch_id: _Optional[bytes] = ..., acks: _Optional[_Iterable[_Union[AvailabilityAck, _Mapping]]] = ..., epoch_number: _Optional[int] = ...) -> None: ...

class AvailabilityAck(_message.Message):
    __slots__ = ("signature",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signature: _crypto_pb2.Signature
    def __init__(self, signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., **kwargs) -> None: ...

class ConsensusMessage(_message.Message):
    __slots__ = ("block_metadata", "view_number", "pre_prepare", "prepare", "commit", "view_change", "new_view")
    BLOCK_METADATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    PRE_PREPARE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    VIEW_CHANGE_FIELD_NUMBER: _ClassVar[int]
    NEW_VIEW_FIELD_NUMBER: _ClassVar[int]
    block_metadata: BlockMetadata
    view_number: int
    pre_prepare: PrePrepare
    prepare: Prepare
    commit: Commit
    view_change: ViewChange
    new_view: NewView
    def __init__(self, block_metadata: _Optional[_Union[BlockMetadata, _Mapping]] = ..., view_number: _Optional[int] = ..., pre_prepare: _Optional[_Union[PrePrepare, _Mapping]] = ..., prepare: _Optional[_Union[Prepare, _Mapping]] = ..., commit: _Optional[_Union[Commit, _Mapping]] = ..., view_change: _Optional[_Union[ViewChange, _Mapping]] = ..., new_view: _Optional[_Union[NewView, _Mapping]] = ..., **kwargs) -> None: ...

class BlockMetadata(_message.Message):
    __slots__ = ("epoch_number", "block_number")
    EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    epoch_number: int
    block_number: int
    def __init__(self, epoch_number: _Optional[int] = ..., block_number: _Optional[int] = ...) -> None: ...

class PrePrepare(_message.Message):
    __slots__ = ("block", "bft_time_canonical_commit_set")
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    BFT_TIME_CANONICAL_COMMIT_SET_FIELD_NUMBER: _ClassVar[int]
    block: OrderingBlock
    bft_time_canonical_commit_set: CanonicalCommitSet
    def __init__(self, block: _Optional[_Union[OrderingBlock, _Mapping]] = ..., bft_time_canonical_commit_set: _Optional[_Union[CanonicalCommitSet, _Mapping]] = ...) -> None: ...

class Prepare(_message.Message):
    __slots__ = ("block_hash",)
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    block_hash: bytes
    def __init__(self, block_hash: _Optional[bytes] = ...) -> None: ...

class Commit(_message.Message):
    __slots__ = ("block_hash", "local_timestamp")
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    block_hash: bytes
    local_timestamp: int
    def __init__(self, block_hash: _Optional[bytes] = ..., local_timestamp: _Optional[int] = ...) -> None: ...

class ViewChange(_message.Message):
    __slots__ = ("consensus_certs",)
    CONSENSUS_CERTS_FIELD_NUMBER: _ClassVar[int]
    consensus_certs: _containers.RepeatedCompositeFieldContainer[ConsensusCertificate]
    def __init__(self, consensus_certs: _Optional[_Iterable[_Union[ConsensusCertificate, _Mapping]]] = ...) -> None: ...

class NewView(_message.Message):
    __slots__ = ("view_changes", "pre_prepares")
    VIEW_CHANGES_FIELD_NUMBER: _ClassVar[int]
    PRE_PREPARES_FIELD_NUMBER: _ClassVar[int]
    view_changes: _containers.RepeatedCompositeFieldContainer[SignedMessage]
    pre_prepares: _containers.RepeatedCompositeFieldContainer[SignedMessage]
    def __init__(self, view_changes: _Optional[_Iterable[_Union[SignedMessage, _Mapping]]] = ..., pre_prepares: _Optional[_Iterable[_Union[SignedMessage, _Mapping]]] = ...) -> None: ...

class CanonicalCommitSet(_message.Message):
    __slots__ = ("canonical_commits",)
    CANONICAL_COMMITS_FIELD_NUMBER: _ClassVar[int]
    canonical_commits: _containers.RepeatedCompositeFieldContainer[SignedMessage]
    def __init__(self, canonical_commits: _Optional[_Iterable[_Union[SignedMessage, _Mapping]]] = ...) -> None: ...

class ConsensusCertificate(_message.Message):
    __slots__ = ("prepare_certificate", "commit_certificate")
    PREPARE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    COMMIT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    prepare_certificate: PrepareCertificate
    commit_certificate: CommitCertificate
    def __init__(self, prepare_certificate: _Optional[_Union[PrepareCertificate, _Mapping]] = ..., commit_certificate: _Optional[_Union[CommitCertificate, _Mapping]] = ...) -> None: ...

class PrepareCertificate(_message.Message):
    __slots__ = ("pre_prepare", "prepares")
    PRE_PREPARE_FIELD_NUMBER: _ClassVar[int]
    PREPARES_FIELD_NUMBER: _ClassVar[int]
    pre_prepare: SignedMessage
    prepares: _containers.RepeatedCompositeFieldContainer[SignedMessage]
    def __init__(self, pre_prepare: _Optional[_Union[SignedMessage, _Mapping]] = ..., prepares: _Optional[_Iterable[_Union[SignedMessage, _Mapping]]] = ...) -> None: ...

class CommitCertificate(_message.Message):
    __slots__ = ("pre_prepare", "commits")
    PRE_PREPARE_FIELD_NUMBER: _ClassVar[int]
    COMMITS_FIELD_NUMBER: _ClassVar[int]
    pre_prepare: SignedMessage
    commits: _containers.RepeatedCompositeFieldContainer[SignedMessage]
    def __init__(self, pre_prepare: _Optional[_Union[SignedMessage, _Mapping]] = ..., commits: _Optional[_Iterable[_Union[SignedMessage, _Mapping]]] = ...) -> None: ...

class RetransmissionMessage(_message.Message):
    __slots__ = ("retransmission_request", "retransmission_response")
    RETRANSMISSION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RETRANSMISSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    retransmission_request: EpochStatus
    retransmission_response: RetransmissionResponse
    def __init__(self, retransmission_request: _Optional[_Union[EpochStatus, _Mapping]] = ..., retransmission_response: _Optional[_Union[RetransmissionResponse, _Mapping]] = ...) -> None: ...

class RetransmissionResponse(_message.Message):
    __slots__ = ("commit_certificates",)
    COMMIT_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    commit_certificates: _containers.RepeatedCompositeFieldContainer[CommitCertificate]
    def __init__(self, commit_certificates: _Optional[_Iterable[_Union[CommitCertificate, _Mapping]]] = ...) -> None: ...

class EpochStatus(_message.Message):
    __slots__ = ("epoch_number", "segments")
    EPOCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    epoch_number: int
    segments: _containers.RepeatedCompositeFieldContainer[SegmentStatus]
    def __init__(self, epoch_number: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[SegmentStatus, _Mapping]]] = ...) -> None: ...

class SegmentStatus(_message.Message):
    __slots__ = ("complete", "in_view_change", "in_progress")
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    IN_VIEW_CHANGE_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    complete: _empty_pb2.Empty
    in_view_change: SegmentInViewChange
    in_progress: SegmentInProgress
    def __init__(self, complete: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., in_view_change: _Optional[_Union[SegmentInViewChange, _Mapping]] = ..., in_progress: _Optional[_Union[SegmentInProgress, _Mapping]] = ...) -> None: ...

class SegmentInViewChange(_message.Message):
    __slots__ = ("view_number", "view_change_messages_present", "are_blocks_complete")
    VIEW_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VIEW_CHANGE_MESSAGES_PRESENT_FIELD_NUMBER: _ClassVar[int]
    ARE_BLOCKS_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    view_number: int
    view_change_messages_present: _containers.RepeatedScalarFieldContainer[bool]
    are_blocks_complete: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, view_number: _Optional[int] = ..., view_change_messages_present: _Optional[_Iterable[bool]] = ..., are_blocks_complete: _Optional[_Iterable[bool]] = ...) -> None: ...

class SegmentInProgress(_message.Message):
    __slots__ = ("view_number", "block_statuses")
    VIEW_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BLOCK_STATUSES_FIELD_NUMBER: _ClassVar[int]
    view_number: int
    block_statuses: _containers.RepeatedCompositeFieldContainer[BlockStatus]
    def __init__(self, view_number: _Optional[int] = ..., block_statuses: _Optional[_Iterable[_Union[BlockStatus, _Mapping]]] = ...) -> None: ...

class BlockStatus(_message.Message):
    __slots__ = ("complete", "in_progress")
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    complete: _empty_pb2.Empty
    in_progress: BlockInProgress
    def __init__(self, complete: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., in_progress: _Optional[_Union[BlockInProgress, _Mapping]] = ...) -> None: ...

class BlockInProgress(_message.Message):
    __slots__ = ("pre_prepared", "prepares_present", "commits_present")
    PRE_PREPARED_FIELD_NUMBER: _ClassVar[int]
    PREPARES_PRESENT_FIELD_NUMBER: _ClassVar[int]
    COMMITS_PRESENT_FIELD_NUMBER: _ClassVar[int]
    pre_prepared: bool
    prepares_present: _containers.RepeatedScalarFieldContainer[bool]
    commits_present: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, pre_prepared: bool = ..., prepares_present: _Optional[_Iterable[bool]] = ..., commits_present: _Optional[_Iterable[bool]] = ...) -> None: ...

class StateTransferMessage(_message.Message):
    __slots__ = ("block_request", "block_response")
    BLOCK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BLOCK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    block_request: BlockTransferRequest
    block_response: BlockTransferResponse
    def __init__(self, block_request: _Optional[_Union[BlockTransferRequest, _Mapping]] = ..., block_response: _Optional[_Union[BlockTransferResponse, _Mapping]] = ...) -> None: ...

class BlockTransferRequest(_message.Message):
    __slots__ = ("epoch",)
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    def __init__(self, epoch: _Optional[int] = ...) -> None: ...

class BlockTransferResponse(_message.Message):
    __slots__ = ("commit_certificate",)
    COMMIT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    commit_certificate: CommitCertificate
    def __init__(self, commit_certificate: _Optional[_Union[CommitCertificate, _Mapping]] = ...) -> None: ...
