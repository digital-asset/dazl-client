#!/usr/bin/env python3
# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Utilities for working with Daml Connect.
#
# This script has no external dependencies and can run in Python 3.6+.

from argparse import ArgumentParser
from collections import defaultdict
import io
import os
from pathlib import Path
from typing import Collection, Optional, Sequence, Set, TextIO, Tuple, Union
from urllib.request import urlretrieve

__all__ = ["Protos"]

from zipfile import ZipFile

root_dir = Path(__file__).absolute().parent.parent.parent
default_cache_dir = root_dir / ".cache"


class Protos:
    """
    Simple app to download, list, and update the Protobuf files that are used to generate parts of dazl.
    """

    def __init__(self, cache_dir: "Union[str, os.PathLike]" = default_cache_dir):
        self.cache_dir = os.fspath(cache_dir)
        self.manifest_file = os.fspath(Path(__file__).absolute().parent / "daml-connect.conf")
        if os.path.exists(self.manifest_file):
            with open(self.manifest_file, "r") as f:
                self.cached_manifest = ProtobufManifest.from_conf_file(f)
            self.version = self.cached_manifest.version
        else:
            self.cached_manifest = None
            self.version = None
        self.kind = None

    def main(self) -> "None":
        parser = ArgumentParser()
        parser.add_argument(
            "--cache-dir",
            default=self.cache_dir,
            help=f"cache directory (default: {self.cache_dir})",
        )
        subparsers = parser.add_subparsers(title="subcommands")

        for fn in (self.list, self.unpack, self.download, self.update):
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

            if fn.__name__ == "list":
                p.add_argument("--kind")

        parser.parse_args(namespace=self)
        if hasattr(self, "_run"):
            self._run()
        else:
            parser.print_help()

    def list(self):
        """
        Produce a list of Protobuf files, rooted from the Protobuf root path.
        """
        manifest = self.cached_manifest
        if manifest is None:
            self.download()
            with ZipFile(self.protobufs_zip_path) as z:
                manifest = ProtobufManifest.from_zip_file(self.version, z)

        for k, p in manifest.paths:
            if self.kind is None or self.kind == k:
                print(p)

    def unpack(self):
        """
        Unzips protobuf files to a directory.

        Some slight modifications are made to the contents:

         * The enclosing directory is removed; ``output_dir`` is assumed to be a Protobuf root path,
           so the zip file's enclosing directory is not helpful
         * Versions other than the most recent Daml-LF version are excluded from the output
         * "go package" directives are added to all of the files
         * Daml-LF 1.14 has an improper package name that breaks code generation; fix it.
            (see https://github.com/digital-asset/daml/blob/1ee53c0736cbb758a9968d5c7ab6c57b24a87ed0/daml-lf/archive/src/main/protobuf/com/daml/daml_lf_1_14/daml_lf.proto#L5)
        """
        self.download()

        self.protobufs_output_path.mkdir(parents=True, exist_ok=True)
        with ZipFile(self.protobufs_zip_path) as z:
            manifest = ProtobufManifest.from_zip_file(self.version, z)

            # first, create all of our necessary directories
            for kind, path in manifest.paths:
                if kind == "dir":
                    (self.protobufs_output_path / path).mkdir(exist_ok=True)

            for kind, path in manifest.paths:
                if kind in ("pb", "grpc"):
                    with z.open(f"protos-{manifest.version}/{path}") as r, io.TextIOWrapper(
                        r
                    ) as buf_in, (self.protobufs_output_path / path).open("w") as buf_out:
                        for line in buf_in:
                            # patch a mislabeled file:
                            # see https://github.com/digital-asset/daml/blob/1ee53c0736cbb758a9968d5c7ab6c57b24a87ed0/daml-lf/archive/src/main/protobuf/com/daml/daml_lf_1_14/daml_lf.proto#L5
                            if line == "package daml_lf_1_13;\n":
                                buf_out.write("package daml_lf_1;\n")
                            else:
                                # insert a line after option java_package that specifies the go_package
                                buf_out.write(line)
                                if line.startswith("option java_package = "):
                                    java_pkg = line.partition('"')[2].rpartition('"')[0]
                                    go_pkg = (
                                        "github.com/digital-asset/dazl-client/v7/go/api/"
                                        + java_pkg.replace(".", "/")
                                    )
                                    buf_out.write(f'option go_package = "{go_pkg}";\n')

    def download(self) -> "None":
        """
        Download the Protobuf files for a particular Daml Connect version to a local cache directory.
        """
        if not self.protobufs_zip_path.exists():
            self.protobufs_zip_path.parent.mkdir(parents=True, exist_ok=True)
            url = f"https://github.com/digital-asset/daml/releases/download/v{self.version}/{self.protobufs_file_name}"
            urlretrieve(url, self.protobufs_zip_path)

    def update(self) -> "None":
        """
        Updates the version of Daml Connect and Daml-LF that dazl is built against.
        Running this script modifies some files that are checked in to the repository; these files
        should be modified and checked in.
        """
        self.download()

        with ZipFile(self.protobufs_zip_path) as z:
            manifest = ProtobufManifest.from_zip_file(self.version, z)

        with open(self.manifest_file, "w") as buf:
            manifest.dump(buf)

    @property
    def protobufs_file_name(self) -> str:
        return f"protobufs-{self.version}.zip"

    @property
    def protobufs_zip_path(self) -> "Path":
        return Path(self.cache_dir) / "download" / self.protobufs_file_name

    @property
    def protobufs_output_path(self) -> "Path":
        return Path(self.cache_dir) / "protos"


def get_doc(fn):
    for line in fn.__doc__.splitlines():
        line = line.strip()
        if line:
            return line


def detect_file_kind(buf: "TextIO") -> "str":
    for line in buf:
        if line.lstrip().startswith("service "):
            return "grpc"
    return "pb"


def detect_daml_lf_dir(paths: "Collection[str]") -> "Optional[str]":
    """
    Find the biggest Daml-LF v1 version in the set of file names from a Protobuf archive, and return
    the path that contains the associated files (with a trailing slash).

    If there is ever a Daml-LF 2, then this logic will need to be revisited; however, when that
    happens, there are likely to be even larger changes required so we won't worry about this too
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


class ProtobufManifest:
    @classmethod
    def from_zip_file(cls, version: str, protobufs_zip: "ZipFile"):
        paths_by_kind = defaultdict(set)

        daml_lf_dir = detect_daml_lf_dir(protobufs_zip.namelist())
        for name in protobufs_zip.namelist():
            _, _, truncated_path = name.partition("/")

            if truncated_path.startswith("com/daml/ledger/api/v1/"):
                with protobufs_zip.open(name, "r") as f:
                    with io.TextIOWrapper(f) as buf:
                        kind = detect_file_kind(buf)
                paths_by_kind[kind].add(truncated_path)

            elif truncated_path.startswith(daml_lf_dir):
                paths_by_kind["pb"].add(truncated_path)

        # find all of the unique directories and their parents
        paths_by_kind["dir"] = {
            parent_dir
            for paths in paths_by_kind.values()
            for path in paths
            for parent_dir in parent_dirs(path)
        }
        return cls(
            version, [(kind, path) for kind, paths in paths_by_kind.items() for path in paths]
        )

    @classmethod
    def from_conf_file(cls, buf: "TextIO"):
        version = None
        paths = []

        for line in buf:
            if not line.startswith("#"):
                k, _, p = line.rstrip().partition(" ")
                if k == "version":
                    version = p
                else:
                    paths.append((k, p))

        return cls(version, paths)

    def __init__(self, version: str, paths: "Sequence[Tuple[str, str]]"):
        self.version = version
        self.paths = tuple(sorted(paths, key=lambda t: t[1]))

    def dump(self, buf: "TextIO") -> None:
        for line in (root_dir / "COPYRIGHT").read_text().splitlines():
            buf.write(f"# {line}\n")
        buf.write("#\n")
        buf.write("# This file is automatically generated. To regenerate, run\n")
        buf.write(f"#     _build/daml-connect/protos.py update {self.version}\n")
        buf.write(f"version {self.version}\n")

        # for convenience and determinism, sort the remaining lines by file name
        for line_tuple in sorted(self.paths, key=lambda t: t[1]):
            buf.write(f"{' '.join(line_tuple)}\n")


def parent_dirs(p: str) -> Sequence[str]:
    c = p.split("/")
    return ["/".join(c[:i]) for i in range(1, len(c))]


if __name__ == "__main__":
    Protos().main()
