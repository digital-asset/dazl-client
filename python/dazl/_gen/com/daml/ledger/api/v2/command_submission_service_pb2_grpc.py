# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import command_submission_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2

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
        + f' but the generated code in com/daml/ledger/api/v2/command_submission_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CommandSubmissionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Submit = channel.unary_unary(
                '/com.daml.ledger.api.v2.CommandSubmissionService/Submit',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitResponse.FromString,
                _registered_method=True)
        self.SubmitReassignment = channel.unary_unary(
                '/com.daml.ledger.api.v2.CommandSubmissionService/SubmitReassignment',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitReassignmentRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitReassignmentResponse.FromString,
                _registered_method=True)


class CommandSubmissionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Submit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitReassignment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommandSubmissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Submit': grpc.unary_unary_rpc_method_handler(
                    servicer.Submit,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitResponse.SerializeToString,
            ),
            'SubmitReassignment': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitReassignment,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitReassignmentRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitReassignmentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v2.CommandSubmissionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.daml.ledger.api.v2.CommandSubmissionService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CommandSubmissionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Submit(request,
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
            '/com.daml.ledger.api.v2.CommandSubmissionService/Submit',
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitResponse.FromString,
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
    def SubmitReassignment(request,
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
            '/com.daml.ledger.api.v2.CommandSubmissionService/SubmitReassignment',
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitReassignmentRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v2_dot_command__submission__service__pb2.SubmitReassignmentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
