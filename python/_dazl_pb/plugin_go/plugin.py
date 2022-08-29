# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse

from . import plugin_grpc, plugin_pb

__all__ = ["run_all_plugins"]


def run_all_plugins(request: CodeGeneratorRequest) -> CodeGeneratorResponse:
    response = CodeGeneratorResponse()
    response.MergeFrom(plugin_grpc.run_plugin(request))
    response.MergeFrom(plugin_pb.run_plugin(request))
    return response
