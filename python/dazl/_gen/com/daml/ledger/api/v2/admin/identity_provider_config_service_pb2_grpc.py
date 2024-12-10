# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import identity_provider_config_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2

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
        + f' but the generated code in com/daml/ledger/api/v2/admin/identity_provider_config_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class IdentityProviderConfigServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateIdentityProviderConfig = channel.unary_unary(
                '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/CreateIdentityProviderConfig',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.CreateIdentityProviderConfigRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.CreateIdentityProviderConfigResponse.FromString,
                _registered_method=True)
        self.GetIdentityProviderConfig = channel.unary_unary(
                '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/GetIdentityProviderConfig',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.GetIdentityProviderConfigRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.GetIdentityProviderConfigResponse.FromString,
                _registered_method=True)
        self.UpdateIdentityProviderConfig = channel.unary_unary(
                '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/UpdateIdentityProviderConfig',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.UpdateIdentityProviderConfigRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.UpdateIdentityProviderConfigResponse.FromString,
                _registered_method=True)
        self.ListIdentityProviderConfigs = channel.unary_unary(
                '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/ListIdentityProviderConfigs',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.ListIdentityProviderConfigsRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.ListIdentityProviderConfigsResponse.FromString,
                _registered_method=True)
        self.DeleteIdentityProviderConfig = channel.unary_unary(
                '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/DeleteIdentityProviderConfig',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.DeleteIdentityProviderConfigRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.DeleteIdentityProviderConfigResponse.FromString,
                _registered_method=True)


class IdentityProviderConfigServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateIdentityProviderConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIdentityProviderConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateIdentityProviderConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListIdentityProviderConfigs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIdentityProviderConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentityProviderConfigServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateIdentityProviderConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateIdentityProviderConfig,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.CreateIdentityProviderConfigRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.CreateIdentityProviderConfigResponse.SerializeToString,
            ),
            'GetIdentityProviderConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIdentityProviderConfig,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.GetIdentityProviderConfigRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.GetIdentityProviderConfigResponse.SerializeToString,
            ),
            'UpdateIdentityProviderConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateIdentityProviderConfig,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.UpdateIdentityProviderConfigRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.UpdateIdentityProviderConfigResponse.SerializeToString,
            ),
            'ListIdentityProviderConfigs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListIdentityProviderConfigs,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.ListIdentityProviderConfigsRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.ListIdentityProviderConfigsResponse.SerializeToString,
            ),
            'DeleteIdentityProviderConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIdentityProviderConfig,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.DeleteIdentityProviderConfigRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.DeleteIdentityProviderConfigResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v2.admin.IdentityProviderConfigService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.daml.ledger.api.v2.admin.IdentityProviderConfigService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class IdentityProviderConfigService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateIdentityProviderConfig(request,
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
            '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/CreateIdentityProviderConfig',
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.CreateIdentityProviderConfigRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.CreateIdentityProviderConfigResponse.FromString,
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
    def GetIdentityProviderConfig(request,
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
            '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/GetIdentityProviderConfig',
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.GetIdentityProviderConfigRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.GetIdentityProviderConfigResponse.FromString,
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
    def UpdateIdentityProviderConfig(request,
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
            '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/UpdateIdentityProviderConfig',
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.UpdateIdentityProviderConfigRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.UpdateIdentityProviderConfigResponse.FromString,
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
    def ListIdentityProviderConfigs(request,
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
            '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/ListIdentityProviderConfigs',
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.ListIdentityProviderConfigsRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.ListIdentityProviderConfigsResponse.FromString,
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
    def DeleteIdentityProviderConfig(request,
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
            '/com.daml.ledger.api.v2.admin.IdentityProviderConfigService/DeleteIdentityProviderConfig',
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.DeleteIdentityProviderConfigRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_admin_dot_identity__provider__config__service__pb2.DeleteIdentityProviderConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)