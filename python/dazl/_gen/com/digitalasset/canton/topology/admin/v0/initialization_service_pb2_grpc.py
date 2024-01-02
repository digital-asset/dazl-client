# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import initialization_service_pb2 as com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


class InitializationServiceStub(object):
    """*
    The node initialization service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitId = channel.unary_unary(
                '/com.digitalasset.canton.topology.admin.v0.InitializationService/InitId',
                request_serializer=com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.InitIdRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.InitIdResponse.FromString,
                )
        self.GetId = channel.unary_unary(
                '/com.digitalasset.canton.topology.admin.v0.InitializationService/GetId',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.GetIdResponse.FromString,
                )
        self.CurrentTime = channel.unary_unary(
                '/com.digitalasset.canton.topology.admin.v0.InitializationService/CurrentTime',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_timestamp__pb2.Timestamp.FromString,
                )


class InitializationServiceServicer(object):
    """*
    The node initialization service
    """

    def InitId(self, request, context):
        """*
        Initialize the node with the unique identifier (can and must be done once)

        When a domain or participant instance starts for the first time, we need to bind it
        to a globally unique stable identifier before we can continue with the
        initialization procedure.

        This method is only used once during initialization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetId(self, request, context):
        """*
        Returns the id of the node (or empty if not initialized)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentTime(self, request, context):
        """*
        Returns the current time of the node (used for testing with static time)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InitializationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitId': grpc.unary_unary_rpc_method_handler(
                    servicer.InitId,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.InitIdRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.InitIdResponse.SerializeToString,
            ),
            'GetId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetId,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.GetIdResponse.SerializeToString,
            ),
            'CurrentTime': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrentTime,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_timestamp__pb2.Timestamp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.topology.admin.v0.InitializationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InitializationService(object):
    """*
    The node initialization service
    """

    @staticmethod
    def InitId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.topology.admin.v0.InitializationService/InitId',
            com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.InitIdRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.InitIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.topology.admin.v0.InitializationService/GetId',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_topology_dot_admin_dot_v0_dot_initialization__service__pb2.GetIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.topology.admin.v0.InitializationService/CurrentTime',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_timestamp__pb2.Timestamp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
