# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse

__all__ = ["with_file_header", "services_only"]


def with_file_header(response: "CodeGeneratorResponse", header: str) -> "CodeGeneratorResponse":
    """
    Add a file header to each file in the response, and return a new :class:`CodeGeneratorResponse`
    with the modified files.

    :param response: The :class:`CodeGeneratorResponse` that contains files to modify.
    :param header: The header string to prepend to each file.
    :return: A new :class:`CodeGeneratorResponse`.
    """
    return CodeGeneratorResponse(
        file=[
            CodeGeneratorResponse.File(name=f.name, content=header + f.content)
            for f in response.file
        ]
    )


def services_only(request: "CodeGeneratorRequest") -> "CodeGeneratorRequest":
    """
    Create a :class:`CodeGeneratorRequest` with the non-gRPC files stripped out (those without
    ``service`` declarations. The original request is not modified.
    """
    # include all of the Protobuf files, but restrict the list of "files_to_generate"
    files_with_services = {f.name for f in request.proto_file if len(f.service) > 0}
    return CodeGeneratorRequest(
        proto_file=request.proto_file,
        file_to_generate=[f for f in request.file_to_generate if f in files_with_services],
    )
