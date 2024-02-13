# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections import defaultdict
from os.path import basename, dirname
from pathlib import Path
from typing import DefaultDict, Set

from google.protobuf.descriptor_pb2 import FileDescriptorSet

from ..syntax.python import all_decl
from .python_header import HEADER
from .util import get_root_name

__all__ = ["write_init_files"]


def write_init_files(fds: FileDescriptorSet, to: Path) -> None:
    """
    Write __init__.py files next to the generated Protobuf files.
    """
    plan = defaultdict(list)

    # organize our Protobuf files by enclosing directory
    for fd in fds.file:
        if (
            fd.name.startswith("com/daml") or fd.name.startswith("com/digitalasset")
        ) and not fd.name.endswith(".pyi"):
            plan[dirname(fd.name)].append(fd)

    # for each directory we identified, make sure there is an entry for all of their parent
    # directories too; we may also want to generate empty __init__ files
    for directory in list(plan):
        components = directory.split("/")
        for i in range(0, len(components)):
            _ = plan["/".join(components[:i])]

    for directory, files in plan.items():
        import_map = defaultdict(set)  # type: DefaultDict[str, Set[str]]
        for file in files:
            current_module_base = basename(get_root_name(file.name)[0])

            current_module_pb = "." + current_module_base + "_pb2"
            current_module_grpc = "." + current_module_base + "_pb2_grpc"
            for e in file.enum_type:
                import_map[current_module_pb].add(e.name)
            for m in file.message_type:
                import_map[current_module_pb].add(m.name)
            for s in file.service:
                import_map[current_module_grpc].add(s.name + "Stub")

        d = to / directory
        d.mkdir(parents=True, exist_ok=True)
        p = d / "__init__.py"
        with p.open("w") as buf:
            buf.write(HEADER)
            buf.write("\n")

            all_symbols = set()  # type: Set[str]
            for f, imports in import_map.items():
                buf.write(f"from {f} import {', '.join(sorted(imports))}\n")
                all_symbols.update(imports)
            buf.write("\n")
            buf.write(all_decl(sorted(all_symbols)))
