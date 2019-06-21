# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Types that describe the behavior of the ledger itself.
"""

import abc
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from .types_store import PackageStore
from .writing import Serializer


class TimeModel(abc.ABC):
    """
    Definition for a time model.
    """

    @abc.abstractmethod
    def get_time(self) -> datetime:
        """
        Retrieve the current time.
        """


class StaticTimeModel(TimeModel):
    """
    Time model backed by a static clock that only advances in time in response to an explicit
    request.
    """

    def __init__(self, start_time: datetime):
        if not isinstance(start_time, datetime):
            raise TypeError('start_time must be a datetime')
        self.current_time = start_time

    def get_time(self) -> datetime:
        return self.current_time


class RealTimeModel(TimeModel):

    def get_time(self) -> datetime:
        """
        Retrieve the current time.
        """
        return datetime.utcnow().replace(tzinfo=timezone.utc)


@dataclass(frozen=True)
class LedgerMetadata:
    """
    Attributes that are invariant with respect to any party on the ledger.
    """
    ledger_id: str
    store: PackageStore
    time_model: TimeModel
    serializer: Serializer[Any, Any]
    protocol_version: str
