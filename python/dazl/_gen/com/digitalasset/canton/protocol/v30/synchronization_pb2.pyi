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

class TypedSignedProtocolMessageContent(_message.Message):
    __slots__ = ("confirmation_responses", "confirmation_result", "acs_commitment", "set_traffic_purchased")
    CONFIRMATION_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ACS_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    SET_TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    confirmation_responses: bytes
    confirmation_result: bytes
    acs_commitment: bytes
    set_traffic_purchased: bytes
    def __init__(self, confirmation_responses: _Optional[bytes] = ..., confirmation_result: _Optional[bytes] = ..., acs_commitment: _Optional[bytes] = ..., set_traffic_purchased: _Optional[bytes] = ...) -> None: ...

class SignedProtocolMessage(_message.Message):
    __slots__ = ("signature", "typed_signed_protocol_message_content")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TYPED_SIGNED_PROTOCOL_MESSAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    signature: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    typed_signed_protocol_message_content: bytes
    def __init__(self, signature: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., typed_signed_protocol_message_content: _Optional[bytes] = ...) -> None: ...

class LsuSequencingTestMessage(_message.Message):
    __slots__ = ("content", "signatures")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    signatures: _crypto_pb2.Signature
    def __init__(self, content: _Optional[bytes] = ..., signatures: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class LsuSequencingTestMessageContent(_message.Message):
    __slots__ = ("physical_synchronizer_id", "sender")
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    physical_synchronizer_id: str
    sender: str
    def __init__(self, physical_synchronizer_id: _Optional[str] = ..., sender: _Optional[str] = ...) -> None: ...
