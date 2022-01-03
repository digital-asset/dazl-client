# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from threading import Event

from ..scheduler import RunLevel

__all__ = ["RunState"]


class RunState:
    """
    Manage the current run level of the client.
    """

    def __init__(self, level=RunLevel.RUN_FOREVER):
        self._terminate = Event()
        self.level = level

    def handle_sigint(self):
        self.level = RunLevel.TERMINATE_GRACEFULLY
        self._terminate.set()

    def handle_sigquit(self):
        self.level = RunLevel.TERMINATE_IMMEDIATELY
        self._terminate.set()

    @property
    def terminate_requested(self) -> bool:
        """
        Indication of whether the user has requested a shutdown.
        """
        return self._terminate.is_set()
