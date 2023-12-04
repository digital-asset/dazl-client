# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
from os import PathLike
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
from typing import Collection, Optional

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse, Version
from google.protobuf.descriptor_pb2 import FileDescriptorSet
import grpc_tools.protoc

__all__ = ["run", "request", "write_response"]


def run(
    fds_file: PathLike, plugins: Collection[str], options: Collection[str] = ()
) -> CodeGeneratorResponse:
    """
    Run the Protobuf compiler on built-in plugins.
    """
    fds = FileDescriptorSet()
    fds.ParseFromString(Path(fds_file).read_bytes())
    filelist = [
        f.name
        for f in fds.file
        if f.name.startswith("com/daml") or f.name.startswith("com/digitalasset")
    ]

    path = os.getenv("PATH")
    path = f"{Path(__file__).parent.parent.parent.parent}/.cache/bin:{path}"
    os.environ["PATH"] = path

    fds_path = Path(fds_file)
    with TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        args = [
            "grpc_tools.protoc",
            f"--descriptor_set_in={fds_path}",
            *(f"--{plugin}_out={tmpdir}" for plugin in plugins),
            *options,
            *filelist,
        ]

        grpc_tools.protoc.main(args)

        return CodeGeneratorResponse(
            file=[
                CodeGeneratorResponse.File(
                    name=str(f.relative_to(tmpdir_path)), content=f.read_text()
                )
                for f in tmpdir_path.glob("**/*")
                if f.is_file()
            ]
        )


def generate_descriptors(root_dir: Path, to: Path) -> None:
    cwd = os.getcwd()
    os.chdir(root_dir)
    try:
        args = ["grpc_tools.protoc", f"--descriptor_set_out={to}"]
        grpc_tools.protoc.main(args)
    finally:
        os.chdir(cwd)


def request(fds_file: PathLike, parameter: Optional[str] = None) -> CodeGeneratorRequest:
    b = Path(fds_file).read_bytes()

    fds = FileDescriptorSet()
    fds.ParseFromString(b)

    request = CodeGeneratorRequest(
        file_to_generate=[f.name for f in fds.file if f.name.startswith("com/")],
        parameter=parameter,
        proto_file=fds.file,
        compiler_version=Version(),
    )

    with TemporaryDirectory() as tmpdir:
        grpc_tools.protoc.main()

    if parameter is not None:
        request.parameter = parameter
    return request


def write_response(response: CodeGeneratorResponse, output_dir: Path) -> None:
    """
    Write the files indicated in ``response`` to the specified output directory. If the directory
    does not exist, it is created. If the specified path has files, it is cleared first.
    """
    shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for f in response.file:
        output_file = output_dir / f.name
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(f.content)
