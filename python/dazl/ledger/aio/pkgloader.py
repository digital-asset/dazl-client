# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import ensure_future, gather, get_event_loop, sleep, wait_for
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from typing import Awaitable, Callable, Dict, Optional, Set, TypeVar
import warnings

from . import PackageService
from ... import LOG
from ...damlast.daml_lf_1 import Archive, Package, PackageRef
from ...damlast.errors import NameNotFoundError, PackageNotFoundError
from ...damlast.lookup import MultiPackageLookup, validate_template
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
        self._loading_futs = dict()  # type: Dict[PackageRef, Awaitable[Package]]
        self._parsing_futs = dict()  # type: Dict[PackageRef, Awaitable[Archive]]
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
        failed_types = set()  # type: Set[str]
        failed_packages = set()  # type: Set[PackageRef]
        while True:
            try:
                return fn()

            except PackageNotFoundError as ex:
                # every time we fail serialization due to a missing package or type,
                # try to resolve it; remember what we tried, because if we fail again
                # for the same reason it is likely fatal
                if ex.ref in failed_packages:
                    # we already looked for this package and couldn't find it; this will
                    # never succeed
                    raise
                failed_packages.add(ex.ref)
                await self.load(ex.ref)

            except NameNotFoundError as ex:
                if ex.ref in failed_types:
                    # we already looked for this type and couldn't find it; this will
                    # never succeed
                    LOG.verbose(
                        "Failed to find name %s in all known packages, "
                        "even after fetching the latest.",
                        ex.ref,
                    )
                    raise

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", DeprecationWarning)
                    pkg_id, name = validate_template(
                        ex.ref, allow_deprecated_identifiers=self._allow_deprecated_identifiers
                    )
                if pkg_id == "*":
                    # we don't know what package contains this type, so we have no
                    # choice but to look in all known packages
                    LOG.verbose(
                        "Failed to find name %s in all known packages, "
                        "so loading ALL packages...",
                        name,
                    )
                    failed_types.add(ex.ref)
                    await self.load_all()
                else:
                    # we know what package this type comes from, but it did not contain
                    # the required type
                    LOG.warning("Found package %s, but it did not include type %s", pkg_id, name)
                    raise

    async def preload(self, *contents: "Dar") -> None:
        """
        Populate a :class:`PackageCache` with types from DARs.

        :param contents:
            One or more DARs to load into a local package cache.
        """

    async def load(self, ref: "PackageRef") -> "Package":
        """
        Load a package ID from the remote server. If the package has additional dependencies, they
        are also loaded.

        :param ref: One or more :class:`PackageRef`s.
        :raises: PackageNotFoundError if the package could not be resolved
        """
        # If the package has already been loaded, then skip all the expensive I/O stuff
        try:
            return self._package_lookup.package(ref)
        except PackageNotFoundError:
            pass

        # If we already have a request in-flight, simply return that same Future to our caller;
        # do not try to schedule a new request
        fut = self._loading_futs.get(ref)
        if fut is None:
            fut = ensure_future(self._load_and_parse_package(ref))
            self._loading_futs[ref] = fut
        package = await fut

        _ = self._loading_futs.pop(ref, None)
        _ = self._parsing_futs.pop(ref, None)

        return package

    async def _load_and_parse_package(self, package_id: "PackageRef") -> "Package":
        LOG.info("Loading package: %s", package_id)

        loop = get_event_loop()
        conn = self._conn
        if conn is None:
            raise DazlError("a connection is not configured")

        archive_bytes = await wait_for(
            self.__fetch_package_bytes(conn, package_id), timeout=self._timeout.total_seconds()
        )

        LOG.info("Loaded for package: %s, %d bytes", package_id, len(archive_bytes))

        # we only ever want a package to be parsed once; it could be that there were multiple
        # attempts to load a package in flight (though this shouldn't happen either)
        fut = self._parsing_futs.get(package_id)
        if fut is None:
            fut = ensure_future(
                loop.run_in_executor(
                    self._executor, lambda: parse_archive(package_id, archive_bytes)
                )
            )
            self._parsing_futs[package_id] = fut

        archive = await fut
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

    async def load_all(self):
        """
        Load all packages from the remote server.
        """
        package_ids = set(await self._conn.list_package_ids())
        package_ids -= self._package_lookup.package_ids()
        if package_ids:
            await gather(*(self.load(package_id) for package_id in package_ids))
