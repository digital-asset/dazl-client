# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import io
from typing import Optional

from .. import dazl_go_module

__all__ = ["canton_proto_rewrite", "daml_proto_rewrite"]


def canton_proto_rewrite(short_name: str, input_file: str) -> str:
    with io.StringIO() as buf_out:
        for line in input_file.splitlines(keepends=True):
            rewrite_canton_proto_line(short_name, line, buf_out)
        return buf_out.getvalue()


def rewrite_canton_proto_line(short_name: str, line: str, buf_out: io.StringIO) -> None:
    s = line.strip()
    if s.startswith("None = "):
        # the gRPC Python code generator spits out invalid Python
        # code when fields are called None, so rename fields that
        # we encounter that are called None
        buf_out.write(line.replace("None", "None_"))

    elif s == 'import "com/digitalasset/canton/topology/admin/v0/topology_ext.proto";':
        # this import needs to be rewritten because we move this
        # file around in order to make its package name match
        buf_out.write('import "com/digitalasset/canton/protocol/v0/topology_ext.proto";\n')

    elif s == 'import "com/digitalasset/canton/time/admin/v0/domain_time_service.proto";':
        # this import needs to be rewritten because we move this
        # file around in order to make its package name match
        buf_out.write('import "com/digitalasset/canton/domain/api/v0/domain_time_service.proto";\n')

    elif "scalapb" in line:
        # scalapb imports must be ignored, because we don't have those proto files handy
        # (and they're not actually required for our own purposes anyway)
        pass

    else:
        # write all other lines as-is, but also look for the
        # package directive as a hint for where we write our
        # own things
        buf_out.write(line)
        if proto_pkg := parse_proto_package(line):
            if (
                short_name
                == "com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto"
            ):
                # avoid import cycles
                go_pkg = f"{dazl_go_module}/go/api/com/digitalasset/canton/domain/admin/v0/sequencerinitializationservice"
            else:
                go_pkg = f"{dazl_go_module}/go/api/" + proto_pkg.replace(".", "/")

            buf_out.write(f'option go_package = "{go_pkg}";\n')


def daml_proto_rewrite(short_name: str, input_file: str) -> str:
    with io.StringIO() as buf_out:
        did_write_package = False

        for line in input_file.splitlines(keepends=True):
            buf_out.write(line)

            # prefer the java_package directive for inferring our own package location,
            # because that's correct for Daml-LF 1.16; but TraceContext in the Ledger API
            # doesn't define that, so fall back to the protobuf package
            if not did_write_package:
                suggested_pkg = parse_java_package(line)
                if suggested_pkg is None:
                    suggested_pkg = parse_proto_package(line)
                if suggested_pkg is not None:
                    go_pkg = (
                        "github.com/digital-asset/dazl-client/v8/go/api/"
                        + suggested_pkg.replace(".", "/")
                    )
                    buf_out.write(f'option go_package = "{go_pkg}";\n')
                    did_write_package = True
        return buf_out.getvalue()


def parse_proto_package(line: str) -> Optional[str]:
    if line.startswith("package "):
        _, _, proto_pkg = line.partition(" ")
        return proto_pkg.strip().replace(";", "")
    else:
        return None


def parse_java_package(line: str) -> Optional[str]:
    if line.startswith("option java_package = "):
        return line.partition('"')[2].rpartition('"')[0]
    else:
        return None
