# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import BytesIO
from os import PathLike
from pathlib import Path
import threading
from typing import AbstractSet, BinaryIO, Collection, Generator, Mapping, Optional, Union
import warnings
from zipfile import ZipFile

from .._gen.com.daml.daml_lf_1_15 import daml_lf_pb2 as pb
from ..prim import TimeDeltaLike
from .daml_lf_1 import Archive, Package, PackageRef
from .parse import parse_archive

# Wherever the API expects a DAR, we can take a file path, `bytes`, or a byte buffer.
Dar = Union[bytes, str, Path, BinaryIO]

__all__ = ["Dar", "DarFile", "CachedDarFile", "get_dar_package_ids"]


class DarFile:
    """
    Provides access to the contents of a .dar file.

    This conforms to the :class:`PackageProvider` protocol.

    This class is _not_ thread-safe.
    """

    filename: Optional[str]

    def __init__(self, dar: "Dar"):
        """
        Initialize a new DarFile.

        :param dar:
            A path to a file (either expressed as str or pathlib.Path), a bytes blob, or a buffer.
        """
        if isinstance(dar, str):
            self.filename = dar
            self._buf = None
            self._zip = ZipFile(self.filename)

        elif isinstance(dar, PathLike):
            self.filename = dar.__fspath__()
            self._buf = None
            self._zip = ZipFile(self.filename)

        elif isinstance(dar, bytes):
            self.filename = None
            self._buf = BytesIO(dar)
            self._zip = ZipFile(self._buf)

        elif hasattr(dar, "read"):
            # file-like object (buffers, files, etc.)
            self.filename = None
            self._buf = None
            self._zip = ZipFile(dar)

        else:
            raise TypeError("DarFile only understands file paths or binary blobs")

    def __enter__(self) -> "DarFile":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._zip.close()
        if self._buf is not None:
            self._buf.close()

    def manifest(self) -> "Optional[Mapping[str, str]]":
        """
        Return the contents of the manifest of this DAR.
        """
        names = self._zip.namelist()
        if "META-INF/MANIFEST.MF" in names:
            manifest_bytes = self._zip.read("META-INF/MANIFEST.MF")
            manifest = {}
            for line in manifest_bytes.decode("utf-8").splitlines():
                name, _, value = line.partition(":")
                manifest[name] = value.strip()
            return manifest
        else:
            return None

    def sdk_version(self) -> "Optional[str]":
        """
        Return the SDK version used to compile this dar (if this information is available).
        """
        manifest = self.manifest()
        return manifest.get("Sdk-Version") if manifest is not None else None

    def archives(self) -> "Collection[Archive]":
        """
        Return :class:`Archive` instances from this :class:`DarFile`.

        :class:`CachedDarFile` is a better choice than `DarFile` if this method is frequently called
        on the same :class:`DarFile`, as package parsing is an expensive operation.
        """
        return [parse_archive(PackageRef(a.hash), a.payload) for a in self._pb_archives()]

    def package(self, package_id: "PackageRef") -> "Package":
        """
        Return the :class:`Package` corresponding to the specified :class:`PackageRef`.

        This function is somewhat inefficient as it must check every DALF for the specified package
        ID. The :method:`DarFile.archives` function should be used if it is known that all archives
        in a DAR are to be accessed, or use a :class:`CachedDarFile` instance if random access of
        packages by package ID are needed.
        """
        payload = self.package_bytes(package_id)
        return parse_archive(package_id, payload).package

    def package_bytes(self, package_id: "PackageRef") -> bytes:
        """
        Return bytes corresponding to the specified :class:`PackageRef`. If this DAR were to be
        uploaded to a ledger, these are the bytes that would be returned for the specified
        :class:`PackageRef`.

        Note that this NOT the same as simply returning a ``.dalf`` file within a DAR, because a
        ``.dalf`` contains an envelope in the form of ``ArchivePayload`` messages, and it is the
        _contents_ of this message that are persisted by Ledger API implementations.
        """
        for a in self._pb_archives():
            if a.hash == package_id:
                return a.payload

        # We do not raise PackageNotFoundError here (even though it seems like it would be a more
        # apt error) because PackageNotFoundError implies the operation is retryable
        raise Exception(f"package not found in a DAR: {package_id!r}")

    def package_ids(self) -> "AbstractSet[PackageRef]":
        """
        Return the set of package IDs from this DAR.
        """
        return frozenset(PackageRef(a.hash) for a in self._pb_archives())

    def async_package_service(self) -> "DarFileAsyncPackageService":
        """
        Return an implementation of :class:`dazl.ledger.aio.PackageService` that is backed by
        the contents of this :class:`DarFile`.
        """
        return DarFileAsyncPackageService(self)

    def blocking_package_service(self) -> "DarFileBlockingPackageService":
        """
        Return an implementation of :class:`dazl.ledger.blocking.PackageService` that is backed by
        the contents of this :class:`DarFile`.

        The returned service is thread-safe as long as this :class:`DarFile` is not accessed
        concurrently by other processes.
        """
        return DarFileBlockingPackageService(self)

    async def get_package(self, package_id: "PackageRef") -> bytes:
        """
        This method is deprecated; use :meth:`DarFile.async_package_service` instead.
        """
        warnings.warn(
            "DarFile.get_package is deprecated; use DarFile.async_package_service.get_package instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.package_bytes(package_id)

    async def list_package_ids(self):
        """
        This method is deprecated; use :meth:`DarFile.async_package_service` instead.
        """
        warnings.warn(
            "DarFile.list_package_ids is deprecated; use DarFile.async_package_service.list_package_ids instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.package_ids()

    def _dalf_names(self) -> "Generator[PackageRef, None, None]":
        """
        Return a generator over the names of DALF files in this DarFile.
        """
        return (PackageRef(name) for name in self._zip.namelist() if name.endswith(".dalf"))

    def _pb_archives(self) -> "Generator[pb.Archive, None, None]":
        """
        Return a generator over :class:`pb.Archive` instances. Crucially, the Protobuf messages
        contain DAML-LF as a ``bytes`` field that has not yet been parsed.
        """
        for name in self._dalf_names():
            contents = self._zip.read(name)

            a = pb.Archive()
            a.ParseFromString(contents)
            yield a


class CachedDarFile:
    """
    A caching variation of :class:`DarFile`.

    :class:`CachedDarFile` tries to do disk operations only once, and hold onto their results in
    memory. This will generally improve performance at the expense of increased memory usage.
    """

    def __init__(self, dar: "Dar"):
        self._dar = dar
        from threading import Lock

        self._lock = Lock()
        self._archives = None  # type: Optional[Collection[Archive]]

    def archives(self) -> "Collection[Archive]":
        if self._archives is None:
            with self._lock:
                if self._archives is None:
                    with DarFile(self._dar) as dar:
                        self._archives = dar.archives()
        return self._archives

    def package(self, package_id: "PackageRef") -> "Package":
        # TODO: This import needs to be local as long as the dazl.util.dar module still exists
        #  to avoid import cycles. Move this to the top of the file when dazl.util.dar is removed.
        from .errors import PackageNotFoundError

        for archive in self.archives():
            if archive.hash == package_id:
                return archive.package

        raise PackageNotFoundError(package_id)

    def package_ids(self) -> "AbstractSet[PackageRef]":
        return frozenset([archive.hash for archive in self.archives()])


def get_dar_package_ids(dar: "Dar") -> "AbstractSet[PackageRef]":
    """
    Return the package IDs for a DAR.
    """
    with DarFile(dar) as dar_file:
        return dar_file.package_ids()


class DarFileAsyncPackageService:
    def __init__(self, __dar_file: "DarFile"):
        self._dar_file = __dar_file

    async def get_package(
        self, package_id: "PackageRef", timeout: Optional[TimeDeltaLike] = None
    ) -> bytes:
        return self._dar_file.package_bytes(package_id)

    async def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = None
    ) -> "AbstractSet[PackageRef]":
        return self._dar_file.package_ids()


class DarFileBlockingPackageService:
    def __init__(self, __dar_file: "DarFile"):
        self._dar_file = __dar_file
        self._lock = threading.RLock()

    def get_package(
        self, package_id: PackageRef, *, timeout: Optional[TimeDeltaLike] = None
    ) -> bytes:
        with self._lock:
            return self._dar_file.package_bytes(package_id)

    def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = None
    ) -> AbstractSet[PackageRef]:
        with self._lock:
            return self._dar_file.package_ids()
