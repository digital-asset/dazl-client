# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import sequencer_connect_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2
from . import service_agreement_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2
from ....protocol.v0 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2


class SequencerConnectServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Handshake = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/Handshake',
                request_serializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.Handshake.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.Handshake.Response.FromString,
                )
        self.GetDomainId = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainId',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainId.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainId.Response.FromString,
                )
        self.GetDomainParameters = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainParameters',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainParameters.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainParameters.Response.FromString,
                )
        self.VerifyActive = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/VerifyActive',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.VerifyActive.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.VerifyActive.Response.FromString,
                )
        self.GetServiceAgreement = channel.unary_unary(
                '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetServiceAgreement',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2.GetServiceAgreementRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2.GetServiceAgreementResponse.FromString,
                )


class SequencerConnectServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Handshake(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDomainId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDomainParameters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyActive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceAgreement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SequencerConnectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Handshake': grpc.unary_unary_rpc_method_handler(
                    servicer.Handshake,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.Handshake.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.Handshake.Response.SerializeToString,
            ),
            'GetDomainId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDomainId,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainId.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainId.Response.SerializeToString,
            ),
            'GetDomainParameters': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDomainParameters,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainParameters.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainParameters.Response.SerializeToString,
            ),
            'VerifyActive': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyActive,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.VerifyActive.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.VerifyActive.Response.SerializeToString,
            ),
            'GetServiceAgreement': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceAgreement,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2.GetServiceAgreementRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2.GetServiceAgreementResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.api.v0.SequencerConnectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SequencerConnectService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Handshake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/Handshake',
            com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.Handshake.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.Handshake.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDomainId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainId',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainId.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainId.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDomainParameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetDomainParameters',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainParameters.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.GetDomainParameters.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyActive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/VerifyActive',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.VerifyActive.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_sequencer__connect__service__pb2.SequencerConnect.VerifyActive.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceAgreement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.api.v0.SequencerConnectService/GetServiceAgreement',
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2.GetServiceAgreementRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_api_dot_v0_dot_service__agreement__pb2.GetServiceAgreementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
