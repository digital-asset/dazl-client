# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import domain_service_pb2 as com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2
from ....protocol.v0 import sequencing_pb2 as com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DomainServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListServiceAgreementAcceptances = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.DomainService/ListServiceAgreementAcceptances',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.ServiceAgreementAcceptances.FromString,
                )
        self.GetDomainParameters = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.DomainService/GetDomainParameters',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.StaticDomainParameters.FromString,
                )
        self.GetDomainParametersVersioned = channel.unary_unary(
                '/com.digitalasset.canton.domain.admin.v0.DomainService/GetDomainParametersVersioned',
                request_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.GetDomainParameters.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.GetDomainParameters.Response.FromString,
                )


class DomainServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListServiceAgreementAcceptances(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDomainParameters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDomainParametersVersioned(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DomainServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListServiceAgreementAcceptances': grpc.unary_unary_rpc_method_handler(
                    servicer.ListServiceAgreementAcceptances,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.ServiceAgreementAcceptances.SerializeToString,
            ),
            'GetDomainParameters': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDomainParameters,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.StaticDomainParameters.SerializeToString,
            ),
            'GetDomainParametersVersioned': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDomainParametersVersioned,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.GetDomainParameters.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.GetDomainParameters.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.domain.admin.v0.DomainService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DomainService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListServiceAgreementAcceptances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v0.DomainService/ListServiceAgreementAcceptances',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.ServiceAgreementAcceptances.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v0.DomainService/GetDomainParameters',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_protocol_dot_v0_dot_sequencing__pb2.StaticDomainParameters.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDomainParametersVersioned(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.digitalasset.canton.domain.admin.v0.DomainService/GetDomainParametersVersioned',
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.GetDomainParameters.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_domain_dot_admin_dot_v0_dot_domain__service__pb2.GetDomainParameters.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
