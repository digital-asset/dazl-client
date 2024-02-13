# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import io

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
        # java_package directive as a hint for where we write our
        # own things
        buf_out.write(line)
        if line.startswith("package "):
            _, _, proto_pkg = line.partition(" ")
            proto_pkg = proto_pkg.strip().replace(";", "")
            if (
                short_name
                == "com/digitalasset/canton/domain/admin/v0/sequencer_initialization_service.proto"
            ):
                # avoid import cycles
                go_pkg = "github.com/digital-asset/dazl-client/v7/go/api/com/digitalasset/canton/domain/admin/v0/sequencerinitializationservice"
            else:
                go_pkg = "github.com/digital-asset/dazl-client/v7/go/api/" + proto_pkg.replace(
                    ".", "/"
                )

            buf_out.write(f'option go_package = "{go_pkg}";\n')


def daml_proto_rewrite(short_name: str, input_file: str) -> str:
    with io.StringIO() as buf_out:
        for line in input_file.splitlines(keepends=True):
            buf_out.write(line)
            if line.startswith("option java_package = "):
                java_pkg = line.partition('"')[2].rpartition('"')[0]
                go_pkg = "github.com/digital-asset/dazl-client/v7/go/api/" + java_pkg.replace(
                    ".", "/"
                )
                buf_out.write(f'option go_package = "{go_pkg}";\n')
        return buf_out.getvalue()
