# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import sequencer_initialization_service_pb2 as com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2

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
        + f' but the generated code in com/digitalasset/canton/sequencer/admin/v30/sequencer_initialization_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SequencerInitializationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitializeSequencerFromGenesisState = channel.stream_unary(
                '/com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService/InitializeSequencerFromGenesisState',
                request_serializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromGenesisStateRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromGenesisStateResponse.FromString,
                _registered_method=True)
        self.InitializeSequencerFromOnboardingState = channel.stream_unary(
                '/com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService/InitializeSequencerFromOnboardingState',
                request_serializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromOnboardingStateRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromOnboardingStateResponse.FromString,
                _registered_method=True)


class SequencerInitializationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InitializeSequencerFromGenesisState(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitializeSequencerFromOnboardingState(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SequencerInitializationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitializeSequencerFromGenesisState': grpc.stream_unary_rpc_method_handler(
                    servicer.InitializeSequencerFromGenesisState,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromGenesisStateRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromGenesisStateResponse.SerializeToString,
            ),
            'InitializeSequencerFromOnboardingState': grpc.stream_unary_rpc_method_handler(
                    servicer.InitializeSequencerFromOnboardingState,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromOnboardingStateRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromOnboardingStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SequencerInitializationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InitializeSequencerFromGenesisState(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService/InitializeSequencerFromGenesisState',
            com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromGenesisStateRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromGenesisStateResponse.FromString,
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
    def InitializeSequencerFromOnboardingState(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/com.digitalasset.canton.sequencer.admin.v30.SequencerInitializationService/InitializeSequencerFromOnboardingState',
            com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromOnboardingStateRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_sequencer_dot_admin_dot_v30_dot_sequencer__initialization__service__pb2.InitializeSequencerFromOnboardingStateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
