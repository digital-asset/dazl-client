#!/usr/bin/env python3
# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Utilities for working with Daml Connect.
#
# This script has no external dependencies and can run in Python 3.8+.

from __future__ import annotations

from argparse import ArgumentParser
from dataclasses import dataclass
import io
import os
from pathlib import Path
import re
from typing import (
    Collection,
    Final,
    Iterator,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Set,
    TextIO,
    Union,
)
from urllib.request import urlretrieve

__all__ = ["Protos"]

from zipfile import ZipFile

root_dir = Path(__file__).absolute().parent.parent.parent
default_cache_dir = root_dir / ".cache"

replace_ext = re.compile("\.proto$")

PROTOS_CACHE_DIR: Final = ".cache"
GO_GENERATED_ROOT: Final = "go/api"
PYTHON_GENERATED_ROOT: Final = "python/dazl/_gen"


# region Data Types


@dataclass(frozen=True)
class ProtobufManifest:
    version: str
    entries: Sequence[ProtobufManifestEntry]

    def dir_entries(self) -> Iterator[ProtobufManifestDir]:
        for entry in self.entries:
            if isinstance(entry, ProtobufManifestDir):
                yield entry

    def file_entries(
        self, source: Literal[None, "canton", "daml"] = None
    ) -> Iterator[ProtobufManifestFile]:
        for entry in self.entries:
            if isinstance(entry, ProtobufManifestFile):
                if source is None or source == entry.source:
                    yield entry


@dataclass(frozen=True)
class ProtobufManifestDir:
    path: str

    def __str__(self):
        return f"dir {self.path}"


@dataclass(frozen=True)
class ProtobufManifestFile:
    file_type: Literal["pb", "grpc"]
    source: Literal["canton", "daml"]
    path: str

    def __str__(self) -> str:
        return f"file {self.file_type} {self.source} {self.path}"


ProtobufManifestEntry = Union[ProtobufManifestDir, ProtobufManifestFile]


# endregion


class ProtobufArchives:
    def __init__(self, version: str, canton_zip: Path, daml_zip: Path):
        self.canton_zip = ZipFile(canton_zip)
        self.daml_zip = ZipFile(daml_zip)
        self.manifest = manifest_from_zip_files(version, self.canton_zip, self.daml_zip)
        self.canton_files = canton_proto_files(self.canton_zip.namelist())
        self.daml_files = daml_proto_files(self.daml_zip.namelist())

        for k, v in self.canton_files.items():
            print(k, " -> ", v)
        for k, v in self.daml_files.items():
            print(k, " -> ", v)

    def __enter__(self) -> ProtobufArchives:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.canton_zip.close()
        self.daml_zip.close()


class Protos:
    """
    Simple app to download, list, and update the Protobuf files that are used to generate parts of dazl.
    """

    version: Optional[str]
    cached_manifest: Optional[ProtobufManifest]

    def __init__(self, cache_dir: Union[str, os.PathLike] = default_cache_dir):
        self.cache_dir = os.fspath(cache_dir)
        self.manifest_file = os.fspath(Path(__file__).absolute().parent / "daml-connect.conf")
        if os.path.exists(self.manifest_file):
            with open(self.manifest_file, "r") as f:
                self.cached_manifest = manifest_from_conf_file(f)
            self.version = self.cached_manifest.version
        else:
            self.cached_manifest = None
            self.version = None

    def main(self) -> None:
        parser = ArgumentParser()
        parser.add_argument(
            "--cache-dir",
            default=self.cache_dir,
            help=f"cache directory (default: {self.cache_dir})",
        )
        subparsers = parser.add_subparsers(title="subcommands")

        for fn in (self.unpack, self.download, self.update):
            p = subparsers.add_parser(fn.__name__.replace("_", "-"), help=get_doc(fn))
            p.set_defaults(_run=fn)

            # for the "update" function specifically, a Daml version is required; all other
            # functions take it from our default (unless the manifest file is missing, in which
            # case it is required)
            if fn.__name__ == "update":
                p.add_argument("version")
            else:
                p.add_argument(
                    "--version",
                    default=self.version,
                    help=f"version of Daml Connect (default: {self.version})",
                )

        parser.parse_args(namespace=self)
        if hasattr(self, "_run"):
            self._run()
        else:
            parser.print_help()

    def unpack(self):
        """
        Unzips protobuf files to a directory.

        Some slight modifications are made to the contents:

         * The enclosing directory is removed; ``output_dir`` is assumed to be a Protobuf root path,
           so the zip file's enclosing directory is not helpful
         * Versions other than the most recent Daml-LF version are excluded from the output
         * "go package" directives are added to all of the files
        """
        self.download()

        self.protobufs_output_path.mkdir(parents=True, exist_ok=True)
        archives = ProtobufArchives(
            self.cached_manifest.version,
            self.protobufs_download_path / self.canton_distro_file_name,
            self.protobufs_download_path / self.daml_protobufs_file_name,
        )
        with archives:
            # first, create all of our necessary directories
            for entry in archives.manifest.dir_entries():
                (self.protobufs_output_path / entry.path).mkdir(exist_ok=True)

            for short_name, zip_name in archives.canton_files.items():
                with archives.canton_zip.open(zip_name) as r:
                    with io.TextIOWrapper(r) as buf_in:
                        contents = rewrite_canton_proto(short_name, buf_in.read())

                with (self.protobufs_output_path / short_name).open("w") as buf_out:
                    buf_out.write(contents)

            for short_name, zip_name in archives.daml_files.items():
                with archives.daml_zip.open(zip_name) as r:
                    with io.TextIOWrapper(r) as buf_in:
                        contents = rewrite_daml_proto(short_name, buf_in.read())
                with (self.protobufs_output_path / short_name).open("w") as buf_out:
                    buf_out.write(contents)

    def download(self) -> None:
        """
        Download the Protobuf files for a particular Daml Connect version to a local cache directory.
        """
        if not (self.protobufs_download_path / self.canton_distro_file_name).exists():
            self.protobufs_download_path.mkdir(parents=True, exist_ok=True)
            url = f"https://github.com/digital-asset/canton/releases/download/v{self.version}/{self.canton_distro_file_name}"
            urlretrieve(url, self.protobufs_download_path / self.canton_distro_file_name)

        if not (self.protobufs_download_path / self.daml_protobufs_file_name).exists():
            self.protobufs_download_path.mkdir(parents=True, exist_ok=True)
            url = f"https://github.com/digital-asset/daml/releases/download/v{self.version}/{self.daml_protobufs_file_name}"
            urlretrieve(url, self.protobufs_download_path / self.daml_protobufs_file_name)

    def update(self) -> None:
        """
        Updates the version of Daml Connect and Daml-LF that dazl is built against.
        Running this script modifies some files that are checked in to the repository; these files
        should be modified and checked in.
        """
        if self.version is None:
            raise ValueError("version is required")

        self.download()

        with ZipFile(self.protobufs_download_path / self.canton_distro_file_name) as canton_zip:
            with ZipFile(self.protobufs_download_path / self.daml_protobufs_file_name) as daml_zip:
                manifest = manifest_from_zip_files(self.version, canton_zip, daml_zip)

        proto_files = []  # type: List[str]
        python_files = [f"{PYTHON_GENERATED_ROOT}/__init__.py"]
        go_files = []  # type: List[str]
        for entry in manifest.entries:
            if isinstance(entry, ProtobufManifestDir):
                python_files.extend(
                    [
                        f"{PYTHON_GENERATED_ROOT}/{entry.path}/__init__.py",
                    ]
                )
            else:
                proto_files.append(f".cache/protos/{entry.path}")
                go_files.extend([f"{GO_GENERATED_ROOT}/{replace_ext.sub('.pb.go', entry.path)}"])
                python_files.extend(
                    [
                        f"{PYTHON_GENERATED_ROOT}/{replace_ext.sub('_pb2.py', entry.path )}",
                        f"{PYTHON_GENERATED_ROOT}/{replace_ext.sub('_pb2.pyi', entry.path )}",
                    ]
                )
                if entry.file_type == "grpc":
                    go_files.extend(
                        [f"{GO_GENERATED_ROOT}/{replace_ext.sub( '_grpc.pb.go', entry.path )}"]
                    )
                    python_files.extend(
                        [
                            f"{PYTHON_GENERATED_ROOT}/{replace_ext.sub('_pb2_grpc.py', entry.path )}",
                            f"{PYTHON_GENERATED_ROOT}/{replace_ext.sub('_pb2_grpc.pyi', entry.path )}",
                        ]
                    )

        proto_files.sort()
        python_files.sort()
        go_files.sort()

        filelist_dir = root_dir / "_build" / "filelists"
        filelist_dir.mkdir(parents=True, exist_ok=True)
        (filelist_dir / "protobufs.txt").write_text("\n".join(proto_files) + "\n")
        (filelist_dir / "python.txt").write_text("\n".join(python_files) + "\n")
        (filelist_dir / "go.txt").write_text("\n".join(go_files) + "\n")

        with open(self.manifest_file, "w") as buf:
            dump_manifest(manifest, buf)

    @property
    def canton_distro_file_name(self) -> str:
        return f"canton-open-source-{self.version}.zip"

    @property
    def daml_protobufs_file_name(self) -> str:
        return f"protobufs-{self.version}.zip"

    @property
    def protobufs_download_path(self) -> Path:
        return Path(self.cache_dir) / "download"

    @property
    def protobufs_output_path(self) -> Path:
        return Path(self.cache_dir) / "protos"


def get_doc(fn):
    for line in fn.__doc__.splitlines():
        line = line.strip()
        if line:
            return line


def detect_file_kind(buf: TextIO) -> Literal["pb", "grpc"]:
    for line in buf:
        if line.lstrip().startswith("service "):
            return "grpc"
    return "pb"


def detect_daml_lf_dir(paths: Collection[str]) -> Optional[str]:
    """
    Find the biggest Daml-LF v1 version in the set of file names from a Protobuf archive, and return
    the path that contains the associated files (with a trailing slash).

    If there is ever a Daml-LF 2, then this logic will need to be revisited; however, when that
    happens, there are likely to be even larger changes required, so we won't worry about this too
    much right now.

    :param paths: The paths in a Protobuf zipfile to examine.
    :return: The root directory of a target Daml-LF protobuf version, stripped of a prefix.

    >>> detect_daml_lf_dir([
    ...    "protos-1.15.0/com/daml/daml_lf_1_10/something.proto",
    ...    "protos-1.15.0/com/daml/daml_lf_1_9/something.proto",
    ...    "protos-1.15.0/com/daml/daml_lf_dev/something.proto",
    ...    "protos-1.15.0/com/daml/daml_lf_1_what/something.proto",
    ... ])
    'com/daml/daml_lf_1_10/'
    """
    daml_lf_prefix = "com/daml/daml_lf_1_"

    minor_versions = set()  # type: Set[int]
    for p in paths:
        _, _, truncated_path = p.partition("/")

        if truncated_path.startswith(daml_lf_prefix):
            version_str, _, _ = truncated_path[len(daml_lf_prefix) :].partition("/")
            try:
                minor_versions.add(int(version_str))
            except ValueError:
                # skip over unrecognized directory names
                pass
    if minor_versions:
        return f"{daml_lf_prefix}{max(minor_versions)}/"
    else:
        return None


def manifest_from_zip_files(
    version: str, canton_zip: ZipFile, daml_zip: ZipFile
) -> ProtobufManifest:
    file_entries = set()  # type: Set[ProtobufManifestFile]

    for short_name, zip_name in canton_proto_files(canton_zip.namelist()).items():
        with canton_zip.open(zip_name, "r") as f:
            with io.TextIOWrapper(f) as buf:
                kind = detect_file_kind(buf)
        file_entries.add(ProtobufManifestFile(kind, "canton", short_name))

    for short_name, zip_name in daml_proto_files(daml_zip.namelist()).items():
        with daml_zip.open(zip_name, "r") as f:
            with io.TextIOWrapper(f) as buf:
                kind = detect_file_kind(buf)
        file_entries.add(ProtobufManifestFile(kind, "daml", short_name))

    unique_dirs = {parent_dir for entry in file_entries for parent_dir in parent_dirs(entry.path)}
    return ProtobufManifest(
        version=version,
        entries=tuple(
            sorted(
                (*file_entries, *(ProtobufManifestDir(d) for d in unique_dirs)),
                key=lambda e: e.path,
            )
        ),
    )


def manifest_from_conf_file(buf: TextIO) -> ProtobufManifest:
    """
    Parse a manifest.conf file
    """
    version = None  # type: Optional[str]
    entries = []  # type: List[ProtobufManifestEntry]

    for line in buf:
        if line.startswith("#"):
            continue
        elif line.startswith("version "):
            _, _, version = line.rstrip().partition(" ")
        elif line.startswith("file "):
            args = line.rstrip().split(" ", maxsplit=4)
            try:
                entries.append(ProtobufManifestFile(args[1], args[2], args[3]))  # type: ignore
            except TypeError:
                print(args)
                raise
        elif line.startswith("dir "):
            entries.append(ProtobufManifestDir(line.rstrip()))

    if version is not None:
        return ProtobufManifest(version, entries)
    else:
        raise ValueError("couldn't find a version line")


def canton_proto_files(zip_file_names: Collection[str]) -> Mapping[str, str]:
    """
    Return paths to Canton protobuf/gRPC files that are interesting for code generation.
    The key is the "short" file path (starting with com/digitalasset) and the value is
    the full file path as it exists in the Canton .zip file distribution.
    """
    file_names = {}
    for name in zip_file_names:
        components = name.split("/")
        short_name = "/".join(name.split("/")[3:])

        if short_name == "com/digitalasset/canton/topology/admin/v0/topology_ext.proto":
            # this file has a different package name from its file location for historical
            # reasons, but leaving it like this breaks Python codegen because it has
            # an expectation that these lines match
            file_names["com/digitalasset/canton/protocol/v0/topology_ext.proto"] = name

        elif short_name == "com/digitalasset/canton/time/admin/v0/domain_time_service.proto":
            file_names["com/digitalasset/canton/domain/api/v0/domain_time_service.proto"] = name

        elif (
            components[1] == "protobuf"
            and components[-1].endswith(".proto")
            and not name.endswith("package.proto")
        ):
            # grab everything in the */protobuf directory that is a Protobuf file except
            # for the package.proto files, since those are just configuration for
            # Scala code generation, and that doesn't apply here
            file_names[short_name] = name
    return file_names


def daml_proto_files(zip_file_names: Collection[str]) -> Mapping[str, str]:
    """
    Return paths to Daml protobuf/gRPC files that are interesting for code generation.
    The key is the "short" file path (starting with com/daml) and the value is
    the full file path as it exists in the Canton .zip file distribution.

    :param zip_file_names:
        The names of files inside the Daml protobuf distribution.
    """
    file_names = {}

    daml_lf_dir = detect_daml_lf_dir(zip_file_names)
    if daml_lf_dir is None:
        print(zip_file_names)
        raise ValueError("could not detect daml_lf_dir")
    for name in zip_file_names:
        short_name = "/".join(name.split("/")[1:])

        if short_name.startswith("com/daml/ledger/api/v1/") and short_name.endswith(".proto"):
            # Ledger API protos
            file_names[short_name] = name
        elif short_name.startswith(daml_lf_dir) and short_name.endswith(".proto"):
            # Daml-LF protos
            file_names[short_name] = name

    return file_names


def rewrite_canton_proto(short_name: str, input_file: str) -> str:
    """ """
    with io.StringIO() as buf_out:
        # slightly rewrite Protobuf files to make them more amenable
        # to our own codegen process
        for line in input_file.splitlines(keepends=True):
            if line.strip().startswith("None = "):
                # the gRPC Python code generator spits out invalid Python
                # code when fields are called None, so rename fields that
                # we encounter that are called None
                buf_out.write(line.replace("None", "None_"))
            elif (
                line.strip()
                == 'import "com/digitalasset/canton/topology/admin/v0/topology_ext.proto";'
            ):
                # this import needs to be rewritten because we move this
                # file around in order to make its package name match
                buf_out.write('import "com/digitalasset/canton/protocol/v0/topology_ext.proto";\n')
            elif (
                line.strip()
                == 'import "com/digitalasset/canton/time/admin/v0/domain_time_service.proto";'
            ):
                # this import needs to be rewritten because we move this
                # file around in order to make its package name match
                buf_out.write(
                    'import "com/digitalasset/canton/domain/api/v0/domain_time_service.proto";\n'
                )
            elif "scalapb" in line:
                # scalapb imports must be ignored, because we don't have
                # those proto files handy (and they're not actually required
                # for our own purpsoes too)
                pass
            else:
                # write all other lines as-is, but also look for the
                # java_package directive as a hint for where we write our
                # own things
                buf_out.write(line)
                if line.startswith("package "):
                    _, _, proto_pkg = line.partition(" ")
                    proto_pkg = proto_pkg.strip().replace(";", "")
                    if (
                        short_name
                        == "com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto"
                    ):
                        # avoid import cycles
                        go_pkg = "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/domain/admin/v0/sequencerinitializationservice"
                    else:
                        go_pkg = (
                            "github.com/digital-asset/dazl-client/v7/go/api/"
                            + proto_pkg.replace(".", "/")
                        )

                    buf_out.write(f'option go_package = "{go_pkg}";\n')
        return buf_out.getvalue()


def rewrite_daml_proto(short_name: str, input_file: str) -> str:
    with io.StringIO() as buf_out:
        for line in input_file.splitlines(keepends=True):
            buf_out.write(line)
            if line.startswith("option java_package = "):
                java_pkg = line.partition('"')[2].rpartition('"')[0]
                go_pkg = "github.com/digital-asset/dazl-client/v7/go/api/" + java_pkg.replace(
                    ".", "/"
                )
                buf_out.write(f'option go_package = "{go_pkg}";\n')
        return buf_out.getvalue()


def dump_manifest(manifest: ProtobufManifest, buf: TextIO) -> None:
    for line in (root_dir / "COPYRIGHT").read_text().splitlines():
        buf.write(f"# {line}\n")
    buf.write("#\n")
    buf.write("# This file is automatically generated. To regenerate, run\n")
    buf.write(f"#     _build/daml-connect/protos.py update {manifest.version}\n")
    buf.write(f"version {manifest.version}\n")

    # for convenience and determinism, sort the remaining lines by file name
    for line_tuple in manifest.entries:
        buf.write(f"{line_tuple}\n")


def parent_dirs(p: str) -> Sequence[str]:
    c = p.split("/")
    return ["/".join(c[:i]) for i in range(1, len(c))]


if __name__ == "__main__":
    Protos().main()
