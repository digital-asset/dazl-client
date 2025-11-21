# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from enum import Enum


class JsPrepareSubmissionResponseHashingSchemeVersion(str, Enum):
    HASHING_SCHEME_VERSION_UNSPECIFIED = "HASHING_SCHEME_VERSION_UNSPECIFIED"
    HASHING_SCHEME_VERSION_V2 = "HASHING_SCHEME_VERSION_V2"

    def __str__(self) -> str:
        return str(self.value)
