# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import ensure_future, gather, get_event_loop, sleep, wait_for
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from typing import Awaitable, Callable, Optional, TypeVar

from . import PackageService
from ... import LOG
from ...damlast.daml_lf_1 import Package, PackageRef
from ...damlast.errors import PackageNotFoundError
from ...damlast.lookup import STAR, MultiPackageLookup, PackageExceptionTracker
from ...damlast.parse import parse_archive
from ...damlast.pkgfile import Dar, DarFile
from ...prim import DazlError
from ..auth import TokenOrTokenProvider

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
        package_lookup: MultiPackageLookup,
        conn: Optional[PackageService] = None,
        timeout: Optional[timedelta] = DEFAULT_TIMEOUT,
        executor: Optional[ThreadPoolExecutor] = None,
    ):
        self._package_lookup = package_lookup
        self._conn = conn
        self._timeout = timeout or DEFAULT_TIMEOUT
        self._futures = dict[PackageRef, Awaitable[Package]]()
        self._executor = executor or ThreadPoolExecutor(3)

    def set_connection(self, conn: Optional[PackageService]):
        self._conn = conn

    async def do_with_retry(
        self, fn: Callable[[], T], *, token: Optional[TokenOrTokenProvider] = None
    ) -> T:
        """
        Perform a synchronous action that assumes the existence of one or more packages. In the
        event the function raises :class:`PackageNotFoundError` or a wildcarded
        :class:`NameNotFoundError`, the required package/type is fetched and the operation retried.

        If, after a retry, an expected package or type could not be found, the exception is
        re-raised to the caller.

        :param fn:
            A function to invoke.
        :param token:
            An optional token to use in place of a connection-level token when fetching packages.
        :return:
            The result of that function.
        """
        guard = PackageExceptionTracker()
        while True:
            pkg_ref = guard.pop_package()
            while pkg_ref is not None:
                await self.load(pkg_ref, token=token)
                pkg_ref = guard.pop_package()

            with guard:
                return fn()

    async def preload(self, contents: bytes) -> None:
        """
        Populate a :class:`PackageCache` with types from a DAR.

        :param contents:
            A DAR to load in a local cache.
        """
        with DarFile(contents) as dar_file:
            self._package_lookup.add_archive(*dar_file.archives())

    async def load(
        self, ref: PackageRef, *, token: Optional[TokenOrTokenProvider] = None
    ) -> Optional[Package]:
        """
        Load a package ID from the remote server. If the package has additional dependencies, they
        are also loaded.

        :param ref:
            One or more :class:`PackageRef`s.
        :param token:
            An optional token to use in place of a connection-level token when fetching packages.
        :raises:
            PackageNotFoundError if the package could not be resolved
        """
        # With Daml 2, the best we can do when presented with a '*' or SCU-style template reference
        # is to load _all_ packages, and give ourselves the best chance for finding the package we
        # want. In Daml 3, newer services allow us to subscribe to package ID changes which will
        # allow us to keep a local cache of packages more cheaply without the intermediate unnecessary
        # fetching
        if ref == STAR or ref.startswith("#"):
            await self.load_all(token=token)
            if ref == STAR:
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
            fut = ensure_future(self._load(ref, token=token))
            self._futures[ref] = fut
        package = await fut

        _ = self._futures.pop(ref, None)

        return package

    async def _load(
        self, package_id: PackageRef, *, token: Optional[TokenOrTokenProvider] = None
    ) -> Package:
        LOG.info("Loading package: %s", package_id)

        loop = get_event_loop()
        conn = self._conn
        if conn is None:
            raise DazlError("a connection is not configured")

        archive_bytes = await wait_for(
            self.__fetch_package_bytes(conn, package_id, token=token),
            timeout=self._timeout.total_seconds(),
        )

        LOG.info("Loaded for package: %s, %d bytes", package_id, len(archive_bytes))

        archive = await loop.run_in_executor(
            self._executor, lambda: parse_archive(package_id, archive_bytes)
        )
        self._package_lookup.add_archive(archive)
        return archive.package

    @staticmethod
    async def __fetch_package_bytes(
        conn: PackageService,
        package_id: PackageRef,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> bytes:
        sleep_interval = 1

        while True:
            # noinspection PyBroadException
            try:
                return await conn.get_package(package_id, token=token)
            except Exception:
                # We tried fetching the package but got an error. Retry, backing off to waiting as
                # much as 30 seconds between each attempt.
                await sleep(sleep_interval)
                sleep_interval = min(sleep_interval * 2, 30)
                LOG.exception("Failed to fetch package; this will be retried.")

    async def load_all(self, *, token: Optional[TokenOrTokenProvider] = None) -> None:
        """
        Load all packages from the remote server.
        """
        conn = self._conn
        if conn is None:
            raise DazlError("a connection is not configured")

        package_ids = set(await conn.list_package_ids(token=token))
        package_ids -= self._package_lookup.package_ids()
        if package_ids:
            await gather(*(self.load(package_id, token=token) for package_id in package_ids))

        return None
