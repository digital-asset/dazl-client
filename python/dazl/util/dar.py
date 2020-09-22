# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from io import BytesIO
from os import path
from pathlib import Path
from typing import Dict, Collection, Mapping, Optional, Sequence, TYPE_CHECKING
from zipfile import ZipFile

from ..util.path_util import pathify

if TYPE_CHECKING:
    from ..model.core import Dar
    from ..model.types import PackageId, PackageIdSet
    from ..model.types_store import PackageStore, PackageProvider


def get_archives(contents: bytes) -> 'Mapping[str, bytes]':
    """
    Attempt to parse the specified contents as either a DALF or a DAR, and return a mapping of
    package IDs to DALF bytes.

    :param contents: A byte array to attempt to parse.
    :return: Return a mapping from package ID to byte contents.
    """
    if contents[0:4] == b'PK\03\04':
        with BytesIO(contents) as buf:
            with DarFile(buf) as dar:
                return dar.get_archives()
    else:
        # parse as a single DALF
        from ..protocols.v1.pb_parse_metadata import parse_archive_payload
        a = parse_archive_payload(contents)
        return {a.hash: contents}


class DarFile:
    """
    Provides access to the contents of a .dar file.
    """
    def __init__(self, dar: 'Dar'):
        if isinstance(dar, (str, Path)):
            self._buf = None
            self.dar_path = pathify(dar)
            self.dar_contents = ZipFile(str(self.dar_path))
        elif isinstance(dar, bytes):
            self._buf = BytesIO(dar)
            self.dar_path = None
            self.dar_contents = ZipFile(self._buf)
        else:
            self._buf = None
            self.dar_path = None
            self.dar_contents = ZipFile(dar)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._buf is not None:
            self._buf.close()
        self.close()

    def close(self):
        self.dar_contents.close()

    def read_metadata(self) -> 'PackageStore':
        from ..model.types_store import PackageStore
        store = PackageStore.empty()
        dalf_names = self.get_dalf_names()
        for dalf_name in dalf_names:
            contents = self.dar_contents.read(dalf_name)
            store.register_all(parse_dalf(contents))
        return store

    def get_archives(self) -> 'Mapping[str, bytes]':
        """
        Return a mapping from package ID to byte contents.
        """
        from ..protocols.v1.pb_parse_metadata import parse_archive_payload
        archives = {}  # type: Dict[str, bytes]
        for dalf_name in self.get_dalf_names():
            contents = self.dar_contents.read(dalf_name)
            payload = parse_archive_payload(contents)
            archives[payload.hash] = contents
        return archives

    def get_dalf_names(self) -> 'Sequence[str]':
        dalf_names = []
        for name in self.dar_contents.namelist():
            _, ext = path.splitext(name)
            if ext == '.dalf':
                dalf_names.append(name)
        return dalf_names

    def get_manifest(self) -> 'Optional[Mapping[str, str]]':
        """
        Return the contents of the manifest of this DAR.
        :return:
        """
        names = self.dar_contents.namelist()
        if 'META-INF/MANIFEST.MF' in names:
            manifest_bytes = self.dar_contents.read('META-INF/MANIFEST.MF')
            manifest = {}
            for line in manifest_bytes.decode('utf-8').splitlines():
                print(line)
                name, _, value = line.partition(':')
                manifest[name] = value.strip()
            return manifest
        else:
            return None

    def get_sdk_version(self) -> 'Optional[str]':
        """
        Return the SDK version used to compile this dar (if this information is available).
        """
        manifest = self.get_manifest()
        return manifest.get('Sdk-Version') if manifest is not None else None

    def get_package_ids(self) -> 'PackageIdSet':
        """
        Return the set of package IDs from this DAR.
        """
        # In order to make this call perform more quickly, we read the Archive object, but not any
        # of its contents.
        package_ids = set()
        for dalf_name in self.get_dalf_names():
            from ..model.types import PackageId
            from .._gen.com.daml.daml_lf_dev.daml_lf_pb2 import Archive

            contents = self.dar_contents.read(dalf_name)

            a = Archive()
            a.ParseFromString(contents)

            package_ids.add(PackageId(a.hash))

        return frozenset(package_ids)

    def get_package_provider(self) -> 'PackageProvider':
        from typing import Dict
        from ..model.types_store import MemoryPackageProvider
        from ..damlast.daml_lf_1 import PackageRef
        from .._gen.com.daml.daml_lf_dev.daml_lf_pb2 import Archive

        packages = {}  # type: Dict[PackageRef, bytes]
        dalf_names = self.get_dalf_names()
        for dalf_name in dalf_names:
            contents = self.dar_contents.read(dalf_name)

            a = Archive()
            a.ParseFromString(contents)

            packages[a.hash] = a.payload

        return MemoryPackageProvider(packages)


def parse_dalf(contents: bytes) -> 'PackageStore':
    from .._gen.com.daml.daml_lf_dev.daml_lf_pb2 import Archive
    from ..protocols.v1.pb_parse_metadata import parse_archive_payload, parse_daml_metadata_pb
    a = Archive()
    a.ParseFromString(contents)
    p = parse_archive_payload(a.payload)
    return parse_daml_metadata_pb(a.hash, p)


def get_dar_package_ids(dar: 'Dar') -> 'Collection[PackageId]':
    with DarFile(dar) as dar_file:
        return dar_file.get_package_ids()


class DamlcPackageError(Exception):
    """
    Raised when DAMLC fails to compile a DAR.
    """
    def __init__(self, exit_code):
        self.exit_code = exit_code
