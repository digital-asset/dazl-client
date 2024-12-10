# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import package_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in com/daml/ledger/api/v1/package_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PackageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPackages = channel.unary_unary(
                '/com.daml.ledger.api.v1.PackageService/ListPackages',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.ListPackagesRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.ListPackagesResponse.FromString,
                _registered_method=True)
        self.GetPackage = channel.unary_unary(
                '/com.daml.ledger.api.v1.PackageService/GetPackage',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageResponse.FromString,
                _registered_method=True)
        self.GetPackageStatus = channel.unary_unary(
                '/com.daml.ledger.api.v1.PackageService/GetPackageStatus',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageStatusRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageStatusResponse.FromString,
                _registered_method=True)


class PackageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListPackages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPackage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPackageStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PackageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPackages': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPackages,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.ListPackagesRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.ListPackagesResponse.SerializeToString,
            ),
            'GetPackage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPackage,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageResponse.SerializeToString,
            ),
            'GetPackageStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPackageStatus,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageStatusRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.PackageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.daml.ledger.api.v1.PackageService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PackageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListPackages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.daml.ledger.api.v1.PackageService/ListPackages',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.ListPackagesRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.ListPackagesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.daml.ledger.api.v1.PackageService/GetPackage',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPackageStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.daml.ledger.api.v1.PackageService/GetPackageStatus',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageStatusRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_package__service__pb2.GetPackageStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
