# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import sequencer_initialization_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2


class SequencerInitializationServiceStub(object):
    """Service allowing a Domain node to initialize the sequencer instance.
    Should typically only be exposed to the domain node and not all clients
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Initialize = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v2.SequencerInitializationService/Initialize',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitializeSequencerRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitializeSequencerResponse.FromString,
                )


class SequencerInitializationServiceServicer(object):
    """Service allowing a Domain node to initialize the sequencer instance.
    Should typically only be exposed to the domain node and not all clients
    """

    def Initialize(self, request, context):
        """Initialize the Sequencer
        If the sequencer has not been previously initialized the request must either fail or start the sequencer and return successfully.
        The domain will expect the SequencerService to be fully available when it receives a successful response
        and will immediately attempt to use it.
        If the request is received after the sequencer has been successfully initialized it should return successfully
        if the domain_id matches the domain that the sequencer has been initialized for, otherwise it should fail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SequencerInitializationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.Initialize,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitializeSequencerRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitializeSequencerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.admin.v2.SequencerInitializationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SequencerInitializationService(object):
    """Service allowing a Domain node to initialize the sequencer instance.
    Should typically only be exposed to the domain node and not all clients
    """

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
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v2.SequencerInitializationService/Initialize',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitializeSequencerRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v2_dot_sequencer__initialization__service__pb2.InitializeSequencerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)