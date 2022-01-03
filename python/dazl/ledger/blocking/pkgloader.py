# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from concurrent.futures import Future, ThreadPoolExecutor
from datetime import timedelta
import threading
from time import sleep
from typing import Callable, Dict, Optional, TypeVar

from . import PackageService
from ... import LOG
from ...damlast.daml_lf_1 import Package, PackageRef
from ...damlast.errors import PackageNotFoundError
from ...damlast.lookup import STAR, MultiPackageLookup, PackageExceptionTracker
from ...damlast.parse import parse_archive
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
        self._lock = threading.RLock()
        self._futures = dict()  # type: Dict[PackageRef, Future[Package]]
        self._executor = executor or ThreadPoolExecutor(3)

    def set_connection(self, conn: "Optional[PackageService]"):
        self._conn = conn

    def do_with_retry(self, fn: "Callable[[], T]") -> "T":
        """
        Perform a synchronous action that assumes the existence of one or more packages. In the
        event the function raises :class:`PackageNotFoundError` or a wildcarded
        :class:`NameNotFoundError`, the required package/type is fetched and the operation retried.

        If, after a retry, an expected package or type could not be found, the exception is
        re-raised to the caller.

        :param fn: A function to invoke.
        :return: The result of that function.
        """
        guard = PackageExceptionTracker()
        while True:
            pkg_ref = guard.pop_package()
            while pkg_ref is not None:
                self.load(pkg_ref)
                pkg_ref = guard.pop_package()

            with guard:
                return fn()

    def load(self, ref: "PackageRef") -> "Optional[Package]":
        """
        Load a package ID from the remote server. If the package has additional dependencies, they
        are also loaded.

        :param ref: One or more :class:`PackageRef`s.
        :raises: PackageNotFoundError if the package could not be resolved
        """
        if ref == STAR:
            # I'd prefer `return self.load_all()`, but https://github.com/python/mypy/issues/6549
            # was closed as "not a bug, won't fix"
            self.load_all()
            return None

        # If the package has already been loaded, then skip all the expensive I/O stuff
        try:
            return self._package_lookup.package(ref)
        except PackageNotFoundError:
            pass

        # If we already have a request in-flight, simply return that same Future to our caller;
        # do not try to schedule a new request
        with self._lock:
            fut = self._futures.get(ref)
            if fut is None:
                fut = self._executor.submit(self._load, ref)
                self._futures[ref] = fut

        package = fut.result()

        with self._lock:
            _ = self._futures.pop(ref, None)

        return package

    def _load(self, package_id: "PackageRef") -> "Package":
        LOG.info("Loading package: %s", package_id)

        conn = self._conn
        if conn is None:
            raise DazlError("a connection is not configured")

        archive_bytes = self.__fetch_package_bytes(conn, package_id)

        LOG.info("Loaded for package: %s, %d bytes", package_id, len(archive_bytes))

        archive = parse_archive(package_id, archive_bytes)
        self._package_lookup.add_archive(archive)
        return archive.package

    @staticmethod
    def __fetch_package_bytes(conn: "PackageService", package_id: "PackageRef") -> bytes:
        sleep_interval = 1

        while True:
            # noinspection PyBroadException
            try:
                return conn.get_package(package_id)
            except Exception:
                # We tried fetching the package but got an error. Retry, backing off to waiting as
                # much as 30 seconds between each attempt.
                sleep(sleep_interval)
                sleep_interval = min(sleep_interval * 2, 30)
                LOG.exception("Failed to fetch package; this will be retried.")

    def load_all(self) -> None:
        """
        Load all packages from the remote server.
        """
        conn = self._conn
        if conn is None:
            raise DazlError("a connection is not configured")

        package_ids = set(conn.list_package_ids()) - self._package_lookup.package_ids()

        # wait for the Futures for all missing packages to be resolved, and then return
        futs = []
        with self._lock:
            for ref in package_ids:
                fut = self._futures.get(ref)
                if fut is None:
                    fut = self._executor.submit(self._load, ref)
                    self._futures[ref] = fut
                futs.append(fut)

        # wait for all interesting Futures to be complete
        for fut in futs:
            fut.result()

        return None
