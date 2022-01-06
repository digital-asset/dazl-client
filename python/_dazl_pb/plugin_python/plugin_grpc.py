# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse

from .. import protoc, util
from ..syntax.python import rewrite_file_content
from ._header import HEADER

__all__ = ["run_plugin"]


def run_plugin(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    response = protoc.run_plugin("grpc_python", util.services_only(request))
    for file in response.file:
        file.content = rewrite_file_content(file.name, file.content)

    return util.with_file_header(response, HEADER)
