# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse

from . import plugin_archive

__all__ = ["run_all_plugins"]


def run_all_plugins(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    response = CodeGeneratorResponse()
    response.MergeFrom(plugin_archive.run_plugin(request))
    return response
