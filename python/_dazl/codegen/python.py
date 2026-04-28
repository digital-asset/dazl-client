# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from os.path import splitext
from pathlib import Path
import shutil
from typing import Sequence, TextIO

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
        write_corrected_content(p, rewrite_file_content(f.name, f.content))


def write_corrected_content(path: Path, content: str) -> None:
    lines = content.splitlines()
    with path.open("w") as buf:
        buf.write(HEADER)

        if str(path).endswith("v30/package_service_pb2.pyi"):
            write_corrected_content_package_service_pyi(buf, lines)
        else:
            write_content_unchanged(buf, lines)


def write_corrected_content_package_service_pyi(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        # the field 'bytes' causes mypy to get confused when typechecking this file
        if (
            line
            == "from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union"
        ):
            buf.write(line + "\n")
            buf.write("from builtins import bytes as _bytes\n")

        elif "def __init__(self, bytes: _Optional[bytes] = ..." in line:
            buf.write(line.replace("_Optional[bytes]", "_Optional[_bytes]") + "\n")

        else:
            buf.write(line + "\n")


def write_content_unchanged(buf: TextIO, lines: Sequence[str]) -> None:
    for line in lines:
        buf.write(line + "\n")
