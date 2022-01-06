# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from typing import Optional

from google.protobuf.descriptor_pb2 import FieldDescriptorProto
from grpc_tools.protoc import _PROTO_MODULE_SUFFIX, _SERVICE_MODULE_SUFFIX

from .types import BOOL, BYTES, FLOAT, INT, STRING, PyType

__all__ = ["py_message_package", "py_service_package", "py_scalar_type"]


FLOAT_TYPES = frozenset(
    [
        FieldDescriptorProto.TYPE_DOUBLE,
        FieldDescriptorProto.TYPE_FIXED32,
        FieldDescriptorProto.TYPE_FIXED64,
        FieldDescriptorProto.TYPE_FLOAT,
        FieldDescriptorProto.TYPE_SFIXED32,
        FieldDescriptorProto.TYPE_SFIXED64,
    ]
)
INT_TYPES = frozenset(
    [
        FieldDescriptorProto.TYPE_INT32,
        FieldDescriptorProto.TYPE_INT64,
        FieldDescriptorProto.TYPE_SINT32,
        FieldDescriptorProto.TYPE_SINT64,
        FieldDescriptorProto.TYPE_UINT32,
        FieldDescriptorProto.TYPE_UINT64,
    ]
)


def py_scalar_type(__fd_type: "FieldDescriptorProto.Type.V") -> "Optional[PyType]":
    """
    Return an appropriate :class:`PyType` for the given field type, or ``None`` if the type is a
    complex type that cannot be represented by a simple Python type.

    :param __fd_type: The type descriptor.
    :return: A representative :class:`PyType`.
    """
    if __fd_type in FLOAT_TYPES:
        return FLOAT
    elif __fd_type in INT_TYPES:
        return INT
    elif __fd_type == FieldDescriptorProto.TYPE_BOOL:
        return BOOL
    elif __fd_type == FieldDescriptorProto.TYPE_STRING:
        return STRING
    elif __fd_type == FieldDescriptorProto.TYPE_BYTES:
        return BYTES
    return None


def py_message_package(__file_name: str) -> str:
    """
    Return the Python package name for a ``.proto`` file with the specified name that contains
    Protobuf messages.

    :param __file_name: The path to a .proto file.
    :return: A Python module name for Protobuf messages.
    >>> py_message_package("foo/bar/messages.proto")
    'foo.bar.messages_pb2'
    """
    return os.path.splitext(__file_name)[0].replace("/", ".") + _PROTO_MODULE_SUFFIX


def py_service_package(__file_name: str) -> str:
    """
    Return the Python package name for a ``.proto`` file with the specified name that contains
    gRPC services.

    :param __file_name: The path to a .proto file.
    :return: A Python module name for gRPC services.
    >>> py_service_package("foo/bar/service.proto")
    'foo.bar.service_pb2_grpc'
    """
    return os.path.splitext(__file_name)[0].replace("/", ".") + _SERVICE_MODULE_SUFFIX
