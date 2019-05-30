# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from ..model.core import RunLevel


class RunState:
    """
    Manage the current run level of the client.
    """
    def __init__(self, level=RunLevel.RUN_FOREVER):
        self.level = level

    def handle_sigint(self):
        self.level = RunLevel.TERMINATE_GRACEFULLY

    def handle_sigquit(self):
        self.level = RunLevel.TERMINATE_IMMEDIATELY
