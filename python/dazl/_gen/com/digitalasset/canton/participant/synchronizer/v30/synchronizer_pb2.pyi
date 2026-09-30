# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PendingLsuOperation(_message.Message):
    __slots__ = ("successor_physical_synchronizer_id",)
    SUCCESSOR_PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    successor_physical_synchronizer_id: str
    def __init__(self, successor_physical_synchronizer_id: _Optional[str] = ...) -> None: ...

class PendingOnboardingTransactions(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, transactions: _Optional[_Iterable[bytes]] = ...) -> None: ...
