# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import mediator_initialization_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_mediator__initialization__service__pb2


class MediatorInitializationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Initialize = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v2.MediatorInitializationService/Initialize',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_mediator__initialization__service__pb2.InitializeMediatorRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_mediator__initialization__service__pb2.InitializeMediatorResponse.FromString,
                )


class MediatorInitializationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Initialize(self, request, context):
        """Initialize a Mediator service
        If the Mediator is uninitialized it should initialize itself with the provided configuration
        If the Mediator is already initialized then verify the request is for the domain we're running against,
        if correct then just return the current key otherwise fail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MediatorInitializationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.Initialize,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_mediator__initialization__service__pb2.InitializeMediatorRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_mediator__initialization__service__pb2.InitializeMediatorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.admin.v2.MediatorInitializationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MediatorInitializationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Initialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v2.MediatorInitializationService/Initialize',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_mediator__initialization__service__pb2.InitializeMediatorRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_mediator__initialization__service__pb2.InitializeMediatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
