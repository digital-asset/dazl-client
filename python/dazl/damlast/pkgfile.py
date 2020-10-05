# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import BytesIO
from os import PathLike
from pathlib import Path
from typing import AbstractSet, BinaryIO, Collection, Generator, Mapping, Optional, Union
from zipfile import ZipFile

from .daml_lf_1 import Archive, Package, PackageRef
from .parse import parse_archive

from .._gen.com.daml.daml_lf_dev import daml_lf_pb2 as pb

# Wherever the API expects a DAR, we can take a file path, `bytes`, or a byte buffer.
Dar = Union[bytes, str, Path, BinaryIO]

__all__ = ['Dar', 'DarFile', 'CachedDarFile', 'get_dar_package_ids']


class DarFile:
    """
    Provides access to the contents of a .dar file.

    This conforms to the :class:`PackageProvider` protocol.

    This class is _not_ thread-safe.
    """

    def __init__(self, dar: 'Dar'):
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

        elif hasattr(dar, 'read'):
            # file-like object (buffers, files, etc.)
            self.filename = None
            self._buf = None
            self._zip = ZipFile(dar)

        else:
            raise TypeError('DarFile only understands file paths or binary blobs')

    def __enter__(self) -> 'DarFile':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._zip.close()
        if self._buf is not None:
            self._buf.close()

    def manifest(self) -> 'Optional[Mapping[str, str]]':
        """
        Return the contents of the manifest of this DAR.
        """
        names = self._zip.namelist()
        if 'META-INF/MANIFEST.MF' in names:
            manifest_bytes = self._zip.read('META-INF/MANIFEST.MF')
            manifest = {}
            for line in manifest_bytes.decode('utf-8').splitlines():
                name, _, value = line.partition(':')
                manifest[name] = value.strip()
            return manifest
        else:
            return None

    def sdk_version(self) -> 'Optional[str]':
        """
        Return the SDK version used to compile this dar (if this information is available).
        """
        manifest = self.manifest()
        return manifest.get('Sdk-Version') if manifest is not None else None

    def archives(self) -> 'Collection[Archive]':
        """
        Return :class:`Archive` instances from this :class:`DarFile`.

        :class:`CachedDarFile` is a better choice than `DarFile` if this method is frequently called
        on the same :class:`DarFile`, as package parsing is an expensive operation.
        """
        return [parse_archive(a.hash, a.payload) for a in self._pb_archives()]

    def package(self, package_id: 'PackageRef') -> 'Package':
        """
        Return the :class:`Package` corresponding to the specified :class:`PackageRef`.

        This function is somewhat inefficient as it must check every DALF for the specified package
        ID. The :method:`DarFile.archives` function should be used if it is known that all archives
        in a DAR are to be accessed, or use a :class:`CachedDarFile` instance if random access of
        packages by package ID are needed.
        """
        for a in self._pb_archives():
            if a.hash == package_id:
                return parse_archive(a.hash, a.payload).package

    def package_ids(self) -> 'AbstractSet[PackageRef]':
        """
        Return the set of package IDs from this DAR.
        """
        return frozenset(a.hash for a in self._pb_archives())

    def _dalf_names(self) -> 'Generator[str, None, None]':
        """
        Return a generator over the names of DALF files in this DarFile.
        """
        return (name for name in self._zip.namelist() if name.endswith('.dalf'))

    def _pb_archives(self) -> 'Generator[pb.Archive, None, None]':
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

    def __init__(self, dar: 'Dar'):
        self._dar = dar
        from threading import Lock
        self._lock = Lock()
        self._archives = None

    def archives(self) -> 'Collection[Archive]':
        if self._archives is None:
            with self._lock:
                if self._archives is None:
                    with DarFile(self._dar) as dar:
                        self._archives = dar.archives()
        return self._archives

    def package(self, package_id: 'PackageRef') -> 'Package':
        # TODO: This import needs to be local as long as the dazl.util.dar module still exists
        #  to avoid import cycles. Move this to the top of the file when dazl.util.dar is removed.
        from .errors import PackageNotFoundError

        for archive in self.archives():
            if archive.hash == package_id:
                return archive.package

        raise PackageNotFoundError(package_id)

    def package_ids(self) -> 'AbstractSet[PackageRef]':
        return frozenset([archive.hash for archive in self.archives()])


def get_dar_package_ids(dar: 'Dar') -> 'AbstractSet[PackageRef]':
    """
    Return the package IDs for a DAR.
    """
    with DarFile(dar) as dar_file:
        return dar_file.package_ids()
