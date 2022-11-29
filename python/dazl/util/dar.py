# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import BytesIO
from typing import TYPE_CHECKING, AbstractSet, Collection, Mapping, Optional, Sequence
import warnings

from ..damlast.daml_lf_1 import PackageRef
from ..damlast.parse import parse_archive
from ..damlast.pkgfile import Dar, DarFile as _DarFile

if TYPE_CHECKING:
    from ..model.types_store import PackageProvider, PackageStore


def get_archives(contents: bytes) -> "Mapping[PackageRef, bytes]":
    """
    Attempt to parse the specified contents as either a DALF or a DAR, and return a mapping of
    package IDs to DALF bytes.
    This class is deprecated as it assumes and expose use of a :class:`PackageStore` and

    :class:`Type`, all of which are deprecated.

    :param contents: A byte array to attempt to parse.
    :return: Return a mapping from package ID to byte contents.
    """
    warnings.warn(
        "get_archives is deprecated. For DAR parsing, use dazl.damlast.DarFile instead. "
        "There is no replacement for DALF parsing.",
        DeprecationWarning,
        stacklevel=2,
    )

    if contents[0:4] == b"PK\03\04":
        with BytesIO(contents) as buf:
            with _DarFile(buf) as dar:
                # noinspection PyProtectedMember
                return {name: dar._zip.read(name) for name in dar._dalf_names()}

    raise Exception(
        "get_archives(...) only works on DAR files, and is additionally deprecated. "
        "Use dazl.damlast.DarFile instead."
    )


class DarFile(_DarFile):
    """
    Provides access to the contents of a .dar file.
    """

    def __init__(self, dar: "Dar"):
        super().__init__(dar)
        warnings.warn(
            "dazl.util.dar.DarFile is deprecated; please use dazl.damlast.DarFile instead.",
            DeprecationWarning,
            stacklevel=2,
        )

    def read_metadata(self) -> "PackageStore":
        warnings.warn(
            "read_metadata is deprecated. For DAR parsing, use dazl.damlast.DarFile instead. "
            "There is no replacement for DALF parsing.",
            DeprecationWarning,
            stacklevel=2,
        )
        # noinspection PyProtectedMember
        from ..model.types_store import PackageStore
        from ..protocols.v1.pb_parse_metadata import _parse_daml_metadata_pb

        store = PackageStore.empty()

        for archive in self.archives():
            store.register_all(_parse_daml_metadata_pb(archive))
        return store

    def get_archives(self) -> "Mapping[PackageRef, bytes]":
        """
        Return a mapping from package ID to byte contents.
        """
        warnings.warn(
            "get_archives is deprecated; there is no replacement.", DeprecationWarning, stacklevel=2
        )
        return {PackageRef(a.hash): a.payload for a in self._pb_archives()}

    def get_dalf_names(self) -> "Sequence[PackageRef]":
        warnings.warn(
            "get_dalf_names is deprecated; there is no replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        return list(self._dalf_names())

    def get_manifest(self) -> "Optional[Mapping[str, str]]":
        """
        Return the contents of the manifest of this DAR.
        """
        warnings.warn(
            "get_manifest() is deprecated; use manifest() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.manifest()

    def get_sdk_version(self) -> "Optional[str]":
        """
        Return the SDK version used to compile this dar (if this information is available).

        This method is deprecated; use dazl.damlast..DarFile
        """
        warnings.warn(
            "get_sdk_version() is deprecated; use sdk_versions() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.sdk_version()

    def get_package_ids(self) -> "AbstractSet[PackageRef]":
        """
        Return the set of package IDs from this DAR.
        """
        warnings.warn(
            "get_package_ids() is deprecated; please use package_ids() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.package_ids()

    def get_package_provider(self) -> "PackageProvider":
        warnings.warn(
            "get_package_provider() is deprecated; use the methods of the "
            "dazl.damlast.PackageProvider protocol as implemented on DarFile directly.",
            DeprecationWarning,
        )
        from ..model.types_store import MemoryPackageProvider

        return MemoryPackageProvider(self.get_archives())


def parse_dalf(contents: bytes) -> "PackageStore":
    warnings.warn(
        "parse_dalf is deprecated, as PackageStore and Type are deprecated.",
        DeprecationWarning,
        stacklevel=2,
    )
    # noinspection PyProtectedMember
    from .._gen.com.daml.daml_lf_1_15.daml_lf_pb2 import Archive
    from ..protocols.v1.pb_parse_metadata import _parse_daml_metadata_pb

    a = Archive()
    a.ParseFromString(contents)
    return _parse_daml_metadata_pb(parse_archive(PackageRef(a.hash), a.payload))


def get_dar_package_ids(dar: "Dar") -> "Collection[PackageRef]":
    warnings.warn(
        "dazl.util.dar.get_dar_package_ids is deprecated; "
        "please use dazl.damlast.get_dar_package_ids instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    # This is a local import to get around circular dependencies; also the replacement function
    # is the same name as our own
    from ..damlast.pkgfile import get_dar_package_ids

    return get_dar_package_ids(dar)
