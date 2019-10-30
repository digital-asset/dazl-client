# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from io import BytesIO
from os import path
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import BinaryIO, Dict, Collection, Mapping, Optional, Sequence, Union, TYPE_CHECKING
from zipfile import ZipFile

from .process import ProcessWatcher
from ..util.path_util import pathify

if TYPE_CHECKING:
    from ..model.types_store import PackageStore, PackageProvider


def build_dar(
        daml_path: 'Union[str, Path]',
        dar_path: 'Union[str, Path]',
        damlc_component: 'Optional[str]' = None,
        damlc_extra_args: 'Sequence[str]' = None,
        allow_caching: bool = False) -> bool:
    """
    Create a .dar file from a .daml file.

    :param daml_path: Path to the DAML file.
    :param dar_path: Path to the DAR file to create.
    :param damlc_component: Version of the DAML compiler to use.
    :param damlc_extra_args: Extra arguments of damlc.
    :param allow_caching:
        ``True`` if timestamps should be checked to see if a DAR actually needs to be built;
        otherwise ``False`` to always force compilation.
    :return:
        ``True`` if a DAR was created; ``False`` if compilation was skipped.
    """
    daml_path = Path(daml_path)
    dar_path = Path(dar_path)

    if not daml_path.exists():
        raise FileNotFoundError(str(daml_path))

    if allow_caching and dar_path.exists():
        if daml_path.lstat().st_mtime < dar_path.lstat().st_mtime:
            return False

    from ..damlsdk.package import package, PackageOptions
    options = PackageOptions([str(daml_path)], dar_path, damlc_extra_args)
    proc_opts = package(options, component=damlc_component)
    with ProcessWatcher(proc_opts) as pw:
        code = pw.run()

    # the daml compiler spits out .hi and .hie files next to source, and there is currently no way
    # to suppress this behavior
    try:
        daml_path.with_suffix('.hi').unlink()
    except FileNotFoundError:
        pass
    try:
        daml_path.with_suffix('.hie').unlink()
    except FileNotFoundError:
        pass

    if code != 0:
        raise DamlcPackageError(code)
    return True


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


class TemporaryDar:
    """
    Wrapper that creates a .dar file from .daml files that is only present on the file system
    during the scope of this object.
    """
    __slots__ = ('daml_path', 'dar_paths', 'damlc_component', '_tmp_dir', 'damlc_extra_args')

    daml_path: 'Path'
    dar_paths: 'Optional[Sequence[Path]]'
    damlc_component: 'Optional[str]'
    _tmp_dir: 'TemporaryDirectory'
    damlc_extra_args: 'Sequence[str]'

    def __init__(self, daml_path: Union[str, Path], damlc_component: Optional[str] = None, damlc_extra_args=None):
        self.daml_path = pathify(daml_path)
        self.dar_paths = None
        self.damlc_component = damlc_component
        self._tmp_dir = TemporaryDirectory()
        self.damlc_extra_args = damlc_extra_args

    def store(self) -> 'PackageStore':
        from .dar_repo import LocalDarRepository
        repo = LocalDarRepository()
        repo.add_source(*self.ensure_dar())
        return repo.store

    def ensure_dar(self) -> 'Sequence[Path]':
        if self.dar_paths is None:
            dar_path = path.join(self._tmp_dir.name, 'file.dar')
            build_dar(self.daml_path, dar_path, damlc_component=self.damlc_component,
                      damlc_extra_args=self.damlc_extra_args)
            from os import listdir
            self.dar_paths = [Path(path.join(self._tmp_dir.name, o)) for o in listdir(self._tmp_dir.name)]

        return self.dar_paths

    def __enter__(self) -> 'Sequence[Path]':
        return self.ensure_dar()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

    def cleanup(self) -> None:
        if self._tmp_dir is not None:
            self._tmp_dir.cleanup()
            self._tmp_dir = None


class DarFile:
    """
    Provides access to the contents of a .dar file.
    """
    def __init__(self, dar_path: 'Union[str, Path, BinaryIO]'):
        if isinstance(dar_path, (str, Path)):
            self.dar_path = pathify(dar_path)
            self.dar_contents = ZipFile(str(self.dar_path))
        else:
            self.dar_path = None
            self.dar_contents = ZipFile(dar_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
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

    def get_package_provider(self) -> 'PackageProvider':
        from typing import Dict
        from ..model.types_store import MemoryPackageProvider
        from .._gen.com.digitalasset.daml_lf_dev.daml_lf_pb2 import Archive

        packages = {}  # type: Dict[str, bytes]
        dalf_names = self.get_dalf_names()
        for dalf_name in dalf_names:
            contents = self.dar_contents.read(dalf_name)

            a = Archive()
            a.ParseFromString(contents)

            packages[a.hash] = a.payload

        return MemoryPackageProvider(packages)


def parse_dalf(contents: bytes) -> 'PackageStore':
    from .._gen.com.digitalasset.daml_lf_dev.daml_lf_pb2 import Archive
    from ..protocols.v1.pb_parse_metadata import parse_archive_payload, parse_daml_metadata_pb
    a = Archive()
    a.ParseFromString(contents)
    p = parse_archive_payload(a.payload)
    return parse_daml_metadata_pb(a.hash, p)


def get_dar_package_ids(contents: bytes) -> 'Collection[str]':
    with BytesIO(contents) as buf:
        with DarFile(buf) as dar:
            return dar.read_metadata().package_ids()


class DamlcPackageError(Exception):
    """
    Raised when DAMLC fails to compile a DAR.
    """
    def __init__(self, exit_code):
        self.exit_code = exit_code
