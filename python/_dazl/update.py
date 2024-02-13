# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import asdict
import logging
from pathlib import Path
from typing import Optional

from . import codegen, protopack
from .download import download_dependencies

repo_root = Path(__file__).parent.parent.parent

logger = logging.getLogger("_dazl")


def update(*, daml_sdk_version: str, cache_dir: Path, temp_dir: Optional[Path] = None) -> None:
    """
    Update the parts of the dazl codebase that are code-generated.

    :param daml_sdk_version:
        The Daml SDK version.

    :param cache_dir:
        The directory where artifacts should be downloaded to. These files are kept around in order
        to make subsequent runs quicker.

    :param temp_dir:
        If ``None`` (the default), a temporary directory is created on the fly, and erased when the
        process finishes.

        If specified, temporary files are written to this directory. The directory's contents are
        cleared before running, and are NOT cleaned up afterwards in order to facilitate debugging.
    """
    logger.info("Updating protobuf files:")
    logger.info("    Daml SDK version: %s", daml_sdk_version)
    logger.info("    cache directory:  %s", cache_dir)
    if temp_dir is not None:
        logger.info("    temp directory:  %s", temp_dir)

    proto_pack = repo_root / ".cache" / "protos.pb"
    python_gen_dir = repo_root / "python" / "dazl" / "_gen"
    go_gen_dir = repo_root / "go" / "api"

    # grab the Daml protobufs and the Canton distribution; internally, this function
    # caches the downloaded files so that this function can be run over and over again
    # quickly
    downloads = download_dependencies(daml_sdk_version, to=cache_dir)

    # prepare a single protos.pb file that contains definitions for everything we
    # wish to generate
    protopack.build(**asdict(downloads), to=proto_pack, cache_dir=temp_dir)

    # now generate our various files
    codegen.python_files(from_=proto_pack, to=python_gen_dir)
    codegen.go_files(from_=proto_pack, to=go_gen_dir)
