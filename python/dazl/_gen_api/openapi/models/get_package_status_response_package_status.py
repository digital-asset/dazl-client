# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from enum import Enum


class GetPackageStatusResponsePackageStatus(str, Enum):
    PACKAGE_STATUS_REGISTERED = "PACKAGE_STATUS_REGISTERED"
    PACKAGE_STATUS_UNSPECIFIED = "PACKAGE_STATUS_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
