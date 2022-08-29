# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import ensure_future, gather, get_event_loop, sleep, wait_for
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from typing import Awaitable, Callable, Dict, Optional, TypeVar

from . import PackageService
from ... import LOG
from ...damlast.daml_lf_1 import Package, PackageRef
from ...damlast.errors import PackageNotFoundError
from ...damlast.lookup import STAR, MultiPackageLookup, PackageExceptionTracker
from ...damlast.parse import parse_archive
from ...damlast.pkgfile import Dar
from ...prim import DazlError

__all__ = ["PackageLoader", "DEFAULT_TIMEOUT"]

T = TypeVar("T")

# mypy insists on having a type annotation here, or it will complain about not being able to
# determine the type of this field in pkgloader_aio_compat.py
DEFAULT_TIMEOUT: timedelta = timedelta(seconds=30)


class PackageLoader:
    """
    Loader for packages from a remote PackageService.

    This class handles retries and backoffs, and avoids having more than one request in flight for
    the same package ID. It is intended to be shared by all local clients that may need package
    information.
    """

    _allow_deprecated_identifiers = False

    def __init__(
        self,
        package_lookup: "MultiPackageLookup",
        conn: "Optional[PackageService]" = None,
        timeout: "Optional[timedelta]" = DEFAULT_TIMEOUT,
        executor: "Optional[ThreadPoolExecutor]" = None,
    ):
        self._package_lookup = package_lookup
        self._conn = conn
        self._timeout = timeout or DEFAULT_TIMEOUT
        self._futures = dict()  # type: Dict[PackageRef, Awaitable[Package]]
        self._executor = executor or ThreadPoolExecutor(3)

    def set_connection(self, conn: "Optional[PackageService]"):
        self._conn = conn

    async def do_with_retry(self, fn: "Callable[[], T]") -> "T":
        """
        Perform a synchronous action that assumes the existence of one or more packages. In the
        event the function raises :class:`PackageNotFoundError` or a wildcarded
        :class:`NameNotFoundError`, the required package/type is fetched and the operation retried.

        If, after a retry, an expected package or type could not be found, the exception is
        re-raised to the caller.

        :param fn: A function to invoke.
        :return: The result of that function.
        """
        guard = PackageExceptionTracker(
            allow_deprecated_identifiers=self._allow_deprecated_identifiers
        )
        while True:
            pkg_ref = guard.pop_package()
            while pkg_ref is not None:
                await self.load(pkg_ref)
                pkg_ref = guard.pop_package()

            with guard:
                return fn()

    async def preload(self, *contents: "Dar") -> None:
        """
        Populate a :class:`PackageCache` with types from DARs.

        :param contents:
            One or more DARs to load into a local package cache.
        """

    async def load(self, ref: "PackageRef") -> "Optional[Package]":
        """
        Load a package ID from the remote server. If the package has additional dependencies, they
        are also loaded.

        :param ref: One or more :class:`PackageRef`s.
        :raises: PackageNotFoundError if the package could not be resolved
        """
        if ref == STAR:
            await self.load_all()
            return None

        # If the package has already been loaded, then skip all the expensive I/O stuff
        try:
            return self._package_lookup.package(ref)
        except PackageNotFoundError:
            pass

        # If we already have a request in-flight, simply return that same Future to our caller;
        # do not try to schedule a new request
        fut = self._futures.get(ref)
        if fut is None:
            fut = ensure_future(self._load(ref))
            self._futures[ref] = fut
        package = await fut

        _ = self._futures.pop(ref, None)

        return package

    async def _load(self, package_id: "PackageRef") -> "Package":
        LOG.info("Loading package: %s", package_id)

        loop = get_event_loop()
        conn = self._conn
        if conn is None:
            raise DazlError("a connection is not configured")

        archive_bytes = await wait_for(
            self.__fetch_package_bytes(conn, package_id), timeout=self._timeout.total_seconds()
        )

        LOG.info("Loaded for package: %s, %d bytes", package_id, len(archive_bytes))

        archive = await loop.run_in_executor(
            self._executor, lambda: parse_archive(package_id, archive_bytes)
        )
        self._package_lookup.add_archive(archive)
        return archive.package

    @staticmethod
    async def __fetch_package_bytes(conn: "PackageService", package_id: "PackageRef") -> bytes:
        sleep_interval = 1

        while True:
            # noinspection PyBroadException
            try:
                return await conn.get_package(package_id)
            except Exception:
                # We tried fetching the package but got an error. Retry, backing off to waiting as
                # much as 30 seconds between each attempt.
                await sleep(sleep_interval)
                sleep_interval = min(sleep_interval * 2, 30)
                LOG.exception("Failed to fetch package; this will be retried.")

    async def load_all(self) -> None:
        """
        Load all packages from the remote server.
        """
        conn = self._conn
        if conn is None:
            raise DazlError("a connection is not configured")

        package_ids = set(await conn.list_package_ids())
        package_ids -= self._package_lookup.package_ids()
        if package_ids:
            await gather(*(self.load(package_id) for package_id in package_ids))

        return None
