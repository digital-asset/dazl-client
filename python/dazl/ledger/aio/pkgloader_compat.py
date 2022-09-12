# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Backwards compatibility symbols in support of the to-be-removed dazl.client.pkg_loader module.
This file is here in order to avoid import cycles.
"""

from asyncio import get_event_loop
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import timedelta
import sys
from typing import AbstractSet, Optional
import warnings

from dazl.damlast.daml_lf_1 import PackageRef
from dazl.damlast.lookup import MultiPackageLookup

from ...prim import TimeDeltaLike
from .pkgloader import DEFAULT_TIMEOUT, PackageLoader as NewPackageLoader

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

__all__ = ["SyncPackageService", "PackageLoader"]


class SyncPackageService(Protocol):
    """
    A service that synchronously provides package information.

    This _synchronous_ protocol was used in support of the _asynchronous_ PackageLoader for v7;
    this mismatch is a little confusing, so this API is deprecated.
    """

    def __init__(self):
        warnings.warn(
            "SyncPackageService is deprecated; implement the PackageService protocol instead.",
            DeprecationWarning,
            stacklevel=2,
        )

    def package_bytes(
        self, package_id: PackageRef, *, timeout: Optional[TimeDeltaLike] = None
    ) -> bytes:
        raise NotImplementedError("SyncPackageService.package_bytes requires an implementation")

    def package_ids(self, *, timeout: Optional[TimeDeltaLike] = None) -> AbstractSet[PackageRef]:
        raise NotImplementedError("SyncPackageService.package_ids requires an implementation")


class PackageLoader(NewPackageLoader):
    """
    Backwards-compatibility shim for dazl.client.pkg_loader.PackageLoader that exposes the same
    historical API but also emits a deprecation warning on construction.

    This shim will be removed in v9.
    """

    _allow_deprecated_identifiers = True

    def __init__(
        self,
        package_lookup: "MultiPackageLookup",
        conn: "Optional[SyncPackageService]" = None,
        timeout: "Optional[timedelta]" = DEFAULT_TIMEOUT,
    ):
        warnings.warn(
            "dazl.client.pkg_loader.PackageLoader has moved to "
            "dazl.protocols.pkgloader_aio.PackageLoader and now requires an async package loader.",
            DeprecationWarning,
            stacklevel=2,
        )
        executor = ThreadPoolExecutor(3)
        if conn is None:
            raise ValueError("conn is required")
        super().__init__(package_lookup, PackageServiceWrapper(conn, executor), timeout, executor)


class PackageServiceWrapper:
    def __init__(self, impl: "SyncPackageService", executor: "ThreadPoolExecutor"):
        self.impl = impl
        self.executor = executor

    async def get_package(
        self, package_id: PackageRef, *, timeout: Optional[TimeDeltaLike] = None
    ) -> bytes:
        loop = get_event_loop()
        return await loop.run_in_executor(
            self.executor, lambda: self.impl.package_bytes(package_id, timeout=timeout)
        )

    async def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = None
    ) -> "AbstractSet[PackageRef]":
        loop = get_event_loop()
        return await loop.run_in_executor(
            self.executor, lambda: self.impl.package_ids(timeout=timeout)
        )
