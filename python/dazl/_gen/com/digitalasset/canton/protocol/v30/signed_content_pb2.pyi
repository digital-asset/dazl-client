# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignedContent(_message.Message):
    __slots__ = ("content", "signatures", "timestamp_of_signing_key")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_OF_SIGNING_KEY_FIELD_NUMBER: _ClassVar[int]
    content: _wrappers_pb2.BytesValue
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    timestamp_of_signing_key: _wrappers_pb2.Int64Value
    def __init__(self, content: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., timestamp_of_signing_key: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
