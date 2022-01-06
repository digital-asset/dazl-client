# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
from io import StringIO
from os.path import basename, dirname, splitext
from typing import DefaultDict, Set

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse

from ..syntax.python import all_decl
from ._header import HEADER

__all__ = ["run_plugin"]


def run_plugin(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    """
    Create `__init__.py` files for all directories.
    """
    directories = set()

    # for all of the requested files, add those files' parent directories, and the parents of all
    # THOSE directories
    for proto_dir in {dirname(f) for f in request.file_to_generate}:
        components = proto_dir.split("/")
        for i in range(0, len(components) + 1):
            directories.add("/".join(components[:i]))

    return CodeGeneratorResponse(
        file=[package_file(proto_dir, request) for proto_dir in sorted(directories)]
    )


def package_file(proto_dir: str, request: "CodeGeneratorRequest") -> "CodeGeneratorResponse.File":
    proto_package = proto_dir.replace("/", ".")

    import_map = defaultdict(set)  # type: DefaultDict[str, Set[str]]
    for file in request.proto_file:
        if file.package == proto_package:
            current_module_base = splitext(basename(file.name))[0]
            current_module_pb = "." + current_module_base + "_pb2"
            current_module_grpc = "." + current_module_base + "_pb2_grpc"
            for e in file.enum_type:
                import_map[current_module_pb].add(e.name)
            for m in file.message_type:
                import_map[current_module_pb].add(m.name)
            for s in file.service:
                import_map[current_module_grpc].add(s.name + "Stub")

    with StringIO() as buf:
        buf.write(HEADER)
        buf.write("\n")
        all_symbols = set()
        for f, i in import_map.items():
            buf.write(f"from {f} import {', '.join(sorted(i))}\n")
            all_symbols.update(i)
        buf.write("\n")
        buf.write(all_decl(sorted(all_symbols)))

        return CodeGeneratorResponse.File(name=f"{proto_dir}/__init__.py", content=buf.getvalue())
