# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AggregatedSignaturesOfSender(_message.Message):
    __slots__ = ("signatures_by_envelope",)
    class SignaturesForEnvelope(_message.Message):
        __slots__ = ("signatures",)
        SIGNATURES_FIELD_NUMBER: _ClassVar[int]
        signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
        def __init__(self, signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...
    SIGNATURES_BY_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    signatures_by_envelope: _containers.RepeatedCompositeFieldContainer[AggregatedSignaturesOfSender.SignaturesForEnvelope]
    def __init__(self, signatures_by_envelope: _Optional[_Iterable[_Union[AggregatedSignaturesOfSender.SignaturesForEnvelope, _Mapping]]] = ...) -> None: ...
