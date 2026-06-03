# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from enum import Enum


class UpdateVettedPackagesRequestUpdateVettedPackagesForceFlagsItem(str, Enum):
    UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES = (
        "UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES"
    )
    UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_VET_INCOMPATIBLE_UPGRADES = (
        "UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_VET_INCOMPATIBLE_UPGRADES"
    )
    UPDATE_VETTED_PACKAGES_FORCE_FLAG_UNSPECIFIED = "UPDATE_VETTED_PACKAGES_FORCE_FLAG_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
