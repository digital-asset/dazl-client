# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import inspection_service_pb2 as com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2

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
        + f' but the generated code in com/digitalasset/canton/participant/admin/v0/inspection_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class InspectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LookupContractDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupContractDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Response.FromString,
                _registered_method=True)
        self.LookupTransactionDomain = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupTransactionDomain',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Response.FromString,
                _registered_method=True)
        self.LookupOffsetByTime = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByTime',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Response.FromString,
                _registered_method=True)
        self.LookupOffsetByIndex = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByIndex',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Response.FromString,
                _registered_method=True)
        self.CountInFlight = channel.unary_unary(
                '/com.digitalasset.canton.participant.admin.v0.InspectionService/CountInFlight',
                request_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.CountInFlight.Request.SerializeToString,
                response_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.CountInFlight.Response.FromString,
                _registered_method=True)


class InspectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LookupContractDomain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupTransactionDomain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupOffsetByTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupOffsetByIndex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CountInFlight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InspectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LookupContractDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupContractDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Response.SerializeToString,
            ),
            'LookupTransactionDomain': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupTransactionDomain,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Response.SerializeToString,
            ),
            'LookupOffsetByTime': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupOffsetByTime,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Response.SerializeToString,
            ),
            'LookupOffsetByIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupOffsetByIndex,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Response.SerializeToString,
            ),
            'CountInFlight': grpc.unary_unary_rpc_method_handler(
                    servicer.CountInFlight,
                    request_deserializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.CountInFlight.Request.FromString,
                    response_serializer=com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.CountInFlight.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.digitalasset.canton.participant.admin.v0.InspectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('com.digitalasset.canton.participant.admin.v0.InspectionService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InspectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LookupContractDomain(request,
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
            '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupContractDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupContractDomain.Response.FromString,
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
    def LookupTransactionDomain(request,
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
            '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupTransactionDomain',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupTransactionDomain.Response.FromString,
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
    def LookupOffsetByTime(request,
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
            '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByTime',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByTime.Response.FromString,
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
    def LookupOffsetByIndex(request,
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
            '/com.digitalasset.canton.participant.admin.v0.InspectionService/LookupOffsetByIndex',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.LookupOffsetByIndex.Response.FromString,
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
    def CountInFlight(request,
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
            '/com.digitalasset.canton.participant.admin.v0.InspectionService/CountInFlight',
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.CountInFlight.Request.SerializeToString,
            com_dot_digitalasset_dot_canton_dot_participant_dot_admin_dot_v0_dot_inspection__service__pb2.CountInFlight.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
