# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Utilities for running protoc, and easily composing Protobuf calls in python.

To create a Protobuf plugin in Python, define an entrypoint as so:

.. code-block:: python

   @protoc_plugin
   def main(request: CodeGeneratorRequest) -> CodeGeneratorResponse:
       # This does what `python3 -m grpc_tools.protoc ...` does,
       # but as a function call in Python instead of an awkward exec
       python_response = run_plugin('python', request)

       # It is typical for a plugin to need to ultimately call one of the
       # built-in plugins (for example, to post-process the data from a built-in plugin).
       for f in python_response.file:
           f.proto_file = COPYRIGHT_NOTICE + f.proto_file

       response = CodeGeneratorResponse()
       response.MergeFrom(python_response)
       return response
"""

from functools import wraps
import os
from pathlib import Path
import site
import subprocess
import sys
from tempfile import TemporaryDirectory
from traceback import print_exc
from typing import Callable, List, NoReturn

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse
from google.protobuf.descriptor_pb2 import FileDescriptorSet
from grpc_tools import protoc as _protoc
import pkg_resources

__all__ = ["main", "protoc_plugin", "run_plugin"]


def main() -> "NoReturn":
    """
    Entrypoint that runs ``protoc``, but with locally exported binary plugins, and automatically
    including Protobuf files that are built into ``grpc_tools`` and that have been pulled through
    as Python dependencies.
    """
    sys.exit(_main(sys.argv))


def _main(argv):
    os.environ["PATH"] = f'{os.getenv("PATH")}:{os.path.dirname(sys.executable)}'

    includes = [
        pkg_resources.resource_filename("grpc_tools", "_proto"),
        *site.getsitepackages(),
    ]
    return _protoc.main(argv + ["-I" + inc for inc in includes])


def protoc_plugin(
    fn: "Callable[[CodeGeneratorRequest], CodeGeneratorResponse]",
) -> "Callable[[], NoReturn]":
    """
    Decorator that converts a callable function to a ``protoc`` plugin.

    This function does NOT return, and is intended to be used as the main function for a Python
    program/script.
    """

    @wraps(fn)
    def _body() -> "NoReturn":
        try:
            data = sys.stdin.buffer.read()
            request = CodeGeneratorRequest.FromString(data)
            response = fn(request)
            code = 0
        except Exception as ex:
            print_exc(file=sys.stderr)
            response = CodeGeneratorResponse(error=str(ex))
            code = 1

        sys.stdout.buffer.write(response.SerializeToString())
        sys.exit(code)

    return _body


def run_plugin(plugin_name: "str", request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    if plugin_name in ("python", "grpc_python"):
        return run_plugin_built_in(plugin_name, request)
    else:
        return run_plugin_external(plugin_name, request)


def run_plugin_built_in(
    plugin_name: "str", request: "CodeGeneratorRequest"
) -> "CodeGeneratorResponse":
    with TemporaryDirectory() as tmpdir:
        input_file = Path(tmpdir) / "in.bin"
        output_dir = Path(tmpdir) / "out"

        output_dir.mkdir()

        input_file.write_bytes(FileDescriptorSet(file=request.proto_file).SerializeToString())

        # re-run the built-in code generator, but with the arguments that we were given
        invocation = [
            "_dazl_pb.protoc",
            f"--descriptor_set_in={input_file}",
            f"--{plugin_name}_out={output_dir}",
            *request.file_to_generate,
        ]

        exit_code = _main(invocation)
        if exit_code:
            raise Exception(f"failed to run {invocation} (exit code {exit_code})")

        files = [
            CodeGeneratorResponse.File(name=str(p.relative_to(output_dir)), content=p.read_text())
            for p in output_dir.rglob("*")
            if p.is_file()
        ]
        return CodeGeneratorResponse(file=files)


def run_plugin_external(
    plugin_name: "str", request: "CodeGeneratorRequest"
) -> "CodeGeneratorResponse":
    args = ["protoc-gen-" + plugin_name]  # type: List[str]
    proc = subprocess.run(args, input=request.SerializeToString(), capture_output=True)  # type: ignore

    response = CodeGeneratorResponse()
    response.ParseFromString(proc.stdout)
    return response
