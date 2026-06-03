# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from enum import Enum


class CostEstimationHintsExpectedSignaturesItem(str, Enum):
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256 = "SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256"
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384 = "SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384"
    SIGNING_ALGORITHM_SPEC_ED25519 = "SIGNING_ALGORITHM_SPEC_ED25519"
    SIGNING_ALGORITHM_SPEC_UNSPECIFIED = "SIGNING_ALGORITHM_SPEC_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
