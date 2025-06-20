# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import domain_connectivity_pb2 as com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2

GRPC_GENERATED_VERSION = '1.72.1'
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
        + f' but the generated code in com/digitalasset/canton/participant/admin/v0/domain_connectivity_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DomainConnectivityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReconnectDomains = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ReconnectDomains',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ReconnectDomainsRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ReconnectDomainsResponse.FromString,
                _registered_method=True)
        self.RegisterDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/RegisterDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.RegisterDomainRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.RegisterDomainResponse.FromString,
                _registered_method=True)
        self.ModifyDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ModifyDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ModifyDomainRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ModifyDomainResponse.FromString,
                _registered_method=True)
        self.ConnectDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ConnectDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ConnectDomainRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ConnectDomainResponse.FromString,
                _registered_method=True)
        self.DisconnectDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/DisconnectDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.DisconnectDomainRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.DisconnectDomainResponse.FromString,
                _registered_method=True)
        self.ListConnectedDomains = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConnectedDomains',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConnectedDomainsRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConnectedDomainsResponse.FromString,
                _registered_method=True)
        self.ListConfiguredDomains = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConfiguredDomains',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConfiguredDomainsRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConfiguredDomainsResponse.FromString,
                _registered_method=True)
        self.GetAgreement = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetAgreement',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetAgreementRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetAgreementResponse.FromString,
                _registered_method=True)
        self.AcceptAgreement = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/AcceptAgreement',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.AcceptAgreementRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.AcceptAgreementResponse.FromString,
                _registered_method=True)
        self.GetDomainId = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetDomainId',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetDomainIdRequest.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetDomainIdResponse.FromString,
                _registered_method=True)


class DomainConnectivityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReconnectDomains(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterDomain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyDomain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectDomain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisconnectDomain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListConnectedDomains(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListConfiguredDomains(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgreement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptAgreement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDomainId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DomainConnectivityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReconnectDomains': grpc.unary_unary_rpc_method_handler(
                    servicer.ReconnectDomains,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ReconnectDomainsRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ReconnectDomainsResponse.SerializeToString,
            ),
            'RegisterDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.RegisterDomainRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.RegisterDomainResponse.SerializeToString,
            ),
            'ModifyDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ModifyDomainRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ModifyDomainResponse.SerializeToString,
            ),
            'ConnectDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ConnectDomainRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ConnectDomainResponse.SerializeToString,
            ),
            'DisconnectDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.DisconnectDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.DisconnectDomainRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.DisconnectDomainResponse.SerializeToString,
            ),
            'ListConnectedDomains': grpc.unary_unary_rpc_method_handler(
                    servicer.ListConnectedDomains,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConnectedDomainsRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConnectedDomainsResponse.SerializeToString,
            ),
            'ListConfiguredDomains': grpc.unary_unary_rpc_method_handler(
                    servicer.ListConfiguredDomains,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConfiguredDomainsRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConfiguredDomainsResponse.SerializeToString,
            ),
            'GetAgreement': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgreement,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetAgreementRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetAgreementResponse.SerializeToString,
            ),
            'AcceptAgreement': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptAgreement,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.AcceptAgreementRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.AcceptAgreementResponse.SerializeToString,
            ),
            'GetDomainId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDomainId,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetDomainIdRequest.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetDomainIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.participant.admin.v0.DomainConnectivityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.digitalasset.canton.participant.admin.v0.DomainConnectivityService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DomainConnectivityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReconnectDomains(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ReconnectDomains',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ReconnectDomainsRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ReconnectDomainsResponse.FromString,
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
    def RegisterDomain(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/RegisterDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.RegisterDomainRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.RegisterDomainResponse.FromString,
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
    def ModifyDomain(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ModifyDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ModifyDomainRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ModifyDomainResponse.FromString,
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
    def ConnectDomain(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ConnectDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ConnectDomainRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ConnectDomainResponse.FromString,
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
    def DisconnectDomain(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/DisconnectDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.DisconnectDomainRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.DisconnectDomainResponse.FromString,
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
    def ListConnectedDomains(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConnectedDomains',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConnectedDomainsRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConnectedDomainsResponse.FromString,
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
    def ListConfiguredDomains(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/ListConfiguredDomains',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConfiguredDomainsRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.ListConfiguredDomainsResponse.FromString,
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
    def GetAgreement(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetAgreement',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetAgreementRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetAgreementResponse.FromString,
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
    def AcceptAgreement(request,
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
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/AcceptAgreement',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.AcceptAgreementRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.AcceptAgreementResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/com.digitalasset.canton.participant.admin.v0.DomainConnectivityService/GetDomainId',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetDomainIdRequest.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_domain__connectivity__pb2.GetDomainIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
