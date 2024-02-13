# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from os.path import splitext
from pathlib import Path
import shutil

from google.protobuf.descriptor_pb2 import FileDescriptorSet

from .. import protoc
from ..syntax.python import rewrite_file_content
from .python_grpc_pyi import write_grpc_pyi_files
from .python_header import HEADER
from .python_init import write_init_files
from .util import get_root_name

__all__ = ["python_files"]


def python_files(from_: Path, to: Path) -> None:
    fds = FileDescriptorSet()
    fds.ParseFromString(from_.read_bytes())

    if to.exists():
        shutil.rmtree(to)

    write_init_files(fds, to)
    write_grpc_pyi_files(fds, to)
    write_standard_files(from_, fds, to)


def write_standard_files(from_: Path, fds: FileDescriptorSet, to: Path) -> None:
    """
    Writes (most of) the files from the standard Protobuf plugins.

    Files that came from the gRPC plugin but correspond to Protobufs that have no services are omitted.
    """
    response = protoc.run(from_, plugins=["python", "pyi", "grpc_python"])
    proto_files = {splitext(fd.name)[0]: fd for fd in fds.file}

    for f in response.file:
        root_name, suffix = get_root_name(f.name)
        if suffix == "_pb2_grpc.py" and not proto_files[root_name].service:
            # skip gRPC generated files if the corresponding Protobuf has no services
            continue

        p = to / f.name
        p.parent.mkdir(parents=True, exist_ok=True)

        # add a copyright to each of the files from the plugin
        p.write_text(HEADER + rewrite_file_content(f.name, f.content))
