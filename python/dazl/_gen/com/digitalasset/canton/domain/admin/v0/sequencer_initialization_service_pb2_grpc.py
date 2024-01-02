# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import sequencer_initialization_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2
from ..v1 import sequencer_initialization_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v1_dot_sequencer__initialization__service__pb2
from ..v2 import sequencer_initialization_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class SequencerInitializationServiceStub(object):
    """Service allowing a Domain node to initialize the sequencer instance.
    Should typically only be exposed to the domain node and not all clients
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/Init',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.FromString,
                )
        self.InitV1 = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/InitV1',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v1_dot_sequencer__initialization__service__pb2.InitRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.FromString,
                )
        self.InitV2 = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/InitV2',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.FromString,
                )


class SequencerInitializationServiceServicer(object):
    """Service allowing a Domain node to initialize the sequencer instance.
    Should typically only be exposed to the domain node and not all clients
    """

    def Init(self, request, context):
        """Initialize the Sequencer
        If the sequencer has not been previously initialized the request must either fail or start the sequencer and return successfully.
        The domain node will expect the SequencerService to be fully available when it receives a successful response
        and will immediately attempt to use it.
        If the request is received after the sequencer has been successfully initialized it should return successfully
        if the domain_id matches the domain that the sequencer has been initialized for, otherwise it should fail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitV1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitV2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SequencerInitializationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.SerializeToString,
            ),
            'InitV1': grpc.unary_unary_rpc_method_handler(
                    servicer.InitV1,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v1_dot_sequencer__initialization__service__pb2.InitRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.SerializeToString,
            ),
            'InitV2': grpc.unary_unary_rpc_method_handler(
                    servicer.InitV2,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.admin.v0.SequencerInitializationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SequencerInitializationService(object):
    """Service allowing a Domain node to initialize the sequencer instance.
    Should typically only be exposed to the domain node and not all clients
    """

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/Init',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitV1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/InitV1',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v1_dot_sequencer__initialization__service__pb2.InitRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v0.SequencerInitializationService/InitV2',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TopologyBootstrapServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Bootstrap = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.TopologyBootstrapService/Bootstrap',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.TopologyBootstrapRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class TopologyBootstrapServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Bootstrap(self, request, context):
        """allows sequencer to sequence initial topology transactions before IDM can be authenticated
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TopologyBootstrapServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Bootstrap': grpc.unary_unary_rpc_method_handler(
                    servicer.Bootstrap,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.TopologyBootstrapRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.admin.v0.TopologyBootstrapService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TopologyBootstrapService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Bootstrap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v0.TopologyBootstrapService/Bootstrap',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_sequencer__initialization__service__pb2.TopologyBootstrapRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
