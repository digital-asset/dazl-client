# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import warnings

from dazl.ledger.pkgloader_aio_compat import PackageLoader, SyncPackageService

warnings.warn("dazl.client.pkg_loader is deprecated; use dazl.protocols.pkgloader_aio instead.")

__all__ = ["SyncPackageService", "PackageLoader"]
