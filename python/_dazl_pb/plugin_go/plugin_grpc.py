# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse

from .. import protoc, util
from ._header import HEADER

__all__ = ["run_plugin"]


def run_plugin(request: CodeGeneratorRequest) -> CodeGeneratorResponse:
    request.parameter = "paths=source_relative"
    response = protoc.run_plugin("go-grpc", util.services_only(request))
    return util.with_file_header(response, HEADER)
