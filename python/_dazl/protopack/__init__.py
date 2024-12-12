# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from contextlib import ExitStack
import io
import os
from pathlib import Path
from shutil import rmtree
from tempfile import TemporaryDirectory
from typing import Collection, Mapping, Optional, Protocol
from zipfile import ZipFile

from . import rename, rewrite
from .. import protoc

__all__ = ["build"]


class Renamer(Protocol):
    def __call__(self, zip_file_list: Collection[str], /) -> Mapping[str, str]: ...


class Rewriter(Protocol):
    def __call__(self, target_name: str, contents: str, /) -> str: ...


def build(
    *,
    canton_2_zip: Path,
    daml_2_protos_zip: Path,
    daml_3_protos_zip: Path,
    to: Path,
    cache_dir: Optional[Path] = None,
) -> None:
    with ExitStack() as stack:
        canton_2 = stack.enter_context(ZipFile(canton_2_zip))
        daml_2_proto = stack.enter_context(ZipFile(daml_2_protos_zip))
        daml_3_proto = stack.enter_context(ZipFile(daml_3_protos_zip))

        if cache_dir is not None:
            rmtree(cache_dir)
        else:
            cache_dir = Path(stack.enter_context(TemporaryDirectory()))

        _build_zip_part(
            archive=canton_2,
            out_dir=cache_dir,
            renamer=rename.canton_proto_files,
            rewriter=rewrite.canton_proto_rewrite,
        )

        if canton_3_dir := os.getenv("CN_ENTERPRISE_PATH"):
            _build_dir_part(
                input_dir=Path(canton_3_dir),
                out_dir=cache_dir,
                renamer=rename.canton_proto_files,
                rewriter=rewrite.canton_proto_rewrite,
            )

        _build_zip_part(
            archive=daml_2_proto,
            out_dir=cache_dir,
            renamer=lambda names: rename.daml_proto_files(names, "v1"),
            rewriter=rewrite.daml_proto_rewrite,
        )

        _build_zip_part(
            archive=daml_3_proto,
            out_dir=cache_dir,
            renamer=lambda names: rename.daml_proto_files(names, "v2"),
            rewriter=rewrite.daml_proto_rewrite,
        )

        protoc.generate_descriptors(cache_dir, to)


def _build_zip_part(archive: ZipFile, out_dir: Path, renamer: Renamer, rewriter: Rewriter) -> None:
    proto_files = renamer(archive.namelist())

    for target_name, zip_name in proto_files.items():
        with archive.open(zip_name) as r:
            with io.TextIOWrapper(r) as buf_in:
                contents = rewriter(target_name, buf_in.read())

        out_file = out_dir / target_name
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(contents)


def _build_dir_part(input_dir: Path, out_dir: Path, renamer: Renamer, rewriter: Rewriter) -> None:
    proto_files = renamer(
        [
            str(input_name.relative_to(input_dir.parent))
            for input_name in input_dir.glob("**/*.proto")
        ]
    )

    for target_name, original_name in proto_files.items():
        input_name = input_dir.parent / original_name
        with input_name.open() as buf_in:
            contents = rewriter(target_name, buf_in.read())

        out_file = out_dir / target_name
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(contents)
