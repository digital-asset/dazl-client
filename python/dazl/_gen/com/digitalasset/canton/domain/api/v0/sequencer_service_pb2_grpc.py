# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import sequencer_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2
from ....protocol.v0 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

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
        + f' but the generated code in com/digitalasset/canton/domain/api/v0/sequencer_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SequencerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendAsync = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsync',
                request_serializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SubmissionRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.FromString,
                _registered_method=True)
        self.SendAsyncSigned = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncSigned',
                request_serializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SignedContent.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncSignedResponse.FromString,
                _registered_method=True)
        self.SendAsyncUnauthenticated = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncUnauthenticated',
                request_serializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SubmissionRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.FromString,
                _registered_method=True)
        self.SendAsyncVersioned = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncVersioned',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncVersionedRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncSignedResponse.FromString,
                _registered_method=True)
        self.SendAsyncUnauthenticatedVersioned = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncUnauthenticatedVersioned',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncUnauthenticatedVersionedRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.FromString,
                _registered_method=True)
        self.Subscribe = channel.unary_stream(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/Subscribe',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionResponse.FromString,
                _registered_method=True)
        self.SubscribeVersioned = channel.unary_stream(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeVersioned',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.VersionedSubscriptionResponse.FromString,
                _registered_method=True)
        self.SubscribeUnauthenticated = channel.unary_stream(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeUnauthenticated',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionResponse.FromString,
                _registered_method=True)
        self.SubscribeUnauthenticatedVersioned = channel.unary_stream(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeUnauthenticatedVersioned',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.VersionedSubscriptionResponse.FromString,
                _registered_method=True)
        self.Acknowledge = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/Acknowledge',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.AcknowledgeRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.AcknowledgeSigned = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerService/AcknowledgeSigned',
                request_serializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SignedContent.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class SequencerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendAsync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendAsyncSigned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendAsyncUnauthenticated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendAsyncVersioned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendAsyncUnauthenticatedVersioned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeVersioned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeUnauthenticated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeUnauthenticatedVersioned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Acknowledge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcknowledgeSigned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SequencerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendAsync': grpc.unary_unary_rpc_method_handler(
                    servicer.SendAsync,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SubmissionRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.SerializeToString,
            ),
            'SendAsyncSigned': grpc.unary_unary_rpc_method_handler(
                    servicer.SendAsyncSigned,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SignedContent.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncSignedResponse.SerializeToString,
            ),
            'SendAsyncUnauthenticated': grpc.unary_unary_rpc_method_handler(
                    servicer.SendAsyncUnauthenticated,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SubmissionRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.SerializeToString,
            ),
            'SendAsyncVersioned': grpc.unary_unary_rpc_method_handler(
                    servicer.SendAsyncVersioned,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncVersionedRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncSignedResponse.SerializeToString,
            ),
            'SendAsyncUnauthenticatedVersioned': grpc.unary_unary_rpc_method_handler(
                    servicer.SendAsyncUnauthenticatedVersioned,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncUnauthenticatedVersionedRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionResponse.SerializeToString,
            ),
            'SubscribeVersioned': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeVersioned,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.VersionedSubscriptionResponse.SerializeToString,
            ),
            'SubscribeUnauthenticated': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeUnauthenticated,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionResponse.SerializeToString,
            ),
            'SubscribeUnauthenticatedVersioned': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeUnauthenticatedVersioned,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.VersionedSubscriptionResponse.SerializeToString,
            ),
            'Acknowledge': grpc.unary_unary_rpc_method_handler(
                    servicer.Acknowledge,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.AcknowledgeRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AcknowledgeSigned': grpc.unary_unary_rpc_method_handler(
                    servicer.AcknowledgeSigned,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SignedContent.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.api.v0.SequencerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.digitalasset.canton.domain.api.v0.SequencerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SequencerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendAsync(request,
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
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsync',
            com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SubmissionRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.FromString,
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
    def SendAsyncSigned(request,
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
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncSigned',
            com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SignedContent.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncSignedResponse.FromString,
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
    def SendAsyncUnauthenticated(request,
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
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncUnauthenticated',
            com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SubmissionRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.FromString,
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
    def SendAsyncVersioned(request,
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
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncVersioned',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncVersionedRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncSignedResponse.FromString,
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
    def SendAsyncUnauthenticatedVersioned(request,
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
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SendAsyncUnauthenticatedVersioned',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncUnauthenticatedVersionedRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SendAsyncResponse.FromString,
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
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/com.digitalasset.canton.domain.api.v0.SequencerService/Subscribe',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionResponse.FromString,
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
    def SubscribeVersioned(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeVersioned',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.VersionedSubscriptionResponse.FromString,
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
    def SubscribeUnauthenticated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeUnauthenticated',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionResponse.FromString,
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
    def SubscribeUnauthenticatedVersioned(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/com.digitalasset.canton.domain.api.v0.SequencerService/SubscribeUnauthenticatedVersioned',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.SubscriptionRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.VersionedSubscriptionResponse.FromString,
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
    def Acknowledge(request,
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
            '/com.digitalasset.canton.domain.api.v0.SequencerService/Acknowledge',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__service__pb2.AcknowledgeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
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
    def AcknowledgeSigned(request,
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
            '/com.digitalasset.canton.domain.api.v0.SequencerService/AcknowledgeSigned',
            com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.SignedContent.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
