# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import warnings

from ..ledger.aio.pkgloader_compat import PackageLoader, SyncPackageService

warnings.warn(
    "dazl.client.pkg_loader is deprecated; use dazl.ledger.aio instead.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["SyncPackageService", "PackageLoader"]
