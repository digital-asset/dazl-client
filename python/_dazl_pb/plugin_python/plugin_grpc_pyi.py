# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import StringIO
import os
from typing import TextIO

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse
from google.protobuf.descriptor_pb2 import FileDescriptorProto, ServiceDescriptorProto

from .. import util
from ..syntax.python import ImportContext, SymbolTable, Usage, all_decl, py_service_package
from ._header import HEADER

__all__ = ["run_plugin"]


def run_plugin(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    """
    Generate .pyi (typing stubs files) for gPRC services.
    """
    # build a mapping of all types that we'll ever need to generate any of the requested files
    symbol_table = SymbolTable()
    for fd in request.proto_file:
        symbol_table.load_file(fd)

    request = util.services_only(request)

    return CodeGeneratorResponse(
        file=[
            typing_file(pf, ImportContext(symbol_table))
            for pf in request.proto_file
            if pf.name in request.file_to_generate
        ]
    )


def typing_file(fd: "FileDescriptorProto", ictx: "ImportContext") -> "CodeGeneratorResponse.File":
    name = os.path.splitext(fd.name)[0] + "_pb2_grpc.pyi"
    with StringIO() as buf:
        for sd in fd.service:
            write_service(buf, sd, ictx)

        body = buf.getvalue()

    ictx.add_system_import("", "builtins as _builtins")
    ictx.add_system_import("", "typing as _typing")
    ictx.add_import("", "grpc as _grpc")
    ictx.add_import("grpc", "aio as _grpc_aio")

    imports = ictx.py_import_block(py_service_package(fd.name))

    all_str = all_decl(md.name + "Stub" for md in fd.service)

    return CodeGeneratorResponse.File(name=name, content=f"{HEADER}\n{imports}\n{all_str}\n{body}")


def write_service(buf: "TextIO", sd: "ServiceDescriptorProto", ictx: "ImportContext") -> None:
    buf.write("\n")

    with StringIO() as stub_buf, StringIO() as abuf, StringIO() as bbuf:
        astub = f"_{sd.name}AsyncStub"
        bstub = f"_{sd.name}BlockingStub"

        stub_buf.write(
            f"# noinspection PyPep8Naming,DuplicatedCode\n"
            f"class {sd.name}Stub:\n"
            f"    @classmethod\n"
            f"    @_typing.overload\n"
            f"    def __new__(cls, channel: _grpc.Channel) -> {bstub}: ...  # type: ignore\n"
            f"    @classmethod\n"
            f"    @_typing.overload\n"
            f"    def __new__(cls, channel: _grpc_aio.Channel) -> {astub}: ...  # type: ignore\n"
        )

        abuf.write("# noinspection PyPep8Naming,DuplicatedCode\n")
        abuf.write(f"class {astub}({sd.name}Stub):\n")

        bbuf.write("# noinspection PyPep8Naming,DuplicatedCode\n")
        bbuf.write(f"class {bstub}({sd.name}Stub):\n")

        for method in sd.method:
            arg = ictx.py_type(
                method.input_type, Usage.ARG_STREAM if method.client_streaming else Usage.ARG
            )
            a_ret = ictx.py_type(
                method.output_type,
                Usage.RET_STREAM_ASYNC if method.server_streaming else Usage.RET_ASYNC,
            )
            b_ret = ictx.py_type(
                method.output_type, Usage.RET_STREAM if method.server_streaming else Usage.RET
            )

            timeout_param = "timeout: _typing.Optional[float] = ..."
            credentials_param = "credentials: _typing.Optional[_grpc.CallCredentials] = ..."
            wait_for_ready_param = "wait_for_ready: _typing.Optional[bool] = ..."
            compression_param = "compression: _typing.Optional[_grpc.Compression] = ..."

            stub_buf.write(f"    def {method.name}(self, __1: {arg.py_str}, *, ")
            stub_buf.write(timeout_param)
            stub_buf.write(
                ", metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ...,"
            )
            stub_buf.write(
                f" {credentials_param}, {wait_for_ready_param}, {compression_param}) -> "
            )
            stub_buf.write(f"_typing.Union[{b_ret.py_str}, {a_ret.py_str}]: ...\n")

            # when using AsyncIO-flavored channels, the optional parameters are explicitly
            # keyword-only
            abuf.write(f"    def {method.name}(self, __1: {arg.py_str}, *, ")
            abuf.write(timeout_param)
            abuf.write(", metadata: _typing.Optional[_grpc_aio.Metadata] = ...,")
            abuf.write(f" {credentials_param}, {wait_for_ready_param}, {compression_param}) -> ")
            abuf.write(a_ret.py_str)
            abuf.write(": ...\n")

            bbuf.write(
                f"    def {method.name}(self, __1: {arg.py_str}, {timeout_param}, "
                + "metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..."
                + f", {credentials_param}, {wait_for_ready_param}, {compression_param}) -> "
                + b_ret.py_str
                + ": ...\n"
            )

        buf.write(stub_buf.getvalue() + "\n")
        buf.write(bbuf.getvalue() + "\n")
        buf.write(abuf.getvalue())
