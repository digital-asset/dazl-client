# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from enum import Enum


class ConnectedSynchronizerPermission(str, Enum):
    PARTICIPANT_PERMISSION_CONFIRMATION = "PARTICIPANT_PERMISSION_CONFIRMATION"
    PARTICIPANT_PERMISSION_OBSERVATION = "PARTICIPANT_PERMISSION_OBSERVATION"
    PARTICIPANT_PERMISSION_SUBMISSION = "PARTICIPANT_PERMISSION_SUBMISSION"
    PARTICIPANT_PERMISSION_UNSPECIFIED = "PARTICIPANT_PERMISSION_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
